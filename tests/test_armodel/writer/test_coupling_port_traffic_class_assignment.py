"""Writer/reader round-trip tests for CouplingPortTrafficClassAssignment (Table 3.75, p.128).

CouplingPortTrafficClassAssignment is an inline Referrable value type consumed by
CouplingPortDetails.ethernetTrafficClassAssignments (serialized as
ETHERNET-TRAFFIC-CLASS-ASSIGNMENTS/COUPLING-PORT-TRAFFIC-CLASS-ASSIGNMENT). It carries
the attributes priority (0..8, PositiveInteger) and trafficClass (0..1, PositiveInteger).
"""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    CouplingPortDetails,
    CouplingPortTrafficClassAssignment,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


def _serialize_and_wrap(parent: ET.Element) -> ET.Element:
    inner = ET.tostring(parent).decode("utf-8")
    root = ET.fromstring(f"<AUTOSAR xmlns='{NS}'>{inner}</AUTOSAR>")
    return root[0]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser()


def _new_assignment(short_name="TA1", priorities=(1, 2), traffic_class=3):
    details = CouplingPortDetails()
    assignment = CouplingPortTrafficClassAssignment(details, short_name)
    for p in priorities:
        priority = PositiveInteger()
        priority.setValue(str(p))
        assignment.addPriority(priority)
    tc = PositiveInteger()
    tc.setValue(str(traffic_class))
    assignment.setTrafficClass(tc)
    return details, assignment


class TestWriteCouplingPortTrafficClassAssignment:
    def test_write_all_fields(self, writer):
        details, assignment = _new_assignment()
        details.setEthernetTrafficClassAssignments([assignment])
        parent = ET.Element("PARENT")
        writer.setCouplingPortDetails(parent, "COUPLING-PORT-DETAILS", details)
        details_element = parent.find("COUPLING-PORT-DETAILS")
        assert details_element is not None
        wrapper = details_element.find("ETHERNET-TRAFFIC-CLASS-ASSIGNMENTS")
        assert wrapper is not None
        items = wrapper.findall("COUPLING-PORT-TRAFFIC-CLASS-ASSIGNMENT")
        assert len(items) == 1
        item = items[0]
        assert item.find("SHORT-NAME").text == "TA1"
        priorities = item.findall("PRIORITY")
        assert [int(p.text) for p in priorities] == [1, 2]
        assert item.find("TRAFFIC-CLASS").text == "3"

    def test_write_empty_omits_wrapper(self, writer):
        details = CouplingPortDetails()
        parent = ET.Element("PARENT")
        writer.setCouplingPortDetails(parent, "COUPLING-PORT-DETAILS", details)
        details_element = parent.find("COUPLING-PORT-DETAILS")
        assert details_element is not None
        assert details_element.find("ETHERNET-TRAFFIC-CLASS-ASSIGNMENTS") is None


class TestCouplingPortTrafficClassAssignmentRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, parser):
        details, assignment = _new_assignment()
        details.setEthernetTrafficClassAssignments([assignment])
        parent = ET.Element("PARENT")
        writer.setCouplingPortDetails(parent, "COUPLING-PORT-DETAILS", details)
        details_element = _serialize_and_wrap(parent)
        parsed = parser.getCouplingPortDetails(details_element, "COUPLING-PORT-DETAILS")
        assignments = parsed.getEthernetTrafficClassAssignments()
        assert len(assignments) == 1
        result = assignments[0]
        assert isinstance(result, CouplingPortTrafficClassAssignment)
        assert result.getShortName() == "TA1"
        assert [p.getValue() for p in result.getPriorities()] == [1, 2]
        assert result.getTrafficClass().getValue() == 3

    def test_reader_empty_fields(self, writer, parser):
        parent = ET.Element("{%s}PARENT" % NS)
        ET.SubElement(parent, "{%s}COUPLING-PORT-DETAILS" % NS)
        parsed = parser.getCouplingPortDetails(parent, "COUPLING-PORT-DETAILS")
        assert parsed.getEthernetTrafficClassAssignments() == []
