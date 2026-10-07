import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    ContainerIPduHeaderTypeEnum,
)

CLASS_NOTE = "Is used to define the header type and size of ContainerIPdus. The header size includes the header id and the length information."


class TestContainerIPduHeaderTypeEnum:
    """Test cases for ContainerIPduHeaderTypeEnum (Table 6.37, p.355)."""

    def test_member_presence_and_values(self):
        assert ContainerIPduHeaderTypeEnum.LONG_HEADER == "LONG-HEADER"
        assert ContainerIPduHeaderTypeEnum.NO_HEADER == "NO-HEADER"
        assert ContainerIPduHeaderTypeEnum.SHORT_HEADER == "SHORT-HEADER"
        assert list(ContainerIPduHeaderTypeEnum().getEnumValues()) == [
            ContainerIPduHeaderTypeEnum.LONG_HEADER,
            ContainerIPduHeaderTypeEnum.NO_HEADER,
            ContainerIPduHeaderTypeEnum.SHORT_HEADER,
        ]

    def test_instantiability(self):
        enum = ContainerIPduHeaderTypeEnum()
        assert enum == enum.setValue(ContainerIPduHeaderTypeEnum.SHORT_HEADER)
        assert enum.getValue() == ContainerIPduHeaderTypeEnum.SHORT_HEADER

    def test_class_docstring_note(self):
        assert inspect.cleandoc(ContainerIPduHeaderTypeEnum.__doc__) == CLASS_NOTE
