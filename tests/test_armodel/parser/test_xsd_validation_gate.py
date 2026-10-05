import os

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.parser.arxml_parser import ARXMLParser
from armodel.validation.validator import register_schema_file

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "validation", "data")
TINY_XSD = os.path.join(DATA_DIR, "tiny_autosar.xsd")

VALID_DOC = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<AUTOSAR xmlns="http://autosar.org/schema/r4.0"'
    ' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"'
    ' xsi:schemaLocation="http://autosar.org/schema/r4.0 AUTOSAR_TINY.xsd"/>'
)
SCHEMA_INVALID_DOC = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<AUTOSAR xmlns="http://autosar.org/schema/r4.0"'
    ' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"'
    ' xsi:schemaLocation="http://autosar.org/schema/r4.0 AUTOSAR_TINY.xsd">'
    "<BOGUS/>"
    "</AUTOSAR>"
)


@pytest.fixture(autouse=True)
def _register_tiny_schema():
    register_schema_file("AUTOSAR_TINY.xsd", TINY_XSD)
    yield


@pytest.fixture(autouse=True)
def _fresh_document():
    AUTOSAR.getInstance().new()
    yield


def _write(tmp_path, name, content):
    path = os.path.join(str(tmp_path), name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path


def test_valid_file_loads(tmp_path):
    document = AUTOSAR.getInstance()
    parser = ARXMLParser()
    parser.load(_write(tmp_path, "valid.arxml", VALID_DOC), document)
    assert document is not None


def test_schema_invalid_file_raises_with_line_number(tmp_path):
    document = AUTOSAR.getInstance()
    parser = ARXMLParser()
    with pytest.raises(ValueError) as exc_info:
        parser.load(_write(tmp_path, "invalid.arxml", SCHEMA_INVALID_DOC), document)
    assert "failed schema validation" in str(exc_info.value)


def test_warning_mode_logs_and_continues(tmp_path, caplog):
    document = AUTOSAR.getInstance()
    parser = ARXMLParser(options={"warning": True})
    parser.load(_write(tmp_path, "invalid.arxml", SCHEMA_INVALID_DOC), document)


def test_validate_false_skips_validation(tmp_path):
    document = AUTOSAR.getInstance()
    parser = ARXMLParser(options={"validate": False, "warning": True})
    parser.load(_write(tmp_path, "invalid.arxml", SCHEMA_INVALID_DOC), document)


def test_no_matching_schema_logs_warning_and_continues(tmp_path):
    doc_without_bundled_schema = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<AUTOSAR xmlns="http://autosar.org/schema/r4.0"'
        ' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"'
        ' xsi:schemaLocation="http://autosar.org/schema/r4.0 AUTOSAR_4-0-3.xsd"/>'
    )
    document = AUTOSAR.getInstance()
    parser = ARXMLParser()
    parser.load(_write(tmp_path, "unbundled.arxml", doc_without_bundled_schema), document)
