"""
This module contains comprehensive tests for the DataElements module in SWComponentTemplate.SwcInternalBehavior.
Tests cover all classes and methods in the DataElements.py file to achieve 100% test coverage.
"""

import typing

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import AutosarParameterRef, AutosarVariableRef, ParameterAccess, VariableAccess
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps


class TestParameterAccess:
    """Test class for ParameterAccess class."""

    def test_initialization(self):
        """Test ParameterAccess initialization defaults."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        param_access = ParameterAccess(ar_root, "TestParameterAccess")

        assert param_access.parent == ar_root
        assert param_access.short_name == "TestParameterAccess"
        assert param_access.returnValueProvision is None
        assert param_access.accessedParameter is None
        assert param_access.swDataDefProps is None

    def test_get_set_accessedParameter(self):
        """Test accessedParameter round-trip, None no-op and type hints."""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.InstanceRefsUsage import ParameterInAtomicSWCTypeInstanceRef

        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        param_access = ParameterAccess(ar_root, "TestParameterAccess")

        param_ref = AutosarParameterRef()
        iref = ParameterInAtomicSWCTypeInstanceRef()
        target_ref = RefType()
        target_ref.setValue("/Prm")
        iref.setTargetDataPrototypeRef(target_ref)
        param_ref.setAutosarParameterIRef(iref)

        assert param_access.setAccessedParameter(param_ref) is param_access
        assert param_access.getAccessedParameter() is param_ref
        assert param_access.getAccessedParameter().getAutosarParameterIRef().getTargetDataPrototypeRef().getValue() == "/Prm"

        assert param_access.setAccessedParameter(None) is param_access
        assert param_access.getAccessedParameter() is param_ref

        hints = typing.get_type_hints(ParameterAccess.setAccessedParameter)
        assert hints.get("value") == typing.Optional[AutosarParameterRef]
        assert hints.get("return") is ParameterAccess
        assert typing.get_type_hints(ParameterAccess.getAccessedParameter).get("return") == typing.Optional[AutosarParameterRef]

    def test_get_set_swDataDefProps(self):
        """Test swDataDefProps round-trip, None no-op and type hints."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        param_access = ParameterAccess(ar_root, "TestParameterAccess")

        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral

        props = SwDataDefProps()
        access_literal = ARLiteral()
        access_literal.setValue("notAccessible")
        props.setSwCalibrationAccess(access_literal)

        assert param_access.setSwDataDefProps(props) is param_access
        assert param_access.getSwDataDefProps() is props
        assert param_access.getSwDataDefProps().getSwCalibrationAccess().getValue() == "notAccessible"

        assert param_access.setSwDataDefProps(None) is param_access
        assert param_access.getSwDataDefProps() is props

        hints = typing.get_type_hints(ParameterAccess.setSwDataDefProps)
        assert hints.get("value") == typing.Optional[SwDataDefProps]
        assert hints.get("return") is ParameterAccess
        assert typing.get_type_hints(ParameterAccess.getSwDataDefProps).get("return") == typing.Optional[SwDataDefProps]


class TestVariableAccess:
    """Test class for VariableAccess class."""

    def test_initialization(self):
        """Test VariableAccess initialization defaults."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        var_access = VariableAccess(ar_root, "TestVariableAccess")

        assert var_access.parent == ar_root
        assert var_access.short_name == "TestVariableAccess"
        assert var_access.returnValueProvision is None
        assert var_access.accessedVariable is None
        assert var_access.scope is None

    def test_get_set_accessedVariable(self):
        """Test accessedVariable round-trip, None no-op and type hints."""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.InstanceRefsUsage import VariableInAtomicSWCTypeInstanceRef

        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        var_access = VariableAccess(ar_root, "TestVariableAccess")

        var_ref = AutosarVariableRef()
        iref = VariableInAtomicSWCTypeInstanceRef()
        target_ref = RefType()
        target_ref.setValue("/Var")
        iref.setTargetDataPrototypeRef(target_ref)
        var_ref.setAutosarVariableIRef(iref)

        assert var_access.setAccessedVariable(var_ref) is var_access
        assert var_access.getAccessedVariable() is var_ref
        assert var_access.getAccessedVariable().getAutosarVariableIRef().getTargetDataPrototypeRef().getValue() == "/Var"

        assert var_access.setAccessedVariable(None) is var_access
        assert var_access.getAccessedVariable() is var_ref

        hints = typing.get_type_hints(VariableAccess.setAccessedVariable)
        assert hints.get("value") == typing.Optional[AutosarVariableRef]
        assert hints.get("return") is VariableAccess
        assert typing.get_type_hints(VariableAccess.getAccessedVariable).get("return") == typing.Optional[AutosarVariableRef]

    def test_get_set_scope(self):
        """Test scope round-trip, None no-op and type hints."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral

        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        var_access = VariableAccess(ar_root, "TestVariableAccess")

        scope = ARLiteral()
        scope.setValue("communicationIntraPartition")

        assert var_access.setScope(scope) is var_access
        assert var_access.getScope() is scope
        assert var_access.getScope().getValue() == "communicationIntraPartition"

        assert var_access.setScope(None) is var_access
        assert var_access.getScope() is scope

        hints = typing.get_type_hints(VariableAccess.setScope)
        assert hints.get("value") == typing.Optional[ARLiteral]
        assert hints.get("return") is VariableAccess
        assert typing.get_type_hints(VariableAccess.getScope).get("return") == typing.Optional[ARLiteral]
