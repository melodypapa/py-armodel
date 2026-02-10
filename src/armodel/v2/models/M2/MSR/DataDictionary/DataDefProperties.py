"""
AUTOSAR Package - DataDefProperties

Package: M2::MSR::DataDictionary::DataDefProperties
"""

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Float,
    Identifier,
    Integer,
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class SwPointerTargetProps(ARObject):
    """
    This element defines, that the data object (which is specified by the
    aggregating element) contains a reference to another data object or to a
    function in the CPU code. This corresponds to a pointer in the C-language.
    The attributes of this element describe the category and the detailed
    properties of the target which is either a data description or a function
    signature.

    Package: M2::MSR::DataDictionary::DataDefProperties::SwPointerTargetProps

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 39, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 311, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 286, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 471, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The referenced BswModuleEntry serves as the signature a function pointer
                # definition.
        # Primary use case: function as argument to other function.
        self._functionPointer: Optional["BswModuleEntry"] = None

    @property
    def function_pointer(self) -> Optional["BswModuleEntry"]:
        """Get functionPointer (Pythonic accessor)."""
        return self._functionPointer

    @function_pointer.setter
    def function_pointer(self, value: Optional["BswModuleEntry"]) -> None:
        """
        Set functionPointer with validation.

        Args:
            value: The functionPointer to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._functionPointer = None
            return

        if not isinstance(value, BswModuleEntry):
            raise TypeError(
                f"functionPointer must be BswModuleEntry or None, got {type(value).__name__}"
            )
        self._functionPointer = value
        # atpSplitable.
        self._swDataDef: Optional["SwDataDefProps"] = None

    @property
    def sw_data_def(self) -> Optional["SwDataDefProps"]:
        """Get swDataDef (Pythonic accessor)."""
        return self._swDataDef

    @sw_data_def.setter
    def sw_data_def(self, value: Optional["SwDataDefProps"]) -> None:
        """
        Set swDataDef with validation.

        Args:
            value: The swDataDef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swDataDef = None
            return

        if not isinstance(value, SwDataDefProps):
            raise TypeError(
                f"swDataDef must be SwDataDefProps or None, got {type(value).__name__}"
            )
        self._swDataDef = value
                # specify the category of data.
        # case of a function pointer, it could be used to denote of the referenced
                # BswModuleEntry.
        self._targetCategory: Optional["Identifier"] = None

    @property
    def target_category(self) -> Optional["Identifier"]:
        """Get targetCategory (Pythonic accessor)."""
        return self._targetCategory

    @target_category.setter
    def target_category(self, value: Optional["Identifier"]) -> None:
        """
        Set targetCategory with validation.

        Args:
            value: The targetCategory to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetCategory = None
            return

        if not isinstance(value, (Identifier, str)):
            raise TypeError(
                f"targetCategory must be Identifier or str or None, got {type(value).__name__}"
            )
        self._targetCategory = value

    def with_annotation(self, value):
        """
        Set annotation and return self for chaining.

        Args:
            value: The annotation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_annotation("value")
        """
        self.annotation = value  # Use property setter (gets validation)
        return self

    def with_sw_comparison(self, value):
        """
        Set sw_comparison and return self for chaining.

        Args:
            value: The sw_comparison to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_comparison("value")
        """
        self.sw_comparison = value  # Use property setter (gets validation)
        return self

    def with_sw_value_block(self, value):
        """
        Set sw_value_block and return self for chaining.

        Args:
            value: The sw_value_block to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_value_block("value")
        """
        self.sw_value_block = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFunctionPointer(self) -> "BswModuleEntry":
        """
        AUTOSAR-compliant getter for functionPointer.

        Returns:
            The functionPointer value

        Note:
            Delegates to function_pointer property (CODING_RULE_V2_00017)
        """
        return self.function_pointer  # Delegates to property

    def setFunctionPointer(self, value: "BswModuleEntry") -> "SwPointerTargetProps":
        """
        AUTOSAR-compliant setter for functionPointer with method chaining.

        Args:
            value: The functionPointer to set

        Returns:
            self for method chaining

        Note:
            Delegates to function_pointer property setter (gets validation automatically)
        """
        self.function_pointer = value  # Delegates to property setter
        return self

    def getSwDataDef(self) -> "SwDataDefProps":
        """
        AUTOSAR-compliant getter for swDataDef.

        Returns:
            The swDataDef value

        Note:
            Delegates to sw_data_def property (CODING_RULE_V2_00017)
        """
        return self.sw_data_def  # Delegates to property

    def setSwDataDef(self, value: "SwDataDefProps") -> "SwPointerTargetProps":
        """
        AUTOSAR-compliant setter for swDataDef with method chaining.

        Args:
            value: The swDataDef to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_data_def property setter (gets validation automatically)
        """
        self.sw_data_def = value  # Delegates to property setter
        return self

    def getTargetCategory(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for targetCategory.

        Returns:
            The targetCategory value

        Note:
            Delegates to target_category property (CODING_RULE_V2_00017)
        """
        return self.target_category  # Delegates to property

    def setTargetCategory(self, value: "Identifier") -> "SwPointerTargetProps":
        """
        AUTOSAR-compliant setter for targetCategory with method chaining.

        Args:
            value: The targetCategory to set

        Returns:
            self for method chaining

        Note:
            Delegates to target_category property setter (gets validation automatically)
        """
        self.target_category = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_function_pointer(self, value: Optional["BswModuleEntry"]) -> "SwPointerTargetProps":
        """
        Set functionPointer and return self for chaining.

        Args:
            value: The functionPointer to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_function_pointer("value")
        """
        self.function_pointer = value  # Use property setter (gets validation)
        return self

    def with_sw_data_def(self, value: Optional["SwDataDefProps"]) -> "SwPointerTargetProps":
        """
        Set swDataDef and return self for chaining.

        Args:
            value: The swDataDef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_data_def("value")
        """
        self.sw_data_def = value  # Use property setter (gets validation)
        return self

    def with_target_category(self, value: Optional["Identifier"]) -> "SwPointerTargetProps":
        """
        Set targetCategory and return self for chaining.

        Args:
            value: The targetCategory to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target_category("value")
        """
        self.target_category = value  # Use property setter (gets validation)
        return self



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

        if not isinstance(value, (Float, float)):
            raise TypeError(
                f"stepSize must be Float or float or None, got {type(value).__name__}"
            )
        self._stepSize = value
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
        # This is mainly applicable to calibration.
        self._swCalprmAxis: Optional["RefType"] = None

    @property
    def sw_calprm_axis(self) -> Optional["RefType"]:
        """Get swCalprmAxis (Pythonic accessor)."""
        return self._swCalprmAxis

    @sw_calprm_axis.setter
    def sw_calprm_axis(self, value: Optional["RefType"]) -> None:
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
        # 381 Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module
                # Description Template R23-11.
        self._swComparison: List["RefType"] = []

    @property
    def sw_comparison(self) -> List["RefType"]:
        """Get swComparison (Pythonic accessor)."""
        return self._swComparison
        # Describes how the value of the data object has to be from the value of
        # another data object (by the.
        self._swData: Optional["RefType"] = None

    @property
    def sw_data(self) -> Optional["RefType"]:
        """Get swData (Pythonic accessor)."""
        return self._swData

    @sw_data.setter
    def sw_data(self, value: Optional["RefType"]) -> None:
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
        # Only applicable to bit.
        self._swHostVariable: Optional["RefType"] = None

    @property
    def sw_host_variable(self) -> Optional["RefType"]:
        """Get swHostVariable (Pythonic accessor)."""
        return self._swHostVariable

    @sw_host_variable.setter
    def sw_host_variable(self, value: Optional["RefType"]) -> None:
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

        if not isinstance(value, (Identifier, str)):
            raise TypeError(
                f"swInterpolation must be Identifier or str or None, got {type(value).__name__}"
            )
        self._swInterpolation = value
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

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"swIsVirtual must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._swIsVirtual = value
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

    def getSwCalprmAxis(self) -> "RefType":
        """
        AUTOSAR-compliant getter for swCalprmAxis.

        Returns:
            The swCalprmAxis value

        Note:
            Delegates to sw_calprm_axis property (CODING_RULE_V2_00017)
        """
        return self.sw_calprm_axis  # Delegates to property

    def setSwCalprmAxis(self, value: "RefType") -> "SwDataDefProps":
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

    def getSwComparison(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for swComparison.

        Returns:
            The swComparison value

        Note:
            Delegates to sw_comparison property (CODING_RULE_V2_00017)
        """
        return self.sw_comparison  # Delegates to property

    def getSwData(self) -> "RefType":
        """
        AUTOSAR-compliant getter for swData.

        Returns:
            The swData value

        Note:
            Delegates to sw_data property (CODING_RULE_V2_00017)
        """
        return self.sw_data  # Delegates to property

    def setSwData(self, value: "RefType") -> "SwDataDefProps":
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

    def getSwHostVariable(self) -> "RefType":
        """
        AUTOSAR-compliant getter for swHostVariable.

        Returns:
            The swHostVariable value

        Note:
            Delegates to sw_host_variable property (CODING_RULE_V2_00017)
        """
        return self.sw_host_variable  # Delegates to property

    def setSwHostVariable(self, value: "RefType") -> "SwDataDefProps":
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



class SwTextProps(ARObject):
    """
    This meta-class expresses particular properties applicable to strings in
    variables or calibration parameters.

    Package: M2::MSR::DataDictionary::DataDefProperties::SwTextProps

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 343, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 313, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 249, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 216, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute controls the semantics of the arraysize for the array
                # representing the string in an Implementation there to support a safe
                # conversion between ImplementationDatatype, even length strings as required e.
        # g.
        # for Support of.
        self._arraySize: Optional["ArraySizeSemantics"] = None

    @property
    def array_size(self) -> Optional["ArraySizeSemantics"]:
        """Get arraySize (Pythonic accessor)."""
        return self._arraySize

    @array_size.setter
    def array_size(self, value: Optional["ArraySizeSemantics"]) -> None:
        """
        Set arraySize with validation.

        Args:
            value: The arraySize to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._arraySize = None
            return

        if not isinstance(value, ArraySizeSemantics):
            raise TypeError(
                f"arraySize must be ArraySizeSemantics or None, got {type(value).__name__}"
            )
        self._arraySize = value
        # In baseType denotes the intended encoding of in the string on level of
                # ApplicationData.
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
        # will be interpreted according to the encoding the associated base type of the
                # data object, (hex) represents the ASCII character zero as and 0 (dec)
                # represents an end of string as of the fill character depends on the
                # arraySize.
        self._swFillCharacter: Optional["Integer"] = None

    @property
    def sw_fill_character(self) -> Optional["Integer"]:
        """Get swFillCharacter (Pythonic accessor)."""
        return self._swFillCharacter

    @sw_fill_character.setter
    def sw_fill_character(self, value: Optional["Integer"]) -> None:
        """
        Set swFillCharacter with validation.

        Args:
            value: The swFillCharacter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swFillCharacter = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"swFillCharacter must be Integer or int or None, got {type(value).__name__}"
            )
        self._swFillCharacter = value
        # Note the bytes depends on the encoding in the.
        self._swMaxTextSize: Optional["Integer"] = None

    @property
    def sw_max_text_size(self) -> Optional["Integer"]:
        """Get swMaxTextSize (Pythonic accessor)."""
        return self._swMaxTextSize

    @sw_max_text_size.setter
    def sw_max_text_size(self, value: Optional["Integer"]) -> None:
        """
        Set swMaxTextSize with validation.

        Args:
            value: The swMaxTextSize to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swMaxTextSize = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"swMaxTextSize must be Integer or int or None, got {type(value).__name__}"
            )
        self._swMaxTextSize = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getArraySize(self) -> "ArraySizeSemantics":
        """
        AUTOSAR-compliant getter for arraySize.

        Returns:
            The arraySize value

        Note:
            Delegates to array_size property (CODING_RULE_V2_00017)
        """
        return self.array_size  # Delegates to property

    def setArraySize(self, value: "ArraySizeSemantics") -> "SwTextProps":
        """
        AUTOSAR-compliant setter for arraySize with method chaining.

        Args:
            value: The arraySize to set

        Returns:
            self for method chaining

        Note:
            Delegates to array_size property setter (gets validation automatically)
        """
        self.array_size = value  # Delegates to property setter
        return self

    def getBaseType(self) -> "SwBaseType":
        """
        AUTOSAR-compliant getter for baseType.

        Returns:
            The baseType value

        Note:
            Delegates to base_type property (CODING_RULE_V2_00017)
        """
        return self.base_type  # Delegates to property

    def setBaseType(self, value: "SwBaseType") -> "SwTextProps":
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

    def getSwFillCharacter(self) -> "Integer":
        """
        AUTOSAR-compliant getter for swFillCharacter.

        Returns:
            The swFillCharacter value

        Note:
            Delegates to sw_fill_character property (CODING_RULE_V2_00017)
        """
        return self.sw_fill_character  # Delegates to property

    def setSwFillCharacter(self, value: "Integer") -> "SwTextProps":
        """
        AUTOSAR-compliant setter for swFillCharacter with method chaining.

        Args:
            value: The swFillCharacter to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_fill_character property setter (gets validation automatically)
        """
        self.sw_fill_character = value  # Delegates to property setter
        return self

    def getSwMaxTextSize(self) -> "Integer":
        """
        AUTOSAR-compliant getter for swMaxTextSize.

        Returns:
            The swMaxTextSize value

        Note:
            Delegates to sw_max_text_size property (CODING_RULE_V2_00017)
        """
        return self.sw_max_text_size  # Delegates to property

    def setSwMaxTextSize(self, value: "Integer") -> "SwTextProps":
        """
        AUTOSAR-compliant setter for swMaxTextSize with method chaining.

        Args:
            value: The swMaxTextSize to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_max_text_size property setter (gets validation automatically)
        """
        self.sw_max_text_size = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_array_size(self, value: Optional["ArraySizeSemantics"]) -> "SwTextProps":
        """
        Set arraySize and return self for chaining.

        Args:
            value: The arraySize to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_array_size("value")
        """
        self.array_size = value  # Use property setter (gets validation)
        return self

    def with_base_type(self, value: Optional["SwBaseType"]) -> "SwTextProps":
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

    def with_sw_fill_character(self, value: Optional["Integer"]) -> "SwTextProps":
        """
        Set swFillCharacter and return self for chaining.

        Args:
            value: The swFillCharacter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_fill_character("value")
        """
        self.sw_fill_character = value  # Use property setter (gets validation)
        return self

    def with_sw_max_text_size(self, value: Optional["Integer"]) -> "SwTextProps":
        """
        Set swMaxTextSize and return self for chaining.

        Args:
            value: The swMaxTextSize to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_max_text_size("value")
        """
        self.sw_max_text_size = value  # Use property setter (gets validation)
        return self



