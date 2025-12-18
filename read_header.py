import pandas as pd
import sys

file_path = "API Templates/$index.xlsm"
try:
    df = pd.read_excel(file_path, sheet_name='Schemas', header=None, nrows=5)
    print("Row 0:", df.iloc[0].tolist())
    print("Row 1:", df.iloc[1].tolist())
    print("Row 2:", df.iloc[2].tolist())
except Exception as e:
    print(e)
