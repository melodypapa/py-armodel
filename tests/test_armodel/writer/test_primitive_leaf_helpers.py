"""
Writer tests: ARLiteral primitives are emitted through the typed leaf helpers
setChildElementOptional<Cls> (Rule 0013.2), carrying the inherited T timestamp.

Reader counterpart: tests/test_armodel/parser/test_primitive_leaf_helpers.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.AgeConstraint import (
    AgeConstraint,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions import (
    EcuTiming,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import (
    MultidimensionalTime,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CategoryString,
    CseCodeType,
    DateTime,
    DiagRequirementIdString,
    Integer,
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
from armodel.validation.validator import ARXMLValidator
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


class TestCategoryStringLeaf:
    def test_writes_concrete_type_and_t(self):
        value = CategoryString()
        value.setValue("SW_COMPONENT_TYPE")
        value.timestamp = "2023-05-05T00:00:00Z"

        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalCategoryString(element, "CATEGORY", value)

        written = element.find("CATEGORY")
        assert written is not None
        assert written.text == "SW_COMPONENT_TYPE"
        assert written.attrib["T"] == "2023-05-05T00:00:00Z"

    def test_none_emits_nothing(self):
        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalCategoryString(element, "CATEGORY", None)

        assert element.find("CATEGORY") is None


class TestMcdIdentifierLeaf:
    def test_writes_concrete_type_and_t(self):
        value = McdIdentifier()
        value.setValue("DISP_1")
        value.timestamp = "2023-06-06T00:00:00Z"

        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalMcdIdentifier(element, "DISPLAY-IDENTIFIER", value)

        written = element.find("DISPLAY-IDENTIFIER")
        assert written is not None
        assert written.text == "DISP_1"
        assert written.attrib["T"] == "2023-06-06T00:00:00Z"

    def test_none_emits_nothing(self):
        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalMcdIdentifier(element, "DISPLAY-IDENTIFIER", None)

        assert element.find("DISPLAY-IDENTIFIER") is None


class TestSymbolStringLeaf:
    def test_writes_concrete_type_name_pattern_and_t(self):
        value = SymbolString()
        value.setValue("Sym")
        value.setNamePattern(String().setValue("[A-Z]+"))
        value.timestamp = "2023-07-07T00:00:00Z"

        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalSymbolString(element, "SYMBOL", value)

        written = element.find("SYMBOL")
        assert written is not None
        assert written.text == "Sym"
        assert written.attrib["NAME-PATTERN"] == "[A-Z]+"
        assert written.attrib["T"] == "2023-07-07T00:00:00Z"

    def test_name_pattern_absent_emits_no_attribute(self):
        value = SymbolString()
        value.setValue("Sym")

        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalSymbolString(element, "SYMBOL", value)

        written = element.find("SYMBOL")
        assert written is not None
        assert "NAME-PATTERN" not in written.attrib

    def test_none_emits_nothing(self):
        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalSymbolString(element, "SYMBOL", None)

        assert element.find("SYMBOL") is None


class TestDiagRequirementIdStringLeaf:
    def test_writes_concrete_type_and_t(self):
        value = DiagRequirementIdString()
        value.setValue("REQ-1")
        value.timestamp = "2023-08-08T00:00:00Z"

        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalDiagRequirementIdString(element, "DIAG-REQUIREMENT", value)

        written = element.find("DIAG-REQUIREMENT")
        assert written is not None
        assert written.text == "REQ-1"
        assert written.attrib["T"] == "2023-08-08T00:00:00Z"

    def test_none_emits_nothing(self):
        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalDiagRequirementIdString(element, "DIAG-REQUIREMENT", None)

        assert element.find("DIAG-REQUIREMENT") is None


class TestIpAddressStringLeaf:
    def test_writes_concrete_ip4_type_and_t(self):
        value = Ip4AddressString()
        value.setValue("192.168.0.1")
        value.timestamp = "2023-10-10T00:00:00Z"

        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalIp4AddressString(element, "IPV-4-ADDRESS", value)

        written = element.find("IPV-4-ADDRESS")
        assert written is not None
        assert written.text == "192.168.0.1"
        assert written.attrib["T"] == "2023-10-10T00:00:00Z"

    def test_none_emits_nothing_ip4(self):
        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalIp4AddressString(element, "IPV-4-ADDRESS", None)

        assert element.find("IPV-4-ADDRESS") is None

    def test_writes_concrete_ip6_type_and_t(self):
        value = Ip6AddressString()
        value.setValue("2001:0db8:0000:0000:0000:0000:0000:0001")
        value.timestamp = "2023-10-10T00:00:00Z"

        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalIp6AddressString(element, "IPV-6-ADDRESS", value)

        written = element.find("IPV-6-ADDRESS")
        assert written is not None
        assert written.text == "2001:0db8:0000:0000:0000:0000:0000:0001"
        assert written.attrib["T"] == "2023-10-10T00:00:00Z"

    def test_none_emits_nothing(self):
        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalIp6AddressString(element, "IPV-6-ADDRESS", None)

        assert element.find("IPV-6-ADDRESS") is None


class TestDateTimeLeaf:
    def test_writes_concrete_type_and_t(self):
        value = DateTime()
        value.setValue("2009-07-23T14:38:00+01:00")
        value.timestamp = "2023-11-11T00:00:00Z"

        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalDateTime(element, "DATE", value)

        written = element.find("DATE")
        assert written is not None
        assert written.text == "2009-07-23T14:38:00+01:00"
        assert written.attrib["T"] == "2023-11-11T00:00:00Z"

    def test_writes_date_only_value(self):
        """The Table 4.48 pattern makes the time part optional: `yyyy-mm-dd` alone is legal."""
        value = DateTime().setValue("2009-07-23")

        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalDateTime(element, "DATE", value)

        written = element.find("DATE")
        assert written is not None
        assert written.text == "2009-07-23"

    def test_none_emits_nothing(self):
        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalDateTime(element, "DATE", None)

        assert element.find("DATE") is None


class TestRegularExpressionLeaf:
    def test_writes_concrete_type_and_t(self):
        value = RegularExpression()
        value.setValue("[0-9]+")
        value.timestamp = "2023-12-12T00:00:00Z"

        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalRegularExpression(element, "PATTERN", value)

        written = element.find("PATTERN")
        assert written is not None
        assert written.text == "[0-9]+"
        assert written.attrib["T"] == "2023-12-12T00:00:00Z"

    def test_writes_alternation_value(self):
        """Table 4.60 has no pattern facet, so any XML Schema regex is a legal value."""
        value = RegularExpression().setValue("critical|significant|minor|low")

        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalRegularExpression(element, "REGULAR-EXPRESSION", value)

        written = element.find("REGULAR-EXPRESSION")
        assert written is not None
        assert written.text == "critical|significant|minor|low"

    def test_none_emits_nothing(self):
        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalRegularExpression(element, "PATTERN", None)

        assert element.find("PATTERN") is None


class TestRevisionLabelStringLeaf:
    def test_writes_concrete_type_and_t(self):
        value = RevisionLabelString()
        value.setValue("4.0.0")
        value.timestamp = "2024-01-14T00:00:00Z"

        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalRevisionLabelString(element, "REVISION-LABEL", value)

        written = element.find("REVISION-LABEL")
        assert written is not None
        assert written.text == "4.0.0"
        assert written.attrib["T"] == "2024-01-14T00:00:00Z"

    def test_writes_semicolon_suffix_value(self):
        """The Table 4.61 Note lists `4.0.0;12` as a legal pattern: `;` is one of the three allowed suffix separators."""
        value = RevisionLabelString().setValue("4.0.0;12")

        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalRevisionLabelString(element, "REVISION-LABEL", value)

        written = element.find("REVISION-LABEL")
        assert written is not None
        assert written.text == "4.0.0;12"

    def test_none_emits_nothing(self):
        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalRevisionLabelString(element, "REVISION-LABEL", None)

        assert element.find("REVISION-LABEL") is None


class TestStrongRevisionLabelStringLeaf:
    def test_writes_concrete_type_and_t(self):
        value = StrongRevisionLabelString()
        value.setValue("1.0.0-alpha+001")
        value.timestamp = "2026-10-14T00:00:00Z"

        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalStrongRevisionLabelString(element, "VERSION", value)

        written = element.find("VERSION")
        assert written is not None
        assert written.text == "1.0.0-alpha+001"
        assert written.attrib["T"] == "2026-10-14T00:00:00Z"

    def test_writes_build_metadata_value(self):
        """The Table 4.64 Note lists `1.0.0+20130313144700` as a legal pattern: bare `+build-metadata` with no pre-release part."""
        value = StrongRevisionLabelString().setValue("1.0.0+20130313144700")

        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalStrongRevisionLabelString(element, "VERSION", value)

        written = element.find("VERSION")
        assert written is not None
        assert written.text == "1.0.0+20130313144700"

    def test_writes_dotted_pre_release_and_metadata_value(self):
        """The Table 4.64 Note lists `1.0.0-beta+exp.sha.5114f85`: dotted identifiers on both the `-` and `+` sides."""
        value = StrongRevisionLabelString().setValue("1.0.0-beta+exp.sha.5114f85")

        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalStrongRevisionLabelString(element, "VERSION", value)

        written = element.find("VERSION")
        assert written is not None
        assert written.text == "1.0.0-beta+exp.sha.5114f85"

    def test_none_emits_nothing(self):
        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalStrongRevisionLabelString(element, "VERSION", None)

        assert element.find("VERSION") is None


class TestCseCodeTypeLeaf:
    def test_writes_concrete_type_and_t(self):
        value = CseCodeType()
        value.setValue("100")
        value.timestamp = "2026-10-17T00:00:00Z"

        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalCseCodeType(element, "CSE-CODE", value)

        written = element.find("CSE-CODE")
        assert written is not None
        assert written.text == "100"
        assert written.attrib["T"] == "2026-10-17T00:00:00Z"

    def test_writes_zero_value(self):
        """`0` is the unsignedInt lower bound and the value the existing MultidimensionalTime fixtures use."""
        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalCseCodeType(element, "CSE-CODE", CseCodeType().setValue("0"))

        written = element.find("CSE-CODE")
        assert written is not None
        assert written.text == "0"

    def test_writes_unsigned_int_max_value(self):
        """`4294967295` is xsd:unsignedInt's inclusive upper bound — the constraint CSE-CODE-TYPE-STRING--SIMPLE actually applies."""
        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalCseCodeType(element, "CSE-CODE", CseCodeType().setValue("4294967295"))

        written = element.find("CSE-CODE")
        assert written is not None
        assert written.text == "4294967295"

    def test_none_emits_nothing(self):
        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalCseCodeType(element, "CSE-CODE", None)

        assert element.find("CSE-CODE") is None


