import pandas as pd
import os

file_path = r"C:\Users\giuse\.gemini\antigravity\scratch\OAS_Generation_Tool\API Templates\$index.xlsm"

def analyze_sheet(sheet_name):
    print(f"\n--- Analyzing Sheet: {sheet_name} ---")
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        print("Columns:", df.columns.tolist())
        print("First 5 rows:")
        print(df.head())
    except Exception as e:
        print(f"Error reading sheet {sheet_name}: {e}")

sheets_to_analyze = [
    "General Description",
    "Paths",
    "Tags",
    "Parameters",
    "Headers",
    "Schemas",
    "Responses"
]

if os.path.exists(file_path):
    for sheet in sheets_to_analyze:
        analyze_sheet(sheet)
else:
    print(f"File not found at: {file_path}")
