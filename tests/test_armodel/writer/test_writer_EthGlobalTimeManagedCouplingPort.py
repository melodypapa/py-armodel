"""Writer/reader round-trip tests for EthGlobalTimeManagedCouplingPort (Table 9.17, p.875)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import EthGlobalTimeManagedCouplingPort
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    GlobalTimePortRoleEnum,
    RefType,
    String,
    TimeValue,
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
    return ARXMLWriter()


@pytest.fixture
def parser():
    return ARXMLParser()


def _new_port():
    port = EthGlobalTimeManagedCouplingPort()
    port.setChecksum(String().setValue("7"))
    ref = RefType()
    ref.setValue("/Cluster/CouplingPort1")
    ref.setDest("COUPLING-PORT")
    port.setCouplingPortRef(ref)
    port.setGlobalTimePortRole(GlobalTimePortRoleEnum().setValue(GlobalTimePortRoleEnum.TIME_SLAVE))
    port.setGlobalTimeTxPeriod(TimeValue().setValue("0.25"))
    port.setPdelayLatencyThreshold(TimeValue().setValue("0.001"))
    port.setPdelayRequestPeriod(TimeValue().setValue("1.0"))
    port.setPdelayRespAndRespFollowUpTimeout(TimeValue().setValue("0.5"))
    port.setPdelayResponseEnabled(Boolean().setValue(True))
    return port


class TestWriteEthGlobalTimeManagedCouplingPort:
    def test_write_all_elements_in_xsd_order(self, writer):
        """
        The helper emits the ETH-GLOBAL-TIME-MANAGED-COUPLING-PORT element with its seven
        attributes in the XSD sequenceOffset order.
        """
        parent = ET.Element("ETH-GLOBAL-TIME-DOMAIN-PROPS")
        writer.writeEthGlobalTimeManagedCouplingPort(parent, _new_port())

        element = parent.find("ETH-GLOBAL-TIME-MANAGED-COUPLING-PORT")
        assert element is not None
        assert element.attrib["S"] == "7"
        assert [child.tag for child in element] == [
            "COUPLING-PORT-REF",
            "GLOBAL-TIME-PORT-ROLE",
            "GLOBAL-TIME-TX-PERIOD",
            "PDELAY-LATENCY-THRESHOLD",
            "PDELAY-REQUEST-PERIOD",
            "PDELAY-RESP-AND-RESP-FOLLOW-UP-TIMEOUT",
            "PDELAY-RESPONSE-ENABLED",
        ]
        assert element.find("COUPLING-PORT-REF").text == "/Cluster/CouplingPort1"
        assert element.find("COUPLING-PORT-REF").attrib["DEST"] == "COUPLING-PORT"
        assert element.find("GLOBAL-TIME-PORT-ROLE").text == "TIME-SLAVE"
        assert element.find("GLOBAL-TIME-TX-PERIOD").text == "0.25"
        assert element.find("PDELAY-LATENCY-THRESHOLD").text == "0.001"
        assert element.find("PDELAY-REQUEST-PERIOD").text == "1.0"
        assert element.find("PDELAY-RESP-AND-RESP-FOLLOW-UP-TIMEOUT").text == "0.5"
        assert element.find("PDELAY-RESPONSE-ENABLED").text == "true"

    def test_write_empty_element(self, writer):
        """
        An unset port emits the element without attribute content.
        """
        parent = ET.Element("ETH-GLOBAL-TIME-DOMAIN-PROPS")
        writer.writeEthGlobalTimeManagedCouplingPort(parent, EthGlobalTimeManagedCouplingPort())

        element = parent.find("ETH-GLOBAL-TIME-MANAGED-COUPLING-PORT")
        assert element is not None
        assert len(element) == 0


class TestEthGlobalTimeManagedCouplingPortRoundTrip:
    def test_round_trip_preserves_field_values(self, writer, parser):
        """
        Write -> serialize -> parse keeps every field value.
        """
        parent = ET.Element("ETH-GLOBAL-TIME-DOMAIN-PROPS")
        writer.writeEthGlobalTimeManagedCouplingPort(parent, _new_port())
        xml = ET.tostring(parent, encoding="unicode")

        parsed_parent = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))
        element = parsed_parent[0][0]
        port = EthGlobalTimeManagedCouplingPort()
        parser.readEthGlobalTimeManagedCouplingPort(element, port)

        assert port.getChecksum().getValue() == "7"
        assert port.getCouplingPortRef().getValue() == "/Cluster/CouplingPort1"
        assert port.getCouplingPortRef().getDest() == "COUPLING-PORT"
        assert port.getGlobalTimePortRole().getValue() == "TIME-SLAVE"
        assert port.getGlobalTimeTxPeriod().getValue() == pytest.approx(0.25)
        assert port.getPdelayLatencyThreshold().getValue() == pytest.approx(0.001)
        assert port.getPdelayRequestPeriod().getValue() == pytest.approx(1.0)
        assert port.getPdelayRespAndRespFollowUpTimeout().getValue() == pytest.approx(0.5)
        assert port.getPdelayResponseEnabled().getValue() is True
