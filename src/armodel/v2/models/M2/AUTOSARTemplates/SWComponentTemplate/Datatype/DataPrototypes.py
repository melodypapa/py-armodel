"""
AUTOSAR Package - DataPrototypes

Package: M2::AUTOSARTemplates::SWComponentTemplate::Datatype::DataPrototypes
"""

from abc import ABC
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class DataPrototype(Identifiable, ABC):
    """
    Base class for prototypical roles of any data type.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Datatype::DataPrototypes::DataPrototype

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 311, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 311, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 305, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2013, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is DataPrototype:
            raise TypeError("DataPrototype is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This property allows to specify data definition properties apply on data
        # prototype level.
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

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSwDataDef(self) -> "SwDataDefProps":
        """
        AUTOSAR-compliant getter for swDataDef.

        Returns:
            The swDataDef value

        Note:
            Delegates to sw_data_def property (CODING_RULE_V2_00017)
        """
        return self.sw_data_def  # Delegates to property

    def setSwDataDef(self, value: "SwDataDefProps") -> "DataPrototype":
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sw_data_def(self, value: Optional["SwDataDefProps"]) -> "DataPrototype":
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



class AutosarDataPrototype(DataPrototype, ABC):
    """
    Base class for prototypical roles of an AutosarDataType.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Datatype::DataPrototypes::AutosarDataPrototype

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 305, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 301, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 306, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2001, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is AutosarDataPrototype:
            raise TypeError("AutosarDataPrototype is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        self._type: Optional["AutosarDataType"] = None

    @property
    def type(self) -> Optional["AutosarDataType"]:
        """Get type (Pythonic accessor)."""
        return self._type

    @type.setter
    def type(self, value: Optional["AutosarDataType"]) -> None:
        """
        Set type with validation.

        Args:
            value: The type to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._type = None
            return

        if not isinstance(value, AutosarDataType):
            raise TypeError(
                f"type must be AutosarDataType or None, got {type(value).__name__}"
            )
        self._type = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getType(self) -> "AutosarDataType":
        """
        AUTOSAR-compliant getter for type.

        Returns:
            The type value

        Note:
            Delegates to type property (CODING_RULE_V2_00017)
        """
        return self.type  # Delegates to property

    def setType(self, value: "AutosarDataType") -> "AutosarDataPrototype":
        """
        AUTOSAR-compliant setter for type with method chaining.

        Args:
            value: The type to set

        Returns:
            self for method chaining

        Note:
            Delegates to type property setter (gets validation automatically)
        """
        self.type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_type(self, value: Optional["AutosarDataType"]) -> "AutosarDataPrototype":
        """
        Set type and return self for chaining.

        Args:
            value: The type to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_type("value")
        """
        self.type = value  # Use property setter (gets validation)
        return self



class ApplicationCompositeElementDataPrototype(DataPrototype, ABC):
    """
    This class represents a data prototype which is aggregated within a
    composite application data type (record or array). It is introduced to
    provide a better distinction between target and context in instance Refs.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Datatype::DataPrototypes::ApplicationCompositeElementDataPrototype

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 306, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 1996, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is ApplicationCompositeElementDataPrototype:
            raise TypeError("ApplicationCompositeElementDataPrototype is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        self._type: Optional["ApplicationDataType"] = None

    @property
    def type(self) -> Optional["ApplicationDataType"]:
        """Get type (Pythonic accessor)."""
        return self._type

    @type.setter
    def type(self, value: Optional["ApplicationDataType"]) -> None:
        """
        Set type with validation.

        Args:
            value: The type to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._type = None
            return

        if not isinstance(value, ApplicationDataType):
            raise TypeError(
                f"type must be ApplicationDataType or None, got {type(value).__name__}"
            )
        self._type = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getType(self) -> "ApplicationDataType":
        """
        AUTOSAR-compliant getter for type.

        Returns:
            The type value

        Note:
            Delegates to type property (CODING_RULE_V2_00017)
        """
        return self.type  # Delegates to property

    def setType(self, value: "ApplicationDataType") -> "ApplicationCompositeElementDataPrototype":
        """
        AUTOSAR-compliant setter for type with method chaining.

        Args:
            value: The type to set

        Returns:
            self for method chaining

        Note:
            Delegates to type property setter (gets validation automatically)
        """
        self.type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_type(self, value: Optional["ApplicationDataType"]) -> "ApplicationCompositeElementDataPrototype":
        """
        Set type and return self for chaining.

        Args:
            value: The type to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_type("value")
        """
        self.type = value  # Use property setter (gets validation)
        return self



class ParameterDataPrototype(AutosarDataPrototype):
    """
    A ParameterDataPrototype represents a formalized generic piece of
    information that is typically immutable by the application software layer,
    but mutable by measurement and calibration tools. ParameterDataPrototype is
    used in various contexts and the specific context gives the otherwise
    generic ParameterDataPrototype a dedicated semantics.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Datatype::DataPrototypes::ParameterDataPrototype

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 107, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 310, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2042, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 457, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies initial value(s) of the ParameterDataPrototype.
        self._initValue: Optional["ValueSpecification"] = None

    @property
    def init_value(self) -> Optional["ValueSpecification"]:
        """Get initValue (Pythonic accessor)."""
        return self._initValue

    @init_value.setter
    def init_value(self, value: Optional["ValueSpecification"]) -> None:
        """
        Set initValue with validation.

        Args:
            value: The initValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._initValue = None
            return

        if not isinstance(value, ValueSpecification):
            raise TypeError(
                f"initValue must be ValueSpecification or None, got {type(value).__name__}"
            )
        self._initValue = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInitValue(self) -> "ValueSpecification":
        """
        AUTOSAR-compliant getter for initValue.

        Returns:
            The initValue value

        Note:
            Delegates to init_value property (CODING_RULE_V2_00017)
        """
        return self.init_value  # Delegates to property

    def setInitValue(self, value: "ValueSpecification") -> "ParameterDataPrototype":
        """
        AUTOSAR-compliant setter for initValue with method chaining.

        Args:
            value: The initValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to init_value property setter (gets validation automatically)
        """
        self.init_value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_init_value(self, value: Optional["ValueSpecification"]) -> "ParameterDataPrototype":
        """
        Set initValue and return self for chaining.

        Args:
            value: The initValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_init_value("value")
        """
        self.init_value = value  # Use property setter (gets validation)
        return self



class VariableDataPrototype(AutosarDataPrototype):
    """
    A VariableDataPrototype represents a formalized generic piece of information
    that is typically mutable by the application software layer.
    VariableDataPrototype is used in various contexts and the specific context
    gives the otherwise generic VariableDataPrototype a dedicated semantics.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Datatype::DataPrototypes::VariableDataPrototype

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 107, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 310, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2077, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 256, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 29, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 223, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies initial value(s) of the VariableDataPrototype.
        self._initValue: Optional["ValueSpecification"] = None

    @property
    def init_value(self) -> Optional["ValueSpecification"]:
        """Get initValue (Pythonic accessor)."""
        return self._initValue

    @init_value.setter
    def init_value(self, value: Optional["ValueSpecification"]) -> None:
        """
        Set initValue with validation.

        Args:
            value: The initValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._initValue = None
            return

        if not isinstance(value, ValueSpecification):
            raise TypeError(
                f"initValue must be ValueSpecification or None, got {type(value).__name__}"
            )
        self._initValue = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInitValue(self) -> "ValueSpecification":
        """
        AUTOSAR-compliant getter for initValue.

        Returns:
            The initValue value

        Note:
            Delegates to init_value property (CODING_RULE_V2_00017)
        """
        return self.init_value  # Delegates to property

    def setInitValue(self, value: "ValueSpecification") -> "VariableDataPrototype":
        """
        AUTOSAR-compliant setter for initValue with method chaining.

        Args:
            value: The initValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to init_value property setter (gets validation automatically)
        """
        self.init_value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_init_value(self, value: Optional["ValueSpecification"]) -> "VariableDataPrototype":
        """
        Set initValue and return self for chaining.

        Args:
            value: The initValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_init_value("value")
        """
        self.init_value = value  # Use property setter (gets validation)
        return self



class ApplicationArrayElement(ApplicationCompositeElementDataPrototype):
    """
    Describes the properties of the elements of an application array data type.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Datatype::DataPrototypes::ApplicationArrayElement

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 252, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 43, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute controls how the information about the array size shall be
        # interpreted.
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
                # array.
        # The texttable entries textual value to an index number such that with that
                # index number is represented by a.
        self._indexDataType: Optional["ApplicationPrimitive"] = None

    @property
    def index_data_type(self) -> Optional["ApplicationPrimitive"]:
        """Get indexDataType (Pythonic accessor)."""
        return self._indexDataType

    @index_data_type.setter
    def index_data_type(self, value: Optional["ApplicationPrimitive"]) -> None:
        """
        Set indexDataType with validation.

        Args:
            value: The indexDataType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._indexDataType = None
            return

        if not isinstance(value, ApplicationPrimitive):
            raise TypeError(
                f"indexDataType must be ApplicationPrimitive or None, got {type(value).__name__}"
            )
        self._indexDataType = value
        self._maxNumberOf: Optional["PositiveInteger"] = None

    @property
    def max_number_of(self) -> Optional["PositiveInteger"]:
        """Get maxNumberOf (Pythonic accessor)."""
        return self._maxNumberOf

    @max_number_of.setter
    def max_number_of(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxNumberOf with validation.

        Args:
            value: The maxNumberOf to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxNumberOf = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"maxNumberOf must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._maxNumberOf = value

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

    def setArraySize(self, value: "ArraySizeSemantics") -> "ApplicationArrayElement":
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

    def getIndexDataType(self) -> "ApplicationPrimitive":
        """
        AUTOSAR-compliant getter for indexDataType.

        Returns:
            The indexDataType value

        Note:
            Delegates to index_data_type property (CODING_RULE_V2_00017)
        """
        return self.index_data_type  # Delegates to property

    def setIndexDataType(self, value: "ApplicationPrimitive") -> "ApplicationArrayElement":
        """
        AUTOSAR-compliant setter for indexDataType with method chaining.

        Args:
            value: The indexDataType to set

        Returns:
            self for method chaining

        Note:
            Delegates to index_data_type property setter (gets validation automatically)
        """
        self.index_data_type = value  # Delegates to property setter
        return self

    def getMaxNumberOf(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxNumberOf.

        Returns:
            The maxNumberOf value

        Note:
            Delegates to max_number_of property (CODING_RULE_V2_00017)
        """
        return self.max_number_of  # Delegates to property

    def setMaxNumberOf(self, value: "PositiveInteger") -> "ApplicationArrayElement":
        """
        AUTOSAR-compliant setter for maxNumberOf with method chaining.

        Args:
            value: The maxNumberOf to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_number_of property setter (gets validation automatically)
        """
        self.max_number_of = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_array_size(self, value: Optional["ArraySizeSemantics"]) -> "ApplicationArrayElement":
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

    def with_index_data_type(self, value: Optional["ApplicationPrimitive"]) -> "ApplicationArrayElement":
        """
        Set indexDataType and return self for chaining.

        Args:
            value: The indexDataType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_index_data_type("value")
        """
        self.index_data_type = value  # Use property setter (gets validation)
        return self

    def with_max_number_of(self, value: Optional["PositiveInteger"]) -> "ApplicationArrayElement":
        """
        Set maxNumberOf and return self for chaining.

        Args:
            value: The maxNumberOf to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_number_of("value")
        """
        self.max_number_of = value  # Use property setter (gets validation)
        return self



class ApplicationRecordElement(ApplicationCompositeElementDataPrototype):
    """
    Describes the properties of one particular element of an application record
    data type.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Datatype::DataPrototypes::ApplicationRecordElement

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 261, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 1997, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 43, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represents the ability to declare the as optional.
        # This that, at runtime, the ApplicationRecord or may not have a valid value
                # and shall ignored.
        # runtime software provides means to set as not valid at the sending a
                # communication and determine its validity at the.
        self._isOptional: Optional["Boolean"] = None

    @property
    def is_optional(self) -> Optional["Boolean"]:
        """Get isOptional (Pythonic accessor)."""
        return self._isOptional

    @is_optional.setter
    def is_optional(self, value: Optional["Boolean"]) -> None:
        """
        Set isOptional with validation.

        Args:
            value: The isOptional to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._isOptional = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"isOptional must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._isOptional = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIsOptional(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for isOptional.

        Returns:
            The isOptional value

        Note:
            Delegates to is_optional property (CODING_RULE_V2_00017)
        """
        return self.is_optional  # Delegates to property

    def setIsOptional(self, value: "Boolean") -> "ApplicationRecordElement":
        """
        AUTOSAR-compliant setter for isOptional with method chaining.

        Args:
            value: The isOptional to set

        Returns:
            self for method chaining

        Note:
            Delegates to is_optional property setter (gets validation automatically)
        """
        self.is_optional = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_is_optional(self, value: Optional["Boolean"]) -> "ApplicationRecordElement":
        """
        Set isOptional and return self for chaining.

        Args:
            value: The isOptional to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_is_optional("value")
        """
        self.is_optional = value  # Use property setter (gets validation)
        return self
