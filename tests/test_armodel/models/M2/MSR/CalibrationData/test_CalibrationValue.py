"""
This module contains tests for the CalibrationValue module in MSR.CalibrationData.
"""
from armodel.models.M2.MSR.CalibrationData.CalibrationValue import *
from armodel.models.M2.MSR.AsamHdo.Units import SingleLanguageUnitNames
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARNumerical, RefType
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import ValueList


class TestSwValues:
    """Test class for SwValues class."""
    
    def test_sw_values_initialization(self):
        """Test that a SwValues object can be initialized with default values."""
        sw_values = SwValues()
        assert sw_values._v == []
        assert sw_values.vt is None
    
    def test_sw_values_v_methods(self):
        """Test adding and getting values."""
        sw_values = SwValues()
        value = ARNumerical()
        
        sw_values.addV(value)
        vs = sw_values.getVs()
        assert value in vs
        assert len(vs) == 1


class TestSwValueCont:
    """Test class for SwValueCont class."""
    
    def test_sw_value_cont_initialization(self):
        """Test that a SwValueCont object can be initialized with default values."""
        sw_value_cont = SwValueCont()
        assert sw_value_cont.swArraysize is None
        assert sw_value_cont.swValuesPhys is None
        assert sw_value_cont.unitRef is None
        assert sw_value_cont.unitDisplayName is None
    
    def test_sw_value_cont_array_size_methods(self):
        """Test the swArraysize getter and setter."""
        sw_value_cont = SwValueCont()
        array_size = ValueList()
        
        result = sw_value_cont.setSwArraysize(array_size)
        assert sw_value_cont.getSwArraysize() == array_size
        assert result == sw_value_cont
    
    def test_sw_value_cont_sw_values_phys_methods(self):
        """Test the swValuesPhys getter and setter."""
        sw_value_cont = SwValueCont()
        values_phys = SwValues()
        
        result = sw_value_cont.setSwValuesPhys(values_phys)
        assert sw_value_cont.getSwValuesPhys() == values_phys
        assert result == sw_value_cont
    
    def test_sw_value_cont_unit_ref_methods(self):
        """Test the unitRef getter and setter."""
        sw_value_cont = SwValueCont()
        unit_ref = RefType()
        
        result = sw_value_cont.setUnitRef(unit_ref)
        assert sw_value_cont.getUnitRef() == unit_ref
        assert result == sw_value_cont
    
    def test_sw_value_cont_unit_display_name_methods(self):
        """Test the unitDisplayName getter and setter."""
        sw_value_cont = SwValueCont()
        unit_display_name = SingleLanguageUnitNames()
        
        result = sw_value_cont.setUnitDisplayName(unit_display_name)
        assert sw_value_cont.getUnitDisplayName() == unit_display_name
        assert result == sw_value_cont