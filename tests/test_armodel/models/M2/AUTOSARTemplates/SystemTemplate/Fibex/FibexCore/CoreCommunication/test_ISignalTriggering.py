import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import ISignalTriggering

CLASS_NOTE = "A ISignalTriggering allows an assignment of ISignals to physical channels."
NOTES = {
    "iSignalRef": ("This reference shall be used if an ISignal is transported on the PhysicalChannel. This reference forms an XOR " "relationship with the ISignalTriggering-ISignalGroup reference."),
    "iSignalGroupRef": (
        "This reference shall be used if an ISignalGroup is transported on the PhysicalChannel. This reference forms an XOR " "relationship with the ISignal Triggering-ISignal reference."
    ),
    "iSignalPortRefs": (
        "References to the ISignalPort on every ECU of the system which sends and/or receives the ISignal. References for "
        "both the sender and the receiver side shall be included when the system is completely defined."
    ),
}


class TestISignalTriggering:
    """Test cases for ISignalTriggering (Table 6.16, p.330)."""

    def test_inheritance(self):
        assert issubclass(ISignalTriggering, Identifiable)
        assert issubclass(ISignalTriggering, VariationPointCapable)

    def test_initialization_defaults(self):
        triggering = ISignalTriggering(None, "Triggering")
        assert triggering.getISignalRef() is None
        assert triggering.getISignalGroupRef() is None
        assert triggering.getISignalPortRefs() == []
        assert triggering.getVariationPoint() is None

    def test_get_set_i_signal_ref(self):
        triggering = ISignalTriggering(None, "Triggering")

        ref = RefType()
        ref.value = "/ISignals/ISignal1"
        assert triggering.setISignalRef(ref) is triggering
        assert triggering.getISignalRef() is ref
        triggering.setISignalRef(None)
        assert triggering.getISignalRef() is ref

    def test_get_set_i_signal_group_ref(self):
        triggering = ISignalTriggering(None, "Triggering")

        ref = RefType()
        ref.value = "/ISignalGroups/ISignalGroup1"
        assert triggering.setISignalGroupRef(ref) is triggering
        assert triggering.getISignalGroupRef() is ref
        triggering.setISignalGroupRef(None)
        assert triggering.getISignalGroupRef() is ref

    def test_add_i_signal_port_refs(self):
        triggering = ISignalTriggering(None, "Triggering")

        ref1 = RefType()
        ref1.value = "/ECUs/Ecu1/ISignalPorts/Port1"
        assert triggering.addISignalPortRef(ref1) is triggering
        ref2 = RefType()
        ref2.value = "/ECUs/Ecu2/ISignalPorts/Port2"
        assert triggering.addISignalPortRef(ref2) is triggering
        assert triggering.getISignalPortRefs() == [ref1, ref2]
        triggering.addISignalPortRef(None)
        assert triggering.getISignalPortRefs() == [ref1, ref2]

    def test_class_docstring_note(self):
        assert inspect.cleandoc(ISignalTriggering.__doc__) == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        triggering = ISignalTriggering(None, "Triggering")
        pairs = (
            ("getISignalRef", "setISignalRef", "iSignalRef"),
            ("getISignalGroupRef", "setISignalGroupRef", "iSignalGroupRef"),
            ("getISignalPortRefs", "addISignalPortRef", "iSignalPortRefs"),
        )
        for getter_name, mutator_name, key in pairs:
            getter = getattr(triggering, getter_name)
            mutator = getattr(triggering, mutator_name)
            assert inspect.cleandoc(getter.__doc__) == NOTES[key], key
            assert inspect.cleandoc(mutator.__doc__).split("\n")[0] == NOTES[key], key

    def test_init_has_no_docstring(self):
        assert ISignalTriggering.__init__.__doc__ is None
