from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import SenderComSpec


class NonqueuedSenderComSpec(SenderComSpec):
    """
    Communication attributes for non-queued sender/receiver communication
    (sender side)

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication::NonqueuedSenderComSpec

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 179, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 198, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The applicable filter algorithm for filtering the value of the.
        self._dataFilter: Optional["DataFilter"] = None

    @property
    def data_filter(self) -> Optional["DataFilter"]:
        """Get dataFilter (Pythonic accessor)."""
        return self._dataFilter

    @data_filter.setter
    def data_filter(self, value: Optional["DataFilter"]) -> None:
        """
        Set dataFilter with validation.

        Args:
            value: The dataFilter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataFilter = None
            return

        if not isinstance(value, DataFilter):
            raise TypeError(
                f"dataFilter must be DataFilter or None, got {type(value).__name__}"
            )
        self._dataFilter = value
        # Initial value to be sent if sender component is not yet fully receiver needs
        # data already.
        self._initValue: Optional["ValueSpecification"] = None

    @property
    def init_value(self) -> Optional["ValueSpecification"]:
        """Get initValue (Pythonic accessor)."""
        return self._initValue

    @init_value.setter
    def init_value(self, value: Optional["ValueSpecification"]) -> None:
        """
        Set initValue with validation.

        Args:
            value: The initValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._initValue = None
            return

        if not isinstance(value, ValueSpecification):
            raise TypeError(
                f"initValue must be ValueSpecification or None, got {type(value).__name__}"
            )
        self._initValue = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataFilter(self) -> "DataFilter":
        """
        AUTOSAR-compliant getter for dataFilter.

        Returns:
            The dataFilter value

        Note:
            Delegates to data_filter property (CODING_RULE_V2_00017)
        """
        return self.data_filter  # Delegates to property

    def setDataFilter(self, value: "DataFilter") -> "NonqueuedSenderComSpec":
        """
        AUTOSAR-compliant setter for dataFilter with method chaining.

        Args:
            value: The dataFilter to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_filter property setter (gets validation automatically)
        """
        self.data_filter = value  # Delegates to property setter
        return self

    def getInitValue(self) -> "ValueSpecification":
        """
        AUTOSAR-compliant getter for initValue.

        Returns:
            The initValue value

        Note:
            Delegates to init_value property (CODING_RULE_V2_00017)
        """
        return self.init_value  # Delegates to property

    def setInitValue(self, value: "ValueSpecification") -> "NonqueuedSenderComSpec":
        """
        AUTOSAR-compliant setter for initValue with method chaining.

        Args:
            value: The initValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to init_value property setter (gets validation automatically)
        """
        self.init_value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_filter(self, value: Optional["DataFilter"]) -> "NonqueuedSenderComSpec":
        """
        Set dataFilter and return self for chaining.

        Args:
            value: The dataFilter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_filter("value")
        """
        self.data_filter = value  # Use property setter (gets validation)
        return self

    def with_init_value(self, value: Optional["ValueSpecification"]) -> "NonqueuedSenderComSpec":
        """
        Set initValue and return self for chaining.

        Args:
            value: The initValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_init_value("value")
        """
        self.init_value = value  # Use property setter (gets validation)
        return self
