"""
This module contains tests for the DataDefProperties module in MSR.DataDictionary.
"""
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import *
from armodel.models.M2.MSR.Documentation.Annotation import Annotation
from armodel.models.M2.MSR.DataDictionary.CalibrationParameter import SwCalprmAxisSet
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARFloat, RefType, ARLiteral
from armodel.models.M2.AUTOSARTemplates.CommonStructure import NumericalValueSpecification


class TestSwImplPolicyEnum:
    """Test class for SwImplPolicyEnum class."""
    
    def test_sw_impl_policy_enum_initialization(self):
        """Test that SwImplPolicyEnum can be initialized with default values."""
        sw_impl_policy_enum = SwImplPolicyEnum()
        # Since SwImplPolicyEnum inherits from AREnum, check that it has the expected values
        assert SwImplPolicyEnum.CONST == "const"
        assert SwImplPolicyEnum.FIXED == "fixed"
        assert SwImplPolicyEnum.MEASUREMENT_POINT == "measurementPoint"
        assert SwImplPolicyEnum.QUEUED == "queued"
        assert SwImplPolicyEnum.STANDARD == "standard"
    
    def test_sw_impl_policy_enum_values(self):
        """Test that SwImplPolicyEnum has the expected values."""
        assert hasattr(SwImplPolicyEnum, 'CONST')
        assert hasattr(SwImplPolicyEnum, 'FIXED')
        assert hasattr(SwImplPolicyEnum, 'MEASUREMENT_POINT')
        assert hasattr(SwImplPolicyEnum, 'QUEUED')
        assert hasattr(SwImplPolicyEnum, 'STANDARD')
        assert SwImplPolicyEnum.CONST == "const"
        assert SwImplPolicyEnum.FIXED == "fixed"
        assert SwImplPolicyEnum.MEASUREMENT_POINT == "measurementPoint"
        assert SwImplPolicyEnum.QUEUED == "queued"
        assert SwImplPolicyEnum.STANDARD == "standard"


class TestSwDataDefPropsConditional:
    """Test class for SwDataDefPropsConditional class."""
    
    def test_sw_data_def_props_conditional_initialization(self):
        """Test that a SwDataDefPropsConditional object can be initialized."""
        sw_data_def_props_conditional = SwDataDefPropsConditional()
        assert sw_data_def_props_conditional is not None


