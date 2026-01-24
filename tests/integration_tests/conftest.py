"""Pytest fixtures for integration tests."""
from pathlib import Path
from typing import Dict, Generator, List, Tuple

import pytest

try:
    import yaml
except ImportError:
    yaml = None

from armodel.models import AUTOSAR


def get_test_files_dir() -> Path:
    """Get the default test files directory."""
    return Path(__file__).parent / "test_files"


def load_config() -> Dict:
    """Load configuration from config.yaml if it exists.

    Returns:
        Configuration dict with additional_directories and exclude_patterns
    """
    if yaml is None:
        return {"additional_directories": [], "exclude_patterns": []}

    config_path = Path(__file__).parent / "config.yaml"
    if not config_path.exists():
        return {"additional_directories": [], "exclude_patterns": []}

    with open(config_path, "r") as f:
        return yaml.safe_load(f) or {"additional_directories": [],
                                      "exclude_patterns": []}


def collect_arxml_files(
    directory: Path,
    recursive: bool = False,
    exclude_patterns: List[str] = None
) -> List[Path]:
    """Collect ARXML files from a directory.

    Args:
        directory: Directory to scan
        recursive: Whether to scan subdirectories
        exclude_patterns: List of glob patterns to exclude

    Returns:
        List of ARXML file paths
    """
    if not directory.exists() or not directory.is_dir():
        return []

    exclude_patterns = exclude_patterns or []
    arxml_files = []

    if recursive:
        pattern = "**/*.arxml"
    else:
        pattern = "*.arxml"

    for file_path in directory.glob(pattern):
        # Check exclude patterns
        excluded = False
        for pattern_str in exclude_patterns:
            if file_path.match(pattern_str):
                excluded = True
                break

        if not excluded:
            arxml_files.append(file_path)

    return arxml_files


@pytest.fixture
def test_files_dir() -> Path:
    """Return the default test files directory."""
    return get_test_files_dir()


@pytest.fixture
def autosar_reset() -> Generator[None, None, None]:
    """Reset AUTOSAR singleton before and after each test.

    Yields:
        None
    """
    # Reset before test
    AUTOSAR.getInstance().new()
    yield
    # Reset after test
    AUTOSAR.getInstance().new()


@pytest.fixture
def temp_file(tmp_path: Path) -> Path:
    """Create a temporary file path.

    Args:
        tmp_path: Pytest's built-in tmp_path fixture

    Returns:
        Path to temporary file
    """
    return tmp_path / "temp.arxml"


@pytest.fixture
def arxml_files() -> List[Tuple[Path, str]]:
    """Return list of all ARXML file paths with their category.

    Returns:
        List of tuples (file_path, category) where category is:
        - "default" for files from test_files/
        - Config-specified category for additional files
    """
    result = []

    # Get default test files
    default_dir = get_test_files_dir()
    if default_dir.exists():
        for file_path in default_dir.glob("*.arxml"):
            result.append((file_path, "default"))

    # Load additional directories from config
    config = load_config()
    config_dir = Path(__file__).parent
    for dir_config in config.get("additional_directories", []):
        dir_path = config_dir / dir_config["path"]
        category = dir_config.get("category", "additional")
        recursive = dir_config.get("recursive", False)

        files = collect_arxml_files(
            dir_path,
            recursive=recursive,
            exclude_patterns=config.get("exclude_patterns", [])
        )

        for file_path in files:
            result.append((file_path, category))

    return result


@pytest.fixture
def xsd_to_version_mapping() -> Dict[str, str]:
    """Mapping from XSD filenames to AUTOSAR release versions.

    Returns:
        Dict mapping XSD filename to ARRelease version string
    """
    return {
        # AUTOSAR 4.x releases
        "AUTOSAR_4-0-3.xsd": "4.0.3",
        "AUTOSAR_4-1-0.xsd": "4.1.0",
        "AUTOSAR_4-1-1.xsd": "4.1.1",
        "AUTOSAR_4-1-2.xsd": "4.1.2",
        "AUTOSAR_4-1-3.xsd": "4.1.3",
        "AUTOSAR_4-2-1.xsd": "4.2.1",
        "AUTOSAR_4-2-2.xsd": "4.2.2",
        "AUTOSAR_4-3-0.xsd": "4.3.0",
        "AUTOSAR_4-3-1.xsd": "4.3.1",
        "AUTOSAR_4-4-0.xsd": "4.4.0",
        # AUTOSAR R19-11 (CP)
        "AUTOSAR_00048.xsd": "R19-11",
        # AUTOSAR R20-11 (CP)
        "AUTOSAR_00049.xsd": "R20-11",
        # AUTOSAR R21-11 (CP)
        "AUTOSAR_00050.xsd": "R21-11",
        # AUTOSAR R22-11 (CP)
        "AUTOSAR_00051.xsd": "R22-11",
        # AUTOSAR R23-11 (CP)
        "AUTOSAR_00052.xsd": "R23-11",
        # AUTOSAR R24-11 (CP)
        "AUTOSAR_00053.xsd": "R24-11",
    }


@pytest.fixture
def default_ar_version() -> str:
    """Default AUTOSAR version when auto-detection fails.

    Returns:
        Default ARRelease version string
    """
    return "R23-11"
