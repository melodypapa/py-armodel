"""
Writer/reader round-trip tests for MacSecProps (CP_TPS_SystemTemplate Table 3.118, p.173, R23-11).

Checks the AR-OBJECT base level (S/T checksum/timestamp attribute emission), the child
element values and the XSD sequence order (AUTO-START, MAC-SEC-KAY-CONFIG,
ON-FAIL-PERMISSIVE-MODE, ON-FAIL-PERMISSIVE-MODE-TIMEOUT, SAK-REKEY-TIME-SPAN per group
MAC-SEC-PROPS, AUTOSAR_00052.xsd), the partial-emission case, the wrapper-absent/empty
cases and the write→parse round-trip — both at the dedicated writeMacSecProps/
readMacSecProps level and dispatched through the aggregating CouplingPort
(MAC-SEC-PROPSS wrapper via setMacSecProps/getMacSecProps).

Reader counterpart: tests/test_armodel/parser/test_mac_sec_props.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, DateTime, PositiveInteger, String, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import CouplingPort
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import (
    MacSecFailPermissiveModeEnum,
    MacSecLocalKayProps,
    MacSecProps,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


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


def _bool(value):
    val = Boolean()
    val.setValue(value)
    return val


def _time(value):
    val = TimeValue()
    val.setValue(value)
    return val


def _pos_int(value):
    val = PositiveInteger()
    val.setValue(value)
    return val


def _fail_mode(value):
    enum = MacSecFailPermissiveModeEnum()
    enum.setValue(value)
    return enum


def _full_props() -> MacSecProps:
    props = MacSecProps()
    props.setAutoStart(_bool("true"))
    kay = MacSecLocalKayProps()
    kay.setKeyServerPriority(_pos_int("16"))
    props.setMacSecKayConfig(kay)
    props.setOnFailPermissiveMode(_fail_mode(MacSecFailPermissiveModeEnum.TIMEOUT))
    props.setOnFailPermissiveModeTimeout(_time("30.0"))
    props.setSakRekeyTimeSpan(_time("3600.0"))
    return props


def _new_port() -> CouplingPort:
    port = CouplingPort(MockParent(), "CP1")
    port.addMacSecProps(_full_props())
    return port


class TestWriteMacSecProps:
    def test_write_arobject_base_level(self, writer):
        props = MacSecProps()
        props.setChecksum(String().setValue("chk-1"))
        props.setTimestamp(DateTime().setValue("2009-07-23T13:38:00Z"))
        element = ET.Element("MAC-SEC-PROPS")
        writer.writeMacSecProps(element, props)

        assert element.attrib["S"] == "chk-1"
        assert element.attrib["T"] == "2009-07-23T13:38:00Z"

    def test_write_all_children_in_xsd_order(self, writer):
        element = ET.Element("MAC-SEC-PROPS")
        writer.writeMacSecProps(element, _full_props())

        assert [child.tag for child in element] == [
            "AUTO-START",
            "MAC-SEC-KAY-CONFIG",
            "ON-FAIL-PERMISSIVE-MODE",
            "ON-FAIL-PERMISSIVE-MODE-TIMEOUT",
            "SAK-REKEY-TIME-SPAN",
        ]
        assert element.find("AUTO-START").text == "true"
        assert element.find("MAC-SEC-KAY-CONFIG").find("KEY-SERVER-PRIORITY").text == "16"
        assert element.find("ON-FAIL-PERMISSIVE-MODE").text == "TIMEOUT"
        assert element.find("ON-FAIL-PERMISSIVE-MODE-TIMEOUT").text == "30.0"
        assert element.find("SAK-REKEY-TIME-SPAN").text == "3600.0"

    def test_write_partial_emission(self, writer):
        props = MacSecProps()
        props.setAutoStart(_bool("false"))
        props.setSakRekeyTimeSpan(_time("60.0"))

        element = ET.Element("MAC-SEC-PROPS")
        writer.writeMacSecProps(element, props)

        assert [child.tag for child in element] == ["AUTO-START", "SAK-REKEY-TIME-SPAN"]
        assert element.find("AUTO-START").text == "false"
        assert element.find("SAK-REKEY-TIME-SPAN").text == "60.0"

    def test_write_empty_emits_no_props_children(self, writer):
        element = ET.Element("MAC-SEC-PROPS")
        writer.writeMacSecProps(element, MacSecProps())

        assert [child.tag for child in element] == []

    def test_write_coupling_port_wrapper_emission(self, writer):
        parent = ET.Element("COUPLING-PORT")
        writer.setMacSecProps(parent, "MAC-SEC-PROPS", _full_props())

        wrapper = parent.find("MAC-SEC-PROPS")
        assert wrapper is not None
        assert [child.tag for child in wrapper] == [
            "AUTO-START",
            "MAC-SEC-KAY-CONFIG",
            "ON-FAIL-PERMISSIVE-MODE",
            "ON-FAIL-PERMISSIVE-MODE-TIMEOUT",
            "SAK-REKEY-TIME-SPAN",
        ]

    def test_write_coupling_port_wrapper_absent(self, writer):
        parent = ET.Element("COUPLING-PORT")
        writer.setMacSecProps(parent, "MAC-SEC-PROPS", None)

        assert parent.find("MAC-SEC-PROPS") is None

    def test_write_coupling_port_aggregation(self, writer):
        parent = ET.Element("PARENT")
        writer.writeCouplingPort(parent, _new_port())

        node = parent.find("COUPLING-PORT")
        assert node is not None
        wrapper = node.find("MAC-SEC-PROPSS")
        assert wrapper is not None
        items = wrapper.findall("MAC-SEC-PROPS")
        assert len(items) == 1
        assert items[0].find("AUTO-START").text == "true"
        assert items[0].find("ON-FAIL-PERMISSIVE-MODE").text == "TIMEOUT"

    def test_write_coupling_port_empty_list_no_wrapper(self, writer):
        port = CouplingPort(MockParent(), "CP1")
        parent = ET.Element("PARENT")
        writer.writeCouplingPort(parent, port)

        node = parent.find("COUPLING-PORT")
        assert node is not None
        assert node.find("MAC-SEC-PROPSS") is None


class TestMacSecPropsRoundTrip:
    def test_write_and_reparse_round_trip(self, parser):
        element = ET.Element("MAC-SEC-PROPS")
        ARXMLWriter().writeMacSecProps(element, _full_props())

        inner = ET.tostring(element).decode("utf-8")
        namespaced = ET.fromstring(inner.replace(element.tag, "%s xmlns='%s'" % (element.tag, NS), 1))
        recovered = MacSecProps()
        parser.readMacSecProps(namespaced, recovered)

        assert recovered.getAutoStart().getValue() is True
        assert recovered.getMacSecKayConfig().getKeyServerPriority().getValue() == 16
        assert recovered.getOnFailPermissiveMode().getValue() == "TIMEOUT"
        assert recovered.getOnFailPermissiveModeTimeout().getValue() == 30.0
        assert recovered.getSakRekeyTimeSpan().getValue() == 3600.0

    def test_round_trip_preserves_base_level(self, parser):
        props = MacSecProps()
        props.setChecksum(String().setValue("chk-9"))
        props.setTimestamp(DateTime().setValue("2009-07-23T13:38:00Z"))
        element = ET.Element("MAC-SEC-PROPS")
        ARXMLWriter().writeMacSecProps(element, props)

        inner = ET.tostring(element).decode("utf-8")
        namespaced = ET.fromstring(inner.replace(element.tag, "%s xmlns='%s'" % (element.tag, NS), 1))
        recovered = MacSecProps()
        parser.readMacSecProps(namespaced, recovered)

        assert recovered.getChecksum().getValue() == "chk-9"
        assert recovered.getTimestamp().getValue() == "2009-07-23T13:38:00Z"

    def test_round_trip_through_coupling_port(self, writer, parser, tmp_path):
        parent = ET.Element("PARENT")
        writer.writeCouplingPort(parent, _new_port())

        out_file = str(tmp_path / "mac_sec_props.arxml")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(ET.tostring(_wrap(parent), encoding="unicode"))

        tree = ET.parse(out_file)
        recovered = CouplingPort(MockParent(), "CP1")
        parser.readCouplingPort(tree.getroot()[0][0], recovered)

        props_list = recovered.getMacSecProps()
        assert len(props_list) == 1
        props = props_list[0]
        assert props.getAutoStart().getValue() is True
        assert props.getMacSecKayConfig().getKeyServerPriority().getValue() == 16
        assert props.getOnFailPermissiveMode().getValue() == "TIMEOUT"
        assert props.getOnFailPermissiveModeTimeout().getValue() == 30.0
        assert props.getSakRekeyTimeSpan().getValue() == 3600.0


def _wrap(element: ET.Element) -> ET.Element:
    inner = ET.tostring(element).decode("utf-8")
    return ET.fromstring(f"<AUTOSAR xmlns='{NS}'>{inner}</AUTOSAR>")