class TestSwDataDefProps:
    """Test class for SwDataDefProps class."""
    
    def test_sw_data_def_props_initialization(self):
        """Test that a SwDataDefProps object can be initialized with default values."""
        sw_data_def_props = SwDataDefProps()
        assert sw_data_def_props.additionalNativeTypeQualifier is None
        assert sw_data_def_props.annotations == []
        assert sw_data_def_props.baseTypeRef is None
        assert sw_data_def_props.compuMethodRef is None
        assert sw_data_def_props.dataConstrRef is None
        assert sw_data_def_props.displayFormat is None
        assert sw_data_def_props.displayPresentation is None
        assert sw_data_def_props.implementationDataTypeRef is None
        assert sw_data_def_props.invalidValue is None
        assert sw_data_def_props.stepSize is None
        assert sw_data_def_props.swAddrMethodRef is None
        assert sw_data_def_props.swAlignment is None
        assert sw_data_def_props.swBitRepresentation is None
        assert sw_data_def_props.swCalibrationAccess is None
        assert sw_data_def_props.swCalprmAxisSet is None
        assert sw_data_def_props.swComparisonVariables == []
        assert sw_data_def_props.swDataDependency is None
        assert sw_data_def_props.swHostVariable is None
        assert sw_data_def_props.swImplPolicy is None
        assert sw_data_def_props.swIntendedResolution is None
        assert sw_data_def_props.swInterpolationMethod is None
        assert sw_data_def_props.swIsVirtual is None
        assert sw_data_def_props.swPointerTargetProps is None
        assert sw_data_def_props.swRecordLayoutRef is None
        assert sw_data_def_props.swRefreshTiming is None
        assert sw_data_def_props.swTextProps is None
        assert sw_data_def_props.swValueBlockSize is None
        assert sw_data_def_props.swValueBlockSizeMults == []
        assert sw_data_def_props.unitRef is None
        assert sw_data_def_props.valueAxisDataTypeRef is None
        assert sw_data_def_props.conditional is not None
    
    def test_sw_data_def_props_additional_native_type_qualifier_methods(self):
        """Test the additionalNativeTypeQualifier getter and setter."""
        sw_data_def_props = SwDataDefProps()
        qualifier = "const"
        
        result = sw_data_def_props.setAdditionalNativeTypeQualifier(qualifier)
        assert sw_data_def_props.getAdditionalNativeTypeQualifier() == qualifier
        assert result == sw_data_def_props
    
    def test_sw_data_def_props_annotations_methods(self):
        """Test adding annotations."""
        sw_data_def_props = SwDataDefProps()
        annotation = Annotation()
        
        result = sw_data_def_props.addAnnotation(annotation)
        annotations = sw_data_def_props.getAnnotations()
        assert annotation in annotations
        assert result == sw_data_def_props
    
    def test_sw_data_def_props_base_type_ref_methods(self):
        """Test the baseTypeRef getter and setter."""
        sw_data_def_props = SwDataDefProps()
        ref = RefType()
        
        result = sw_data_def_props.setBaseTypeRef(ref)
        assert sw_data_def_props.getBaseTypeRef() == ref
        assert result == sw_data_def_props
    
    def test_sw_data_def_props_compu_method_ref_methods(self):
        """Test the compuMethodRef getter and setter."""
        sw_data_def_props = SwDataDefProps()
        ref = RefType()
        
        result = sw_data_def_props.setCompuMethodRef(ref)
        assert sw_data_def_props.getCompuMethodRef() == ref
        assert result == sw_data_def_props
    
    def test_sw_data_def_props_data_constr_ref_methods(self):
        """Test the dataConstrRef getter and setter."""
        sw_data_def_props = SwDataDefProps()
        ref = RefType()
        
        result = sw_data_def_props.setDataConstrRef(ref)
        assert sw_data_def_props.getDataConstrRef() == ref
        assert result == sw_data_def_props
    
    def test_sw_data_def_props_display_format_methods(self):
        """Test the displayFormat getter and setter."""
        sw_data_def_props = SwDataDefProps()
        format_str = ARLiteral()
        
        result = sw_data_def_props.setDisplayFormat(format_str)
        assert sw_data_def_props.getDisplayFormat() == format_str
        assert result == sw_data_def_props
    
    def test_sw_data_def_props_display_presentation_methods(self):
        """Test the displayPresentation getter and setter."""
        sw_data_def_props = SwDataDefProps()
        presentation = ARLiteral()
        
        result = sw_data_def_props.setDisplayPresentation(presentation)
        assert sw_data_def_props.getDisplayPresentation() == presentation
        assert result == sw_data_def_props
    
    def test_sw_data_def_props_implementation_data_type_ref_methods(self):
        """Test the implementationDataTypeRef getter and setter."""
        sw_data_def_props = SwDataDefProps()
        ref = RefType()
        
        result = sw_data_def_props.setImplementationDataTypeRef(ref)
        assert sw_data_def_props.getImplementationDataTypeRef() == ref
        assert result == sw_data_def_props
    
    def test_sw_data_def_props_invalid_value_methods(self):
        """Test the invalidValue getter and setter."""
        sw_data_def_props = SwDataDefProps()
        # Using a concrete implementation of ValueSpecification instead of abstract class
        invalid_val = NumericalValueSpecification()
        
        result = sw_data_def_props.setInvalidValue(invalid_val)
        assert sw_data_def_props.getInvalidValue() == invalid_val
        assert result == sw_data_def_props
    
    def test_sw_data_def_props_step_size_methods(self):
        """Test the stepSize getter and setter."""
        sw_data_def_props = SwDataDefProps()
        step_size = ARFloat()
        
        result = sw_data_def_props.setStepSize(step_size)
        assert sw_data_def_props.getStepSize() == step_size
        assert result == sw_data_def_props
    
    def test_sw_data_def_props_sw_addr_method_ref_methods(self):
        """Test the swAddrMethodRef getter and setter."""
        sw_data_def_props = SwDataDefProps()
        ref = RefType()
        
        result = sw_data_def_props.setSwAddrMethodRef(ref)
        assert sw_data_def_props.getSwAddrMethodRef() == ref
        assert result == sw_data_def_props
    
    def test_sw_data_def_props_sw_alignment_methods(self):
        """Test the swAlignment getter and setter."""
        sw_data_def_props = SwDataDefProps()
        alignment = ARLiteral()
        
        result = sw_data_def_props.setSwAlignment(alignment)
        assert sw_data_def_props.getSwAlignment() == alignment
        assert result == sw_data_def_props
    
    def test_sw_data_def_props_sw_bit_representation_methods(self):
        """Test the swBitRepresentation getter and setter."""
        sw_data_def_props = SwDataDefProps()
        bit_rep = ARLiteral()
        
        result = sw_data_def_props.setSwBitRepresentation(bit_rep)
        assert sw_data_def_props.getSwBitRepresentation() == bit_rep
        assert result == sw_data_def_props
    
    def test_sw_data_def_props_sw_calibration_access_methods(self):
        """Test the swCalibrationAccess getter and setter."""
        sw_data_def_props = SwDataDefProps()
        cal_access = ARLiteral()
        
        result = sw_data_def_props.setSwCalibrationAccess(cal_access)
        assert sw_data_def_props.getSwCalibrationAccess() == cal_access
        assert result == sw_data_def_props
    
    def test_sw_data_def_props_sw_calprm_axis_set_methods(self):
        """Test the swCalprmAxisSet getter and setter."""
        sw_data_def_props = SwDataDefProps()
        calprm_axis_set = SwCalprmAxisSet()
        
        result = sw_data_def_props.setSwCalprmAxisSet(calprm_axis_set)
        assert sw_data_def_props.getSwCalprmAxisSet() == calprm_axis_set
        assert result == sw_data_def_props
    
    def test_sw_data_def_props_sw_comparison_variables_methods(self):
        """Test the swComparisonVariables getter and setter."""
        sw_data_def_props = SwDataDefProps()
        comp_vars = ["var1", "var2"]
        
        result = sw_data_def_props.setSwComparisonVariables(comp_vars)
        assert sw_data_def_props.getSwComparisonVariables() == comp_vars
        assert result == sw_data_def_props
    
    def test_sw_data_def_props_sw_data_dependency_methods(self):
        """Test the swDataDependency getter and setter."""
        sw_data_def_props = SwDataDefProps()
        data_dep = "dependency"
        
        result = sw_data_def_props.setSwDataDependency(data_dep)
        assert sw_data_def_props.getSwDataDependency() == data_dep
        assert result == sw_data_def_props
    
    def test_sw_data_def_props_sw_host_variable_methods(self):
        """Test the swHostVariable getter and setter."""
        sw_data_def_props = SwDataDefProps()
        host_var = "host"
        
        result = sw_data_def_props.setSwHostVariable(host_var)
        assert sw_data_def_props.getSwHostVariable() == host_var
        assert result == sw_data_def_props
    
    def test_sw_data_def_props_sw_impl_policy_methods(self):
        """Test the swImplPolicy getter and setter."""
        sw_data_def_props = SwDataDefProps()
        impl_policy = ARLiteral()
        
        result = sw_data_def_props.setSwImplPolicy(impl_policy)
        assert sw_data_def_props.getSwImplPolicy() == impl_policy
        assert result == sw_data_def_props
    
    def test_sw_data_def_props_sw_intended_resolution_methods(self):
        """Test the swIntendedResolution getter and setter."""
        sw_data_def_props = SwDataDefProps()
        resolution = "resolution"
        
        result = sw_data_def_props.setSwIntendedResolution(resolution)
        assert sw_data_def_props.getSwIntendedResolution() == resolution
        assert result == sw_data_def_props
    
    def test_sw_data_def_props_sw_interpolation_method_methods(self):
        """Test the swInterpolationMethod getter and setter."""
        sw_data_def_props = SwDataDefProps()
        interp_method = "linear"
        
        result = sw_data_def_props.setSwInterpolationMethod(interp_method)
        assert sw_data_def_props.getSwInterpolationMethod() == interp_method
        assert result == sw_data_def_props
    
    def test_sw_data_def_props_sw_is_virtual_methods(self):
        """Test the swIsVirtual getter and setter."""
        sw_data_def_props = SwDataDefProps()
        is_virtual = True
        
        result = sw_data_def_props.setSwIsVirtual(is_virtual)
        assert sw_data_def_props.getSwIsVirtual() == is_virtual
        assert result == sw_data_def_props
    
    def test_sw_data_def_props_sw_pointer_target_props_methods(self):
        """Test the swPointerTargetProps getter and setter."""
        sw_data_def_props = SwDataDefProps()
        ptr_target_props = SwPointerTargetProps()
        
        result = sw_data_def_props.setSwPointerTargetProps(ptr_target_props)
        assert sw_data_def_props.getSwPointerTargetProps() == ptr_target_props
        assert result == sw_data_def_props
    
    def test_sw_data_def_props_sw_record_layout_ref_methods(self):
        """Test the swRecordLayoutRef getter and setter."""
        sw_data_def_props = SwDataDefProps()
        ref = RefType()
        
        result = sw_data_def_props.setSwRecordLayoutRef(ref)
        assert sw_data_def_props.getSwRecordLayoutRef() == ref
        assert result == sw_data_def_props
    
    def test_sw_data_def_props_sw_refresh_timing_methods(self):
        """Test the swRefreshTiming getter and setter."""
        sw_data_def_props = SwDataDefProps()
        refresh_timing = "timing"
        
        result = sw_data_def_props.setSwRefreshTiming(refresh_timing)
        assert sw_data_def_props.getSwRefreshTiming() == refresh_timing
        assert result == sw_data_def_props
    
    def test_sw_data_def_props_sw_text_props_methods(self):
        """Test the swTextProps getter and setter."""
        sw_data_def_props = SwDataDefProps()
        text_props = "text_props"
        
        result = sw_data_def_props.setSwTextProps(text_props)
        assert sw_data_def_props.getSwTextProps() == text_props
        assert result == sw_data_def_props
    
    def test_sw_data_def_props_sw_value_block_size_methods(self):
        """Test the swValueBlockSize getter and setter."""
        sw_data_def_props = SwDataDefProps()
        block_size = "size"
        
        result = sw_data_def_props.setSwValueBlockSize(block_size)
        assert sw_data_def_props.getSwValueBlockSize() == block_size
        assert result == sw_data_def_props
    
    def test_sw_data_def_props_sw_value_block_size_mults_methods(self):
        """Test the swValueBlockSizeMults getter and setter."""
        sw_data_def_props = SwDataDefProps()
        mults = ["mult1", "mult2"]
        
        result = sw_data_def_props.setSwValueBlockSizeMults(mults)
        assert sw_data_def_props.getSwValueBlockSizeMults() == mults
        assert result == sw_data_def_props
    
    def test_sw_data_def_props_unit_ref_methods(self):
        """Test the unitRef getter and setter."""
        sw_data_def_props = SwDataDefProps()
        ref = RefType()
        
        result = sw_data_def_props.setUnitRef(ref)
        assert sw_data_def_props.getUnitRef() == ref
        assert result == sw_data_def_props
    
    def test_sw_data_def_props_value_axis_data_type_ref_methods(self):
        """Test the valueAxisDataTypeRef getter and setter."""
        sw_data_def_props = SwDataDefProps()
        ref = RefType()
        
        result = sw_data_def_props.setValueAxisDataTypeRef(ref)
        assert sw_data_def_props.getValueAxisDataTypeRef() == ref
        assert result == sw_data_def_props


