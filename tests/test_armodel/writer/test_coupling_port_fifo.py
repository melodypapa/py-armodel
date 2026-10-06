"""Writer/reader round-trip tests for CouplingPortFifo (Table 3.68, p.124).

CouplingPortFifo is a CouplingPortStructuralElement value type aggregated by
CouplingPortDetails.couplingPortStructuralElement.
"""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import CouplingPortCreditBasedShaper, CouplingPortFifo
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


def _new_fifo():
    fifo = CouplingPortFifo(MockParent(), "Fifo1")
    fifo.setUuid(String().setValue("DCE:2fac1234-31f8-11b4-a222-08002b34c003"))
    fifo.addAssignedTrafficClass(PositiveInteger().setValue(3))
    fifo.addAssignedTrafficClass(PositiveInteger().setValue(5))
    fifo.setMinimumFifoLength(PositiveInteger().setValue(1522))
    cbs = CouplingPortCreditBasedShaper(fifo, "Cbs1")
    cbs.setIdleSlope(PositiveInteger().setValue(300))
    fifo.setShaper(cbs)
    return fifo


class TestWriteCouplingPortFifo:
    def test_write_all_fields(self, writer):
        parent = ET.Element("PARENT")
        writer.writeCouplingPortFifo(parent, _new_fifo())
        node = parent.find("COUPLING-PORT-FIFO")
        assert node is not None
        assert node.attrib.get("UUID") == "DCE:2fac1234-31f8-11b4-a222-08002b34c003"
        assert node.find("SHORT-NAME").text == "Fifo1"
        classes = node.findall("ASSIGNED-TRAFFIC-CLASSS/ASSIGNED-TRAFFIC-CLASS")
        assert len(classes) == 2
        assert classes[0].text == "3"
        assert classes[1].text == "5"
        assert node.find("MINIMUM-FIFO-LENGTH").text == "1522"
        assert node.find("SHAPER/COUPLING-PORT-CREDIT-BASED-SHAPER/SHORT-NAME").text == "Cbs1"
        children = [child.tag for child in node]
        assert children.index("ASSIGNED-TRAFFIC-CLASSS") < children.index("MINIMUM-FIFO-LENGTH") < children.index("SHAPER")

    def test_write_empty_fields_omits_optional_tags(self, writer):
        parent = ET.Element("PARENT")
        writer.writeCouplingPortFifo(parent, CouplingPortFifo(MockParent(), "Empty"))
        node = parent.find("COUPLING-PORT-FIFO")
        assert node is not None
        assert node.find("ASSIGNED-TRAFFIC-CLASSS") is None
        assert node.find("MINIMUM-FIFO-LENGTH") is None
        assert node.find("SHAPER") is None


class TestCouplingPortFifoRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, parser):
        parent = ET.Element("PARENT")
        writer.writeCouplingPortFifo(parent, _new_fifo())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))
        parsed = CouplingPortFifo(MockParent(), "Fifo1")
        parser.readCouplingPortFifo(root[0][0], parsed)
        assert parsed.getShortName() == "Fifo1"
        assert parsed.getUuid().getValue() == "DCE:2fac1234-31f8-11b4-a222-08002b34c003"
        classes = parsed.getAssignedTrafficClasses()
        assert len(classes) == 2
        assert classes[0].getValue() == 3
        assert classes[1].getValue() == 5
        assert parsed.getMinimumFifoLength().getValue() == 1522
        shaper = parsed.getShaper()
        assert isinstance(shaper, CouplingPortCreditBasedShaper)
        assert shaper.getShortName() == "Cbs1"
        assert shaper.getIdleSlope().getValue() == 300

    def test_reader_empty_fields(self, parser):
        element = ET.fromstring("<COUPLING-PORT-FIFO xmlns='%s'><SHORT-NAME>Empty</SHORT-NAME></COUPLING-PORT-FIFO>" % NS)
        parsed = CouplingPortFifo(MockParent(), "Empty")
        parser.readCouplingPortFifo(element, parsed)
        assert parsed.getAssignedTrafficClasses() == []
        assert parsed.getMinimumFifoLength() is None
        assert parsed.getShaper() is None
