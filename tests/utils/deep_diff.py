"""
Deep diff utility for comparing OpenAPI specifications.
Performs recursive structural comparison with detailed diff reporting.
"""

from typing import Any, Union


def deep_diff(
    expected: Any,
    actual: Any,
    path: str = "root",
    ignore_keys: set = None
) -> list[str]:
    """
    Recursively compare two structures (dict, list, or scalar).
    
    Args:
        expected: The expected (golden) value
        actual: The actual (generated) value
        path: Current path in the structure (for reporting)
        ignore_keys: Set of keys to ignore during comparison
        
    Returns:
        List of difference strings describing mismatches
    """
    if ignore_keys is None:
        ignore_keys = set()
    
    differences = []
    
    # Handle None cases
    if expected is None and actual is None:
        return differences
    if expected is None:
        differences.append(f"EXTRA: {path} (expected None, got {type(actual).__name__})")
        return differences
    if actual is None:
        differences.append(f"MISSING: {path} (expected {type(expected).__name__}, got None)")
        return differences
    
    # Type mismatch
    if type(expected) != type(actual):
        # Special case: int vs float (1 == 1.0)
        if isinstance(expected, (int, float)) and isinstance(actual, (int, float)):
            if expected != actual:
                differences.append(f"CHANGED: {path}: {expected!r} → {actual!r}")
        else:
            differences.append(
                f"TYPE_MISMATCH: {path}: expected {type(expected).__name__}, got {type(actual).__name__}"
            )
        return differences
    
    # Dict comparison
    if isinstance(expected, dict):
        # Check for missing keys in actual
        for key in expected:
            if key in ignore_keys:
                continue
            if key not in actual:
                differences.append(f"MISSING: {path}.{key}")
            else:
                differences.extend(
                    deep_diff(expected[key], actual[key], f"{path}.{key}", ignore_keys)
                )
        
        # Check for extra keys in actual
        for key in actual:
            if key in ignore_keys:
                continue
            if key not in expected:
                differences.append(f"EXTRA: {path}.{key}")
        
        return differences
    
    # List comparison
    if isinstance(expected, list):
        if len(expected) != len(actual):
            differences.append(
                f"LENGTH_MISMATCH: {path}: expected {len(expected)} items, got {len(actual)}"
            )
        
        # Compare items up to the shorter length
        for i, (exp_item, act_item) in enumerate(zip(expected, actual)):
            differences.extend(
                deep_diff(exp_item, act_item, f"{path}[{i}]", ignore_keys)
            )
        
        # Report extra items in actual
        if len(actual) > len(expected):
            for i in range(len(expected), len(actual)):
                differences.append(f"EXTRA: {path}[{i}]")
        
        # Report missing items in expected
        if len(expected) > len(actual):
            for i in range(len(actual), len(expected)):
                differences.append(f"MISSING: {path}[{i}]")
        
        return differences
    
    # Scalar comparison
    if expected != actual:
        # Truncate long values for readability
        exp_str = repr(expected)
        act_str = repr(actual)
        if len(exp_str) > 100:
            exp_str = exp_str[:100] + "..."
        if len(act_str) > 100:
            act_str = act_str[:100] + "..."
        differences.append(f"CHANGED: {path}: {exp_str} -> {act_str}")
    
    return differences


def format_diff_report(differences: list[str], max_items: int = 50) -> str:
    """
    Format a list of differences into a human-readable report.
    
    Args:
        differences: List of difference strings
        max_items: Maximum number of items to show
        
    Returns:
        Formatted report string
    """
    if not differences:
        return "[OK] No differences found."
    
    lines = [f"[FAIL] Found {len(differences)} difference(s):\n"]
    
    # Group by type
    missing = [d for d in differences if d.startswith("MISSING:")]
    extra = [d for d in differences if d.startswith("EXTRA:")]
    changed = [d for d in differences if d.startswith("CHANGED:")]
    type_mismatch = [d for d in differences if d.startswith("TYPE_MISMATCH:")]
    length_mismatch = [d for d in differences if d.startswith("LENGTH_MISMATCH:")]
    
    if missing:
        lines.append(f"\n--- MISSING ({len(missing)}) ---")
        for item in missing[:max_items]:
            lines.append(f"  {item}")
        if len(missing) > max_items:
            lines.append(f"  ... and {len(missing) - max_items} more")
    
    if extra:
        lines.append(f"\n--- EXTRA ({len(extra)}) ---")
        for item in extra[:max_items]:
            lines.append(f"  {item}")
        if len(extra) > max_items:
            lines.append(f"  ... and {len(extra) - max_items} more")
    
    if changed:
        lines.append(f"\n--- CHANGED ({len(changed)}) ---")
        for item in changed[:max_items]:
            lines.append(f"  {item}")
        if len(changed) > max_items:
            lines.append(f"  ... and {len(changed) - max_items} more")
    
    if type_mismatch:
        lines.append(f"\n--- TYPE MISMATCH ({len(type_mismatch)}) ---")
        for item in type_mismatch[:max_items]:
            lines.append(f"  {item}")
    
    if length_mismatch:
        lines.append(f"\n--- LENGTH MISMATCH ({len(length_mismatch)}) ---")
        for item in length_mismatch[:max_items]:
            lines.append(f"  {item}")
    
    return "\n".join(lines)


def compare_oas_files(expected_path: str, actual_path: str, ignore_keys: set = None) -> tuple[bool, str]:
    """
    Compare two OAS YAML files.
    
    Args:
        expected_path: Path to expected (golden) file
        actual_path: Path to actual (generated) file
        ignore_keys: Set of keys to ignore
        
    Returns:
        Tuple of (is_equal, report_string)
    """
    import yaml
    
    with open(expected_path, 'r', encoding='utf-8') as f:
        expected = yaml.safe_load(f)
    
    with open(actual_path, 'r', encoding='utf-8') as f:
        actual = yaml.safe_load(f)
    
    differences = deep_diff(expected, actual, "root", ignore_keys or set())
    report = format_diff_report(differences)
    
    return len(differences) == 0, report
