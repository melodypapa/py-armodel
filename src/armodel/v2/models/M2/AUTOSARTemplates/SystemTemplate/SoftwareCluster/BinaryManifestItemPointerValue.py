from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    Address,
    BinaryManifestItemValue,
    SymbolString,
)


class BinaryManifestItemPointerValue(BinaryManifestItemValue):
    """
    This meta-class has the ability to provide a value for a pointer in the
    context of a binary manifest item.

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::BinaryManifest::BinaryManifestItemPointerValue

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 922, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represents the address value of the value.
        self._address: Optional["Address"] = None

    @property
    def address(self) -> Optional["Address"]:
        """Get address (Pythonic accessor)."""
        return self._address

    @address.setter
    def address(self, value: Optional["Address"]) -> None:
        """
        Set address with validation.

        Args:
            value: The address to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._address = None
            return

        if not isinstance(value, Address):
            raise TypeError(
                f"address must be Address or None, got {type(value).__name__}"
            )
        self._address = value
        # This attribute represents the symbol associated with the handle.
        self._symbol: Optional["SymbolString"] = None

    @property
    def symbol(self) -> Optional["SymbolString"]:
        """Get symbol (Pythonic accessor)."""
        return self._symbol

    @symbol.setter
    def symbol(self, value: Optional["SymbolString"]) -> None:
        """
        Set symbol with validation.

        Args:
            value: The symbol to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._symbol = None
            return

        if not isinstance(value, SymbolString):
            raise TypeError(
                f"symbol must be SymbolString or None, got {type(value).__name__}"
            )
        self._symbol = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAddress(self) -> "Address":
        """
        AUTOSAR-compliant getter for address.

        Returns:
            The address value

        Note:
            Delegates to address property (CODING_RULE_V2_00017)
        """
        return self.address  # Delegates to property

    def setAddress(self, value: "Address") -> "BinaryManifestItemPointerValue":
        """
        AUTOSAR-compliant setter for address with method chaining.

        Args:
            value: The address to set

        Returns:
            self for method chaining

        Note:
            Delegates to address property setter (gets validation automatically)
        """
        self.address = value  # Delegates to property setter
        return self

    def getSymbol(self) -> "SymbolString":
        """
        AUTOSAR-compliant getter for symbol.

        Returns:
            The symbol value

        Note:
            Delegates to symbol property (CODING_RULE_V2_00017)
        """
        return self.symbol  # Delegates to property

    def setSymbol(self, value: "SymbolString") -> "BinaryManifestItemPointerValue":
        """
        AUTOSAR-compliant setter for symbol with method chaining.

        Args:
            value: The symbol to set

        Returns:
            self for method chaining

        Note:
            Delegates to symbol property setter (gets validation automatically)
        """
        self.symbol = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_address(self, value: Optional["Address"]) -> "BinaryManifestItemPointerValue":
        """
        Set address and return self for chaining.

        Args:
            value: The address to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_address("value")
        """
        self.address = value  # Use property setter (gets validation)
        return self

    def with_symbol(self, value: Optional["SymbolString"]) -> "BinaryManifestItemPointerValue":
        """
        Set symbol and return self for chaining.

        Args:
            value: The symbol to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_symbol("value")
        """
        self.symbol = value  # Use property setter (gets validation)
        return self