class ValueList(ARObject):
    """
    This is a generic list of numerical values.

    Package: M2::MSR::DataDictionary::DataDefProperties::ValueList

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 350, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 314, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 459, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 222, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is a particular numerical value without variation.
        # Numerical * attr This is one entry in the list of numerical values.
        self._v: Optional["Numerical"] = None

    @property
    def v(self) -> Optional["Numerical"]:
        """Get v (Pythonic accessor)."""
        return self._v

    @v.setter
    def v(self, value: Optional["Numerical"]) -> None:
        """
        Set v with validation.

        Args:
            value: The v to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._v = None
            return

        if not isinstance(value, Numerical):
            raise TypeError(
                f"v must be Numerical or None, got {type(value).__name__}"
            )
        self._v = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getV(self) -> "Numerical":
        """
        AUTOSAR-compliant getter for v.

        Returns:
            The v value

        Note:
            Delegates to v property (CODING_RULE_V2_00017)
        """
        return self.v  # Delegates to property

    def setV(self, value: "Numerical") -> "ValueList":
        """
        AUTOSAR-compliant setter for v with method chaining.

        Args:
            value: The v to set

        Returns:
            self for method chaining

        Note:
            Delegates to v property setter (gets validation automatically)
        """
        self.v = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_v(self, value: Optional["Numerical"]) -> "ValueList":
        """
        Set v and return self for chaining.

        Args:
            value: The v to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_v("value")
        """
        self.v = value  # Use property setter (gets validation)
        return self



