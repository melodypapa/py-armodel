"""
Reader tests for MacSecProps (CP_TPS_SystemTemplate Table 3.118, p.173, R23-11).

Covers the AR-OBJECT base level (S/T checksum/timestamp attributes), the five optional
children of the MAC-SEC-PROPS element shape in XSD group order (AUTO-START,
MAC-SEC-KAY-CONFIG, ON-FAIL-PERMISSIVE-MODE, ON-FAIL-PERMISSIVE-MODE-TIMEOUT,
SAK-REKEY-TIME-SPAN per group MAC-SEC-PROPS, AUTOSAR_00052.xsd), the empty-element
case and the dispatch through the aggregating CouplingPort (MAC-SEC-PROPSS wrapper).

Round-trip counterpart: tests/test_armodel/writer/test_mac_sec_props.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import CouplingPort
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import MacSecProps
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<MAC-SEC-PROPS xmlns='{NS}'>{inner}</MAC-SEC-PROPS>")


def _snip_with_attrs(attrs: str, inner: str) -> ET.Element:
    return ET.fromstring(f"<MAC-SEC-PROPS xmlns='{NS}' {attrs}>{inner}</MAC-SEC-PROPS>")


def _full_inner() -> str:
    return (
        "<AUTO-START>true</AUTO-START>"
        "<MAC-SEC-KAY-CONFIG><KEY-SERVER-PRIORITY>16</KEY-SERVER-PRIORITY></MAC-SEC-KAY-CONFIG>"
        "<ON-FAIL-PERMISSIVE-MODE>TIMEOUT</ON-FAIL-PERMISSIVE-MODE>"
        "<ON-FAIL-PERMISSIVE-MODE-TIMEOUT>30.0</ON-FAIL-PERMISSIVE-MODE-TIMEOUT>"
        "<SAK-REKEY-TIME-SPAN>3600.0</SAK-REKEY-TIME-SPAN>"
    )


class TestReadMacSecProps:
    def test_read_arobject_base_level(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip_with_attrs("S='chk-1' T='2009-07-23T13:38:00Z'", "")
        props = MacSecProps()
        parser.readMacSecProps(element, props)

        assert props.getChecksum().getValue() == "chk-1"
        assert props.getTimestamp().getValue() == "2009-07-23T13:38:00Z"
        assert props.getAutoStart() is None

    def test_read_all_attributes(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip(_full_inner())
        props = MacSecProps()
        parser.readMacSecProps(element, props)

        assert props.getAutoStart().getValue() is True
        assert props.getMacSecKayConfig().getKeyServerPriority().getValue() == 16
        assert props.getOnFailPermissiveMode().getValue() == "TIMEOUT"
        assert props.getOnFailPermissiveModeTimeout().getValue() == 30.0
        assert props.getSakRekeyTimeSpan().getValue() == 3600.0

    def test_read_partial_attributes(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<AUTO-START>false</AUTO-START><SAK-REKEY-TIME-SPAN>60.0</SAK-REKEY-TIME-SPAN>")
        props = MacSecProps()
        parser.readMacSecProps(element, props)

        assert props.getAutoStart().getValue() is False
        assert props.getSakRekeyTimeSpan().getValue() == 60.0
        assert props.getMacSecKayConfig() is None
        assert props.getOnFailPermissiveMode() is None
        assert props.getOnFailPermissiveModeTimeout() is None

    def test_read_empty_element(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("")
        props = MacSecProps()
        parser.readMacSecProps(element, props)

        assert props.getAutoStart() is None
        assert props.getMacSecKayConfig() is None
        assert props.getOnFailPermissiveMode() is None
        assert props.getOnFailPermissiveModeTimeout() is None
        assert props.getSakRekeyTimeSpan() is None

    def test_get_mac_sec_props_helper(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip(_full_inner())
        props = parser.getMacSecProps(element)

        assert props is not None
        assert props.getAutoStart().getValue() is True
        assert props.getOnFailPermissiveMode().getValue() == "TIMEOUT"
        assert props.getSakRekeyTimeSpan().getValue() == 3600.0


class TestCouplingPortMacSecPropsDispatch:
    class MockParent(ARObject):
        def __init__(self):
            super().__init__()

    def _fresh_port(self) -> CouplingPort:
        return CouplingPort(self.MockParent(), "CP1")

    def test_read_coupling_port_wrapper_dispatch(self):
        parser = ARXMLParser(options={"warning": True})
        element = ET.fromstring("<COUPLING-PORT xmlns='%s'><SHORT-NAME>CP1</SHORT-NAME>" "<MAC-SEC-PROPSS><MAC-SEC-PROPS>%s</MAC-SEC-PROPS></MAC-SEC-PROPSS>" "</COUPLING-PORT>" % (NS, _full_inner()))
        port = self._fresh_port()
        parser.readCouplingPort(element, port)

        props_list = port.getMacSecProps()
        assert len(props_list) == 1
        props = props_list[0]
        assert props.getAutoStart().getValue() is True
        assert props.getMacSecKayConfig().getKeyServerPriority().getValue() == 16
        assert props.getOnFailPermissiveMode().getValue() == "TIMEOUT"
        assert props.getOnFailPermissiveModeTimeout().getValue() == 30.0
        assert props.getSakRekeyTimeSpan().getValue() == 3600.0

    def test_read_coupling_port_multiple_items(self):
        parser = ARXMLParser(options={"warning": True})
        element = ET.fromstring(
            "<COUPLING-PORT xmlns='%s'><SHORT-NAME>CP1</SHORT-NAME>"
            "<MAC-SEC-PROPSS>"
            "<MAC-SEC-PROPS><AUTO-START>true</AUTO-START></MAC-SEC-PROPS>"
            "<MAC-SEC-PROPS><AUTO-START>false</AUTO-START></MAC-SEC-PROPS>"
            "</MAC-SEC-PROPSS>"
            "</COUPLING-PORT>" % NS
        )
        port = self._fresh_port()
        parser.readCouplingPort(element, port)

        props_list = port.getMacSecProps()
        assert len(props_list) == 2
        assert props_list[0].getAutoStart().getValue() is True
        assert props_list[1].getAutoStart().getValue() is False

    def test_read_coupling_port_wrapper_absent(self):
        parser = ARXMLParser(options={"warning": True})
        element = ET.fromstring("<COUPLING-PORT xmlns='%s'><SHORT-NAME>CP1</SHORT-NAME></COUPLING-PORT>" % NS)
        port = self._fresh_port()
        parser.readCouplingPort(element, port)

        assert port.getMacSecProps() == []

    def test_read_coupling_port_empty_wrapper(self):
        parser = ARXMLParser(options={"warning": True})
        element = ET.fromstring("<COUPLING-PORT xmlns='%s'><SHORT-NAME>CP1</SHORT-NAME><MAC-SEC-PROPSS></MAC-SEC-PROPSS></COUPLING-PORT>" % NS)
        port = self._fresh_port()
        parser.readCouplingPort(element, port)

        assert port.getMacSecProps() == []
