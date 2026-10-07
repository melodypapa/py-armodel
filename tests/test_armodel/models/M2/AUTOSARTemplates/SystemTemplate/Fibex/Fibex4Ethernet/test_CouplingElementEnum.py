import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    CouplingElementEnum,
)

CLASS_NOTE = "Identifies the Coupling type."


class TestCouplingElementEnum:
    """Test cases for CouplingElementEnum (CP_TPS_SystemTemplate Table 3.53, p.108, R23-11)."""

    def test_member_presence_and_values(self):
        assert CouplingElementEnum.HUB == "HUB"
        assert CouplingElementEnum.ROUTER == "ROUTER"
        assert CouplingElementEnum.SWITCH == "SWITCH"
        assert list(CouplingElementEnum().getEnumValues()) == ["HUB", "ROUTER", "SWITCH"]

    def test_instantiability_round_trip(self):
        hub = CouplingElementEnum().setValue(CouplingElementEnum.HUB)
        assert hub.getValue() == CouplingElementEnum.HUB

        router = CouplingElementEnum().setValue(CouplingElementEnum.ROUTER)
        assert router.getValue() == CouplingElementEnum.ROUTER

        switch = CouplingElementEnum().setValue(CouplingElementEnum.SWITCH)
        assert switch.getValue() == CouplingElementEnum.SWITCH

    def test_class_docstring_note(self):
        assert inspect.cleandoc(CouplingElementEnum.__doc__) == CLASS_NOTE
