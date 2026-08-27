import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventVfb import (
    ConcreteTDEventVfb,
    TDEventModeDeclaration,
    TDEventOperation,
    TDEventTrigger,
    TDEventVariableDataPrototype,
    TDEventVfb,
    TDEventVfbPort,
    TDEventVfbReference,
)


class TestTDEventVfbFamily:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_vfb_abstract(self):
        with pytest.raises(TypeError, match="TDEventVfb is an abstract class"):
            TDEventVfb(self._parent(), "Event1")

    def test_vfb_port_abstract(self):
        with pytest.raises(TypeError, match="TDEventVfbPort is an abstract class"):
            TDEventVfbPort(self._parent(), "Event1")

    def test_concrete_subclass_of_base_chain(self):
        event = ConcreteTDEventVfb(self._parent(), "Event1")
        assert isinstance(event, TDEventVfb)
        assert event.getShortName() == "Event1"
        assert event.getComponentIRef() is None

    def test_vfb_reference(self):
        parent = self._parent()
        event = TDEventVfbReference(parent, "Event1")
        assert isinstance(event, TDEventVfb)
        assert event.getReferencedTDEventVfbRef() is None

    def test_mode_declaration_defaults(self):
        parent = self._parent()
        event = TDEventModeDeclaration(parent, "Event1")
        assert isinstance(event, TDEventVfbPort)
        assert event.getIsExternal() is None
        assert event.getPortRef() is None
        assert event.getPortPrototypeBlueprintRef() is None
        assert event.getEntryModeDeclarationRef() is None
        assert event.getExitModeDeclarationRef() is None
        assert event.getModeDeclarationRef() is None

    def test_operation_members(self):
        parent = self._parent()
        event = TDEventOperation(parent, "Event1")
        assert event.getOperationRef() is None
        assert event.getTdEventOperationType() is None

    def test_trigger_members(self):
        parent = self._parent()
        event = TDEventTrigger(parent, "Event1")
        assert event.getTriggerRef() is None
        assert event.getTdEventTriggerType() is None

    def test_variable_data_prototype_members(self):
        parent = self._parent()
        event = TDEventVariableDataPrototype(parent, "Event1")
        assert event.getDataElementRef() is None
        assert event.getTdEventVariableDataPrototypeType() is None
