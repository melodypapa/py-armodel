from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import Integer
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class TDHeaderIdRange(ARObject):
    """
    Specifies a range of PDU header identifiers. This range is specified by a
    minimum and maximum header identifier; and the maximum header identifier
    shall be greater than or equal the minimum header identifier.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDHeaderIdRange

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 70, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the maximum PDU header identifier, in other upper bound of a range
        # of PDU header.
        self._maxHeaderId: Optional["Integer"] = None

    @property
    def max_header_id(self) -> Optional["Integer"]:
        """Get maxHeaderId (Pythonic accessor)."""
        return self._maxHeaderId

    @max_header_id.setter
    def max_header_id(self, value: Optional["Integer"]) -> None:
        """
        Set maxHeaderId with validation.

        Args:
            value: The maxHeaderId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxHeaderId = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"maxHeaderId must be Integer or None, got {type(value).__name__}"
            )
        self._maxHeaderId = value
        # Specifies the minimum PDU header identifier, in other lower bound of a range
        # of PDU header.
        self._minHeaderId: Optional["Integer"] = None

    @property
    def min_header_id(self) -> Optional["Integer"]:
        """Get minHeaderId (Pythonic accessor)."""
        return self._minHeaderId

    @min_header_id.setter
    def min_header_id(self, value: Optional["Integer"]) -> None:
        """
        Set minHeaderId with validation.

        Args:
            value: The minHeaderId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minHeaderId = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"minHeaderId must be Integer or None, got {type(value).__name__}"
            )
        self._minHeaderId = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMaxHeaderId(self) -> "Integer":
        """
        AUTOSAR-compliant getter for maxHeaderId.

        Returns:
            The maxHeaderId value

        Note:
            Delegates to max_header_id property (CODING_RULE_V2_00017)
        """
        return self.max_header_id  # Delegates to property

    def setMaxHeaderId(self, value: "Integer") -> "TDHeaderIdRange":
        """
        AUTOSAR-compliant setter for maxHeaderId with method chaining.

        Args:
            value: The maxHeaderId to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_header_id property setter (gets validation automatically)
        """
        self.max_header_id = value  # Delegates to property setter
        return self

    def getMinHeaderId(self) -> "Integer":
        """
        AUTOSAR-compliant getter for minHeaderId.

        Returns:
            The minHeaderId value

        Note:
            Delegates to min_header_id property (CODING_RULE_V2_00017)
        """
        return self.min_header_id  # Delegates to property

    def setMinHeaderId(self, value: "Integer") -> "TDHeaderIdRange":
        """
        AUTOSAR-compliant setter for minHeaderId with method chaining.

        Args:
            value: The minHeaderId to set

        Returns:
            self for method chaining

        Note:
            Delegates to min_header_id property setter (gets validation automatically)
        """
        self.min_header_id = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_max_header_id(self, value: Optional["Integer"]) -> "TDHeaderIdRange":
        """
        Set maxHeaderId and return self for chaining.

        Args:
            value: The maxHeaderId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_header_id("value")
        """
        self.max_header_id = value  # Use property setter (gets validation)
        return self

    def with_min_header_id(self, value: Optional["Integer"]) -> "TDHeaderIdRange":
        """
        Set minHeaderId and return self for chaining.

        Args:
            value: The minHeaderId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_min_header_id("value")
        """
        self.min_header_id = value  # Use property setter (gets validation)
        return self
