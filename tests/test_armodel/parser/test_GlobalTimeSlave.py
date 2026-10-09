"""Reader tests for the GlobalTimeSlave reusable helper (Table 9.5, p.861)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import GlobalTimeSlave
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class ConcreteGlobalTimeSlave(GlobalTimeSlave):
    pass


@pytest.fixture(autouse=True)
def reset_autosar():
    from armodel.models import AUTOSAR

    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    return ARXMLParser()


class TestReadGlobalTimeSlave:
    def test_read_all_elements(self, parser):
        """
        All six GLOBAL-TIME-SLAVE group elements plus the Identifiable level (SHORT-NAME, UUID)
        and the trailing VARIATION-POINT are read into the object.
        """
        element = ET.fromstring(
            "<GLOBAL-TIME-CAN-SLAVE xmlns='%s' UUID='0f1e2d3c-4b5a-6978-8796-a5b4c3d2e1f0'>"
            "<SHORT-NAME>slave1</SHORT-NAME>"
            "<COMMUNICATION-CONNECTOR-REF DEST='CAN-COMMUNICATION-CONNECTOR'>/Clusters/Cluster1/Connector1</COMMUNICATION-CONNECTOR-REF>"
            "<FOLLOW-UP-TIMEOUT-VALUE>0.05</FOLLOW-UP-TIMEOUT-VALUE>"
            "<ICV-VERIFICATION>ICV-VERIFIED</ICV-VERIFICATION>"
            "<TIME-LEAP-FUTURE-THRESHOLD>0.5</TIME-LEAP-FUTURE-THRESHOLD>"
            "<TIME-LEAP-HEALING-COUNTER>4</TIME-LEAP-HEALING-COUNTER>"
            "<TIME-LEAP-PAST-THRESHOLD>0.25</TIME-LEAP-PAST-THRESHOLD>"
            "<VARIATION-POINT><SHORT-LABEL>vpLabel</SHORT-LABEL></VARIATION-POINT>"
            "</GLOBAL-TIME-CAN-SLAVE>" % NS
        )

        slave = parser.readGlobalTimeSlave(element, ConcreteGlobalTimeSlave(None, "slave1"))

        assert slave.getShortName() == "slave1"
        assert slave.getUuid().getValue() == "0f1e2d3c-4b5a-6978-8796-a5b4c3d2e1f0"
        assert slave.getCommunicationConnectorRef().getValue() == "/Clusters/Cluster1/Connector1"
        assert slave.getCommunicationConnectorRef().getDest() == "CAN-COMMUNICATION-CONNECTOR"
        assert slave.getFollowUpTimeoutValue().getValue() == pytest.approx(0.05)
        assert slave.getIcvVerification().getValue() == "ICV-VERIFIED"
        assert slave.getTimeLeapFutureThreshold().getValue() == pytest.approx(0.5)
        assert slave.getTimeLeapHealingCounter().getValue() == 4
        assert slave.getTimeLeapPastThreshold().getValue() == pytest.approx(0.25)
        assert slave.getVariationPoint().getShortLabel().getValue() == "vpLabel"

    def test_read_empty_element(self, parser):
        """
        A concrete subclass element without group content leaves the fields unset.
        """
        element = ET.fromstring("<USER-DEFINED-GLOBAL-TIME-SLAVE xmlns='%s'></USER-DEFINED-GLOBAL-TIME-SLAVE>" % NS)

        slave = parser.readGlobalTimeSlave(element, ConcreteGlobalTimeSlave(None, "slave2"))

        assert slave.getCommunicationConnectorRef() is None
        assert slave.getFollowUpTimeoutValue() is None
        assert slave.getIcvVerification() is None
        assert slave.getTimeLeapFutureThreshold() is None
        assert slave.getTimeLeapHealingCounter() is None
        assert slave.getTimeLeapPastThreshold() is None
        assert slave.getVariationPoint() is None