class SwBitRepresentation(ARObject):
    """
    Description of the structure of a bit variable: Comprises of the bitPosition
    in a memory object (e.g. sw HostVariable, which stands parallel to
    swBitRepresentation) and the numberOfBits . In this way, interrelated memory
    areas can be described. Non-related memory areas are not supported.

    Package: M2::MSR::DataDictionary::DataDefProperties::SwBitRepresentation

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 333, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # If the "bit data object" is hosted within another data object the memory can
        # be accessed via byte as well as this attribute specifies the position of the
        # The count starts at zero (0).
        self._bitPosition: Optional["Integer"] = None

    @property
    def bit_position(self) -> Optional["Integer"]:
        """Get bitPosition (Pythonic accessor)."""
        return self._bitPosition

    @bit_position.setter
    def bit_position(self, value: Optional["Integer"]) -> None:
        """
        Set bitPosition with validation.

        Args:
            value: The bitPosition to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bitPosition = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"bitPosition must be Integer or int or None, got {type(value).__name__}"
            )
        self._bitPosition = value
        self._numberOfBits: Optional["Integer"] = None

    @property
    def number_of_bits(self) -> Optional["Integer"]:
        """Get numberOfBits (Pythonic accessor)."""
        return self._numberOfBits

    @number_of_bits.setter
    def number_of_bits(self, value: Optional["Integer"]) -> None:
        """
        Set numberOfBits with validation.

        Args:
            value: The numberOfBits to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._numberOfBits = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"numberOfBits must be Integer or int or None, got {type(value).__name__}"
            )
        self._numberOfBits = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBitPosition(self) -> "Integer":
        """
        AUTOSAR-compliant getter for bitPosition.

        Returns:
            The bitPosition value

        Note:
            Delegates to bit_position property (CODING_RULE_V2_00017)
        """
        return self.bit_position  # Delegates to property

    def setBitPosition(self, value: "Integer") -> "SwBitRepresentation":
        """
        AUTOSAR-compliant setter for bitPosition with method chaining.

        Args:
            value: The bitPosition to set

        Returns:
            self for method chaining

        Note:
            Delegates to bit_position property setter (gets validation automatically)
        """
        self.bit_position = value  # Delegates to property setter
        return self

    def getNumberOfBits(self) -> "Integer":
        """
        AUTOSAR-compliant getter for numberOfBits.

        Returns:
            The numberOfBits value

        Note:
            Delegates to number_of_bits property (CODING_RULE_V2_00017)
        """
        return self.number_of_bits  # Delegates to property

    def setNumberOfBits(self, value: "Integer") -> "SwBitRepresentation":
        """
        AUTOSAR-compliant setter for numberOfBits with method chaining.

        Args:
            value: The numberOfBits to set

        Returns:
            self for method chaining

        Note:
            Delegates to number_of_bits property setter (gets validation automatically)
        """
        self.number_of_bits = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bit_position(self, value: Optional["Integer"]) -> "SwBitRepresentation":
        """
        Set bitPosition and return self for chaining.

        Args:
            value: The bitPosition to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bit_position("value")
        """
        self.bit_position = value  # Use property setter (gets validation)
        return self

    def with_number_of_bits(self, value: Optional["Integer"]) -> "SwBitRepresentation":
        """
        Set numberOfBits and return self for chaining.

        Args:
            value: The numberOfBits to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_number_of_bits("value")
        """
        self.number_of_bits = value  # Use property setter (gets validation)
        return self



class SwDataDependency(ARObject):
    """
    This element describes the interdependencies of data objects, e.g. variables
    and parameters. Use cases: • Calculate the value of a calibration parameter
    (by the MCD system) from the value(s) of other calibration parameters. •
    Virtual data - that means the data object is not directly in the ecu and
    this property describes how the "virtual variable" can be computed from the
    real ones (by the MCD system).

    Package: M2::MSR::DataDictionary::DataDefProperties::SwDataDependency

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 373, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This element describes the formula with which the between the participating
        # objects are.
        self._swData: Optional["CompuGenericMath"] = None

    @property
    def sw_data(self) -> Optional["CompuGenericMath"]:
        """Get swData (Pythonic accessor)."""
        return self._swData

    @sw_data.setter
    def sw_data(self, value: Optional["CompuGenericMath"]) -> None:
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

        if not isinstance(value, CompuGenericMath):
            raise TypeError(
                f"swData must be CompuGenericMath or None, got {type(value).__name__}"
            )
        self._swData = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSwData(self) -> "CompuGenericMath":
        """
        AUTOSAR-compliant getter for swData.

        Returns:
            The swData value

        Note:
            Delegates to sw_data property (CODING_RULE_V2_00017)
        """
        return self.sw_data  # Delegates to property

    def setSwData(self, value: "CompuGenericMath") -> "SwDataDependency":
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sw_data(self, value: Optional["CompuGenericMath"]) -> "SwDataDependency":
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



