import hashlib
import os

import pytest

from armodel.validation.validator import SCHEMA_DIR, get_schema

REPO_ROOT = os.path.join(os.path.dirname(__file__), "..", "..", "..")

BUNDLED_SCHEMAS = [
    ("R23-11", "AUTOSAR_00052.xsd"),
    ("R4.4.0", "AUTOSAR_00046.xsd"),
    ("R4.3.1", "AUTOSAR_00044.xsd"),
    ("R3.2.3", "AUTOSAR.xsd"),
]


def _sha256(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


@pytest.mark.parametrize("release,xsd_name", BUNDLED_SCHEMAS)
def test_bundled_schemas_match_repo_copies(release, xsd_name):
    bundled = os.path.join(SCHEMA_DIR, release, xsd_name)
    repo = os.path.join(REPO_ROOT, "autosar", release, "xsd", xsd_name)
    assert _sha256(bundled) == _sha256(repo)


@pytest.mark.slow
@pytest.mark.parametrize("release,xsd_name", BUNDLED_SCHEMAS)
def test_bundled_schema_compiles(release, xsd_name):
    schema = get_schema(os.path.join(SCHEMA_DIR, release, xsd_name))
    assert schema is not None
