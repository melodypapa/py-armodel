import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    TransferPropertyEnum,
)

CLASS_NOTE = "Transfer Properties of a Signal."


class TestTransferPropertyEnum:
    """Test cases for TransferPropertyEnum (Table 6.15, p.327)."""

    def test_member_presence_and_values(self):
        assert TransferPropertyEnum.PENDING == "PENDING"
        assert TransferPropertyEnum.TRIGGERED == "TRIGGERED"
        assert TransferPropertyEnum.TRIGGERED_ON_CHANGE == "TRIGGERED-ON-CHANGE"
        assert TransferPropertyEnum.TRIGGERED_ON_CHANGE_WITHOUT_REPETITION == "TRIGGERED-ON-CHANGE-WITHOUT-REPETITION"
        assert TransferPropertyEnum.TRIGGERED_WITHOUT_REPETITION == "TRIGGERED-WITHOUT-REPETITION"
        assert list(TransferPropertyEnum().getEnumValues()) == [
            "PENDING",
            "TRIGGERED",
            TransferPropertyEnum.TRIGGERED_ON_CHANGE,
            TransferPropertyEnum.TRIGGERED_ON_CHANGE_WITHOUT_REPETITION,
            TransferPropertyEnum.TRIGGERED_WITHOUT_REPETITION,
        ]

    def test_instantiability(self):
        enum = TransferPropertyEnum()
        assert enum == enum.setValue(TransferPropertyEnum.TRIGGERED_ON_CHANGE)
        assert enum.getValue() == TransferPropertyEnum.TRIGGERED_ON_CHANGE

    def test_class_docstring_note(self):
        assert inspect.cleandoc(TransferPropertyEnum.__doc__) == CLASS_NOTE