class SwDataDependencyArgs(ARObject):
    """
    This element specifies the elements used in a SwDataDependency.

    Package: M2::MSR::DataDictionary::DataDefProperties::SwDataDependencyArgs

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 374, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies a calibration parameter as an input argument to.
        self._swCalprmRef: Optional["RefType"] = None

    @property
    def sw_calprm_ref(self) -> Optional["RefType"]:
        """Get swCalprmRef (Pythonic accessor)."""
        return self._swCalprmRef

    @sw_calprm_ref.setter
    def sw_calprm_ref(self, value: Optional["RefType"]) -> None:
        """
        Set swCalprmRef with validation.

        Args:
            value: The swCalprmRef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swCalprmRef = None
            return

        self._swCalprmRef = value
        self._swVariable: Optional["RefType"] = None

    @property
    def sw_variable(self) -> Optional["RefType"]:
        """Get swVariable (Pythonic accessor)."""
        return self._swVariable

    @sw_variable.setter
    def sw_variable(self, value: Optional["RefType"]) -> None:
        """
        Set swVariable with validation.

        Args:
            value: The swVariable to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swVariable = None
            return

        self._swVariable = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSwCalprmRef(self) -> "RefType":
        """
        AUTOSAR-compliant getter for swCalprmRef.

        Returns:
            The swCalprmRef value

        Note:
            Delegates to sw_calprm_ref property (CODING_RULE_V2_00017)
        """
        return self.sw_calprm_ref  # Delegates to property

    def setSwCalprmRef(self, value: "RefType") -> "SwDataDependencyArgs":
        """
        AUTOSAR-compliant setter for swCalprmRef with method chaining.

        Args:
            value: The swCalprmRef to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_calprm_ref property setter (gets validation automatically)
        """
        self.sw_calprm_ref = value  # Delegates to property setter
        return self

    def getSwVariable(self) -> "RefType":
        """
        AUTOSAR-compliant getter for swVariable.

        Returns:
            The swVariable value

        Note:
            Delegates to sw_variable property (CODING_RULE_V2_00017)
        """
        return self.sw_variable  # Delegates to property

    def setSwVariable(self, value: "RefType") -> "SwDataDependencyArgs":
        """
        AUTOSAR-compliant setter for swVariable with method chaining.

        Args:
            value: The swVariable to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_variable property setter (gets validation automatically)
        """
        self.sw_variable = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sw_calprm_ref(self, value: Optional[RefType]) -> "SwDataDependencyArgs":
        """
        Set swCalprmRef and return self for chaining.

        Args:
            value: The swCalprmRef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_calprm_ref("value")
        """
        self.sw_calprm_ref = value  # Use property setter (gets validation)
        return self

    def with_sw_variable(self, value: Optional[RefType]) -> "SwDataDependencyArgs":
        """
        Set swVariable and return self for chaining.

        Args:
            value: The swVariable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_variable("value")
        """
        self.sw_variable = value  # Use property setter (gets validation)
        return self


class SwCalibrationAccessEnum(AREnum):
    """
    SwCalibrationAccessEnum enumeration

