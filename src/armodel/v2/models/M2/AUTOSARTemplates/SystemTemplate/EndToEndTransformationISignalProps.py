from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class EndToEndTransformationISignalProps(ARObject):
    """
    Holds all the ISignal specific attributes for the EndToEndTransformer.

    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::EndToEndTransformationISignalProps

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 808, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Length of payload and E2E header in bits.
        self._dataLength: Optional["PositiveInteger"] = None

    @property
    def data_length(self) -> Optional["PositiveInteger"]:
        """Get dataLength (Pythonic accessor)."""
        return self._dataLength

    @data_length.setter
    def data_length(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set dataLength with validation.

        Args:
            value: The dataLength to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataLength = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"dataLength must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._dataLength = value
        # Maximum length of payload and E2E header in bits.
        self._maxDataLength: Optional["PositiveInteger"] = None

    @property
    def max_data_length(self) -> Optional["PositiveInteger"]:
        """Get maxDataLength (Pythonic accessor)."""
        return self._maxDataLength

    @max_data_length.setter
    def max_data_length(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxDataLength with validation.

        Args:
            value: The maxDataLength to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxDataLength = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"maxDataLength must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._maxDataLength = value
        # Minimum length of payload and E2E header in bits.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._minDataLength: Optional["PositiveInteger"] = None

    @property
    def min_data_length(self) -> Optional["PositiveInteger"]:
        """Get minDataLength (Pythonic accessor)."""
        return self._minDataLength

    @min_data_length.setter
    def min_data_length(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set minDataLength with validation.

        Args:
            value: The minDataLength to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minDataLength = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"minDataLength must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._minDataLength = value
        # This attribute represents a unique numerical identifier source of a certain
                # transmission.
        # In case of this ID uniquely identifies the client.
        # is used for protection against masquerading.
        # concerning the maximum number of values is specific for each E2E profile)
                # this attribute are controlled by a semantic depends on the category of the
                # EndToEnd.
        self._sourceId: Optional["PositiveInteger"] = None

    @property
    def source_id(self) -> Optional["PositiveInteger"]:
        """Get sourceId (Pythonic accessor)."""
        return self._sourceId

    @source_id.setter
    def source_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set sourceId with validation.

        Args:
            value: The sourceId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sourceId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"sourceId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._sourceId = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataLength(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for dataLength.

        Returns:
            The dataLength value

        Note:
            Delegates to data_length property (CODING_RULE_V2_00017)
        """
        return self.data_length  # Delegates to property

    def setDataLength(self, value: "PositiveInteger") -> "EndToEndTransformationISignalProps":
        """
        AUTOSAR-compliant setter for dataLength with method chaining.

        Args:
            value: The dataLength to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_length property setter (gets validation automatically)
        """
        self.data_length = value  # Delegates to property setter
        return self

    def getMaxDataLength(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxDataLength.

        Returns:
            The maxDataLength value

        Note:
            Delegates to max_data_length property (CODING_RULE_V2_00017)
        """
        return self.max_data_length  # Delegates to property

    def setMaxDataLength(self, value: "PositiveInteger") -> "EndToEndTransformationISignalProps":
        """
        AUTOSAR-compliant setter for maxDataLength with method chaining.

        Args:
            value: The maxDataLength to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_data_length property setter (gets validation automatically)
        """
        self.max_data_length = value  # Delegates to property setter
        return self

    def getMinDataLength(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for minDataLength.

        Returns:
            The minDataLength value

        Note:
            Delegates to min_data_length property (CODING_RULE_V2_00017)
        """
        return self.min_data_length  # Delegates to property

    def setMinDataLength(self, value: "PositiveInteger") -> "EndToEndTransformationISignalProps":
        """
        AUTOSAR-compliant setter for minDataLength with method chaining.

        Args:
            value: The minDataLength to set

        Returns:
            self for method chaining

        Note:
            Delegates to min_data_length property setter (gets validation automatically)
        """
        self.min_data_length = value  # Delegates to property setter
        return self

    def getSourceId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for sourceId.

        Returns:
            The sourceId value

        Note:
            Delegates to source_id property (CODING_RULE_V2_00017)
        """
        return self.source_id  # Delegates to property

    def setSourceId(self, value: "PositiveInteger") -> "EndToEndTransformationISignalProps":
        """
        AUTOSAR-compliant setter for sourceId with method chaining.

        Args:
            value: The sourceId to set

        Returns:
            self for method chaining

        Note:
            Delegates to source_id property setter (gets validation automatically)
        """
        self.source_id = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_length(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationISignalProps":
        """
        Set dataLength and return self for chaining.

        Args:
            value: The dataLength to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_length("value")
        """
        self.data_length = value  # Use property setter (gets validation)
        return self

    def with_max_data_length(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationISignalProps":
        """
        Set maxDataLength and return self for chaining.

        Args:
            value: The maxDataLength to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_data_length("value")
        """
        self.max_data_length = value  # Use property setter (gets validation)
        return self

    def with_min_data_length(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationISignalProps":
        """
        Set minDataLength and return self for chaining.

        Args:
            value: The minDataLength to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_min_data_length("value")
        """
        self.min_data_length = value  # Use property setter (gets validation)
        return self

    def with_source_id(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationISignalProps":
        """
        Set sourceId and return self for chaining.

        Args:
            value: The sourceId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_source_id("value")
        """
        self.source_id = value  # Use property setter (gets validation)
        return self
