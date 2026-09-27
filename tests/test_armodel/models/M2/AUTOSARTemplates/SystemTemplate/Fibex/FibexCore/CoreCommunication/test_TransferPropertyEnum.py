import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    TransferPropertyEnum,
)

CLASS_NOTE = "Transfer Properties of a Signal."


class TestTransferPropertyEnum:
    """Test cases for TransferPropertyEnum (Table 6.15, p.327)."""

    def test_member_presence_and_values(self):
        assert TransferPropertyEnum.PENDING == "pending"
        assert TransferPropertyEnum.TRIGGERED == "triggered"
        assert TransferPropertyEnum.TRIGGERED_ON_CHANGE == "triggeredOnChange"
        assert TransferPropertyEnum.TRIGGERED_ON_CHANGE_WITHOUT_REPETITION == "triggeredOnChangeWithoutRepetition"
        assert TransferPropertyEnum.TRIGGERED_WITHOUT_REPETITION == "triggeredWithoutRepetition"
        assert list(TransferPropertyEnum().getEnumValues()) == [
            "pending",
            "triggered",
            "triggeredOnChange",
            "triggeredOnChangeWithoutRepetition",
            "triggeredWithoutRepetition",
        ]

    def test_instantiability(self):
        enum = TransferPropertyEnum()
        assert enum == enum.setValue(TransferPropertyEnum.TRIGGERED_ON_CHANGE)
        assert enum.getValue() == "triggeredOnChange"

    def test_class_docstring_note(self):
        assert inspect.cleandoc(TransferPropertyEnum.__doc__) == CLASS_NOTE
