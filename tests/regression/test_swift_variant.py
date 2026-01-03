"""
SWIFT Variant Tests.

SWIFT variants have specific requirements:
- Keep all examples EXCEPT Bad Request examples
- Remove all x-sandbox-* extensions
- Preserve same structure (paths, schemas)
"""

import pytest
import yaml


class TestSwiftVariant:
    """
    Test suite for SWIFT variant validation.
    """
    
    @pytest.mark.xfail(reason="Known bug: SWIFT generator still includes Bad Request examples")
    def test_swift_31_has_examples_except_bad_request(self, generate_oas):
        """
        Verify OAS 3.1 SWIFT has examples but NOT for Bad Request (400).
        """
        output_dir = generate_oas(gen_30=False, gen_31=True, gen_swift=True)
        
        swift_files = list(output_dir.glob("*3.1*SWIFT*.yaml"))
        assert swift_files, "No OAS 3.1 SWIFT file generated"
        
        with open(swift_files[0], 'r', encoding='utf-8') as f:
            oas = yaml.safe_load(f)
        
        # Check that examples exist in general
        has_examples = False
        bad_request_examples = []
        
        for path, path_obj in oas.get('paths', {}).items():
            for method, op in path_obj.items():
                if method in ['get', 'post', 'put', 'patch', 'delete']:
                    responses = op.get('responses', {})
                    for code, resp in responses.items():
                        content = resp.get('content', {})
                        for media_type, media_obj in content.items():
                            if 'example' in media_obj or 'examples' in media_obj:
                                has_examples = True
                                if code == '400':
                                    bad_request_examples.append(f"{path}.{method}.{code}")
        
        assert has_examples, "SWIFT should have examples (except Bad Request)"
        assert len(bad_request_examples) == 0, f"SWIFT should NOT have Bad Request examples: {bad_request_examples}"
    
    @pytest.mark.xfail(reason="Known bug: SWIFT generator still includes Bad Request examples")
    def test_swift_30_has_examples_except_bad_request(self, generate_oas):
        """
        Verify OAS 3.0 SWIFT has examples but NOT for Bad Request (400).
        """
        output_dir = generate_oas(gen_30=True, gen_31=False, gen_swift=True)
        
        swift_files = list(output_dir.glob("*3.0*SWIFT*.yaml"))
        assert swift_files, "No OAS 3.0 SWIFT file generated"
        
        with open(swift_files[0], 'r', encoding='utf-8') as f:
            oas = yaml.safe_load(f)
        
        has_examples = False
        bad_request_examples = []
        
        for path, path_obj in oas.get('paths', {}).items():
            for method, op in path_obj.items():
                if method in ['get', 'post', 'put', 'patch', 'delete']:
                    responses = op.get('responses', {})
                    for code, resp in responses.items():
                        content = resp.get('content', {})
                        for media_type, media_obj in content.items():
                            if 'example' in media_obj or 'examples' in media_obj:
                                has_examples = True
                                if code == '400':
                                    bad_request_examples.append(f"{path}.{method}.{code}")
        
        assert has_examples, "SWIFT should have examples (except Bad Request)"
        assert len(bad_request_examples) == 0, f"SWIFT should NOT have Bad Request examples: {bad_request_examples}"
    
    def test_swift_no_sandbox_extensions(self, generate_oas):
        """
        Verify SWIFT has NO x-sandbox-* extensions.
        """
        output_dir = generate_oas(gen_30=False, gen_31=True, gen_swift=True)
        
        swift_files = list(output_dir.glob("*3.1*SWIFT*.yaml"))
        assert swift_files, "No OAS 3.1 SWIFT file generated"
        
        with open(swift_files[0], 'r', encoding='utf-8') as f:
            content = f.read()
        
        sandbox_count = content.count('x-sandbox')
        assert sandbox_count == 0, f"SWIFT should NOT have x-sandbox extensions, found {sandbox_count}"
    
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
    
    @pytest.mark.xfail(reason="Known bug: SWIFT has extra schemas (ErrorMessage, Errors)")
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
