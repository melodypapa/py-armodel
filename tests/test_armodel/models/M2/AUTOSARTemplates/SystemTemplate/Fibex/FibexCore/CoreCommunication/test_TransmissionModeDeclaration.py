import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing import (
    ModeDrivenTransmissionModeCondition,
    TransmissionModeCondition,
    TransmissionModeDeclaration,
    TransmissionModeTiming,
)


def _ref():
    ref = RefType()
    ref.value = "/mode/decl"
    return ref


CLASS_NOTE = """AUTOSAR COM provides the possibility to define two different TRANSMISSION MODES (True and False) for each I-PDU. As TransmissionMode selector the signal content can be evaluated via transmissionModeCondition (implemented directly in the COM module) or mode conditions can be defined with the modeDrivenTrue Condition or modeDrivenFalseCondition (evaluated by BswM and invoking Com_SwitchIpduTxMode COM API). If modeDrivenTrueCondition and modeDrivenFalseCondition are defined they shall never evaluate to true both at the same time. The mixing of Transmission Mode Switch via API and signal value is not allowed."""


class TestTransmissionModeDeclaration:
    """Test cases for TransmissionModeDeclaration (Table 6.59, p.392)."""

    def test_initialization_defaults(self):
        obj = TransmissionModeDeclaration()
        assert obj.modeDrivenFalseConditions == []
        assert obj.modeDrivenTrueConditions == []
        assert obj.transmissionModeConditions == []
        assert obj.getTransmissionModeFalseTiming() is None
        assert obj.getTransmissionModeTrueTiming() is None

    def test_setters_round_trip_and_none_noop(self):
        obj = TransmissionModeDeclaration()
        item = ModeDrivenTransmissionModeCondition()
        assert obj.addModeDrivenFalseCondition(item) is obj
        assert obj.modeDrivenFalseConditions == [item]
        obj.addModeDrivenFalseCondition(None)
        assert obj.modeDrivenFalseConditions == [item]
        item = ModeDrivenTransmissionModeCondition()
        assert obj.addModeDrivenTrueCondition(item) is obj
        assert obj.modeDrivenTrueConditions == [item]
        obj.addModeDrivenTrueCondition(None)
        assert obj.modeDrivenTrueConditions == [item]
        item = TransmissionModeCondition()
        assert obj.addTransmissionModeCondition(item) is obj
        assert obj.transmissionModeConditions == [item]
        obj.addTransmissionModeCondition(None)
        assert obj.transmissionModeConditions == [item]
        item = TransmissionModeTiming()
        assert obj.setTransmissionModeFalseTiming(item) is obj
        assert obj.getTransmissionModeFalseTiming() is item
        obj.setTransmissionModeFalseTiming(None)
        assert obj.getTransmissionModeFalseTiming() is item
        item = TransmissionModeTiming()
        assert obj.setTransmissionModeTrueTiming(item) is obj
        assert obj.getTransmissionModeTrueTiming() is item
        obj.setTransmissionModeTrueTiming(None)
        assert obj.getTransmissionModeTrueTiming() is item

    def test_class_docstring_note(self):
        assert inspect.cleandoc(TransmissionModeDeclaration.__doc__).split("\n\n")[0] == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        obj = TransmissionModeDeclaration()
        assert (
            inspect.cleandoc(obj.addModeDrivenFalseCondition.__doc__).split("\n")[0]
            == "Defines the trigger for the Com_SwitchIpduTxMode Transmission Mode switch. Only if all defined modeDriven FalseConditions evaluate to true (AND associated) the transmissionModeFalseTiming shall be activated. mode DrivenTrueCondition and modeDrivenFalseCondition shall never evaluate to true both at the same time."
        )
        assert (
            inspect.cleandoc(obj.addModeDrivenTrueCondition.__doc__).split("\n")[0]
            == "Defines the trigger for the Com_SwitchIpduTxMode Transmission Mode switch. Only if all defined modeDriven TrueConditions evaluate to true (AND associated) the transmissionModeTrueTiming shall be activated. mode DrivenTrueCondition and modeDrivenFalseCondition shall never evaluate to true both at the same time."
        )
        assert (
            inspect.cleandoc(obj.addTransmissionModeCondition.__doc__).split("\n")[0]
            == 'The Transmission Mode Selector evaluates the conditions for a subset of signals and decides which transmission mode should be used. In case only one transmission mode is used there is no need for the "TransmissionMode Condition" and its sub-structure. In case the transmission mode shall be switched using the COM-API "Com_Switch IpduTxMode" there is no need for the "TransmissionMode Condition" and its sub-structure.'
        )
        assert (
            inspect.cleandoc(obj.getTransmissionModeFalseTiming.__doc__)
            == "Timing Specification if the COM Transmission Mode is false. The Transmission Mode Selector is defined to be false, if all Conditions evaluate to false."
        )
        assert (
            inspect.cleandoc(obj.setTransmissionModeFalseTiming.__doc__).split("\n")[0]
            == "Timing Specification if the COM Transmission Mode is false. The Transmission Mode Selector is defined to be false, if all Conditions evaluate to false."
        )
        assert (
            inspect.cleandoc(obj.getTransmissionModeTrueTiming.__doc__)
            == "Timing Specification if the COM Transmission Mode is true. The Transmission Mode Selector is defined to be true, if at least one Condition evaluates to true."
        )
        assert (
            inspect.cleandoc(obj.setTransmissionModeTrueTiming.__doc__).split("\n")[0]
            == "Timing Specification if the COM Transmission Mode is true. The Transmission Mode Selector is defined to be true, if at least one Condition evaluates to true."
        )
