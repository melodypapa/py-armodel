import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import NmEcu
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


def _ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _time(value):
    time_value = TimeValue()
    time_value.setValue(value)
    return time_value


def _new_ecu():
    ecu = NmEcu(MockParent(), "NmEcu")
    ecu.setEcuInstanceRef(_ref("ECU-INSTANCE", "/Topology/Ecu1"))
    ecu.setNmBusSynchronizationEnabled(_bool(True))
    ecu.setNmComControlEnabled(_bool(False))
    ecu.setNmCycletimeMainFunction(_time("0.05"))
    ecu.setNmPduRxIndicationEnabled(_bool(True))
    ecu.setNmRemoteSleepIndEnabled(_bool(False))
    ecu.setNmStateChangeIndEnabled(_bool(True))
    ecu.setNmUserDataEnabled(_bool(True))
    return ecu


_SPEC_ELEMENT_ORDER = [
    "ECU-INSTANCE-REF",
    "NM-BUS-SYNCHRONIZATION-ENABLED",
    "NM-COM-CONTROL-ENABLED",
    "NM-CYCLETIME-MAIN-FUNCTION",
    "NM-PDU-RX-INDICATION-ENABLED",
    "NM-REMOTE-SLEEP-IND-ENABLED",
    "NM-STATE-CHANGE-IND-ENABLED",
    "NM-USER-DATA-ENABLED",
]


class TestWriteNmEcu:
    def test_write_nm_ecu_element_order(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeNmEcu(parent, _new_ecu())
        nm_ecu_element = parent.find("NM-ECU")
        tags = [child.tag for child in nm_ecu_element if child.tag != "SHORT-NAME"]
        assert tags == _SPEC_ELEMENT_ORDER
        assert nm_ecu_element.find("NM-NODE-DETECTION-ENABLED") is None
        assert nm_ecu_element.find("NM-NODE-ID-ENABLED") is None
        assert nm_ecu_element.find("NM-REPEAT-MSG-IND-ENABLED") is None

    def test_write_nm_ecu_round_trip_field_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeNmEcu(parent, _new_ecu())
        parent.set("xmlns", NS)
        root = ET.fromstring(ET.tostring(parent, encoding="unicode")).find("{%s}NM-ECU" % NS)
        ecu = NmEcu(MockParent(), "NmEcu")
        ARXMLParser().readNmEcu(root, ecu)
        assert ecu.getEcuInstanceRef().getValue() == "/Topology/Ecu1"
        assert ecu.getNmBusSynchronizationEnabled().getValue() is True
        assert ecu.getNmComControlEnabled().getValue() is False
        assert ecu.getNmCycletimeMainFunction().getValue() == 0.05
        assert ecu.getNmPduRxIndicationEnabled().getValue() is True
        assert ecu.getNmRemoteSleepIndEnabled().getValue() is False
        assert ecu.getNmStateChangeIndEnabled().getValue() is True
        assert ecu.getNmUserDataEnabled().getValue() is True
