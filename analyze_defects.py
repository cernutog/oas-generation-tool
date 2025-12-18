import re

def analyze_defects(filepath):
    # Pattern 1: Column Shifts for "M" (Mandatory)
    # usually "M" is in a specific column. If we see "M" being removed from Col X and added to Col Y for the same key.
    
    # Pattern 2: "Bad Request" -> "fri" / "FpadResponseIdentifier"
    
    # Pattern 3: Missing Schemas (Added Rows in $index)
    
    shifts = []
    fri_fixes = []
    schema_adds = []
    
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            if "Bad Request" in line and ("fri" in line or "FpadResponseIdentifier" in line):
                fri_fixes.append(line.strip())
            
            if "Basic structure for reporting messages" in line: # Description cleanup
                pass
                
            # Detect shifts: Value: 'M' -> '' or '' -> 'M' (or Yes)
            if "Value: 'M' -> ''" in line or "Value: '' -> 'M'" in line or "Value: '' -> 'Yes'" in line:
                shifts.append(line.strip())
                
            if "[$index.xlsm][Schemas] ADDED Row" in line:
                schema_adds.append(line.strip())

    print("--- POTENTIAL COLUMN SHIFTS (Mandatory) ---")
    for s in shifts[:10]: print(s)
    print(f"... and {len(shifts)-10} more.")
    
    print("\n--- FRI / BAD REQUEST FIXES ---")
    for s in fri_fixes: print(s)
    
    print("\n--- MISSING SCHEMAS (Added in Index) ---")
    for s in schema_adds[:10]: print(s)

if __name__ == "__main__":
    analyze_defects("excel_diff_report_smart.txt")
