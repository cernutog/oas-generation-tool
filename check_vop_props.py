import openpyxl

file_path = "API Templates/$index.xlsm"
sheet_name = "Schemas"

wb = openpyxl.load_workbook(file_path, data_only=True)
ws = wb[sheet_name]

print(f"Checking properties for VopBulkIdentification in {file_path}...")

found = False
for row in ws.iter_rows(values_only=True):
    name = row[0]
    parent = row[1]
    
    if parent == "VopBulkIdentification":
        print(f" - Found property: {name}")
        found = True

if not found:
    print("No properties found for VopBulkIdentification (or parent name doesn't match).")
