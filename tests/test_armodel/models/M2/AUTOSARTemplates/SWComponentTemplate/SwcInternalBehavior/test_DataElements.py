"""
This module contains comprehensive tests for the DataElements module in SWComponentTemplate.SwcInternalBehavior.
Tests cover all classes and methods in the DataElements.py file to achieve 100% test coverage.
"""

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import (
    ParameterAccess, VariableAccess
)
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR


class TestParameterAccess:
    """Test class for ParameterAccess class."""
    
    def test_parameter_access_initialization(self):
        """Test ParameterAccess initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        param_access = ParameterAccess(ar_root, "TestParameterAccess")
        
        assert param_access.parent == ar_root
        assert param_access.short_name == "TestParameterAccess"
        assert param_access.returnValueProvision is None
        assert param_access.accessedParameter is None
        assert param_access.swDataDefProps is None
        
        # Test returnValueProvision methods
        return_prov = "test_provision"
        param_access.setReturnValueProvision(return_prov)
        assert param_access.getReturnValueProvision() == return_prov
        
        # Test accessedParameter methods
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import AutosarParameterRef
        param_ref = AutosarParameterRef()
        param_access.setAccessedParameter(param_ref)
        assert param_access.getAccessedParameter() == param_ref
        
        # Test swDataDefProps methods
        from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
        sw_data_def = SwDataDefProps()
        param_access.setSwDataDefProps(sw_data_def)
        assert param_access.getSwDataDefProps() == sw_data_def


class TestVariableAccess:
    """Test class for VariableAccess class."""
    
    def test_variable_access_initialization(self):
        """Test VariableAccess initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        var_access = VariableAccess(ar_root, "TestVariableAccess")
        
        assert var_access.parent == ar_root
        assert var_access.short_name == "TestVariableAccess"
        assert var_access.accessedVariableRef is None
        assert var_access.scope is None
        
        # Test accessedVariableRef methods
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import AutosarVariableRef
        var_ref = AutosarVariableRef()
        var_access.setAccessedVariableRef(var_ref)
        assert var_access.getAccessedVariableRef() == var_ref
        
        # Test scope methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral
        scope = ARLiteral()
        scope.setValue("test_scope")
        var_access.setScope(scope)
        assert var_access.getScope() == scope