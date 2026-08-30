from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior import DataPrototypeGroup
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.InstanceRef import (
    InnerDataPrototypeGroupInCompositionInstanceRef,
    VariableDataPrototypeInCompositionInstanceRef,
)


class TestDataPrototypeGroupInitialization:
    def test_initialization(self):
        """Test DataPrototypeGroup __init__ defaults"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        data_group = DataPrototypeGroup(ar_root, "Group")

        assert data_group is not None
        assert isinstance(data_group, DataPrototypeGroup)
        assert isinstance(data_group, AtpStructureElement)
        assert data_group.getShortName() == "Group"
        assert data_group.dataPrototypeGroupIRefs == []
        assert data_group.implicitDataAccessIRefs == []


class TestDataPrototypeGroupDataPrototypeGroup:
    def test_add_get_data_prototype_group_iref(self):
        """Test addDataPrototypeGroupIRef appends and returns self"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        data_group = DataPrototypeGroup(ar_root, "Group")

        iref = InnerDataPrototypeGroupInCompositionInstanceRef()
        result = data_group.addDataPrototypeGroupIRef(iref)
        assert result is data_group
        assert data_group.getDataPrototypeGroupIRefs() == [iref]

    def test_add_data_prototype_group_iref_none_is_noop(self):
        """Test adding a None dataPrototypeGroup iref is a no-op"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        data_group = DataPrototypeGroup(ar_root, "Group")

        data_group.addDataPrototypeGroupIRef(None)
        assert data_group.getDataPrototypeGroupIRefs() == []

    def test_add_multiple_data_prototype_group_irefs(self):
        """Test adding multiple dataPrototypeGroup irefs"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        data_group = DataPrototypeGroup(ar_root, "Group")

        iref1 = InnerDataPrototypeGroupInCompositionInstanceRef()
        iref2 = InnerDataPrototypeGroupInCompositionInstanceRef()
        data_group.addDataPrototypeGroupIRef(iref1).addDataPrototypeGroupIRef(iref2)
        assert data_group.getDataPrototypeGroupIRefs() == [iref1, iref2]


class TestDataPrototypeGroupImplicitDataAccess:
    def test_add_get_implicit_data_access_iref(self):
        """Test addImplicitDataAccessIRef appends and returns self"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        data_group = DataPrototypeGroup(ar_root, "Group")

        iref = VariableDataPrototypeInCompositionInstanceRef()
        result = data_group.addImplicitDataAccessIRef(iref)
        assert result is data_group
        assert data_group.getImplicitDataAccessIRefs() == [iref]

    def test_add_implicit_data_access_iref_none_is_noop(self):
        """Test adding a None implicitDataAccess iref is a no-op"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        data_group = DataPrototypeGroup(ar_root, "Group")

        data_group.addImplicitDataAccessIRef(None)
        assert data_group.getImplicitDataAccessIRefs() == []

    def test_add_multiple_implicit_data_access_irefs(self):
        """Test adding multiple implicitDataAccess irefs"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        data_group = DataPrototypeGroup(ar_root, "Group")

        iref1 = VariableDataPrototypeInCompositionInstanceRef()
        iref2 = VariableDataPrototypeInCompositionInstanceRef()
        data_group.addImplicitDataAccessIRef(iref1).addImplicitDataAccessIRef(iref2)
        assert data_group.getImplicitDataAccessIRefs() == [iref1, iref2]
