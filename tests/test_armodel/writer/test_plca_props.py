"""
Writer/reader round-trip tests for PlcaProps (CP_TPS_SystemTemplate Table 3.117, p.169, R23-11).

Checks the AR-OBJECT base level (S/T checksum/timestamp attribute emission), the child
element values and the XSD sequence order (PLCA-LOCAL-NODE-ID, PLCA-MAX-BURST-COUNT,
PLCA-MAX-BURST-TIMER per group PLCA-PROPS, AUTOSAR_00052.xsd), the partial-emission case,
the wrapper-absent/empty-wrapper cases and the write→parse round-trip — both at the
dedicated writePlcaProps/readPlcaProps level and dispatched through the aggregating
CouplingPort (setPlcaProps/getPlcaProps).

Reader counterpart: tests/test_armodel/parser/test_plca_props.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, PositiveInteger, String
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


def _full_props() -> PlcaProps:
    props = PlcaProps()
    props.setPlcaLocalNodeId(_pos_int("2"))
    props.setPlcaMaxBurstCount(_pos_int("5"))
    props.setPlcaMaxBurstTimer(_pos_int("42"))
    return props


def _new_port():
    port = CouplingPort(MockParent(), "CP1")
    props = PlcaProps()
    props.setPlcaLocalNodeId(_pos_int("5"))
    props.setPlcaMaxBurstCount(_pos_int("3"))
    props.setPlcaMaxBurstTimer(_pos_int("10"))
    port.setPlcaProps(props)
    return port


class TestWritePlcaProps:
    def test_write_arobject_base_level(self, writer):
        props = PlcaProps()
        props.setChecksum(String().setValue("chk-1"))
        props.setTimestamp(DateTime().setValue("2009-07-23T13:38:00Z"))
        element = ET.Element("PLCA-PROPS")
        writer.writePlcaProps(element, props)

        assert element.attrib["S"] == "chk-1"
        assert element.attrib["T"] == "2009-07-23T13:38:00Z"

    def test_write_all_children_in_xsd_order(self, writer):
        element = ET.Element("PLCA-PROPS")
        writer.writePlcaProps(element, _full_props())

        assert [child.tag for child in element] == [
            "PLCA-LOCAL-NODE-ID",
            "PLCA-MAX-BURST-COUNT",
            "PLCA-MAX-BURST-TIMER",
        ]
        assert element.find("PLCA-LOCAL-NODE-ID").text == "2"
        assert element.find("PLCA-MAX-BURST-COUNT").text == "5"
        assert element.find("PLCA-MAX-BURST-TIMER").text == "42"

    def test_write_partial_emission(self, writer):
        props = PlcaProps()
        props.setPlcaLocalNodeId(_pos_int("7"))
        props.setPlcaMaxBurstTimer(_pos_int("9"))

        element = ET.Element("PLCA-PROPS")
        writer.writePlcaProps(element, props)

        assert [child.tag for child in element] == ["PLCA-LOCAL-NODE-ID", "PLCA-MAX-BURST-TIMER"]
        assert element.find("PLCA-LOCAL-NODE-ID").text == "7"
        assert element.find("PLCA-MAX-BURST-TIMER").text == "9"

    def test_write_empty_emits_no_props_children(self, writer):
        element = ET.Element("PLCA-PROPS")
        writer.writePlcaProps(element, PlcaProps())

        assert [child.tag for child in element] == []

    def test_write_coupling_port_wrapper_emission(self, writer):
        parent = ET.Element("COUPLING-PORT")
        writer.setPlcaProps(parent, "PLCA-PROPS", _full_props())

        wrapper = parent.find("PLCA-PROPS")
        assert wrapper is not None
        assert [child.tag for child in wrapper] == [
            "PLCA-LOCAL-NODE-ID",
            "PLCA-MAX-BURST-COUNT",
            "PLCA-MAX-BURST-TIMER",
        ]

    def test_write_coupling_port_wrapper_absent(self, writer):
        parent = ET.Element("COUPLING-PORT")
        writer.setPlcaProps(parent, "PLCA-PROPS", None)

        assert parent.find("PLCA-PROPS") is None

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
    def test_write_and_reparse_round_trip(self, parser):
        element = ET.Element("PLCA-PROPS")
        ARXMLWriter().writePlcaProps(element, _full_props())

        inner = ET.tostring(element).decode("utf-8")
        namespaced = ET.fromstring(inner.replace(element.tag, "%s xmlns='%s'" % (element.tag, NS), 1))
        recovered = PlcaProps()
        parser.readPlcaProps(namespaced, recovered)

        assert recovered.getPlcaLocalNodeId().getValue() == 2
        assert recovered.getPlcaMaxBurstCount().getValue() == 5
        assert recovered.getPlcaMaxBurstTimer().getValue() == 42

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
