from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class CanClusterBusOffRecovery(ARObject):
    """
    This element contains the attributes that are used to configure the CAN bus
    off monitoring / recovery at system level.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 62, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This threshold defines the count of bus-offs until the recovery switches from
        # level 1 (short recovery level 2 (long recovery time).
        self._borCounterL1To: Optional["PositiveInteger"] = None

    @property
    def bor_counter_l1_to(self) -> Optional["PositiveInteger"]:
        """Get borCounterL1To (Pythonic accessor)."""
        return self._borCounterL1To

    @bor_counter_l1_to.setter
    def bor_counter_l1_to(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set borCounterL1To with validation.

        Args:
            value: The borCounterL1To to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._borCounterL1To = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"borCounterL1To must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._borCounterL1To = value
        # This attribute defines the duration of the bus-off recovery level 1 (short
                # recovery time) in seconds.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._borTimeL1: Optional["TimeValue"] = None

    @property
    def bor_time_l1(self) -> Optional["TimeValue"]:
        """Get borTimeL1 (Pythonic accessor)."""
        return self._borTimeL1

    @bor_time_l1.setter
    def bor_time_l1(self, value: Optional["TimeValue"]) -> None:
        """
        Set borTimeL1 with validation.

        Args:
            value: The borTimeL1 to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._borTimeL1 = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"borTimeL1 must be TimeValue or None, got {type(value).__name__}"
            )
        self._borTimeL1 = value
        # This attribute defines the duration of the bus-off recovery level 2 (long
        # recovery time) in seconds.
        self._borTimeL2: Optional["TimeValue"] = None

    @property
    def bor_time_l2(self) -> Optional["TimeValue"]:
        """Get borTimeL2 (Pythonic accessor)."""
        return self._borTimeL2

    @bor_time_l2.setter
    def bor_time_l2(self, value: Optional["TimeValue"]) -> None:
        """
        Set borTimeL2 with validation.

        Args:
            value: The borTimeL2 to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._borTimeL2 = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"borTimeL2 must be TimeValue or None, got {type(value).__name__}"
            )
        self._borTimeL2 = value
        # This attribute defines the duration of the bus-off event in seconds.
        self._borTimeTx: Optional["TimeValue"] = None

    @property
    def bor_time_tx(self) -> Optional["TimeValue"]:
        """Get borTimeTx (Pythonic accessor)."""
        return self._borTimeTx

    @bor_time_tx.setter
    def bor_time_tx(self, value: Optional["TimeValue"]) -> None:
        """
        Set borTimeTx with validation.

        Args:
            value: The borTimeTx to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._borTimeTx = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"borTimeTx must be TimeValue or None, got {type(value).__name__}"
            )
        self._borTimeTx = value
        # This attribute defines the cycle time of the function Can in seconds.
        self._mainFunction: Optional["TimeValue"] = None

    @property
    def main_function(self) -> Optional["TimeValue"]:
        """Get mainFunction (Pythonic accessor)."""
        return self._mainFunction

    @main_function.setter
    def main_function(self, value: Optional["TimeValue"]) -> None:
        """
        Set mainFunction with validation.

        Args:
            value: The mainFunction to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mainFunction = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"mainFunction must be TimeValue or None, got {type(value).__name__}"
            )
        self._mainFunction = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBorCounterL1To(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for borCounterL1To.

        Returns:
            The borCounterL1To value

        Note:
            Delegates to bor_counter_l1_to property (CODING_RULE_V2_00017)
        """
        return self.bor_counter_l1_to  # Delegates to property

    def setBorCounterL1To(self, value: "PositiveInteger") -> "CanClusterBusOffRecovery":
        """
        AUTOSAR-compliant setter for borCounterL1To with method chaining.

        Args:
            value: The borCounterL1To to set

        Returns:
            self for method chaining

        Note:
            Delegates to bor_counter_l1_to property setter (gets validation automatically)
        """
        self.bor_counter_l1_to = value  # Delegates to property setter
        return self

    def getBorTimeL1(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for borTimeL1.

        Returns:
            The borTimeL1 value

        Note:
            Delegates to bor_time_l1 property (CODING_RULE_V2_00017)
        """
        return self.bor_time_l1  # Delegates to property

    def setBorTimeL1(self, value: "TimeValue") -> "CanClusterBusOffRecovery":
        """
        AUTOSAR-compliant setter for borTimeL1 with method chaining.

        Args:
            value: The borTimeL1 to set

        Returns:
            self for method chaining

        Note:
            Delegates to bor_time_l1 property setter (gets validation automatically)
        """
        self.bor_time_l1 = value  # Delegates to property setter
        return self

    def getBorTimeL2(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for borTimeL2.

        Returns:
            The borTimeL2 value

        Note:
            Delegates to bor_time_l2 property (CODING_RULE_V2_00017)
        """
        return self.bor_time_l2  # Delegates to property

    def setBorTimeL2(self, value: "TimeValue") -> "CanClusterBusOffRecovery":
        """
        AUTOSAR-compliant setter for borTimeL2 with method chaining.

        Args:
            value: The borTimeL2 to set

        Returns:
            self for method chaining

        Note:
            Delegates to bor_time_l2 property setter (gets validation automatically)
        """
        self.bor_time_l2 = value  # Delegates to property setter
        return self

    def getBorTimeTx(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for borTimeTx.

        Returns:
            The borTimeTx value

        Note:
            Delegates to bor_time_tx property (CODING_RULE_V2_00017)
        """
        return self.bor_time_tx  # Delegates to property

    def setBorTimeTx(self, value: "TimeValue") -> "CanClusterBusOffRecovery":
        """
        AUTOSAR-compliant setter for borTimeTx with method chaining.

        Args:
            value: The borTimeTx to set

        Returns:
            self for method chaining

        Note:
            Delegates to bor_time_tx property setter (gets validation automatically)
        """
        self.bor_time_tx = value  # Delegates to property setter
        return self

    def getMainFunction(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for mainFunction.

        Returns:
            The mainFunction value

        Note:
            Delegates to main_function property (CODING_RULE_V2_00017)
        """
        return self.main_function  # Delegates to property

    def setMainFunction(self, value: "TimeValue") -> "CanClusterBusOffRecovery":
        """
        AUTOSAR-compliant setter for mainFunction with method chaining.

        Args:
            value: The mainFunction to set

        Returns:
            self for method chaining

        Note:
            Delegates to main_function property setter (gets validation automatically)
        """
        self.main_function = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bor_counter_l1_to(self, value: Optional["PositiveInteger"]) -> "CanClusterBusOffRecovery":
        """
        Set borCounterL1To and return self for chaining.

        Args:
            value: The borCounterL1To to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bor_counter_l1_to("value")
        """
        self.bor_counter_l1_to = value  # Use property setter (gets validation)
        return self

    def with_bor_time_l1(self, value: Optional["TimeValue"]) -> "CanClusterBusOffRecovery":
        """
        Set borTimeL1 and return self for chaining.

        Args:
            value: The borTimeL1 to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bor_time_l1("value")
        """
        self.bor_time_l1 = value  # Use property setter (gets validation)
        return self

    def with_bor_time_l2(self, value: Optional["TimeValue"]) -> "CanClusterBusOffRecovery":
        """
        Set borTimeL2 and return self for chaining.

        Args:
            value: The borTimeL2 to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bor_time_l2("value")
        """
        self.bor_time_l2 = value  # Use property setter (gets validation)
        return self

    def with_bor_time_tx(self, value: Optional["TimeValue"]) -> "CanClusterBusOffRecovery":
        """
        Set borTimeTx and return self for chaining.

        Args:
            value: The borTimeTx to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bor_time_tx("value")
        """
        self.bor_time_tx = value  # Use property setter (gets validation)
        return self

    def with_main_function(self, value: Optional["TimeValue"]) -> "CanClusterBusOffRecovery":
        """
        Set mainFunction and return self for chaining.

        Args:
            value: The mainFunction to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_main_function("value")
        """
        self.main_function = value  # Use property setter (gets validation)
        return self