class TestSwPointerTargetProps:
    """Test class for SwPointerTargetProps class."""
    
    def test_sw_pointer_target_props_initialization(self):
        """Test that a SwPointerTargetProps object can be initialized with default values."""
        sw_pointer_target_props = SwPointerTargetProps()
        assert sw_pointer_target_props.functionPointerSignatureRef is None
        assert sw_pointer_target_props.swDataDefProps is None
        assert sw_pointer_target_props.targetCategory is None
    
    def test_sw_pointer_target_props_function_pointer_signature_ref_methods(self):
        """Test the functionPointerSignatureRef getter and setter."""
        sw_pointer_target_props = SwPointerTargetProps()
        ref = RefType()
        
        result = sw_pointer_target_props.setFunctionPointerSignatureRef(ref)
        assert sw_pointer_target_props.getFunctionPointerSignatureRef() == ref
        assert result == sw_pointer_target_props
    
    def test_sw_pointer_target_props_sw_data_def_props_methods(self):
        """Test the swDataDefProps getter and setter."""
        sw_pointer_target_props = SwPointerTargetProps()
        data_def_props = SwDataDefProps()
        
        result = sw_pointer_target_props.setSwDataDefProps(data_def_props)
        assert sw_pointer_target_props.getSwDataDefProps() == data_def_props
        assert result == sw_pointer_target_props
    
    def test_sw_pointer_target_props_target_category_methods(self):
        """Test the targetCategory getter and setter."""
        sw_pointer_target_props = SwPointerTargetProps()
        category = ARLiteral()
        
        result = sw_pointer_target_props.setTargetCategory(category)
        assert sw_pointer_target_props.getTargetCategory() == category
        assert result == sw_pointer_target_props


class TestValueList:
    """Test class for ValueList class."""
    
    def test_value_list_initialization(self):
        """Test that a ValueList object can be initialized with default values."""
        value_list = ValueList()
        assert value_list.v is None
        assert value_list._vf == []
    
    def test_value_list_v_methods(self):
        """Test the v getter and setter."""
        value_list = ValueList()
        value = ARFloat()
        
        result = value_list.setV(value)
        assert value_list.getV() == value
        assert result == value_list
    
    def test_value_list_vf_methods(self):
        """Test adding and getting vf values."""
        value_list = ValueList()
        vf = ARLiteral()
        
        value_list.addVf(vf)
        vfs = value_list.getVfs()
        assert vf in vfs
        assert len(vfs) == 1