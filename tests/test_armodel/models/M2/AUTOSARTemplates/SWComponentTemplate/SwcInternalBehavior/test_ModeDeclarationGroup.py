"""
This module contains comprehensive tests for the ModeDeclarationGroup module in SWComponentTemplate.SwcInternalBehavior.
Tests cover all classes and methods in the ModeDeclarationGroup.py file to achieve 100% test coverage.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup import IncludedModeDeclarationGroupSet, ModeAccessPoint, ModeSwitchPoint


class TestModeAccessPoint:
    """Test class for ModeAccessPoint class."""

    def test_mode_access_point_initialization(self):
        """Test ModeAccessPoint initialization and methods."""
        mode_access_point = ModeAccessPoint()

        assert mode_access_point.ident is None
        assert mode_access_point.modeGroupIRef is None

        # Test ident methods
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import ModeAccessPointIdent

        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        ident = ModeAccessPointIdent(ar_root, "TestIdent")
        mode_access_point.setIdent(ident)
        assert mode_access_point.getIdent() == ident

        # Test modeGroupIRef methods
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import RModeGroupInAtomicSWCInstanceRef

        iref = RModeGroupInAtomicSWCInstanceRef()
        mode_access_point.setModeGroupIRef(iref)
        assert mode_access_point.getModeGroupIRef() == iref


class TestModeSwitchPoint:
    """Test class for ModeSwitchPoint class."""

    def test_mode_switch_point_initialization(self):
        """Test ModeSwitchPoint initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        mode_switch_point = ModeSwitchPoint(ar_root, "TestModeSwitchPoint")

        assert mode_switch_point.parent == ar_root
        assert mode_switch_point.short_name == "TestModeSwitchPoint"
        assert mode_switch_point.returnValueProvision is None
        assert mode_switch_point.modeGroupIRef is None

        # Test returnValueProvision methods
        return_prov = "test_provision"
        mode_switch_point.setReturnValueProvision(return_prov)
        assert mode_switch_point.getReturnValueProvision() == return_prov

        # Test modeGroupIRef methods
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import PModeGroupInAtomicSwcInstanceRef

        iref = PModeGroupInAtomicSwcInstanceRef()
        mode_switch_point.setModeGroupIRef(iref)
        assert mode_switch_point.getModeGroupIRef() == iref


class TestIncludedModeDeclarationGroupSet:
    """Test class for IncludedModeDeclarationGroupSet class."""

    def test_included_mode_declaration_group_set_initialization(self):
        included_set = IncludedModeDeclarationGroupSet()

        assert included_set.modeDeclarationGroupRefs == []
        assert included_set.prefix is None

        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

        ref = RefType()
        ref.setValue("/Test/ModeGroup")
        assert included_set.addModeDeclarationGroupRef(ref) is included_set
        assert included_set.getModeDeclarationGroupRefs() == [ref]
        assert included_set.addModeDeclarationGroupRef(None) is included_set
        assert included_set.getModeDeclarationGroupRefs() == [ref]

        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier

        prefix = Identifier().setValue("RTE_")
        assert included_set.setPrefix(prefix) is included_set
        assert included_set.getPrefix() is prefix
        assert included_set.setPrefix(None) is included_set
        assert included_set.getPrefix() is prefix

    def test_included_mode_declaration_group_set_class_docstring(self):
        expected = (
            "An IncludedModeDeclarationGroupSet declares that a set of ModeDeclarationGroups used by the software component "
            "for its implementation and consequently these ModeDeclarationGroups become part of the contract."
        )
        assert IncludedModeDeclarationGroupSet.__doc__.strip() == expected
