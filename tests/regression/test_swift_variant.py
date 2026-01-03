"""
SWIFT Variant Tests.

SWIFT variants have specific requirements:
- Add: Errors and ErrorMessage schemas
- Add: X-Request-ID headers in all responses
- Add: securitySchemes and global security
- Add: ivUserKey and ivUserBic parameters
- Remove: x-sandbox-* extensions (sandbox is for testing only)
- 400 responses use oneOf schema
"""

import pytest
import yaml


class TestSwiftVariant:
    """
    Test suite for SWIFT variant validation.
    Tests verify that SWIFT has the expected differences from Standard.
    """
    
    def test_swift_has_errors_schemas(self, generate_oas):
        """
        Verify OAS 3.1 SWIFT has Errors and ErrorMessage schemas.
        These are SWIFT-specific requirements.
        """
        output_dir = generate_oas(gen_30=False, gen_31=True, gen_swift=True)
        
        swift_files = list(output_dir.glob("*3.1*SWIFT*.yaml"))
        assert swift_files, "No OAS 3.1 SWIFT file generated"
        
        with open(swift_files[0], 'r', encoding='utf-8') as f:
            oas = yaml.safe_load(f)
        
        schemas = oas.get('components', {}).get('schemas', {})
        
        assert 'Errors' in schemas, "SWIFT should have 'Errors' schema"
        assert 'ErrorMessage' in schemas, "SWIFT should have 'ErrorMessage' schema"
    
    def test_swift_has_security_schemes(self, generate_oas):
        """
        Verify SWIFT has securitySchemes and global security.
        """
        output_dir = generate_oas(gen_30=False, gen_31=True, gen_swift=True)
        
        swift_files = list(output_dir.glob("*3.1*SWIFT*.yaml"))
        
        with open(swift_files[0], 'r', encoding='utf-8') as f:
            oas = yaml.safe_load(f)
        
        # Check for security schemes
        security_schemes = oas.get('components', {}).get('securitySchemes', {})
        assert security_schemes, "SWIFT should have securitySchemes"
        
        # Check for global security
        security = oas.get('security', [])
        assert security, "SWIFT should have global security requirements"
    
    def test_swift_has_x_request_id_header(self, generate_oas):
        """
        Verify SWIFT has X-Request-ID header in components.
        """
        output_dir = generate_oas(gen_30=False, gen_31=True, gen_swift=True)
        
        swift_files = list(output_dir.glob("*3.1*SWIFT*.yaml"))
        
        with open(swift_files[0], 'r', encoding='utf-8') as f:
            oas = yaml.safe_load(f)
        
        headers = oas.get('components', {}).get('headers', {})
        assert 'X-Request-ID' in headers, "SWIFT should have X-Request-ID header component"
    
    def test_swift_has_iv_parameters(self, generate_oas):
        """
        Verify SWIFT has ivUserKey and ivUserBic parameters.
        """
        output_dir = generate_oas(gen_30=False, gen_31=True, gen_swift=True)
        
        swift_files = list(output_dir.glob("*3.1*SWIFT*.yaml"))
        
        with open(swift_files[0], 'r', encoding='utf-8') as f:
            oas = yaml.safe_load(f)
        
        params = oas.get('components', {}).get('parameters', {})
        assert 'ivUserKey' in params, "SWIFT should have ivUserKey parameter"
        assert 'ivUserBic' in params, "SWIFT should have ivUserBic parameter"
    
    def test_swift_no_sandbox_extensions(self, generate_oas):
        """
        Verify SWIFT has NO x-sandbox-* extensions.
        Sandbox extensions are for testing only, not for SWIFT production.
        """
        output_dir = generate_oas(gen_30=False, gen_31=True, gen_swift=True)
        
        swift_files = list(output_dir.glob("*3.1*SWIFT*.yaml"))
        assert swift_files, "No OAS 3.1 SWIFT file generated"
        
        with open(swift_files[0], 'r', encoding='utf-8') as f:
            content = f.read()
        
        sandbox_count = content.count('x-sandbox')
        assert sandbox_count == 0, f"SWIFT should NOT have x-sandbox extensions, found {sandbox_count}"
    
    def test_swift_400_uses_oneof_schema(self, generate_oas):
        """
        Verify SWIFT 400 responses use oneOf schema.
        """
        output_dir = generate_oas(gen_30=False, gen_31=True, gen_swift=True)
        
        swift_files = list(output_dir.glob("*3.1*SWIFT*.yaml"))
        
        with open(swift_files[0], 'r', encoding='utf-8') as f:
            oas = yaml.safe_load(f)
        
        # Check at least one 400 response
        for path, path_obj in oas.get('paths', {}).items():
            for method, op in path_obj.items():
                if method in ['get', 'post', 'put', 'patch', 'delete']:
                    resp_400 = op.get('responses', {}).get('400', {})
                    content = resp_400.get('content', {}).get('application/json', {})
                    schema = content.get('schema', {})
                    if 'oneOf' in schema:
                        # Found at least one - test passes
                        return
        
        pytest.fail("SWIFT 400 responses should use oneOf schema")
    
    def test_swift_preserves_paths(self, generate_oas):
        """
        Verify SWIFT has the same paths as standard version.
        """
        output_dir = generate_oas(gen_30=False, gen_31=True, gen_swift=True)
        
        standard_files = [f for f in output_dir.glob("*3.1*.yaml") if "SWIFT" not in f.name]
        swift_files = list(output_dir.glob("*3.1*SWIFT*.yaml"))
        
        assert standard_files and swift_files, "Both standard and SWIFT should be generated"
        
        with open(standard_files[0], 'r', encoding='utf-8') as f:
            standard = yaml.safe_load(f)
        with open(swift_files[0], 'r', encoding='utf-8') as f:
            swift = yaml.safe_load(f)
        
        standard_paths = set(standard.get('paths', {}).keys())
        swift_paths = set(swift.get('paths', {}).keys())
        
        assert standard_paths == swift_paths, f"SWIFT has different paths:\nMissing: {standard_paths - swift_paths}\nExtra: {swift_paths - standard_paths}"
    
    def test_swift_has_more_schemas_than_standard(self, generate_oas):
        """
        Verify SWIFT has at least as many schemas as standard (plus Errors, ErrorMessage).
        """
        output_dir = generate_oas(gen_30=False, gen_31=True, gen_swift=True)
        
        standard_files = [f for f in output_dir.glob("*3.1*.yaml") if "SWIFT" not in f.name]
        swift_files = list(output_dir.glob("*3.1*SWIFT*.yaml"))
        
        with open(standard_files[0], 'r', encoding='utf-8') as f:
            standard = yaml.safe_load(f)
        with open(swift_files[0], 'r', encoding='utf-8') as f:
            swift = yaml.safe_load(f)
        
        standard_schemas = set(standard.get('components', {}).get('schemas', {}).keys())
        swift_schemas = set(swift.get('components', {}).get('schemas', {}).keys())
        
        # SWIFT should have all standard schemas plus Errors and ErrorMessage
        expected_extra = {'Errors', 'ErrorMessage'}
        missing_from_swift = standard_schemas - swift_schemas
        
        assert not missing_from_swift, f"SWIFT is missing schemas from Standard: {missing_from_swift}"
        assert expected_extra.issubset(swift_schemas), f"SWIFT should have {expected_extra}, but has: {swift_schemas & expected_extra}"
