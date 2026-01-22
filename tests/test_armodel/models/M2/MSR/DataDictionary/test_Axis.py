"""
This module contains tests for the Axis module in MSR.DataDictionary.
"""
from armodel.models.M2.MSR.DataDictionary.Axis import *
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARFloat, ARNumerical, RefType


class TestSwGenericAxisParam:
    """Test class for SwGenericAxisParam class."""
    
    def test_sw_generic_axis_param_initialization(self):
        """Test that a SwGenericAxisParam object can be initialized with default values."""
        sw_generic_axis_param = SwGenericAxisParam()
        assert sw_generic_axis_param.swGenericAxisParamTypeRef is None
        assert sw_generic_axis_param.vfs == []
    
    def test_sw_generic_axis_param_type_ref_methods(self):
        """Test the swGenericAxisParamTypeRef getter and setter."""
        sw_generic_axis_param = SwGenericAxisParam()
        ref = RefType()
        
        result = sw_generic_axis_param.setSwGenericAxisParamTypeRef(ref)
        assert sw_generic_axis_param.getSwGenericAxisParamTypeRef() == ref
        assert result == sw_generic_axis_param
    
    def test_sw_generic_axis_param_vfs_methods(self):
        """Test adding and getting float values."""
        sw_generic_axis_param = SwGenericAxisParam()
        value = ARFloat()
        
        result = sw_generic_axis_param.addVf(value)
        vfs = sw_generic_axis_param.getVfs()
        assert value in vfs
        assert result == sw_generic_axis_param


class TestSwAxisGeneric:
    """Test class for SwAxisGeneric class."""
    
    def test_sw_axis_generic_initialization(self):
        """Test that a SwAxisGeneric object can be initialized with default values."""
        sw_axis_generic = SwAxisGeneric()
        assert sw_axis_generic.swAxisTypeRef is None
        assert sw_axis_generic.swGenericAxisParams == []
    
    def test_sw_axis_type_ref_methods(self):
        """Test the swAxisTypeRef getter and setter."""
        sw_axis_generic = SwAxisGeneric()
        ref = RefType()
        
        result = sw_axis_generic.setSwAxisTypeRef(ref)
        assert sw_axis_generic.getSwAxisTypeRef() == ref
        assert result == sw_axis_generic
    
    def test_sw_axis_generic_params_methods(self):
        """Test adding and getting generic axis parameters."""
        sw_axis_generic = SwAxisGeneric()
        param = SwGenericAxisParam()
        
        result = sw_axis_generic.addSwGenericAxisParam(param)
        params = sw_axis_generic.getSwGenericAxisParams()
        assert param in params
        assert result == sw_axis_generic


