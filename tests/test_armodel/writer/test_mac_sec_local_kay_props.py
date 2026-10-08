"""
Writer/reader round-trip tests for MacSecLocalKayProps (CP_TPS_SystemTemplate Table 3.119, p.174, R23-11).

Checks the AR-OBJECT base level (S/T checksum/timestamp attribute emission), the child
element values and the XSD sequence order (DESTINATION-MAC-ADDRESS, GLOBAL-KAY-PROPS-REF,
KEY-SERVER-PRIORITY, MKA-PARTICIPANT-REFS/MKA-PARTICIPANT-REF, ROLE, SOURCE-MAC-ADDRESS per
group MAC-SEC-LOCAL-KAY-PROPS, AUTOSAR_00052.xsd), the partial-emission and
empty-wrapper cases and the write→parse round-trip — both at the dedicated
writeMacSecLocalKayProps/readMacSecLocalKayProps level and dispatched through the
aggregating MacSecProps (MAC-SEC-KAY-CONFIG child via setMacSecLocalKayProps/
getMacSecLocalKayProps).

Reader counterpart: tests/test_armodel/parser/test_mac_sec_local_kay_props.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, MacAddressString, PositiveInteger, RefType, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import MacSecLocalKayProps, MacSecProps, MacSecRoleEnum
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


def _wrap(element: ET.Element) -> ET.Element:
    inner = ET.tostring(element).decode("utf-8")
    return ET.fromstring(f"<AUTOSAR xmlns='{NS}'>{inner}</AUTOSAR>")


def _mac(value):
    mac = MacAddressString()
    mac.setValue(value)
    return mac


def _pos_int(value):
    p = PositiveInteger()
    p.setValue(str(value))
    return p


def _ref(value):
    ref = RefType()
    ref.setValue(value)
    return ref


def _role(value):
    e = MacSecRoleEnum()
    e.setValue(value)
    return e


def _new_mac_sec_local_kay_props():
    props = MacSecLocalKayProps()
    props.setDestinationMacAddress(_mac("00-11-22-33-44-55"))
    props.setGlobalKayPropsRef(_ref("/Sec/MacSecGlobalKay"))
    props.setKeyServerPriority(_pos_int("16"))
    props.addMkaParticipantRef(_ref("/Sec/MkaParticipant1"))
    props.addMkaParticipantRef(_ref("/Sec/MkaParticipant2"))
    props.setRole(_role(MacSecRoleEnum.KEY_SERVER))
    props.setSourceMacAddress(_mac("AA-BB-CC-DD-EE-FF"))
    return props


def _assert_all_field_values(props: MacSecLocalKayProps):
    assert props.getDestinationMacAddress().getValue() == "00-11-22-33-44-55"
    assert props.getGlobalKayPropsRef().getValue() == "/Sec/MacSecGlobalKay"
    assert props.getKeyServerPriority().getValue() == 16
    assert [r.getValue() for r in props.getMkaParticipantRefs()] == ["/Sec/MkaParticipant1", "/Sec/MkaParticipant2"]
    assert props.getRole().getValue() == MacSecRoleEnum.KEY_SERVER
    assert props.getSourceMacAddress().getValue() == "AA-BB-CC-DD-EE-FF"


class TestWriteMacSecLocalKayProps:
    def test_write_arobject_base_level(self, writer):
        props = MacSecLocalKayProps()
        props.setChecksum(String().setValue("chk-1"))
        props.setTimestamp(DateTime().setValue("2009-07-23T13:38:00Z"))
        element = ET.Element("MAC-SEC-KAY-CONFIG")
        writer.writeMacSecLocalKayProps(element, props)

        assert element.attrib["S"] == "chk-1"
        assert element.attrib["T"] == "2009-07-23T13:38:00Z"

    def test_write_all_children_in_xsd_order(self, writer):
        element = ET.Element("MAC-SEC-KAY-CONFIG")
        writer.writeMacSecLocalKayProps(element, _new_mac_sec_local_kay_props())

        assert [child.tag for child in element] == [
            "DESTINATION-MAC-ADDRESS",
            "GLOBAL-KAY-PROPS-REF",
            "KEY-SERVER-PRIORITY",
            "MKA-PARTICIPANT-REFS",
            "ROLE",
            "SOURCE-MAC-ADDRESS",
        ]
        assert element.find("DESTINATION-MAC-ADDRESS").text == "00-11-22-33-44-55"
        assert element.find("GLOBAL-KAY-PROPS-REF").text == "/Sec/MacSecGlobalKay"
        assert element.find("KEY-SERVER-PRIORITY").text == "16"
        mka_refs = element.findall("MKA-PARTICIPANT-REFS/MKA-PARTICIPANT-REF")
        assert [r.text for r in mka_refs] == ["/Sec/MkaParticipant1", "/Sec/MkaParticipant2"]
        assert element.find("ROLE").text == "KEY-SERVER"
        assert element.find("SOURCE-MAC-ADDRESS").text == "AA-BB-CC-DD-EE-FF"

    def test_write_partial_emission(self, writer):
        props = MacSecLocalKayProps()
        props.setDestinationMacAddress(_mac("00-11-22-33-44-55"))
        props.setRole(_role(MacSecRoleEnum.PEER))

        element = ET.Element("MAC-SEC-KAY-CONFIG")
        writer.writeMacSecLocalKayProps(element, props)

        assert [child.tag for child in element] == ["DESTINATION-MAC-ADDRESS", "ROLE"]
        assert element.find("DESTINATION-MAC-ADDRESS").text == "00-11-22-33-44-55"
        assert element.find("ROLE").text == "PEER"

    def test_write_empty_emits_no_children(self, writer):
        element = ET.Element("MAC-SEC-KAY-CONFIG")
        writer.writeMacSecLocalKayProps(element, MacSecLocalKayProps())

        assert [child.tag for child in element] == []

    def test_write_empty_mka_list_omits_wrapper(self, writer):
        props = MacSecLocalKayProps()
        props.setKeyServerPriority(_pos_int("16"))

        element = ET.Element("MAC-SEC-KAY-CONFIG")
        writer.writeMacSecLocalKayProps(element, props)

        assert [child.tag for child in element] == ["KEY-SERVER-PRIORITY"]
        assert element.find("MKA-PARTICIPANT-REFS") is None


class TestSetMacSecLocalKayPropsWrapper:
    def test_write_wrapper_level_all_fields(self, writer):
        parent = ET.Element("MAC-SEC-PROPS")
        writer.setMacSecLocalKayProps(parent, "MAC-SEC-KAY-CONFIG", _new_mac_sec_local_kay_props())

        node = parent.find("MAC-SEC-KAY-CONFIG")
        assert node is not None
        assert node.find("DESTINATION-MAC-ADDRESS").text == "00-11-22-33-44-55"
        assert node.find("GLOBAL-KAY-PROPS-REF").text == "/Sec/MacSecGlobalKay"
        assert node.find("KEY-SERVER-PRIORITY").text == "16"
        assert node.find("ROLE").text == "KEY-SERVER"
        assert node.find("SOURCE-MAC-ADDRESS").text == "AA-BB-CC-DD-EE-FF"

    def test_write_wrapper_level_none_props(self, writer):
        parent = ET.Element("MAC-SEC-PROPS")
        writer.setMacSecLocalKayProps(parent, "MAC-SEC-KAY-CONFIG", None)

        assert parent.find("MAC-SEC-KAY-CONFIG") is None

    def test_write_mac_sec_props_dispatches_kay_config(self, writer):
        props = MacSecProps()
        kay = MacSecLocalKayProps()
        kay.setKeyServerPriority(_pos_int("16"))
        kay.setRole(_role(MacSecRoleEnum.KEY_SERVER))
        props.setMacSecKayConfig(kay)

        element = ET.Element("MAC-SEC-PROPS")
        writer.writeMacSecProps(element, props)

        node = element.find("MAC-SEC-KAY-CONFIG")
        assert node is not None
        assert [child.tag for child in node] == ["KEY-SERVER-PRIORITY", "ROLE"]
        assert node.find("KEY-SERVER-PRIORITY").text == "16"
        assert node.find("ROLE").text == "KEY-SERVER"


class TestMacSecLocalKayPropsRoundTrip:
    def test_write_and_reparse_round_trip_dedicated_level(self, parser):
        element = ET.Element("MAC-SEC-KAY-CONFIG")
        ARXMLWriter().writeMacSecLocalKayProps(element, _new_mac_sec_local_kay_props())

        inner = ET.tostring(element).decode("utf-8")
        namespaced = ET.fromstring(inner.replace(element.tag, "%s xmlns='%s'" % (element.tag, NS), 1))
        recovered = MacSecLocalKayProps()
        parser.readMacSecLocalKayProps(namespaced, recovered)

        _assert_all_field_values(recovered)

    def test_round_trip_preserves_base_level(self, parser):
        props = MacSecLocalKayProps()
        props.setChecksum(String().setValue("chk-9"))
        props.setTimestamp(DateTime().setValue("2009-07-23T13:38:00Z"))
        props.setKeyServerPriority(_pos_int("16"))
        element = ET.Element("MAC-SEC-KAY-CONFIG")
        ARXMLWriter().writeMacSecLocalKayProps(element, props)

        inner = ET.tostring(element).decode("utf-8")
        namespaced = ET.fromstring(inner.replace(element.tag, "%s xmlns='%s'" % (element.tag, NS), 1))
        recovered = MacSecLocalKayProps()
        parser.readMacSecLocalKayProps(namespaced, recovered)

        assert recovered.getChecksum().getValue() == "chk-9"
        assert recovered.getTimestamp().getValue() == "2009-07-23T13:38:00Z"
        assert recovered.getKeyServerPriority().getValue() == 16

    def test_round_trip_through_mac_sec_props(self, parser):
        props = MacSecProps()
        props.setMacSecKayConfig(_new_mac_sec_local_kay_props())
        element = ET.Element("MAC-SEC-PROPS")
        ARXMLWriter().writeMacSecProps(element, props)

        inner = ET.tostring(element).decode("utf-8")
        namespaced = ET.fromstring(inner.replace(element.tag, "%s xmlns='%s'" % (element.tag, NS), 1))
        recovered = MacSecProps()
        parser.readMacSecProps(namespaced, recovered)

        kay = recovered.getMacSecKayConfig()
        assert kay is not None
        _assert_all_field_values(kay)

    def test_round_trip_helper_level(self, writer, parser, tmp_path):
        props = _new_mac_sec_local_kay_props()

        parent = ET.Element("MAC-SEC-PROPS")
        writer.setMacSecLocalKayProps(parent, "MAC-SEC-KAY-CONFIG", props)

        out_file = str(tmp_path / "mac_sec_local_kay_props.arxml")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(ET.tostring(_wrap(parent), encoding="unicode"))

        tree = ET.parse(out_file)
        recovered = parser.getMacSecLocalKayProps(tree.getroot()[0][0])

        assert recovered is not None
        _assert_all_field_values(recovered)

    def test_reader_empty_fields(self, parser):
        xml = "<AUTOSAR xmlns='%s'>" "<MAC-SEC-PROPS><MAC-SEC-KAY-CONFIG/></MAC-SEC-PROPS>" "</AUTOSAR>" % NS
        root = ET.fromstring(xml)
        recovered = parser.getMacSecLocalKayProps(root[0][0])

        assert recovered is not None
        assert recovered.getDestinationMacAddress() is None
        assert recovered.getGlobalKayPropsRef() is None
        assert recovered.getKeyServerPriority() is None
        assert recovered.getMkaParticipantRefs() == []
        assert recovered.getRole() is None
        assert recovered.getSourceMacAddress() is None

    def test_reader_empty_wrapper_list(self, parser):
        xml = "<AUTOSAR xmlns='%s'>" "<MAC-SEC-PROPS><MAC-SEC-KAY-CONFIG><MKA-PARTICIPANT-REFS/></MAC-SEC-KAY-CONFIG></MAC-SEC-PROPS>" "</AUTOSAR>" % NS
        root = ET.fromstring(xml)
        recovered = parser.getMacSecLocalKayProps(root[0][0])

        assert recovered is not None
        assert recovered.getMkaParticipantRefs() == []
