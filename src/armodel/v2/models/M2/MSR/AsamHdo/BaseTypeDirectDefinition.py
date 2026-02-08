from typing import Optional


class BaseTypeDirectDefinition(BaseTypeDefinition):
    """
    This BaseType is defined directly (as opposite to a derived BaseType)

    Package: M2::MSR::AsamHdo::BaseTypes

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 302, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 290, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2002, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (Page 29, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This specifies, how an object of the current BaseType is encoded, e.
        # g.
        # in an ECU within a message sequence.
        self._baseType: Optional["BaseTypeEncoding"] = None

    @property
    def base_type(self) -> Optional["BaseTypeEncoding"]:
        """Get baseType (Pythonic accessor)."""
        return self._baseType

    @base_type.setter
    def base_type(self, value: Optional["BaseTypeEncoding"]) -> None:
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

        if not isinstance(value, BaseTypeEncoding):
            raise TypeError(
                f"baseType must be BaseTypeEncoding or None, got {type(value).__name__}"
            )
        self._baseType = value
        # Describes the length of the data type specified in the bits.
        self._baseTypeSize: Optional["PositiveInteger"] = None

    @property
    def base_type_size(self) -> Optional["PositiveInteger"]:
        """Get baseTypeSize (Pythonic accessor)."""
        return self._baseTypeSize

    @base_type_size.setter
    def base_type_size(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set baseTypeSize with validation.

        Args:
            value: The baseTypeSize to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._baseTypeSize = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"baseTypeSize must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._baseTypeSize = value
        # This attribute specifies the byte order of the base type.
        # 719 Document ID 673: AUTOSAR_CP_TPS_DiagnosticExtractTemplate Template
                # R23-11.
        self._byteOrder: Optional["ByteOrderEnum"] = None

    @property
    def byte_order(self) -> Optional["ByteOrderEnum"]:
        """Get byteOrder (Pythonic accessor)."""
        return self._byteOrder

    @byte_order.setter
    def byte_order(self, value: Optional["ByteOrderEnum"]) -> None:
        """
        Set byteOrder with validation.

        Args:
            value: The byteOrder to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._byteOrder = None
            return

        if not isinstance(value, ByteOrderEnum):
            raise TypeError(
                f"byteOrder must be ByteOrderEnum or None, got {type(value).__name__}"
            )
        self._byteOrder = value
        # This attribute describes the alignment of the memory bits.
        # E.
        # g.
        # "8" specifies, that the object in aligned to a byte while "32" specifies that
                # it is byte.
        # If the value is set to "0" the meaning interpreted as "unspecified".
        self._memAlignment: Optional["PositiveInteger"] = None

    @property
    def mem_alignment(self) -> Optional["PositiveInteger"]:
        """Get memAlignment (Pythonic accessor)."""
        return self._memAlignment

    @mem_alignment.setter
    def mem_alignment(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set memAlignment with validation.

        Args:
            value: The memAlignment to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._memAlignment = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"memAlignment must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._memAlignment = value
        # This attribute describes the declaration of such a base in the native
                # programming language, primarily in the C.
        # This can then be used by a to include the necessary declarations into file.
        # For example shortName: "MyUnsignedInt" native short" short MyUnsignedInt;
                # attribute is not defined the referring Implementation not be generated as a
                # typedef by RTE.
        # nativeDeclaration type is given it shall fulfill the by basetypeEncoding and
                # baseType required to ensure the consistent handling and software components,
                # RTE, COM and.
        self._native: Optional["NativeDeclarationString"] = None

    @property
    def native(self) -> Optional["NativeDeclarationString"]:
        """Get native (Pythonic accessor)."""
        return self._native

    @native.setter
    def native(self, value: Optional["NativeDeclarationString"]) -> None:
        """
        Set native with validation.

        Args:
            value: The native to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._native = None
            return

        if not isinstance(value, NativeDeclarationString):
            raise TypeError(
                f"native must be NativeDeclarationString or None, got {type(value).__name__}"
            )
        self._native = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBaseType(self) -> "BaseTypeEncoding":
        """
        AUTOSAR-compliant getter for baseType.

        Returns:
            The baseType value

        Note:
            Delegates to base_type property (CODING_RULE_V2_00017)
        """
        return self.base_type  # Delegates to property

    def setBaseType(self, value: "BaseTypeEncoding") -> "BaseTypeDirectDefinition":
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

    def getBaseTypeSize(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for baseTypeSize.

        Returns:
            The baseTypeSize value

        Note:
            Delegates to base_type_size property (CODING_RULE_V2_00017)
        """
        return self.base_type_size  # Delegates to property

    def setBaseTypeSize(self, value: "PositiveInteger") -> "BaseTypeDirectDefinition":
        """
        AUTOSAR-compliant setter for baseTypeSize with method chaining.

        Args:
            value: The baseTypeSize to set

        Returns:
            self for method chaining

        Note:
            Delegates to base_type_size property setter (gets validation automatically)
        """
        self.base_type_size = value  # Delegates to property setter
        return self

    def getByteOrder(self) -> "ByteOrderEnum":
        """
        AUTOSAR-compliant getter for byteOrder.

        Returns:
            The byteOrder value

        Note:
            Delegates to byte_order property (CODING_RULE_V2_00017)
        """
        return self.byte_order  # Delegates to property

    def setByteOrder(self, value: "ByteOrderEnum") -> "BaseTypeDirectDefinition":
        """
        AUTOSAR-compliant setter for byteOrder with method chaining.

        Args:
            value: The byteOrder to set

        Returns:
            self for method chaining

        Note:
            Delegates to byte_order property setter (gets validation automatically)
        """
        self.byte_order = value  # Delegates to property setter
        return self

    def getMemAlignment(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for memAlignment.

        Returns:
            The memAlignment value

        Note:
            Delegates to mem_alignment property (CODING_RULE_V2_00017)
        """
        return self.mem_alignment  # Delegates to property

    def setMemAlignment(self, value: "PositiveInteger") -> "BaseTypeDirectDefinition":
        """
        AUTOSAR-compliant setter for memAlignment with method chaining.

        Args:
            value: The memAlignment to set

        Returns:
            self for method chaining

        Note:
            Delegates to mem_alignment property setter (gets validation automatically)
        """
        self.mem_alignment = value  # Delegates to property setter
        return self

    def getNative(self) -> "NativeDeclarationString":
        """
        AUTOSAR-compliant getter for native.

        Returns:
            The native value

        Note:
            Delegates to native property (CODING_RULE_V2_00017)
        """
        return self.native  # Delegates to property

    def setNative(self, value: "NativeDeclarationString") -> "BaseTypeDirectDefinition":
        """
        AUTOSAR-compliant setter for native with method chaining.

        Args:
            value: The native to set

        Returns:
            self for method chaining

        Note:
            Delegates to native property setter (gets validation automatically)
        """
        self.native = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_base_type(self, value: Optional["BaseTypeEncoding"]) -> "BaseTypeDirectDefinition":
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

    def with_base_type_size(self, value: Optional["PositiveInteger"]) -> "BaseTypeDirectDefinition":
        """
        Set baseTypeSize and return self for chaining.

        Args:
            value: The baseTypeSize to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_base_type_size("value")
        """
        self.base_type_size = value  # Use property setter (gets validation)
        return self

    def with_byte_order(self, value: Optional["ByteOrderEnum"]) -> "BaseTypeDirectDefinition":
        """
        Set byteOrder and return self for chaining.

        Args:
            value: The byteOrder to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_byte_order("value")
        """
        self.byte_order = value  # Use property setter (gets validation)
        return self

    def with_mem_alignment(self, value: Optional["PositiveInteger"]) -> "BaseTypeDirectDefinition":
        """
        Set memAlignment and return self for chaining.

        Args:
            value: The memAlignment to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mem_alignment("value")
        """
        self.mem_alignment = value  # Use property setter (gets validation)
        return self

    def with_native(self, value: Optional["NativeDeclarationString"]) -> "BaseTypeDirectDefinition":
        """
        Set native and return self for chaining.

        Args:
            value: The native to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_native("value")
        """
        self.native = value  # Use property setter (gets validation)
        return self