class TestCseCodeTypeXsdValidation:
    """XSD-validated proof of the ``CSE-CODE`` emission shape (Rule 0027).

    ``CseCodeType`` has no own XML element (XSD ``complexType
    CSE-CODE-TYPE-STRING`` is ``xsd:simpleContent`` with only the ``AR-OBJECT``
    attributeGroup), so its writer shape is judged by the element its consumer emits:
    ``CSE-CODE`` inside ``MULTIDIMENSIONAL-TIME`` (XSD group l.83759, sequence
    ``CSE-CODE`` → ``CSE-CODE-FACTOR``, both 0..1).

    A **document-level** ``save`` → ``load`` round-trip is not reachable for this path
    today: no ARPackage-reachable model class carries a ``TimingExtension``
    (``grep "def setTiming("`` over ``src/armodel/models/`` returns nothing, and
    ``EcuInstance`` exposes zero timing accessors), so ``writeEcuTiming`` is only
    exercised at the element level. This test therefore validates the writer's real
    subtree against the bundled R23-11 schema inside the minimum ``AR-PACKAGE`` /
    ``ELEMENTS`` scaffolding the schema requires — ``ELEMENTS`` is the wrapper the
    ``AR-PACKAGE`` choice lives in (AUTOSAR_00052.xsd l.4938-4945), and omitting it
    makes the validator reject ``ECU-TIMING`` itself, which is scaffolding behaviour,
    not a writer defect.
    """

    @pytest.fixture(autouse=True)
    def reset_autosar(self):
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease("R23-11")
        yield
        AUTOSAR.getInstance().new()

    def _emit(self):
        document = AUTOSAR.getInstance()
        timing = EcuTiming(document, "EcuTiming1")
        constraint = AgeConstraint(timing, "Age1")
        constraint.setMaximum(MultidimensionalTime().setCseCode(CseCodeType().setValue("100")).setCseCodeFactor(Integer().setValue(360)))
        constraint.setMinimum(MultidimensionalTime().setCseCode(CseCodeType().setValue("0")))
        timing.addTimingGuarantee(constraint)

        package = ET.Element("AR-PACKAGE")
        short_name = ET.SubElement(package, "SHORT-NAME")
        short_name.text = "P"
        ARXMLWriter().writeEcuTiming(ET.SubElement(package, "ELEMENTS"), timing)
        return package

    def test_emitted_cse_code_shape_validates_against_bundled_schema(self):
        package = self._emit()

        assert package.find("ELEMENTS/ECU-TIMING/TIMING-GUARANTEES/AGE-CONSTRAINT/MAXIMUM/CSE-CODE").text == "100"

        root = ET.Element(
            "AUTOSAR",
            {
                "xmlns": NS,
                "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
                "xsi:schemaLocation": NS + " AUTOSAR_00052.xsd",
            },
        )
        packages = ET.SubElement(root, "AR-PACKAGES")
        wrapper = ET.SubElement(packages, "AR-PACKAGE")
        name = ET.SubElement(wrapper, "SHORT-NAME")
        name.text = "P"
        for child in list(package)[1:]:
            wrapper.append(child)

        data = ET.tostring(root, encoding="UTF-8")
        validator = ARXMLValidator.for_document(data)
        assert validator is not None, "bundled R23-11 schema not detected"
        assert [f"line {e.line} col {e.column}: {e.message}" for e in validator.validate_bytes(data)] == []


class TestUriStringLeaf:
    def test_writes_concrete_type_and_t(self):
        value = UriString()
        value.setValue("https://example.com/resource")
        value.timestamp = "2026-10-15T00:00:00Z"

        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalUriString(element, "URI", value)

        written = element.find("URI")
        assert written is not None
        assert written.text == "https://example.com/resource"
        assert written.attrib["T"] == "2026-10-15T00:00:00Z"

    def test_writes_ldap_url_value(self):
        """The LDAP-URL of ACL-ROLE (XSD l.1288) is one of the ten element-form consumers of AR:URI-STRING."""
        value = UriString().setValue("ldap://example.com/Role")

        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalUriString(element, "LDAP-URL", value)

        written = element.find("LDAP-URL")
        assert written is not None
        assert written.text == "ldap://example.com/Role"

    def test_none_emits_nothing(self):
        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalUriString(element, "URI", None)

        assert element.find("URI") is None
