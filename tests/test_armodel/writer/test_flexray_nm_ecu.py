"""Writer round-trip tests for FlexrayNmEcu (Table 6.307, p.679).

XML element order per XSD group FLEXRAY-NM-ECU (active elements):
NM-HW-VOTE-ENABLED, NM-MAIN-FUNCTION-ACROSS-FR-CYCLE. Coverage runs through
the BUS-DEPENDENT-NM-ECUS wrapper dispatch on NmEcu.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import FlexrayNmEcu, NmEcu
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _bool(value):
    boolean = Boolean()
    boolean.setValue(value)
    return boolean


def _new_ecu():
    ecu = FlexrayNmEcu()
    ecu.setNmHwVoteEnabled(_bool(True))
    ecu.setNmMainFunctionAcrossFrCycle(_bool(False))
    return ecu


class TestWriteFlexrayNmEcu:
    def test_write_all_fields_in_xsd_order(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeFlexrayNmEcu(parent, _new_ecu())
        node = parent.find("FLEXRAY-NM-ECU")
        assert node is not None
        assert [child.tag for child in node] == ["NM-HW-VOTE-ENABLED", "NM-MAIN-FUNCTION-ACROSS-FR-CYCLE"]

    def test_write_field_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeFlexrayNmEcu(parent, _new_ecu())
        node = parent.find("FLEXRAY-NM-ECU")
        assert node.find("NM-HW-VOTE-ENABLED").text == "true"
        assert node.find("NM-MAIN-FUNCTION-ACROSS-FR-CYCLE").text == "false"

    def test_write_dispatch_via_bus_dependent_nm_ecus(self):
        nm_ecu = NmEcu(MockParent(), "NmEcu1")
        nm_ecu.addBusDependentNmEcu(_new_ecu())
        parent = ET.Element("PARENT")
        ARXMLWriter().writeBusDependentNmEcus(parent, nm_ecu)
        assert parent.find("BUS-DEPENDENT-NM-ECUS/FLEXRAY-NM-ECU") is not None

    def test_round_trip_preserves_all_values(self):
        nm_ecu = NmEcu(MockParent(), "NmEcu1")
        nm_ecu.addBusDependentNmEcu(_new_ecu())
        parent = ET.Element("PARENT")
        ARXMLWriter().writeBusDependentNmEcus(parent, nm_ecu)
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))

        parsed_ecu = NmEcu(MockParent(), "NmEcu1")
        ARXMLParser().readBusDependentNmEcus(root[0], parsed_ecu)
        dependent = parsed_ecu.getBusDependentNmEcus()
        assert len(dependent) == 1
        parsed = dependent[0]
        assert isinstance(parsed, FlexrayNmEcu)
        assert parsed.getNmHwVoteEnabled().getValue() is True
        assert parsed.getNmMainFunctionAcrossFrCycle().getValue() is False
