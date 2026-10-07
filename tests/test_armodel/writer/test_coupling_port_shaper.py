"""Writer round-trip tests for CouplingPortShaper (Table 3.67, p.123).

CouplingPortShaper is a CouplingPortStructuralElement value type aggregated by
CouplingPortDetails.couplingPortStructuralElement. XML element order per XSD group
COUPLING-PORT-SHAPER: IDLE-SLOPE, PREDECESSOR-FIFO-REF.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import CouplingPortDetails, CouplingPortShaper
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


def _pos_int(text):
    value = PositiveInteger()
    value.setValue(text)
    return value


def _new_shaper():
    shaper = CouplingPortShaper(MockParent(), "Shaper1")
    shaper.setIdleSlope(_pos_int("12500000"))
    ref = RefType()
    ref.setDest("COUPLING-PORT-FIFO")
    ref.setValue("/Clusters/Switch/CouplingPort/Fifo1")
    shaper.setPredecessorFifoRef(ref)
    return shaper


class TestWriteCouplingPortShaper:
    def test_write_all_fields(self, writer):
        parent = ET.Element("PARENT")
        writer.writeCouplingPortShaper(parent, _new_shaper())
        node = parent.find("COUPLING-PORT-SHAPER")
        assert node is not None
        assert node.find("SHORT-NAME").text == "Shaper1"
        assert node.find("IDLE-SLOPE").text == "12500000"
        ref = node.find("PREDECESSOR-FIFO-REF")
        assert ref.text == "/Clusters/Switch/CouplingPort/Fifo1"
        assert ref.attrib["DEST"] == "COUPLING-PORT-FIFO"
        children = [child.tag for child in node]
        assert children.index("IDLE-SLOPE") < children.index("PREDECESSOR-FIFO-REF")

    def test_write_empty_fields_omits_optional_tags(self, writer):
        parent = ET.Element("PARENT")
        writer.writeCouplingPortShaper(parent, CouplingPortShaper(MockParent(), "Empty"))
        node = parent.find("COUPLING-PORT-SHAPER")
        assert node is not None
        assert node.find("IDLE-SLOPE") is None
        assert node.find("PREDECESSOR-FIFO-REF") is None

    def test_write_dispatch_via_coupling_port_details(self, writer):
        details = CouplingPortDetails()
        details.createCouplingPortShaper("Shaper1")
        details.createCouplingPortFifo("Fifo1")

        parent = ET.Element("PARENT")
        writer.writeCouplingPortDetailsCouplingPortStructuralElements(parent, details)
        wrapper = parent.find("COUPLING-PORT-STRUCTURAL-ELEMENTS")
        assert wrapper is not None
        children = [child.tag for child in wrapper]
        assert children == ["COUPLING-PORT-SHAPER", "COUPLING-PORT-FIFO"]
        assert wrapper.find("COUPLING-PORT-SHAPER/SHORT-NAME").text == "Shaper1"


class TestCouplingPortShaperRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, parser):
        parent = ET.Element("PARENT")
        writer.writeCouplingPortShaper(parent, _new_shaper())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))
        parsed = CouplingPortShaper(MockParent(), "Shaper1")
        parser.readCouplingPortShaper(root[0][0], parsed)
        assert parsed.getShortName() == "Shaper1"
        assert parsed.getIdleSlope() is not None
        assert parsed.getIdleSlope().getValue() == 12500000
        ref = parsed.getPredecessorFifoRef()
        assert ref is not None
        assert ref.getValue() == "/Clusters/Switch/CouplingPort/Fifo1"
        assert ref.getDest() == "COUPLING-PORT-FIFO"

    def test_reader_empty_fields(self, parser):
        element = ET.fromstring("<COUPLING-PORT-SHAPER xmlns='%s'><SHORT-NAME>Empty</SHORT-NAME></COUPLING-PORT-SHAPER>" % NS)
        parsed = CouplingPortShaper(MockParent(), "Empty")
        parser.readCouplingPortShaper(element, parsed)
        assert parsed.getIdleSlope() is None
        assert parsed.getPredecessorFifoRef() is None

    def test_reader_dispatch_via_coupling_port_details(self, parser):
        parent = ET.fromstring(
            "<ROOT xmlns='%s'>"
            "<COUPLING-PORT-STRUCTURAL-ELEMENTS>"
            "<COUPLING-PORT-SHAPER>"
            "<SHORT-NAME>Shaper1</SHORT-NAME>"
            "<IDLE-SLOPE>12500000</IDLE-SLOPE>"
            "<PREDECESSOR-FIFO-REF DEST='COUPLING-PORT-FIFO'>/Clusters/Switch/CouplingPort/Fifo1</PREDECESSOR-FIFO-REF>"
            "</COUPLING-PORT-SHAPER>"
            "</COUPLING-PORT-STRUCTURAL-ELEMENTS>"
            "</ROOT>" % NS
        )
        details = CouplingPortDetails()
        parser.readCouplingPortDetailsCouplingPortStructuralElements(parent, details)
        elements = details.getCouplingPortStructuralElements()
        assert len(elements) == 1
        assert isinstance(elements[0], CouplingPortShaper)
        assert elements[0].getShortName() == "Shaper1"
        assert elements[0].getIdleSlope().getValue() == 12500000
        assert elements[0].getPredecessorFifoRef().getValue() == "/Clusters/Switch/CouplingPort/Fifo1"
