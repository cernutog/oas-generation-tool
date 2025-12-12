import pandas as pd

op_file_path = r"C:\Users\giuse\.gemini\antigravity\scratch\OAS_Generation_Tool\API Templates\account_assessment.251111.xlsm"

def inspect_response_sheet(sheet_name):
    print(f"\n--- Analyzing Operation Sheet: {sheet_name} ---")
    try:
        df = pd.read_excel(op_file_path, sheet_name=sheet_name)
        print("Columns:", df.columns.tolist())
        if len(df.columns) > 5:
            print(df.head(5).T.to_string())
        else:
            print(df.head(5).to_string())
    except Exception as e:
        print(f"Error reading sheet {sheet_name}: {e}")

inspect_response_sheet("201")
inspect_response_sheet("400")
inspect_response_sheet("409")
