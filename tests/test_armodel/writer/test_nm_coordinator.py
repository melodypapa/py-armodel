import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Integer, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import NmCoordinator
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _bool(value):
    boolean = Boolean()
    boolean.setValue(value)
    return boolean


def _integer(value):
    integer = Integer()
    integer.setValue(value)
    return integer


def _time(value):
    time_value = TimeValue()
    time_value.setValue(value)
    return time_value


def _ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _new_coordinator():
    coordinator = NmCoordinator()
    coordinator.setIndex(_integer(1))
    coordinator.setNmCoordSyncSupport(_bool(True))
    coordinator.setNmGlobalCoordinatorTime(_time("2.5"))
    coordinator.addNmNodeRef(_ref("NM-NODE", "/Clusters/Can1/node"))
    return coordinator


class TestWriteNmCoordinator:
    def test_write_nm_coordinator_element_order(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeNmCoordinator(parent, _new_coordinator())
        coordinator_element = parent.find("NM-COORDINATOR")
        tags = [child.tag for child in coordinator_element]
        assert tags == ["INDEX", "NM-COORD-SYNC-SUPPORT", "NM-GLOBAL-COORDINATOR-TIME", "NM-NODE-REFS"]
        assert coordinator_element.find("NM-NODE-REFS/NM-NODE-REF").text == "/Clusters/Can1/node"
        assert coordinator_element.find("NM-NODE-REFS/NM-NODE-REF").attrib["DEST"] == "NM-NODE"

    def test_write_nm_coordinator_empty(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeNmCoordinator(parent, NmCoordinator())
        coordinator_element = parent.find("NM-COORDINATOR")
        assert list(coordinator_element) == []

    def test_write_nm_coordinator_round_trip_field_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeNmCoordinator(parent, _new_coordinator())
        wrapper = ET.Element("WRAPPER")
        wrapper.append(parent.find("NM-COORDINATOR"))
        wrapper.set("xmlns", NS)
        coordinator_element = ET.fromstring(ET.tostring(wrapper, encoding="unicode"))[0]
        parsed = NmCoordinator()
        ARXMLParser().readNmCoordinator(coordinator_element, parsed)
        assert parsed.getIndex().getValue() == 1
        assert parsed.getNmCoordSyncSupport().getValue() is True
        assert parsed.getNmGlobalCoordinatorTime().getValue() == 2.5
        nodes = parsed.getNmNodeRefs()
        assert len(nodes) == 1
        assert nodes[0].getDest() == "NM-NODE"
        assert nodes[0].getValue() == "/Clusters/Can1/node"
