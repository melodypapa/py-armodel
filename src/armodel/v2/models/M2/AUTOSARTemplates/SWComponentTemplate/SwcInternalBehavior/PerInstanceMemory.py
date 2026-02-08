from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    CIdentifier,
    String,
    SwDataDefProps,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class PerInstanceMemory(Identifiable):
    """
    Defines a ’C’ typed memory-block that needs to be available for each
    instance of the SW-component. This is typically only useful if
    supportsMultipleInstantiation is set to "true" or if the software-component
    defines NVRAM access via permanent blocks.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::PerInstanceMemory::PerInstanceMemory

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 597, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies initial value(s) of the PerInstanceMemory.
        self._initValue: Optional["String"] = None

    @property
    def init_value(self) -> Optional["String"]:
        """Get initValue (Pythonic accessor)."""
        return self._initValue

    @init_value.setter
    def init_value(self, value: Optional["String"]) -> None:
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

        if not isinstance(value, String):
            raise TypeError(
                f"initValue must be String or None, got {type(value).__name__}"
            )
        self._initValue = value
        # This represents the ability to to allocate RAM at specific sections, for
        # example, to support the RAM Block by mapping to uninitialized RAM.
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
        # The name of the "C"-type.
        self._type: Optional["CIdentifier"] = None

    @property
    def type(self) -> Optional["CIdentifier"]:
        """Get type (Pythonic accessor)."""
        return self._type

    @type.setter
    def type(self, value: Optional["CIdentifier"]) -> None:
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

        if not isinstance(value, CIdentifier):
            raise TypeError(
                f"type must be CIdentifier or None, got {type(value).__name__}"
            )
        self._type = value
        # A definition of the type with the syntax of a ’C’ typedef.
        self._typeDefinition: Optional["String"] = None

    @property
    def type_definition(self) -> Optional["String"]:
        """Get typeDefinition (Pythonic accessor)."""
        return self._typeDefinition

    @type_definition.setter
    def type_definition(self, value: Optional["String"]) -> None:
        """
        Set typeDefinition with validation.

        Args:
            value: The typeDefinition to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._typeDefinition = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"typeDefinition must be String or None, got {type(value).__name__}"
            )
        self._typeDefinition = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInitValue(self) -> "String":
        """
        AUTOSAR-compliant getter for initValue.

        Returns:
            The initValue value

        Note:
            Delegates to init_value property (CODING_RULE_V2_00017)
        """
        return self.init_value  # Delegates to property

    def setInitValue(self, value: "String") -> "PerInstanceMemory":
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

    def getSwDataDef(self) -> "SwDataDefProps":
        """
        AUTOSAR-compliant getter for swDataDef.

        Returns:
            The swDataDef value

        Note:
            Delegates to sw_data_def property (CODING_RULE_V2_00017)
        """
        return self.sw_data_def  # Delegates to property

    def setSwDataDef(self, value: "SwDataDefProps") -> "PerInstanceMemory":
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

    def getType(self) -> "CIdentifier":
        """
        AUTOSAR-compliant getter for type.

        Returns:
            The type value

        Note:
            Delegates to type property (CODING_RULE_V2_00017)
        """
        return self.type  # Delegates to property

    def setType(self, value: "CIdentifier") -> "PerInstanceMemory":
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

    def getTypeDefinition(self) -> "String":
        """
        AUTOSAR-compliant getter for typeDefinition.

        Returns:
            The typeDefinition value

        Note:
            Delegates to type_definition property (CODING_RULE_V2_00017)
        """
        return self.type_definition  # Delegates to property

    def setTypeDefinition(self, value: "String") -> "PerInstanceMemory":
        """
        AUTOSAR-compliant setter for typeDefinition with method chaining.

        Args:
            value: The typeDefinition to set

        Returns:
            self for method chaining

        Note:
            Delegates to type_definition property setter (gets validation automatically)
        """
        self.type_definition = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_init_value(self, value: Optional["String"]) -> "PerInstanceMemory":
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

    def with_sw_data_def(self, value: Optional["SwDataDefProps"]) -> "PerInstanceMemory":
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

    def with_type(self, value: Optional["CIdentifier"]) -> "PerInstanceMemory":
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

    def with_type_definition(self, value: Optional["String"]) -> "PerInstanceMemory":
        """
        Set typeDefinition and return self for chaining.

        Args:
            value: The typeDefinition to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_type_definition("value")
        """
        self.type_definition = value  # Use property setter (gets validation)
        return self
