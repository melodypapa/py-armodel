import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing import (
    TriggerIPduSendCondition,
)


def _ref():
    ref = RefType()
    ref.value = "/mode/decl"
    return ref


CLASS_NOTE = """The condition defined by this class evaluates to true if one of the referenced modeDeclarations (OR associated) is active. The condition is used to define when the Pdu is triggered with the Com_Trigger IPDUSend API call."""


class TestTriggerIPduSendCondition:
    """Test cases for TriggerIPduSendCondition (Table 6.70, p.399)."""

    def test_initialization_defaults(self):
        obj = TriggerIPduSendCondition()
        assert obj.modeDeclarationRefs == []

    def test_setters_round_trip_and_none_noop(self):
        obj = TriggerIPduSendCondition()
        item = _ref()
        assert obj.addModeDeclarationRef(item) is obj
        assert obj.modeDeclarationRefs == [item]
        obj.addModeDeclarationRef(None)
        assert obj.modeDeclarationRefs == [item]

    def test_class_docstring_note(self):
        assert inspect.cleandoc(TriggerIPduSendCondition.__doc__).split("\n\n")[0] == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        obj = TriggerIPduSendCondition()
        assert inspect.cleandoc(obj.getModeDeclarationRefs.__doc__) == "Reference to one modeDeclaration which is OR associated in the context of the TriggerIPduSend Condition."
