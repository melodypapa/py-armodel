from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class FlexrayFifoRange(ARObject):
    """
    FIFO Frame Id range acceptance criteria.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Flexray::FlexrayTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 87, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Max Range.
        self._rangeMax: Optional["Integer"] = None

    @property
    def range_max(self) -> Optional["Integer"]:
        """Get rangeMax (Pythonic accessor)."""
        return self._rangeMax

    @range_max.setter
    def range_max(self, value: Optional["Integer"]) -> None:
        """
        Set rangeMax with validation.

        Args:
            value: The rangeMax to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rangeMax = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"rangeMax must be Integer or None, got {type(value).__name__}"
            )
        self._rangeMax = value
        # Min Range.
        self._rangeMin: Optional["Integer"] = None

    @property
    def range_min(self) -> Optional["Integer"]:
        """Get rangeMin (Pythonic accessor)."""
        return self._rangeMin

    @range_min.setter
    def range_min(self, value: Optional["Integer"]) -> None:
        """
        Set rangeMin with validation.

        Args:
            value: The rangeMin to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rangeMin = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"rangeMin must be Integer or None, got {type(value).__name__}"
            )
        self._rangeMin = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRangeMax(self) -> "Integer":
        """
        AUTOSAR-compliant getter for rangeMax.

        Returns:
            The rangeMax value

        Note:
            Delegates to range_max property (CODING_RULE_V2_00017)
        """
        return self.range_max  # Delegates to property

    def setRangeMax(self, value: "Integer") -> "FlexrayFifoRange":
        """
        AUTOSAR-compliant setter for rangeMax with method chaining.

        Args:
            value: The rangeMax to set

        Returns:
            self for method chaining

        Note:
            Delegates to range_max property setter (gets validation automatically)
        """
        self.range_max = value  # Delegates to property setter
        return self

    def getRangeMin(self) -> "Integer":
        """
        AUTOSAR-compliant getter for rangeMin.

        Returns:
            The rangeMin value

        Note:
            Delegates to range_min property (CODING_RULE_V2_00017)
        """
        return self.range_min  # Delegates to property

    def setRangeMin(self, value: "Integer") -> "FlexrayFifoRange":
        """
        AUTOSAR-compliant setter for rangeMin with method chaining.

        Args:
            value: The rangeMin to set

        Returns:
            self for method chaining

        Note:
            Delegates to range_min property setter (gets validation automatically)
        """
        self.range_min = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_range_max(self, value: Optional["Integer"]) -> "FlexrayFifoRange":
        """
        Set rangeMax and return self for chaining.

        Args:
            value: The rangeMax to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_range_max("value")
        """
        self.range_max = value  # Use property setter (gets validation)
        return self

    def with_range_min(self, value: Optional["Integer"]) -> "FlexrayFifoRange":
        """
        Set rangeMin and return self for chaining.

        Args:
            value: The rangeMin to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_range_min("value")
        """
        self.range_min = value  # Use property setter (gets validation)
        return self
