"""Writer/reader round-trip tests for MacSecLocalKayProps (Table 3.119, p.174).

MacSecLocalKayProps is an ARObject aggregated by MacSecProps.macSecKayConfig
(0..1). It carries the optional attributes destinationMacAddress
(MacAddressString, element DESTINATION-MAC-ADDRESS), globalKayProps (RefType,
element GLOBAL-KAY-PROPS), keyServerPriority (PositiveInteger, element
KEY-SERVER-PRIORITY), mkaParticipant (List[RefType], wrapper
MKA-PARTICIPANT-REFS/MKA-PARTICIPANT-REF), role (MacSecRoleEnum, element ROLE)
and sourceMacAddress (MacAddressString, element SOURCE-MAC-ADDRESS).
"""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import MacAddressString, PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import MacSecLocalKayProps, MacSecRoleEnum
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
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
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
    props.setGlobalKayProps(_ref("/Sec/MacSecGlobalKay"))
    props.setKeyServerPriority(_pos_int("16"))
    props.addMkaParticipant(_ref("/Sec/MkaParticipant1"))
    props.addMkaParticipant(_ref("/Sec/MkaParticipant2"))
    props.setRole(_role("keyServer"))
    props.setSourceMacAddress(_mac("AA-BB-CC-DD-EE-FF"))
    return props


class TestWriteMacSecLocalKayProps:
    def test_write_all_fields(self, writer):
        props = _new_mac_sec_local_kay_props()
        parent = ET.Element("CONFIGS")
        writer.setMacSecLocalKayProps(parent, "MAC-SEC-KAY-CONFIG", props)

        node = parent.find("MAC-SEC-KAY-CONFIG")
        assert node is not None
        assert node.find("DESTINATION-MAC-ADDRESS").text == "00-11-22-33-44-55"
        assert node.find("GLOBAL-KAY-PROPS").text == "/Sec/MacSecGlobalKay"
        assert node.find("KEY-SERVER-PRIORITY").text == "16"
        mka_refs = node.findall("MKA-PARTICIPANT-REFS/MKA-PARTICIPANT-REF")
        assert [r.text for r in mka_refs] == ["/Sec/MkaParticipant1", "/Sec/MkaParticipant2"]
        assert node.find("ROLE").text == "keyServer"
        assert node.find("SOURCE-MAC-ADDRESS").text == "AA-BB-CC-DD-EE-FF"

    def test_write_empty_omits_fields(self, writer):
        props = MacSecLocalKayProps()
        parent = ET.Element("CONFIGS")
        writer.setMacSecLocalKayProps(parent, "MAC-SEC-KAY-CONFIG", props)

        node = parent.find("MAC-SEC-KAY-CONFIG")
        assert node is not None
        assert node.find("DESTINATION-MAC-ADDRESS") is None
        assert node.find("GLOBAL-KAY-PROPS") is None
        assert node.find("KEY-SERVER-PRIORITY") is None
        assert node.find("MKA-PARTICIPANT-REFS") is None
        assert node.find("ROLE") is None
        assert node.find("SOURCE-MAC-ADDRESS") is None


class TestMacSecLocalKayPropsRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, parser, tmp_path):
        props = _new_mac_sec_local_kay_props()

        parent = ET.Element("CONFIGS")
        writer.setMacSecLocalKayProps(parent, "MAC-SEC-KAY-CONFIG", props)

        out_file = str(tmp_path / "mac_sec_local_kay_props.arxml")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(ET.tostring(_wrap(parent), encoding="unicode"))

        tree = ET.parse(out_file)
        recovered = parser.getMacSecLocalKayProps(tree.getroot()[0][0])

        assert recovered.getDestinationMacAddress().getValue() == "00-11-22-33-44-55"
        assert recovered.getGlobalKayProps().getValue() == "/Sec/MacSecGlobalKay"
        assert recovered.getKeyServerPriority().getValue() == 16
        assert [r.getValue() for r in recovered.getMkaParticipant()] == ["/Sec/MkaParticipant1", "/Sec/MkaParticipant2"]
        assert recovered.getRole().getValue() == "keyServer"
        assert recovered.getSourceMacAddress().getValue() == "AA-BB-CC-DD-EE-FF"

    def test_reader_empty_fields(self, parser):
        xml = "<AUTOSAR xmlns='%s'>" "<CONFIGS><MAC-SEC-KAY-CONFIG/></CONFIGS>" "</AUTOSAR>" % NS
        root = ET.fromstring(xml)
        recovered = parser.getMacSecLocalKayProps(root[0][0])

        assert recovered.getDestinationMacAddress() is None
        assert recovered.getGlobalKayProps() is None
        assert recovered.getKeyServerPriority() is None
        assert recovered.getMkaParticipant() == []
        assert recovered.getRole() is None
        assert recovered.getSourceMacAddress() is None

    def test_reader_empty_wrapper_list(self, parser):
        xml = "<AUTOSAR xmlns='%s'>" "<CONFIGS><MAC-SEC-KAY-CONFIG><MKA-PARTICIPANT-REFS/></MAC-SEC-KAY-CONFIG></CONFIGS>" "</AUTOSAR>" % NS
        root = ET.fromstring(xml)
        recovered = parser.getMacSecLocalKayProps(root[0][0])

        assert recovered.getMkaParticipant() == []
