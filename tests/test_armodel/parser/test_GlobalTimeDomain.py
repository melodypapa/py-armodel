"""Reader tests for the GlobalTimeDomain aggregator (Table 9.1, p.859)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    CanGlobalTimeDomainProps,
    EthGlobalTimeDomainProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import GlobalTimeDomain
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    GlobalTimeCanMaster,
    GlobalTimeCanSlave,
    GlobalTimeGateway,
    UserDefinedGlobalTimeSlave,
)
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


class TestReadGlobalTimeDomain:
    def test_read_all_elements(self, parser):
        """
        All twelve Table 9.1 rows are read: the two attr rows, the four aggregation
        wrappers (GATEWAYS, GLOBAL-TIME-CORRECTION-PROPS, GLOBAL-TIME-DOMAIN-PROPERTYS,
        GLOBAL-TIME-MASTERS, SLAVES), the two REF-CONDITIONAL wrappers and the
        NETWORK-SEGMENT-ID element.
        """
        element = ET.fromstring(
            "<GLOBAL-TIME-DOMAIN xmlns='%s' UUID='1a2b3c4d-5e6f-4aaa-bbbc-2e3f4a5b6c7d'>"
            "<SHORT-NAME>domain1</SHORT-NAME>"
            "<DEBOUNCE-TIME>0.5</DEBOUNCE-TIME>"
            "<DOMAIN-ID>8</DOMAIN-ID>"
            "<GATEWAYS>"
            "<GLOBAL-TIME-GATEWAY><SHORT-NAME>gateway1</SHORT-NAME>"
            "<HOST-REF DEST='ECU-INSTANCE'>/Ecu/Ecu1</HOST-REF>"
            "</GLOBAL-TIME-GATEWAY>"
            "</GATEWAYS>"
            "<GLOBAL-TIME-CORRECTION-PROPS>"
            "<OFFSET-CORRECTION-JUMP-THRESHOLD>0.2</OFFSET-CORRECTION-JUMP-THRESHOLD>"
            "</GLOBAL-TIME-CORRECTION-PROPS>"
            "<GLOBAL-TIME-DOMAIN-PROPERTYS>"
            "<CAN-GLOBAL-TIME-DOMAIN-PROPS>"
            "<FUP-DATA-ID-LISTS><FUP-DATA-ID-LIST>16</FUP-DATA-ID-LIST></FUP-DATA-ID-LISTS>"
            "</CAN-GLOBAL-TIME-DOMAIN-PROPS>"
            "</GLOBAL-TIME-DOMAIN-PROPERTYS>"
            "<GLOBAL-TIME-MASTERS>"
            "<GLOBAL-TIME-CAN-MASTER><SHORT-NAME>master1</SHORT-NAME>"
            "<SYNC-PERIOD>0.2</SYNC-PERIOD>"
            "</GLOBAL-TIME-CAN-MASTER>"
            "</GLOBAL-TIME-MASTERS>"
            "<GLOBAL-TIME-SUB-DOMAINS>"
            "<GLOBAL-TIME-DOMAIN-REF-CONDITIONAL>"
            "<GLOBAL-TIME-DOMAIN-REF DEST='GLOBAL-TIME-DOMAIN'>/TimeDomains/Sub1</GLOBAL-TIME-DOMAIN-REF>"
            "</GLOBAL-TIME-DOMAIN-REF-CONDITIONAL>"
            "<GLOBAL-TIME-DOMAIN-REF-CONDITIONAL>"
            "<GLOBAL-TIME-DOMAIN-REF DEST='GLOBAL-TIME-DOMAIN'>/TimeDomains/Sub2</GLOBAL-TIME-DOMAIN-REF>"
            "</GLOBAL-TIME-DOMAIN-REF-CONDITIONAL>"
            "</GLOBAL-TIME-SUB-DOMAINS>"
            "<NETWORK-SEGMENT-ID><NETWORK-SEGMENT-ID>5</NETWORK-SEGMENT-ID></NETWORK-SEGMENT-ID>"
            "<OFFSET-TIME-DOMAIN-REF DEST='GLOBAL-TIME-DOMAIN'>/TimeDomains/Base1</OFFSET-TIME-DOMAIN-REF>"
            "<PDU-TRIGGERINGS>"
            "<PDU-TRIGGERING-REF-CONDITIONAL>"
            "<PDU-TRIGGERING-REF DEST='PDU-TRIGGERING'>/Com/Triggering1</PDU-TRIGGERING-REF>"
            "</PDU-TRIGGERING-REF-CONDITIONAL>"
            "</PDU-TRIGGERINGS>"
            "<SLAVES>"
            "<GLOBAL-TIME-CAN-SLAVE><SHORT-NAME>slave1</SHORT-NAME>"
            "<CRC-VALIDATED>CRC-VALIDATED</CRC-VALIDATED>"
            "<SEQUENCE-COUNTER-JUMP-WIDTH>2</SEQUENCE-COUNTER-JUMP-WIDTH>"
            "</GLOBAL-TIME-CAN-SLAVE>"
            "</SLAVES>"
            "<SYNC-LOSS-TIMEOUT>1.0</SYNC-LOSS-TIMEOUT>"
            "</GLOBAL-TIME-DOMAIN>" % NS
        )

        domain = parser.readGlobalTimeDomain(element, GlobalTimeDomain(None, "domain1"))

        assert domain.getShortName() == "domain1"
        assert domain.getUuid().getValue() == "1a2b3c4d-5e6f-4aaa-bbbc-2e3f4a5b6c7d"
        assert domain.getDebounceTime().getValue() == pytest.approx(0.5)
        assert domain.getDomainId().getValue() == 8

        gateways = domain.getGateways()
        assert len(gateways) == 1
        assert isinstance(gateways[0], GlobalTimeGateway)
        assert gateways[0].getShortName() == "gateway1"
        assert gateways[0].getHostRef().getValue() == "/Ecu/Ecu1"
        assert gateways[0].getHostRef().getDest() == "ECU-INSTANCE"

        assert domain.getGlobalTimeCorrectionProps().getOffsetCorrectionJumpThreshold().getValue() == pytest.approx(0.2)

        props = domain.getGlobalTimeDomainProperty()
        assert isinstance(props, CanGlobalTimeDomainProps)
        assert len(props.getFupDataIDLists()) == 1
        assert props.getFupDataIDLists()[0].getValue() == 16

        master = domain.getGlobalTimeMaster()
        assert isinstance(master, GlobalTimeCanMaster)
        assert master.getShortName() == "master1"
        assert master.getSyncPeriod().getValue() == pytest.approx(0.2)

        refs = domain.getGlobalTimeSubDomainRefs()
        assert [ref.getValue() for ref in refs] == ["/TimeDomains/Sub1", "/TimeDomains/Sub2"]
        assert refs[0].getDest() == "GLOBAL-TIME-DOMAIN"

        assert domain.getNetworkSegmentId().getNetworkSegmentId().getValue() == 5

        assert domain.getOffsetTimeDomainRef().getValue() == "/TimeDomains/Base1"
        assert domain.getOffsetTimeDomainRef().getDest() == "GLOBAL-TIME-DOMAIN"

        assert domain.getPduTriggeringRef().getValue() == "/Com/Triggering1"
        assert domain.getPduTriggeringRef().getDest() == "PDU-TRIGGERING"

        slaves = domain.getSlaves()
        assert len(slaves) == 1
        assert isinstance(slaves[0], GlobalTimeCanSlave)
        assert slaves[0].getShortName() == "slave1"
        assert slaves[0].getCrcValidated().getValue() == "CRC-VALIDATED"
        assert slaves[0].getSequenceCounterJumpWidth().getValue() == 2

        assert domain.getSyncLossTimeout().getValue() == pytest.approx(1.0)

    def test_read_dispatches_concrete_subtypes(self, parser):
        """
        The GLOBAL-TIME-DOMAIN-PROPERTYS and SLAVES wrapper dispatches construct the
        concrete Eth props / UserDefined slave subclasses.
        """
        element = ET.fromstring(
            "<GLOBAL-TIME-DOMAIN xmlns='%s'>"
            "<SHORT-NAME>domain2</SHORT-NAME>"
            "<GLOBAL-TIME-DOMAIN-PROPERTYS>"
            "<ETH-GLOBAL-TIME-DOMAIN-PROPS>"
            "<VLAN-PRIORITY>6</VLAN-PRIORITY>"
            "</ETH-GLOBAL-TIME-DOMAIN-PROPS>"
            "</GLOBAL-TIME-DOMAIN-PROPERTYS>"
            "<SLAVES>"
            "<USER-DEFINED-GLOBAL-TIME-SLAVE><SHORT-NAME>slave2</SHORT-NAME></USER-DEFINED-GLOBAL-TIME-SLAVE>"
            "</SLAVES>"
            "</GLOBAL-TIME-DOMAIN>" % NS
        )

        domain = parser.readGlobalTimeDomain(element, GlobalTimeDomain(None, "domain2"))

        props = domain.getGlobalTimeDomainProperty()
        assert isinstance(props, EthGlobalTimeDomainProps)
        assert props.getVlanPriority().getValue() == 6

        slaves = domain.getSlaves()
        assert len(slaves) == 1
        assert isinstance(slaves[0], UserDefinedGlobalTimeSlave)
        assert slaves[0].getShortName() == "slave2"

    def test_read_empty_element(self, parser):
        """
        A domain without group content leaves all fields unset.
        """
        element = ET.fromstring("<GLOBAL-TIME-DOMAIN xmlns='%s'><SHORT-NAME>domain3</SHORT-NAME></GLOBAL-TIME-DOMAIN>" % NS)

        domain = parser.readGlobalTimeDomain(element, GlobalTimeDomain(None, "domain3"))

        assert domain.getDebounceTime() is None
        assert domain.getDomainId() is None
        assert domain.getGateways() == []
        assert domain.getGlobalTimeCorrectionProps() is None
        assert domain.getGlobalTimeDomainProperty() is None
        assert domain.getGlobalTimeMaster() is None
        assert domain.getGlobalTimeSubDomainRefs() == []
        assert domain.getNetworkSegmentId() is None
        assert domain.getOffsetTimeDomainRef() is None
        assert domain.getPduTriggeringRef() is None
        assert domain.getSlaves() == []
        assert domain.getSyncLossTimeout() is None
