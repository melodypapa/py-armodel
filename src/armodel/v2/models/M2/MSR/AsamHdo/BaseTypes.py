"""
AUTOSAR Package - BaseTypes

Package: M2::MSR::AsamHdo::BaseTypes
"""


from __future__ import annotations
from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
)


class BaseType(ARElement, ABC):
    """
    This abstract meta-class represents the ability to specify a platform
    dependent base type.

    Package: M2::MSR::AsamHdo::BaseTypes::BaseType

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 302, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 291, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2002, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is BaseType:
            raise TypeError("BaseType is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the actual definition of the base type.
        self._baseType: BaseTypeDefinition = None

    @property
    def base_type(self) -> BaseTypeDefinition:
        """Get baseType (Pythonic accessor)."""
        return self._baseType

    @base_type.setter
    def base_type(self, value: BaseTypeDefinition) -> None:
        """
        Set baseType with validation.

        Args:
            value: The baseType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, BaseTypeDefinition):
            raise TypeError(
                f"baseType must be BaseTypeDefinition, got {type(value).__name__}"
            )
        self._baseType = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBaseType(self) -> BaseTypeDefinition:
        """
        AUTOSAR-compliant getter for baseType.

        Returns:
            The baseType value

        Note:
            Delegates to base_type property (CODING_RULE_V2_00017)
        """
        return self.base_type  # Delegates to property

    def setBaseType(self, value: BaseTypeDefinition) -> BaseType:
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_base_type(self, value: BaseTypeDefinition) -> BaseType:
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



class BaseTypeDefinition(ARObject, ABC):
    """
    This meta-class represents the ability to define a basetype.

    Package: M2::MSR::AsamHdo::BaseTypes::BaseTypeDefinition

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 290, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is BaseTypeDefinition:
            raise TypeError("BaseTypeDefinition is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class SwBaseType(BaseType):
    """
    This meta-class represents a base type used within ECU software.

    Package: M2::MSR::AsamHdo::BaseTypes::SwBaseType

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 337, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 329, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 290, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2060, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (Page 33, Foundation R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 210, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class BaseTypeDirectDefinition(BaseTypeDefinition):
    """
    This BaseType is defined directly (as opposite to a derived BaseType)

    Package: M2::MSR::AsamHdo::BaseTypes::BaseTypeDirectDefinition

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

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"baseTypeSize must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._baseTypeSize = value
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

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"memAlignment must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._memAlignment = value
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

    def setBaseType(self, value: "BaseTypeEncoding") -> BaseTypeDirectDefinition:
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

    def setBaseTypeSize(self, value: "PositiveInteger") -> BaseTypeDirectDefinition:
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

    def setByteOrder(self, value: "ByteOrderEnum") -> BaseTypeDirectDefinition:
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

    def setMemAlignment(self, value: "PositiveInteger") -> BaseTypeDirectDefinition:
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

    def setNative(self, value: "NativeDeclarationString") -> BaseTypeDirectDefinition:
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

    def with_base_type(self, value: Optional["BaseTypeEncoding"]) -> BaseTypeDirectDefinition:
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

    def with_base_type_size(self, value: Optional["PositiveInteger"]) -> BaseTypeDirectDefinition:
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

    def with_byte_order(self, value: Optional["ByteOrderEnum"]) -> BaseTypeDirectDefinition:
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

    def with_mem_alignment(self, value: Optional["PositiveInteger"]) -> BaseTypeDirectDefinition:
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

    def with_native(self, value: Optional["NativeDeclarationString"]) -> BaseTypeDirectDefinition:
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


class BaseTypeEncodingString(ARLiteral):
    """
    BaseTypeEncodingString primitive type

This is the string denotion of a BaseType encoding. It may be refined by specific use-cases. Tags: xml.xsd.customType=BASE-TYPE-ENCODING-STRING xml.xsd.type=string Table 5.25: BaseTypeEncodingString

Package: M2::MSR::AsamHdo::BaseTypes
    """
    pass


