from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class BinaryManifestAddressableObject(Identifiable, ABC):
    """
    This meta-class acts as an abstract base class for addressable objects in
    the context of the binary manifest of a CP software cluster.

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::BinaryManifest::BinaryManifestAddressableObject

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 920, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is BinaryManifestAddressableObject:
            raise TypeError("BinaryManifestAddressableObject is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute specifies the address of the enclosing.
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
        # This attribute specifies the symbol of the addressable.
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

    def setAddress(self, value: "Address") -> "BinaryManifestAddressableObject":
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

    def setSymbol(self, value: "SymbolString") -> "BinaryManifestAddressableObject":
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

    def with_address(self, value: Optional["Address"]) -> "BinaryManifestAddressableObject":
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

    def with_symbol(self, value: Optional["SymbolString"]) -> "BinaryManifestAddressableObject":
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
