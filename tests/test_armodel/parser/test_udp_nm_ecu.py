"""Parser round-trip tests for UdpNmEcu (Table 6.316, p.688; legacy attr R4.3.1 Table 6.238, p.431)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import NmEcu, UdpNmEcu
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


NM_ECU_XML = (
    "<NM-ECU xmlns='%(ns)s'>"
    "<SHORT-NAME>NmEcu1</SHORT-NAME>"
    "<BUS-DEPENDENT-NM-ECUS>"
    "<UDP-NM-ECU>"
    "<NM-SYNCHRONIZATION-POINT-ENABLED>true</NM-SYNCHRONIZATION-POINT-ENABLED>"
    "</UDP-NM-ECU>"
    "</BUS-DEPENDENT-NM-ECUS>"
    "</NM-ECU>" % {"ns": NS}
)


class TestParseUdpNmEcu:
    def _parse_ecus(self, xml):
        root = ET.fromstring(xml)
        nm_ecu = NmEcu(MockParent(), "NmEcu1")
        ARXMLParser().readBusDependentNmEcus(root, nm_ecu)
        return nm_ecu.getBusDependentNmEcus()

    def test_parse_legacy_attribute(self):
        dependent = self._parse_ecus(NM_ECU_XML)
        assert len(dependent) == 1
        ecu = dependent[0]
        assert isinstance(ecu, UdpNmEcu)
        assert ecu.getNmSynchronizationPointEnabled().getValue() is True

    def test_parse_empty_udp_nm_ecu(self):
        xml = "<NM-ECU xmlns='%s'>" "<SHORT-NAME>NmEcu1</SHORT-NAME>" "<BUS-DEPENDENT-NM-ECUS><UDP-NM-ECU></UDP-NM-ECU></BUS-DEPENDENT-NM-ECUS>" "</NM-ECU>" % NS
        dependent = self._parse_ecus(xml)
        assert len(dependent) == 1
        assert dependent[0].getNmSynchronizationPointEnabled() is None
