import re
from collections import defaultdict

def generate_remediation(filepath):
    # Data structure: File -> Sheet -> Column -> ChangePattern -> Count
    data = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(int))))
    
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.startswith('['): continue
            try:
                # Parse: [File][Sheet] Key='...' Col=... Value: 'Old' -> 'New'
                # Log format: [$index.xlsm][Responses] Key='content' Col=2 Value: 'ErrorResponse_401' -> 'ErrorResponse_403'
                
                parts = line.split('] ')
                meta = parts[0] + ']' 
                m = re.match(r'\[(.*?)\]\[(.*?)\]', meta)
                if not m: continue
                filename, sheet = m.group(1), m.group(2)
                
                rest = parts[1]
                val_part = re.split(r'Value: ', rest)[-1].strip()
                
                # Extract Col Index using regex
                col_m = re.search(r'Col=(\d+)', rest)
                col = col_m.group(1) if col_m else "Unknown"
                
                # Filter noise?
                # Timestamp diffs: '2024-...' -> '2024-...'
                if re.match(r"'20\d\d-.*?' -> '20\d\d-.*?'", val_part):
                     val_part = "Timestamp update (Standardized)"
                
                data[filename][sheet][col][val_part] += 1
                
            except: continue

    # Output
    lines = []
    lines.append("# Full Remediation Log")
    lines.append("Complete list of differences detected between Original and Current templates.\n")
    
    for filename in sorted(data.keys()):
        lines.append(f"## {filename}")
        for sheet in sorted(data[filename].keys()):
            lines.append(f"### Sheet: {sheet}")
            
            changes_in_sheet = data[filename][sheet]
            
            # Group by Column to identify shifts
            for col in sorted(changes_in_sheet.keys(), key=lambda x: int(x) if x.isdigit() else 999):
                patterns = changes_in_sheet[col]
                total = sum(patterns.values())
                lines.append(f"- **Column {col}** ({total} edits):")
                
                for pattern, count in sorted(patterns.items(), key=lambda x: x[1], reverse=True):
                    lines.append(f"  - {pattern} **(x{count} rows)**")
            lines.append("")
    
    return "\n".join(lines)

if __name__ == "__main__":
    report = generate_remediation("excel_diff_report_smart.txt")
    with open("full_remediation_log.md", "w", encoding="utf-8") as f:
        f.write(report)
    print("Log generated.")
