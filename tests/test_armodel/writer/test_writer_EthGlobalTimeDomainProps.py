"""Writer/reader round-trip tests for EthGlobalTimeDomainProps (Table 9.14, p.867)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    EthGlobalTimeDomainProps,
    EthGlobalTimeManagedCouplingPort,
    EthTSynCrcFlags,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    EthGlobalTimeMessageFormatEnum,
    Identifier,
    MacAddressString,
    PositiveInteger,
    RefType,
    String,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
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
    return ARXMLWriter()


@pytest.fixture
def parser():
    return ARXMLParser()


def _new_props():
    props = EthGlobalTimeDomainProps()
    props.setChecksum(String().setValue("11"))
    variation_point = VariationPoint()
    variation_point.setShortLabel(Identifier().setValue("vpLabel"))
    props.setVariationPoint(variation_point)

    crc_flags = EthTSynCrcFlags()
    crc_flags.setCrcSequenceId(Boolean().setValue("true"))
    props.setCrcFlags(crc_flags)

    props.setDestinationPhysicalAddress(MacAddressString().setValue("01:80:C2:00:00:0E"))
    props.addFupDataIDList(PositiveInteger().setValue("1"))
    props.addFupDataIDList(PositiveInteger().setValue("2"))

    port = EthGlobalTimeManagedCouplingPort()
    ref = RefType()
    ref.setValue("/Cluster/CouplingPort1")
    ref.setDest("COUPLING-PORT")
    port.setCouplingPortRef(ref)
    props.addManagedCouplingPort(port)

    props.setMessageCompliance(EthGlobalTimeMessageFormatEnum().setValue(EthGlobalTimeMessageFormatEnum.IEEE802_1AS))
    props.setVlanPriority(PositiveInteger().setValue("5"))
    return props


class TestWriteEthGlobalTimeDomainProps:
    def test_write_all_elements_in_xsd_order(self, writer):
        """
        The helper writes the VARIATION-POINT (inherited abstract group) first and then the six
        Table 9.14 elements in the XSD ETH-GLOBAL-TIME-DOMAIN-PROPS group order; the two wrapper
        elements are emitted only when non-empty.
        """
        element = ET.Element("ETH-GLOBAL-TIME-DOMAIN-PROPS")
        writer.writeEthGlobalTimeDomainProps(element, _new_props())

        assert element.attrib["S"] == "11"
        assert [child.tag for child in element] == [
            "VARIATION-POINT",
            "CRC-FLAGS",
            "DESTINATION-PHYSICAL-ADDRESS",
            "FUP-DATA-ID-LISTS",
            "MANAGED-COUPLING-PORTS",
            "MESSAGE-COMPLIANCE",
            "VLAN-PRIORITY",
        ]
        assert element.find("CRC-FLAGS").find("CRC-SEQUENCE-ID").text == "true"
        assert element.find("DESTINATION-PHYSICAL-ADDRESS").text == "01:80:C2:00:00:0E"
        fup_items = element.find("FUP-DATA-ID-LISTS").findall("FUP-DATA-ID-LIST")
        assert [item.text for item in fup_items] == ["1", "2"]
        port_element = element.find("MANAGED-COUPLING-PORTS").find("ETH-GLOBAL-TIME-MANAGED-COUPLING-PORT")
        assert port_element.find("COUPLING-PORT-REF").text == "/Cluster/CouplingPort1"
        assert port_element.find("COUPLING-PORT-REF").attrib["DEST"] == "COUPLING-PORT"
        assert element.find("MESSAGE-COMPLIANCE").text == "IEEE802-1AS"
        assert element.find("VLAN-PRIORITY").text == "5"

    def test_write_empty_element(self, writer):
        """
        With no attribute content, no wrapper elements are emitted.
        """
        element = ET.Element("ETH-GLOBAL-TIME-DOMAIN-PROPS")
        writer.writeEthGlobalTimeDomainProps(element, EthGlobalTimeDomainProps())

        assert len(element) == 0


class TestEthGlobalTimeDomainPropsRoundTrip:
    def test_round_trip_preserves_field_values(self, writer, parser):
        """
        Write -> serialize -> parse keeps the variation point and every Table 9.14 field value,
        including the aggregated CRC flags and managed coupling port one level down.
        """
        element = ET.Element("ETH-GLOBAL-TIME-DOMAIN-PROPS")
        writer.writeEthGlobalTimeDomainProps(element, _new_props())
        xml = ET.tostring(element, encoding="unicode")

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        props = parser.readEthGlobalTimeDomainProps(parsed_element, EthGlobalTimeDomainProps())

        assert props.getChecksum().getValue() == "11"
        assert props.getVariationPoint().getShortLabel().getValue() == "vpLabel"
        assert props.getCrcFlags().getCrcSequenceId().getValue() is True
        assert props.getDestinationPhysicalAddress().getValue() == "01:80:C2:00:00:0E"

        fup = props.getFupDataIDLists()
        assert len(fup) == 2
        assert fup[0].getValue() == 1
        assert fup[1].getValue() == 2

        ports = props.getManagedCouplingPorts()
        assert len(ports) == 1
        assert ports[0].getCouplingPortRef().getValue() == "/Cluster/CouplingPort1"
        assert ports[0].getCouplingPortRef().getDest() == "COUPLING-PORT"

        assert props.getMessageCompliance().getValue() == "IEEE802-1AS"
        assert props.getVlanPriority().getValue() == 5

    def test_round_trip_empty_wrapper_lists(self, writer, parser):
        """
        A props object without DataIDLists / managed coupling ports round-trips to empty lists
        (no wrapper tags emitted).
        """
        props = EthGlobalTimeDomainProps()
        props.setMessageCompliance(EthGlobalTimeMessageFormatEnum().setValue(EthGlobalTimeMessageFormatEnum.IEEE802_1AS_AUTOSAR))

        element = ET.Element("ETH-GLOBAL-TIME-DOMAIN-PROPS")
        writer.writeEthGlobalTimeDomainProps(element, props)
        xml = ET.tostring(element, encoding="unicode")

        assert "DATA-ID-LISTS" not in xml
        assert "MANAGED-COUPLING-PORTS" not in xml

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        parsed_props = parser.readEthGlobalTimeDomainProps(parsed_element, EthGlobalTimeDomainProps())

        assert parsed_props.getFupDataIDLists() == []
        assert parsed_props.getManagedCouplingPorts() == []
        assert parsed_props.getMessageCompliance().getValue() == "IEEE802-1AS-AUTOSAR"
        assert parsed_props.getCrcFlags() is None
        assert parsed_props.getDestinationPhysicalAddress() is None
        assert parsed_props.getVlanPriority() is None
