"""Writer/reader round-trip tests for GlobalTimeDomain (Table 9.1, p.859)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    CanGlobalTimeDomainProps,
    GlobalTimeCorrectionProps,
    NetworkSegmentIdentification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import GlobalTimeDomain
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    GlobalTimeCanMaster,
    GlobalTimeCanSlave,
    GlobalTimeGateway,
    UserDefinedGlobalTimeSlave,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    RefType,
    String,
    TimeValue,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    autosar = AUTOSAR.getInstance()
    autosar.new()
    autosar.setARRelease("R23-11")
    yield
    autosar.new()


@pytest.fixture
def writer():
    return ARXMLWriter()


@pytest.fixture
def parser():
    return ARXMLParser()


def _new_domain():
    domain = GlobalTimeDomain(None, "domain1")
    domain.setUuid(String().setValue("1a2b3c4d-5e6f-4aaa-bbbc-2e3f4a5b6c7d"))
    domain.setDebounceTime(TimeValue().setValue("0.5"))
    domain.setDomainId(PositiveInteger().setValue(8))
    gateway = domain.createGlobalTimeGateway("gateway1")
    gateway.setHostRef(RefType().setValue("/Ecu/Ecu1").setDest("ECU-INSTANCE"))
    correction_props = GlobalTimeCorrectionProps()
    correction_props.setOffsetCorrectionJumpThreshold(TimeValue().setValue("0.2"))
    domain.setGlobalTimeCorrectionProps(correction_props)
    can_props = CanGlobalTimeDomainProps()
    can_props.addFupDataIDList(PositiveInteger().setValue(16))
    domain.setGlobalTimeDomainProperty(can_props)
    master = domain.createGlobalTimeCanMaster("master1")
    master.setSyncPeriod(TimeValue().setValue("0.2"))
    domain.addGlobalTimeSubDomainRef(RefType().setValue("/TimeDomains/Sub1").setDest("GLOBAL-TIME-DOMAIN"))
    domain.addGlobalTimeSubDomainRef(RefType().setValue("/TimeDomains/Sub2").setDest("GLOBAL-TIME-DOMAIN"))
    segment = NetworkSegmentIdentification()
    segment.setNetworkSegmentId(PositiveInteger().setValue(5))
    domain.setNetworkSegmentId(segment)
    domain.setOffsetTimeDomainRef(RefType().setValue("/TimeDomains/Base1").setDest("GLOBAL-TIME-DOMAIN"))
    domain.setPduTriggeringRef(RefType().setValue("/Com/Triggering1").setDest("PDU-TRIGGERING"))
    slave = domain.createGlobalTimeCanSlave("slave1")
    slave.setCommunicationConnectorRef(RefType().setValue("/Clusters/Cluster1/Connector1").setDest("CAN-COMMUNICATION-CONNECTOR"))
    domain.createUserDefinedGlobalTimeSlave("slave2")
    domain.setSyncLossTimeout(TimeValue().setValue("1.0"))
    return domain


class TestWriteGlobalTimeDomain:
    def test_write_all_elements_in_xsd_order(self, writer):
        """
        The helper writes the SHORT-NAME first, then the twelve Table 9.1 members in
        the XSD group element order; the aggregation wrappers are emitted only when
        non-empty.
        """
        parent = ET.Element("AR-PACKAGE")
        writer.writeGlobalTimeDomain(parent, _new_domain())

        element = parent[0]
        assert element.tag == "GLOBAL-TIME-DOMAIN"
        assert element.attrib["UUID"] == "1a2b3c4d-5e6f-4aaa-bbbc-2e3f4a5b6c7d"
        assert [child.tag for child in element][0] == "SHORT-NAME"
        assert element.find("SHORT-NAME").text == "domain1"

        assert element.find("DEBOUNCE-TIME").text == "0.5"
        assert element.find("DOMAIN-ID").text == "8"

        gateways = element.find("GATEWAYS")
        assert [child.tag for child in gateways] == ["GLOBAL-TIME-GATEWAY"]
        assert gateways[0].find("SHORT-NAME").text == "gateway1"
        assert gateways[0].find("HOST-REF").text == "/Ecu/Ecu1"
        assert gateways[0].find("HOST-REF").attrib["DEST"] == "ECU-INSTANCE"

        assert element.find("GLOBAL-TIME-CORRECTION-PROPS/OFFSET-CORRECTION-JUMP-THRESHOLD").text == "0.2"

        propertys = element.find("GLOBAL-TIME-DOMAIN-PROPERTYS")
        assert [child.tag for child in propertys] == ["CAN-GLOBAL-TIME-DOMAIN-PROPS"]
        assert propertys[0].find("FUP-DATA-ID-LISTS/FUP-DATA-ID-LIST").text == "16"

        masters = element.find("GLOBAL-TIME-MASTERS")
        assert [child.tag for child in masters] == ["GLOBAL-TIME-CAN-MASTER"]
        assert masters[0].find("SHORT-NAME").text == "master1"
        assert masters[0].find("SYNC-PERIOD").text == "0.2"

        sub_domains = element.find("GLOBAL-TIME-SUB-DOMAINS")
        assert [child.tag for child in sub_domains] == ["GLOBAL-TIME-DOMAIN-REF-CONDITIONAL", "GLOBAL-TIME-DOMAIN-REF-CONDITIONAL"]
        assert sub_domains[0].find("GLOBAL-TIME-DOMAIN-REF").text == "/TimeDomains/Sub1"
        assert sub_domains[0].find("GLOBAL-TIME-DOMAIN-REF").attrib["DEST"] == "GLOBAL-TIME-DOMAIN"
        assert sub_domains[1].find("GLOBAL-TIME-DOMAIN-REF").text == "/TimeDomains/Sub2"

        assert element.find("NETWORK-SEGMENT-ID/NETWORK-SEGMENT-ID").text == "5"

        assert element.find("OFFSET-TIME-DOMAIN-REF").text == "/TimeDomains/Base1"

        pdu_triggerings = element.find("PDU-TRIGGERINGS")
        assert [child.tag for child in pdu_triggerings] == ["PDU-TRIGGERING-REF-CONDITIONAL"]
        assert pdu_triggerings[0].find("PDU-TRIGGERING-REF").text == "/Com/Triggering1"
        assert pdu_triggerings[0].find("PDU-TRIGGERING-REF").attrib["DEST"] == "PDU-TRIGGERING"

        slaves = element.find("SLAVES")
        assert [child.tag for child in slaves] == ["GLOBAL-TIME-CAN-SLAVE", "USER-DEFINED-GLOBAL-TIME-SLAVE"]
        assert slaves[0].find("SHORT-NAME").text == "slave1"
        assert slaves[0].find("COMMUNICATION-CONNECTOR-REF").text == "/Clusters/Cluster1/Connector1"
        assert slaves[1].find("SHORT-NAME").text == "slave2"

        assert element.find("SYNC-LOSS-TIMEOUT").text == "1.0"

        tags = [child.tag for child in element]
        assert (
            tags.index("DEBOUNCE-TIME")
            < tags.index("DOMAIN-ID")
            < tags.index("GATEWAYS")
            < tags.index("GLOBAL-TIME-CORRECTION-PROPS")
            < tags.index("GLOBAL-TIME-DOMAIN-PROPERTYS")
            < tags.index("GLOBAL-TIME-MASTERS")
            < tags.index("GLOBAL-TIME-SUB-DOMAINS")
            < tags.index("NETWORK-SEGMENT-ID")
            < tags.index("OFFSET-TIME-DOMAIN-REF")
            < tags.index("PDU-TRIGGERINGS")
            < tags.index("SLAVES")
            < tags.index("SYNC-LOSS-TIMEOUT")
        )

    def test_write_empty_element(self, writer):
        """
        A domain without members emits no aggregation wrappers.
        """
        parent = ET.Element("AR-PACKAGE")
        writer.writeGlobalTimeDomain(parent, GlobalTimeDomain(None, "domain2"))

        element = parent[0]
        assert element.find("GATEWAYS") is None
        assert element.find("GLOBAL-TIME-CORRECTION-PROPS") is None
        assert element.find("GLOBAL-TIME-DOMAIN-PROPERTYS") is None
        assert element.find("GLOBAL-TIME-MASTERS") is None
        assert element.find("GLOBAL-TIME-SUB-DOMAINS") is None
        assert element.find("NETWORK-SEGMENT-ID") is None
        assert element.find("PDU-TRIGGERINGS") is None
        assert element.find("SLAVES") is None


class TestGlobalTimeDomainRoundTrip:
    def test_round_trip_preserves_field_values(self, writer, parser):
        """
        Write -> serialize -> parse keeps every field value including the concrete
        subtype elements inside the aggregation wrappers.
        """
        parent = ET.Element("AR-PACKAGE")
        writer.writeGlobalTimeDomain(parent, _new_domain())
        xml = ET.tostring(parent[0], encoding="unicode")

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        domain = parser.readGlobalTimeDomain(parsed_element, GlobalTimeDomain(None, "domain1"))

        assert domain.getShortName() == "domain1"
        assert domain.getUuid().getValue() == "1a2b3c4d-5e6f-4aaa-bbbc-2e3f4a5b6c7d"
        assert domain.getDebounceTime().getValue() == pytest.approx(0.5)
        assert domain.getDomainId().getValue() == 8

        gateways = domain.getGateways()
        assert len(gateways) == 1
        assert isinstance(gateways[0], GlobalTimeGateway)
        assert gateways[0].getShortName() == "gateway1"
        assert gateways[0].getHostRef().getValue() == "/Ecu/Ecu1"

        assert domain.getGlobalTimeCorrectionProps().getOffsetCorrectionJumpThreshold().getValue() == pytest.approx(0.2)

        props = domain.getGlobalTimeDomainProperty()
        assert isinstance(props, CanGlobalTimeDomainProps)
        assert props.getFupDataIDLists()[0].getValue() == 16

        master = domain.getGlobalTimeMaster()
        assert isinstance(master, GlobalTimeCanMaster)
        assert master.getShortName() == "master1"
        assert master.getSyncPeriod().getValue() == pytest.approx(0.2)

        refs = domain.getGlobalTimeSubDomainRefs()
        assert [ref.getValue() for ref in refs] == ["/TimeDomains/Sub1", "/TimeDomains/Sub2"]

        assert domain.getNetworkSegmentId().getNetworkSegmentId().getValue() == 5
        assert domain.getOffsetTimeDomainRef().getValue() == "/TimeDomains/Base1"
        assert domain.getPduTriggeringRef().getValue() == "/Com/Triggering1"

        slaves = domain.getSlaves()
        assert len(slaves) == 2
        assert isinstance(slaves[0], GlobalTimeCanSlave)
        assert slaves[0].getShortName() == "slave1"
        assert slaves[0].getCommunicationConnectorRef().getValue() == "/Clusters/Cluster1/Connector1"
        assert isinstance(slaves[1], UserDefinedGlobalTimeSlave)
        assert slaves[1].getShortName() == "slave2"

        assert domain.getSyncLossTimeout().getValue() == pytest.approx(1.0)
