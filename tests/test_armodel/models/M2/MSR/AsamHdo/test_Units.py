"""
This module contains tests for the Units module in MSR.AsamHdo.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARNumerical, Float, RefType
from armodel.models.M2.MSR.AsamHdo.Units import (
    PhysicalDimension,
    SingleLanguageUnitNames,
    Unit,
)


class TestPhysicalDimension:
    """Test class for PhysicalDimension class."""

    def _make(self) -> PhysicalDimension:
        parent_obj = ARPackage(None, "parent_test")
        return PhysicalDimension(parent_obj, "test_name")

    def test_physical_dimension_initialization(self):
        """Test that a PhysicalDimension object can be initialized with default values."""
        physical_dimension = self._make()
        assert physical_dimension.getCurrentExp() is None
        assert physical_dimension.getLengthExp() is None
        assert physical_dimension.getLuminousIntensityExp() is None
        assert physical_dimension.getMassExp() is None
        assert physical_dimension.getMolarAmountExp() is None
        assert physical_dimension.getTemperatureExp() is None
        assert physical_dimension.getTimeExp() is None

    def test_physical_dimension_current_exp_methods(self):
        """Test the currentExp getter and setter including None no-op."""
        physical_dimension = self._make()
        exp_value = ARNumerical()

        result = physical_dimension.setCurrentExp(exp_value)
        assert physical_dimension.getCurrentExp() == exp_value
        assert result == physical_dimension
        assert physical_dimension.setCurrentExp(None) is physical_dimension
        assert physical_dimension.getCurrentExp() == exp_value

    def test_physical_dimension_length_exp_methods(self):
        """Test the lengthExp getter and setter including None no-op."""
        physical_dimension = self._make()
        exp_value = ARNumerical()

        result = physical_dimension.setLengthExp(exp_value)
        assert physical_dimension.getLengthExp() == exp_value
        assert result == physical_dimension
        assert physical_dimension.setLengthExp(None) is physical_dimension
        assert physical_dimension.getLengthExp() == exp_value

    def test_physical_dimension_luminous_intensity_exp_methods(self):
        """Test the luminousIntensityExp getter and setter including None no-op."""
        physical_dimension = self._make()
        exp_value = ARNumerical()

        result = physical_dimension.setLuminousIntensityExp(exp_value)
        assert physical_dimension.getLuminousIntensityExp() == exp_value
        assert result == physical_dimension
        assert physical_dimension.setLuminousIntensityExp(None) is physical_dimension
        assert physical_dimension.getLuminousIntensityExp() == exp_value

    def test_physical_dimension_mass_exp_methods(self):
        """Test the massExp getter and setter including None no-op."""
        physical_dimension = self._make()
        exp_value = ARNumerical()

        result = physical_dimension.setMassExp(exp_value)
        assert physical_dimension.getMassExp() == exp_value
        assert result == physical_dimension
        assert physical_dimension.setMassExp(None) is physical_dimension
        assert physical_dimension.getMassExp() == exp_value

    def test_physical_dimension_molar_amount_exp_methods(self):
        """Test the molarAmountExp getter and setter including None no-op."""
        physical_dimension = self._make()
        exp_value = ARNumerical()

        result = physical_dimension.setMolarAmountExp(exp_value)
        assert physical_dimension.getMolarAmountExp() == exp_value
        assert result == physical_dimension
        assert physical_dimension.setMolarAmountExp(None) is physical_dimension
        assert physical_dimension.getMolarAmountExp() == exp_value

    def test_physical_dimension_temperature_exp_methods(self):
        """Test the temperatureExp getter and setter including None no-op."""
        physical_dimension = self._make()
        exp_value = ARNumerical()

        result = physical_dimension.setTemperatureExp(exp_value)
        assert physical_dimension.getTemperatureExp() == exp_value
        assert result == physical_dimension
        assert physical_dimension.setTemperatureExp(None) is physical_dimension
        assert physical_dimension.getTemperatureExp() == exp_value

    def test_physical_dimension_time_exp_methods(self):
        """Test the timeExp getter and setter including None no-op."""
        physical_dimension = self._make()
        exp_value = ARNumerical()

        result = physical_dimension.setTimeExp(exp_value)
        assert physical_dimension.getTimeExp() == exp_value
        assert result == physical_dimension
        assert physical_dimension.setTimeExp(None) is physical_dimension
        assert physical_dimension.getTimeExp() == exp_value


class TestSingleLanguageUnitNames:
    """Test class for SingleLanguageUnitNames class."""

    def test_single_language_unit_names_initialization(self):
        """Test that a SingleLanguageUnitNames object can be initialized."""
        single_lang_unit_names = SingleLanguageUnitNames()
        assert single_lang_unit_names is not None
        assert single_lang_unit_names.getValue() == ""

    def test_single_language_unit_names_value(self):
        """Test that a SingleLanguageUnitNames object can carry a value."""
        single_lang_unit_names = SingleLanguageUnitNames().setValue("m")
        assert single_lang_unit_names.getValue() == "m"


class TestUnit:
    """Test class for Unit class."""

    def _make(self) -> Unit:
        parent_obj = ARPackage(None, "parent_test")
        return Unit(parent_obj, "test_name")

    def test_unit_initialization(self):
        """Test that a Unit object can be initialized with default values."""
        unit = self._make()
        assert unit.getDisplayName() is None
        assert unit.getFactorSiToUnit() is None
        assert unit.getOffsetSiToUnit() is None
        assert unit.getPhysicalDimensionRef() is None

    def test_unit_display_name_methods(self):
        """Test the displayName getter and setter including None no-op."""
        unit = self._make()
        display_name = SingleLanguageUnitNames()

        result = unit.setDisplayName(display_name)
        assert unit.getDisplayName() == display_name
        assert result == unit
        assert unit.setDisplayName(None) is unit
        assert unit.getDisplayName() == display_name

    def test_unit_factor_si_to_unit_methods(self):
        """Test the factorSiToUnit getter and setter including None no-op."""
        unit = self._make()
        factor = Float()

        result = unit.setFactorSiToUnit(factor)
        assert unit.getFactorSiToUnit() == factor
        assert result == unit
        assert unit.setFactorSiToUnit(None) is unit
        assert unit.getFactorSiToUnit() == factor

    def test_unit_offset_si_to_unit_methods(self):
        """Test the offsetSiToUnit getter and setter including None no-op."""
        unit = self._make()
        offset = Float()

        result = unit.setOffsetSiToUnit(offset)
        assert unit.getOffsetSiToUnit() == offset
        assert result == unit
        assert unit.setOffsetSiToUnit(None) is unit
        assert unit.getOffsetSiToUnit() == offset

    def test_unit_physical_dimension_ref_methods(self):
        """Test the physicalDimensionRef getter and setter including None no-op."""
        unit = self._make()
        ref = RefType()

        result = unit.setPhysicalDimensionRef(ref)
        assert unit.getPhysicalDimensionRef() == ref
        assert result == unit
        assert unit.setPhysicalDimensionRef(None) is unit
        assert unit.getPhysicalDimensionRef() == ref
