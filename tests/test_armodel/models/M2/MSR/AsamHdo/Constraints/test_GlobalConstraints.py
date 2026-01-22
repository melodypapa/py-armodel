"""
This module contains tests for the GlobalConstraints module in MSR.AsamHdo.Constraints.
"""
from armodel.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints import *
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage


class TestInternalConstrs:
    """Test class for InternalConstrs class."""
    
    def test_internal_constrs_initialization(self):
        """Test that an InternalConstrs object can be initialized with default values."""
        internal_constrs = InternalConstrs()
        assert internal_constrs.lower_limit is None
        assert internal_constrs.upper_limit is None


class TestPhysConstrs:
    """Test class for PhysConstrs class."""
    
    def test_phys_constrs_initialization(self):
        """Test that a PhysConstrs object can be initialized with default values."""
        phys_constrs = PhysConstrs()
        assert phys_constrs.lower_limit is None
        assert phys_constrs.upper_limit is None
        assert phys_constrs.unit_ref is None


class TestDataConstrRule:
    """Test class for DataConstrRule class."""
    
    def test_data_constr_rule_initialization(self):
        """Test that a DataConstrRule object can be initialized with default values."""
        data_constr_rule = DataConstrRule()
        assert data_constr_rule.constrLevel is None
        assert data_constr_rule.internalConstrs is None
        assert data_constr_rule.physConstrs is None


class TestDataConstr:
    """Test class for DataConstr class."""
    
    def test_data_constr_initialization(self):
        """Test that a DataConstr object can be initialized with default values."""
        parent_obj = ARPackage(None, "parent_test")  # Using ARPackage as a concrete ARObject subclass
        data_constr = DataConstr(parent_obj, "test_name")
        assert data_constr.data_constr_rule == []
    
    def test_data_constr_rule_methods(self):
        """Test adding and getting data constraint rules."""
        parent_obj = ARPackage(None, "parent_test")  # Using ARPackage as a concrete ARObject subclass
        data_constr = DataConstr(parent_obj, "test_name")
        rule = DataConstrRule()
        
        # Test addDataConstrRule and getDataConstrRules
        data_constr.addDataConstrRule(rule)
        rules = data_constr.getDataConstrRules()
        assert rule in rules
        assert len(rules) == 1