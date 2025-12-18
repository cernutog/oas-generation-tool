import re
from collections import defaultdict

def parse_diff_report(filepath):
    # Regex to parse the line structure
    # [filename][sheet] Key='...' Col=... Value: 'old' -> 'new'
    # Pattern might vary if Key contains quotes.
    # Let's simple split by tokens if possible or use regex.
    
    # Example: [$index.xlsm][Responses] Key='content' Col=1 Value: 'text/plain' -> 'application/json'
    
    # We want to group by: File -> Sheet -> Column -> "Old -> New"
    stats = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(int))))
    
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.startswith('['): continue
            
            try:
                # Naive parsing
                parts = line.split('] ')
                meta = parts[0] + ']' # [$index.xlsm][Responses
                
                # Extract File and Sheet
                # [$index.xlsm][Responses]
                m = re.match(r'\[(.*?)\]\[(.*?)\]', meta)
                if not m: continue
                filename = m.group(1)
                sheet = m.group(2)
                
                rest = parts[1] # Key='...' Col=... Value: '...' -> '...'
                
                # Extract Column index (roughly)
                # finding "Col="
                col_part = re.search(r'Col=(\d+)', rest)
                col_idx = col_part.group(1) if col_part else "??"
                
                # Extract Value change
                # Value: 'old' -> 'new'
                val_part = re.split(r'Value: ', rest)[-1].strip()
                
                stats[filename][sheet][col_idx][val_part] += 1
                
            except Exception:
                continue
                
    return stats

def generate_human_report(stats):
    lines = []
    lines.append("# Change Request Summary")
    lines.append("This document summarizes the systematic updates required to align the templates.\n")
    
    for filename in sorted(stats.keys()):
        lines.append(f"## File: `{filename}`")
        
        for sheet in sorted(stats[filename].keys()):
            lines.append(f"### Sheet: **{sheet}**")
            
            # Aggregate by column
            col_changes = stats[filename][sheet]
            
            for col in sorted(col_changes.keys(), key=lambda x: int(x) if x.isdigit() else 999):
                patterns = col_changes[col]
                total = sum(patterns.values())
                
                # Try to map col index to name if possible (hard without context, but we can guess)
                col_name = f"Column {col}"
                
                lines.append(f"- **{col_name}** ({total} changes):")
                
                # List patterns
                # If too many distinct patterns, summarize
                sorted_patterns = sorted(patterns.items(), key=lambda x: x[1], reverse=True)
                
                for pat, count in sorted_patterns[:5]:
                    lines.append(f"    - {pat} (x{count})")
                
                if len(sorted_patterns) > 5:
                    lines.append(f"    - ... and {len(sorted_patterns)-5} other variations.")
            
            lines.append("")
        lines.append("---")
        
    return "\n".join(lines)

if __name__ == "__main__":
    s = parse_diff_report("excel_diff_report_smart.txt")
    report = generate_human_report(s)
    
    with open("change_request_digest.md", "w", encoding="utf-8") as f:
        f.write(report)
    
    print("Report generated: change_request_digest.md")
