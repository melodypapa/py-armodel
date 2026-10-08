"""Reader tests for EthGlobalTimeManagedCouplingPort (Table 9.17, p.875)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import EthGlobalTimeManagedCouplingPort
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


class TestReadEthGlobalTimeManagedCouplingPort:
    def test_read_all_elements(self, parser):
        """
        All seven Table 9.17 attributes plus the AR-OBJECT S attribute are read from the
        ETH-GLOBAL-TIME-MANAGED-COUPLING-PORT element.
        """
        element = ET.fromstring(
            "<ETH-GLOBAL-TIME-MANAGED-COUPLING-PORT xmlns='%s' S='7'>"
            "<COUPLING-PORT-REF DEST='COUPLING-PORT'>/Cluster/CouplingPort1</COUPLING-PORT-REF>"
            "<GLOBAL-TIME-PORT-ROLE>TIME-SLAVE</GLOBAL-TIME-PORT-ROLE>"
            "<GLOBAL-TIME-TX-PERIOD>0.25</GLOBAL-TIME-TX-PERIOD>"
            "<PDELAY-LATENCY-THRESHOLD>0.001</PDELAY-LATENCY-THRESHOLD>"
            "<PDELAY-REQUEST-PERIOD>1.0</PDELAY-REQUEST-PERIOD>"
            "<PDELAY-RESP-AND-RESP-FOLLOW-UP-TIMEOUT>0.5</PDELAY-RESP-AND-RESP-FOLLOW-UP-TIMEOUT>"
            "<PDELAY-RESPONSE-ENABLED>true</PDELAY-RESPONSE-ENABLED>"
            "</ETH-GLOBAL-TIME-MANAGED-COUPLING-PORT>" % NS
        )

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

    def test_read_empty_element(self, parser):
        """
        An element without attribute content leaves the fields unset.
        """
        element = ET.fromstring("<ETH-GLOBAL-TIME-MANAGED-COUPLING-PORT xmlns='%s'></ETH-GLOBAL-TIME-MANAGED-COUPLING-PORT>" % NS)

        port = EthGlobalTimeManagedCouplingPort()
        parser.readEthGlobalTimeManagedCouplingPort(element, port)

        assert port.getCouplingPortRef() is None
        assert port.getGlobalTimePortRole() is None
        assert port.getGlobalTimeTxPeriod() is None
        assert port.getPdelayLatencyThreshold() is None
        assert port.getPdelayRequestPeriod() is None
        assert port.getPdelayRespAndRespFollowUpTimeout() is None
        assert port.getPdelayResponseEnabled() is None
