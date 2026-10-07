"""
Reader tests for PlcaProps (CP_TPS_SystemTemplate Table 3.117, p.169, R23-11).

Covers the AR-OBJECT base level (S/T checksum/timestamp attributes), the three optional
PLCA-* children of the PLCA-PROPS element shape (AUTOSAR_00052.xsd group PLCA-PROPS —
dispatched by the aggregating CouplingPort via getPlcaProps), the absent-wrapper case and
the empty-wrapper case.

Round-trip counterpart: tests/test_armodel/writer/test_plca_props.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import PlcaProps
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<PLCA-PROPS xmlns='{NS}'>{inner}</PLCA-PROPS>")


def _snip_with_attrs(attrs: str, inner: str) -> ET.Element:
    return ET.fromstring(f"<PLCA-PROPS xmlns='{NS}' {attrs}>{inner}</PLCA-PROPS>")


def _full_inner() -> str:
    return "<PLCA-LOCAL-NODE-ID>2</PLCA-LOCAL-NODE-ID>" "<PLCA-MAX-BURST-COUNT>5</PLCA-MAX-BURST-COUNT>" "<PLCA-MAX-BURST-TIMER>42</PLCA-MAX-BURST-TIMER>"


class TestReadPlcaProps:
    def test_read_arobject_base_level(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip_with_attrs("S='chk-1' T='2009-07-23T13:38:00Z'", "")
        props = PlcaProps()
        parser.readPlcaProps(element, props)

        assert props.getChecksum().getValue() == "chk-1"
        assert props.getTimestamp().getValue() == "2009-07-23T13:38:00Z"
        assert props.getPlcaLocalNodeId() is None

    def test_read_all_attributes(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip(_full_inner())
        props = PlcaProps()
        parser.readPlcaProps(element, props)

        assert props.getPlcaLocalNodeId().getValue() == 2
        assert props.getPlcaMaxBurstCount().getValue() == 5
        assert props.getPlcaMaxBurstTimer().getValue() == 42

    def test_read_partial_attributes(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<PLCA-LOCAL-NODE-ID>7</PLCA-LOCAL-NODE-ID><PLCA-MAX-BURST-TIMER>9</PLCA-MAX-BURST-TIMER>")
        props = PlcaProps()
        parser.readPlcaProps(element, props)

        assert props.getPlcaLocalNodeId().getValue() == 7
        assert props.getPlcaMaxBurstTimer().getValue() == 9
        assert props.getPlcaMaxBurstCount() is None

    def test_read_empty_element(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("")
        props = PlcaProps()
        parser.readPlcaProps(element, props)

        assert props.getPlcaLocalNodeId() is None
        assert props.getPlcaMaxBurstCount() is None
        assert props.getPlcaMaxBurstTimer() is None

    def test_coupling_port_wrapper_dispatch(self):
        parser = ARXMLParser(options={"warning": True})
        parent = ET.fromstring(f"<COUPLING-PORT xmlns='{NS}'><PLCA-PROPS>{_full_inner()}</PLCA-PROPS></COUPLING-PORT>")
        props = parser.getPlcaProps(parent, "PLCA-PROPS")

        assert props is not None
        assert props.getPlcaLocalNodeId().getValue() == 2
        assert props.getPlcaMaxBurstCount().getValue() == 5
        assert props.getPlcaMaxBurstTimer().getValue() == 42

    def test_coupling_port_wrapper_absent(self):
        parser = ARXMLParser(options={"warning": True})
        parent = ET.fromstring(f"<COUPLING-PORT xmlns='{NS}'></COUPLING-PORT>")

        assert parser.getPlcaProps(parent, "PLCA-PROPS") is None
