import pandas as pd
import os

base_dir = r"C:\Users\giuse\.gemini\antigravity\scratch\OAS_Generation_Tool\API Templates"
file_path = os.path.join(base_dir, "$index.xlsm")

def inspect_schemas():
    try:
        df = pd.read_excel(file_path, sheet_name="Schemas")
        print("\n--- SCHEMA RiskInfoArray ---")
        row = df[df['Name'] == 'RiskInfoArray']
        if not row.empty:
             print(row.iloc[0])
        else:
             print("RiskInfoArray not found")
             
        # Check vopBulkRequest too
        print("\n--- SCHEMA VopBulkRequest ---")
        row = df[df['Name'] == 'VopBulkRequest']
        if not row.empty:
             print(row.iloc[0])
    except Exception as e:
        print(e)

if __name__ == "__main__":
    inspect_schemas()