Determines the access rights to a data object w.r.t. measurement and calibration. Aggregated by ModeDeclarationGroupPrototype.swCalibrationAccess, SwCalprmAxis.swCalibrationAccess, SwData DefProps.swCalibrationAccess

Package: M2::MSR::DataDictionary::DataDefProperties
    """
    # The element will not be accessible via MCD tools, i.e. will not appear in the ASAP file.
    notAccessible = "0"

    # The element will only appear as read-only in an ASAP file.
    readOnly = "1"

    # The element will appear in the ASAP file with both read and write access.
    readWrite = "2"



class SwImplPolicyEnum(AREnum):
    """
    SwImplPolicyEnum enumeration

Specifies the implementation strategy with respect to consistency mechanisms of variables. Aggregated by BswInternalTriggeringPoint.swImplPolicy, InternalTriggeringPoint.swImplPolicy, SwDataDefProps.sw ImplPolicy, Trigger.swImplPolicy

Package: M2::MSR::DataDictionary::DataDefProperties
    """
    # forced implementation such that the running software within the ECU shall not modify it. For example implemented with the "const" modifier in C. This can be applied for parameters (not for those in
    const = "0"

    # Software Module Description Template
    Basic = "None"

    # CP R23-11
    AUTOSAR = "None"

    # This data element is fixed. In particular this indicates, that it might also be implemented e.g. as in place data, (#DEFINE).
    fixed = "1"

    # The data element is created for measurement purposes only. The data element is never read directly within the ECU software. In contrast to a "standard" data element in an unconnected provide port is, this unconnection is guaranteed for measurementPoint data elements.
    measurementPoint = "2"

    # The content of the data element is queued and the data element has ’event’ semantics, i.e. data elements are stored in a queue and all data elements are processed in ’first in first out’ order. The queuing is intended to be implemented by RTE Generator. This value is not applicable for parameters.
    queued = "3"

    # This is applicable for all kinds of data elements. For variable data prototypes the ’last is best’ semantics applies. For parameter there is no specific implementation directive.
    standard = "4"



class DisplayPresentationEnum(AREnum):
    """
    DisplayPresentationEnum enumeration

This meta-class represents the ability to provide values for controlling the presentation of data within measurement and calibration tools. Aggregated by SwDataDefProps.displayPresentation

Package: M2::MSR::DataDictionary::DataDefProperties
    """
    # The presentation of data shall form a continuous graph between data points.
    presentationContinuous = "0"

    # The presentation of data shall be step-shaped between data points.
    presentationDiscrete = "1"
