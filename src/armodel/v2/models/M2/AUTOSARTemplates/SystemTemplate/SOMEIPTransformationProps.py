from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class SOMEIPTransformationProps(TransformationProps):
    """
    The class SOMEIPTransformationProps specifies SOME/IP specific configuration
    properties.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::SOMEIPTransformationProps
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 783, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the padding for alignment purposes that will be the SOME/IP
                # transformer after the serialized the variable data length data element.
        # The be specified in Bits.
        self._alignment: Optional["PositiveInteger"] = None

    @property
    def alignment(self) -> Optional["PositiveInteger"]:
        """Get alignment (Pythonic accessor)."""
        return self._alignment

    @alignment.setter
    def alignment(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set alignment with validation.
        
        Args:
            value: The alignment to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._alignment = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"alignment must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._alignment = value
        # This attribute describes the size of the length field (in that will be put in
        # front of the referenced Array in message.
        self._sizeOfArray: Optional["PositiveInteger"] = None

    @property
    def size_of_array(self) -> Optional["PositiveInteger"]:
        """Get sizeOfArray (Pythonic accessor)."""
        return self._sizeOfArray

    @size_of_array.setter
    def size_of_array(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set sizeOfArray with validation.
        
        Args:
            value: The sizeOfArray to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sizeOfArray = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"sizeOfArray must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._sizeOfArray = value
        # This attribute describes the size of the length field (in that will be put in
        # front of the referenced String in message.
        self._sizeOfString: Optional["PositiveInteger"] = None

    @property
    def size_of_string(self) -> Optional["PositiveInteger"]:
        """Get sizeOfString (Pythonic accessor)."""
        return self._sizeOfString

    @size_of_string.setter
    def size_of_string(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set sizeOfString with validation.
        
        Args:
            value: The sizeOfString to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sizeOfString = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"sizeOfString must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._sizeOfString = value
        # This attribute describes the size of the length field (in that will be put in
        # front of a Structure in the SOME/.
        self._sizeOfStruct: Optional["PositiveInteger"] = None

    @property
    def size_of_struct(self) -> Optional["PositiveInteger"]:
        """Get sizeOfStruct (Pythonic accessor)."""
        return self._sizeOfStruct

    @size_of_struct.setter
    def size_of_struct(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set sizeOfStruct with validation.
        
        Args:
            value: The sizeOfStruct to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sizeOfStruct = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"sizeOfStruct must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._sizeOfStruct = value
        # This attribute describes the size of the length field (in that will be put in
        # front of a Union in the SOME/IP.
        self._sizeOfUnion: Optional["PositiveInteger"] = None

    @property
    def size_of_union(self) -> Optional["PositiveInteger"]:
        """Get sizeOfUnion (Pythonic accessor)."""
        return self._sizeOfUnion

    @size_of_union.setter
    def size_of_union(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set sizeOfUnion with validation.
        
        Args:
            value: The sizeOfUnion to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sizeOfUnion = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"sizeOfUnion must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._sizeOfUnion = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAlignment(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for alignment.
        
        Returns:
            The alignment value
        
        Note:
            Delegates to alignment property (CODING_RULE_V2_00017)
        """
        return self.alignment  # Delegates to property

    def setAlignment(self, value: "PositiveInteger") -> "SOMEIPTransformationProps":
        """
        AUTOSAR-compliant setter for alignment with method chaining.
        
        Args:
            value: The alignment to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to alignment property setter (gets validation automatically)
        """
        self.alignment = value  # Delegates to property setter
        return self

    def getSizeOfArray(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for sizeOfArray.
        
        Returns:
            The sizeOfArray value
        
        Note:
            Delegates to size_of_array property (CODING_RULE_V2_00017)
        """
        return self.size_of_array  # Delegates to property

    def setSizeOfArray(self, value: "PositiveInteger") -> "SOMEIPTransformationProps":
        """
        AUTOSAR-compliant setter for sizeOfArray with method chaining.
        
        Args:
            value: The sizeOfArray to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to size_of_array property setter (gets validation automatically)
        """
        self.size_of_array = value  # Delegates to property setter
        return self

    def getSizeOfString(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for sizeOfString.
        
        Returns:
            The sizeOfString value
        
        Note:
            Delegates to size_of_string property (CODING_RULE_V2_00017)
        """
        return self.size_of_string  # Delegates to property

    def setSizeOfString(self, value: "PositiveInteger") -> "SOMEIPTransformationProps":
        """
        AUTOSAR-compliant setter for sizeOfString with method chaining.
        
        Args:
            value: The sizeOfString to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to size_of_string property setter (gets validation automatically)
        """
        self.size_of_string = value  # Delegates to property setter
        return self

    def getSizeOfStruct(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for sizeOfStruct.
        
        Returns:
            The sizeOfStruct value
        
        Note:
            Delegates to size_of_struct property (CODING_RULE_V2_00017)
        """
        return self.size_of_struct  # Delegates to property

    def setSizeOfStruct(self, value: "PositiveInteger") -> "SOMEIPTransformationProps":
        """
        AUTOSAR-compliant setter for sizeOfStruct with method chaining.
        
        Args:
            value: The sizeOfStruct to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to size_of_struct property setter (gets validation automatically)
        """
        self.size_of_struct = value  # Delegates to property setter
        return self

    def getSizeOfUnion(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for sizeOfUnion.
        
        Returns:
            The sizeOfUnion value
        
        Note:
            Delegates to size_of_union property (CODING_RULE_V2_00017)
        """
        return self.size_of_union  # Delegates to property

    def setSizeOfUnion(self, value: "PositiveInteger") -> "SOMEIPTransformationProps":
        """
        AUTOSAR-compliant setter for sizeOfUnion with method chaining.
        
        Args:
            value: The sizeOfUnion to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to size_of_union property setter (gets validation automatically)
        """
        self.size_of_union = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_alignment(self, value: Optional["PositiveInteger"]) -> "SOMEIPTransformationProps":
        """
        Set alignment and return self for chaining.
        
        Args:
            value: The alignment to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_alignment("value")
        """
        self.alignment = value  # Use property setter (gets validation)
        return self

    def with_size_of_array(self, value: Optional["PositiveInteger"]) -> "SOMEIPTransformationProps":
        """
        Set sizeOfArray and return self for chaining.
        
        Args:
            value: The sizeOfArray to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_size_of_array("value")
        """
        self.size_of_array = value  # Use property setter (gets validation)
        return self

    def with_size_of_string(self, value: Optional["PositiveInteger"]) -> "SOMEIPTransformationProps":
        """
        Set sizeOfString and return self for chaining.
        
        Args:
            value: The sizeOfString to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_size_of_string("value")
        """
        self.size_of_string = value  # Use property setter (gets validation)
        return self

    def with_size_of_struct(self, value: Optional["PositiveInteger"]) -> "SOMEIPTransformationProps":
        """
        Set sizeOfStruct and return self for chaining.
        
        Args:
            value: The sizeOfStruct to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_size_of_struct("value")
        """
        self.size_of_struct = value  # Use property setter (gets validation)
        return self

    def with_size_of_union(self, value: Optional["PositiveInteger"]) -> "SOMEIPTransformationProps":
        """
        Set sizeOfUnion and return self for chaining.
        
        Args:
            value: The sizeOfUnion to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_size_of_union("value")
        """
        self.size_of_union = value  # Use property setter (gets validation)
        return self