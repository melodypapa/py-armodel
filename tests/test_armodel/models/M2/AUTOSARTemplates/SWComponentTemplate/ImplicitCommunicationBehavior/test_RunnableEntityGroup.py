from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior import RunnableEntityGroup
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.InstanceRef import (
    InnerRunnableEntityGroupInCompositionInstanceRef,
    RunnableEntityInCompositionInstanceRef,
)


class TestRunnableEntityGroupInitialization:
    def test_initialization(self):
        """Test RunnableEntityGroup __init__ defaults"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        runnable_group = RunnableEntityGroup(ar_root, "Group")

        assert runnable_group is not None
        assert isinstance(runnable_group, RunnableEntityGroup)
        assert isinstance(runnable_group, AtpStructureElement)
        assert runnable_group.getShortName() == "Group"
        assert runnable_group.runnableEntityIRefs == []
        assert runnable_group.runnableEntityGroupIRefs == []


class TestRunnableEntityGroupRunnableEntity:
    def test_add_get_runnable_entity_iref(self):
        """Test addRunnableEntityIRef appends and returns self"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        runnable_group = RunnableEntityGroup(ar_root, "Group")

        iref = RunnableEntityInCompositionInstanceRef()
        result = runnable_group.addRunnableEntityIRef(iref)
        assert result is runnable_group
        assert runnable_group.getRunnableEntityIRefs() == [iref]

    def test_add_runnable_entity_iref_none_is_noop(self):
        """Test adding a None runnableEntity iref is a no-op"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        runnable_group = RunnableEntityGroup(ar_root, "Group")

        runnable_group.addRunnableEntityIRef(None)
        assert runnable_group.getRunnableEntityIRefs() == []

    def test_add_multiple_runnable_entity_irefs(self):
        """Test adding multiple runnableEntity irefs"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        runnable_group = RunnableEntityGroup(ar_root, "Group")

        iref1 = RunnableEntityInCompositionInstanceRef()
        iref2 = RunnableEntityInCompositionInstanceRef()
        runnable_group.addRunnableEntityIRef(iref1).addRunnableEntityIRef(iref2)
        assert runnable_group.getRunnableEntityIRefs() == [iref1, iref2]


class TestRunnableEntityGroupRunnableEntityGroup:
    def test_add_get_runnable_entity_group_iref(self):
        """Test addRunnableEntityGroupIRef appends and returns self"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        runnable_group = RunnableEntityGroup(ar_root, "Group")

        iref = InnerRunnableEntityGroupInCompositionInstanceRef()
        result = runnable_group.addRunnableEntityGroupIRef(iref)
        assert result is runnable_group
        assert runnable_group.getRunnableEntityGroupIRefs() == [iref]

    def test_add_runnable_entity_group_iref_none_is_noop(self):
        """Test adding a None runnableEntityGroup iref is a no-op"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        runnable_group = RunnableEntityGroup(ar_root, "Group")

        runnable_group.addRunnableEntityGroupIRef(None)
        assert runnable_group.getRunnableEntityGroupIRefs() == []

    def test_add_multiple_runnable_entity_group_irefs(self):
        """Test adding multiple runnableEntityGroup irefs"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        runnable_group = RunnableEntityGroup(ar_root, "Group")

        iref1 = InnerRunnableEntityGroupInCompositionInstanceRef()
        iref2 = InnerRunnableEntityGroupInCompositionInstanceRef()
        runnable_group.addRunnableEntityGroupIRef(iref1).addRunnableEntityGroupIRef(iref2)
        assert runnable_group.getRunnableEntityGroupIRefs() == [iref1, iref2]
