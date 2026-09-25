"""
This module contains comprehensive tests for the ModeDeclarationGroup module in SWComponentTemplate.SwcInternalBehavior.
Tests cover all classes and methods in the ModeDeclarationGroup.py file to achieve 100% test coverage.
"""

import typing

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import ModeGroupInAtomicSwcInstanceRef, PModeGroupInAtomicSwcInstanceRef, RModeGroupInAtomicSWCInstanceRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import ModeAccessPointIdent
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup import IncludedModeDeclarationGroupSet, ModeAccessPoint, ModeSwitchPoint


def _make_ref(value):
    ref = RefType()
    ref.setValue(value)
    return ref


class TestModeAccessPoint:
    """Test class for ModeAccessPoint class."""

    def test_initialization(self):
        """Test ModeAccessPoint initialization defaults."""
        mode_access_point = ModeAccessPoint()

        assert mode_access_point.ident is None
        assert mode_access_point.modeGroupIRef is None

    def test_create_ident(self):
        """Test ident factory: appended, duplicate returns existing."""
        mode_access_point = ModeAccessPoint()

        ident = mode_access_point.createIdent("map_ident")
        assert isinstance(ident, ModeAccessPointIdent)
        assert ident.getShortName() == "map_ident"
        assert mode_access_point.getIdent() is ident
        assert mode_access_point.createIdent("map_ident") is ident

    def test_get_set_modeGroupIRef(self):
        """Test modeGroupIRef round-trip, polymorphic P/R variants and None no-op."""
        mode_access_point = ModeAccessPoint()

        iref = RModeGroupInAtomicSWCInstanceRef()
        iref.setContextRPortRef(_make_ref("/rp"))
        iref.setTargetModeGroupRef(_make_ref("/mg"))
        assert mode_access_point.setModeGroupIRef(iref) is mode_access_point
        assert mode_access_point.getModeGroupIRef() is iref

        assert mode_access_point.setModeGroupIRef(None) is mode_access_point
        assert mode_access_point.getModeGroupIRef() is iref

        piref = PModeGroupInAtomicSwcInstanceRef()
        piref.setContextPPortRef(_make_ref("/pp"))
        piref.setTargetModeGroupRef(_make_ref("/mg"))
        mode_access_point.setModeGroupIRef(piref)
        assert mode_access_point.getModeGroupIRef() is piref

    def test_get_type_hints(self):
        """Test spec-typed annotations resolve at runtime (plain get_type_hints)."""
        hints = typing.get_type_hints(ModeAccessPoint.setModeGroupIRef)
        assert hints.get("value") == typing.Optional[ModeGroupInAtomicSwcInstanceRef]
        assert hints.get("return") is ModeAccessPoint

        assert typing.get_type_hints(ModeAccessPoint.getModeGroupIRef).get("return") == typing.Optional[ModeGroupInAtomicSwcInstanceRef]
        assert typing.get_type_hints(ModeAccessPoint.getIdent).get("return") == typing.Optional[ModeAccessPointIdent]

        create_hints = typing.get_type_hints(ModeAccessPoint.createIdent)
        assert create_hints.get("short_name") is str
        assert create_hints.get("return") is ModeAccessPointIdent

    def test_ident_is_created_not_set(self):
        """Rule 0001.6: ModeAccessPointIdent is a 0..1 Referrable child, created via createIdent(short_name)."""
        assert not hasattr(ModeAccessPoint, "setIdent")


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
