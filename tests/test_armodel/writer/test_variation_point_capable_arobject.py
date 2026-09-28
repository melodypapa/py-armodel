"""
Tests for writing VARIATION-POINT on ARObject-most-derived VariationPointCapable classes.

The shared VP plumbing lives in writeIdentifiable, which ARObject-level writers
never call. This pass adds the shared helper writeVariationPointCapable and wires
it into every ARObject-most-derived VariationPointCapable writer. VARIATION-POINT
is mixin-owned with XSD sequenceOffset 10000 — emitted after all own group
members (R23-11 AUTOSAR_00052.xsd); inside the ValueSpecification/EcucValue
dispatch layers it lands before the concrete subclass own fields.

Round-trip counterpart: tests/test_armodel/parser/test_variation_point_capable_arobject.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswModeSenderPolicy
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import TextValueSpecification
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import RoleBasedDataAssignment
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import EcucTextualParamValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DateTime,
    Identifier,
    Integer,
    RefType,
    String,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import (
    ModeSwitchEventTriggeredActivity,
    NvBlockDataMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.EndToEndProtection import EndToEndProtectionISignalIPdu
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import CanTpEcu
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    """Create ARXML writer instance."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLWriter()


def _variation_point():
    variation_point = VariationPoint()
    label = Identifier()
    label.setValue("vp1")
    variation_point.setShortLabel(label)
    return variation_point


class TestWriteVariationPointCapableARObjectWriters:
    """Each ARObject-most-derived VariationPointCapable writer must emit VARIATION-POINT last."""

    def test_write_mode_switch_event_triggered_activity_vp_last(self, writer):
        activity = ModeSwitchEventTriggeredActivity()
        role = Identifier()
        role.setValue("WriteBlock")
        activity.setRole(role)
        activity.setVariationPoint(_variation_point())

        parent = ET.Element("PARENT")
        writer.writeModeSwitchEventTriggeredActivity(parent, activity)

        element = parent.find("MODE-SWITCH-EVENT-TRIGGERED-ACTIVITY")
        assert [elem.tag for elem in element] == ["ROLE", "VARIATION-POINT"]
        assert element.find("VARIATION-POINT").find("SHORT-LABEL").text == "vp1"

    def test_write_nv_block_data_mapping_vp_last(self, writer):
        mapping = NvBlockDataMapping()
        mapping.setVariationPoint(_variation_point())

        parent = ET.Element("PARENT")
        writer.writeNvBlockDataMapping(parent, mapping)

        element = parent.find("NV-BLOCK-DATA-MAPPING")
        assert element[-1].tag == "VARIATION-POINT"

    def test_write_can_tp_ecu_vp_last(self, writer):
        tp_ecu = CanTpEcu()
        tp_ecu.setVariationPoint(_variation_point())

        parent = ET.Element("PARENT")
        writer.writeCanTpEcu(parent, tp_ecu)

        element = parent.find("CAN-TP-ECU")
        assert [elem.tag for elem in element] == ["VARIATION-POINT"]

    def test_write_can_tp_ecu_ar_object_attributes(self, writer):
        tp_ecu = CanTpEcu()
        checksum = String()
        checksum.setValue("abc123")
        tp_ecu.setChecksum(checksum)
        timestamp = DateTime()
        timestamp.setValue("2024-01-01T12:00:00+00:00")
        tp_ecu.setTimestamp(timestamp)

        parent = ET.Element("PARENT")
        writer.writeCanTpEcu(parent, tp_ecu)

        element = parent.find("CAN-TP-ECU")
        assert element.attrib.get("S") == "abc123"
        assert element.attrib.get("T") is not None

    def test_write_end_to_end_protection_isignal_ipdu_vp_last(self, writer):
        ipdu = EndToEndProtectionISignalIPdu()
        ipdu.setVariationPoint(_variation_point())

        parent = ET.Element("PARENT")
        writer.writeEndToEndProtectionISignalIPdu(parent, ipdu)

        element = parent.find("END-TO-END-PROTECTION-I-SIGNAL-I-PDU")
        assert element[-1].tag == "VARIATION-POINT"

    def test_write_end_to_end_protection_isignal_ipdu_ar_object_attributes(self, writer):
        ipdu = EndToEndProtectionISignalIPdu()
        checksum = String()
        checksum.setValue("abc123")
        ipdu.setChecksum(checksum)

        parent = ET.Element("PARENT")
        writer.writeEndToEndProtectionISignalIPdu(parent, ipdu)

        element = parent.find("END-TO-END-PROTECTION-I-SIGNAL-I-PDU")
        assert element.attrib.get("S") == "abc123"

    def test_write_text_value_specification_vp_in_value_specification_group(self, writer):
        value_spec = TextValueSpecification()
        value_spec.setVariationPoint(_variation_point())

        parent = ET.Element("PARENT")
        writer.writeTextValueSpecification(parent, value_spec)

        element = parent.find("TEXT-VALUE-SPECIFICATION")
        assert [elem.tag for elem in element] == ["VARIATION-POINT"]

    def test_write_ecuc_textual_param_value_vp_after_dispatcher_content(self, writer):
        param_value = EcucTextualParamValue()
        definition_ref = RefType()
        definition_ref.setValue("/Def")
        definition_ref.setDest("ECUC-STRING-PARAM-DEF")
        param_value.setDefinitionRef(definition_ref)
        param_value.setVariationPoint(_variation_point())

        parent = ET.Element("PARENT")
        writer.writeEcucTextualParamValue(parent, param_value)

        element = parent.find("ECUC-TEXTUAL-PARAM-VALUE")
        assert [elem.tag for elem in element] == ["DEFINITION-REF", "VARIATION-POINT"]

    def test_write_role_based_data_assignment_vp_last(self, writer):
        assignment = RoleBasedDataAssignment()
        assignment.setVariationPoint(_variation_point())

        parent = ET.Element("PARENT")
        writer.writeRoleBasedDataAssignment(parent, assignment)

        element = parent.find("ROLE-BASED-DATA-ASSIGNMENT")
        assert element[-1].tag == "VARIATION-POINT"

    def test_write_bsw_mode_sender_policy_vp_last(self, writer):
        policy = BswModeSenderPolicy()
        policy.setVariationPoint(_variation_point())

        parent = ET.Element("PARENT")
        writer.setBswModeSenderPolicy(parent, policy)

        element = parent.find("BSW-MODE-SENDER-POLICY")
        assert element[-1].tag == "VARIATION-POINT"

    def test_absent_variation_point_emits_no_element(self, writer):
        parent = ET.Element("PARENT")
        writer.writeModeSwitchEventTriggeredActivity(parent, ModeSwitchEventTriggeredActivity())

        element = parent.find("MODE-SWITCH-EVENT-TRIGGERED-ACTIVITY")
        assert element.find("VARIATION-POINT") is None


