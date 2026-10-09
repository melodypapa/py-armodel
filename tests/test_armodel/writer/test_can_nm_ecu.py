"""Writer round-trip tests for CanNmEcu (Table 6.312, p.683).

R23-11 table has zero attribute rows (all members inherited via
BusspecificNmEcu/ARObject); the S/T ARObject level (Rule 0025) is emitted by
writeCanNmEcu and pinned here through the BUS-DEPENDENT-NM-ECUS dispatch.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import CanNmEcu, NmEcu
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


def _new_ecu():
    ecu = CanNmEcu()
    checksum = String()
    checksum.setValue("42")
    ecu.setChecksum(checksum)
    timestamp = DateTime()
    timestamp.setValue("2023-01-01T00:00:00+02:00")
    ecu.setTimestamp(timestamp)
    return ecu


class TestWriteCanNmEcu:
    def test_write_emits_can_nm_ecu_element(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeCanNmEcu(parent, CanNmEcu())
        assert parent.find("CAN-NM-ECU") is not None

    def test_write_base_s_t_attributes(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeCanNmEcu(parent, _new_ecu())
        node = parent.find("CAN-NM-ECU")
        assert node.attrib["S"] == "42"
        assert node.attrib["T"] == "2023-01-01T00:00:00+02:00"

    def test_write_dispatch_via_bus_dependent_nm_ecus(self):
        nm_ecu = NmEcu(MockParent(), "NmEcu1")
        nm_ecu.addBusDependentNmEcu(_new_ecu())
        parent = ET.Element("PARENT")
        ARXMLWriter().writeBusDependentNmEcus(parent, nm_ecu)
        assert parent.find("BUS-DEPENDENT-NM-ECUS/CAN-NM-ECU") is not None

    def test_round_trip_preserves_base_s_t(self):
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
        assert isinstance(parsed, CanNmEcu)
        assert parsed.getChecksum().getValue() == "42"
        assert parsed.getTimestamp().getValue() == "2023-01-01T00:00:00+02:00"
