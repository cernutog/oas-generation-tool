"""
Validation Module Tests.

Tests for the Spectral linter integration (linter.py).
"""

import pytest
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


class TestLinterModule:
    """
    Test suite for the Spectral linter integration.
    """
    
    def test_linter_import(self):
        """Verify linter module can be imported."""
        from src import linter
        assert hasattr(linter, 'SpectralRunner'), "SpectralRunner class should exist"
    
    def test_linter_initialization(self):
        """Verify SpectralRunner can be instantiated."""
        from src.linter import SpectralRunner
        
        runner = SpectralRunner()
        assert runner is not None
        assert hasattr(runner, 'cmd'), "Should have cmd attribute"
    
    def test_linter_has_required_methods(self):
        """Verify SpectralRunner has required methods."""
        from src.linter import SpectralRunner
        
        runner = SpectralRunner()
        assert hasattr(runner, 'run_lint'), "Should have run_lint method"
    
    def test_linter_custom_command(self):
        """Test SpectralRunner with custom command."""
        from src.linter import SpectralRunner
        
        runner = SpectralRunner(spectral_cmd="custom_spectral")
        assert runner.cmd == "custom_spectral"
    
    def test_linter_lint_nonexistent_file(self):
        """Test linting a file that doesn't exist."""
        from src.linter import SpectralRunner
        
        runner = SpectralRunner()
        result = runner.run_lint("/nonexistent/path/file.yaml")
        
        assert result is not None
        assert result.get('success') == False, "Should fail for nonexistent file"
        assert 'error_msg' in result


class TestRulesData:
    """
    Test suite for validation rules (rules_data.py).
    """
    
    def test_rules_data_import(self):
        """Verify rules_data module can be imported."""
        from src import rules_data
        assert rules_data is not None
    
    def test_rules_data_has_spectral_rules(self):
        """Verify rules_data contains SPECTRAL_RULES."""
        from src import rules_data
        
        assert hasattr(rules_data, 'SPECTRAL_RULES'), "Should have SPECTRAL_RULES dict"
        assert isinstance(rules_data.SPECTRAL_RULES, dict), "SPECTRAL_RULES should be a dict"
    
    def test_rules_data_has_expected_rules(self):
        """Verify SPECTRAL_RULES contains known rules."""
        from src.rules_data import SPECTRAL_RULES
        
        # Check for some known rules
        known_rules = [
            'oas3-schema',
            'operation-operationId',
            'path-params',
        ]
        
        for rule in known_rules:
            assert rule in SPECTRAL_RULES, f"Should contain '{rule}' rule"
    
    def test_rules_data_structure(self):
        """Verify each rule has expected structure."""
        from src.rules_data import SPECTRAL_RULES
        
        for rule_name, rule_data in SPECTRAL_RULES.items():
            assert 'description' in rule_data, f"Rule '{rule_name}' should have description"
            assert 'url' in rule_data, f"Rule '{rule_name}' should have url"
