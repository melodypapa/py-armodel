"""
This module contains tests for the EOCExecutableEntityRef class in the
AUTOSAR CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint import (
    EOCExecutableEntityRef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestEOCExecutableEntityRef:
    """
    Test class for EOCExecutableEntityRef functionality.
    """

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_initialization(self):
        parent = self._parent()
        entity_ref = EOCExecutableEntityRef(parent, "Entity1")
        assert isinstance(entity_ref, EOCExecutableEntityRef)
        assert entity_ref.getShortName() == "Entity1"
        assert entity_ref.getBswModuleInstanceRef() is None
        assert entity_ref.getComponentIRef() is None
        assert entity_ref.getExecutableRef() is None
        assert entity_ref.getSuccessorRefs() == []

    def test_base_properties(self):
        parent = self._parent()
        entity_ref = EOCExecutableEntityRef(parent, "Entity1")

        assert entity_ref.addDirectSuccessorRef(RefType().setValue("/AUTOSAR/Group1").setDest("EOC-EXECUTABLE-ENTITY-REF-GROUP")) is entity_ref

        refs = entity_ref.getDirectSuccessorRefs()
        assert len(refs) == 1
        assert refs[0].getValue() == "/AUTOSAR/Group1"
        assert refs[0].getDest() == "EOC-EXECUTABLE-ENTITY-REF-GROUP"

        entity_ref.addDirectSuccessorRef(None)
        assert len(entity_ref.getDirectSuccessorRefs()) == 1

    def test_get_set_bsw_module_instance_ref(self):
        parent = self._parent()
        entity_ref = EOCExecutableEntityRef(parent, "Entity1")

        ref = RefType().setValue("/AUTOSAR/BswImpl").setDest("BSW-IMPLEMENTATION")
        assert entity_ref.setBswModuleInstanceRef(ref) is entity_ref
        assert entity_ref.getBswModuleInstanceRef() is ref
        assert entity_ref.getBswModuleInstanceRef().getValue() == "/AUTOSAR/BswImpl"

        entity_ref.setBswModuleInstanceRef(None)
        assert entity_ref.getBswModuleInstanceRef() is ref

    def test_get_set_component_iref(self):
        parent = self._parent()
        entity_ref = EOCExecutableEntityRef(parent, "Entity1")

        iref = RefType().setValue("/AUTOSAR/SwcProto").setDest("SW-COMPONENT-PROTOTYPE")
        assert entity_ref.setComponentIRef(iref) is entity_ref
        assert entity_ref.getComponentIRef() is iref
        assert entity_ref.getComponentIRef().getValue() == "/AUTOSAR/SwcProto"

        entity_ref.setComponentIRef(None)
        assert entity_ref.getComponentIRef() is iref

    def test_get_set_executable_ref(self):
        parent = self._parent()
        entity_ref = EOCExecutableEntityRef(parent, "Entity1")

        ref = RefType().setValue("/AUTOSAR/Runnable").setDest("RUNNABLE-ENTITY")
        assert entity_ref.setExecutableRef(ref) is entity_ref
        assert entity_ref.getExecutableRef() is ref
        assert entity_ref.getExecutableRef().getValue() == "/AUTOSAR/Runnable"

        entity_ref.setExecutableRef(None)
        assert entity_ref.getExecutableRef() is ref

    def test_add_get_successor_refs(self):
        parent = self._parent()
        entity_ref = EOCExecutableEntityRef(parent, "Entity1")

        assert entity_ref.addSuccessorRef(RefType().setValue("/AUTOSAR/Entity2").setDest("EOC-EXECUTABLE-ENTITY-REF")) is entity_ref
        assert entity_ref.addSuccessorRef(RefType().setValue("/AUTOSAR/Entity3").setDest("EOC-EVENT-REF")) is entity_ref

        refs = entity_ref.getSuccessorRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/AUTOSAR/Entity2"
        assert refs[0].getDest() == "EOC-EXECUTABLE-ENTITY-REF"
        assert refs[1].getValue() == "/AUTOSAR/Entity3"

        entity_ref.addSuccessorRef(None)
        assert len(entity_ref.getSuccessorRefs()) == 2
