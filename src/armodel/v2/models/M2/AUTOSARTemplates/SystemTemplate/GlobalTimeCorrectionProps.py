from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class GlobalTimeCorrectionProps(ARObject):
    """
    This meta-class defines the attributes for rate and offset correction.

    Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime::GlobalTimeCorrectionProps

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 862, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Threshold for the correction method.
        # Deviations below value will be corrected by a linear reduction over a Values
                # equal- and greater than this be corrected by immediately setting the correct
                # rate in form of a jump.
        self._offsetCorrection: Optional["TimeValue"] = None

    @property
    def offset_correction(self) -> Optional["TimeValue"]:
        """Get offsetCorrection (Pythonic accessor)."""
        return self._offsetCorrection

    @offset_correction.setter
    def offset_correction(self, value: Optional["TimeValue"]) -> None:
        """
        Set offsetCorrection with validation.

        Args:
            value: The offsetCorrection to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._offsetCorrection = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"offsetCorrection must be TimeValue or None, got {type(value).__name__}"
            )
        self._offsetCorrection = value
        # Definition of the time span which is used to calculate the deviation.
        self._rateCorrection: Optional["TimeValue"] = None

    @property
    def rate_correction(self) -> Optional["TimeValue"]:
        """Get rateCorrection (Pythonic accessor)."""
        return self._rateCorrection

    @rate_correction.setter
    def rate_correction(self, value: Optional["TimeValue"]) -> None:
        """
        Set rateCorrection with validation.

        Args:
            value: The rateCorrection to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rateCorrection = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"rateCorrection must be TimeValue or None, got {type(value).__name__}"
            )
        self._rateCorrection = value
        # Defines the number of simultaneous rate measurements determine the current
        # rate deviation.
        self._rateCorrections: Optional["PositiveInteger"] = None

    @property
    def rate_corrections(self) -> Optional["PositiveInteger"]:
        """Get rateCorrections (Pythonic accessor)."""
        return self._rateCorrections

    @rate_corrections.setter
    def rate_corrections(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set rateCorrections with validation.

        Args:
            value: The rateCorrections to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rateCorrections = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"rateCorrections must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._rateCorrections = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getOffsetCorrection(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for offsetCorrection.

        Returns:
            The offsetCorrection value

        Note:
            Delegates to offset_correction property (CODING_RULE_V2_00017)
        """
        return self.offset_correction  # Delegates to property

    def setOffsetCorrection(self, value: "TimeValue") -> "GlobalTimeCorrectionProps":
        """
        AUTOSAR-compliant setter for offsetCorrection with method chaining.

        Args:
            value: The offsetCorrection to set

        Returns:
            self for method chaining

        Note:
            Delegates to offset_correction property setter (gets validation automatically)
        """
        self.offset_correction = value  # Delegates to property setter
        return self

    def getRateCorrection(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for rateCorrection.

        Returns:
            The rateCorrection value

        Note:
            Delegates to rate_correction property (CODING_RULE_V2_00017)
        """
        return self.rate_correction  # Delegates to property

    def setRateCorrection(self, value: "TimeValue") -> "GlobalTimeCorrectionProps":
        """
        AUTOSAR-compliant setter for rateCorrection with method chaining.

        Args:
            value: The rateCorrection to set

        Returns:
            self for method chaining

        Note:
            Delegates to rate_correction property setter (gets validation automatically)
        """
        self.rate_correction = value  # Delegates to property setter
        return self

    def getRateCorrections(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for rateCorrections.

        Returns:
            The rateCorrections value

        Note:
            Delegates to rate_corrections property (CODING_RULE_V2_00017)
        """
        return self.rate_corrections  # Delegates to property

    def setRateCorrections(self, value: "PositiveInteger") -> "GlobalTimeCorrectionProps":
        """
        AUTOSAR-compliant setter for rateCorrections with method chaining.

        Args:
            value: The rateCorrections to set

        Returns:
            self for method chaining

        Note:
            Delegates to rate_corrections property setter (gets validation automatically)
        """
        self.rate_corrections = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_offset_correction(self, value: Optional["TimeValue"]) -> "GlobalTimeCorrectionProps":
        """
        Set offsetCorrection and return self for chaining.

        Args:
            value: The offsetCorrection to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_offset_correction("value")
        """
        self.offset_correction = value  # Use property setter (gets validation)
        return self

    def with_rate_correction(self, value: Optional["TimeValue"]) -> "GlobalTimeCorrectionProps":
        """
        Set rateCorrection and return self for chaining.

        Args:
            value: The rateCorrection to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rate_correction("value")
        """
        self.rate_correction = value  # Use property setter (gets validation)
        return self

    def with_rate_corrections(self, value: Optional["PositiveInteger"]) -> "GlobalTimeCorrectionProps":
        """
        Set rateCorrections and return self for chaining.

        Args:
            value: The rateCorrections to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rate_corrections("value")
        """
        self.rate_corrections = value  # Use property setter (gets validation)
        return self
