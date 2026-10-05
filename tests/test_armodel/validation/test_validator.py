import os

import pytest
from lxml import etree

from armodel.validation.validator import (
    ARXMLValidator,
    ValidationError,
    detect_schema_path,
    get_schema,
    register_schema_file,
)

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
TINY_XSD = os.path.join(DATA_DIR, "tiny_autosar.xsd")

VALID_DOC = '<AUTOSAR xmlns="http://autosar.org/schema/r4.0"' ' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"' ' xsi:schemaLocation="http://autosar.org/schema/r4.0 AUTOSAR_TINY.xsd"/>'
INVALID_DOC = (
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


class TestDetectSchemaPath:
    def test_returns_tiny_xsd_for_registered_location(self):
        assert detect_schema_path(VALID_DOC.encode("utf-8")) == TINY_XSD

    def test_returns_none_without_schema_location(self):
        assert detect_schema_path(b'<AUTOSAR xmlns="http://autosar.org/schema/r4.0"/>') is None

    def test_returns_none_for_unbundled_schema(self):
        doc = '<AUTOSAR xmlns="http://autosar.org/schema/r4.0"' ' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"' ' xsi:schemaLocation="http://autosar.org/schema/r4.0 AUTOSAR_4-0-3.xsd"/>'
        assert detect_schema_path(doc.encode("utf-8")) is None

    def test_returns_none_on_undetectable_release(self):
        assert detect_schema_path(b"<NOT-XML/>") is None


class TestARXMLValidator:
    def test_valid_document_returns_no_errors(self):
        assert ARXMLValidator(TINY_XSD).validate_bytes(VALID_DOC.encode("utf-8")) == []

    def test_invalid_document_returns_structured_errors(self):
        errors = ARXMLValidator(TINY_XSD).validate_bytes(INVALID_DOC.encode("utf-8"))
        assert len(errors) >= 1
        assert all(isinstance(e, ValidationError) for e in errors)
        assert errors[0].line == 1
        assert "BOGUS" in errors[0].message

    def test_validate_string_accepts_str(self):
        assert ARXMLValidator(TINY_XSD).validate_string(VALID_DOC) == []

    def test_schema_compilation_is_cached(self):
        first = get_schema(TINY_XSD)
        second = get_schema(TINY_XSD)
        assert first is second

    def test_syntax_error_returns_domain_syntax(self):
        errors = ARXMLValidator(TINY_XSD).validate_bytes(b"<NOT-XML>")
        assert len(errors) == 1
        assert errors[0].domain == "syntax"

    def test_resolver_falls_back_to_shared_xml_xsd(self):
        importing_xsd = os.path.join(DATA_DIR, "importing_autosar.xsd")
        schema = get_schema(importing_xsd)
        assert schema.validate(etree.fromstring(VALID_DOC.encode("utf-8")))

    def test_resolver_resolves_sibling_import(self):
        importing_xsd = os.path.join(DATA_DIR, "importing_local.xsd")
        schema = get_schema(importing_xsd)
        assert schema is not None
        assert schema.validate(etree.fromstring('<HOST xmlns="http://example.org/host"/>'.encode("utf-8")))
