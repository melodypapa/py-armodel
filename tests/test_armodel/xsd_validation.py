"""Shared helper to validate ARXML fragments against the AUTOSAR XSD schema.

The AUTOSAR_00046.xsd schema imports the W3C ``xml.xsd`` namespace schema,
which is not shipped alongside it. We therefore install a custom
``etree.Resolver`` that maps relative ``import``/``include`` filenames to the
sibling ``docs/requirements/xsd/`` directory, so lxml can resolve ``xml.xsd``.
"""

import os

from lxml import etree

XSD_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "docs", "requirements", "xsd")
XSD_PATH = os.path.join(XSD_DIR, "AUTOSAR_00046.xsd")


class _AUTOSARResolver(etree.Resolver):
    def resolve(self, url, id, context):
        candidate = os.path.join(XSD_DIR, os.path.basename(url))
        if os.path.exists(candidate):
            return self.resolve_filename(candidate, context)
        return None


def get_schema():
    """Return a compiled lxml XMLSchema for AUTOSAR_00046.xsd (cached)."""
    parser = etree.XMLParser()
    parser.resolvers.add(_AUTOSARResolver())
    return etree.XMLSchema(etree.parse(XSD_PATH, parser))


def is_valid(xml):
    """Return True when the given XML byte/string is valid per the AUTOSAR XSD."""
    return get_schema().validate(etree.fromstring(xml.encode("utf-8") if isinstance(xml, str) else xml))


def assert_valid(xml):
    """Assert that the given XML byte/string is valid per the AUTOSAR XSD."""
    schema = get_schema()
    result = schema.validate(etree.fromstring(xml.encode("utf-8") if isinstance(xml, str) else xml))
    assert result, "XML does not validate against AUTOSAR_00046.xsd:\n%s" % "\n".join(str(e) for e in schema.error_log[:10])
