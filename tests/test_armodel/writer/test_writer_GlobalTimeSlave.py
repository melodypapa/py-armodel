"""Writer/reader round-trip tests for the GlobalTimeSlave reusable helper (Table 9.5, p.861)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import GlobalTimeSlave
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    GlobalTimeIcvVerificationEnum,
    PositiveInteger,
    RefType,
    String,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


class ConcreteGlobalTimeSlave(GlobalTimeSlave):
    pass


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


def _new_slave():
    slave = ConcreteGlobalTimeSlave(None, "slave1")
    slave.setUuid(String().setValue("0f1e2d3c-4b5a-6978-8796-a5b4c3d2e1f0"))
    ref = RefType()
    ref.setValue("/Clusters/Cluster1/Connector1")
    ref.setDest("CAN-COMMUNICATION-CONNECTOR")
    slave.setCommunicationConnectorRef(ref)
    slave.setFollowUpTimeoutValue(TimeValue().setValue("0.05"))
    slave.setIcvVerification(GlobalTimeIcvVerificationEnum().setValue(GlobalTimeIcvVerificationEnum.ICV_VERIFIED))
    slave.setTimeLeapFutureThreshold(TimeValue().setValue("0.5"))
    slave.setTimeLeapHealingCounter(PositiveInteger().setValue("4"))
    slave.setTimeLeapPastThreshold(TimeValue().setValue("0.25"))
    variation_point = VariationPoint()
    variation_point.setShortLabel(String().setValue("vpLabel"))
    slave.setVariationPoint(variation_point)
    return slave


class TestWriteGlobalTimeSlave:
    def test_write_all_elements_in_xsd_order(self, writer):
        """
        The helper writes the Identifiable level, the six group elements in the XSD
        sequenceOffset order and the VARIATION-POINT tail last.
        """
        element = ET.Element("GLOBAL-TIME-CAN-SLAVE")
        writer.writeGlobalTimeSlave(element, _new_slave())

        tags = [child.tag for child in element]
        assert tags[0] == "SHORT-NAME"
        assert tags[-1] == "VARIATION-POINT"
        assert tags[-7:] == [
            "COMMUNICATION-CONNECTOR-REF",
            "FOLLOW-UP-TIMEOUT-VALUE",
            "ICV-VERIFICATION",
            "TIME-LEAP-FUTURE-THRESHOLD",
            "TIME-LEAP-HEALING-COUNTER",
            "TIME-LEAP-PAST-THRESHOLD",
            "VARIATION-POINT",
        ]
        assert element.attrib["UUID"] == "0f1e2d3c-4b5a-6978-8796-a5b4c3d2e1f0"
        assert element.find("COMMUNICATION-CONNECTOR-REF").text == "/Clusters/Cluster1/Connector1"
        assert element.find("COMMUNICATION-CONNECTOR-REF").attrib["DEST"] == "CAN-COMMUNICATION-CONNECTOR"
        assert element.find("FOLLOW-UP-TIMEOUT-VALUE").text == "0.05"
        assert element.find("ICV-VERIFICATION").text == "ICV-VERIFIED"
        assert element.find("TIME-LEAP-FUTURE-THRESHOLD").text == "0.5"
        assert element.find("TIME-LEAP-HEALING-COUNTER").text == "4"
        assert element.find("TIME-LEAP-PAST-THRESHOLD").text == "0.25"
        assert element.find("VARIATION-POINT").find("SHORT-LABEL").text == "vpLabel"

    def test_write_empty_element(self, writer):
        """
        An unset slave emits no group content beyond the SHORT-NAME and no VARIATION-POINT.
        """
        element = ET.Element("USER-DEFINED-GLOBAL-TIME-SLAVE")
        writer.writeGlobalTimeSlave(element, ConcreteGlobalTimeSlave(None, "slave2"))

        assert [child.tag for child in element] == ["SHORT-NAME"]
        assert element.find("VARIATION-POINT") is None


class TestGlobalTimeSlaveRoundTrip:
    def test_round_trip_preserves_field_values(self, writer, parser):
        """
        Write -> serialize -> parse keeps every field value including the variation point.
        """
        element = ET.Element("GLOBAL-TIME-CAN-SLAVE")
        writer.writeGlobalTimeSlave(element, _new_slave())
        xml = ET.tostring(element, encoding="unicode")

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        slave = parser.readGlobalTimeSlave(parsed_element, ConcreteGlobalTimeSlave(None, "slave1"))

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
