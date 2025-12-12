import pandas as pd

op_file_path = r"C:\Users\giuse\.gemini\antigravity\scratch\OAS_Generation_Tool\API Templates\account_assessment.251111.xlsm"

def check_headers_in_sheet(sheet_name):
    try:
        df = pd.read_excel(op_file_path, sheet_name=sheet_name)
        # Check if 'Type' column exists
        type_col = None
        for col in df.columns:
            if "Type" in col and "Items" not in col:
                type_col = col
                break
        
        if type_col:
            headers = df[df[type_col].astype(str).str.lower() == 'header']
            if not headers.empty:
                print(f"Found headers in {sheet_name}:")
                print(headers.to_string())
            else:
                print(f"No headers found in {sheet_name}")
        else:
             print(f"No Type column in {sheet_name}")

    except Exception as e:
        print(f"Error reading {sheet_name}: {e}")

check_headers_in_sheet("201")
check_headers_in_sheet("400")
check_headers_in_sheet("409")
