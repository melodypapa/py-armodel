"""
This module contains tests for the EOCEventRef class in the
AUTOSAR CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint import (
    EOCEventRef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestEOCEventRef:
    """
    Test class for EOCEventRef functionality.
    """

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_initialization(self):
        parent = self._parent()
        event_ref = EOCEventRef(parent, "EventRef1")
        assert isinstance(event_ref, EOCEventRef)
        assert event_ref.getShortName() == "EventRef1"
        assert event_ref.getBswModuleInstanceRef() is None
        assert event_ref.getComponentIRef() is None
        assert event_ref.getEventRef() is None
        assert event_ref.getSuccessorRefs() == []

    def test_base_properties(self):
        parent = self._parent()
        event_ref = EOCEventRef(parent, "EventRef1")

        assert event_ref.addDirectSuccessorRef(RefType().setValue("/AUTOSAR/Entity1").setDest("EOC-EXECUTABLE-ENTITY-REF")) is event_ref

        refs = event_ref.getDirectSuccessorRefs()
        assert len(refs) == 1
        assert refs[0].getValue() == "/AUTOSAR/Entity1"

        event_ref.addDirectSuccessorRef(None)
        assert len(event_ref.getDirectSuccessorRefs()) == 1

    def test_get_set_bsw_module_instance_ref(self):
        parent = self._parent()
        event_ref = EOCEventRef(parent, "EventRef1")

        ref = RefType().setValue("/AUTOSAR/BswImpl").setDest("BSW-IMPLEMENTATION")
        assert event_ref.setBswModuleInstanceRef(ref) is event_ref
        assert event_ref.getBswModuleInstanceRef() is ref

        event_ref.setBswModuleInstanceRef(None)
        assert event_ref.getBswModuleInstanceRef() is ref

    def test_get_set_component_iref(self):
        parent = self._parent()
        event_ref = EOCEventRef(parent, "EventRef1")

        iref = RefType().setValue("/AUTOSAR/SwcProto").setDest("SW-COMPONENT-PROTOTYPE")
        assert event_ref.setComponentIRef(iref) is event_ref
        assert event_ref.getComponentIRef() is iref

        event_ref.setComponentIRef(None)
        assert event_ref.getComponentIRef() is iref

    def test_get_set_event_ref(self):
        parent = self._parent()
        event_ref = EOCEventRef(parent, "EventRef1")

        ref = RefType().setValue("/AUTOSAR/RteEvent").setDest("RTE-EVENT")
        assert event_ref.setEventRef(ref) is event_ref
        assert event_ref.getEventRef() is ref
        assert event_ref.getEventRef().getValue() == "/AUTOSAR/RteEvent"

        event_ref.setEventRef(None)
        assert event_ref.getEventRef() is ref

    def test_add_get_successor_refs(self):
        parent = self._parent()
        event_ref = EOCEventRef(parent, "EventRef1")

        assert event_ref.addSuccessorRef(RefType().setValue("/AUTOSAR/Entity1").setDest("EOC-EXECUTABLE-ENTITY-REF")) is event_ref

        refs = event_ref.getSuccessorRefs()
        assert len(refs) == 1
        assert refs[0].getValue() == "/AUTOSAR/Entity1"

        event_ref.addSuccessorRef(None)
        assert len(event_ref.getSuccessorRefs()) == 1
