"""
Section-Specific Tests.

These tests verify individual sections of the OAS spec
to provide more granular failure reporting.
"""

import pytest
import yaml
from tests.utils.deep_diff import deep_diff, format_diff_report


class TestInfoSection:
    """Tests for the 'info' section."""
    
    def test_info_attributes(self, generate_oas, golden_oas31):
        """Verify all info attributes match."""
        output_dir = generate_oas(gen_30=False, gen_31=True, gen_swift=False)
        
        generated_files = [f for f in output_dir.glob("*3.1*.yaml") if "SWIFT" not in f.name]
        
        with open(golden_oas31, 'r', encoding='utf-8') as f:
            expected = yaml.safe_load(f)
        with open(generated_files[0], 'r', encoding='utf-8') as f:
            actual = yaml.safe_load(f)
        
        diffs = deep_diff(expected.get('info', {}), actual.get('info', {}), "info")
        
        if diffs:
            pytest.fail(f"Info section mismatch:\n{format_diff_report(diffs)}")


class TestComponentsSection:
    """Tests for the 'components' section."""
    
    def test_all_schemas_present(self, generate_oas, golden_oas31):
        """Verify all schemas are present."""
        output_dir = generate_oas(gen_30=False, gen_31=True, gen_swift=False)
        
        generated_files = [f for f in output_dir.glob("*3.1*.yaml") if "SWIFT" not in f.name]
        
        with open(golden_oas31, 'r', encoding='utf-8') as f:
            expected = yaml.safe_load(f)
        with open(generated_files[0], 'r', encoding='utf-8') as f:
            actual = yaml.safe_load(f)
        
        expected_schemas = set(expected.get('components', {}).get('schemas', {}).keys())
        actual_schemas = set(actual.get('components', {}).get('schemas', {}).keys())
        
        missing = expected_schemas - actual_schemas
        extra = actual_schemas - expected_schemas
        
        assert not missing, f"Missing schemas: {missing}"
        assert not extra, f"Extra schemas: {extra}"
    
    def test_schemas_deep_equality(self, generate_oas, golden_oas31):
        """Verify all schema attributes match."""
        output_dir = generate_oas(gen_30=False, gen_31=True, gen_swift=False)
        
        generated_files = [f for f in output_dir.glob("*3.1*.yaml") if "SWIFT" not in f.name]
        
        with open(golden_oas31, 'r', encoding='utf-8') as f:
            expected = yaml.safe_load(f)
        with open(generated_files[0], 'r', encoding='utf-8') as f:
            actual = yaml.safe_load(f)
        
        expected_schemas = expected.get('components', {}).get('schemas', {})
        actual_schemas = actual.get('components', {}).get('schemas', {})
        
        diffs = deep_diff(expected_schemas, actual_schemas, "components.schemas")
        
        if diffs:
            pytest.fail(f"Schema mismatch:\n{format_diff_report(diffs)}")
    
    def test_all_parameters_present(self, generate_oas, golden_oas31):
        """Verify all reusable parameters are present."""
        output_dir = generate_oas(gen_30=False, gen_31=True, gen_swift=False)
        
        generated_files = [f for f in output_dir.glob("*3.1*.yaml") if "SWIFT" not in f.name]
        
        with open(golden_oas31, 'r', encoding='utf-8') as f:
            expected = yaml.safe_load(f)
        with open(generated_files[0], 'r', encoding='utf-8') as f:
            actual = yaml.safe_load(f)
        
        expected_params = set(expected.get('components', {}).get('parameters', {}).keys())
        actual_params = set(actual.get('components', {}).get('parameters', {}).keys())
        
        missing = expected_params - actual_params
        extra = actual_params - expected_params
        
        if missing or extra:
            pytest.fail(f"Parameter mismatch:\nMissing: {missing}\nExtra: {extra}")
    
    def test_all_responses_present(self, generate_oas, golden_oas31):
        """Verify all reusable responses are present."""
        output_dir = generate_oas(gen_30=False, gen_31=True, gen_swift=False)
        
        generated_files = [f for f in output_dir.glob("*3.1*.yaml") if "SWIFT" not in f.name]
        
        with open(golden_oas31, 'r', encoding='utf-8') as f:
            expected = yaml.safe_load(f)
        with open(generated_files[0], 'r', encoding='utf-8') as f:
            actual = yaml.safe_load(f)
        
        expected_responses = set(expected.get('components', {}).get('responses', {}).keys())
        actual_responses = set(actual.get('components', {}).get('responses', {}).keys())
        
        missing = expected_responses - actual_responses
        extra = actual_responses - expected_responses
        
        if missing or extra:
            pytest.fail(f"Response mismatch:\nMissing: {missing}\nExtra: {extra}")


class TestPathsSection:
    """Tests for the 'paths' section."""
    
    def test_paths_deep_equality(self, generate_oas, golden_oas31):
        """Verify all paths and operations match."""
        output_dir = generate_oas(gen_30=False, gen_31=True, gen_swift=False)
        
        generated_files = [f for f in output_dir.glob("*3.1*.yaml") if "SWIFT" not in f.name]
        
        with open(golden_oas31, 'r', encoding='utf-8') as f:
            expected = yaml.safe_load(f)
        with open(generated_files[0], 'r', encoding='utf-8') as f:
            actual = yaml.safe_load(f)
        
        diffs = deep_diff(expected.get('paths', {}), actual.get('paths', {}), "paths")
        
        if diffs:
            # Limit output for readability
            report = format_diff_report(diffs, max_items=20)
            pytest.fail(f"Paths mismatch:\n{report}")


class TestExtensions:
    """Tests for custom extensions (x-*)."""
    
    def test_extensions_present(self, generate_oas, golden_oas31):
        """Verify custom extensions are preserved."""
        output_dir = generate_oas(gen_30=False, gen_31=True, gen_swift=False)
        
        generated_files = [f for f in output_dir.glob("*3.1*.yaml") if "SWIFT" not in f.name]
        
        with open(golden_oas31, 'r', encoding='utf-8') as f:
            expected_content = f.read()
        with open(generated_files[0], 'r', encoding='utf-8') as f:
            actual_content = f.read()
        
        # Count x-sandbox extensions
        expected_count = expected_content.count('x-sandbox')
        actual_count = actual_content.count('x-sandbox')
        
        assert actual_count == expected_count, f"Extension count mismatch: expected {expected_count}, got {actual_count}"
