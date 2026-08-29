"""Writer/reader round-trip tests for CouplingPortDetails (Table 3.63, p.122)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    CouplingPortDetails,
    CouplingPortFifo,
    CouplingPortRatePolicy,
    CouplingPortRatePolicyActionEnum,
    CouplingPortScheduler,
    CouplingPortTrafficClassAssignment,
    GlobalTimeCouplingPortProps,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    return ARXMLParser()


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _new_details():
    details = CouplingPortDetails()
    fifo = details.createCouplingPortFifo("Fifo1")
    fifo.setMinimumFifoLength(_pos_int("1522"))
    details.createCouplingPortScheduler("Sched1")
    regen = details.createEthernetPriorityRegeneration("Regen1")
    regen.setIngressPriority(_pos_int("3"))
    regen.setRegeneratedPriority(_pos_int("7"))
    assignment = CouplingPortTrafficClassAssignment(details, "Assign1")
    assignment.setTrafficClass(_pos_int("2"))
    details.addEthernetTrafficClassAssignment(assignment)
    ref = _ref("/Ecu/CouplingPort/Sched9")
    details.setLastEgressSchedulerRef(ref)
    return details


def _pos_int(text):
    val = PositiveInteger()
    val.setValue(text)
    return val


def _ref(value):
    ref = RefType()
    ref.setValue(value)
    return ref


class TestWriteCouplingPortDetails:
    def test_write_all_fields(self, writer):
        parent = ET.Element("PARENT")
        writer.setCouplingPortDetails(parent, "COUPLING-PORT-DETAILS", _new_details())
        node = parent.find("COUPLING-PORT-DETAILS")
        assert node is not None
        elements = node.findall("COUPLING-PORT-STRUCTURAL-ELEMENTS/*")
        assert len(elements) == 2
        assert node.find("ETHERNET-PRIORITY-REGENERATIONS/ETHERNET-PRIORITY-REGENERATION/INGRESS-PRIORITY").text == "3"
        assignments = node.findall("ETHERNET-TRAFFIC-CLASS-ASSIGNMENTS/COUPLING-PORT-TRAFFIC-CLASS-ASSIGNMENT")
        assert len(assignments) == 1
        assert assignments[0].find("TRAFFIC-CLASS").text == "2"
        assert node.find("LAST-EGRESS-SCHEDULER-REF").text == "/Ecu/CouplingPort/Sched9"


class TestCouplingPortDetailsRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, parser):
        parent = ET.Element("PARENT")
        writer.setCouplingPortDetails(parent, "COUPLING-PORT-DETAILS", _new_details())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))
        parsed = parser.getCouplingPortDetails(root[0], "COUPLING-PORT-DETAILS")

        assert isinstance(parsed, CouplingPortDetails)
        elements = parsed.getCouplingPortStructuralElements()
        assert len(elements) == 2
        assert isinstance(elements[0], CouplingPortFifo)
        assert isinstance(elements[1], CouplingPortScheduler)
        regens = parsed.getEthernetPriorityRegenerations()
        assert len(regens) == 1
        assert regens[0].getIngressPriority().getValue() == 3
        assert regens[0].getRegeneratedPriority().getValue() == 7
        assignments = parsed.getEthernetTrafficClassAssignments()
        assert len(assignments) == 1
        assert assignments[0].getTrafficClass().getValue() == 2
        assert parsed.getLastEgressSchedulerRef().getValue() == "/Ecu/CouplingPort/Sched9"

    def test_reader_empty_fields(self, parser):
        parent = ET.fromstring("<PARENT xmlns='%s'><COUPLING-PORT-DETAILS/></PARENT>" % NS)
        parsed = parser.getCouplingPortDetails(parent, "COUPLING-PORT-DETAILS")
        assert isinstance(parsed, CouplingPortDetails)
        assert parsed.getCouplingPortStructuralElements() == []
        assert parsed.getEthernetTrafficClassAssignments() == []
        assert parsed.getLastEgressSchedulerRef() is None


class TestCouplingPortDetailsElementOrder:
    def test_write_child_element_order_matches_xsd(self, writer):
        details = _new_details()
        details.setGlobalTimeProps(GlobalTimeCouplingPortProps())
        rate_policy = CouplingPortRatePolicy()
        rate_policy.setPolicyAction(CouplingPortRatePolicyActionEnum().setValue(CouplingPortRatePolicyActionEnum.DROP_FRAME))
        details.addRatePolicy(rate_policy)

        parent = ET.Element("PARENT")
        writer.setCouplingPortDetails(parent, "COUPLING-PORT-DETAILS", details)
        node = parent.find("COUPLING-PORT-DETAILS")
        # AUTOSAR_00052.xsd group COUPLING-PORT-DETAILS sequence
        assert [child.tag for child in node] == [
            "COUPLING-PORT-STRUCTURAL-ELEMENTS",
            "ETHERNET-PRIORITY-REGENERATIONS",
            "ETHERNET-TRAFFIC-CLASS-ASSIGNMENTS",
            "GLOBAL-TIME-PROPS",
            "LAST-EGRESS-SCHEDULER-REF",
            "RATE-POLICYS",
        ]
