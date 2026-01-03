"""
Pytest configuration and shared fixtures for regression tests.
"""

import os
import sys
import pytest
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))


# --- Path Fixtures ---

@pytest.fixture
def project_root() -> Path:
    """Return the project root directory."""
    return PROJECT_ROOT


@pytest.fixture
def api_templates_dir(project_root) -> Path:
    """Return the API Templates directory."""
    return project_root / "API Templates"


@pytest.fixture
def expected_results_dir(project_root) -> Path:
    """Return the Expected results directory."""
    return project_root / "Expected results"


@pytest.fixture
def oas_generated_dir(project_root) -> Path:
    """Return the OAS Generated directory."""
    return project_root / "OAS Generated"


# --- Golden File Fixtures ---

@pytest.fixture
def golden_oas31(expected_results_dir) -> Path:
    """Return path to OAS 3.1 golden file (latest by date in filename)."""
    files = list(expected_results_dir.glob("*OpenApi3.1*FPAD*.yaml"))
    # Exclude SWIFT variants
    files = [f for f in files if "SWIFT" not in f.name]
    if not files:
        pytest.skip("No OAS 3.1 golden file found")
    # Sort by date in filename (YYYYMMDD format after EBACL_FPAD_)
    files.sort(key=lambda f: f.name.split('_')[2] if len(f.name.split('_')) > 2 else "", reverse=True)
    return files[0]  # Latest by date


@pytest.fixture
def golden_oas30(expected_results_dir) -> Path:
    """Return path to OAS 3.0 golden file (latest by date in filename)."""
    files = list(expected_results_dir.glob("*OpenApi3.0*FPAD*.yaml"))
    # Exclude SWIFT variants
    files = [f for f in files if "SWIFT" not in f.name]
    if not files:
        pytest.skip("No OAS 3.0 golden file found")
    # Sort by date in filename
    files.sort(key=lambda f: f.name.split('_')[2] if len(f.name.split('_')) > 2 else "", reverse=True)
    return files[0]


@pytest.fixture
def golden_oas31_swift(expected_results_dir) -> Path:
    """Return path to OAS 3.1 SWIFT golden file."""
    files = list(expected_results_dir.glob("*OpenApi3.1*SWIFT*.yaml"))
    if not files:
        pytest.skip("No OAS 3.1 SWIFT golden file found")
    return sorted(files)[-1]


@pytest.fixture
def golden_oas30_swift(expected_results_dir) -> Path:
    """Return path to OAS 3.0 SWIFT golden file."""
    files = list(expected_results_dir.glob("*OpenApi3.0*SWIFT*.yaml"))
    if not files:
        pytest.skip("No OAS 3.0 SWIFT golden file found")
    return sorted(files)[-1]


# --- Generator Fixture ---

@pytest.fixture
def generate_oas(api_templates_dir, tmp_path):
    """
    Fixture that returns a function to generate OAS files.
    
    Usage:
        def test_something(generate_oas):
            output_dir = generate_oas(gen_30=True, gen_31=True, gen_swift=False)
            # Check files in output_dir
    """
    from src import main
    
    def _generate(gen_30=True, gen_31=True, gen_swift=False):
        output_dir = tmp_path / "generated"
        output_dir.mkdir(exist_ok=True)
        
        logs = []
        main.generate_oas(
            base_dir=str(api_templates_dir),
            gen_30=gen_30,
            gen_31=gen_31,
            gen_swift=gen_swift,
            output_dir=str(output_dir),
            log_callback=lambda msg: logs.append(msg)
        )
        
        return output_dir
    
    return _generate


# --- Comparison Fixture ---

@pytest.fixture
def compare_yaml():
    """
    Fixture that returns the compare_oas_files function.
    """
    from tests.utils.deep_diff import compare_oas_files
    return compare_oas_files
