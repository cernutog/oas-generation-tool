import pandas as pd
import os

file_path = r"C:\Users\giuse\.gemini\antigravity\scratch\OAS_Generation_Tool\API Templates\$index.xlsm"
op_file_path = r"C:\Users\giuse\.gemini\antigravity\scratch\OAS_Generation_Tool\API Templates\account_assessment.251111.xlsm"
output_file = r"C:\Users\giuse\.gemini\antigravity\scratch\OAS_Generation_Tool\analysis_output.txt"

with open(output_file, "w", encoding="utf-8") as f:
    def log(msg):
        f.write(msg + "\n")
        print(msg)

    def inspect_sheet(name, path, sheet_name):
        log(f"\n--- Analyzing {name} / {sheet_name} ---")
        try:
            df = pd.read_excel(path, sheet_name=sheet_name)
            log(f"Columns: {df.columns.tolist()}")
            log("First 2 rows (transposed if > 5 cols):")
            if len(df.columns) > 5:
                log(df.head(2).T.to_string())
            else:
                log(df.head(2).to_string())
        except Exception as e:
            log(f"Error: {e}")

    # Inspect Master Index
    inspect_sheet("Index", file_path, "General Description")
    inspect_sheet("Index", file_path, "Paths")
    
    # Inspect one operation file to understand Request/Response structure
    if os.path.exists(op_file_path):
        log("\n--- Analyzing Operation File: account_assessment ---")
        # Try to guess sheet names if standard; usually they might be 'Request', 'Response' or similar. 
        # But let's list all sheets first.
        xl = pd.ExcelFile(op_file_path)
        log(f"Sheet names in operation file: {xl.sheet_names}")
        
        # Analyze first sheet assuming it's the main desc, or specific ones if we can guess
        # Based on user prompt: "first column contains name of excel file... contains details of single operation (request, responses, etc)"
        for sheet in xl.sheet_names[:3]: # Inspect first 3 sheets to be safe
            inspect_sheet("Operation", op_file_path, sheet)
            
