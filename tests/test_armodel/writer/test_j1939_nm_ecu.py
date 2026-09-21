"""Writer round-trip tests for J1939NmEcu (Table 6.323, p.694).

J1939NmEcu has zero attribute rows (XSD group J-1939-NM-ECU is an empty
sequence), so it serializes as an empty element through the
BUS-DEPENDENT-NM-ECUS wrapper dispatch on NmEcu.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import J1939NmEcu, NmEcu
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


class TestWriteJ1939NmEcu:
    def test_write_empty_element(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeJ1939NmEcu(parent, J1939NmEcu())
        node = parent.find("J-1939-NM-ECU")
        assert node is not None
        assert len(list(node)) == 0

    def test_write_dispatch_via_bus_dependent_nm_ecus(self):
        nm_ecu = NmEcu(MockParent(), "NmEcu1")
        nm_ecu.addBusDependentNmEcu(J1939NmEcu())
        parent = ET.Element("PARENT")
        ARXMLWriter().writeBusDependentNmEcus(parent, nm_ecu)
        assert parent.find("BUS-DEPENDENT-NM-ECUS/J-1939-NM-ECU") is not None

    def test_round_trip_preserves_type(self):
        nm_ecu = NmEcu(MockParent(), "NmEcu1")
        nm_ecu.addBusDependentNmEcu(J1939NmEcu())
        parent = ET.Element("PARENT")
        ARXMLWriter().writeBusDependentNmEcus(parent, nm_ecu)
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))

        parsed_ecu = NmEcu(MockParent(), "NmEcu1")
        ARXMLParser().readBusDependentNmEcus(root[0], parsed_ecu)
        dependent = parsed_ecu.getBusDependentNmEcus()
        assert len(dependent) == 1
        assert isinstance(dependent[0], J1939NmEcu)
