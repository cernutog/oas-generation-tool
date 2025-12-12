import pandas as pd
import os

base_dir = r"C:\Users\giuse\.gemini\antigravity\scratch\OAS_Generation_Tool\API Templates"
file_name = "account_assessment.251111.xlsm"
file_path = os.path.join(base_dir, file_name)

def inspect_op():
    print(f"Loading {file_path}...")
    try:
        xl = pd.ExcelFile(file_path)
        print(f"Sheets: {xl.sheet_names}")
        
        for sheet in ["201", "400", "401", "500"]:
            if sheet in xl.sheet_names:
                print(f"\n--- SHEET {sheet} ---")
                df = pd.read_excel(file_path, sheet_name=sheet)
                print(df.head(5))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    inspect_op()
