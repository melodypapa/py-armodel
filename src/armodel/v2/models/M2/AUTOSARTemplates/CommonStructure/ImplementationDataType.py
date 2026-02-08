from typing import List, Optional
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import AbstractImplementationDataType


class ImplementationDataType(AbstractImplementationDataType):
    """
    Describes a reusable data type on the implementation level. This will
    typically correspond to a typedef in C-code.

    Package: M2::AUTOSARTemplates::CommonStructure::ImplementationDataTypes::ImplementationDataType

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 320, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 230, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 299, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 268, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2031, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 47, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 451, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 193, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the profile which the array will follow in case this type is a
        # variable size array.
        self._dynamicArray: Optional["String"] = None

    @property
    def dynamic_array(self) -> Optional["String"]:
        """Get dynamicArray (Pythonic accessor)."""
        return self._dynamicArray

    @dynamic_array.setter
    def dynamic_array(self, value: Optional["String"]) -> None:
        """
        Set dynamicArray with validation.

        Args:
            value: The dynamicArray to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dynamicArray = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"dynamicArray must be String or None, got {type(value).__name__}"
            )
        self._dynamicArray = value
        # Specifies an element of an array, struct, or union data type.
        # of ImplementionDataTypeElement is variability with the purpose to support the
                # of elements inside a Implementation a structure.
        # atpVariation.
        self._subElement: List["ImplementationData"] = []

    @property
    def sub_element(self) -> List["ImplementationData"]:
        """Get subElement (Pythonic accessor)."""
        return self._subElement
        # This represents the SymbolProps for the Implementation.
        self._symbolProps: Optional["SymbolProps"] = None

    @property
    def symbol_props(self) -> Optional["SymbolProps"]:
        """Get symbolProps (Pythonic accessor)."""
        return self._symbolProps

    @symbol_props.setter
    def symbol_props(self, value: Optional["SymbolProps"]) -> None:
        """
        Set symbolProps with validation.

        Args:
            value: The symbolProps to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._symbolProps = None
            return

        if not isinstance(value, SymbolProps):
            raise TypeError(
                f"symbolProps must be SymbolProps or None, got {type(value).__name__}"
            )
        self._symbolProps = value
        # This attribute is used to control which part of the is supposed to trigger
        # data type.
        self._typeEmitter: Optional["NameToken"] = None

    @property
    def type_emitter(self) -> Optional["NameToken"]:
        """Get typeEmitter (Pythonic accessor)."""
        return self._typeEmitter

    @type_emitter.setter
    def type_emitter(self, value: Optional["NameToken"]) -> None:
        """
        Set typeEmitter with validation.

        Args:
            value: The typeEmitter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._typeEmitter = None
            return

        if not isinstance(value, NameToken):
            raise TypeError(
                f"typeEmitter must be NameToken or None, got {type(value).__name__}"
            )
        self._typeEmitter = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDynamicArray(self) -> "String":
        """
        AUTOSAR-compliant getter for dynamicArray.

        Returns:
            The dynamicArray value

        Note:
            Delegates to dynamic_array property (CODING_RULE_V2_00017)
        """
        return self.dynamic_array  # Delegates to property

    def setDynamicArray(self, value: "String") -> "ImplementationDataType":
        """
        AUTOSAR-compliant setter for dynamicArray with method chaining.

        Args:
            value: The dynamicArray to set

        Returns:
            self for method chaining

        Note:
            Delegates to dynamic_array property setter (gets validation automatically)
        """
        self.dynamic_array = value  # Delegates to property setter
        return self

    def getSubElement(self) -> List["ImplementationData"]:
        """
        AUTOSAR-compliant getter for subElement.

        Returns:
            The subElement value

        Note:
            Delegates to sub_element property (CODING_RULE_V2_00017)
        """
        return self.sub_element  # Delegates to property

    def getSymbolProps(self) -> "SymbolProps":
        """
        AUTOSAR-compliant getter for symbolProps.

        Returns:
            The symbolProps value

        Note:
            Delegates to symbol_props property (CODING_RULE_V2_00017)
        """
        return self.symbol_props  # Delegates to property

    def setSymbolProps(self, value: "SymbolProps") -> "ImplementationDataType":
        """
        AUTOSAR-compliant setter for symbolProps with method chaining.

        Args:
            value: The symbolProps to set

        Returns:
            self for method chaining

        Note:
            Delegates to symbol_props property setter (gets validation automatically)
        """
        self.symbol_props = value  # Delegates to property setter
        return self

    def getTypeEmitter(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for typeEmitter.

        Returns:
            The typeEmitter value

        Note:
            Delegates to type_emitter property (CODING_RULE_V2_00017)
        """
        return self.type_emitter  # Delegates to property

    def setTypeEmitter(self, value: "NameToken") -> "ImplementationDataType":
        """
        AUTOSAR-compliant setter for typeEmitter with method chaining.

        Args:
            value: The typeEmitter to set

        Returns:
            self for method chaining

        Note:
            Delegates to type_emitter property setter (gets validation automatically)
        """
        self.type_emitter = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_dynamic_array(self, value: Optional["String"]) -> "ImplementationDataType":
        """
        Set dynamicArray and return self for chaining.

        Args:
            value: The dynamicArray to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dynamic_array("value")
        """
        self.dynamic_array = value  # Use property setter (gets validation)
        return self

    def with_symbol_props(self, value: Optional["SymbolProps"]) -> "ImplementationDataType":
        """
        Set symbolProps and return self for chaining.

        Args:
            value: The symbolProps to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_symbol_props("value")
        """
        self.symbol_props = value  # Use property setter (gets validation)
        return self

    def with_type_emitter(self, value: Optional["NameToken"]) -> "ImplementationDataType":
        """
        Set typeEmitter and return self for chaining.

        Args:
            value: The typeEmitter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_type_emitter("value")
        """
        self.type_emitter = value  # Use property setter (gets validation)
        return self
