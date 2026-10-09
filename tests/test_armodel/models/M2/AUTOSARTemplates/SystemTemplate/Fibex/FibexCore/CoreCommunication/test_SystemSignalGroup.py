import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import SystemSignalGroup

CLASS_NOTE = (
    "A signal group refers to a set of signals that shall always be kept together. A signal group is used to "
    "guarantee the atomic transfer of AUTOSAR composite data types. The SystemSignalGroup defines a signal "
    "grouping on VFB level. On cluster level the Signal grouping is described by the ISignalGroup element. "
    "Tags: atp.recommendedPackage=SystemSignalGroups"
)
NOTES = {
    "systemSignalRefs": "Reference to a set of SystemSignals that shall always be kept together.",
    "transformingSystemSignalRef": "Optional reference to the SystemSignal which shall contain the transformed (linear) data.",
}


class TestSystemSignalGroup:
    """Test cases for SystemSignalGroup (Table 6.13, p.324)."""

    def test_inheritance(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement

        assert issubclass(SystemSignalGroup, ARElement)

    def test_initialization_defaults(self):
        group = SystemSignalGroup(None, "Group")
        assert group.getSystemSignalRefs() == []
        assert group.getTransformingSystemSignalRef() is None

    def test_get_set_transforming_system_signal_ref(self):
        group = SystemSignalGroup(None, "Group")

        ref = RefType()
        ref.value = "/system_signals/transformed"
        assert group.setTransformingSystemSignalRef(ref) is group
        assert group.getTransformingSystemSignalRef() is ref
        group.setTransformingSystemSignalRef(None)
        assert group.getTransformingSystemSignalRef() is ref

    def test_add_refs_append_and_none_noop(self):
        group = SystemSignalGroup(None, "Group")

        ref = RefType()
        ref.value = "/system_signals/signal1"
        assert group.addSystemSignalRef(ref) is group
        assert group.getSystemSignalRefs() == [ref]
        group.addSystemSignalRef(None)
        assert group.getSystemSignalRefs() == [ref]

    def test_class_docstring_note(self):
        assert inspect.cleandoc(SystemSignalGroup.__doc__) == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        group = SystemSignalGroup(None, "Group")
        pairs = (
            ("getSystemSignalRefs", "addSystemSignalRef", "systemSignalRefs"),
            ("getTransformingSystemSignalRef", "setTransformingSystemSignalRef", "transformingSystemSignalRef"),
        )
        for getter_name, mutator_name, key in pairs:
            getter = getattr(group, getter_name)
            mutator = getattr(group, mutator_name)
            assert inspect.cleandoc(getter.__doc__) == NOTES[key], key
            assert inspect.cleandoc(mutator.__doc__).split("\n")[0] == NOTES[key], key

    def test_init_has_no_docstring(self):
        assert SystemSignalGroup.__init__.__doc__ is None
