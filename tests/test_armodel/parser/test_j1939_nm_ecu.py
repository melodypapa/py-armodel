"""Parser round-trip tests for J1939NmEcu (Table 6.323, p.694)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import J1939NmEcu, NmEcu
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


class TestParseJ1939NmEcu:
    def _parse_ecus(self, xml):
        root = ET.fromstring(xml)
        nm_ecu = NmEcu(MockParent(), "NmEcu1")
        ARXMLParser().readBusDependentNmEcus(root, nm_ecu)
        return nm_ecu.getBusDependentNmEcus()

    def test_parse_j1939_nm_ecu(self):
        xml = "<NM-ECU xmlns='%s'>" "<SHORT-NAME>NmEcu1</SHORT-NAME>" "<BUS-DEPENDENT-NM-ECUS><J-1939-NM-ECU></J-1939-NM-ECU></BUS-DEPENDENT-NM-ECUS>" "</NM-ECU>" % NS
        dependent = self._parse_ecus(xml)
        assert len(dependent) == 1
        assert isinstance(dependent[0], J1939NmEcu)
