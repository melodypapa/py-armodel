"""
Reader tests: ARLiteral primitives are materialised as their concrete type via
the typed leaf helpers getChildElementOptional<Cls> (Rule 0013.2), and the
inherited T timestamp survives.

Writer counterpart: tests/test_armodel/writer/test_primitive_leaf_helpers.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CategoryString,
    CseCodeType,
    DateTime,
    DiagRequirementIdString,
    Ip4AddressString,
    Ip6AddressString,
    McdIdentifier,
    RegularExpression,
    RevisionLabelString,
    String,
    StrongRevisionLabelString,
    SymbolString,
    UriString,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class TestCategoryStringLeaf:
    def test_reads_concrete_type_and_t(self):
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><CATEGORY T='2023-05-05T00:00:00Z'>SW_COMPONENT_TYPE</CATEGORY></ROOT>")

        value = ARXMLParser().getChildElementOptionalCategoryString(element, "CATEGORY")

        assert isinstance(value, CategoryString)
        assert value.getValue() == "SW_COMPONENT_TYPE"
        assert value.timestamp == "2023-05-05T00:00:00Z"

    def test_missing_returns_none(self):
        element = ET.fromstring(f"<ROOT xmlns='{NS}'/>")

        assert ARXMLParser().getChildElementOptionalCategoryString(element, "CATEGORY") is None


class TestMcdIdentifierLeaf:
    def test_reads_concrete_type_and_t(self):
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><DISPLAY-IDENTIFIER T='2023-06-06T00:00:00Z'>DISP_1</DISPLAY-IDENTIFIER></ROOT>")

        value = ARXMLParser().getChildElementOptionalMcdIdentifier(element, "DISPLAY-IDENTIFIER")

        assert isinstance(value, McdIdentifier)
        assert value.getValue() == "DISP_1"
        assert value.timestamp == "2023-06-06T00:00:00Z"

    def test_missing_returns_none(self):
        element = ET.fromstring(f"<ROOT xmlns='{NS}'/>")

        assert ARXMLParser().getChildElementOptionalMcdIdentifier(element, "DISPLAY-IDENTIFIER") is None


class TestSymbolStringLeaf:
    def test_reads_concrete_type_name_pattern_and_t(self):
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><SYMBOL NAME-PATTERN='[A-Z]+' T='2023-07-07T00:00:00Z'>Sym</SYMBOL></ROOT>")

        value = ARXMLParser().getChildElementOptionalSymbolString(element, "SYMBOL")

        assert isinstance(value, SymbolString)
        assert value.getValue() == "Sym"
        assert isinstance(value.getNamePattern(), String)
        assert value.getNamePattern().getValue() == "[A-Z]+"
        assert value.timestamp == "2023-07-07T00:00:00Z"

    def test_absent_name_pattern_leaves_the_member_unset(self):
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><SYMBOL>Sym</SYMBOL></ROOT>")

        value = ARXMLParser().getChildElementOptionalSymbolString(element, "SYMBOL")

        assert value is not None
        assert value.getNamePattern() is None

    def test_missing_returns_none(self):
        element = ET.fromstring(f"<ROOT xmlns='{NS}'/>")

        assert ARXMLParser().getChildElementOptionalSymbolString(element, "SYMBOL") is None


class TestDiagRequirementIdStringLeaf:
    def test_reads_concrete_type_and_t(self):
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><DIAG-REQUIREMENT T='2023-08-08T00:00:00Z'>REQ-1</DIAG-REQUIREMENT></ROOT>")

        value = ARXMLParser().getChildElementOptionalDiagRequirementIdString(element, "DIAG-REQUIREMENT")

        assert isinstance(value, DiagRequirementIdString)
        assert value.getValue() == "REQ-1"
        assert value.timestamp == "2023-08-08T00:00:00Z"

    def test_missing_returns_none(self):
        element = ET.fromstring(f"<ROOT xmlns='{NS}'/>")

        assert ARXMLParser().getChildElementOptionalDiagRequirementIdString(element, "DIAG-REQUIREMENT") is None


class TestIpAddressStringLeaf:
    def test_reads_concrete_ip4_type_and_t(self):
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><IPV-4-ADDRESS T='2023-10-10T00:00:00Z'>192.168.0.1</IPV-4-ADDRESS></ROOT>")

        value = ARXMLParser().getChildElementOptionalIp4AddressString(element, "IPV-4-ADDRESS")

        assert isinstance(value, Ip4AddressString)
        assert value.getValue() == "192.168.0.1"
        assert value.timestamp == "2023-10-10T00:00:00Z"

    def test_reads_concrete_ip6_type_and_t(self):
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><IPV-6-ADDRESS T='2023-10-10T00:00:00Z'>2001:0db8:0000:0000:0000:0000:0000:0001</IPV-6-ADDRESS></ROOT>")

        value = ARXMLParser().getChildElementOptionalIp6AddressString(element, "IPV-6-ADDRESS")

        assert isinstance(value, Ip6AddressString)
        assert value.getValue() == "2001:0db8:0000:0000:0000:0000:0000:0001"
        assert value.timestamp == "2023-10-10T00:00:00Z"

    def test_missing_returns_none(self):
        element = ET.fromstring(f"<ROOT xmlns='{NS}'/>")

        assert ARXMLParser().getChildElementOptionalIp4AddressString(element, "IPV-4-ADDRESS") is None
        assert ARXMLParser().getChildElementOptionalIp6AddressString(element, "IPV-6-ADDRESS") is None


class TestDateTimeLeaf:
    def test_reads_concrete_type_and_t(self):
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><DATE T='2023-11-11T00:00:00Z'>2009-07-23T14:38:00+01:00</DATE></ROOT>")

        value = ARXMLParser().getChildElementOptionalDateTime(element, "DATE")

        assert isinstance(value, DateTime)
        assert value.getValue() == "2009-07-23T14:38:00+01:00"
        assert value.timestamp == "2023-11-11T00:00:00Z"

    def test_reads_date_only_value(self):
        """The Table 4.48 pattern makes the time part optional: `yyyy-mm-dd` alone is legal."""
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><DATE>2009-07-23</DATE></ROOT>")

        value = ARXMLParser().getChildElementOptionalDateTime(element, "DATE")

        assert isinstance(value, DateTime)
        assert value.getValue() == "2009-07-23"

    def test_missing_returns_none(self):
        element = ET.fromstring(f"<ROOT xmlns='{NS}'/>")

        assert ARXMLParser().getChildElementOptionalDateTime(element, "DATE") is None


class TestRegularExpressionLeaf:
    def test_reads_concrete_type_and_t(self):
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><PATTERN T='2023-12-12T00:00:00Z'>[0-9]+</PATTERN></ROOT>")

        value = ARXMLParser().getChildElementOptionalRegularExpression(element, "PATTERN")

        assert isinstance(value, RegularExpression)
        assert value.getValue() == "[0-9]+"
        assert value.timestamp == "2023-12-12T00:00:00Z"

    def test_reads_alternation_value(self):
        """Table 4.60 has no pattern facet, so any XML Schema regex is a legal value."""
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><REGULAR-EXPRESSION>critical|significant|minor|low</REGULAR-EXPRESSION></ROOT>")

        value = ARXMLParser().getChildElementOptionalRegularExpression(element, "REGULAR-EXPRESSION")

        assert isinstance(value, RegularExpression)
        assert value.getValue() == "critical|significant|minor|low"

    def test_empty_element_becomes_empty_string(self):
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><PATTERN/></ROOT>")

        value = ARXMLParser().getChildElementOptionalRegularExpression(element, "PATTERN")

        assert isinstance(value, RegularExpression)
        assert value.getValue() == ""

    def test_missing_returns_none(self):
        element = ET.fromstring(f"<ROOT xmlns='{NS}'/>")

        assert ARXMLParser().getChildElementOptionalRegularExpression(element, "PATTERN") is None


class TestRevisionLabelStringLeaf:
    def test_reads_concrete_type_and_t(self):
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><REVISION-LABEL T='2024-01-14T00:00:00Z'>4.0.0</REVISION-LABEL></ROOT>")

        value = ARXMLParser().getChildElementOptionalRevisionLabelString(element, "REVISION-LABEL")

        assert isinstance(value, RevisionLabelString)
        assert value.getValue() == "4.0.0"
        assert value.timestamp == "2024-01-14T00:00:00Z"

    def test_reads_semicolon_suffix_value(self):
        """The Table 4.61 Note lists `4.0.0;12` as a legal pattern: `;` is one of the three allowed suffix separators."""
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><REVISION-LABEL>4.0.0;12</REVISION-LABEL></ROOT>")

        value = ARXMLParser().getChildElementOptionalRevisionLabelString(element, "REVISION-LABEL")

        assert isinstance(value, RevisionLabelString)
        assert value.getValue() == "4.0.0;12"

    def test_rejects_text_violating_the_spec_pattern(self):
        """The reader validates against `[0-9]+\\.[0-9]+\\.[0-9]+([\\._;].*)?`; a permissive ARLiteral would not."""
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><REVISION-LABEL>R23-11</REVISION-LABEL></ROOT>")

        with pytest.raises(ValueError):
            ARXMLParser().getChildElementOptionalRevisionLabelString(element, "REVISION-LABEL")

    def test_missing_returns_none(self):
        element = ET.fromstring(f"<ROOT xmlns='{NS}'/>")

        assert ARXMLParser().getChildElementOptionalRevisionLabelString(element, "REVISION-LABEL") is None


class TestStrongRevisionLabelStringLeaf:
    def test_reads_concrete_type_and_t(self):
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><VERSION T='2026-10-14T00:00:00Z'>1.0.0-alpha+001</VERSION></ROOT>")

        value = ARXMLParser().getChildElementOptionalStrongRevisionLabelString(element, "VERSION")

        assert isinstance(value, StrongRevisionLabelString)
        assert value.getValue() == "1.0.0-alpha+001"
        assert value.timestamp == "2026-10-14T00:00:00Z"

    def test_reads_build_metadata_value(self):
        """The Table 4.64 Note lists `1.0.0+20130313144700` as a legal pattern: bare `+build-metadata` with no pre-release part."""
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><VERSION>1.0.0+20130313144700</VERSION></ROOT>")

        value = ARXMLParser().getChildElementOptionalStrongRevisionLabelString(element, "VERSION")

        assert isinstance(value, StrongRevisionLabelString)
        assert value.getValue() == "1.0.0+20130313144700"

    def test_reads_dotted_pre_release_and_metadata_value(self):
        """The Table 4.64 Note lists `1.0.0-beta+exp.sha.5114f85`: dotted identifiers on both the `-` and `+` sides."""
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><VERSION>1.0.0-beta+exp.sha.5114f85</VERSION></ROOT>")

        value = ARXMLParser().getChildElementOptionalStrongRevisionLabelString(element, "VERSION")

        assert isinstance(value, StrongRevisionLabelString)
        assert value.getValue() == "1.0.0-beta+exp.sha.5114f85"

    def test_empty_element_becomes_empty_string(self):
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><VERSION/></ROOT>")

        value = ARXMLParser().getChildElementOptionalStrongRevisionLabelString(element, "VERSION")

        assert isinstance(value, StrongRevisionLabelString)
        assert value.getValue() == ""

    def test_missing_returns_none(self):
        element = ET.fromstring(f"<ROOT xmlns='{NS}'/>")

        assert ARXMLParser().getChildElementOptionalStrongRevisionLabelString(element, "VERSION") is None


class TestCseCodeTypeLeaf:
    def test_reads_concrete_type_and_t(self):
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><CSE-CODE T='2026-10-17T00:00:00Z'>100</CSE-CODE></ROOT>")

        value = ARXMLParser().getChildElementOptionalCseCodeType(element, "CSE-CODE")

        assert isinstance(value, CseCodeType)
        assert value.getValue() == "100"
        assert value.timestamp == "2026-10-17T00:00:00Z"

    def test_reads_zero_value(self):
        """`0` is the unsignedInt lower bound and the value the existing MultidimensionalTime fixtures use."""
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><CSE-CODE>0</CSE-CODE></ROOT>")

        value = ARXMLParser().getChildElementOptionalCseCodeType(element, "CSE-CODE")

        assert isinstance(value, CseCodeType)
        assert value.getValue() == "0"

    def test_reads_unsigned_int_max_value(self):
        """`4294967295` is xsd:unsignedInt's inclusive upper bound — the constraint CSE-CODE-TYPE-STRING--SIMPLE actually applies."""
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><CSE-CODE>4294967295</CSE-CODE></ROOT>")

        value = ARXMLParser().getChildElementOptionalCseCodeType(element, "CSE-CODE")

        assert isinstance(value, CseCodeType)
        assert value.getValue() == "4294967295"

    def test_empty_element_becomes_empty_string(self):
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><CSE-CODE/></ROOT>")

        value = ARXMLParser().getChildElementOptionalCseCodeType(element, "CSE-CODE")

        assert isinstance(value, CseCodeType)
        assert value.getValue() == ""

    def test_missing_returns_none(self):
        element = ET.fromstring(f"<ROOT xmlns='{NS}'/>")

        assert ARXMLParser().getChildElementOptionalCseCodeType(element, "CSE-CODE") is None


