"""Parser round-trip tests for FlexrayNmEcu (Table 6.307, p.679)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import FlexrayNmEcu, NmEcu
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


BUS_DEPENDENT_XML = (
    "<NM-ECU xmlns='%(ns)s'>"
    "<SHORT-NAME>NmEcu1</SHORT-NAME>"
    "<BUS-DEPENDENT-NM-ECUS>"
    "<FLEXRAY-NM-ECU>"
    "<NM-HW-VOTE-ENABLED>true</NM-HW-VOTE-ENABLED>"
    "<NM-MAIN-FUNCTION-ACROSS-FR-CYCLE>false</NM-MAIN-FUNCTION-ACROSS-FR-CYCLE>"
    "</FLEXRAY-NM-ECU>"
    "</BUS-DEPENDENT-NM-ECUS>"
    "</NM-ECU>" % {"ns": NS}
)


class TestParseFlexrayNmEcu:
    def _parse_ecus(self, xml):
        root = ET.fromstring(xml)
        nm_ecu = NmEcu(MockParent(), "NmEcu1")
        ARXMLParser().readBusDependentNmEcus(root, nm_ecu)
        return nm_ecu.getBusDependentNmEcus()

    def test_parse_field_values(self):
        dependent = self._parse_ecus(BUS_DEPENDENT_XML)
        assert len(dependent) == 1
        ecu = dependent[0]
        assert isinstance(ecu, FlexrayNmEcu)
        assert ecu.getNmHwVoteEnabled().getValue() is True
        assert ecu.getNmMainFunctionAcrossFrCycle().getValue() is False

    def test_parse_empty_flexray_nm_ecu(self):
        xml = (
            "<NM-ECU xmlns='%s'>"
            "<SHORT-NAME>NmEcu1</SHORT-NAME>"
            "<BUS-DEPENDENT-NM-ECUS><FLEXRAY-NM-ECU></FLEXRAY-NM-ECU></BUS-DEPENDENT-NM-ECUS>"
            "</NM-ECU>" % NS
        )
        dependent = self._parse_ecus(xml)
        assert len(dependent) == 1
        assert isinstance(dependent[0], FlexrayNmEcu)
        assert dependent[0].getNmHwVoteEnabled() is None
