from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    DataFilter,
    HandleTimeoutEnum,
    ReceiverComSpec,
    TimeValue,
    ValueSpecification,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class NonqueuedReceiverComSpec(ReceiverComSpec):
    """
    Communication attributes specific to non-queued receiving.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication::NonqueuedReceiverComSpec

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 172, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2039, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 198, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specify the amount of time (in seconds) after which the (via the RTE) needs
                # to be notified if data item have not been received the specified timing
                # description.
        # aliveTimeout attribute is 0 no timeout monitoring performed.
        self._aliveTimeout: Optional["TimeValue"] = None

    @property
    def alive_timeout(self) -> Optional["TimeValue"]:
        """Get aliveTimeout (Pythonic accessor)."""
        return self._aliveTimeout

    @alive_timeout.setter
    def alive_timeout(self, value: Optional["TimeValue"]) -> None:
        """
        Set aliveTimeout with validation.

        Args:
            value: The aliveTimeout to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._aliveTimeout = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"aliveTimeout must be TimeValue or None, got {type(value).__name__}"
            )
        self._aliveTimeout = value
        # This attribute controls whether application code is entitled whether the
        # value of the corresponding Variable been updated.
        self._enableUpdate: Optional["Boolean"] = None

    @property
    def enable_update(self) -> Optional["Boolean"]:
        """Get enableUpdate (Pythonic accessor)."""
        return self._enableUpdate

    @enable_update.setter
    def enable_update(self, value: Optional["Boolean"]) -> None:
        """
        Set enableUpdate with validation.

        Args:
            value: The enableUpdate to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._enableUpdate = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"enableUpdate must be Boolean or None, got {type(value).__name__}"
            )
        self._enableUpdate = value
        # The applicable filter algorithm for filtering the value of the.
        self._filter: Optional["DataFilter"] = None

    @property
    def filter(self) -> Optional["DataFilter"]:
        """Get filter (Pythonic accessor)."""
        return self._filter

    @filter.setter
    def filter(self, value: Optional["DataFilter"]) -> None:
        """
        Set filter with validation.

        Args:
            value: The filter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._filter = None
            return

        if not isinstance(value, DataFilter):
            raise TypeError(
                f"filter must be DataFilter or None, got {type(value).__name__}"
            )
        self._filter = value
        # If this attribute is set to true, then the Rte_IStatus API exist.
        # If the attribute does not exist or is set to false, Rte_IStatus API may still
                # exist in response to the further conditions.
        self._handleData: Optional["Boolean"] = None

    @property
    def handle_data(self) -> Optional["Boolean"]:
        """Get handleData (Pythonic accessor)."""
        return self._handleData

    @handle_data.setter
    def handle_data(self, value: Optional["Boolean"]) -> None:
        """
        Set handleData with validation.

        Args:
            value: The handleData to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._handleData = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"handleData must be Boolean or None, got {type(value).__name__}"
            )
        self._handleData = value
        # This attribute specifies whether for the corresponding the "never received"
                # flag is yes, the RTE is supposed to assume that VariableDataPrototype has not
                # been received the first reception of the corresponding flag is cleared.
        # the value of this attribute is set to "true" the flag is set to "false", the
                # RTE shall not support the "never for the corresponding Variable.
        self._handleNever: Optional["Boolean"] = None

    @property
    def handle_never(self) -> Optional["Boolean"]:
        """Get handleNever (Pythonic accessor)."""
        return self._handleNever

    @handle_never.setter
    def handle_never(self, value: Optional["Boolean"]) -> None:
        """
        Set handleNever with validation.

        Args:
            value: The handleNever to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._handleNever = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"handleNever must be Boolean or None, got {type(value).__name__}"
            )
        self._handleNever = value
        # This attribute controls the behavior with respect to the of timeouts.
        self._handleTimeout: Optional["HandleTimeoutEnum"] = None

    @property
    def handle_timeout(self) -> Optional["HandleTimeoutEnum"]:
        """Get handleTimeout (Pythonic accessor)."""
        return self._handleTimeout

    @handle_timeout.setter
    def handle_timeout(self, value: Optional["HandleTimeoutEnum"]) -> None:
        """
        Set handleTimeout with validation.

        Args:
            value: The handleTimeout to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._handleTimeout = None
            return

        if not isinstance(value, HandleTimeoutEnum):
            raise TypeError(
                f"handleTimeout must be HandleTimeoutEnum or None, got {type(value).__name__}"
            )
        self._handleTimeout = value
        # Initial value to be used in case the sending component is initialized.
        # If the sender also specifies an initial the receiver’s value will be used.
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
        # This attribute represents the substitution value applicable the case of a
        # timeout.
        self._timeout: Optional["ValueSpecification"] = None

    @property
    def timeout(self) -> Optional["ValueSpecification"]:
        """Get timeout (Pythonic accessor)."""
        return self._timeout

    @timeout.setter
    def timeout(self, value: Optional["ValueSpecification"]) -> None:
        """
        Set timeout with validation.

        Args:
            value: The timeout to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeout = None
            return

        if not isinstance(value, ValueSpecification):
            raise TypeError(
                f"timeout must be ValueSpecification or None, got {type(value).__name__}"
            )
        self._timeout = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAliveTimeout(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for aliveTimeout.

        Returns:
            The aliveTimeout value

        Note:
            Delegates to alive_timeout property (CODING_RULE_V2_00017)
        """
        return self.alive_timeout  # Delegates to property

    def setAliveTimeout(self, value: "TimeValue") -> "NonqueuedReceiverComSpec":
        """
        AUTOSAR-compliant setter for aliveTimeout with method chaining.

        Args:
            value: The aliveTimeout to set

        Returns:
            self for method chaining

        Note:
            Delegates to alive_timeout property setter (gets validation automatically)
        """
        self.alive_timeout = value  # Delegates to property setter
        return self

    def getEnableUpdate(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for enableUpdate.

        Returns:
            The enableUpdate value

        Note:
            Delegates to enable_update property (CODING_RULE_V2_00017)
        """
        return self.enable_update  # Delegates to property

    def setEnableUpdate(self, value: "Boolean") -> "NonqueuedReceiverComSpec":
        """
        AUTOSAR-compliant setter for enableUpdate with method chaining.

        Args:
            value: The enableUpdate to set

        Returns:
            self for method chaining

        Note:
            Delegates to enable_update property setter (gets validation automatically)
        """
        self.enable_update = value  # Delegates to property setter
        return self

    def getFilter(self) -> "DataFilter":
        """
        AUTOSAR-compliant getter for filter.

        Returns:
            The filter value

        Note:
            Delegates to filter property (CODING_RULE_V2_00017)
        """
        return self.filter  # Delegates to property

    def setFilter(self, value: "DataFilter") -> "NonqueuedReceiverComSpec":
        """
        AUTOSAR-compliant setter for filter with method chaining.

        Args:
            value: The filter to set

        Returns:
            self for method chaining

        Note:
            Delegates to filter property setter (gets validation automatically)
        """
        self.filter = value  # Delegates to property setter
        return self

    def getHandleData(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for handleData.

        Returns:
            The handleData value

        Note:
            Delegates to handle_data property (CODING_RULE_V2_00017)
        """
        return self.handle_data  # Delegates to property

    def setHandleData(self, value: "Boolean") -> "NonqueuedReceiverComSpec":
        """
        AUTOSAR-compliant setter for handleData with method chaining.

        Args:
            value: The handleData to set

        Returns:
            self for method chaining

        Note:
            Delegates to handle_data property setter (gets validation automatically)
        """
        self.handle_data = value  # Delegates to property setter
        return self

    def getHandleNever(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for handleNever.

        Returns:
            The handleNever value

        Note:
            Delegates to handle_never property (CODING_RULE_V2_00017)
        """
        return self.handle_never  # Delegates to property

    def setHandleNever(self, value: "Boolean") -> "NonqueuedReceiverComSpec":
        """
        AUTOSAR-compliant setter for handleNever with method chaining.

        Args:
            value: The handleNever to set

        Returns:
            self for method chaining

        Note:
            Delegates to handle_never property setter (gets validation automatically)
        """
        self.handle_never = value  # Delegates to property setter
        return self

    def getHandleTimeout(self) -> "HandleTimeoutEnum":
        """
        AUTOSAR-compliant getter for handleTimeout.

        Returns:
            The handleTimeout value

        Note:
            Delegates to handle_timeout property (CODING_RULE_V2_00017)
        """
        return self.handle_timeout  # Delegates to property

    def setHandleTimeout(self, value: "HandleTimeoutEnum") -> "NonqueuedReceiverComSpec":
        """
        AUTOSAR-compliant setter for handleTimeout with method chaining.

        Args:
            value: The handleTimeout to set

        Returns:
            self for method chaining

        Note:
            Delegates to handle_timeout property setter (gets validation automatically)
        """
        self.handle_timeout = value  # Delegates to property setter
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

    def setInitValue(self, value: "ValueSpecification") -> "NonqueuedReceiverComSpec":
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

    def getTimeout(self) -> "ValueSpecification":
        """
        AUTOSAR-compliant getter for timeout.

        Returns:
            The timeout value

        Note:
            Delegates to timeout property (CODING_RULE_V2_00017)
        """
        return self.timeout  # Delegates to property

    def setTimeout(self, value: "ValueSpecification") -> "NonqueuedReceiverComSpec":
        """
        AUTOSAR-compliant setter for timeout with method chaining.

        Args:
            value: The timeout to set

        Returns:
            self for method chaining

        Note:
            Delegates to timeout property setter (gets validation automatically)
        """
        self.timeout = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_alive_timeout(self, value: Optional["TimeValue"]) -> "NonqueuedReceiverComSpec":
        """
        Set aliveTimeout and return self for chaining.

        Args:
            value: The aliveTimeout to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_alive_timeout("value")
        """
        self.alive_timeout = value  # Use property setter (gets validation)
        return self

    def with_enable_update(self, value: Optional["Boolean"]) -> "NonqueuedReceiverComSpec":
        """
        Set enableUpdate and return self for chaining.

        Args:
            value: The enableUpdate to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_enable_update("value")
        """
        self.enable_update = value  # Use property setter (gets validation)
        return self

    def with_filter(self, value: Optional["DataFilter"]) -> "NonqueuedReceiverComSpec":
        """
        Set filter and return self for chaining.

        Args:
            value: The filter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_filter("value")
        """
        self.filter = value  # Use property setter (gets validation)
        return self

    def with_handle_data(self, value: Optional["Boolean"]) -> "NonqueuedReceiverComSpec":
        """
        Set handleData and return self for chaining.

        Args:
            value: The handleData to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_handle_data("value")
        """
        self.handle_data = value  # Use property setter (gets validation)
        return self

    def with_handle_never(self, value: Optional["Boolean"]) -> "NonqueuedReceiverComSpec":
        """
        Set handleNever and return self for chaining.

        Args:
            value: The handleNever to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_handle_never("value")
        """
        self.handle_never = value  # Use property setter (gets validation)
        return self

    def with_handle_timeout(self, value: Optional["HandleTimeoutEnum"]) -> "NonqueuedReceiverComSpec":
        """
        Set handleTimeout and return self for chaining.

        Args:
            value: The handleTimeout to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_handle_timeout("value")
        """
        self.handle_timeout = value  # Use property setter (gets validation)
        return self

    def with_init_value(self, value: Optional["ValueSpecification"]) -> "NonqueuedReceiverComSpec":
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

    def with_timeout(self, value: Optional["ValueSpecification"]) -> "NonqueuedReceiverComSpec":
        """
        Set timeout and return self for chaining.

        Args:
            value: The timeout to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timeout("value")
        """
        self.timeout = value  # Use property setter (gets validation)
        return self
