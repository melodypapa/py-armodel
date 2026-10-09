"""Writer round-trip tests for PduTriggering (Table 6.31, p.349).

Serialized through the PDU-TRIGGERING element (AUTOSAR_00052.xsd l.88860) and the
PhysicalChannel PDU-TRIGGERINGS dispatch: I-PDU-PORT-REFS wrapper, I-PDU-REF,
I-SIGNAL-TRIGGERINGS wrapper (I-SIGNAL-TRIGGERING-REF-CONDITIONAL items),
SEC-OC-CRYPTO-MAPPING-REF, TRIGGER-I-PDU-SEND-CONDITIONS wrapper, VARIATION-POINT
last (sequenceOffset 10000).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, RefType, String
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanPhysicalChannel
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import PduTriggering, TriggerIPduSendCondition
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _with_ns(parent: ET.Element) -> ET.Element:
    return ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))


def _ref(value: str, dest: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _new_triggering() -> PduTriggering:
    triggering = PduTriggering(None, "PT1")
    triggering.setUuid(String().setValue("11111111-2222-3333-4444-555555555555"))
    triggering.addIPduPortRef(_ref("/Cluster/Ecu1/Port1", "I-PDU-PORT"))
    triggering.addIPduPortRef(_ref("/Cluster/Ecu2/Port2", "I-PDU-PORT"))
    triggering.setIPduRef(_ref("/Cluster/Pdus/Ipdu1", "PDU"))
    triggering.addISignalTriggeringRef(_ref("/Cluster/ST1", "I-SIGNAL-TRIGGERING"))
    triggering.addISignalTriggeringRef(_ref("/Cluster/ST2", "I-SIGNAL-TRIGGERING"))
    triggering.setSecOcCryptoMappingRef(_ref("/SecOc/CryptoMapping1", "SEC-OC-CRYPTO-SERVICE-MAPPING"))
    condition = TriggerIPduSendCondition()
    condition.addModeDeclarationRef(_ref("/Md/ModeDcl1", "MODE-DECLARATION"))
    triggering.addTriggerIPduSendCondition(condition)
    variation_point = VariationPoint()
    variation_point.setShortLabel(Identifier().setValue("vpPt"))
    triggering.setVariationPoint(variation_point)
    return triggering


class TestWritePduTriggering:
    def test_empty(self):
        triggering = PduTriggering(None, "PT1")
        parent = ET.Element("PARENT")
        ARXMLWriter().writePduTriggering(parent, triggering)

        node = parent.find("PDU-TRIGGERING")
        assert node is not None
        assert node.find("I-PDU-PORT-REFS") is None
        assert node.find("I-PDU-REF") is None
        assert node.find("I-SIGNAL-TRIGGERINGS") is None
        assert node.find("SEC-OC-CRYPTO-MAPPING-REF") is None
        assert node.find("TRIGGER-I-PDU-SEND-CONDITIONS") is None
        assert node.find("VARIATION-POINT") is None

    def test_full_element_order(self):
        triggering = _new_triggering()
        parent = ET.Element("PARENT")
        ARXMLWriter().writePduTriggering(parent, triggering)

        node = parent.find("PDU-TRIGGERING")
        tags = [child.tag for child in node]
        assert tags.index("I-PDU-PORT-REFS") < tags.index("I-PDU-REF")
        assert tags.index("I-PDU-REF") < tags.index("I-SIGNAL-TRIGGERINGS")
        assert tags.index("I-SIGNAL-TRIGGERINGS") < tags.index("SEC-OC-CRYPTO-MAPPING-REF")
        assert tags.index("SEC-OC-CRYPTO-MAPPING-REF") < tags.index("TRIGGER-I-PDU-SEND-CONDITIONS")
        assert tags.index("TRIGGER-I-PDU-SEND-CONDITIONS") < tags.index("VARIATION-POINT")

        assert node.find("I-PDU-PORT-REFS/I-PDU-PORT-REF").text == "/Cluster/Ecu1/Port1"
        assert node.find("I-PDU-PORT-REFS/I-PDU-PORT-REF").get("DEST") == "I-PDU-PORT"
        assert node.find("I-PDU-REF").text == "/Cluster/Pdus/Ipdu1"
        conditionals = node.findall("I-SIGNAL-TRIGGERINGS/I-SIGNAL-TRIGGERING-REF-CONDITIONAL")
        assert [c.find("I-SIGNAL-TRIGGERING-REF").text for c in conditionals] == ["/Cluster/ST1", "/Cluster/ST2"]
        assert node.find("SEC-OC-CRYPTO-MAPPING-REF").text == "/SecOc/CryptoMapping1"
        assert node.find("TRIGGER-I-PDU-SEND-CONDITIONS/TRIGGER-I-PDU-SEND-CONDITION/MODE-DECLARATION-REFS/MODE-DECLARATION-REF").text == "/Md/ModeDcl1"
        assert node.find("VARIATION-POINT/SHORT-LABEL").text == "vpPt"

    def test_round_trip_full(self):
        triggering = _new_triggering()
        parent = ET.Element("PARENT")
        ARXMLWriter().writePduTriggering(parent, triggering)

        reloaded = PduTriggering(None, "PT1")
        ARXMLParser().readPduTriggering(_with_ns(parent)[0], reloaded)

        assert reloaded.getUuid() is not None
        assert reloaded.getUuid().getValue() == "11111111-2222-3333-4444-555555555555"
        assert [ref.getValue() for ref in reloaded.getIPduPortRefs()] == ["/Cluster/Ecu1/Port1", "/Cluster/Ecu2/Port2"]
        assert reloaded.getIPduRef().getValue() == "/Cluster/Pdus/Ipdu1"
        assert [ref.getValue() for ref in reloaded.getISignalTriggeringRefs()] == ["/Cluster/ST1", "/Cluster/ST2"]
        assert reloaded.getSecOcCryptoMappingRef().getValue() == "/SecOc/CryptoMapping1"
        conditions = reloaded.getTriggerIPduSendConditions()
        assert len(conditions) == 1
        assert [ref.getValue() for ref in conditions[0].getModeDeclarationRefs()] == ["/Md/ModeDcl1"]
        assert reloaded.getVariationPoint() is not None
        assert reloaded.getVariationPoint().getShortLabel().getValue() == "vpPt"

    def test_round_trip_via_physical_channel_dispatch(self):
        channel = CanPhysicalChannel(None, "CanCh")
        triggering = channel.createPduTriggering("PT1")
        triggering.setIPduRef(_ref("/Cluster/Pdus/Ipdu1", "PDU"))
        triggering.addISignalTriggeringRef(_ref("/Cluster/ST1", "I-SIGNAL-TRIGGERING"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writePhysicalChannelPduTriggerings(parent, channel)

        node = parent.find("PDU-TRIGGERINGS/PDU-TRIGGERING")
        assert node is not None
        assert node.find("SHORT-NAME").text == "PT1"

        reloaded_channel = CanPhysicalChannel(None, "CanCh")
        ARXMLParser().readPhysicalChannelPduTriggerings(_with_ns(parent), reloaded_channel)
        triggerings = reloaded_channel.getPduTriggerings()
        assert len(triggerings) == 1
        assert triggerings[0].getShortName() == "PT1"
        assert triggerings[0].getIPduRef().getValue() == "/Cluster/Pdus/Ipdu1"
        assert [ref.getValue() for ref in triggerings[0].getISignalTriggeringRefs()] == ["/Cluster/ST1"]
