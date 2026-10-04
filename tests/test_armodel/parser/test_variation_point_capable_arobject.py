"""
Tests for reading VARIATION-POINT on ARObject-most-derived VariationPointCapable classes.

The shared VP plumbing lives in readIdentifiable/writeIdentifiable, which
ARObject-level readers/writers never call. This pass adds the shared helpers
readVariationPointCapable/writeVariationPointCapable and wires them into every
ARObject-most-derived VariationPointCapable reader/writer, mirroring the
readIdentifiable VARIATION-POINT block (arxml_parser.py).

XSD ordering (R23-11 AUTOSAR_00052.xsd): VARIATION-POINT is mixin-owned with
sequenceOffset 10000 — emitted after all own group members.

Round-trip counterpart: tests/test_armodel/writer/test_variation_point_capable_arobject.py
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import ApplicationValueSpecification
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport import (
    McSwEmulationMethodSupport,
    RoleBasedMcDataAssignment,
)
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import EcucReferenceValue, EcucTextualParamValue
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition import InstantiationTimingEventProps
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDataMapping, NvBlockDescriptor
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup import ModeAccessPoint
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.EndToEndProtection import EndToEndProtectionISignalIPdu
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import CanTpEcu
from tests.test_armodel.parser._helpers import _autosar_root, _snip

VP_SNIPPET = "<VARIATION-POINT><SHORT-LABEL>vp1</SHORT-LABEL></VARIATION-POINT>"


def _assert_variation_point(obj):
    assert obj.getVariationPoint() is not None
    assert obj.getVariationPoint().getShortLabel().getValue() == "vp1"


class TestVariationPointCapableARObjectReaders:
    """Each ARObject-most-derived VariationPointCapable reader must read VARIATION-POINT."""

    def test_mode_switch_event_triggered_activity(self, parser):
        element = _snip("<ROLE>WriteBlock</ROLE>" + VP_SNIPPET, root_tag="MODE-SWITCH-EVENT-TRIGGERED-ACTIVITY")

        activity = parser.getModeSwitchEventTriggeredActivity(element)

        _assert_variation_point(activity)
        assert activity.getRole().getValue() == "WriteBlock"

    def test_nv_block_data_mapping(self, parser):
        element = _snip(VP_SNIPPET, root_tag="NV-BLOCK-DATA-MAPPING")

        mapping = NvBlockDataMapping()
        parser.readNvBlockDataMapping(element, mapping)

        _assert_variation_point(mapping)

    def test_role_based_data_assignment(self, parser):
        element = _snip(VP_SNIPPET, root_tag="ROLE-BASED-DATA-ASSIGNMENT")

        assignment = parser.getRoleBasedDataAssignment(element)

        _assert_variation_point(assignment)

    def test_role_based_bsw_module_entry_assignment(self, parser):
        element = _snip(VP_SNIPPET, root_tag="ROLE-BASED-BSW-MODULE-ENTRY-ASSIGNMENT")

        assignment = parser.getRoleBasedBswModuleEntryAssignment(element)

        _assert_variation_point(assignment)

    def test_bsw_mode_sender_policy(self, parser):
        element = _snip(VP_SNIPPET, root_tag="BSW-MODE-SENDER-POLICY")

        policy = parser.getBswModeSenderPolicy(element)

        _assert_variation_point(policy)

    def test_bsw_mode_receiver_policy(self, parser):
        element = _snip(VP_SNIPPET, root_tag="BSW-MODE-RECEIVER-POLICY")

        policy = parser.getBswModeReceiverPolicy(element)

        _assert_variation_point(policy)

    def test_bsw_exclusive_area_policy(self, parser):
        element = _snip(VP_SNIPPET, root_tag="BSW-EXCLUSIVE-AREA-POLICY")

        policy = parser.getBswExclusiveAreaPolicy(element)

        _assert_variation_point(policy)

    def test_bsw_trigger_direct_implementation(self, parser):
        element = _snip(VP_SNIPPET, root_tag="BSW-TRIGGER-DIRECT-IMPLEMENTATION")

        implementation = parser.getBswTriggerDirectImplementation(element)

        _assert_variation_point(implementation)

    def test_mc_sw_emulation_method_support(self, parser):
        element = _snip(VP_SNIPPET, root_tag="MC-SW-EMULATION-METHOD-SUPPORT")

        support = McSwEmulationMethodSupport()
        parser.readMcSwEmulationMethodSupport(element, support)

        _assert_variation_point(support)

    def test_role_based_mc_data_assignment(self, parser):
        element = _snip(VP_SNIPPET, root_tag="ROLE-BASED-MC-DATA-ASSIGNMENT")

        assignment = RoleBasedMcDataAssignment()
        parser.readRoleBasedMcDataAssignment(element, assignment)

        _assert_variation_point(assignment)

    def test_mode_access_point(self, parser):
        element = _snip(VP_SNIPPET, root_tag="MODE-ACCESS-POINT")

        point = ModeAccessPoint()
        parser.readModeAccessPoint(element, point)

        _assert_variation_point(point)

    def test_instantiation_rte_event_props(self, parser):
        """Table 3.17 has no variationPoint row (Rule 0015), so an incoming VARIATION-POINT element is ignored, not read."""
        element = _snip(VP_SNIPPET, root_tag="INSTANTIATION-TIMING-EVENT-PROPS")

        props = InstantiationTimingEventProps()
        parser.readInstantiationRTEEventProps(element, props)

        assert props.getShortLabel() is None
        assert props.getRefinedEventIRef() is None

    def test_instantiation_data_def_props(self, parser):
        from armodel.models import ApplicationSwComponentType

        inner = "<INSTANTIATION-DATA-DEF-PROPSS><INSTANTIATION-DATA-DEF-PROPS>" + VP_SNIPPET + "</INSTANTIATION-DATA-DEF-PROPS></INSTANTIATION-DATA-DEF-PROPSS>"
        element = _snip(inner, root_tag="SWC-INTERNAL-BEHAVIOR")
        app = ApplicationSwComponentType(parent=_autosar_root(), short_name="a")
        behavior = app.createSwcInternalBehavior("ib")

        parser.readSwcInternalBehaviorInstantiationDataDefProps(element, behavior)

        _assert_variation_point(behavior.getInstantiationDataDefPropss()[0])

    def test_instantiation_data_def_props_in_nv_block_descriptor(self, parser):
        inner = "<INSTANTIATION-DATA-DEF-PROPSS><INSTANTIATION-DATA-DEF-PROPS>" + VP_SNIPPET + "</INSTANTIATION-DATA-DEF-PROPS></INSTANTIATION-DATA-DEF-PROPSS>"
        element = _snip(inner, root_tag="NV-BLOCK-DESCRIPTOR")
        descriptor = NvBlockDescriptor(parent=_autosar_root(), short_name="d")

        parser.readNvBlockDescriptor(element, descriptor)

        _assert_variation_point(descriptor.getInstantiationDataDefPropss()[0])

    def test_value_specification_family(self, parser):
        element = _snip(VP_SNIPPET, root_tag="APPLICATION-VALUE-SPECIFICATION")

        value_spec = parser.getApplicationValueSpecification(element)

        assert isinstance(value_spec, ApplicationValueSpecification)
        _assert_variation_point(value_spec)

    def test_numerical_or_text(self, parser):
        element = _snip(VP_SNIPPET, root_tag="NUMERICAL-OR-TEXT")

        not_text = parser.getNumericalOrText(element)

        _assert_variation_point(not_text)

    def test_rule_arguments(self, parser):
        element = _snip(VP_SNIPPET, root_tag="RULE-ARGUMENTS")

        arguments = parser.getRuleArguments(element)

        _assert_variation_point(arguments)

    def test_end_to_end_protection_isignal_ipdu(self, parser):
        element = _snip(
            "<DATA-OFFSET>4</DATA-OFFSET>" + VP_SNIPPET,
            root_tag="END-TO-END-PROTECTION-I-SIGNAL-I-PDU",
        )

        ipdu = EndToEndProtectionISignalIPdu()
        parser.readEndToEndProtectionISignalIPdu(element, ipdu)

        _assert_variation_point(ipdu)
        assert ipdu.getDataOffset().getValue() == 4

    def test_can_tp_ecu(self, parser):
        element = _snip("<CYCLE-TIME-MAIN-FUNCTION>0.01</CYCLE-TIME-MAIN-FUNCTION>" + VP_SNIPPET, root_tag="CAN-TP-ECU")

        tp_ecu = CanTpEcu()
        parser.readCanTpEcu(element, tp_ecu)

        _assert_variation_point(tp_ecu)

    def test_ecuc_textual_param_value(self, parser):
        """Table 2.49 has no variationPoint row (Rule 0015), so an incoming VARIATION-POINT element is ignored, not read."""
        element = _snip("<DEFINITION-REF DEST='ECUC-STRING-PARAM-DEF'>/Def</DEFINITION-REF>" + VP_SNIPPET, root_tag="ECUC-TEXTUAL-PARAM-VALUE")

        param_value = EcucTextualParamValue()
        parser.readEcucTextualParamValue(element, param_value)

        assert param_value.getDefinitionRef() is not None
        assert param_value.getDefinitionRef().getValue() == "/Def"

    def test_ecuc_reference_value(self, parser):
        """Table 2.53 has no variationPoint row (Rule 0015), so an incoming VARIATION-POINT element is ignored, not read."""
        element = _snip("<DEFINITION-REF DEST='ECUC-REFERENCE-DEF'>/Def</DEFINITION-REF>" + VP_SNIPPET, root_tag="ECUC-REFERENCE-VALUE")

        value = EcucReferenceValue()
        parser.readEcucReferenceValue(element, value)

        assert value.getDefinitionRef() is not None
        assert value.getDefinitionRef().getValue() == "/Def"

    def test_absent_variation_point_leaves_field_unset(self, parser):
        element = _snip("<ROLE>WriteBlock</ROLE>", root_tag="MODE-SWITCH-EVENT-TRIGGERED-ACTIVITY")

        activity = parser.getModeSwitchEventTriggeredActivity(element)

        assert activity.getVariationPoint() is None
