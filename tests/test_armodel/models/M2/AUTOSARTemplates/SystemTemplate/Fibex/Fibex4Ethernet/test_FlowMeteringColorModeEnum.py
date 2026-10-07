import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    FlowMeteringColorModeEnum,
)

CLASS_NOTE = "Defines whether Flow Metering color-aware or color-blind mode is used. Tags: atp.Status=candidate"


class TestFlowMeteringColorModeEnum:
    """Test cases for FlowMeteringColorModeEnum (CP_TPS_SystemTemplate Table 3.99, p.144, R23-11)."""

    def test_member_presence_and_values(self):
        assert FlowMeteringColorModeEnum.COLOR_AWARE == "COLOR-AWARE"
        assert FlowMeteringColorModeEnum.COLOR_BLIND == "COLOR-BLIND"
        assert list(FlowMeteringColorModeEnum().getEnumValues()) == ["COLOR-AWARE", "COLOR-BLIND"]

    def test_instantiability_round_trip(self):
        color_aware = FlowMeteringColorModeEnum().setValue(FlowMeteringColorModeEnum.COLOR_AWARE)
        assert color_aware.getValue() == FlowMeteringColorModeEnum.COLOR_AWARE

        color_blind = FlowMeteringColorModeEnum().setValue(FlowMeteringColorModeEnum.COLOR_BLIND)
        assert color_blind.getValue() == FlowMeteringColorModeEnum.COLOR_BLIND

    def test_class_docstring_note(self):
        assert inspect.cleandoc(FlowMeteringColorModeEnum.__doc__) == CLASS_NOTE
