"""Writer round-trip tests for GeneralPurposeConnection (Table 6.58, p.388).

Top-level ARElement dispatched by writeARPackageElement (isinstance chain);
XSD child order PDU-TRIGGERING-REFS (GENERAL-PURPOSE-CONNECTION group,
AUTOSAR_00052.xsd l.63807). The PDU-TRIGGERING-REFS wrapper is emitted only
when the list is non-empty, one PDU-TRIGGERING-REF per entry.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage, GeneralPurposeConnection
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DateTime,
    RefType,
    String,
)
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_CHILD_ORDER = [
    "PDU-TRIGGERING-REFS",
]

UUID_VALUE = "3c2b1a0f-9e8d-4c7b-a6f5-1e2d3c4b5a69"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _populate(connection: GeneralPurposeConnection):
    connection.addPduTriggeringRef(RefType().setDest("PDU-TRIGGERING-SUBTYPES-ENUM").setValue("/PduTriggerings/RequestTriggering"))
    connection.addPduTriggeringRef(RefType().setDest("PDU-TRIGGERING-SUBTYPES-ENUM").setValue("/PduTriggerings/ResponseTriggering"))


def _write_ar_package_element(connection: GeneralPurposeConnection) -> ET.Element:
    parent = ET.Element("ELEMENTS")
    ARXMLWriter().writeARPackageElement(parent, connection)
    return parent


def _with_ns(parent: ET.Element) -> ET.Element:
    return ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<AR-PACKAGE>", "<AR-PACKAGE xmlns='%s'>" % NS, 1))


class TestGeneralPurposeConnectionWriter:
    def test_write_dispatch_creates_correct_tag(self):
        connection = AUTOSAR.getInstance().createARPackage("Connections").createGeneralPurposeConnection("Connection1")
        parent = _write_ar_package_element(connection)

        assert len(parent) == 1
        child = parent.find("GENERAL-PURPOSE-CONNECTION")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Connection1"

    def test_write_field_values_and_xsd_element_order(self):
        connection = AUTOSAR.getInstance().createARPackage("Connections").createGeneralPurposeConnection("Connection1")
        _populate(connection)

        child = _write_ar_package_element(connection).find("GENERAL-PURPOSE-CONNECTION")
        refs_tag = child.find("PDU-TRIGGERING-REFS")
        assert refs_tag is not None
        refs = refs_tag.findall("PDU-TRIGGERING-REF")
        assert len(refs) == 2
        assert refs[0].attrib["DEST"] == "PDU-TRIGGERING-SUBTYPES-ENUM"
        assert refs[0].text == "/PduTriggerings/RequestTriggering"
        assert refs[1].attrib["DEST"] == "PDU-TRIGGERING-SUBTYPES-ENUM"
        assert refs[1].text == "/PduTriggerings/ResponseTriggering"
        children = [c.tag for c in child]
        assert children == ["SHORT-NAME"] + XSD_CHILD_ORDER

    def test_write_empty_omits_wrapper(self):
        pkg = AUTOSAR.getInstance().createARPackage("Connections")
        pkg.createGeneralPurposeConnection("Empty")
        child = _write_ar_package_element(pkg.getReferrableElement("Empty", GeneralPurposeConnection)).find("GENERAL-PURPOSE-CONNECTION")

        assert child is not None
        for tag in XSD_CHILD_ORDER:
            assert child.find(tag) is None, tag

    def test_create_duplicate_returns_existing(self):
        pkg = AUTOSAR.getInstance().createARPackage("Connections")
        first = pkg.createGeneralPurposeConnection("Connection1")
        second = pkg.createGeneralPurposeConnection("Connection1")
        assert first is second
        assert isinstance(first, GeneralPurposeConnection)

    def test_write_then_reparse_round_trip(self):
        from armodel.parser.arxml_parser import ARXMLParser

        pkg = AUTOSAR.getInstance().createARPackage("Connections")
        connection = pkg.createGeneralPurposeConnection("Connection1")
        _populate(connection)

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElements(parent, pkg)

        reloaded = ARPackage(parent=AUTOSAR.getInstance(), short_name="Connections")
        ARXMLParser().readARPackageElements(_with_ns(parent), reloaded)

        re_connection = reloaded.getReferrableElement("Connection1", GeneralPurposeConnection)
        assert re_connection is not None
        assert isinstance(re_connection, GeneralPurposeConnection)
        refs = re_connection.getPduTriggeringRefs()
        assert len(refs) == 2
        assert refs[0].getDest() == "PDU-TRIGGERING-SUBTYPES-ENUM"
        assert refs[0].getValue() == "/PduTriggerings/RequestTriggering"
        assert refs[1].getDest() == "PDU-TRIGGERING-SUBTYPES-ENUM"
        assert refs[1].getValue() == "/PduTriggerings/ResponseTriggering"

    def test_round_trip_base_level_attributes(self):
        from armodel.parser.arxml_parser import ARXMLParser

        pkg = AUTOSAR.getInstance().createARPackage("Connections")
        connection = pkg.createGeneralPurposeConnection("Connection1")
        connection.setUuid(String().setValue(UUID_VALUE))
        connection.setChecksum(String().setValue("7"))
        connection.setTimestamp(DateTime().setValue("2025-04-04T00:00:00Z"))
        connection.setCategory("CONN")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElements(parent, pkg)
        node = _with_ns(parent).find("{%s}ELEMENTS" % NS).find("{%s}GENERAL-PURPOSE-CONNECTION" % NS)
        assert node.attrib["UUID"] == UUID_VALUE
        assert node.attrib["S"] == "7"
        assert node.attrib["T"] == "2025-04-04T00:00:00Z"
        assert node.find("{%s}CATEGORY" % NS).text == "CONN"

        reloaded = ARPackage(parent=AUTOSAR.getInstance(), short_name="Connections")
        ARXMLParser().readARPackageElements(_with_ns(parent), reloaded)
        re_connection = reloaded.getReferrableElement("Connection1", GeneralPurposeConnection)
        assert re_connection.getUuid().getValue() == UUID_VALUE
        assert re_connection.getChecksum().getValue() == "7"
        assert re_connection.getTimestamp().getValue() == "2025-04-04T00:00:00Z"
        assert re_connection.getCategory().getValue() == "CONN"

    def test_round_trip_empty(self):
        from armodel.parser.arxml_parser import ARXMLParser

        pkg = AUTOSAR.getInstance().createARPackage("Connections")
        pkg.createGeneralPurposeConnection("Connection1")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElements(parent, pkg)

        reloaded = ARPackage(parent=AUTOSAR.getInstance(), short_name="Connections")
        ARXMLParser().readARPackageElements(_with_ns(parent), reloaded)

        re_connection = reloaded.getReferrableElement("Connection1", GeneralPurposeConnection)
        assert re_connection is not None
        assert re_connection.getPduTriggeringRefs() == []
