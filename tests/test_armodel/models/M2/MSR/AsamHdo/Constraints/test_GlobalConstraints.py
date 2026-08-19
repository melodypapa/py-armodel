"""
This module contains tests for the GlobalConstraints module in MSR.AsamHdo.Constraints.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Limit,
    MonotonyEnum,
    RefType,
)
from armodel.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints import (
    DataConstr,
    DataConstrRule,
    InternalConstrs,
    PhysConstrs,
    ScaleConstr,
)


class TestInternalConstrs:
    """Test class for InternalConstrs class."""

    def test_internal_constrs_initialization(self):
        """Test that an InternalConstrs object can be initialized with default values."""
        internal_constrs = InternalConstrs()
        assert internal_constrs.lower_limit is None
        assert internal_constrs.upper_limit is None


class TestScaleConstr:
    """Test class for ScaleConstr class."""

    def test_scale_constr_initialization(self):
        """Test that a ScaleConstr object can be initialized with default values."""
        scale_constr = ScaleConstr()
        assert scale_constr.getShortLabel() is None
        assert scale_constr.getUpperLimit() is None
        assert scale_constr.getValidity() is None

    def test_scale_constr_methods(self):
        """Test ScaleConstr setter/getter chaining."""
        scale_constr = ScaleConstr()
        limit = Limit()
        scale_constr.setUpperLimit(limit)
        assert scale_constr.getUpperLimit() is limit
        assert scale_constr.setShortLabel(None) is scale_constr


class TestPhysConstrs:
    """Test class for PhysConstrs class."""

    def test_phys_constrs_initialization(self):
        """Test that a PhysConstrs object can be initialized with default values."""
        phys_constrs = PhysConstrs()
        assert phys_constrs.getLowerLimit() is None
        assert phys_constrs.getUpperLimit() is None
        assert phys_constrs.getMaxDiff() is None
        assert phys_constrs.getMaxGradient() is None
        assert phys_constrs.getMonotony() is None
        assert phys_constrs.getScaleConstrs() == []
        assert phys_constrs.getUnitRef() is None

    def test_phys_constrs_methods(self):
        """Test PhysConstrs setter/getter chaining and the ordered scaleConstrs list."""
        phys_constrs = PhysConstrs()

        lower = Limit()
        phys_constrs.setLowerLimit(lower)
        assert phys_constrs.getLowerLimit() is lower

        upper = Limit()
        phys_constrs.setUpperLimit(upper)
        assert phys_constrs.getUpperLimit() is upper

        monotony = MonotonyEnum.INCREASING
        phys_constrs.setMonotony(monotony)
        assert phys_constrs.getMonotony() is monotony

        unit_ref = RefType()
        phys_constrs.setUnitRef(unit_ref)
        assert phys_constrs.getUnitRef() is unit_ref

        scale1 = ScaleConstr()
        scale2 = ScaleConstr()
        phys_constrs.addScaleConstr(scale1)
        phys_constrs.addScaleConstr(scale2)
        assert phys_constrs.getScaleConstrs() == [scale1, scale2]

        assert phys_constrs.setLowerLimit(None) is phys_constrs


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
