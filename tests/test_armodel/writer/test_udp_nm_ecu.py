"""Writer round-trip tests for UdpNmEcu (Table 6.316, p.688).

R23-11 table has zero attribute rows; the legacy attribute
nmSynchronizationPointEnabled (R4.3.1 Table 6.238, p.431; element
NM-SYNCHRONIZATION-POINT-ENABLED, atp.Status=removed in R23-11 XSD) keeps full
reader/writer coverage per the combine rule. Coverage runs through the
BUS-DEPENDENT-NM-ECUS wrapper dispatch on NmEcu.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import NmEcu, UdpNmEcu
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
    ecu = UdpNmEcu()
    ecu.setNmSynchronizationPointEnabled(_bool(True))
    return ecu


class TestWriteUdpNmEcu:
    def test_write_legacy_attribute(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeUdpNmEcu(parent, _new_ecu())
        node = parent.find("UDP-NM-ECU")
        assert node is not None
        assert node.find("NM-SYNCHRONIZATION-POINT-ENABLED").text == "true"
        assert [child.tag for child in node] == ["NM-SYNCHRONIZATION-POINT-ENABLED"]

    def test_write_empty_ecu_omits_optional_tag(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeUdpNmEcu(parent, UdpNmEcu())
        node = parent.find("UDP-NM-ECU")
        assert node is not None
        assert len(list(node)) == 0

    def test_write_dispatch_via_bus_dependent_nm_ecus(self):
        nm_ecu = NmEcu(MockParent(), "NmEcu1")
        nm_ecu.addBusDependentNmEcu(_new_ecu())
        parent = ET.Element("PARENT")
        ARXMLWriter().writeBusDependentNmEcus(parent, nm_ecu)
        assert parent.find("BUS-DEPENDENT-NM-ECUS/UDP-NM-ECU") is not None

    def test_round_trip_preserves_value(self):
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
        assert isinstance(parsed, UdpNmEcu)
        assert parsed.getNmSynchronizationPointEnabled().getValue() is True
