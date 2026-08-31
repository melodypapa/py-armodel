"""
This module contains tests for the DataDefProperties module in MSR.DataDictionary.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure import NumericalValueSpecification
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import ArraySizeSemanticsEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import MultidimensionalTime
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AlignmentType,
    ARNumerical,
    Boolean,
    DisplayFormatString,
    Float,
    Identifier,
    Integer,
    NativeDeclarationString,
    Numerical,
    PrimitiveIdentifier,
    RefType,
)
from armodel.models.M2.MSR.DataDictionary.CalibrationParameter import SwCalprmAxisSet
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import (
    CompuGenericMath,
    DisplayPresentationEnum,
    SwBitRepresentation,
    SwCalibrationAccessEnum,
    SwCalprmRefProxy,
    SwDataDefProps,
    SwDataDependency,
    SwDataDependencyArgs,
    SwImplPolicyEnum,
    SwPointerTargetProps,
    SwTextProps,
    SwVariableRefProxy,
    ValueList,
)
from armodel.models.M2.MSR.Documentation.Annotation import Annotation


class TestSwImplPolicyEnum:
    """Test class for SwImplPolicyEnum class."""

    def test_sw_impl_policy_enum_initialization(self):
        SwImplPolicyEnum()
        assert SwImplPolicyEnum.CONST == "const"
        assert SwImplPolicyEnum.FIXED == "fixed"
        assert SwImplPolicyEnum.MEASUREMENT_POINT == "measurementPoint"
        assert SwImplPolicyEnum.QUEUED == "queued"
        assert SwImplPolicyEnum.STANDARD == "standard"

    def test_sw_impl_policy_enum_values(self):
        assert hasattr(SwImplPolicyEnum, "CONST")
        assert hasattr(SwImplPolicyEnum, "FIXED")
        assert hasattr(SwImplPolicyEnum, "MEASUREMENT_POINT")
        assert hasattr(SwImplPolicyEnum, "QUEUED")
        assert hasattr(SwImplPolicyEnum, "STANDARD")
        assert SwImplPolicyEnum.CONST == "const"
        assert SwImplPolicyEnum.FIXED == "fixed"
        assert SwImplPolicyEnum.MEASUREMENT_POINT == "measurementPoint"
        assert SwImplPolicyEnum.QUEUED == "queued"
        assert SwImplPolicyEnum.STANDARD == "standard"


class TestSwCalibrationAccessEnum:
    """Test class for SwCalibrationAccessEnum class."""

    def test_sw_calibration_access_enum_initialization(self):
        SwCalibrationAccessEnum()
        assert SwCalibrationAccessEnum.NOT_ACCESSIBLE == "notAccessible"
        assert SwCalibrationAccessEnum.READ_ONLY == "readOnly"
        assert SwCalibrationAccessEnum.READ_WRITE == "readWrite"

    def test_sw_calibration_access_enum_values(self):
        assert hasattr(SwCalibrationAccessEnum, "NOT_ACCESSIBLE")
        assert hasattr(SwCalibrationAccessEnum, "READ_ONLY")
        assert hasattr(SwCalibrationAccessEnum, "READ_WRITE")
        assert SwCalibrationAccessEnum.NOT_ACCESSIBLE == "notAccessible"
        assert SwCalibrationAccessEnum.READ_ONLY == "readOnly"
        assert SwCalibrationAccessEnum.READ_WRITE == "readWrite"


class TestDisplayPresentationEnum:
    """Test class for DisplayPresentationEnum class."""

    def test_display_presentation_enum_initialization(self):
        DisplayPresentationEnum()
        assert DisplayPresentationEnum.PRESENTATION_CONTINUOUS == "presentationContinuous"
        assert DisplayPresentationEnum.PRESENTATION_DISCRETE == "presentationDiscrete"

    def test_display_presentation_enum_values(self):
        assert hasattr(DisplayPresentationEnum, "PRESENTATION_CONTINUOUS")
        assert hasattr(DisplayPresentationEnum, "PRESENTATION_DISCRETE")
        assert DisplayPresentationEnum.PRESENTATION_CONTINUOUS == "presentationContinuous"
        assert DisplayPresentationEnum.PRESENTATION_DISCRETE == "presentationDiscrete"


class TestSwBitRepresentation:
    """Test class for SwBitRepresentation class."""

    def test_sw_bit_representation_initialization(self):
        sw_bit_representation = SwBitRepresentation()
        assert sw_bit_representation.getBitPosition() is None
        assert sw_bit_representation.getNumberOfBits() is None

    def test_sw_bit_representation_methods(self):
        sw_bit_representation = SwBitRepresentation()
        bit_position = Integer().setValue("3")
        number_of_bits = Integer().setValue("5")

        assert sw_bit_representation.setBitPosition(bit_position) == sw_bit_representation
        assert sw_bit_representation.getBitPosition() == bit_position
        assert sw_bit_representation.setNumberOfBits(number_of_bits) == sw_bit_representation
        assert sw_bit_representation.getNumberOfBits() == number_of_bits

    def test_sw_bit_representation_none_noop(self):
        sw_bit_representation = SwBitRepresentation()
        sw_bit_representation.setBitPosition(Integer().setValue("3"))
        sw_bit_representation.setBitPosition(None)
        assert sw_bit_representation.getBitPosition().getValue() == 3


class TestSwDataDependencyArgs:
    """Test class for SwDataDependencyArgs class."""

    def test_sw_data_dependency_args_initialization(self):
        args = SwDataDependencyArgs()
        assert args.getSwCalprmRef() is None
        assert args.getSwVariable() is None

    def test_sw_data_dependency_args_methods(self):
        args = SwDataDependencyArgs()
        sw_calprm_ref = SwCalprmRefProxy()
        sw_variable = SwVariableRefProxy()

        assert args.setSwCalprmRef(sw_calprm_ref) == args
        assert args.getSwCalprmRef() == sw_calprm_ref
        assert args.setSwVariable(sw_variable) == args
        assert args.getSwVariable() == sw_variable

    def test_sw_data_dependency_args_none_noop(self):
        args = SwDataDependencyArgs()
        sw_calprm_ref = SwCalprmRefProxy()
        args.setSwCalprmRef(sw_calprm_ref)
        args.setSwCalprmRef(None)
        assert args.getSwCalprmRef() == sw_calprm_ref


class TestCompuGenericMath:
    """Test class for CompuGenericMath class."""

    def test_compu_generic_math_initialization(self):
        compu_generic_math = CompuGenericMath()
        assert compu_generic_math.getLevel() is None

    def test_compu_generic_math_methods(self):
        compu_generic_math = CompuGenericMath()
        level = PrimitiveIdentifier().setValue("INFORMAL")

        assert compu_generic_math.setLevel(level) == compu_generic_math
        assert compu_generic_math.getLevel() == level

    def test_compu_generic_math_none_noop(self):
        compu_generic_math = CompuGenericMath()
        level = PrimitiveIdentifier().setValue("INFORMAL")
        compu_generic_math.setLevel(level)
        compu_generic_math.setLevel(None)
        assert compu_generic_math.getLevel() == level


class TestSwDataDependency:
    """Test class for SwDataDependency class."""

    def test_sw_data_dependency_initialization(self):
        dependency = SwDataDependency()
        assert dependency.getSwDataDependencyFormula() is None
        assert dependency.getSwDataDependencyArgs() is None

    def test_sw_data_dependency_methods(self):
        dependency = SwDataDependency()
        formula = CompuGenericMath()
        args = SwDataDependencyArgs()

        assert dependency.setSwDataDependencyFormula(formula) == dependency
        assert dependency.getSwDataDependencyFormula() == formula
        assert dependency.setSwDataDependencyArgs(args) == dependency
        assert dependency.getSwDataDependencyArgs() == args

    def test_sw_data_dependency_none_noop(self):
        dependency = SwDataDependency()
        formula = CompuGenericMath()
        dependency.setSwDataDependencyFormula(formula)
        dependency.setSwDataDependencyFormula(None)
        assert dependency.getSwDataDependencyFormula() == formula


class TestSwDataDefProps:
    """Test class for SwDataDefProps class."""

    def test_sw_data_def_props_initialization(self):
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

    def test_sw_data_def_props_none_noop_chain(self):
        sw_data_def_props = SwDataDefProps()
        qualifier = NativeDeclarationString().setValue("const")
        sw_data_def_props.setAdditionalNativeTypeQualifier(qualifier)
        result = sw_data_def_props.setAdditionalNativeTypeQualifier(None)
        assert sw_data_def_props.getAdditionalNativeTypeQualifier() == qualifier
        assert result == sw_data_def_props

    def test_sw_data_def_props_additional_native_type_qualifier_methods(self):
        sw_data_def_props = SwDataDefProps()
        qualifier = NativeDeclarationString().setValue("const")
        result = sw_data_def_props.setAdditionalNativeTypeQualifier(qualifier)
        assert sw_data_def_props.getAdditionalNativeTypeQualifier() == qualifier
        assert result == sw_data_def_props

    def test_sw_data_def_props_annotations_methods(self):
        sw_data_def_props = SwDataDefProps()
        annotation = Annotation()
        result = sw_data_def_props.addAnnotation(annotation)
        annotations = sw_data_def_props.getAnnotations()
        assert annotation in annotations
        assert result == sw_data_def_props

    def test_sw_data_def_props_base_type_ref_methods(self):
        sw_data_def_props = SwDataDefProps()
        ref = RefType().setDest("AUTOSAR/BaseTypes/uint8")
        result = sw_data_def_props.setBaseTypeRef(ref)
        assert sw_data_def_props.getBaseTypeRef() == ref
        assert result == sw_data_def_props

    def test_sw_data_def_props_compu_method_ref_methods(self):
        sw_data_def_props = SwDataDefProps()
        ref = RefType().setDest("AUTOSAR/CompuMethods/cm")
        result = sw_data_def_props.setCompuMethodRef(ref)
        assert sw_data_def_props.getCompuMethodRef() == ref
        assert result == sw_data_def_props

    def test_sw_data_def_props_data_constr_ref_methods(self):
        sw_data_def_props = SwDataDefProps()
        ref = RefType().setDest("AUTOSAR/DataConstrs/dc")
        result = sw_data_def_props.setDataConstrRef(ref)
        assert sw_data_def_props.getDataConstrRef() == ref
        assert result == sw_data_def_props

    def test_sw_data_def_props_display_format_methods(self):
        sw_data_def_props = SwDataDefProps()
        format_str = DisplayFormatString().setValue("%5.2f")
        result = sw_data_def_props.setDisplayFormat(format_str)
        assert sw_data_def_props.getDisplayFormat() == format_str
        assert result == sw_data_def_props

    def test_sw_data_def_props_display_presentation_methods(self):
        sw_data_def_props = SwDataDefProps()
        presentation = DisplayPresentationEnum().setValue(DisplayPresentationEnum.PRESENTATION_CONTINUOUS)
        result = sw_data_def_props.setDisplayPresentation(presentation)
        assert sw_data_def_props.getDisplayPresentation() == presentation
        assert result == sw_data_def_props

    def test_sw_data_def_props_implementation_data_type_ref_methods(self):
        sw_data_def_props = SwDataDefProps()
        ref = RefType().setDest("AUTOSAR/ImplementationDataTypes/idt")
        result = sw_data_def_props.setImplementationDataTypeRef(ref)
        assert sw_data_def_props.getImplementationDataTypeRef() == ref
        assert result == sw_data_def_props

    def test_sw_data_def_props_invalid_value_methods(self):
        sw_data_def_props = SwDataDefProps()
        invalid_val = NumericalValueSpecification()
        result = sw_data_def_props.setInvalidValue(invalid_val)
        assert sw_data_def_props.getInvalidValue() == invalid_val
        assert result == sw_data_def_props

    def test_sw_data_def_props_step_size_methods(self):
        sw_data_def_props = SwDataDefProps()
        step_size = Float().setValue("0.5")
        result = sw_data_def_props.setStepSize(step_size)
        assert sw_data_def_props.getStepSize() == step_size
        assert result == sw_data_def_props

    def test_sw_data_def_props_sw_addr_method_ref_methods(self):
        sw_data_def_props = SwDataDefProps()
        ref = RefType().setDest("AUTOSAR/SwAddrMethods/ram")
        result = sw_data_def_props.setSwAddrMethodRef(ref)
        assert sw_data_def_props.getSwAddrMethodRef() == ref
        assert result == sw_data_def_props

    def test_sw_data_def_props_sw_alignment_methods(self):
        sw_data_def_props = SwDataDefProps()
        alignment = AlignmentType().setValue("4")
        result = sw_data_def_props.setSwAlignment(alignment)
        assert sw_data_def_props.getSwAlignment() == alignment
        assert result == sw_data_def_props

    def test_sw_data_def_props_sw_bit_representation_methods(self):
        sw_data_def_props = SwDataDefProps()
        bit_rep = SwBitRepresentation()
        result = sw_data_def_props.setSwBitRepresentation(bit_rep)
        assert sw_data_def_props.getSwBitRepresentation() == bit_rep
        assert result == sw_data_def_props

    def test_sw_data_def_props_sw_calibration_access_methods(self):
        sw_data_def_props = SwDataDefProps()
        cal_access = SwCalibrationAccessEnum().setValue(SwCalibrationAccessEnum.READ_WRITE)
        result = sw_data_def_props.setSwCalibrationAccess(cal_access)
        assert sw_data_def_props.getSwCalibrationAccess() == cal_access
        assert result == sw_data_def_props

    def test_sw_data_def_props_sw_calprm_axis_set_methods(self):
        sw_data_def_props = SwDataDefProps()
        calprm_axis_set = SwCalprmAxisSet()
        result = sw_data_def_props.setSwCalprmAxisSet(calprm_axis_set)
        assert sw_data_def_props.getSwCalprmAxisSet() == calprm_axis_set
        assert result == sw_data_def_props

    def test_sw_data_def_props_sw_comparison_variables_methods(self):
        sw_data_def_props = SwDataDefProps()
        comp_var = SwVariableRefProxy()
        result = sw_data_def_props.addSwComparisonVariable(comp_var)
        assert comp_var in sw_data_def_props.getSwComparisonVariables()
        assert result == sw_data_def_props

    def test_sw_data_def_props_sw_data_dependency_methods(self):
        sw_data_def_props = SwDataDefProps()
        data_dep = SwDataDependency()
        result = sw_data_def_props.setSwDataDependency(data_dep)
        assert sw_data_def_props.getSwDataDependency() == data_dep
        assert result == sw_data_def_props

    def test_sw_data_def_props_sw_host_variable_methods(self):
        sw_data_def_props = SwDataDefProps()
        host_var = SwVariableRefProxy()
        result = sw_data_def_props.setSwHostVariable(host_var)
        assert sw_data_def_props.getSwHostVariable() == host_var
        assert result == sw_data_def_props

    def test_sw_data_def_props_sw_impl_policy_methods(self):
        sw_data_def_props = SwDataDefProps()
        impl_policy = SwImplPolicyEnum().setValue(SwImplPolicyEnum.STANDARD)
        result = sw_data_def_props.setSwImplPolicy(impl_policy)
        assert sw_data_def_props.getSwImplPolicy() == impl_policy
        assert result == sw_data_def_props

    def test_sw_data_def_props_sw_intended_resolution_methods(self):
        sw_data_def_props = SwDataDefProps()
        resolution = ARNumerical().setValue("0.01")
        result = sw_data_def_props.setSwIntendedResolution(resolution)
        assert sw_data_def_props.getSwIntendedResolution() == resolution
        assert result == sw_data_def_props

    def test_sw_data_def_props_sw_interpolation_method_methods(self):
        sw_data_def_props = SwDataDefProps()
        interp_method = Identifier().setValue("linear")
        result = sw_data_def_props.setSwInterpolationMethod(interp_method)
        assert sw_data_def_props.getSwInterpolationMethod() == interp_method
        assert result == sw_data_def_props

    def test_sw_data_def_props_sw_is_virtual_methods(self):
        sw_data_def_props = SwDataDefProps()
        is_virtual = Boolean().setValue("true")
        result = sw_data_def_props.setSwIsVirtual(is_virtual)
        assert sw_data_def_props.getSwIsVirtual() == is_virtual
        assert result == sw_data_def_props

    def test_sw_data_def_props_sw_pointer_target_props_methods(self):
        sw_data_def_props = SwDataDefProps()
        ptr_target_props = SwPointerTargetProps()
        result = sw_data_def_props.setSwPointerTargetProps(ptr_target_props)
        assert sw_data_def_props.getSwPointerTargetProps() == ptr_target_props
        assert result == sw_data_def_props

    def test_sw_data_def_props_sw_record_layout_ref_methods(self):
        sw_data_def_props = SwDataDefProps()
        ref = RefType().setDest("AUTOSAR/RecordLayouts/rl")
        result = sw_data_def_props.setSwRecordLayoutRef(ref)
        assert sw_data_def_props.getSwRecordLayoutRef() == ref
        assert result == sw_data_def_props

    def test_sw_data_def_props_sw_refresh_timing_methods(self):
        sw_data_def_props = SwDataDefProps()
        refresh_timing = MultidimensionalTime()
        result = sw_data_def_props.setSwRefreshTiming(refresh_timing)
        assert sw_data_def_props.getSwRefreshTiming() == refresh_timing
        assert result == sw_data_def_props

    def test_sw_data_def_props_sw_text_props_methods(self):
        sw_data_def_props = SwDataDefProps()
        text_props = SwTextProps()
        result = sw_data_def_props.setSwTextProps(text_props)
        assert sw_data_def_props.getSwTextProps() == text_props
        assert result == sw_data_def_props

    def test_sw_data_def_props_sw_value_block_size_methods(self):
        sw_data_def_props = SwDataDefProps()
        block_size = ARNumerical().setValue("10")
        result = sw_data_def_props.setSwValueBlockSize(block_size)
        assert sw_data_def_props.getSwValueBlockSize() == block_size
        assert result == sw_data_def_props

    def test_sw_data_def_props_sw_value_block_size_mults_methods(self):
        sw_data_def_props = SwDataDefProps()
        mult = ARNumerical().setValue("2")
        result = sw_data_def_props.addSwValueBlockSizeMult(mult)
        assert mult in sw_data_def_props.getSwValueBlockSizeMults()
        assert result == sw_data_def_props

    def test_sw_data_def_props_unit_ref_methods(self):
        sw_data_def_props = SwDataDefProps()
        ref = RefType().setDest("AUTOSAR/Units/second")
        result = sw_data_def_props.setUnitRef(ref)
        assert sw_data_def_props.getUnitRef() == ref
        assert result == sw_data_def_props

    def test_sw_data_def_props_value_axis_data_type_ref_methods(self):
        sw_data_def_props = SwDataDefProps()
        ref = RefType().setDest("AUTOSAR/ApplicationDataTypes/adt")
        result = sw_data_def_props.setValueAxisDataTypeRef(ref)
        assert sw_data_def_props.getValueAxisDataTypeRef() == ref
        assert result == sw_data_def_props


class TestSwPointerTargetProps:
    """Test class for SwPointerTargetProps class."""

    def test_sw_pointer_target_props_initialization(self):
        sw_pointer_target_props = SwPointerTargetProps()
        assert sw_pointer_target_props.functionPointerSignatureRef is None
        assert sw_pointer_target_props.swDataDefProps is None
        assert sw_pointer_target_props.targetCategory is None

    def test_sw_pointer_target_props_function_pointer_signature_ref_methods(self):
        sw_pointer_target_props = SwPointerTargetProps()
        ref = RefType().setDest("AUTOSAR/FunctionPointerSignatures/fps")
        result = sw_pointer_target_props.setFunctionPointerSignatureRef(ref)
        assert sw_pointer_target_props.getFunctionPointerSignatureRef() == ref
        assert result == sw_pointer_target_props

    def test_sw_pointer_target_props_sw_data_def_props_methods(self):
        sw_pointer_target_props = SwPointerTargetProps()
        data_def_props = SwDataDefProps()
        result = sw_pointer_target_props.setSwDataDefProps(data_def_props)
        assert sw_pointer_target_props.getSwDataDefProps() == data_def_props
        assert result == sw_pointer_target_props

    def test_sw_pointer_target_props_target_category_methods(self):
        sw_pointer_target_props = SwPointerTargetProps()
        category = Identifier().setValue("function-pointer")
        result = sw_pointer_target_props.setTargetCategory(category)
        assert sw_pointer_target_props.getTargetCategory() == category
        assert result == sw_pointer_target_props


class TestValueList:
    """Test class for ValueList class."""

    def test_value_list_initialization(self):
        value_list = ValueList()
        assert value_list.v is None
        assert value_list._vf == []

    def test_value_list_v_methods(self):
        value_list = ValueList()
        value = Numerical().setValue("1.5")
        result = value_list.setV(value)
        assert value_list.getV() == value
        assert result == value_list

    def test_value_list_vf_methods(self):
        value_list = ValueList()
        vf = Numerical().setValue("1.5")
        value_list.addVf(vf)
        vfs = value_list.getVfs()
        assert vf in vfs
        assert len(vfs) == 1

    def test_value_list_vf_preserves_order(self):
        """vf is (ordered) per spec Table 5.127: insertion order must be preserved."""
        value_list = ValueList()
        first = Numerical().setValue("3.5")
        second = Numerical().setValue("1.5")
        third = Numerical().setValue("2.5")
        value_list.addVf(first)
        value_list.addVf(second)
        value_list.addVf(third)
        assert value_list.getVfs() == [first, second, third]

    def test_value_list_set_v_none_noop(self):
        value_list = ValueList()
        value = Numerical().setValue("1.5")
        value_list.setV(value)
        result = value_list.setV(None)
        assert result == value_list
        assert value_list.getV() == value

    def test_value_list_set_v_chaining(self):
        value_list = ValueList()
        assert value_list.setV(None) is value_list


class TestSwTextProps:
    """Test class for SwTextProps class."""

    def test_sw_text_props_initialization(self):
        sw_text_props = SwTextProps()
        assert sw_text_props.arraySizeSemantics is None
        assert sw_text_props.baseTypeRef is None
        assert sw_text_props.swFillCharacter is None
        assert sw_text_props.swMaxTextSize is None

    def test_sw_text_props_array_size_semantics_methods(self):
        sw_text_props = SwTextProps()
        semantics = ArraySizeSemanticsEnum().setValue(ArraySizeSemanticsEnum.FIXED_SIZE)
        result = sw_text_props.setArraySizeSemantics(semantics)
        assert sw_text_props.getArraySizeSemantics() == semantics
        assert result == sw_text_props
        sw_text_props.setArraySizeSemantics(None)
        assert sw_text_props.getArraySizeSemantics() == semantics

    def test_sw_text_props_base_type_ref_methods(self):
        sw_text_props = SwTextProps()
        ref = RefType().setDest("AUTOSAR/BaseTypes/uint8")
        result = sw_text_props.setBaseTypeRef(ref)
        assert sw_text_props.getBaseTypeRef() == ref
        assert result == sw_text_props
        sw_text_props.setBaseTypeRef(None)
        assert sw_text_props.getBaseTypeRef() == ref

    def test_sw_text_props_sw_fill_character_methods(self):
        sw_text_props = SwTextProps()
        fill_character = Integer().setValue("0")
        result = sw_text_props.setSwFillCharacter(fill_character)
        assert sw_text_props.getSwFillCharacter() == fill_character
        assert result == sw_text_props
        sw_text_props.setSwFillCharacter(None)
        assert sw_text_props.getSwFillCharacter() == fill_character

    def test_sw_text_props_sw_max_text_size_methods(self):
        sw_text_props = SwTextProps()
        max_text_size = Integer().setValue("200")
        result = sw_text_props.setSwMaxTextSize(max_text_size)
        assert sw_text_props.getSwMaxTextSize() == max_text_size
        assert result == sw_text_props
        sw_text_props.setSwMaxTextSize(None)
        assert sw_text_props.getSwMaxTextSize() == max_text_size
