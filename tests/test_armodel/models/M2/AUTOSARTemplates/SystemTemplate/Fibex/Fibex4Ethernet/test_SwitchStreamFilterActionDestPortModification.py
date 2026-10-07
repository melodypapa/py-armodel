"""
Test suite for SwitchStreamFilterActionDestPortModification (CP_TPS_SystemTemplate Table 3.93, p.140, R23-11).

Validates the member defaults, getter/setter round-trips (None no-ops), the enum
setValue round-trip, the verbatim class-level spec Note and the member declaration
order (markdown displayed row order) of the SwitchStreamFilterActionDestPortModification
model class.
"""

import ast
import importlib
import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    SwitchStreamFilterActionDestPortModification,
    SwitchStreamFilterActionPortModificationEnum,
)

CLASS_NOTE = "Defines the action to modify the destination port(s) determined by the frame forwarding process for an particular Ethernet frame. Either the egress destination of an Ethernet frame is extended or overwritten. Tags: atp.Status=candidate"

EGRESS_PORT_NOTE = "Reference to the egress ports used as the target of the filter action to modify the egress port. Tags: atp.Status=candidate"
MODIFICATION_NOTE = "Defines the method to modify the egress destination. Either overwrite or extend the egress destination. Tags: atp.Status=candidate"


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _ref(value: str) -> RefType:
    ref = RefType()
    ref.setDest("COUPLING-PORT")
    ref.setValue(value)
    return ref


class TestSwitchStreamFilterActionDestPortModification:
    def test_inheritance(self):
        assert issubclass(SwitchStreamFilterActionDestPortModification, Identifiable)

    def test_concrete_class_instantiable(self):
        modification = SwitchStreamFilterActionDestPortModification(MockParent(), "DestMod")
        assert isinstance(modification, Identifiable)
        assert modification.getShortName() == "DestMod"
        assert modification.getParent() is not None

    def test_class_docstring_note(self):
        assert inspect.cleandoc(SwitchStreamFilterActionDestPortModification.__doc__) == CLASS_NOTE

    def test_initialization(self):
        modification = SwitchStreamFilterActionDestPortModification(MockParent(), "DestMod")

        assert modification.getEgressPortRefs() == []
        assert modification.getModification() is None

    def test_member_annotations_and_declaration_order(self):
        module = importlib.import_module("armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology")
        module_source = open(module.__file__, encoding="utf-8").read()
        tree = ast.parse(module_source)
        cls = next(n for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and n.name == "SwitchStreamFilterActionDestPortModification")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = [(st.target.attr, ast.get_source_segment(module_source, st.annotation)) for st in ast.walk(init) if isinstance(st, ast.AnnAssign)]

        assert annotations == [
            ("egressPortRefs", "List[RefType]"),
            ("modification", "Optional[SwitchStreamFilterActionPortModificationEnum]"),
        ]

    def test_member_accessor_type_hints(self):
        assert typing.get_type_hints(SwitchStreamFilterActionDestPortModification.addEgressPortRef).get("value") == typing.Optional[RefType]
        assert typing.get_type_hints(SwitchStreamFilterActionDestPortModification.addEgressPortRef).get("return") is SwitchStreamFilterActionDestPortModification
        assert typing.get_type_hints(SwitchStreamFilterActionDestPortModification.getEgressPortRefs).get("return") == typing.List[RefType]
        assert typing.get_type_hints(SwitchStreamFilterActionDestPortModification.getModification).get("return") == typing.Optional[SwitchStreamFilterActionPortModificationEnum]
        assert typing.get_type_hints(SwitchStreamFilterActionDestPortModification.setModification).get("value") == typing.Optional[SwitchStreamFilterActionPortModificationEnum]
        assert typing.get_type_hints(SwitchStreamFilterActionDestPortModification.setModification).get("return") is SwitchStreamFilterActionDestPortModification

    def test_member_docstrings_are_verbatim_spec_notes(self):
        assert inspect.cleandoc(SwitchStreamFilterActionDestPortModification.addEgressPortRef.__doc__) == EGRESS_PORT_NOTE + "\n\nA None value is a no-op and does not append a egressPortRef."
        assert inspect.cleandoc(SwitchStreamFilterActionDestPortModification.getEgressPortRefs.__doc__) == EGRESS_PORT_NOTE
        assert inspect.cleandoc(SwitchStreamFilterActionDestPortModification.getModification.__doc__) == MODIFICATION_NOTE
        assert (
            inspect.cleandoc(SwitchStreamFilterActionDestPortModification.setModification.__doc__) == MODIFICATION_NOTE + "\n\nA None value is a no-op and does not overwrite an existing modification."
        )

    def test_add_get_egress_port_refs(self):
        modification = SwitchStreamFilterActionDestPortModification(MockParent(), "DestMod")

        ref1 = _ref("/AUTOSAR/Switch/Cport1")
        assert modification.addEgressPortRef(ref1) is modification
        ref2 = _ref("/AUTOSAR/Switch/Cport2")
        modification.addEgressPortRef(ref2)

        egress_port_refs = modification.getEgressPortRefs()
        assert len(egress_port_refs) == 2
        assert egress_port_refs[0] is ref1
        assert egress_port_refs[1] is ref2

        modification.addEgressPortRef(None)
        assert len(modification.getEgressPortRefs()) == 2

    def test_get_set_modification(self):
        modification = SwitchStreamFilterActionDestPortModification(MockParent(), "DestMod")

        value = SwitchStreamFilterActionPortModificationEnum().setValue(SwitchStreamFilterActionPortModificationEnum.OVERWRITE)
        assert modification.setModification(value) is modification
        assert modification.getModification() is value
        assert modification.getModification().getValue() == SwitchStreamFilterActionPortModificationEnum.OVERWRITE

        assert modification.setModification(None) is modification
        assert modification.getModification() is value

    def test_modification_enum_value_round_trip(self):
        modification = SwitchStreamFilterActionDestPortModification(MockParent(), "DestMod")

        extend = SwitchStreamFilterActionPortModificationEnum().setValue(SwitchStreamFilterActionPortModificationEnum.EXTEND)
        modification.setModification(extend)
        assert modification.getModification().getValue() == "EXTEND"

        overwrite = SwitchStreamFilterActionPortModificationEnum().setValue(SwitchStreamFilterActionPortModificationEnum.OVERWRITE)
        modification.setModification(overwrite)
        assert modification.getModification().getValue() == "OVERWRITE"