class TestVariationPointCapableARObjectRoundTrip:
    """Write → re-parse round-trips keep the VARIATION-POINT content."""

    def test_round_trip_mode_switch_event_triggered_activity(self, writer):
        activity = ModeSwitchEventTriggeredActivity()
        activity.setVariationPoint(_variation_point())

        parent = ET.Element("PARENT")
        writer.writeModeSwitchEventTriggeredActivity(parent, activity)
        element = parent.find("MODE-SWITCH-EVENT-TRIGGERED-ACTIVITY")
        xml_text = ET.tostring(element, encoding="unicode")
        reloaded_element = ET.fromstring(xml_text.replace("MODE-SWITCH-EVENT-TRIGGERED-ACTIVITY", "MODE-SWITCH-EVENT-TRIGGERED-ACTIVITY xmlns='http://autosar.org/schema/r4.0'", 1))

        reloaded = ARXMLParser().getModeSwitchEventTriggeredActivity(reloaded_element)

        assert reloaded.getVariationPoint() is not None
        assert reloaded.getVariationPoint().getShortLabel().getValue() == "vp1"

    def test_round_trip_nv_block_data_mapping(self, writer):
        mapping = NvBlockDataMapping()
        mapping.setVariationPoint(_variation_point())

        parent = ET.Element("PARENT")
        writer.writeNvBlockDataMapping(parent, mapping)
        element = parent.find("NV-BLOCK-DATA-MAPPING")
        xml_text = ET.tostring(element, encoding="unicode")
        reloaded_element = ET.fromstring(xml_text.replace("NV-BLOCK-DATA-MAPPING", "NV-BLOCK-DATA-MAPPING xmlns='http://autosar.org/schema/r4.0'", 1))

        reloaded = NvBlockDataMapping()
        ARXMLParser().readNvBlockDataMapping(reloaded_element, reloaded)

        assert reloaded.getVariationPoint() is not None
        assert reloaded.getVariationPoint().getShortLabel().getValue() == "vp1"

    def test_round_trip_can_tp_ecu(self, writer):
        tp_ecu = CanTpEcu()
        tp_ecu.setVariationPoint(_variation_point())

        parent = ET.Element("PARENT")
        writer.writeCanTpEcu(parent, tp_ecu)
        element = parent.find("CAN-TP-ECU")
        xml_text = ET.tostring(element, encoding="unicode")
        reloaded_element = ET.fromstring(xml_text.replace("CAN-TP-ECU", "CAN-TP-ECU xmlns='http://autosar.org/schema/r4.0'", 1))

        reloaded = CanTpEcu()
        ARXMLParser().readCanTpEcu(reloaded_element, reloaded)

        assert reloaded.getVariationPoint() is not None
        assert reloaded.getVariationPoint().getShortLabel().getValue() == "vp1"

    def test_round_trip_end_to_end_protection_isignal_ipdu(self, writer):
        ipdu = EndToEndProtectionISignalIPdu()
        offset = Integer()
        offset.setValue(4)
        ipdu.setDataOffset(offset)
        ipdu.setVariationPoint(_variation_point())

        parent = ET.Element("PARENT")
        writer.writeEndToEndProtectionISignalIPdu(parent, ipdu)
        element = parent.find("END-TO-END-PROTECTION-I-SIGNAL-I-PDU")
        xml_text = ET.tostring(element, encoding="unicode")
        reloaded_element = ET.fromstring(xml_text.replace("END-TO-END-PROTECTION-I-SIGNAL-I-PDU", "END-TO-END-PROTECTION-I-SIGNAL-I-PDU xmlns='http://autosar.org/schema/r4.0'", 1))

        reloaded = EndToEndProtectionISignalIPdu()
        ARXMLParser().readEndToEndProtectionISignalIPdu(reloaded_element, reloaded)

        assert reloaded.getDataOffset().getValue() == 4
        assert reloaded.getVariationPoint() is not None
        assert reloaded.getVariationPoint().getShortLabel().getValue() == "vp1"
