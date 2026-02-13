"""
AUTOSAR Package - Filter

Package: M2::AUTOSARTemplates::CommonStructure::Filter
"""


from __future__ import annotations

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    PositiveInteger,
)


class DataFilter(ARObject):
    """
    Base class for data filters. The type of the filter is specified in
    attribute dataFilterType. Some of the filter types require additional
    arguments which are specified as attributes of this class.

    Package: M2::AUTOSARTemplates::CommonStructure::Filter::DataFilter

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 182, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 394, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute specifies the type of the filter.
        self._dataFilterType: Optional[DataFilterTypeEnum] = None

    @property
    def data_filter_type(self) -> Optional[DataFilterTypeEnum]:
        """Get dataFilterType (Pythonic accessor)."""
        return self._dataFilterType

    @data_filter_type.setter
    def data_filter_type(self, value: Optional[DataFilterTypeEnum]) -> None:
        """
        Set dataFilterType with validation.

        Args:
            value: The dataFilterType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataFilterType = None
            return

        if not isinstance(value, DataFilterTypeEnum):
            raise TypeError(
                f"dataFilterType must be DataFilterTypeEnum or None, got {type(value).__name__}"
            )
        self._dataFilterType = value
        self._mask: Optional["UnlimitedInteger"] = None

    @property
    def mask(self) -> Optional["UnlimitedInteger"]:
        """Get mask (Pythonic accessor)."""
        return self._mask

    @mask.setter
    def mask(self, value: Optional["UnlimitedInteger"]) -> None:
        """
        Set mask with validation.

        Args:
            value: The mask to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mask = None
            return

        if not isinstance(value, UnlimitedInteger):
            raise TypeError(
                f"mask must be UnlimitedInteger or None, got {type(value).__name__}"
            )
        self._mask = value
        self._max: Optional["UnlimitedInteger"] = None

    @property
    def max(self) -> Optional["UnlimitedInteger"]:
        """Get max (Pythonic accessor)."""
        return self._max

    @max.setter
    def max(self, value: Optional["UnlimitedInteger"]) -> None:
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

        if not isinstance(value, UnlimitedInteger):
            raise TypeError(
                f"max must be UnlimitedInteger or None, got {type(value).__name__}"
            )
        self._max = value
        self._min: Optional["UnlimitedInteger"] = None

    @property
    def min(self) -> Optional["UnlimitedInteger"]:
        """Get min (Pythonic accessor)."""
        return self._min

    @min.setter
    def min(self, value: Optional["UnlimitedInteger"]) -> None:
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

        if not isinstance(value, UnlimitedInteger):
            raise TypeError(
                f"min must be UnlimitedInteger or None, got {type(value).__name__}"
            )
        self._min = value
        self._offset: Optional[PositiveInteger] = None

    @property
    def offset(self) -> Optional[PositiveInteger]:
        """Get offset (Pythonic accessor)."""
        return self._offset

    @offset.setter
    def offset(self, value: Optional[PositiveInteger]) -> None:
        """
        Set offset with validation.

        Args:
            value: The offset to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._offset = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"offset must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._offset = value
        self._period: Optional[PositiveInteger] = None

    @property
    def period(self) -> Optional[PositiveInteger]:
        """Get period (Pythonic accessor)."""
        return self._period

    @period.setter
    def period(self, value: Optional[PositiveInteger]) -> None:
        """
        Set period with validation.

        Args:
            value: The period to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._period = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"period must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._period = value
        self._x: Optional["UnlimitedInteger"] = None

    @property
    def x(self) -> Optional["UnlimitedInteger"]:
        """Get x (Pythonic accessor)."""
        return self._x

    @x.setter
    def x(self, value: Optional["UnlimitedInteger"]) -> None:
        """
        Set x with validation.

        Args:
            value: The x to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._x = None
            return

        if not isinstance(value, UnlimitedInteger):
            raise TypeError(
                f"x must be UnlimitedInteger or None, got {type(value).__name__}"
            )
        self._x = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataFilterType(self) -> DataFilterTypeEnum:
        """
        AUTOSAR-compliant getter for dataFilterType.

        Returns:
            The dataFilterType value

        Note:
            Delegates to data_filter_type property (CODING_RULE_V2_00017)
        """
        return self.data_filter_type  # Delegates to property

    def setDataFilterType(self, value: DataFilterTypeEnum) -> DataFilter:
        """
        AUTOSAR-compliant setter for dataFilterType with method chaining.

        Args:
            value: The dataFilterType to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_filter_type property setter (gets validation automatically)
        """
        self.data_filter_type = value  # Delegates to property setter
        return self

    def getMask(self) -> "UnlimitedInteger":
        """
        AUTOSAR-compliant getter for mask.

        Returns:
            The mask value

        Note:
            Delegates to mask property (CODING_RULE_V2_00017)
        """
        return self.mask  # Delegates to property

    def setMask(self, value: "UnlimitedInteger") -> DataFilter:
        """
        AUTOSAR-compliant setter for mask with method chaining.

        Args:
            value: The mask to set

        Returns:
            self for method chaining

        Note:
            Delegates to mask property setter (gets validation automatically)
        """
        self.mask = value  # Delegates to property setter
        return self

    def getMax(self) -> "UnlimitedInteger":
        """
        AUTOSAR-compliant getter for max.

        Returns:
            The max value

        Note:
            Delegates to max property (CODING_RULE_V2_00017)
        """
        return self.max  # Delegates to property

    def setMax(self, value: "UnlimitedInteger") -> DataFilter:
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

    def getMin(self) -> "UnlimitedInteger":
        """
        AUTOSAR-compliant getter for min.

        Returns:
            The min value

        Note:
            Delegates to min property (CODING_RULE_V2_00017)
        """
        return self.min  # Delegates to property

    def setMin(self, value: "UnlimitedInteger") -> DataFilter:
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

    def getOffset(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for offset.

        Returns:
            The offset value

        Note:
            Delegates to offset property (CODING_RULE_V2_00017)
        """
        return self.offset  # Delegates to property

    def setOffset(self, value: PositiveInteger) -> DataFilter:
        """
        AUTOSAR-compliant setter for offset with method chaining.

        Args:
            value: The offset to set

        Returns:
            self for method chaining

        Note:
            Delegates to offset property setter (gets validation automatically)
        """
        self.offset = value  # Delegates to property setter
        return self

    def getPeriod(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for period.

        Returns:
            The period value

        Note:
            Delegates to period property (CODING_RULE_V2_00017)
        """
        return self.period  # Delegates to property

    def setPeriod(self, value: PositiveInteger) -> DataFilter:
        """
        AUTOSAR-compliant setter for period with method chaining.

        Args:
            value: The period to set

        Returns:
            self for method chaining

        Note:
            Delegates to period property setter (gets validation automatically)
        """
        self.period = value  # Delegates to property setter
        return self

    def getX(self) -> "UnlimitedInteger":
        """
        AUTOSAR-compliant getter for x.

        Returns:
            The x value

        Note:
            Delegates to x property (CODING_RULE_V2_00017)
        """
        return self.x  # Delegates to property

    def setX(self, value: "UnlimitedInteger") -> DataFilter:
        """
        AUTOSAR-compliant setter for x with method chaining.

        Args:
            value: The x to set

        Returns:
            self for method chaining

        Note:
            Delegates to x property setter (gets validation automatically)
        """
        self.x = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_filter_type(self, value: Optional[DataFilterTypeEnum]) -> DataFilter:
        """
        Set dataFilterType and return self for chaining.

        Args:
            value: The dataFilterType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_filter_type("value")
        """
        self.data_filter_type = value  # Use property setter (gets validation)
        return self

    def with_mask(self, value: Optional["UnlimitedInteger"]) -> DataFilter:
        """
        Set mask and return self for chaining.

        Args:
            value: The mask to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mask("value")
        """
        self.mask = value  # Use property setter (gets validation)
        return self

    def with_max(self, value: Optional["UnlimitedInteger"]) -> DataFilter:
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

    def with_min(self, value: Optional["UnlimitedInteger"]) -> DataFilter:
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

    def with_offset(self, value: Optional[PositiveInteger]) -> DataFilter:
        """
        Set offset and return self for chaining.

        Args:
            value: The offset to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_offset("value")
        """
        self.offset = value  # Use property setter (gets validation)
        return self

    def with_period(self, value: Optional[PositiveInteger]) -> DataFilter:
        """
        Set period and return self for chaining.

        Args:
            value: The period to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_period("value")
        """
        self.period = value  # Use property setter (gets validation)
        return self

    def with_x(self, value: Optional["UnlimitedInteger"]) -> DataFilter:
        """
        Set x and return self for chaining.

        Args:
            value: The x to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_x("value")
        """
        self.x = value  # Use property setter (gets validation)
        return self


class DataFilterTypeEnum(AREnum):
    """
    DataFilterTypeEnum enumeration

This enum specifies the supported DataFilterTypes. Aggregated by DataFilter.dataFilterType

Package: M2::AUTOSARTemplates::CommonStructure::Filter
    """
    # Component Template
    Software = "None"

    # CP R23-11
    AUTOSAR = "None"

    # No filtering is performed so that the message always passes.
    always = "0"

    # Pass messages where the masked value has changed. new_value if the new message value is not filtered out)
    maskedNewDiffersMaskedOld = "1"

    # Pass messages whose masked value is not equal to a specific value x
    maskedNewDiffersX = "2"

    # Pass messages whose masked value is equal to a specific value x
    maskedNewEqualsX = "3"

    # The filter removes all messages.
    never = "4"

    # Pass a message if its value is outside a predefined boundary.
    newIsOutside = "5"

    # Pass a message if its value is within a predefined boundary.
    newIsWithinmin = "6"

    # Pass a message once every N message occurrences. Each time the message is received or transmitted, occurrence is incremented by 1 after filtering. Length of occurrence is 8 bit (minimum).
    oneEveryN = "7"
