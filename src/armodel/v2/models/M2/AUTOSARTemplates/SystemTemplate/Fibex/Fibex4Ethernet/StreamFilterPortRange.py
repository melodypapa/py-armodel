from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class StreamFilterPortRange(ARObject):
    """
    Configuration of filter rules for IP and TP.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::StreamFilterPortRange

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 139, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Filter to match packets with the maximum UDP/TCP port.
        self._max: Optional["PositiveInteger"] = None

    @property
    def max(self) -> Optional["PositiveInteger"]:
        """Get max (Pythonic accessor)."""
        return self._max

    @max.setter
    def max(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set max with validation.

        Args:
            value: The max to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._max = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"max must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._max = value
        # Filter to match packets with the minimum UDP/TCP port.
        self._min: Optional["PositiveInteger"] = None

    @property
    def min(self) -> Optional["PositiveInteger"]:
        """Get min (Pythonic accessor)."""
        return self._min

    @min.setter
    def min(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set min with validation.

        Args:
            value: The min to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._min = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"min must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._min = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMax(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for max.

        Returns:
            The max value

        Note:
            Delegates to max property (CODING_RULE_V2_00017)
        """
        return self.max  # Delegates to property

    def setMax(self, value: "PositiveInteger") -> "StreamFilterPortRange":
        """
        AUTOSAR-compliant setter for max with method chaining.

        Args:
            value: The max to set

        Returns:
            self for method chaining

        Note:
            Delegates to max property setter (gets validation automatically)
        """
        self.max = value  # Delegates to property setter
        return self

    def getMin(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for min.

        Returns:
            The min value

        Note:
            Delegates to min property (CODING_RULE_V2_00017)
        """
        return self.min  # Delegates to property

    def setMin(self, value: "PositiveInteger") -> "StreamFilterPortRange":
        """
        AUTOSAR-compliant setter for min with method chaining.

        Args:
            value: The min to set

        Returns:
            self for method chaining

        Note:
            Delegates to min property setter (gets validation automatically)
        """
        self.min = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_max(self, value: Optional["PositiveInteger"]) -> "StreamFilterPortRange":
        """
        Set max and return self for chaining.

        Args:
            value: The max to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max("value")
        """
        self.max = value  # Use property setter (gets validation)
        return self

    def with_min(self, value: Optional["PositiveInteger"]) -> "StreamFilterPortRange":
        """
        Set min and return self for chaining.

        Args:
            value: The min to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_min("value")
        """
        self.min = value  # Use property setter (gets validation)
        return self
