import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import (
    FlexrayChannelName,
)

CLASS_NOTE = "Name of the channel."


class TestFlexrayChannelName:
    """Test cases for FlexrayChannelName (Table 3.35, p.89)."""

    def test_member_presence_and_values(self):
        assert FlexrayChannelName.CHANNEL_A == "channelA"
        assert FlexrayChannelName.CHANNEL_B == "channelB"
        assert list(FlexrayChannelName().getEnumValues()) == ["channelA", "channelB"]

    def test_instantiability(self):
        enum = FlexrayChannelName()
        assert enum == enum.setValue(FlexrayChannelName.CHANNEL_B)
        assert enum.getValue() == "channelB"

    def test_class_docstring_note(self):
        assert inspect.cleandoc(FlexrayChannelName.__doc__) == CLASS_NOTE
