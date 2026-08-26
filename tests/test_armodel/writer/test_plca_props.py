"""Writer/reader round-trip tests for PlcaProps (Table 3.117, p.169)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    CouplingPort,
    PlcaProps,
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


def _pos_int(text):
    val = PositiveInteger()
    val.setValue(text)
    return val


def _new_port():
    port = CouplingPort(MockParent(), "CP1")
    props = PlcaProps()
    props.setPlcaLocalNodeId(_pos_int("5"))
    props.setPlcaMaxBurstCount(_pos_int("3"))
    props.setPlcaMaxBurstTimer(_pos_int("10"))
    port.setPlcaProps(props)
    return port


class TestWritePlcaProps:
    def test_write_all_fields(self, writer):
        parent = ET.Element("PARENT")
        writer.writeCouplingPort(parent, _new_port())

        node = parent.find("COUPLING-PORT")
        assert node is not None
        plca = node.find("PLCA-PROPS")
        assert plca is not None
        assert plca.find("PLCA-LOCAL-NODE-ID").text == "5"
        assert plca.find("PLCA-MAX-BURST-COUNT").text == "3"
        assert plca.find("PLCA-MAX-BURST-TIMER").text == "10"


class TestPlcaPropsRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, parser, tmp_path):
        parent = ET.Element("PARENT")
        writer.writeCouplingPort(parent, _new_port())

        out_file = str(tmp_path / "plca_props.arxml")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(ET.tostring(_wrap(parent), encoding="unicode"))

        tree = ET.parse(out_file)
        recovered = CouplingPort(MockParent(), "CP1")
        parser.readCouplingPort(tree.getroot()[0][0], recovered)

        plca = recovered.getPlcaProps()
        assert isinstance(plca, PlcaProps)
        assert plca.getPlcaLocalNodeId().getValue() == 5
        assert plca.getPlcaMaxBurstCount().getValue() == 3
        assert plca.getPlcaMaxBurstTimer().getValue() == 10

    def test_reader_empty_fields(self, parser):
        element = ET.fromstring("<COUPLING-PORT xmlns='%s'><SHORT-NAME>Empty</SHORT-NAME></COUPLING-PORT>" % NS)
        recovered = CouplingPort(MockParent(), "Empty")
        parser.readCouplingPort(element, recovered)

        assert recovered.getShortName() == "Empty"
        assert recovered.getPlcaProps() is None


def _wrap(element: ET.Element) -> ET.Element:
    inner = ET.tostring(element).decode("utf-8")
    return ET.fromstring(f"<AUTOSAR xmlns='{NS}'>{inner}</AUTOSAR>")
