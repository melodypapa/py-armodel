import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    RxAcceptContainedIPduEnum,
)

CLASS_NOTE = "Defines whether this ContainerIPdu has a fixed set of containedIPdus assigned for reception."


class TestRxAcceptContainedIPduEnum:
    """Test cases for RxAcceptContainedIPduEnum (Table 6.38, p.355)."""

    def test_member_presence_and_values(self):
        assert RxAcceptContainedIPduEnum.ACCEPT_ALL == "ACCEPT-ALL"
        assert RxAcceptContainedIPduEnum.ACCEPT_CONFIGURED == "ACCEPT-CONFIGURED"
        assert list(RxAcceptContainedIPduEnum().getEnumValues()) == [
            RxAcceptContainedIPduEnum.ACCEPT_ALL,
            RxAcceptContainedIPduEnum.ACCEPT_CONFIGURED,
        ]

    def test_instantiability(self):
        enum = RxAcceptContainedIPduEnum()
        assert enum == enum.setValue(RxAcceptContainedIPduEnum.ACCEPT_CONFIGURED)
        assert enum.getValue() == RxAcceptContainedIPduEnum.ACCEPT_CONFIGURED

    def test_class_docstring_note(self):
        assert inspect.cleandoc(RxAcceptContainedIPduEnum.__doc__) == CLASS_NOTE
