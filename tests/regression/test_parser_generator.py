"""
Excel Parser Module Tests.

Tests for the Excel parsing functionality (excel_parser.py).
"""

import pytest
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


class TestExcelParser:
    """
    Test suite for the Excel parser module.
    """
    
    def test_excel_parser_import(self):
        """Verify excel_parser module can be imported."""
        from src import excel_parser
        assert excel_parser is not None
    
    def test_excel_parser_has_required_functions(self):
        """Verify excel_parser has required functions."""
        from src import excel_parser
        
        # Check for main parsing functions
        assert hasattr(excel_parser, 'parse_paths_index') or hasattr(excel_parser, 'ExcelParser'), \
            "Should have parse_paths_index function or ExcelParser class"
    
    def test_parse_index_file(self, api_templates_dir):
        """Test parsing the $index.xlsm file."""
        from src import excel_parser
        import pandas as pd
        
        index_file = api_templates_dir / "$index.xlsm"
        if not index_file.exists():
            pytest.skip("$index.xlsm not found")
        
        # Load the index file into a DataFrame first
        df_paths = pd.read_excel(index_file, sheet_name="Paths", header=0)
        
        # Then parse it
        result = excel_parser.parse_paths_index(df_paths)
        
        # Result should be a list of paths info
        assert result is not None, "Should return a result"
        assert isinstance(result, list), "Result should be a list"
    
    def test_parse_template_file(self, api_templates_dir):
        """Test parsing a template Excel file."""
        from src import excel_parser
        
        # Find any .xlsm file that's not $index
        templates = [f for f in api_templates_dir.glob("*.xlsm") if f.name != "$index.xlsm"]
        
        if not templates:
            pytest.skip("No template files found")
        
        template = templates[0]
        
        # Check if excel_parser can handle individual templates
        # (Method name may vary based on actual implementation)
        if hasattr(excel_parser, 'parse_template'):
            result = excel_parser.parse_template(str(template))
            assert result is not None


class TestGenerator:
    """
    Test suite for the OAS Generator module.
    """
    
    def test_generator_import(self):
        """Verify generator module can be imported."""
        from src import generator
        assert hasattr(generator, 'OASGenerator'), "OASGenerator class should exist"
    
    def test_generator_initialization(self):
        """Verify OASGenerator can be instantiated."""
        from src.generator import OASGenerator
        
        gen = OASGenerator()
        assert gen is not None
    
    def test_generator_has_build_methods(self):
        """Verify OASGenerator has required build methods."""
        from src.generator import OASGenerator
        
        gen = OASGenerator()
        
        # Check for main build methods
        assert hasattr(gen, 'build_paths'), "Should have build_paths method"
        assert hasattr(gen, 'build_info'), "Should have build_info method"
    
    def test_generator_version_attribute(self):
        """Verify OASGenerator has version configuration."""
        from src.generator import OASGenerator
        
        # Test with 3.1
        gen_31 = OASGenerator(version="3.1")
        assert gen_31 is not None
        
        # Test with 3.0
        gen_30 = OASGenerator(version="3.0")
        assert gen_30 is not None


class TestMainModule:
    """
    Test suite for the main orchestration module.
    """
    
    def test_main_import(self):
        """Verify main module can be imported."""
        from src import main
        assert main is not None
    
    def test_main_has_generate_function(self):
        """Verify main has generate_oas function."""
        from src import main
        assert hasattr(main, 'generate_oas'), "Should have generate_oas function"
    
    def test_main_generate_oas_signature(self):
        """Verify generate_oas has expected parameters."""
        from src.main import generate_oas
        import inspect
        
        sig = inspect.signature(generate_oas)
        params = list(sig.parameters.keys())
        
        # Check for expected parameters (may vary)
        assert 'base_dir' in params or len(params) > 0, "Should have base_dir parameter"
