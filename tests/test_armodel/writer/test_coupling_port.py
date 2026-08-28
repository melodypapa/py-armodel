"""Writer/reader round-trip tests for CouplingPort (Table 3.54, p.110)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
    Boolean,
    MacAddressString,
    PositiveInteger,
    RefType,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    CouplingPort,
    CouplingPortDetails,
    PlcaProps,
    VlanMembership,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import (
    MacSecFailPermissiveModeEnum,
    MacSecLocalKayProps,
    MacSecProps,
    MacSecRoleEnum,
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


def _ref(value):
    ref = RefType()
    ref.setValue(value)
    return ref


def _pos_int(text):
    val = PositiveInteger()
    val.setValue(text)
    return val


def _literal(value):
    literal = ARLiteral()
    literal.setValue(value)
    return literal


def _new_port():
    port = CouplingPort(MockParent(), "CP1")
    port.setConnectionNegotiationBehavior(_literal("auto"))
    port.setCouplingPortDetails(CouplingPortDetails())
    port.setCouplingPortRole(_literal("edge"))
    port.setDefaultVlanRef(_ref("/Ether/PhysicalChannel/Vlan1"))
    port.setMacLayerType(_literal("ethernet"))
    port.addMacMulticastAddressRef(_ref("/Ether/MacMulticastGroup/MMG1"))
    port.setPhysicalLayerType(_literal("100BaseT1"))
    port.addPncMappingRef(_ref("/System/PncMapping/PM1"))
    port.setReceiveActivity(_literal("receiveActivityUntagged"))
    port.addVlanMembership(VlanMembership())
    port.setVlanModifierRef(_ref("/Ether/PhysicalChannel/Vlan2"))
    port.setWakeupSleepOnDatalineConfigRef(_ref("/Ether/WakeupConfig/WSD1"))
    return port


def _mac(value):
    mac = MacAddressString()
    mac.setValue(value)
    return mac


def _bool(value):
    b = Boolean()
    b.setValue(value)
    return b


def _time(value):
    t = TimeValue()
    t.setValue(value)
    return t


def _pos_int(value):
    p = PositiveInteger()
    p.setValue(value)
    return p


def _new_mac_sec_props():
    props = MacSecProps()
    props.setAutoStart(_bool("true"))
    kay = MacSecLocalKayProps()
    kay.setDestinationMacAddress(_mac("00-11-22-33-44-55"))
    kay.setGlobalKayProps(_ref("/Sec/MacSecGlobalKay"))
    kay.setKeyServerPriority(_pos_int("16"))
    kay.addMkaParticipant(_ref("/Sec/MkaParticipant1"))
    role = MacSecRoleEnum()
    role.setValue("KEY-SERVER")
    kay.setRole(role)
    kay.setSourceMacAddress(_mac("AA-BB-CC-DD-EE-FF"))
    props.setMacSecKayConfig(kay)
    fail_mode = MacSecFailPermissiveModeEnum()
    fail_mode.setValue("TIMEOUT")
    props.setOnFailPermissiveMode(fail_mode)
    props.setOnFailPermissiveModeTimeout(_time("30.0"))
    props.setSakRekeyTimeSpan(_time("3600.0"))
    return props


class TestWriteCouplingPort:
    def test_write_all_fields(self, writer):
        parent = ET.Element("PARENT")
        writer.writeCouplingPort(parent, _new_port())

        node = parent.find("COUPLING-PORT")
        assert node is not None
        assert node.find("CONNECTION-NEGOTIATION-BEHAVIOR").text == "auto"
        assert node.find("COUPLING-PORT-DETAILS") is not None
        assert node.find("COUPLING-PORT-ROLE").text == "edge"
        assert node.find("DEFAULT-VLAN-REF").text == "/Ether/PhysicalChannel/Vlan1"
        assert node.find("MAC-LAYER-TYPE").text == "ethernet"
        mc_refs = node.findall("MAC-MULTICAST-ADDRESS-REFS/MAC-MULTICAST-ADDRESS-REF")
        assert len(mc_refs) == 1
        pnc_refs = node.findall("PNC-MAPPING-REFS/PNC-MAPPING-REF")
        assert len(pnc_refs) == 1
        assert node.find("PHYSICAL-LAYER-TYPE").text == "100BaseT1"
        assert node.find("RECEIVE-ACTIVITY").text == "receiveActivityUntagged"
        assert node.find("VLAN-MEMBERSHIPS/VLAN-MEMBERSHIP") is not None
        assert node.find("VLAN-MODIFIER-REF").text == "/Ether/PhysicalChannel/Vlan2"
        assert node.find("WAKEUP-SLEEP-ON-DATALINE-CONFIG-REF").text == "/Ether/WakeupConfig/WSD1"

    def test_write_mac_sec_props(self, writer):
        port = _new_port()
        port.addMacSecProps(_new_mac_sec_props())
        parent = ET.Element("PARENT")
        writer.writeCouplingPort(parent, port)

        node = parent.find("COUPLING-PORT")
        mac_sec = node.find("MAC-SEC-PROPS")
        assert mac_sec is not None
        assert mac_sec.find("AUTO-START").text == "true"
        kay = mac_sec.find("MAC-SEC-KAY-CONFIG")
        assert kay is not None
        assert kay.find("DESTINATION-MAC-ADDRESS").text == "00-11-22-33-44-55"
        assert kay.find("GLOBAL-KAY-PROPS").text == "/Sec/MacSecGlobalKay"
        assert kay.find("KEY-SERVER-PRIORITY").text == "16"
        mka_refs = kay.findall("MKA-PARTICIPANT-REFS/MKA-PARTICIPANT-REF")
        assert len(mka_refs) == 1
        assert kay.find("ROLE").text == "KEY-SERVER"
        assert kay.find("SOURCE-MAC-ADDRESS").text == "AA-BB-CC-DD-EE-FF"
        assert mac_sec.find("ON-FAIL-PERMISSIVE-MODE").text == "TIMEOUT"
        assert mac_sec.find("ON-FAIL-PERMISSIVE-MODE-TIMEOUT").text == "30.0"
        assert mac_sec.find("SAK-REKEY-TIME-SPAN").text == "3600.0"

    def test_write_child_element_order_matches_xsd(self, writer):
        port = _new_port()
        port.setPlcaProps(PlcaProps())
        port.addMacSecProps(_new_mac_sec_props())
        parent = ET.Element("PARENT")
        writer.writeCouplingPort(parent, port)

        node = parent.find("COUPLING-PORT")
        # AUTOSAR_00052.xsd group COUPLING-PORT sequence; COUPLING-PORT-SPEED is
        # atp.Status=removed and VARIATION-POINT is framework-owned, so neither is modelled.
        xsd_order = [
            "CONNECTION-NEGOTIATION-BEHAVIOR",
            "COUPLING-PORT-DETAILS",
            "COUPLING-PORT-ROLE",
            "DEFAULT-VLAN-REF",
            "MAC-LAYER-TYPE",
            "MAC-MULTICAST-ADDRESS-REFS",
            "MAC-SEC-PROPS",
            "PHYSICAL-LAYER-TYPE",
            "PLCA-PROPS",
            "PNC-MAPPING-REFS",
            "RECEIVE-ACTIVITY",
            "VLAN-MEMBERSHIPS",
            "VLAN-MODIFIER-REF",
            "WAKEUP-SLEEP-ON-DATALINE-CONFIG-REF",
        ]
        emitted = [child.tag for child in node if child.tag in xsd_order]
        assert emitted == xsd_order


class TestCouplingPortRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, parser, tmp_path):
        parent = ET.Element("PARENT")
        writer.writeCouplingPort(parent, _new_port())

        out_file = str(tmp_path / "coupling_port.arxml")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(ET.tostring(_wrap(parent), encoding="unicode"))

        tree = ET.parse(out_file)
        recovered = CouplingPort(MockParent(), "CP1")
        parser.readCouplingPort(tree.getroot()[0][0], recovered)

        assert recovered.getConnectionNegotiationBehavior().getValue() == "auto"
        assert isinstance(recovered.getCouplingPortDetails(), CouplingPortDetails)
        assert recovered.getCouplingPortRole().getValue() == "edge"
        assert recovered.getDefaultVlanRef().getValue() == "/Ether/PhysicalChannel/Vlan1"
        assert recovered.getMacLayerType().getValue() == "ethernet"
        assert recovered.getMacMulticastAddressRefs()[0].getValue() == "/Ether/MacMulticastGroup/MMG1"
        assert recovered.getPncMappingRefs()[0].getValue() == "/System/PncMapping/PM1"
        assert recovered.getPhysicalLayerType().getValue() == "100BaseT1"
        assert recovered.getReceiveActivity().getValue() == "receiveActivityUntagged"
        assert len(recovered.getVlanMemberships()) == 1
        assert recovered.getVlanModifierRef().getValue() == "/Ether/PhysicalChannel/Vlan2"
        assert recovered.getWakeupSleepOnDatalineConfigRef().getValue() == "/Ether/WakeupConfig/WSD1"

    def test_reader_empty_fields(self, parser):
        element = ET.fromstring("<COUPLING-PORT xmlns='%s'><SHORT-NAME>Empty</SHORT-NAME></COUPLING-PORT>" % NS)
        recovered = CouplingPort(MockParent(), "Empty")
        parser.readCouplingPort(element, recovered)

        assert recovered.getShortName() == "Empty"
        assert recovered.getConnectionNegotiationBehavior() is None
        assert recovered.getCouplingPortDetails() is None
        assert recovered.getDefaultVlanRef() is None
        assert recovered.getMacMulticastAddressRefs() == []
        assert recovered.getPncMappingRefs() == []
        assert recovered.getVlanMemberships() == []
        assert recovered.getVlanModifierRef() is None
        assert recovered.getWakeupSleepOnDatalineConfigRef() is None

    def test_round_trip_mac_sec_props(self, writer, parser, tmp_path):
        port = _new_port()
        port.addMacSecProps(_new_mac_sec_props())
        parent = ET.Element("PARENT")
        writer.writeCouplingPort(parent, port)

        out_file = str(tmp_path / "coupling_port_mac_sec.arxml")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(ET.tostring(_wrap(parent), encoding="unicode"))

        tree = ET.parse(out_file)
        recovered = CouplingPort(MockParent(), "CP1")
        parser.readCouplingPort(tree.getroot()[0][0], recovered)

        assert len(recovered.getMacSecProps()) == 1
        props = recovered.getMacSecProps()[0]
        assert props.getAutoStart().getValue() is True
        kay = props.getMacSecKayConfig()
        assert isinstance(kay, MacSecLocalKayProps)
        assert kay.getDestinationMacAddress().getValue() == "00-11-22-33-44-55"
        assert kay.getGlobalKayProps().getValue() == "/Sec/MacSecGlobalKay"
        assert kay.getKeyServerPriority().getValue() == 16
        assert kay.getMkaParticipant()[0].getValue() == "/Sec/MkaParticipant1"
        assert kay.getRole().getValue() == "KEY-SERVER"
        assert kay.getSourceMacAddress().getValue() == "AA-BB-CC-DD-EE-FF"
        assert props.getOnFailPermissiveMode().getValue() == "TIMEOUT"
        assert props.getOnFailPermissiveModeTimeout().getValue() == 30.0
        assert props.getSakRekeyTimeSpan().getValue() == 3600.0


def _wrap(element: ET.Element) -> ET.Element:
    inner = ET.tostring(element).decode("utf-8")
    return ET.fromstring(f"<AUTOSAR xmlns='{NS}'>{inner}</AUTOSAR>")
