import inspect
import sys
import typing

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import CanFrameTriggering
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import FrameTriggering


def _get_type_hints(obj):
    """typing.get_type_hints leaves PEP 563 self-references as ForwardRef on Python 3.8; resolve against the defining module."""
    hints = typing.get_type_hints(obj)
    module_vars = vars(sys.modules[obj.__module__])
    for name, hint in hints.items():
        if isinstance(hint, typing.ForwardRef):
            hints[name] = module_vars.get(hint.__forward_arg__, hint)
    return hints


CLASS_NOTE = (
    "The FrameTriggering describes the instance of a frame sent on a channel and defines the manner of "
    "triggering (timing information) and identification of a frame on the channel, on which it is sent. "
    "For the same frame, if FrameTriggerings exist on more than one channel of the same cluster the "
    "fan-out/in is handled by the Bus interface.\n"
    "\n"
    "[constr_9131] Existence of FrameTriggering.frame: For each FrameTriggering, the reference to Frame "
    "in the role frame shall exist at the time when the System Description is complete."
)

FRAME_NOTE = (
    "One frame can be triggered several times, e.g. on different channels. If a frame has no frame "
    "triggering, it won't be sent at all. A frame triggering has assigned exactly one frame, which it triggers."
)

FRAME_PORT_NOTE = (
    "References to the FramePort on every ECU of the system which sends and/or receives the frame. "
    "References for both the sender and the receiver side shall be included when the system is completely defined."
)

PDU_TRIGGERING_NOTE = (
    "This reference provides the relationship to the Pdu Triggerings that are implemented by the "
    "FrameTriggering. The reference is optional since no PduTriggering can be defined for NmPdus and "
    "XCP Pdus. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=pduTriggering.pduTriggering, "
    "pdu Triggering.variationPoint.shortLabel vh.latestBindingTime=postBuild"
)


class TestFrameTriggering:
    """Test cases for FrameTriggering (Table 6.79, p.418) via the concrete CanFrameTriggering subclass."""

    MEMBERS = [
        "frameRef",
        "framePortRefs",
        "pduTriggeringRefs",
    ]

    def _create(self, short_name: str) -> CanFrameTriggering:
        pkg = AUTOSAR.getInstance().createARPackage("FrameTriggeringPkg")
        return CanFrameTriggering(pkg, short_name)

    def _ref(self, value: str) -> RefType:
        ref = RefType()
        ref.setDest("FRAME")
        ref.setValue(value)
        return ref

    def test_inheritance(self):
        assert issubclass(FrameTriggering, Identifiable)
        assert issubclass(FrameTriggering, VariationPointCapable)
        assert issubclass(FrameTriggering, ARObject)

    def test_abstract_instantiation(self):
        pkg = AUTOSAR.getInstance().createARPackage("FrameTriggeringAbstractPkg")
        with pytest.raises(TypeError):
            FrameTriggering(pkg, "Ft")

    def test_class_docstring_note(self):
        assert inspect.cleandoc(FrameTriggering.__doc__) == CLASS_NOTE

    def test_init_docless(self):
        assert FrameTriggering.__init__.__doc__ is None

    def test_initialization_defaults(self):
        triggering = self._create("Ft")
        assert triggering.getFrameRef() is None
        assert triggering.getFramePortRefs() == []
        assert triggering.getPduTriggeringRefs() == []

    def test_member_order(self):
        triggering = self._create("Ft")
        members = [k for k in vars(triggering) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_get_set_frame_ref(self):
        triggering = self._create("Ft")
        ref = self._ref("/Frame1")
        assert triggering == triggering.setFrameRef(ref)
        assert triggering.getFrameRef() == ref

        assert triggering == triggering.setFrameRef(None)
        assert triggering.getFrameRef() == ref

        getter_hints = _get_type_hints(FrameTriggering.getFrameRef)
        assert getter_hints.get("return") == typing.Optional[RefType]

        setter_hints = _get_type_hints(FrameTriggering.setFrameRef)
        assert setter_hints.get("value") == typing.Optional[RefType]
        assert setter_hints.get("return") is FrameTriggering

    def test_add_frame_port_ref(self):
        triggering = self._create("Ft")
        ref1 = RefType()
        ref1.setDest("FRAME-PORT")
        ref1.setValue("/FramePort1")
        ref2 = RefType()
        ref2.setDest("FRAME-PORT")
        ref2.setValue("/FramePort2")

        assert triggering == triggering.addFramePortRef(ref1)
        assert triggering == triggering.addFramePortRef(ref2)
        assert triggering.getFramePortRefs() == [ref1, ref2]

        assert triggering == triggering.addFramePortRef(None)
        assert triggering.getFramePortRefs() == [ref1, ref2]

        getter_hints = _get_type_hints(FrameTriggering.getFramePortRefs)
        assert getter_hints.get("return") == typing.List[RefType]

        adder_hints = _get_type_hints(FrameTriggering.addFramePortRef)
        assert adder_hints.get("value") == typing.Optional[RefType]
        assert adder_hints.get("return") is FrameTriggering

    def test_add_pdu_triggering_ref(self):
        triggering = self._create("Ft")
        ref1 = RefType()
        ref1.setDest("PDU-TRIGGERING")
        ref1.setValue("/PduTriggering1")
        ref2 = RefType()
        ref2.setDest("PDU-TRIGGERING")
        ref2.setValue("/PduTriggering2")

        assert triggering == triggering.addPduTriggeringRef(ref1)
        assert triggering == triggering.addPduTriggeringRef(ref2)
        assert triggering.getPduTriggeringRefs() == [ref1, ref2]

        assert triggering == triggering.addPduTriggeringRef(None)
        assert triggering.getPduTriggeringRefs() == [ref1, ref2]

        getter_hints = _get_type_hints(FrameTriggering.getPduTriggeringRefs)
        assert getter_hints.get("return") == typing.List[RefType]

        adder_hints = _get_type_hints(FrameTriggering.addPduTriggeringRef)
        assert adder_hints.get("value") == typing.Optional[RefType]
        assert adder_hints.get("return") is FrameTriggering

    def test_docstrings_are_spec_notes(self):
        """Test that the getter/adder docstrings carry the attribute Notes verbatim (Table 6.79)."""
        assert FrameTriggering.getFrameRef.__doc__.strip() == FRAME_NOTE
        assert inspect.cleandoc(FrameTriggering.setFrameRef.__doc__).strip() == FRAME_NOTE + "\nA None value is a no-op and does not overwrite an existing frameRef."
        assert FrameTriggering.getFramePortRefs.__doc__.strip() == FRAME_PORT_NOTE
        assert FrameTriggering.addFramePortRef.__doc__.strip() == FRAME_PORT_NOTE
        assert FrameTriggering.getPduTriggeringRefs.__doc__.strip() == PDU_TRIGGERING_NOTE
        assert FrameTriggering.addPduTriggeringRef.__doc__.strip() == PDU_TRIGGERING_NOTE
