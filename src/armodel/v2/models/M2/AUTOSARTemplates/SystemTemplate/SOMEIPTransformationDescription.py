from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import TransformationDescription


class SOMEIPTransformationDescription(TransformationDescription):
    """
    The SOMEIPTransformationDescription is used to specify SOME/IP transformer
    specific attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::SOMEIPTransformationDescription

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 777, Classic Platform R23-11)
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
        # Defines which byte order shall be serialized by the.
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
        # The interface version the SOME/IP transformer shall use.
        self._interfaceVersion: Optional["PositiveInteger"] = None

    @property
    def interface_version(self) -> Optional["PositiveInteger"]:
        """Get interfaceVersion (Pythonic accessor)."""
        return self._interfaceVersion

    @interface_version.setter
    def interface_version(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set interfaceVersion with validation.

        Args:
            value: The interfaceVersion to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._interfaceVersion = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"interfaceVersion must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._interfaceVersion = value

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

    def setAlignment(self, value: "PositiveInteger") -> "SOMEIPTransformationDescription":
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

    def getByteOrder(self) -> "ByteOrderEnum":
        """
        AUTOSAR-compliant getter for byteOrder.

        Returns:
            The byteOrder value

        Note:
            Delegates to byte_order property (CODING_RULE_V2_00017)
        """
        return self.byte_order  # Delegates to property

    def setByteOrder(self, value: "ByteOrderEnum") -> "SOMEIPTransformationDescription":
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

    def getInterfaceVersion(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for interfaceVersion.

        Returns:
            The interfaceVersion value

        Note:
            Delegates to interface_version property (CODING_RULE_V2_00017)
        """
        return self.interface_version  # Delegates to property

    def setInterfaceVersion(self, value: "PositiveInteger") -> "SOMEIPTransformationDescription":
        """
        AUTOSAR-compliant setter for interfaceVersion with method chaining.

        Args:
            value: The interfaceVersion to set

        Returns:
            self for method chaining

        Note:
            Delegates to interface_version property setter (gets validation automatically)
        """
        self.interface_version = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_alignment(self, value: Optional["PositiveInteger"]) -> "SOMEIPTransformationDescription":
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

    def with_byte_order(self, value: Optional["ByteOrderEnum"]) -> "SOMEIPTransformationDescription":
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

    def with_interface_version(self, value: Optional["PositiveInteger"]) -> "SOMEIPTransformationDescription":
        """
        Set interfaceVersion and return self for chaining.

        Args:
            value: The interfaceVersion to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_interface_version("value")
        """
        self.interface_version = value  # Use property setter (gets validation)
        return self
