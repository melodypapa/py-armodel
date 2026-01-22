"""
This module contains tests for the Units module in MSR.AsamHdo.
"""
from armodel.models.M2.MSR.AsamHdo.Units import *
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARFloat, ARNumerical, RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage


class TestPhysicalDimension:
    """Test class for PhysicalDimension class."""
    
    def test_physical_dimension_initialization(self):
        """Test that a PhysicalDimension object can be initialized with default values."""
        parent_obj = ARPackage(None, "parent_test")  # Using ARPackage as a concrete ARObject subclass
        physical_dimension = PhysicalDimension(parent_obj, "test_name")
        assert physical_dimension.currentExp is None
        assert physical_dimension.lengthExp is None
        assert physical_dimension.luminousIntensityExp is None
        assert physical_dimension.massExp is None
        assert physical_dimension.molarAmountExp is None
        assert physical_dimension.temperatureExp is None
        assert physical_dimension.timeExp is None
    
    def test_physical_dimension_current_exp_methods(self):
        """Test the currentExp getter and setter."""
        parent_obj = ARPackage(None, "parent_test")  # Using ARPackage as a concrete ARObject subclass
        physical_dimension = PhysicalDimension(parent_obj, "test_name")
        exp_value = ARNumerical()
        
        result = physical_dimension.setCurrentExp(exp_value)
        assert physical_dimension.getCurrentExp() == exp_value
        assert result == physical_dimension
    
    def test_physical_dimension_length_exp_methods(self):
        """Test the lengthExp getter and setter."""
        parent_obj = ARPackage(None, "parent_test")  # Using ARPackage as a concrete ARObject subclass
        physical_dimension = PhysicalDimension(parent_obj, "test_name")
        exp_value = ARNumerical()
        
        result = physical_dimension.setLengthExp(exp_value)
        assert physical_dimension.getLengthExp() == exp_value
        assert result == physical_dimension
    
    def test_physical_dimension_luminous_intensity_exp_methods(self):
        """Test the luminousIntensityExp getter and setter."""
        parent_obj = ARPackage(None, "parent_test")  # Using ARPackage as a concrete ARObject subclass
        physical_dimension = PhysicalDimension(parent_obj, "test_name")
        exp_value = ARNumerical()
        
        result = physical_dimension.setLuminousIntensityExp(exp_value)
        assert physical_dimension.getLuminousIntensityExp() == exp_value
        assert result == physical_dimension
    
    def test_physical_dimension_mass_exp_methods(self):
        """Test the massExp getter and setter."""
        parent_obj = ARPackage(None, "parent_test")  # Using ARPackage as a concrete ARObject subclass
        physical_dimension = PhysicalDimension(parent_obj, "test_name")
        exp_value = ARNumerical()
        
        result = physical_dimension.setMassExp(exp_value)
        assert physical_dimension.getMassExp() == exp_value
        assert result == physical_dimension
    
    def test_physical_dimension_molar_amount_exp_methods(self):
        """Test the molarAmountExp getter and setter."""
        parent_obj = ARPackage(None, "parent_test")  # Using ARPackage as a concrete ARObject subclass
        physical_dimension = PhysicalDimension(parent_obj, "test_name")
        exp_value = ARNumerical()
        
        result = physical_dimension.setMolarAmountExp(exp_value)
        assert physical_dimension.getMolarAmountExp() == exp_value
        assert result == physical_dimension
    
    def test_physical_dimension_temperature_exp_methods(self):
        """Test the temperatureExp getter and setter."""
        parent_obj = ARPackage(None, "parent_test")  # Using ARPackage as a concrete ARObject subclass
        physical_dimension = PhysicalDimension(parent_obj, "test_name")
        exp_value = ARNumerical()
        
        result = physical_dimension.setTemperatureExp(exp_value)
        assert physical_dimension.getTemperatureExp() == exp_value
        assert result == physical_dimension
    
    def test_physical_dimension_time_exp_methods(self):
        """Test the timeExp getter and setter."""
        parent_obj = ARPackage(None, "parent_test")  # Using ARPackage as a concrete ARObject subclass
        physical_dimension = PhysicalDimension(parent_obj, "test_name")
        exp_value = ARNumerical()
        
        result = physical_dimension.setTimeExp(exp_value)
        assert physical_dimension.getTimeExp() == exp_value
        assert result == physical_dimension


class TestSingleLanguageUnitNames:
    """Test class for SingleLanguageUnitNames class."""
    
    def test_single_language_unit_names_initialization(self):
        """Test that a SingleLanguageUnitNames object can be initialized."""
        single_lang_unit_names = SingleLanguageUnitNames()
        assert single_lang_unit_names is not None


class TestUnit:
    """Test class for Unit class."""
    
    def test_unit_initialization(self):
        """Test that a Unit object can be initialized with default values."""
        parent_obj = ARPackage(None, "parent_test")  # Using ARPackage as a concrete ARObject subclass
        unit = Unit(parent_obj, "test_name")
        assert unit.displayName is None
        assert unit.factorSiToUnit is None
        assert unit.offsetSiToUnit is None
        assert unit.physicalDimensionRef is None
    
    def test_unit_display_name_methods(self):
        """Test the displayName getter and setter."""
        parent_obj = ARPackage(None, "parent_test")  # Using ARPackage as a concrete ARObject subclass
        unit = Unit(parent_obj, "test_name")
        display_name = SingleLanguageUnitNames()
        
        result = unit.setDisplayName(display_name)
        assert unit.getDisplayName() == display_name
        assert result == unit
    
    def test_unit_factor_si_to_unit_methods(self):
        """Test the factorSiToUnit getter and setter."""
        parent_obj = ARPackage(None, "parent_test")  # Using ARPackage as a concrete ARObject subclass
        unit = Unit(parent_obj, "test_name")
        factor = ARFloat()
        
        result = unit.setFactorSiToUnit(factor)
        assert unit.getFactorSiToUnit() == factor
        assert result == unit
    
    def test_unit_offset_si_to_unit_methods(self):
        """Test the offsetSiToUnit getter and setter."""
        parent_obj = ARPackage(None, "parent_test")  # Using ARPackage as a concrete ARObject subclass
        unit = Unit(parent_obj, "test_name")
        offset = ARFloat()
        
        result = unit.setOffsetSiToUnit(offset)
        assert unit.getOffsetSiToUnit() == offset
        assert result == unit
    
    def test_unit_physical_dimension_ref_methods(self):
        """Test the physicalDimensionRef getter and setter."""
        parent_obj = ARPackage(None, "parent_test")  # Using ARPackage as a concrete ARObject subclass
        unit = Unit(parent_obj, "test_name")
        ref = RefType()
        
        result = unit.setPhysicalDimensionRef(ref)
        assert unit.getPhysicalDimensionRef() == ref
        assert result == unit