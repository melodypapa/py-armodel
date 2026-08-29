"""Writer/reader round-trip tests for CouplingPortRatePolicy (Table 3.69, p.124)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    CouplingPortDetails,
    CouplingPortRatePolicy,
    CouplingPortRatePolicyActionEnum,
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


def _ref(value, dest=None):
    ref = RefType()
    ref.setValue(value)
    if dest is not None:
        ref.setDest(dest)
    return ref


def _full_policy():
    policy = CouplingPortRatePolicy()
    policy.setDataLength(_pos_int("1500"))
    policy.setPolicyAction(CouplingPortRatePolicyActionEnum().setValue(CouplingPortRatePolicyActionEnum.BLOCK_SOURCE))
    policy.setPriority(_pos_int("5"))
    policy.setTimeInterval(TimeValue().setValue("0.01"))
    policy.addVlanRef(_ref("/Clusters/EthCluster/Vlan1", "ETHERNET-PHYSICAL-CHANNEL"))
    policy.addVlanRef(_ref("/Clusters/EthCluster/Vlan2", "ETHERNET-PHYSICAL-CHANNEL"))
    return policy


def _new_details():
    details = CouplingPortDetails()
    details.addRatePolicy(_full_policy())
    minimal = CouplingPortRatePolicy()
    minimal.setPolicyAction(CouplingPortRatePolicyActionEnum().setValue(CouplingPortRatePolicyActionEnum.DROP_FRAME))
    details.addRatePolicy(minimal)
    return details


class TestWriteCouplingPortRatePolicy:
    def test_write_all_fields(self, writer):
        parent = ET.Element("PARENT")
        writer.setCouplingPortDetails(parent, "COUPLING-PORT-DETAILS", _new_details())
        node = parent.find("COUPLING-PORT-DETAILS")
        assert node is not None

        wrapper = node.find("RATE-POLICYS")
        assert wrapper is not None
        policies = wrapper.findall("COUPLING-PORT-RATE-POLICY")
        assert len(policies) == 2

        first = policies[0]
        assert [child.tag for child in first] == [
            "DATA-LENGTH",
            "POLICY-ACTION",
            "PRIORITY",
            "TIME-INTERVAL",
            "V-LAN-REFS",
        ]
        assert first.find("DATA-LENGTH").text == "1500"
        assert first.find("POLICY-ACTION").text == "blockSource"
        assert first.find("PRIORITY").text == "5"
        assert first.find("TIME-INTERVAL").text == "0.01"
        vlan_refs = first.findall("V-LAN-REFS/V-LAN-REF")
        assert len(vlan_refs) == 2
        assert vlan_refs[0].text == "/Clusters/EthCluster/Vlan1"
        assert vlan_refs[0].get("DEST") == "ETHERNET-PHYSICAL-CHANNEL"
        assert vlan_refs[1].text == "/Clusters/EthCluster/Vlan2"

        second = policies[1]
        assert second.find("POLICY-ACTION").text == "dropFrame"
        assert second.find("DATA-LENGTH") is None

    def test_write_empty_omits_wrapper(self, writer):
        parent = ET.Element("PARENT")
        writer.setCouplingPortDetails(parent, "COUPLING-PORT-DETAILS", CouplingPortDetails())
        node = parent.find("COUPLING-PORT-DETAILS")
        assert node is not None
        assert node.find("RATE-POLICYS") is None


class TestCouplingPortRatePolicyRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, parser):
        parent = ET.Element("PARENT")
        writer.setCouplingPortDetails(parent, "COUPLING-PORT-DETAILS", _new_details())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))
        parsed = parser.getCouplingPortDetails(root[0], "COUPLING-PORT-DETAILS")

        policies = parsed.getRatePolicies()
        assert len(policies) == 2
        assert isinstance(policies[0], CouplingPortRatePolicy)

        first = policies[0]
        assert isinstance(first, ARObject)
        assert first.getDataLength().getValue() == 1500
        assert first.getPolicyAction().getValue() == "blockSource"
        assert first.getPriority().getValue() == 5
        assert first.getTimeInterval().getValue() == 0.01
        vlan_refs = first.getVlanRefs()
        assert len(vlan_refs) == 2
        assert vlan_refs[0].getValue() == "/Clusters/EthCluster/Vlan1"
        assert vlan_refs[0].getDest() == "ETHERNET-PHYSICAL-CHANNEL"
        assert vlan_refs[1].getValue() == "/Clusters/EthCluster/Vlan2"

        second = policies[1]
        assert second.getPolicyAction().getValue() == "dropFrame"
        assert second.getDataLength() is None
        assert second.getVlanRefs() == []

    def test_reader_empty_fields(self, parser):
        parent = ET.fromstring("<PARENT xmlns='%s'><COUPLING-PORT-DETAILS/></PARENT>" % NS)
        parsed = parser.getCouplingPortDetails(parent, "COUPLING-PORT-DETAILS")
        assert isinstance(parsed, CouplingPortDetails)
        assert parsed.getRatePolicies() == []
