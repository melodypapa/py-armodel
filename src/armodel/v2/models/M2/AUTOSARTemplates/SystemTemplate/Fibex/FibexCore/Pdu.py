from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore import (
    FibexElement,
)


class Pdu(FibexElement, ABC):
    """
    Collection of all Pdus that can be routed through a bus interface.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 303, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 340, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is Pdu:
            raise TypeError("Pdu is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines whether the Pdu has dynamic (true) or not (false).
        # Please note that the usage of is restricted by [constr_3448].
        self._hasDynamic: Optional["Boolean"] = None

    @property
    def has_dynamic(self) -> Optional["Boolean"]:
        """Get hasDynamic (Pythonic accessor)."""
        return self._hasDynamic

    @has_dynamic.setter
    def has_dynamic(self, value: Optional["Boolean"]) -> None:
        """
        Set hasDynamic with validation.

        Args:
            value: The hasDynamic to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._hasDynamic = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"hasDynamic must be Boolean or None, got {type(value).__name__}"
            )
        self._hasDynamic = value
        # Pdu length in bytes.
        # In case of dynamic length IPdus dynamical length signal), this value maximum
                # data length.
        # It should be noted former AUTOSAR releases (Rel 2.
        # 1, Rel 3.
        # 0, Rel 4.
        # 0 Rev.
        # 1) this parameter was defined in bits.
        # length of zero bytes is allowed.
        self._length: Optional["UnlimitedInteger"] = None

    @property
    def length(self) -> Optional["UnlimitedInteger"]:
        """Get length (Pythonic accessor)."""
        return self._length

    @length.setter
    def length(self, value: Optional["UnlimitedInteger"]) -> None:
        """
        Set length with validation.

        Args:
            value: The length to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._length = None
            return

        if not isinstance(value, UnlimitedInteger):
            raise TypeError(
                f"length must be UnlimitedInteger or None, got {type(value).__name__}"
            )
        self._length = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getHasDynamic(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for hasDynamic.

        Returns:
            The hasDynamic value

        Note:
            Delegates to has_dynamic property (CODING_RULE_V2_00017)
        """
        return self.has_dynamic  # Delegates to property

    def setHasDynamic(self, value: "Boolean") -> "Pdu":
        """
        AUTOSAR-compliant setter for hasDynamic with method chaining.

        Args:
            value: The hasDynamic to set

        Returns:
            self for method chaining

        Note:
            Delegates to has_dynamic property setter (gets validation automatically)
        """
        self.has_dynamic = value  # Delegates to property setter
        return self

    def getLength(self) -> "UnlimitedInteger":
        """
        AUTOSAR-compliant getter for length.

        Returns:
            The length value

        Note:
            Delegates to length property (CODING_RULE_V2_00017)
        """
        return self.length  # Delegates to property

    def setLength(self, value: "UnlimitedInteger") -> "Pdu":
        """
        AUTOSAR-compliant setter for length with method chaining.

        Args:
            value: The length to set

        Returns:
            self for method chaining

        Note:
            Delegates to length property setter (gets validation automatically)
        """
        self.length = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_has_dynamic(self, value: Optional["Boolean"]) -> "Pdu":
        """
        Set hasDynamic and return self for chaining.

        Args:
            value: The hasDynamic to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_has_dynamic("value")
        """
        self.has_dynamic = value  # Use property setter (gets validation)
        return self

    def with_length(self, value: Optional["UnlimitedInteger"]) -> "Pdu":
        """
        Set length and return self for chaining.

        Args:
            value: The length to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_length("value")
        """
        self.length = value  # Use property setter (gets validation)
        return self
