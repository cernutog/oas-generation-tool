"""
SWIFT Variant Tests.

These tests verify SWIFT-specific behavior:
- No example fields present
- Same structure as standard version (minus examples)
"""

import pytest
import yaml


class TestSwiftVariant:
    """
    Test suite for SWIFT variant validation.
    """
    
    @pytest.mark.xfail(reason="Known issue: SWIFT generator doesn't fully strip examples yet")
    def test_swift_31_no_examples(self, generate_oas):
        """
        Verify OAS 3.1 SWIFT has no 'example' or 'examples' fields.
        """
        output_dir = generate_oas(gen_30=False, gen_31=True, gen_swift=True)
        
        swift_files = list(output_dir.glob("*3.1*SWIFT*.yaml"))
        assert swift_files, "No OAS 3.1 SWIFT file generated"
        
        with open(swift_files[0], 'r', encoding='utf-8') as f:
            content = f.read()
            oas = yaml.safe_load(content)
        
        # Check for 'example:' or 'examples:' in the raw content
        example_count = content.count('example:')
        examples_count = content.count('examples:')
        
        assert example_count == 0, f"Found {example_count} 'example:' fields in SWIFT output"
        assert examples_count == 0, f"Found {examples_count} 'examples:' fields in SWIFT output"
    
    @pytest.mark.xfail(reason="Known issue: SWIFT generator doesn't fully strip examples yet")
    def test_swift_30_no_examples(self, generate_oas):
        """
        Verify OAS 3.0 SWIFT has no 'example' or 'examples' fields.
        """
        output_dir = generate_oas(gen_30=True, gen_31=False, gen_swift=True)
        
        swift_files = list(output_dir.glob("*3.0*SWIFT*.yaml"))
        assert swift_files, "No OAS 3.0 SWIFT file generated"
        
        with open(swift_files[0], 'r', encoding='utf-8') as f:
            content = f.read()
        
        example_count = content.count('example:')
        examples_count = content.count('examples:')
        
        assert example_count == 0, f"Found {example_count} 'example:' fields in SWIFT output"
        assert examples_count == 0, f"Found {examples_count} 'examples:' fields in SWIFT output"
    
    def test_swift_preserves_paths(self, generate_oas):
        """
        Verify SWIFT has the same paths as standard version.
        """
        # Generate both standard and SWIFT
        output_dir = generate_oas(gen_30=False, gen_31=True, gen_swift=True)
        
        standard_files = [f for f in output_dir.glob("*3.1*.yaml") if "SWIFT" not in f.name]
        swift_files = list(output_dir.glob("*3.1*SWIFT*.yaml"))
        
        assert standard_files and swift_files, "Both standard and SWIFT should be generated"
        
        with open(standard_files[0], 'r', encoding='utf-8') as f:
            standard = yaml.safe_load(f)
        with open(swift_files[0], 'r', encoding='utf-8') as f:
            swift = yaml.safe_load(f)
        
        standard_paths = set(standard.get('paths', {}).keys())
        swift_paths = set(swift.get('paths', {}).keys())
        
        assert standard_paths == swift_paths, f"SWIFT has different paths:\nMissing: {standard_paths - swift_paths}\nExtra: {swift_paths - standard_paths}"
    
    @pytest.mark.xfail(reason="Known issue: SWIFT has extra schemas (ErrorMessage, Errors)")
    def test_swift_preserves_schemas(self, generate_oas):
        """
        Verify SWIFT has the same schemas as standard version.
        """
        output_dir = generate_oas(gen_30=False, gen_31=True, gen_swift=True)
        
        standard_files = [f for f in output_dir.glob("*3.1*.yaml") if "SWIFT" not in f.name]
        swift_files = list(output_dir.glob("*3.1*SWIFT*.yaml"))
        
        with open(standard_files[0], 'r', encoding='utf-8') as f:
            standard = yaml.safe_load(f)
        with open(swift_files[0], 'r', encoding='utf-8') as f:
            swift = yaml.safe_load(f)
        
        standard_schemas = set(standard.get('components', {}).get('schemas', {}).keys())
        swift_schemas = set(swift.get('components', {}).get('schemas', {}).keys())
        
        assert standard_schemas == swift_schemas, f"SWIFT has different schemas:\nMissing: {standard_schemas - swift_schemas}\nExtra: {swift_schemas - standard_schemas}"
    
    @pytest.mark.xfail(reason="Known issue: SWIFT strips x-sandbox extensions")
    def test_swift_preserves_extensions(self, generate_oas):
        """
        Verify SWIFT preserves custom extensions (x-*).
        """
        output_dir = generate_oas(gen_30=False, gen_31=True, gen_swift=True)
        
        standard_files = [f for f in output_dir.glob("*3.1*.yaml") if "SWIFT" not in f.name]
        swift_files = list(output_dir.glob("*3.1*SWIFT*.yaml"))
        
        with open(standard_files[0], 'r', encoding='utf-8') as f:
            standard_content = f.read()
        with open(swift_files[0], 'r', encoding='utf-8') as f:
            swift_content = f.read()
        
        # Count x-sandbox extensions in both
        standard_ext_count = standard_content.count('x-sandbox')
        swift_ext_count = swift_content.count('x-sandbox')
        
        assert swift_ext_count == standard_ext_count, f"Extension count mismatch: Standard={standard_ext_count}, SWIFT={swift_ext_count}"
