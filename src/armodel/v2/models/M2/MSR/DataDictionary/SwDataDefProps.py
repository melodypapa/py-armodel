from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class SwDataDefProps(ARObject):
    """
    that not all of the attributes or associated elements are useful all of the
    time. Hence, the process definition (e.g. expressed with an OCL or a
    Document Control Instance MSR-DCI) has the task of implementing limitations.
    SwDataDefProps covers various aspects: • Structure of the data element for
    calibration use cases: is it a single value, a curve, or a map, but also the
    recordLayouts which specify how such elements are mapped/converted to the
    DataTypes in the programming language (or in AUTOSAR). This is mainly
    expressed by properties like swRecordLayout and swCalprmAxisSet •
    Implementation aspects, mainly expressed by swImplPolicy,
    swVariableAccessImplPolicy, swAddr Method, swPointerTagetProps, baseType,
    implementationDataType and additionalNativeTypeQualifier • Access policy for
    the MCD system, mainly expressed by swCalibrationAccess • Semantics of the
    data element, mainly expressed by compuMethod and/or unit, dataConstr,
    invalid Value • Code generation policy provided by swRecordLayout Tags:
    vh.latestBindingTime=codeGenerationTime
    
    Package: M2::MSR::DataDictionary::DataDefProperties::SwDataDefProps
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 339, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 46, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 307, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 329, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2062, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 31, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 467, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (Page 34, Foundation R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 211, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute is used to declare native qualifiers of the language which can
                # neither be deduced baseType (e.
        # g.
        # because the data object pointer) nor from other more abstract are qualifiers
                # like "volatile", "strict" or the C-language.
        # All such declarations have to into one string.
        self._additionalNative: Optional["NativeDeclarationString"] = None

    @property
    def additional_native(self) -> Optional["NativeDeclarationString"]:
        """Get additionalNative (Pythonic accessor)."""
        return self._additionalNative

    @additional_native.setter
    def additional_native(self, value: Optional["NativeDeclarationString"]) -> None:
        """
        Set additionalNative with validation.
        
        Args:
            value: The additionalNative to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._additionalNative = None
            return

        if not isinstance(value, NativeDeclarationString):
            raise TypeError(
                f"additionalNative must be NativeDeclarationString or None, got {type(value).__name__}"
            )
        self._additionalNative = value
        # This aggregation allows to add annotations (yellow pads to the current data
        # object.
        self._annotation: List["Annotation"] = []

    @property
    def annotation(self) -> List["Annotation"]:
        """Get annotation (Pythonic accessor)."""
        return self._annotation
        # Base type associated with the containing data object.
        self._baseType: Optional["SwBaseType"] = None

    @property
    def base_type(self) -> Optional["SwBaseType"]:
        """Get baseType (Pythonic accessor)."""
        return self._baseType

    @base_type.setter
    def base_type(self, value: Optional["SwBaseType"]) -> None:
        """
        Set baseType with validation.
        
        Args:
            value: The baseType to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._baseType = None
            return

        if not isinstance(value, SwBaseType):
            raise TypeError(
                f"baseType must be SwBaseType or None, got {type(value).__name__}"
            )
        self._baseType = value
        # Computation method associated with the semantics of object.
        self._compuMethod: Optional["CompuMethod"] = None

    @property
    def compu_method(self) -> Optional["CompuMethod"]:
        """Get compuMethod (Pythonic accessor)."""
        return self._compuMethod

    @compu_method.setter
    def compu_method(self, value: Optional["CompuMethod"]) -> None:
        """
        Set compuMethod with validation.
        
        Args:
            value: The compuMethod to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._compuMethod = None
            return

        if not isinstance(value, CompuMethod):
            raise TypeError(
                f"compuMethod must be CompuMethod or None, got {type(value).__name__}"
            )
        self._compuMethod = value
        # Data constraint for this data object.
        # 381 Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module
                # Description Template R23-11.
        self._dataConstr: Optional["DataConstr"] = None

    @property
    def data_constr(self) -> Optional["DataConstr"]:
        """Get dataConstr (Pythonic accessor)."""
        return self._dataConstr

    @data_constr.setter
    def data_constr(self, value: Optional["DataConstr"]) -> None:
        """
        Set dataConstr with validation.
        
        Args:
            value: The dataConstr to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataConstr = None
            return

        if not isinstance(value, DataConstr):
            raise TypeError(
                f"dataConstr must be DataConstr or None, got {type(value).__name__}"
            )
        self._dataConstr = value
        # This property describes how a number is to be rendered documents or in a
        # measurement and calibration.
        self._displayFormat: Optional["DisplayFormatString"] = None

    @property
    def display_format(self) -> Optional["DisplayFormatString"]:
        """Get displayFormat (Pythonic accessor)."""
        return self._displayFormat

    @display_format.setter
    def display_format(self, value: Optional["DisplayFormatString"]) -> None:
        """
        Set displayFormat with validation.
        
        Args:
            value: The displayFormat to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._displayFormat = None
            return

        if not isinstance(value, DisplayFormatString):
            raise TypeError(
                f"displayFormat must be DisplayFormatString or None, got {type(value).__name__}"
            )
        self._displayFormat = value
        # This attribute controls the presentation of the related data for measurement
        # and calibration tools.
        self._display: Optional["DisplayPresentation"] = None

    @property
    def display(self) -> Optional["DisplayPresentation"]:
        """Get display (Pythonic accessor)."""
        return self._display

    @display.setter
    def display(self, value: Optional["DisplayPresentation"]) -> None:
        """
        Set display with validation.
        
        Args:
            value: The display to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._display = None
            return

        if not isinstance(value, DisplayPresentation):
            raise TypeError(
                f"display must be DisplayPresentation or None, got {type(value).__name__}"
            )
        self._display = value
        # This association denotes the ImplementationDataType of a data declaration via
                # its aggregated SwDataDefProps.
        # It whenever a data declaration is not directly a base type.
        # Especially of an ImplementationDataType via a another ImplementationDatatype
                # target type of a pointer (see SwPointerTarget it does not refer to a base
                # type directly data type of an array or record element within an it does not
                # refer to a base data type of an SwServiceArg, if it does not refer to type
                # directly.
        self._implementation: Optional["AbstractImplementation"] = None

    @property
    def implementation(self) -> Optional["AbstractImplementation"]:
        """Get implementation (Pythonic accessor)."""
        return self._implementation

    @implementation.setter
    def implementation(self, value: Optional["AbstractImplementation"]) -> None:
        """
        Set implementation with validation.
        
        Args:
            value: The implementation to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._implementation = None
            return

        if not isinstance(value, AbstractImplementation):
            raise TypeError(
                f"implementation must be AbstractImplementation or None, got {type(value).__name__}"
            )
        self._implementation = value
        # Optional value to express invalidity of the actual data.
        self._invalidValue: Optional["ValueSpecification"] = None

    @property
    def invalid_value(self) -> Optional["ValueSpecification"]:
        """Get invalidValue (Pythonic accessor)."""
        return self._invalidValue

    @invalid_value.setter
    def invalid_value(self, value: Optional["ValueSpecification"]) -> None:
        """
        Set invalidValue with validation.
        
        Args:
            value: The invalidValue to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._invalidValue = None
            return

        if not isinstance(value, ValueSpecification):
            raise TypeError(
                f"invalidValue must be ValueSpecification or None, got {type(value).__name__}"
            )
        self._invalidValue = value
        # This attribute can be used to define a value which is or subtracted from the
        # value of a DataPrototype up/down keys while calibrating.
        self._stepSize: Optional["Float"] = None

    @property
    def step_size(self) -> Optional["Float"]:
        """Get stepSize (Pythonic accessor)."""
        return self._stepSize

    @step_size.setter
    def step_size(self, value: Optional["Float"]) -> None:
        """
        Set stepSize with validation.
        
        Args:
            value: The stepSize to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._stepSize = None
            return

        if not isinstance(value, Float):
            raise TypeError(
                f"stepSize must be Float or None, got {type(value).__name__}"
            )
        self._stepSize = value
        # Addressing method related to this data object.
        # Via an the same SwAddrMethod it can be several DataPrototypes shall be
                # located in memory without already specifying the memory.
        self._swAddrMethod: Optional["SwAddrMethod"] = None

    @property
    def sw_addr_method(self) -> Optional["SwAddrMethod"]:
        """Get swAddrMethod (Pythonic accessor)."""
        return self._swAddrMethod

    @sw_addr_method.setter
    def sw_addr_method(self, value: Optional["SwAddrMethod"]) -> None:
        """
        Set swAddrMethod with validation.
        
        Args:
            value: The swAddrMethod to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swAddrMethod = None
            return

        if not isinstance(value, SwAddrMethod):
            raise TypeError(
                f"swAddrMethod must be SwAddrMethod or None, got {type(value).__name__}"
            )
        self._swAddrMethod = value
        # The attribute describes the intended typical alignment of If the attribute is
        # not defined the determined by the swBaseType size and the the referenced Sw.
        self._swAlignment: Optional["AlignmentType"] = None

    @property
    def sw_alignment(self) -> Optional["AlignmentType"]:
        """Get swAlignment (Pythonic accessor)."""
        return self._swAlignment

    @sw_alignment.setter
    def sw_alignment(self, value: Optional["AlignmentType"]) -> None:
        """
        Set swAlignment with validation.
        
        Args:
            value: The swAlignment to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swAlignment = None
            return

        if not isinstance(value, AlignmentType):
            raise TypeError(
                f"swAlignment must be AlignmentType or None, got {type(value).__name__}"
            )
        self._swAlignment = value
        # Description of the binary representation in case of a bit.
        self._swBit: Optional["SwBitRepresentation"] = None

    @property
    def sw_bit(self) -> Optional["SwBitRepresentation"]:
        """Get swBit (Pythonic accessor)."""
        return self._swBit

    @sw_bit.setter
    def sw_bit(self, value: Optional["SwBitRepresentation"]) -> None:
        """
        Set swBit with validation.
        
        Args:
            value: The swBit to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swBit = None
            return

        if not isinstance(value, SwBitRepresentation):
            raise TypeError(
                f"swBit must be SwBitRepresentation or None, got {type(value).__name__}"
            )
        self._swBit = value
        # Specifies the read or write access by MCD tools for this data object.
        self._swCalibration: Optional["SwCalibrationAccess"] = None

    @property
    def sw_calibration(self) -> Optional["SwCalibrationAccess"]:
        """Get swCalibration (Pythonic accessor)."""
        return self._swCalibration

    @sw_calibration.setter
    def sw_calibration(self, value: Optional["SwCalibrationAccess"]) -> None:
        """
        Set swCalibration with validation.
        
        Args:
            value: The swCalibration to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swCalibration = None
            return

        if not isinstance(value, SwCalibrationAccess):
            raise TypeError(
                f"swCalibration must be SwCalibrationAccess or None, got {type(value).__name__}"
            )
        self._swCalibration = value
        # This specifies the properties of the axes in case of a or map etc.
        # This is mainly applicable to calibration.
        self._swCalprmAxis: RefType = None

    @property
    def sw_calprm_axis(self) -> RefType:
        """Get swCalprmAxis (Pythonic accessor)."""
        return self._swCalprmAxis

    @sw_calprm_axis.setter
    def sw_calprm_axis(self, value: RefType) -> None:
        """
        Set swCalprmAxis with validation.
        
        Args:
            value: The swCalprmAxis to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swCalprmAxis = None
            return

        self._swCalprmAxis = value
        # Variables used for comparison in an MCD process.
        # 381 Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module
                # Description Template R23-11.
        self._swComparison: List[RefType] = []

    @property
    def sw_comparison(self) -> List[RefType]:
        """Get swComparison (Pythonic accessor)."""
        return self._swComparison
        # Describes how the value of the data object has to be from the value of
        # another data object (by the.
        self._swData: RefType = None

    @property
    def sw_data(self) -> RefType:
        """Get swData (Pythonic accessor)."""
        return self._swData

    @sw_data.setter
    def sw_data(self, value: RefType) -> None:
        """
        Set swData with validation.
        
        Args:
            value: The swData to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swData = None
            return

        self._swData = value
        # Contains a reference to a variable which serves as a a bit variable.
        # Only applicable to bit.
        self._swHostVariable: RefType = None

    @property
    def sw_host_variable(self) -> RefType:
        """Get swHostVariable (Pythonic accessor)."""
        return self._swHostVariable

    @sw_host_variable.setter
    def sw_host_variable(self, value: RefType) -> None:
        """
        Set swHostVariable with validation.
        
        Args:
            value: The swHostVariable to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swHostVariable = None
            return

        self._swHostVariable = value
        # Implementation policy for this data object.
        self._swImplPolicy: Optional["SwImplPolicyEnum"] = None

    @property
    def sw_impl_policy(self) -> Optional["SwImplPolicyEnum"]:
        """Get swImplPolicy (Pythonic accessor)."""
        return self._swImplPolicy

    @sw_impl_policy.setter
    def sw_impl_policy(self, value: Optional["SwImplPolicyEnum"]) -> None:
        """
        Set swImplPolicy with validation.
        
        Args:
            value: The swImplPolicy to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swImplPolicy = None
            return

        if not isinstance(value, SwImplPolicyEnum):
            raise TypeError(
                f"swImplPolicy must be SwImplPolicyEnum or None, got {type(value).__name__}"
            )
        self._swImplPolicy = value
        # The purpose of this element is to describe the requested of data objects
                # early on in the design ultimately occurs via the conversion (compuMethod),
                # which specifies the the physical world to the standardized vice-versa) (here,
                # "the slope per bit" is present the conversion formula).
        # case of a development phase without a fixed a pre-specification can occur
                # through is specified in the physical domain the property "unit".
        self._swIntended: Optional["Numerical"] = None

    @property
    def sw_intended(self) -> Optional["Numerical"]:
        """Get swIntended (Pythonic accessor)."""
        return self._swIntended

    @sw_intended.setter
    def sw_intended(self, value: Optional["Numerical"]) -> None:
        """
        Set swIntended with validation.
        
        Args:
            value: The swIntended to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swIntended = None
            return

        if not isinstance(value, Numerical):
            raise TypeError(
                f"swIntended must be Numerical or None, got {type(value).__name__}"
            )
        self._swIntended = value
        # This is a keyword identifying the mathematical method to applied for
                # interpolation.
        # The keyword needs to be the interpolation routine which needs to be.
        self._swInterpolation: Optional["Identifier"] = None

    @property
    def sw_interpolation(self) -> Optional["Identifier"]:
        """Get swInterpolation (Pythonic accessor)."""
        return self._swInterpolation

    @sw_interpolation.setter
    def sw_interpolation(self, value: Optional["Identifier"]) -> None:
        """
        Set swInterpolation with validation.
        
        Args:
            value: The swInterpolation to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swInterpolation = None
            return

        if not isinstance(value, Identifier):
            raise TypeError(
                f"swInterpolation must be Identifier or None, got {type(value).__name__}"
            )
        self._swInterpolation = value
        # This element distinguishes virtual objects.
        # Virtual objects appear in the memory, their derivation is much on other
                # objects and hence they shall swDataDependency.
        self._swIsVirtual: Optional["Boolean"] = None

    @property
    def sw_is_virtual(self) -> Optional["Boolean"]:
        """Get swIsVirtual (Pythonic accessor)."""
        return self._swIsVirtual

    @sw_is_virtual.setter
    def sw_is_virtual(self, value: Optional["Boolean"]) -> None:
        """
        Set swIsVirtual with validation.
        
        Args:
            value: The swIsVirtual to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swIsVirtual = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"swIsVirtual must be Boolean or None, got {type(value).__name__}"
            )
        self._swIsVirtual = value
        # Specifies that the containing data object is a pointer to data object.
        # atpSplitable property has no atp.
        # Splitkey due (PropertySetPattern).
        self._swPointerTarget: Optional["SwPointerTargetProps"] = None

    @property
    def sw_pointer_target(self) -> Optional["SwPointerTargetProps"]:
        """Get swPointerTarget (Pythonic accessor)."""
        return self._swPointerTarget

    @sw_pointer_target.setter
    def sw_pointer_target(self, value: Optional["SwPointerTargetProps"]) -> None:
        """
        Set swPointerTarget with validation.
        
        Args:
            value: The swPointerTarget to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swPointerTarget = None
            return

        if not isinstance(value, SwPointerTargetProps):
            raise TypeError(
                f"swPointerTarget must be SwPointerTargetProps or None, got {type(value).__name__}"
            )
        self._swPointerTarget = value
        # Record layout for this data object.
        # xml.
        # sequenceOffset=290 381 Document ID 89:
                # AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module Description Template
                # R23-11.
        self._swRecord: Optional["SwRecordLayout"] = None

    @property
    def sw_record(self) -> Optional["SwRecordLayout"]:
        """Get swRecord (Pythonic accessor)."""
        return self._swRecord

    @sw_record.setter
    def sw_record(self, value: Optional["SwRecordLayout"]) -> None:
        """
        Set swRecord with validation.
        
        Args:
            value: The swRecord to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swRecord = None
            return

        if not isinstance(value, SwRecordLayout):
            raise TypeError(
                f"swRecord must be SwRecordLayout or None, got {type(value).__name__}"
            )
        self._swRecord = value
        # This element specifies the frequency in which the object shall be or is
                # called or calculated.
        # This timing collected from the task in which write access the variable run.
        # But this cannot be done by system.
        # attribute can be used in an early phase to express refresh timing and later
                # on to specify the real.
        self._swRefresh: Optional["MultidimensionalTime"] = None

    @property
    def sw_refresh(self) -> Optional["MultidimensionalTime"]:
        """Get swRefresh (Pythonic accessor)."""
        return self._swRefresh

    @sw_refresh.setter
    def sw_refresh(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set swRefresh with validation.
        
        Args:
            value: The swRefresh to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swRefresh = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"swRefresh must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._swRefresh = value
        # the specific properties if the data object is a text object.
        self._swTextProps: Optional["SwTextProps"] = None

    @property
    def sw_text_props(self) -> Optional["SwTextProps"]:
        """Get swTextProps (Pythonic accessor)."""
        return self._swTextProps

    @sw_text_props.setter
    def sw_text_props(self, value: Optional["SwTextProps"]) -> None:
        """
        Set swTextProps with validation.
        
        Args:
            value: The swTextProps to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swTextProps = None
            return

        if not isinstance(value, SwTextProps):
            raise TypeError(
                f"swTextProps must be SwTextProps or None, got {type(value).__name__}"
            )
        self._swTextProps = value
        # This attribute is used to specify the dimensions of a value (VAL_BLK) for the
                # case that that value block has than one dimension.
        # given in this attribute are ordered such first entry represents the first
                # dimension, the represents the second dimension, and so value blocks the
                # attribute swValue be used and this attribute shall not exist.
        self._swValueBlock: List["Numerical"] = []

    @property
    def sw_value_block(self) -> List["Numerical"]:
        """Get swValueBlock (Pythonic accessor)."""
        return self._swValueBlock
        # Physical unit associated with the semantics of this data attribute applies if
        # no compuMethod is both units (this as well as via compuMethod) the units
        # shall be compatible.
        self._unit: Optional["Unit"] = None

    @property
    def unit(self) -> Optional["Unit"]:
        """Get unit (Pythonic accessor)."""
        return self._unit

    @unit.setter
    def unit(self, value: Optional["Unit"]) -> None:
        """
        Set unit with validation.
        
        Args:
            value: The unit to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._unit = None
            return

        if not isinstance(value, Unit):
            raise TypeError(
                f"unit must be Unit or None, got {type(value).__name__}"
            )
        self._unit = value
        # The referenced ApplicationPrimitiveDataType represents the primitive data
                # type of the value axis within a (e.
        # g.
        # curve, map).
        # It supersedes and BaseType.
        self._valueAxisData: Optional["ApplicationPrimitive"] = None

    @property
    def value_axis_data(self) -> Optional["ApplicationPrimitive"]:
        """Get valueAxisData (Pythonic accessor)."""
        return self._valueAxisData

    @value_axis_data.setter
    def value_axis_data(self, value: Optional["ApplicationPrimitive"]) -> None:
        """
        Set valueAxisData with validation.
        
        Args:
            value: The valueAxisData to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._valueAxisData = None
            return

        if not isinstance(value, ApplicationPrimitive):
            raise TypeError(
                f"valueAxisData must be ApplicationPrimitive or None, got {type(value).__name__}"
            )
        self._valueAxisData = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAdditionalNative(self) -> "NativeDeclarationString":
        """
        AUTOSAR-compliant getter for additionalNative.
        
        Returns:
            The additionalNative value
        
        Note:
            Delegates to additional_native property (CODING_RULE_V2_00017)
        """
        return self.additional_native  # Delegates to property

    def setAdditionalNative(self, value: "NativeDeclarationString") -> "SwDataDefProps":
        """
        AUTOSAR-compliant setter for additionalNative with method chaining.
        
        Args:
            value: The additionalNative to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to additional_native property setter (gets validation automatically)
        """
        self.additional_native = value  # Delegates to property setter
        return self

    def getAnnotation(self) -> List["Annotation"]:
        """
        AUTOSAR-compliant getter for annotation.
        
        Returns:
            The annotation value
        
        Note:
            Delegates to annotation property (CODING_RULE_V2_00017)
        """
        return self.annotation  # Delegates to property

    def getBaseType(self) -> "SwBaseType":
        """
        AUTOSAR-compliant getter for baseType.
        
        Returns:
            The baseType value
        
        Note:
            Delegates to base_type property (CODING_RULE_V2_00017)
        """
        return self.base_type  # Delegates to property

    def setBaseType(self, value: "SwBaseType") -> "SwDataDefProps":
        """
        AUTOSAR-compliant setter for baseType with method chaining.
        
        Args:
            value: The baseType to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to base_type property setter (gets validation automatically)
        """
        self.base_type = value  # Delegates to property setter
        return self

    def getCompuMethod(self) -> "CompuMethod":
        """
        AUTOSAR-compliant getter for compuMethod.
        
        Returns:
            The compuMethod value
        
        Note:
            Delegates to compu_method property (CODING_RULE_V2_00017)
        """
        return self.compu_method  # Delegates to property

    def setCompuMethod(self, value: "CompuMethod") -> "SwDataDefProps":
        """
        AUTOSAR-compliant setter for compuMethod with method chaining.
        
        Args:
            value: The compuMethod to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to compu_method property setter (gets validation automatically)
        """
        self.compu_method = value  # Delegates to property setter
        return self

    def getDataConstr(self) -> "DataConstr":
        """
        AUTOSAR-compliant getter for dataConstr.
        
        Returns:
            The dataConstr value
        
        Note:
            Delegates to data_constr property (CODING_RULE_V2_00017)
        """
        return self.data_constr  # Delegates to property

    def setDataConstr(self, value: "DataConstr") -> "SwDataDefProps":
        """
        AUTOSAR-compliant setter for dataConstr with method chaining.
        
        Args:
            value: The dataConstr to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to data_constr property setter (gets validation automatically)
        """
        self.data_constr = value  # Delegates to property setter
        return self

    def getDisplayFormat(self) -> "DisplayFormatString":
        """
        AUTOSAR-compliant getter for displayFormat.
        
        Returns:
            The displayFormat value
        
        Note:
            Delegates to display_format property (CODING_RULE_V2_00017)
        """
        return self.display_format  # Delegates to property

    def setDisplayFormat(self, value: "DisplayFormatString") -> "SwDataDefProps":
        """
        AUTOSAR-compliant setter for displayFormat with method chaining.
        
        Args:
            value: The displayFormat to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to display_format property setter (gets validation automatically)
        """
        self.display_format = value  # Delegates to property setter
        return self

    def getDisplay(self) -> "DisplayPresentation":
        """
        AUTOSAR-compliant getter for display.
        
        Returns:
            The display value
        
        Note:
            Delegates to display property (CODING_RULE_V2_00017)
        """
        return self.display  # Delegates to property

    def setDisplay(self, value: "DisplayPresentation") -> "SwDataDefProps":
        """
        AUTOSAR-compliant setter for display with method chaining.
        
        Args:
            value: The display to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to display property setter (gets validation automatically)
        """
        self.display = value  # Delegates to property setter
        return self

    def getImplementation(self) -> "AbstractImplementation":
        """
        AUTOSAR-compliant getter for implementation.
        
        Returns:
            The implementation value
        
        Note:
            Delegates to implementation property (CODING_RULE_V2_00017)
        """
        return self.implementation  # Delegates to property

    def setImplementation(self, value: "AbstractImplementation") -> "SwDataDefProps":
        """
        AUTOSAR-compliant setter for implementation with method chaining.
        
        Args:
            value: The implementation to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to implementation property setter (gets validation automatically)
        """
        self.implementation = value  # Delegates to property setter
        return self

    def getInvalidValue(self) -> "ValueSpecification":
        """
        AUTOSAR-compliant getter for invalidValue.
        
        Returns:
            The invalidValue value
        
        Note:
            Delegates to invalid_value property (CODING_RULE_V2_00017)
        """
        return self.invalid_value  # Delegates to property

    def setInvalidValue(self, value: "ValueSpecification") -> "SwDataDefProps":
        """
        AUTOSAR-compliant setter for invalidValue with method chaining.
        
        Args:
            value: The invalidValue to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to invalid_value property setter (gets validation automatically)
        """
        self.invalid_value = value  # Delegates to property setter
        return self

    def getStepSize(self) -> "Float":
        """
        AUTOSAR-compliant getter for stepSize.
        
        Returns:
            The stepSize value
        
        Note:
            Delegates to step_size property (CODING_RULE_V2_00017)
        """
        return self.step_size  # Delegates to property

    def setStepSize(self, value: "Float") -> "SwDataDefProps":
        """
        AUTOSAR-compliant setter for stepSize with method chaining.
        
        Args:
            value: The stepSize to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to step_size property setter (gets validation automatically)
        """
        self.step_size = value  # Delegates to property setter
        return self

    def getSwAddrMethod(self) -> "SwAddrMethod":
        """
        AUTOSAR-compliant getter for swAddrMethod.
        
        Returns:
            The swAddrMethod value
        
        Note:
            Delegates to sw_addr_method property (CODING_RULE_V2_00017)
        """
        return self.sw_addr_method  # Delegates to property

    def setSwAddrMethod(self, value: "SwAddrMethod") -> "SwDataDefProps":
        """
        AUTOSAR-compliant setter for swAddrMethod with method chaining.
        
        Args:
            value: The swAddrMethod to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sw_addr_method property setter (gets validation automatically)
        """
        self.sw_addr_method = value  # Delegates to property setter
        return self

    def getSwAlignment(self) -> "AlignmentType":
        """
        AUTOSAR-compliant getter for swAlignment.
        
        Returns:
            The swAlignment value
        
        Note:
            Delegates to sw_alignment property (CODING_RULE_V2_00017)
        """
        return self.sw_alignment  # Delegates to property

    def setSwAlignment(self, value: "AlignmentType") -> "SwDataDefProps":
        """
        AUTOSAR-compliant setter for swAlignment with method chaining.
        
        Args:
            value: The swAlignment to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sw_alignment property setter (gets validation automatically)
        """
        self.sw_alignment = value  # Delegates to property setter
        return self

    def getSwBit(self) -> "SwBitRepresentation":
        """
        AUTOSAR-compliant getter for swBit.
        
        Returns:
            The swBit value
        
        Note:
            Delegates to sw_bit property (CODING_RULE_V2_00017)
        """
        return self.sw_bit  # Delegates to property

    def setSwBit(self, value: "SwBitRepresentation") -> "SwDataDefProps":
        """
        AUTOSAR-compliant setter for swBit with method chaining.
        
        Args:
            value: The swBit to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sw_bit property setter (gets validation automatically)
        """
        self.sw_bit = value  # Delegates to property setter
        return self

    def getSwCalibration(self) -> "SwCalibrationAccess":
        """
        AUTOSAR-compliant getter for swCalibration.
        
        Returns:
            The swCalibration value
        
        Note:
            Delegates to sw_calibration property (CODING_RULE_V2_00017)
        """
        return self.sw_calibration  # Delegates to property

    def setSwCalibration(self, value: "SwCalibrationAccess") -> "SwDataDefProps":
        """
        AUTOSAR-compliant setter for swCalibration with method chaining.
        
        Args:
            value: The swCalibration to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sw_calibration property setter (gets validation automatically)
        """
        self.sw_calibration = value  # Delegates to property setter
        return self

    def getSwCalprmAxis(self) -> RefType:
        """
        AUTOSAR-compliant getter for swCalprmAxis.
        
        Returns:
            The swCalprmAxis value
        
        Note:
            Delegates to sw_calprm_axis property (CODING_RULE_V2_00017)
        """
        return self.sw_calprm_axis  # Delegates to property

    def setSwCalprmAxis(self, value: RefType) -> "SwDataDefProps":
        """
        AUTOSAR-compliant setter for swCalprmAxis with method chaining.
        
        Args:
            value: The swCalprmAxis to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sw_calprm_axis property setter (gets validation automatically)
        """
        self.sw_calprm_axis = value  # Delegates to property setter
        return self

    def getSwComparison(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for swComparison.
        
        Returns:
            The swComparison value
        
        Note:
            Delegates to sw_comparison property (CODING_RULE_V2_00017)
        """
        return self.sw_comparison  # Delegates to property

    def getSwData(self) -> RefType:
        """
        AUTOSAR-compliant getter for swData.
        
        Returns:
            The swData value
        
        Note:
            Delegates to sw_data property (CODING_RULE_V2_00017)
        """
        return self.sw_data  # Delegates to property

    def setSwData(self, value: RefType) -> "SwDataDefProps":
        """
        AUTOSAR-compliant setter for swData with method chaining.
        
        Args:
            value: The swData to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sw_data property setter (gets validation automatically)
        """
        self.sw_data = value  # Delegates to property setter
        return self

    def getSwHostVariable(self) -> RefType:
        """
        AUTOSAR-compliant getter for swHostVariable.
        
        Returns:
            The swHostVariable value
        
        Note:
            Delegates to sw_host_variable property (CODING_RULE_V2_00017)
        """
        return self.sw_host_variable  # Delegates to property

    def setSwHostVariable(self, value: RefType) -> "SwDataDefProps":
        """
        AUTOSAR-compliant setter for swHostVariable with method chaining.
        
        Args:
            value: The swHostVariable to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sw_host_variable property setter (gets validation automatically)
        """
        self.sw_host_variable = value  # Delegates to property setter
        return self

    def getSwImplPolicy(self) -> "SwImplPolicyEnum":
        """
        AUTOSAR-compliant getter for swImplPolicy.
        
        Returns:
            The swImplPolicy value
        
        Note:
            Delegates to sw_impl_policy property (CODING_RULE_V2_00017)
        """
        return self.sw_impl_policy  # Delegates to property

    def setSwImplPolicy(self, value: "SwImplPolicyEnum") -> "SwDataDefProps":
        """
        AUTOSAR-compliant setter for swImplPolicy with method chaining.
        
        Args:
            value: The swImplPolicy to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sw_impl_policy property setter (gets validation automatically)
        """
        self.sw_impl_policy = value  # Delegates to property setter
        return self

    def getSwIntended(self) -> "Numerical":
        """
        AUTOSAR-compliant getter for swIntended.
        
        Returns:
            The swIntended value
        
        Note:
            Delegates to sw_intended property (CODING_RULE_V2_00017)
        """
        return self.sw_intended  # Delegates to property

    def setSwIntended(self, value: "Numerical") -> "SwDataDefProps":
        """
        AUTOSAR-compliant setter for swIntended with method chaining.
        
        Args:
            value: The swIntended to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sw_intended property setter (gets validation automatically)
        """
        self.sw_intended = value  # Delegates to property setter
        return self

    def getSwInterpolation(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for swInterpolation.
        
        Returns:
            The swInterpolation value
        
        Note:
            Delegates to sw_interpolation property (CODING_RULE_V2_00017)
        """
        return self.sw_interpolation  # Delegates to property

    def setSwInterpolation(self, value: "Identifier") -> "SwDataDefProps":
        """
        AUTOSAR-compliant setter for swInterpolation with method chaining.
        
        Args:
            value: The swInterpolation to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sw_interpolation property setter (gets validation automatically)
        """
        self.sw_interpolation = value  # Delegates to property setter
        return self

    def getSwIsVirtual(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for swIsVirtual.
        
        Returns:
            The swIsVirtual value
        
        Note:
            Delegates to sw_is_virtual property (CODING_RULE_V2_00017)
        """
        return self.sw_is_virtual  # Delegates to property

    def setSwIsVirtual(self, value: "Boolean") -> "SwDataDefProps":
        """
        AUTOSAR-compliant setter for swIsVirtual with method chaining.
        
        Args:
            value: The swIsVirtual to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sw_is_virtual property setter (gets validation automatically)
        """
        self.sw_is_virtual = value  # Delegates to property setter
        return self

    def getSwPointerTarget(self) -> "SwPointerTargetProps":
        """
        AUTOSAR-compliant getter for swPointerTarget.
        
        Returns:
            The swPointerTarget value
        
        Note:
            Delegates to sw_pointer_target property (CODING_RULE_V2_00017)
        """
        return self.sw_pointer_target  # Delegates to property

    def setSwPointerTarget(self, value: "SwPointerTargetProps") -> "SwDataDefProps":
        """
        AUTOSAR-compliant setter for swPointerTarget with method chaining.
        
        Args:
            value: The swPointerTarget to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sw_pointer_target property setter (gets validation automatically)
        """
        self.sw_pointer_target = value  # Delegates to property setter
        return self

    def getSwRecord(self) -> "SwRecordLayout":
        """
        AUTOSAR-compliant getter for swRecord.
        
        Returns:
            The swRecord value
        
        Note:
            Delegates to sw_record property (CODING_RULE_V2_00017)
        """
        return self.sw_record  # Delegates to property

    def setSwRecord(self, value: "SwRecordLayout") -> "SwDataDefProps":
        """
        AUTOSAR-compliant setter for swRecord with method chaining.
        
        Args:
            value: The swRecord to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sw_record property setter (gets validation automatically)
        """
        self.sw_record = value  # Delegates to property setter
        return self

    def getSwRefresh(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for swRefresh.
        
        Returns:
            The swRefresh value
        
        Note:
            Delegates to sw_refresh property (CODING_RULE_V2_00017)
        """
        return self.sw_refresh  # Delegates to property

    def setSwRefresh(self, value: "MultidimensionalTime") -> "SwDataDefProps":
        """
        AUTOSAR-compliant setter for swRefresh with method chaining.
        
        Args:
            value: The swRefresh to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sw_refresh property setter (gets validation automatically)
        """
        self.sw_refresh = value  # Delegates to property setter
        return self

    def getSwTextProps(self) -> "SwTextProps":
        """
        AUTOSAR-compliant getter for swTextProps.
        
        Returns:
            The swTextProps value
        
        Note:
            Delegates to sw_text_props property (CODING_RULE_V2_00017)
        """
        return self.sw_text_props  # Delegates to property

    def setSwTextProps(self, value: "SwTextProps") -> "SwDataDefProps":
        """
        AUTOSAR-compliant setter for swTextProps with method chaining.
        
        Args:
            value: The swTextProps to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sw_text_props property setter (gets validation automatically)
        """
        self.sw_text_props = value  # Delegates to property setter
        return self

    def getSwValueBlock(self) -> List["Numerical"]:
        """
        AUTOSAR-compliant getter for swValueBlock.
        
        Returns:
            The swValueBlock value
        
        Note:
            Delegates to sw_value_block property (CODING_RULE_V2_00017)
        """
        return self.sw_value_block  # Delegates to property

    def getUnit(self) -> "Unit":
        """
        AUTOSAR-compliant getter for unit.
        
        Returns:
            The unit value
        
        Note:
            Delegates to unit property (CODING_RULE_V2_00017)
        """
        return self.unit  # Delegates to property

    def setUnit(self, value: "Unit") -> "SwDataDefProps":
        """
        AUTOSAR-compliant setter for unit with method chaining.
        
        Args:
            value: The unit to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to unit property setter (gets validation automatically)
        """
        self.unit = value  # Delegates to property setter
        return self

    def getValueAxisData(self) -> "ApplicationPrimitive":
        """
        AUTOSAR-compliant getter for valueAxisData.
        
        Returns:
            The valueAxisData value
        
        Note:
            Delegates to value_axis_data property (CODING_RULE_V2_00017)
        """
        return self.value_axis_data  # Delegates to property

    def setValueAxisData(self, value: "ApplicationPrimitive") -> "SwDataDefProps":
        """
        AUTOSAR-compliant setter for valueAxisData with method chaining.
        
        Args:
            value: The valueAxisData to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to value_axis_data property setter (gets validation automatically)
        """
        self.value_axis_data = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_additional_native(self, value: Optional["NativeDeclarationString"]) -> "SwDataDefProps":
        """
        Set additionalNative and return self for chaining.
        
        Args:
            value: The additionalNative to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_additional_native("value")
        """
        self.additional_native = value  # Use property setter (gets validation)
        return self

    def with_base_type(self, value: Optional["SwBaseType"]) -> "SwDataDefProps":
        """
        Set baseType and return self for chaining.
        
        Args:
            value: The baseType to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_base_type("value")
        """
        self.base_type = value  # Use property setter (gets validation)
        return self

    def with_compu_method(self, value: Optional["CompuMethod"]) -> "SwDataDefProps":
        """
        Set compuMethod and return self for chaining.
        
        Args:
            value: The compuMethod to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_compu_method("value")
        """
        self.compu_method = value  # Use property setter (gets validation)
        return self

    def with_data_constr(self, value: Optional["DataConstr"]) -> "SwDataDefProps":
        """
        Set dataConstr and return self for chaining.
        
        Args:
            value: The dataConstr to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_data_constr("value")
        """
        self.data_constr = value  # Use property setter (gets validation)
        return self

    def with_display_format(self, value: Optional["DisplayFormatString"]) -> "SwDataDefProps":
        """
        Set displayFormat and return self for chaining.
        
        Args:
            value: The displayFormat to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_display_format("value")
        """
        self.display_format = value  # Use property setter (gets validation)
        return self

    def with_display(self, value: Optional["DisplayPresentation"]) -> "SwDataDefProps":
        """
        Set display and return self for chaining.
        
        Args:
            value: The display to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_display("value")
        """
        self.display = value  # Use property setter (gets validation)
        return self

    def with_implementation(self, value: Optional["AbstractImplementation"]) -> "SwDataDefProps":
        """
        Set implementation and return self for chaining.
        
        Args:
            value: The implementation to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_implementation("value")
        """
        self.implementation = value  # Use property setter (gets validation)
        return self

    def with_invalid_value(self, value: Optional["ValueSpecification"]) -> "SwDataDefProps":
        """
        Set invalidValue and return self for chaining.
        
        Args:
            value: The invalidValue to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_invalid_value("value")
        """
        self.invalid_value = value  # Use property setter (gets validation)
        return self

    def with_step_size(self, value: Optional["Float"]) -> "SwDataDefProps":
        """
        Set stepSize and return self for chaining.
        
        Args:
            value: The stepSize to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_step_size("value")
        """
        self.step_size = value  # Use property setter (gets validation)
        return self

    def with_sw_addr_method(self, value: Optional["SwAddrMethod"]) -> "SwDataDefProps":
        """
        Set swAddrMethod and return self for chaining.
        
        Args:
            value: The swAddrMethod to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sw_addr_method("value")
        """
        self.sw_addr_method = value  # Use property setter (gets validation)
        return self

    def with_sw_alignment(self, value: Optional["AlignmentType"]) -> "SwDataDefProps":
        """
        Set swAlignment and return self for chaining.
        
        Args:
            value: The swAlignment to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sw_alignment("value")
        """
        self.sw_alignment = value  # Use property setter (gets validation)
        return self

    def with_sw_bit(self, value: Optional["SwBitRepresentation"]) -> "SwDataDefProps":
        """
        Set swBit and return self for chaining.
        
        Args:
            value: The swBit to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sw_bit("value")
        """
        self.sw_bit = value  # Use property setter (gets validation)
        return self

    def with_sw_calibration(self, value: Optional["SwCalibrationAccess"]) -> "SwDataDefProps":
        """
        Set swCalibration and return self for chaining.
        
        Args:
            value: The swCalibration to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sw_calibration("value")
        """
        self.sw_calibration = value  # Use property setter (gets validation)
        return self

    def with_sw_calprm_axis(self, value: Optional[RefType]) -> "SwDataDefProps":
        """
        Set swCalprmAxis and return self for chaining.
        
        Args:
            value: The swCalprmAxis to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sw_calprm_axis("value")
        """
        self.sw_calprm_axis = value  # Use property setter (gets validation)
        return self

    def with_sw_data(self, value: Optional[RefType]) -> "SwDataDefProps":
        """
        Set swData and return self for chaining.
        
        Args:
            value: The swData to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sw_data("value")
        """
        self.sw_data = value  # Use property setter (gets validation)
        return self

    def with_sw_host_variable(self, value: Optional[RefType]) -> "SwDataDefProps":
        """
        Set swHostVariable and return self for chaining.
        
        Args:
            value: The swHostVariable to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sw_host_variable("value")
        """
        self.sw_host_variable = value  # Use property setter (gets validation)
        return self

    def with_sw_impl_policy(self, value: Optional["SwImplPolicyEnum"]) -> "SwDataDefProps":
        """
        Set swImplPolicy and return self for chaining.
        
        Args:
            value: The swImplPolicy to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sw_impl_policy("value")
        """
        self.sw_impl_policy = value  # Use property setter (gets validation)
        return self

    def with_sw_intended(self, value: Optional["Numerical"]) -> "SwDataDefProps":
        """
        Set swIntended and return self for chaining.
        
        Args:
            value: The swIntended to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sw_intended("value")
        """
        self.sw_intended = value  # Use property setter (gets validation)
        return self

    def with_sw_interpolation(self, value: Optional["Identifier"]) -> "SwDataDefProps":
        """
        Set swInterpolation and return self for chaining.
        
        Args:
            value: The swInterpolation to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sw_interpolation("value")
        """
        self.sw_interpolation = value  # Use property setter (gets validation)
        return self

    def with_sw_is_virtual(self, value: Optional["Boolean"]) -> "SwDataDefProps":
        """
        Set swIsVirtual and return self for chaining.
        
        Args:
            value: The swIsVirtual to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sw_is_virtual("value")
        """
        self.sw_is_virtual = value  # Use property setter (gets validation)
        return self

    def with_sw_pointer_target(self, value: Optional["SwPointerTargetProps"]) -> "SwDataDefProps":
        """
        Set swPointerTarget and return self for chaining.
        
        Args:
            value: The swPointerTarget to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sw_pointer_target("value")
        """
        self.sw_pointer_target = value  # Use property setter (gets validation)
        return self

    def with_sw_record(self, value: Optional["SwRecordLayout"]) -> "SwDataDefProps":
        """
        Set swRecord and return self for chaining.
        
        Args:
            value: The swRecord to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sw_record("value")
        """
        self.sw_record = value  # Use property setter (gets validation)
        return self

    def with_sw_refresh(self, value: Optional["MultidimensionalTime"]) -> "SwDataDefProps":
        """
        Set swRefresh and return self for chaining.
        
        Args:
            value: The swRefresh to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sw_refresh("value")
        """
        self.sw_refresh = value  # Use property setter (gets validation)
        return self

    def with_sw_text_props(self, value: Optional["SwTextProps"]) -> "SwDataDefProps":
        """
        Set swTextProps and return self for chaining.
        
        Args:
            value: The swTextProps to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sw_text_props("value")
        """
        self.sw_text_props = value  # Use property setter (gets validation)
        return self

    def with_unit(self, value: Optional["Unit"]) -> "SwDataDefProps":
        """
        Set unit and return self for chaining.
        
        Args:
            value: The unit to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_unit("value")
        """
        self.unit = value  # Use property setter (gets validation)
        return self

    def with_value_axis_data(self, value: Optional["ApplicationPrimitive"]) -> "SwDataDefProps":
        """
        Set valueAxisData and return self for chaining.
        
        Args:
            value: The valueAxisData to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_value_axis_data("value")
        """
        self.value_axis_data = value  # Use property setter (gets validation)
        return self