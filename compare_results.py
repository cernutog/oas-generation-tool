import yaml
import os
from deepdiff import DeepDiff # Need to install deepdiff or write simple diff

# Simple recursive diff if deepdiff not available
def compare_dicts(d1, d2, path="root"):
    diffs = []
    if isinstance(d1, dict) and isinstance(d2, dict):
        all_keys = set(d1.keys()) | set(d2.keys())
        for k in all_keys:
            if k not in d1:
                diffs.append(f"Missing key in generated: {path}.{k}")
            elif k not in d2:
                # diffs.append(f"Extra key in generated: {path}.{k}") # Maybe ok
                pass
            else:
                diffs.extend(compare_dicts(d1[k], d2[k], f"{path}.{k}"))
    elif isinstance(d1, list) and isinstance(d2, list):
        if len(d1) != len(d2):
            diffs.append(f"List length mismatch at {path}: {len(d1)} vs {len(d2)}")
        else:
            for i in range(len(d1)):
                diffs.extend(compare_dicts(d1[i], d2[i], f"{path}[{i}]"))
    else:
        if d1 != d2:
            diffs.append(f"Value mismatch at {path}: '{d1}' != '{d2}'")
    return diffs

def load_yaml(path):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

base_dir = r"C:\Users\giuse\.gemini\antigravity\scratch\OAS_Generation_Tool"
expected_dir = os.path.join(base_dir, "Expected results")

# 1. Compare 3.0
gen_30 = os.path.join(base_dir, "generated_oas_3.0.yaml")
exp_30_files = [f for f in os.listdir(expected_dir) if "OpenApi3.0" in f]
if exp_30_files:
    exp_30 = os.path.join(expected_dir, exp_30_files[0])
    print(f"\nComparing 3.0: Generated vs {exp_30_files[0]}")
    try:
        d1 = load_yaml(gen_30)
        d2 = load_yaml(exp_30)
        diffs = compare_dicts(d1, d2)
        if diffs:
            print("Found differences:")
            for d in diffs[:20]: print(d)
        else:
            print("No structural differences found!")
    except Exception as e:
        print(f"Error comparing 3.0: {e}")

# 2. Compare 3.1
gen_31 = os.path.join(base_dir, "generated_oas_3.1.yaml")
exp_31_files = [f for f in os.listdir(expected_dir) if "OpenApi3.1" in f]
if exp_31_files:
    exp_31 = os.path.join(expected_dir, exp_31_files[0])
    print(f"\nComparing 3.1: Generated vs {exp_31_files[0]}")
    try:
        d1 = load_yaml(gen_31)
        d2 = load_yaml(exp_31)
        diffs = compare_dicts(d1, d2)
        if diffs:
            print("Found differences:")
            for d in diffs[:20]: print(d)
        else:
            print("No structural differences found!")
    except Exception as e:
        print(f"Error comparing 3.1: {e}")
