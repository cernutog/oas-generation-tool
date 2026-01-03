"""
Full API Regression Tests.

These tests verify that the generated OAS files match the expected golden files
using deep structural comparison.
"""

import pytest
from pathlib import Path


class TestFullAPIRegression:
    """
    Test suite for full API generation regression.
    Compares generated output against golden files with deep equality.
    """
    
    def test_oas31_deep_equality(self, generate_oas, golden_oas31, compare_yaml):
        """
        Generate OAS 3.1 and compare with golden file.
        Verifies: info, paths, components, examples, extensions.
        """
        # Generate fresh OAS 3.1
        output_dir = generate_oas(gen_30=False, gen_31=True, gen_swift=False)
        
        # Find generated file
        generated_files = list(output_dir.glob("*3.1*.yaml"))
        # Exclude SWIFT variants
        generated_files = [f for f in generated_files if "SWIFT" not in f.name]
        
        assert generated_files, "No OAS 3.1 file was generated"
        generated_file = generated_files[0]
        
        # Deep comparison
        is_equal, report = compare_yaml(str(golden_oas31), str(generated_file))
        
        if not is_equal:
            # Save diff to file for debugging
            diff_file = output_dir / "diff_oas31.txt"
            diff_file.write_text(report, encoding='utf-8')
            pytest.fail(f"OAS 3.1 differs from golden file:\n\n{report}\n\nFull diff saved to: {diff_file}")
    
    def test_oas30_deep_equality(self, generate_oas, golden_oas30, compare_yaml):
        """
        Generate OAS 3.0 and compare with golden file.
        Verifies: info, paths, components, examples, extensions.
        """
        # Generate fresh OAS 3.0
        output_dir = generate_oas(gen_30=True, gen_31=False, gen_swift=False)
        
        # Find generated file
        generated_files = list(output_dir.glob("*3.0*.yaml"))
        # Exclude SWIFT variants
        generated_files = [f for f in generated_files if "SWIFT" not in f.name]
        
        assert generated_files, "No OAS 3.0 file was generated"
        generated_file = generated_files[0]
        
        # Deep comparison
        is_equal, report = compare_yaml(str(golden_oas30), str(generated_file))
        
        if not is_equal:
            diff_file = output_dir / "diff_oas30.txt"
            diff_file.write_text(report, encoding='utf-8')
            pytest.fail(f"OAS 3.0 differs from golden file:\n\n{report}\n\nFull diff saved to: {diff_file}")
    
    def test_oas31_swift_deep_equality(self, generate_oas, golden_oas31_swift, compare_yaml):
        """
        Generate OAS 3.1 SWIFT and compare with golden file.
        SWIFT variants have no examples but same structure.
        """
        # Generate fresh OAS 3.1 SWIFT
        output_dir = generate_oas(gen_30=False, gen_31=True, gen_swift=True)
        
        # Find generated SWIFT file
        generated_files = list(output_dir.glob("*3.1*SWIFT*.yaml"))
        
        assert generated_files, "No OAS 3.1 SWIFT file was generated"
        generated_file = generated_files[0]
        
        # Deep comparison
        is_equal, report = compare_yaml(str(golden_oas31_swift), str(generated_file))
        
        if not is_equal:
            diff_file = output_dir / "diff_oas31_swift.txt"
            diff_file.write_text(report, encoding='utf-8')
            pytest.fail(f"OAS 3.1 SWIFT differs from golden file:\n\n{report}\n\nFull diff saved to: {diff_file}")
    
    def test_oas30_swift_deep_equality(self, generate_oas, golden_oas30_swift, compare_yaml):
        """
        Generate OAS 3.0 SWIFT and compare with golden file.
        SWIFT variants have no examples but same structure.
        """
        # Generate fresh OAS 3.0 SWIFT
        output_dir = generate_oas(gen_30=True, gen_31=False, gen_swift=True)
        
        # Find generated SWIFT file
        generated_files = list(output_dir.glob("*3.0*SWIFT*.yaml"))
        
        assert generated_files, "No OAS 3.0 SWIFT file was generated"
        generated_file = generated_files[0]
        
        # Deep comparison
        is_equal, report = compare_yaml(str(golden_oas30_swift), str(generated_file))
        
        if not is_equal:
            diff_file = output_dir / "diff_oas30_swift.txt"
            diff_file.write_text(report, encoding='utf-8')
            pytest.fail(f"OAS 3.0 SWIFT differs from golden file:\n\n{report}\n\nFull diff saved to: {diff_file}")


class TestVersionParity:
    """
    Test that OAS 3.0 and 3.1 have structural parity.
    They should have the same paths, schemas, and operations.
    """
    
    def test_same_paths(self, generate_oas):
        """Verify 3.0 and 3.1 have the same paths."""
        import yaml
        
        output_dir = generate_oas(gen_30=True, gen_31=True, gen_swift=False)
        
        # Load both files
        oas30_files = [f for f in output_dir.glob("*3.0*.yaml") if "SWIFT" not in f.name]
        oas31_files = [f for f in output_dir.glob("*3.1*.yaml") if "SWIFT" not in f.name]
        
        assert oas30_files and oas31_files, "Both OAS versions should be generated"
        
        with open(oas30_files[0], 'r', encoding='utf-8') as f:
            oas30 = yaml.safe_load(f)
        with open(oas31_files[0], 'r', encoding='utf-8') as f:
            oas31 = yaml.safe_load(f)
        
        paths_30 = set(oas30.get('paths', {}).keys())
        paths_31 = set(oas31.get('paths', {}).keys())
        
        assert paths_30 == paths_31, f"Path mismatch:\nOnly in 3.0: {paths_30 - paths_31}\nOnly in 3.1: {paths_31 - paths_30}"
    
    def test_same_schemas(self, generate_oas):
        """Verify 3.0 and 3.1 have the same schema names."""
        import yaml
        
        output_dir = generate_oas(gen_30=True, gen_31=True, gen_swift=False)
        
        oas30_files = [f for f in output_dir.glob("*3.0*.yaml") if "SWIFT" not in f.name]
        oas31_files = [f for f in output_dir.glob("*3.1*.yaml") if "SWIFT" not in f.name]
        
        with open(oas30_files[0], 'r', encoding='utf-8') as f:
            oas30 = yaml.safe_load(f)
        with open(oas31_files[0], 'r', encoding='utf-8') as f:
            oas31 = yaml.safe_load(f)
        
        schemas_30 = set(oas30.get('components', {}).get('schemas', {}).keys())
        schemas_31 = set(oas31.get('components', {}).get('schemas', {}).keys())
        
        assert schemas_30 == schemas_31, f"Schema mismatch:\nOnly in 3.0: {schemas_30 - schemas_31}\nOnly in 3.1: {schemas_31 - schemas_30}"
