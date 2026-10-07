import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import TriggerToSignalMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import TriggerInSystemInstanceRef


def _ref(value: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    return ref


class TestTriggerToSignalMapping:
    """Test cases for TriggerToSignalMapping (Table 5.35, p.250)."""

    MEMBERS = [
        "systemSignalRef",
        "triggerIRef",
    ]

    def test_inheritance(self):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import DataMapping

        assert issubclass(TriggerToSignalMapping, DataMapping)

    def test_class_docstring_note(self):
        expected = (
            "This meta-class represents the ability to map a trigger to a SystemSignal of size 0. "
            "The Trigger does not transport any other information than its existence, therefore the limitation in terms of signal length."
        )
        assert inspect.cleandoc(TriggerToSignalMapping.__doc__).split("\n\n")[0] == expected

    def test_init_has_no_docstring(self):
        assert TriggerToSignalMapping.__init__.__doc__ is None

    def test_initialization_defaults(self):
        mapping = TriggerToSignalMapping()
        assert mapping.getTriggerIRef() is None
        assert mapping.getSystemSignalRef() is None

    def test_member_order(self):
        mapping = TriggerToSignalMapping()
        members = [k for k in vars(mapping) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_get_set_trigger_i_ref(self):
        mapping = TriggerToSignalMapping()
        iref = TriggerInSystemInstanceRef()
        result = mapping.setTriggerIRef(iref)
        assert result is mapping
        assert mapping.getTriggerIRef() is iref
        mapping.setTriggerIRef(None)
        assert mapping.getTriggerIRef() is iref

    def test_get_set_system_signal_ref(self):
        mapping = TriggerToSignalMapping()
        result = mapping.setSystemSignalRef(_ref("/SystemSignal"))
        assert result is mapping
        assert mapping.getSystemSignalRef().getValue() == "/SystemSignal"
        mapping.setSystemSignalRef(None)
        assert mapping.getSystemSignalRef().getValue() == "/SystemSignal"

    def test_type_hints(self):
        hints = typing.get_type_hints(TriggerToSignalMapping.getTriggerIRef)
        assert hints["return"] == typing.Optional[TriggerInSystemInstanceRef]
        hints = typing.get_type_hints(TriggerToSignalMapping.setTriggerIRef)
        assert hints["value"] == typing.Optional[TriggerInSystemInstanceRef]
        assert hints["return"] is TriggerToSignalMapping
        hints = typing.get_type_hints(TriggerToSignalMapping.getSystemSignalRef)
        assert hints["return"] == typing.Optional[RefType]
        hints = typing.get_type_hints(TriggerToSignalMapping.setSystemSignalRef)
        assert hints["value"] == typing.Optional[RefType]
        assert hints["return"] is TriggerToSignalMapping
