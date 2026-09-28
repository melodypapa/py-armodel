import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import CanNmEcu, NmEcu
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


def _parse_nm_ecu(xml):
    root = ET.fromstring(xml)
    ecu = NmEcu(MockParent(), "NmEcu")
    ARXMLParser().readNmEcu(root, ecu)
    return ecu


class TestParseNmEcu:
    def test_parse_nm_ecu_field_values(self):
        xml = (
            "<NmEcu xmlns='%s'>"
            "<ECU-INSTANCE-REF DEST='ECU-INSTANCE'>/Topology/Ecu1</ECU-INSTANCE-REF>"
            "<NM-BUS-SYNCHRONIZATION-ENABLED>true</NM-BUS-SYNCHRONIZATION-ENABLED>"
            "<NM-COM-CONTROL-ENABLED>false</NM-COM-CONTROL-ENABLED>"
            "<NM-CYCLETIME-MAIN-FUNCTION>0.05</NM-CYCLETIME-MAIN-FUNCTION>"
            "<NM-PDU-RX-INDICATION-ENABLED>true</NM-PDU-RX-INDICATION-ENABLED>"
            "<NM-REMOTE-SLEEP-IND-ENABLED>false</NM-REMOTE-SLEEP-IND-ENABLED>"
            "<NM-STATE-CHANGE-IND-ENABLED>true</NM-STATE-CHANGE-IND-ENABLED>"
            "<NM-USER-DATA-ENABLED>false</NM-USER-DATA-ENABLED>"
            "</NmEcu>" % NS
        )
        ecu = _parse_nm_ecu(xml)
        assert ecu.getEcuInstanceRef().getDest() == "ECU-INSTANCE"
        assert ecu.getEcuInstanceRef().getValue() == "/Topology/Ecu1"
        assert ecu.getNmBusSynchronizationEnabled().getValue() is True
        assert ecu.getNmComControlEnabled().getValue() is False
        assert ecu.getNmCycletimeMainFunction().getValue() == 0.05
        assert ecu.getNmPduRxIndicationEnabled().getValue() is True
        assert ecu.getNmRemoteSleepIndEnabled().getValue() is False
        assert ecu.getNmStateChangeIndEnabled().getValue() is True
        assert ecu.getNmUserDataEnabled().getValue() is False
        assert ecu.getBusDependentNmEcus() == []

    def test_parse_nm_ecu_bus_dependent_nm_ecus(self):
        xml = "<NmEcu xmlns='%s'><BUS-DEPENDENT-NM-ECUS><CAN-NM-ECU/></BUS-DEPENDENT-NM-ECUS></NmEcu>" % NS
        ecu = _parse_nm_ecu(xml)
        assert len(ecu.getBusDependentNmEcus()) == 1
        assert isinstance(ecu.getBusDependentNmEcus()[0], CanNmEcu)

    def test_parse_nm_ecu_ignores_cluster_level_attributes(self):
        xml = "<NmEcu xmlns='%s'><NM-NODE-DETECTION-ENABLED>true</NM-NODE-DETECTION-ENABLED></NmEcu>" % NS
        ecu = _parse_nm_ecu(xml)
        assert not hasattr(ecu, "nmNodeDetectionEnabled")
