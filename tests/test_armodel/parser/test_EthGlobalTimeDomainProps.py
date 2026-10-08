"""Reader tests for EthGlobalTimeDomainProps (Table 9.14, p.867)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import EthGlobalTimeDomainProps
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    from armodel.models import AUTOSAR

    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    return ARXMLParser()


class TestReadEthGlobalTimeDomainProps:
    def test_read_all_elements(self, parser):
        """
        All six Table 9.14 attributes plus the inherited VARIATION-POINT (abstract group) and the
        AR-OBJECT S attribute are read from the ETH-GLOBAL-TIME-DOMAIN-PROPS element; the CRC-FLAGS
        child dispatches to readEthTSynCrcFlags and the MANAGED-COUPLING-PORTS wrapper items to
        readEthGlobalTimeManagedCouplingPort.
        """
        element = ET.fromstring(
            "<ETH-GLOBAL-TIME-DOMAIN-PROPS xmlns='%s' S='11'>"
            "<VARIATION-POINT><SHORT-LABEL>vpLabel</SHORT-LABEL></VARIATION-POINT>"
            "<CRC-FLAGS><CRC-SEQUENCE-ID>true</CRC-SEQUENCE-ID></CRC-FLAGS>"
            "<DESTINATION-PHYSICAL-ADDRESS>01:80:C2:00:00:0E</DESTINATION-PHYSICAL-ADDRESS>"
            "<FUP-DATA-ID-LISTS>"
            "<FUP-DATA-ID-LIST>1</FUP-DATA-ID-LIST>"
            "<FUP-DATA-ID-LIST>2</FUP-DATA-ID-LIST>"
            "</FUP-DATA-ID-LISTS>"
            "<MANAGED-COUPLING-PORTS>"
            "<ETH-GLOBAL-TIME-MANAGED-COUPLING-PORT>"
            "<COUPLING-PORT-REF DEST='COUPLING-PORT'>/Cluster/CouplingPort1</COUPLING-PORT-REF>"
            "</ETH-GLOBAL-TIME-MANAGED-COUPLING-PORT>"
            "<ETH-GLOBAL-TIME-MANAGED-COUPLING-PORT>"
            "<COUPLING-PORT-REF DEST='COUPLING-PORT'>/Cluster/CouplingPort2</COUPLING-PORT-REF>"
            "</ETH-GLOBAL-TIME-MANAGED-COUPLING-PORT>"
            "</MANAGED-COUPLING-PORTS>"
            "<MESSAGE-COMPLIANCE>IEEE802-1AS</MESSAGE-COMPLIANCE>"
            "<VLAN-PRIORITY>5</VLAN-PRIORITY>"
            "</ETH-GLOBAL-TIME-DOMAIN-PROPS>" % NS
        )

        props = EthGlobalTimeDomainProps()
        parser.readEthGlobalTimeDomainProps(element, props)

        assert props.getChecksum().getValue() == "11"
        assert props.getVariationPoint().getShortLabel().getValue() == "vpLabel"

        crc_flags = props.getCrcFlags()
        assert crc_flags is not None
        assert crc_flags.getCrcSequenceId().getValue() is True

        assert props.getDestinationPhysicalAddress().getValue() == "01:80:C2:00:00:0E"

        fup = props.getFupDataIDLists()
        assert len(fup) == 2
        assert fup[0].getValue() == 1
        assert fup[1].getValue() == 2

        ports = props.getManagedCouplingPorts()
        assert len(ports) == 2
        assert ports[0].getCouplingPortRef().getValue() == "/Cluster/CouplingPort1"
        assert ports[0].getCouplingPortRef().getDest() == "COUPLING-PORT"
        assert ports[1].getCouplingPortRef().getValue() == "/Cluster/CouplingPort2"

        assert props.getMessageCompliance().getValue() == "IEEE802-1AS"
        assert props.getVlanPriority().getValue() == 5

    def test_read_empty_element(self, parser):
        """
        An element without attribute content leaves the fields unset and the lists empty.
        """
        element = ET.fromstring("<ETH-GLOBAL-TIME-DOMAIN-PROPS xmlns='%s'></ETH-GLOBAL-TIME-DOMAIN-PROPS>" % NS)

        props = EthGlobalTimeDomainProps()
        parser.readEthGlobalTimeDomainProps(element, props)

        assert props.getVariationPoint() is None
        assert props.getCrcFlags() is None
        assert props.getDestinationPhysicalAddress() is None
        assert props.getFupDataIDLists() == []
        assert props.getManagedCouplingPorts() == []
        assert props.getMessageCompliance() is None
        assert props.getVlanPriority() is None
