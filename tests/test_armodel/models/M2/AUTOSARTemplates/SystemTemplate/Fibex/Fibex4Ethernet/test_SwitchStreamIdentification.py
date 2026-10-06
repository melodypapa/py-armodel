"""
Test suite for SwitchStreamIdentification (CP_TPS_SystemTemplate Table 3.84, p.135, R23-11).

Validates the member defaults, ref-list and factory semantics (duplicate short
name returns the existing element, None no-ops), getter/setter round-trips, the
verbatim class-level spec Note and the member declaration order (markdown
displayed row order) of the SwitchStreamIdentification model class.
"""

import ast
import importlib
import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
    SwitchStreamFilterActionDestPortModification,
    SwitchStreamFilterRule,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    SwitchStreamIdentification,
)

CLASS_NOTE = "SwitchStreamIdentification Tags: atp.Status=candidate"

EGRESS_PORT_NOTE = "Reference to the CouplingPort to be taken into account as the egress role for this SwitchStreamIdentification. Tags: atp.Status=candidate"
FILTER_ACTION_BLOCK_SOURCE_NOTE = "Enables Blocking all frames from the MAC address. Tags: atp.Status=candidate"
FILTER_ACTION_DEST_PORT_MODIFICATION_NOTE = (
    "Defines the action to modify the destination port(s) determined by the frame forwarding process for an particular Ethernet frame. Tags: atp.Status=candidate"
)
FILTER_ACTION_DROP_FRAME_NOTE = "Enables Drop Frame action. Tags: atp.Status=candidate"
FILTER_ACTION_VLAN_MODIFICATION_NOTE = "Defines the action to modify the VLAN-ID within a VLAN tag of an Ethernet frame. Tags: atp.Status=candidate"
INGRESS_PORT_NOTE = "Reference to the CouplingPort to be taken into account as the ingress role for this SwitchStreamIdentification. Tags: atp.Status=candidate"
STREAM_FILTER_RULE_NOTE = "Definition of a stream filter rule for this SwitchStream Identification. Tags: atp.Status=candidate"


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class TestSwitchStreamIdentification:
    def test_inheritance(self):
        assert issubclass(SwitchStreamIdentification, Identifiable)

    def test_concrete_class_instantiable(self):
        stream_identification = SwitchStreamIdentification(MockParent(), "Stream1")
        assert isinstance(stream_identification, Identifiable)
        assert stream_identification.getShortName() == "Stream1"
        assert stream_identification.getParent() is not None

    def test_class_docstring_note(self):
        assert inspect.cleandoc(SwitchStreamIdentification.__doc__) == CLASS_NOTE

    def test_initialization(self):
        stream_identification = SwitchStreamIdentification(MockParent(), "Stream1")

        assert stream_identification.getShortName() == "Stream1"
        assert stream_identification.getEgressPortRefs() == []
        assert stream_identification.getFilterActionBlockSource() is None
        assert stream_identification.getFilterActionDestPortModification() is None
        assert stream_identification.getFilterActionDropFrame() is None
        assert stream_identification.getFilterActionVlanModification() is None
        assert stream_identification.getIngressPortRefs() == []
        assert stream_identification.getStreamFilterRule() is None

    def test_member_annotations_and_declaration_order(self):
        module = importlib.import_module("armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology")
        module_source = open(module.__file__, encoding="utf-8").read()
        tree = ast.parse(module_source)
        cls = next(n for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and n.name == "SwitchStreamIdentification")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = [(st.target.attr, ast.get_source_segment(module_source, st.annotation)) for st in ast.walk(init) if isinstance(st, ast.AnnAssign)]

        assert annotations == [
            ("egressPortRefs", "List[RefType]"),
            ("filterActionBlockSource", "Optional[Boolean]"),
            ("filterActionDestPortModification", "Optional[SwitchStreamFilterActionDestPortModification]"),
            ("filterActionDropFrame", "Optional[Boolean]"),
            ("filterActionVlanModification", "Optional[PositiveInteger]"),
            ("ingressPortRefs", "List[RefType]"),
            ("streamFilterRule", "Optional[SwitchStreamFilterRule]"),
        ]

    def test_member_accessor_type_hints(self):
        assert typing.get_type_hints(SwitchStreamIdentification.addEgressPortRef).get("value") == typing.Optional[RefType]
        assert typing.get_type_hints(SwitchStreamIdentification.addEgressPortRef).get("return") is SwitchStreamIdentification
        assert typing.get_type_hints(SwitchStreamIdentification.getEgressPortRefs).get("return") == typing.List[RefType]
        assert typing.get_type_hints(SwitchStreamIdentification.getFilterActionBlockSource).get("return") == typing.Optional[Boolean]
        assert typing.get_type_hints(SwitchStreamIdentification.setFilterActionBlockSource).get("value") == typing.Optional[Boolean]
        assert typing.get_type_hints(SwitchStreamIdentification.createFilterActionDestPortModification).get("return") is SwitchStreamFilterActionDestPortModification
        assert typing.get_type_hints(SwitchStreamIdentification.getFilterActionDestPortModification).get("return") == typing.Optional[SwitchStreamFilterActionDestPortModification]
        assert typing.get_type_hints(SwitchStreamIdentification.getFilterActionDropFrame).get("return") == typing.Optional[Boolean]
        assert typing.get_type_hints(SwitchStreamIdentification.setFilterActionDropFrame).get("value") == typing.Optional[Boolean]
        assert typing.get_type_hints(SwitchStreamIdentification.getFilterActionVlanModification).get("return") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(SwitchStreamIdentification.setFilterActionVlanModification).get("value") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(SwitchStreamIdentification.addIngressPortRef).get("value") == typing.Optional[RefType]
        assert typing.get_type_hints(SwitchStreamIdentification.getIngressPortRefs).get("return") == typing.List[RefType]
        assert typing.get_type_hints(SwitchStreamIdentification.createStreamFilterRule).get("return") is SwitchStreamFilterRule
        assert typing.get_type_hints(SwitchStreamIdentification.getStreamFilterRule).get("return") == typing.Optional[SwitchStreamFilterRule]

    def test_member_docstrings_are_verbatim_spec_notes(self):
        assert inspect.cleandoc(SwitchStreamIdentification.addEgressPortRef.__doc__) == EGRESS_PORT_NOTE + "\n\nA None value is a no-op and does not append a egressPortRef."
        assert inspect.cleandoc(SwitchStreamIdentification.getEgressPortRefs.__doc__) == EGRESS_PORT_NOTE
        assert inspect.cleandoc(SwitchStreamIdentification.getFilterActionBlockSource.__doc__) == FILTER_ACTION_BLOCK_SOURCE_NOTE
        assert (
            inspect.cleandoc(SwitchStreamIdentification.setFilterActionBlockSource.__doc__)
            == FILTER_ACTION_BLOCK_SOURCE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing filterActionBlockSource."
        )
        assert (
            inspect.cleandoc(SwitchStreamIdentification.createFilterActionDestPortModification.__doc__)
            == FILTER_ACTION_DEST_PORT_MODIFICATION_NOTE + "\nThe existing element is returned when the short name already exists (no duplicate creation)."
        )
        assert inspect.cleandoc(SwitchStreamIdentification.getFilterActionDestPortModification.__doc__) == FILTER_ACTION_DEST_PORT_MODIFICATION_NOTE
        assert inspect.cleandoc(SwitchStreamIdentification.getFilterActionDropFrame.__doc__) == FILTER_ACTION_DROP_FRAME_NOTE
        assert (
            inspect.cleandoc(SwitchStreamIdentification.setFilterActionDropFrame.__doc__)
            == FILTER_ACTION_DROP_FRAME_NOTE + "\n\nA None value is a no-op and does not overwrite an existing filterActionDropFrame."
        )
        assert inspect.cleandoc(SwitchStreamIdentification.getFilterActionVlanModification.__doc__) == FILTER_ACTION_VLAN_MODIFICATION_NOTE
        assert (
            inspect.cleandoc(SwitchStreamIdentification.setFilterActionVlanModification.__doc__)
            == FILTER_ACTION_VLAN_MODIFICATION_NOTE + "\n\nA None value is a no-op and does not overwrite an existing filterActionVlanModification."
        )
        assert inspect.cleandoc(SwitchStreamIdentification.addIngressPortRef.__doc__) == INGRESS_PORT_NOTE + "\n\nA None value is a no-op and does not append a ingressPortRef."
        assert inspect.cleandoc(SwitchStreamIdentification.getIngressPortRefs.__doc__) == INGRESS_PORT_NOTE
        assert (
            inspect.cleandoc(SwitchStreamIdentification.createStreamFilterRule.__doc__)
            == STREAM_FILTER_RULE_NOTE + "\nThe existing element is returned when the short name already exists (no duplicate creation)."
        )
        assert inspect.cleandoc(SwitchStreamIdentification.getStreamFilterRule.__doc__) == STREAM_FILTER_RULE_NOTE

    def test_add_get_egress_port_refs(self):
        stream_identification = SwitchStreamIdentification(MockParent(), "Stream1")

        ref = RefType()
        ref.setValue("/AUTOSAR/Switch/Cport2")
        ref.setDest("COUPLING-PORT")
        assert stream_identification.addEgressPortRef(ref) is stream_identification
        assert stream_identification.getEgressPortRefs() == [ref]

        assert stream_identification.addEgressPortRef(None) is stream_identification
        assert stream_identification.getEgressPortRefs() == [ref]

        second = RefType()
        second.setValue("/AUTOSAR/Switch/Cport3")
        second.setDest("COUPLING-PORT")
        stream_identification.addEgressPortRef(second)
        assert stream_identification.getEgressPortRefs() == [ref, second]

    def test_get_set_filter_action_block_source(self):
        stream_identification = SwitchStreamIdentification(MockParent(), "Stream1")

        value = Boolean().setValue(True)
        assert stream_identification.setFilterActionBlockSource(value) is stream_identification
        assert stream_identification.getFilterActionBlockSource() is value
        assert stream_identification.getFilterActionBlockSource().getValue() is True

        assert stream_identification.setFilterActionBlockSource(None) is stream_identification
        assert stream_identification.getFilterActionBlockSource() is value

    def test_create_get_filter_action_dest_port_modification(self):
        stream_identification = SwitchStreamIdentification(MockParent(), "Stream1")

        modification = stream_identification.createFilterActionDestPortModification("DestMod")
        assert isinstance(modification, SwitchStreamFilterActionDestPortModification)
        assert modification.getShortName() == "DestMod"
        assert stream_identification.getFilterActionDestPortModification() is modification

        duplicate = stream_identification.createFilterActionDestPortModification("DestMod")
        assert duplicate is modification

    def test_get_set_filter_action_drop_frame(self):
        stream_identification = SwitchStreamIdentification(MockParent(), "Stream1")

        value = Boolean().setValue(False)
        assert stream_identification.setFilterActionDropFrame(value) is stream_identification
        assert stream_identification.getFilterActionDropFrame() is value
        assert stream_identification.getFilterActionDropFrame().getValue() is False

        assert stream_identification.setFilterActionDropFrame(None) is stream_identification
        assert stream_identification.getFilterActionDropFrame() is value

    def test_get_set_filter_action_vlan_modification(self):
        stream_identification = SwitchStreamIdentification(MockParent(), "Stream1")

        value = PositiveInteger().setValue("10")
        assert stream_identification.setFilterActionVlanModification(value) is stream_identification
        assert stream_identification.getFilterActionVlanModification() is value
        assert stream_identification.getFilterActionVlanModification().getValue() == 10

        assert stream_identification.setFilterActionVlanModification(None) is stream_identification
        assert stream_identification.getFilterActionVlanModification() is value

    def test_add_get_ingress_port_refs(self):
        stream_identification = SwitchStreamIdentification(MockParent(), "Stream1")

        ref = RefType()
        ref.setValue("/AUTOSAR/Switch/Cport1")
        ref.setDest("COUPLING-PORT")
        assert stream_identification.addIngressPortRef(ref) is stream_identification
        assert stream_identification.getIngressPortRefs() == [ref]

        assert stream_identification.addIngressPortRef(None) is stream_identification
        assert stream_identification.getIngressPortRefs() == [ref]

        second = RefType()
        second.setValue("/AUTOSAR/Switch/Cport4")
        second.setDest("COUPLING-PORT")
        stream_identification.addIngressPortRef(second)
        assert stream_identification.getIngressPortRefs() == [ref, second]

    def test_create_get_stream_filter_rule(self):
        stream_identification = SwitchStreamIdentification(MockParent(), "Stream1")

        rule = stream_identification.createStreamFilterRule("Rule1")
        assert isinstance(rule, SwitchStreamFilterRule)
        assert rule.getShortName() == "Rule1"
        assert stream_identification.getStreamFilterRule() is rule

        duplicate = stream_identification.createStreamFilterRule("Rule1")
        assert duplicate is rule
