import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Identifier, Integer, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import NmCoordinator, NmEcu
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


def _integer(value):
    integer = Integer()
    integer.setValue(value)
    return integer


def _vp(label):
    vp = VariationPoint()
    vp.setShortLabel(Identifier().setValue(label))
    return vp


def _new_coordinator():
    coordinator = NmCoordinator()
    coordinator.setIndex(_integer(1))
    coordinator.setNmCoordSyncSupport(_bool(True))
    coordinator.setNmGlobalCoordinatorTime(_time("2.5"))
    coordinator.addNmNodeRef(_ref("NM-NODE", "/Clusters/Can1/node"))
    return coordinator


def _new_ecu():
    ecu = NmEcu(MockParent(), "NmEcu")
    ecu.setEcuInstanceRef(_ref("ECU-INSTANCE", "/Topology/Ecu1"))
    ecu.setNmBusSynchronizationEnabled(_bool(True))
    ecu.setNmComControlEnabled(_bool(False))
    ecu.setNmCoordinator(_new_coordinator())
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
    "NM-COORDINATOR",
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
        coordinator = ecu.getNmCoordinator()
        assert isinstance(coordinator, NmCoordinator)
        assert coordinator.getIndex().getValue() == 1
        assert coordinator.getNmCoordSyncSupport().getValue() is True
        assert coordinator.getNmGlobalCoordinatorTime().getValue() == 2.5
        nodes = coordinator.getNmNodeRefs()
        assert len(nodes) == 1
        assert nodes[0].getValue() == "/Clusters/Can1/node"

    def test_write_nm_ecu_writes_variation_point_last(self):
        ecu = _new_ecu()
        ecu.setVariationPoint(_vp("VP1"))
        parent = ET.Element("PARENT")
        ARXMLWriter().writeNmEcu(parent, ecu)
        nm_ecu_element = parent.find("NM-ECU")
        tags = [child.tag for child in nm_ecu_element if child.tag != "SHORT-NAME"]
        assert tags == _SPEC_ELEMENT_ORDER + ["VARIATION-POINT"]
        assert nm_ecu_element.find("VARIATION-POINT/SHORT-LABEL").text == "VP1"

    def test_write_nm_ecu_round_trips_variation_point(self):
        ecu = _new_ecu()
        ecu.setVariationPoint(_vp("VP1"))
        parent = ET.Element("PARENT")
        ARXMLWriter().writeNmEcu(parent, ecu)
        parent.set("xmlns", NS)
        root = ET.fromstring(ET.tostring(parent, encoding="unicode")).find("{%s}NM-ECU" % NS)
        parsed = NmEcu(MockParent(), "NmEcu")
        ARXMLParser().readNmEcu(root, parsed)
        assert parsed.getVariationPoint() is not None
        assert parsed.getVariationPoint().getShortLabel().getValue() == "VP1"
