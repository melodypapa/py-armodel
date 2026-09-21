"""Writer round-trip tests for CouplingPortScheduler (Table 3.65, p.123).

CouplingPortScheduler is a CouplingPortStructuralElement value type aggregated by
CouplingPortDetails.couplingPortStructuralElement. XML element order per XSD group
COUPLING-PORT-SCHEDULER: PORT-SCHEDULER, PREDECESSOR-REFS.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import CouplingPortScheduler, EthernetCouplingPortSchedulerEnum
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


def _new_scheduler():
    scheduler = CouplingPortScheduler(MockParent(), "Sched1")
    value = EthernetCouplingPortSchedulerEnum()
    value.setValue("WEIGHTED-ROUND-ROBIN")
    scheduler.setPortScheduler(value)
    ref1 = RefType()
    ref1.setDest("COUPLING-PORT-FIFO")
    ref1.setValue("/Fifos/Fifo1")
    ref2 = RefType()
    ref2.setDest("COUPLING-PORT-SCHEDULER")
    ref2.setValue("/Schedulers/Sched0")
    scheduler.addPredecessorRef(ref1)
    scheduler.addPredecessorRef(ref2)
    return scheduler


class TestWriteCouplingPortScheduler:
    def test_write_all_fields(self, writer):
        parent = ET.Element("PARENT")
        writer.writeCouplingPortScheduler(parent, _new_scheduler())
        node = parent.find("COUPLING-PORT-SCHEDULER")
        assert node is not None
        assert node.find("SHORT-NAME").text == "Sched1"
        assert node.find("PORT-SCHEDULER").text == "WEIGHTED-ROUND-ROBIN"
        refs_wrapper = node.find("PREDECESSOR-REFS")
        assert refs_wrapper is not None
        refs = refs_wrapper.findall("PREDECESSOR-REF")
        assert len(refs) == 2
        assert refs[0].text == "/Fifos/Fifo1"
        assert refs[0].attrib["DEST"] == "COUPLING-PORT-FIFO"
        assert refs[1].text == "/Schedulers/Sched0"
        assert refs[1].attrib["DEST"] == "COUPLING-PORT-SCHEDULER"
        children = [child.tag for child in node]
        assert children.index("PORT-SCHEDULER") < children.index("PREDECESSOR-REFS")

    def test_write_empty_fields_omits_optional_tags(self, writer):
        parent = ET.Element("PARENT")
        writer.writeCouplingPortScheduler(parent, CouplingPortScheduler(MockParent(), "Empty"))
        node = parent.find("COUPLING-PORT-SCHEDULER")
        assert node is not None
        assert node.find("PORT-SCHEDULER") is None
        assert node.find("PREDECESSOR-REFS") is None


class TestCouplingPortSchedulerRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, parser):
        parent = ET.Element("PARENT")
        writer.writeCouplingPortScheduler(parent, _new_scheduler())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))
        parsed = CouplingPortScheduler(MockParent(), "Sched1")
        parser.readCouplingPortScheduler(root[0][0], parsed)
        assert parsed.getShortName() == "Sched1"
        assert parsed.getPortScheduler() is not None
        assert parsed.getPortScheduler().getValue() == "WEIGHTED-ROUND-ROBIN"
        refs = parsed.getPredecessorRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/Fifos/Fifo1"
        assert refs[0].getDest() == "COUPLING-PORT-FIFO"
        assert refs[1].getValue() == "/Schedulers/Sched0"
        assert refs[1].getDest() == "COUPLING-PORT-SCHEDULER"

    def test_reader_empty_fields(self, parser):
        element = ET.fromstring("<COUPLING-PORT-SCHEDULER xmlns='%s'><SHORT-NAME>Empty</SHORT-NAME></COUPLING-PORT-SCHEDULER>" % NS)
        parsed = CouplingPortScheduler(MockParent(), "Empty")
        parser.readCouplingPortScheduler(element, parsed)
        assert parsed.getPortScheduler() is None
        assert parsed.getPredecessorRefs() == []
