"""Shared helper to validate ARXML fragments against the AUTOSAR XSD schema.

Delegates to :mod:`armodel.validation.validator` so the test-suite helper and the
runtime validator share one implementation and one schema cache. Defaults to the
bundled R4.4.0 schema (AUTOSAR_00046.xsd), matching the original behavior of this
helper.
"""

import os

from armodel.validation.validator import SCHEMA_DIR, ARXMLValidator

XSD_DIR = os.path.join(SCHEMA_DIR, "R4.4.0")
XSD_PATH = os.path.join(XSD_DIR, "AUTOSAR_00046.xsd")


def is_valid(xml):
    """Return True when the given XML byte/string is valid per the AUTOSAR XSD."""
    data = xml.encode("utf-8") if isinstance(xml, str) else xml
    return ARXMLValidator(XSD_PATH).validate_bytes(data) == []


def assert_valid(xml):
    """Assert that the given XML byte/string is valid per the AUTOSAR XSD."""
    data = xml.encode("utf-8") if isinstance(xml, str) else xml
    errors = ARXMLValidator(XSD_PATH).validate_bytes(data)
    assert errors == [], "XML does not validate against AUTOSAR_00046.xsd:\n%s" % "\n".join("line %s: %s" % (error.line, error.message) for error in errors)