class TestUriStringLeaf:
    def test_reads_concrete_type_and_t(self):
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><URI T='2026-10-15T00:00:00Z'>https://example.com/resource</URI></ROOT>")

        value = ARXMLParser().getChildElementOptionalUriString(element, "URI")

        assert isinstance(value, UriString)
        assert value.getValue() == "https://example.com/resource"
        assert value.timestamp == "2026-10-15T00:00:00Z"

    def test_reads_ldap_url_value(self):
        """The LDAP-URL of ACL-ROLE (XSD l.1288) is one of the ten element-form consumers of AR:URI-STRING."""
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><LDAP-URL>ldap://example.com/Role</LDAP-URL></ROOT>")

        value = ARXMLParser().getChildElementOptionalUriString(element, "LDAP-URL")

        assert isinstance(value, UriString)
        assert value.getValue() == "ldap://example.com/Role"

    def test_empty_element_becomes_empty_string(self):
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><URI/></ROOT>")

        value = ARXMLParser().getChildElementOptionalUriString(element, "URI")

        assert isinstance(value, UriString)
        assert value.getValue() == ""

    def test_missing_returns_none(self):
        element = ET.fromstring(f"<ROOT xmlns='{NS}'/>")

        assert ARXMLParser().getChildElementOptionalUriString(element, "URI") is None
