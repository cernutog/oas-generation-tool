import pandas as pd
import os

base_dir = r"C:\Users\giuse\.gemini\antigravity\scratch\OAS_Generation_Tool\API Templates"
file_name = "v1_transactions_investigations_{fuid}.251111.xlsm"
file_path = os.path.join(base_dir, file_name)

def inspect_specific():
    print(f"Loading {file_path}...")
    try:
        df = pd.read_excel(file_path, sheet_name="401")
        print(df.head(10))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    inspect_specific()
