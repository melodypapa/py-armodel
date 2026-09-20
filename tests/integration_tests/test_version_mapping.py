import re
from pathlib import Path

import pytest

from armodel.models import AUTOSAR
from tests.integration_tests.test_roundtrip import detect_autosar_version

CANONICAL_RELEASE_XSD_MAPPING = {
    "3.2.3": "autosar.xsd",
    "4.0.3": "AUTOSAR_4-0-3.xsd",
    "4.1.0": "AUTOSAR_4-1-0.xsd",
    "4.1.1": "AUTOSAR_4-1-1.xsd",
    "4.1.2": "AUTOSAR_4-1-2.xsd",
    "4.1.3": "AUTOSAR_4-1-3.xsd",
    "4.2.1": "AUTOSAR_4-2-1.xsd",
    "4.2.2": "AUTOSAR_4-2-2.xsd",
    "4.3.0": "AUTOSAR_00043.xsd",
    "4.3.1": "AUTOSAR_00044.xsd",
    "4.4.0": "AUTOSAR_00046.xsd",
    "R19-11": "AUTOSAR_00048.xsd",
    "R20-11": "AUTOSAR_00049.xsd",
    "R21-11": "AUTOSAR_00050.xsd",
    "R22-11": "AUTOSAR_00051.xsd",
    "R23-11": "AUTOSAR_00052.xsd",
    "R24-11": "AUTOSAR_00053.xsd",
}


def test_xsd_mapping_matches_canonical_autosar_release_mapping(xsd_to_version_mapping):
    for release, schema in CANONICAL_RELEASE_XSD_MAPPING.items():
        assert xsd_to_version_mapping[schema] == release


@pytest.mark.parametrize("schema", ["AUTOSAR_4-3-0.xsd", "AUTOSAR_4-3-1.xsd"])
def test_xsd_mapping_rejects_removed_legacy_4_3_schema_names(tmp_path, xsd_to_version_mapping, schema):
    arxml = tmp_path / schema
    arxml.write_text(
        f'<AUTOSAR xmlns="http://autosar.org/schema/r4.0" ' f'xsi:schemaLocation="http://autosar.org/schema/r4.0 {schema}" ' 'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" />',
        encoding="utf-8",
    )

    assert detect_autosar_version(arxml, xsd_to_version_mapping, "R23-11") == "R23-11"


def test_all_default_fixture_schema_names_are_mapped(xsd_to_version_mapping):
    fixture_dir = Path(__file__).parent / "test_files"
    for arxml in fixture_dir.glob("*.arxml"):
        match = re.search(r'schemaLocation="[^\"]*\s([^\s"]+\.xsd)"', arxml.read_text(encoding="utf-8"))
        assert match is not None, arxml
        schema = match.group(1)
        assert schema in xsd_to_version_mapping, arxml


def test_source_and_integration_release_mappings_agree(xsd_to_version_mapping):
    autosar = AUTOSAR.getInstance()
    for release, schema in CANONICAL_RELEASE_XSD_MAPPING.items():
        assert autosar.release_xsd_mappings[release] == schema
        assert xsd_to_version_mapping[schema] == release