class TestSwAxisIndividual:
    """Test class for SwAxisIndividual class."""
    
    def test_sw_axis_individual_initialization(self):
        """Test that a SwAxisIndividual object can be initialized with default values."""
        sw_axis_individual = SwAxisIndividual()
        assert sw_axis_individual.compuMethodRef is None
        assert sw_axis_individual.dataConstrRef is None
        assert sw_axis_individual.inputVariableTypeRef is None
        assert sw_axis_individual.swAxisGeneric is None
        assert sw_axis_individual.swMaxAxisPoints is None
        assert sw_axis_individual.swMinAxisPoints is None
        assert sw_axis_individual.swVariableRefs == []
        assert sw_axis_individual.unitRef is None
    
    def test_sw_axis_individual_compu_method_ref_methods(self):
        """Test the compuMethodRef getter and setter."""
        sw_axis_individual = SwAxisIndividual()
        ref = RefType()
        
        result = sw_axis_individual.setCompuMethodRef(ref)
        assert sw_axis_individual.getCompuMethodRef() == ref
        assert result == sw_axis_individual
    
    def test_sw_axis_individual_data_constr_ref_methods(self):
        """Test the dataConstrRef getter and setter."""
        sw_axis_individual = SwAxisIndividual()
        ref = RefType()
        
        result = sw_axis_individual.setDataConstrRef(ref)
        assert sw_axis_individual.getDataConstrRef() == ref
        assert result == sw_axis_individual
    
    def test_sw_axis_individual_input_variable_type_ref_methods(self):
        """Test the inputVariableTypeRef getter and setter."""
        sw_axis_individual = SwAxisIndividual()
        ref = RefType()
        
        result = sw_axis_individual.setInputVariableTypeRef(ref)
        assert sw_axis_individual.getInputVariableTypeRef() == ref
        assert result == sw_axis_individual
    
    def test_sw_axis_individual_sw_axis_generic_methods(self):
        """Test the swAxisGeneric getter and setter."""
        sw_axis_individual = SwAxisIndividual()
        sw_axis_gen = SwAxisGeneric()
        
        result = sw_axis_individual.setSwAxisGeneric(sw_axis_gen)
        assert sw_axis_individual.getSwAxisGeneric() == sw_axis_gen
        assert result == sw_axis_individual
    
    def test_sw_axis_individual_max_axis_points_methods(self):
        """Test the swMaxAxisPoints getter and setter."""
        sw_axis_individual = SwAxisIndividual()
        max_points = ARNumerical()
        
        result = sw_axis_individual.setSwMaxAxisPoints(max_points)
        assert sw_axis_individual.getSwMaxAxisPoints() == max_points
        assert result == sw_axis_individual
    
    def test_sw_axis_individual_min_axis_points_methods(self):
        """Test the swMinAxisPoints getter and setter."""
        sw_axis_individual = SwAxisIndividual()
        min_points = ARNumerical()
        
        result = sw_axis_individual.setSwMinAxisPoints(min_points)
        assert sw_axis_individual.getSwMinAxisPoints() == min_points
        assert result == sw_axis_individual
    
    def test_sw_axis_individual_variable_refs_methods(self):
        """Test the swVariableRefs getter and setter."""
        sw_axis_individual = SwAxisIndividual()
        refs = ["ref1", "ref2"]
        
        result = sw_axis_individual.setSwVariableRefs(refs)
        assert sw_axis_individual.getSwVariableRefs() == refs
        assert result == sw_axis_individual
    
    def test_sw_axis_individual_unit_ref_methods(self):
        """Test the unitRef getter and setter."""
        sw_axis_individual = SwAxisIndividual()
        ref = RefType()
        
        result = sw_axis_individual.setUnitRef(ref)
        assert sw_axis_individual.getUnitRef() == ref
        assert result == sw_axis_individual


class TestSwAxisGrouped:
    """Test class for SwAxisGrouped class."""
    
    def test_sw_axis_grouped_initialization(self):
        """Test that a SwAxisGrouped object can be initialized with default values."""
        sw_axis_grouped = SwAxisGrouped()
        assert sw_axis_grouped.sharedAxisTypeRef is None
        assert sw_axis_grouped.swAxisIndex is None
        assert sw_axis_grouped.swCalprmRef is None
    
    def test_sw_axis_grouped_shared_axis_type_ref_methods(self):
        """Test the sharedAxisTypeRef getter and setter."""
        sw_axis_grouped = SwAxisGrouped()
        ref = RefType()
        
        result = sw_axis_grouped.setSharedAxisTypeRef(ref)
        assert sw_axis_grouped.getSharedAxisTypeRef() == ref
        assert result == sw_axis_grouped
    
    def test_sw_axis_grouped_sw_axis_index_methods(self):
        """Test the swAxisIndex getter and setter."""
        sw_axis_grouped = SwAxisGrouped()
        index = ARNumerical()
        
        result = sw_axis_grouped.setSwAxisIndex(index)
        assert sw_axis_grouped.getSwAxisIndex() == index
        assert result == sw_axis_grouped
    
    def test_sw_axis_grouped_sw_calprm_ref_methods(self):
        """Test the swCalprmRef getter and setter."""
        sw_axis_grouped = SwAxisGrouped()
        # Note: SwCalprmRefProxy is not defined in the source, so using a placeholder
        ref = object()
        
        result = sw_axis_grouped.setSwCalprmRef(ref)
        assert sw_axis_grouped.getSwCalprmRef() == ref
        assert result == sw_axis_grouped