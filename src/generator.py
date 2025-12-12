import yaml
import pandas as pd
import json

class OASGenerator:
    def __init__(self, version="3.0.0"):
        self.version = version
        self.oas = {
            "openapi": version,
            "info": {},
            "paths": {},
            "components": {
                "schemas": {},
                "parameters": {},
                "headers": {},
                "responses": {},
                "securitySchemes": {}
            }
        }

    def build_info(self, info_data):
        self.oas["info"] = info_data

    def build_paths(self, paths_list, operations_details):
        for op_meta in paths_list:
            path_url = op_meta.get("path")
            method = op_meta.get("method", "").lower()
            file_ref = op_meta.get("file")
            
            if not path_url or not method:
                continue
                
            if path_url not in self.oas["paths"]:
                self.oas["paths"][path_url] = {}
            
            op_obj = {
                "summary": op_meta.get("summary"),
                "description": op_meta.get("description"),
                "operationId": op_meta.get("operationId"),
                "tags": [op_meta.get("tags")] if op_meta.get("tags") else [],
                "parameters": [],
                "responses": {}
            }

            # Merge Custom Extensions (YAML format)
            extensions_yaml = op_meta.get("extensions")
            if extensions_yaml and isinstance(extensions_yaml, str) and extensions_yaml.strip():
                try:
                    # Clean up YAML: sometimes indentation is messed up in Excel cells
                    # Simple heuristic: remove leading whitespace from first line, 
                    # and adjust subsequent lines? Or just trust safe_load
                    
                    # Problem seen: "x-sandbox-rule-type: ...\n      x-sandbox-rule-content: |"
                    # The second line has 6 spaces, first has 0. This is valid YAML if it's top level?
                    # No, top level map keys must be same indent.
                    
                    # Normalize indentation
                    lines = extensions_yaml.split('\n')
                    if lines:
                        # Strip common leading whitespace?
                        # Or just replace the weird large spacing on line 2+
                        pass

                    ext_dict = yaml.safe_load(extensions_yaml)
                    if isinstance(ext_dict, dict):
                        op_obj.update(ext_dict)
                except Exception as e:
                    print(f"Error parsing custom extensions for {op_meta.get('operationId')}: {e}")

            # Populate details from Operation File
            if file_ref in operations_details:
                details = operations_details[file_ref]
                
                # Parameters
                if details.get("parameters") is not None:
                    op_obj["parameters"] = self._build_parameters(details["parameters"])

                # Request Body
                if details.get("body") is not None:
                    req_body = self._build_request_body(details["body"])
                    if req_body:
                        op_obj["requestBody"] = req_body

                # Responses
                if details.get("responses"):
                    for code, df_resp in details["responses"].items():
                        op_obj["responses"][str(code)] = self._build_single_response(df_resp)
            
            # Fallback for empty responses
            if not op_obj["responses"]:
                op_obj["responses"]["default"] = {"description": "Default response"}

            self.oas["paths"][path_url][method] = op_obj

    def _build_parameters(self, df):
        params = []
        if df is None: return params
        
        for _, row in df.iterrows():
            name = row.get("Name") or row.get("Request Parameters")
            if pd.isna(name): continue
            
            in_loc = row.get("In")
            if pd.isna(in_loc): 
                 # Try to infer or default? Usually 'query' or 'header'
                 continue 
            
            param = {
                "name": name,
                "in": str(in_loc).lower(),
                "description": row.get("Description", ""),
                "required": str(row.get("Mandatory", "")).lower() == "yes",
                "schema": self._map_type_to_schema(row)
            }
            params.append(param)
        return params

    def _build_request_body(self, df):
        if df is None or df.empty: return None
        
        # The structure usually has the content-type as a root or row 0
        # Let's find the content type. 
        # Heuristic: verify if 'application/json' is in Name column
        content_type = "application/json" # Default
        
        # We process the rows to build the schema
        # We need to filter out meta-rows if they exist
        
        schema = self._build_schema_from_flat_table(df)
        
        return {
            "content": {
                content_type: {
                    "schema": schema
                }
            }
        }

    def _build_single_response(self, df):
        if df is None or df.empty: return {"description": "Response"}
        
        # 1. Identify Root Info
        root_row = None
        header_rows = []
        schema_rows_mask = []
        
        for idx, row in df.iterrows():
             r_type = str(row.get("Type")).strip().lower()
             if r_type == 'header':
                 header_rows.append(row)
                 schema_rows_mask.append(False)
             else:
                 schema_rows_mask.append(True)
                 if pd.isna(row.get("Parent")) and root_row is None:
                     root_row = row

        if root_row is None: 
             # Fallback
             return {"description": "Response"}

        desc = root_row.get("Name") or root_row.get("Description") or "Response"
        type_val = str(root_row.get("Type")).strip().lower()
        schema_ref = root_row.get("Schema Name\n(for Type or Items Data Type = 'schema'||'header')") or root_row.get("Schema Name")

        # 2. Global Response Reference (Type == 'response')
        if type_val == 'response' and pd.notna(schema_ref):
             return {"$ref": f"#/components/responses/{schema_ref}"}

        # 3. Inline Response
        resp_obj = {"description": str(desc)}
        
        # Build Schema (filtering out header rows)
        df_schema = df[schema_rows_mask].copy()
        if not df_schema.empty:
            schema = self._build_schema_from_flat_table(df_schema)
            # If the root is 'Type: object' but mostly empty, schema might be empty dict.
            # If Content-Type is implied?
            # Default to application/json
            resp_obj["content"] = {
                "application/json": {
                    "schema": schema
                }
            }
        
        # 4. Headers
        if header_rows:
            headers = {}
            for row in header_rows:
                 h_name = row.get("Name")
                 if pd.notna(h_name):
                      # Headers: description + schema
                      h_schema = self._map_type_to_schema(row)
                      # Extract description from schema as sibling for Header Object
                      h_desc = h_schema.pop("description", None)
                      
                      head_obj = {"schema": h_schema}
                      if h_desc: head_obj["description"] = h_desc
                      # If referencing a global header?
                      h_ref = row.get("Schema Name\n(for Type or Items Data Type = 'schema'||'header')") or row.get("Schema Name")
                      # If Type is 'header' and has Schema Name, maybe it's a ref to component/headers?
                      # But usually Type is 'string' etc.
                      # If Type is 'header', the Row says "This is a header". 
                      # The data type of the header is usually separate?
                      # Assuming standard row mapping works.
                      
                      headers[h_name] = head_obj
            resp_obj["headers"] = headers

        return resp_obj

    def _build_schema_from_flat_table(self, df):
        """
        Reconstructs a nested schema from flat parent/child rows.
        """
        # 1. Index rows by Name for parent lookup
        df.columns = df.columns.str.strip()
        
        nodes = {}
        roots = []
        
        for idx, row in df.iterrows():
            name = row.get("Name")
            if pd.isna(name): continue
            name = str(name).strip()
            
            # Skip rows that look like content-types or section headers if they don't have schema info
            if name == "application/json" and pd.isna(row.get("Parent")):
                continue
            
            # Check for Mandatory at this level to be used by parent later?
            # actually we can check it when processing children.
            
            node = {
                "name": name,
                "type": row.get("Type"),
                "description": row.get("Description"),
                "parent": row.get("Parent"),
                "mandatory": str(row.get("Mandatory", "")).lower() in ["yes", "y", "true"],
                "schema_obj": self._map_type_to_schema(row, is_node=True)
            }
            
            nodes[name] = node
        
        # 2. Build Tree
        for name, node in nodes.items():
            parent_name = node["parent"]
            if pd.isna(parent_name):
                roots.append(node)
            else:
                parent_name = str(parent_name).strip()
                if parent_name in nodes:
                    parent = nodes[parent_name]
                    parent_schema = parent["schema_obj"]
                    
                    if parent_schema.get("type") == "array":
                        parent_schema["items"] = node["schema_obj"]
                    else:
                        if "properties" not in parent_schema:
                            parent_schema["properties"] = {}
                        parent_schema["properties"][name] = node["schema_obj"]
                        
                        # Handle Required
                        if node["mandatory"]:
                            if "required" not in parent_schema:
                                parent_schema["required"] = []
                            if name not in parent_schema["required"]:
                                parent_schema["required"].append(name)
                        
        # 3. Return the Root Schema
        if len(roots) == 1:
            return roots[0]["schema_obj"]
        elif len(roots) > 1:
            return {
                "type": "object",
                "properties": {r["name"]: r["schema_obj"] for r in roots}
            }
        else:
            return {}

    def _map_type_to_schema(self, row, is_node=False):
        """
        Maps Excel row data to an OAS schema object.
        """
        type_val = row.get("Type")
        if pd.isna(type_val): type_val = "string"
        type_val = str(type_val).lower()
        
        schema = {}
        
        # Check if it's a ref
        schema_ref = row.get("Schema Name\n(for Type or Items Data Type = 'schema'||'header')") or row.get("Schema Name")
        desc = row.get("Description")
        
        if pd.notna(schema_ref):
            ref_path = f"#/components/schemas/{schema_ref}"
            
            if type_val == "array":
                schema["type"] = "array"
                schema["items"] = {"$ref": ref_path}
            else:
                # OAS 3.0 Workaround check
                has_desc = pd.notna(desc)
                is_oas30 = self.version.startswith("3.0")
                
                if is_oas30 and has_desc:
                    schema = {
                        "allOf": [ {"$ref": ref_path} ],
                        "description": str(desc)
                    }
                    return schema 
                else:
                    schema["$ref"] = ref_path
        
        if type_val != "array" and "$ref" not in schema and "allOf" not in schema:
            schema["type"] = type_val
        
        # Add Description 
        if pd.notna(desc) and "description" not in schema: 
            schema["description"] = str(desc)

        ex = row.get("Example")
        if pd.notna(ex): schema["example"] = ex
        
        # Enums
        enum_val = row.get("Allowed value") or row.get("Allowed values")
        if pd.notna(enum_val):
            schema["enum"] = [x.strip() for x in str(enum_val).split(',')]

        # Formatting / Constraints
        fmt = row.get("Format")
        if pd.notna(fmt): schema["format"] = str(fmt)
        
        pattern = row.get("PatternEba")
        if pd.notna(pattern): schema["pattern"] = str(pattern)
        
        regex = row.get("Regex")  # Override PatternEba if present? Or allow both?
        if pd.notna(regex): schema["pattern"] = str(regex)

        min_val = row.get("Min\nValue/Length/Item") or row.get("Min Value/Length/Item") or row.get("Min")
        max_val = row.get("Max\nValue/Length/Item") or row.get("Max Value/Length/Item") or row.get("Max")
        
        if pd.notna(min_val):
            # Infer if it's minLength, minimum, or minItems property based on type
            try:
                val = int(min_val) if float(min_val).is_integer() else float(min_val)
                if type_val == "string": schema["minLength"] = int(val)
                elif type_val in ["integer", "number"]: schema["minimum"] = val
                elif type_val == "array": schema["minItems"] = int(val)
            except: pass

        if pd.notna(max_val):
            try:
                val = int(max_val) if float(max_val).is_integer() else float(max_val)
                if type_val == "string": schema["maxLength"] = int(val)
                elif type_val in ["integer", "number"]: schema["maximum"] = val
                elif type_val == "array": schema["maxItems"] = int(val)
            except: pass

        if type_val == "array":
            # If explicit item type is given
            item_type = row.get("Items Data Type\n(Array only)") or row.get("Items Data Type")
            if pd.notna(item_type):
                 schema["items"] = {"type": str(item_type).lower()}
            elif "items" not in schema:
                 schema["items"] = {} 

        return schema

    def build_components(self, global_components):
        """
        Populates self.oas["components"]
        """
        if not global_components: return

        # Schemas
        if global_components.get("schemas") is not None:
             schema_tree = self._build_schema_group(global_components["schemas"])
             self.oas["components"]["schemas"] = schema_tree
        
        # Parameters (Global)
        if global_components.get("parameters") is not None:
            params = self._build_parameters(global_components["parameters"])
            for p in params:
                self.oas["components"]["parameters"][p["name"]] = p

        # Responses (Global)
        if global_components.get("responses") is not None:
             # Global responses are slightly different? Usually definitions.
             # Need to see structure. Assuming similar flat table.
             # If "Name" column gives the component name.
             pass # Logic to be refined if needed, using generic builder
             
    def _build_schema_group(self, df):
        """
        Builds a dictionary of schema components from a single flat sheet containing multiple schemas.
        """
        nodes = {}
        roots = []
        df.columns = df.columns.str.strip()
        
        for idx, row in df.iterrows():
            name = row.get("Name")
            if pd.isna(name): continue
            name = str(name).strip()
            
            node = {
                "name": name,
                "type": row.get("Type"),
                "description": row.get("Description"),
                "parent": row.get("Parent"),
                "item_type": row.get("Items Data Type\n(Array only)") or row.get("Items Data Type"),
                "schema_ref": row.get("Schema Name\n(for Type or Items Data Type = 'schema'||'header')") or row.get("Schema Name"),
                "example": row.get("Example"),
                "enum": row.get("Allowed value"),
                "properties": {},
                "items": None,
                "schema_obj": self._map_type_to_schema(row, is_node=True)
            }
            nodes[name] = node

        # 2. Link
        for name, node in nodes.items():
            parent_name = node["parent"]
            if pd.isna(parent_name):
                roots.append(node)
            elif str(parent_name).strip() in nodes:
                parent = nodes[str(parent_name).strip()]
                parent_schema = parent["schema_obj"]
                
                if parent_schema.get("type") == "array":
                    parent_schema["items"] = node["schema_obj"]
                else:
                    if "properties" not in parent_schema: parent_schema["properties"] = {}
                    
                    # Special check: If we are adding a property that has an allOf wrapper (for 3.0 ref workadound)
                    # We add it as is.
                    parent_schema["properties"][name] = node["schema_obj"]

        # 3. Return map of Root Name -> Schema
        return {r["name"]: r["schema_obj"] for r in roots}

    def get_yaml(self):
        return yaml.dump(self.oas, sort_keys=False, allow_unicode=True)
