from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class CouplingPortRatePolicy(ARObject):
    """
    Defines a rate policy on a CouplingPort.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::CouplingPortRatePolicy

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 124, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Amount of data in bytes (excluding header information) be received to define
        # the rate policy.
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
        # Defines the action to be performed when this rate policy violated.
        self._policyAction: Optional["CouplingPortRatePolicy"] = None

    @property
    def policy_action(self) -> Optional["CouplingPortRatePolicy"]:
        """Get policyAction (Pythonic accessor)."""
        return self._policyAction

    @policy_action.setter
    def policy_action(self, value: Optional["CouplingPortRatePolicy"]) -> None:
        """
        Set policyAction with validation.

        Args:
            value: The policyAction to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._policyAction = None
            return

        if not isinstance(value, CouplingPortRatePolicy):
            raise TypeError(
                f"policyAction must be CouplingPortRatePolicy or None, got {type(value).__name__}"
            )
        self._policyAction = value
        # Defines the priority which this rate policy shall be limited no priority is
        # given this rate policy is not considering.
        self._priority: Optional["PositiveInteger"] = None

    @property
    def priority(self) -> Optional["PositiveInteger"]:
        """Get priority (Pythonic accessor)."""
        return self._priority

    @priority.setter
    def priority(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set priority with validation.

        Args:
            value: The priority to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._priority = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"priority must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._priority = value
        # Time interval used to define the base of the rate policy.
        self._timeInterval: Optional["TimeValue"] = None

    @property
    def time_interval(self) -> Optional["TimeValue"]:
        """Get timeInterval (Pythonic accessor)."""
        return self._timeInterval

    @time_interval.setter
    def time_interval(self, value: Optional["TimeValue"]) -> None:
        """
        Set timeInterval with validation.

        Args:
            value: The timeInterval to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeInterval = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeInterval must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeInterval = value
        # Defines the VLANs this rate policy shall be limited on.
        # If VLAN is given this rate policy is not considering VLAN.
        self._vLan: List["EthernetPhysical"] = []

    @property
    def v_lan(self) -> List["EthernetPhysical"]:
        """Get vLan (Pythonic accessor)."""
        return self._vLan

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

    def setDataLength(self, value: "PositiveInteger") -> "CouplingPortRatePolicy":
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

    def getPolicyAction(self) -> "CouplingPortRatePolicy":
        """
        AUTOSAR-compliant getter for policyAction.

        Returns:
            The policyAction value

        Note:
            Delegates to policy_action property (CODING_RULE_V2_00017)
        """
        return self.policy_action  # Delegates to property

    def setPolicyAction(self, value: "CouplingPortRatePolicy") -> "CouplingPortRatePolicy":
        """
        AUTOSAR-compliant setter for policyAction with method chaining.

        Args:
            value: The policyAction to set

        Returns:
            self for method chaining

        Note:
            Delegates to policy_action property setter (gets validation automatically)
        """
        self.policy_action = value  # Delegates to property setter
        return self

    def getPriority(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for priority.

        Returns:
            The priority value

        Note:
            Delegates to priority property (CODING_RULE_V2_00017)
        """
        return self.priority  # Delegates to property

    def setPriority(self, value: "PositiveInteger") -> "CouplingPortRatePolicy":
        """
        AUTOSAR-compliant setter for priority with method chaining.

        Args:
            value: The priority to set

        Returns:
            self for method chaining

        Note:
            Delegates to priority property setter (gets validation automatically)
        """
        self.priority = value  # Delegates to property setter
        return self

    def getTimeInterval(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for timeInterval.

        Returns:
            The timeInterval value

        Note:
            Delegates to time_interval property (CODING_RULE_V2_00017)
        """
        return self.time_interval  # Delegates to property

    def setTimeInterval(self, value: "TimeValue") -> "CouplingPortRatePolicy":
        """
        AUTOSAR-compliant setter for timeInterval with method chaining.

        Args:
            value: The timeInterval to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_interval property setter (gets validation automatically)
        """
        self.time_interval = value  # Delegates to property setter
        return self

    def getVLan(self) -> List["EthernetPhysical"]:
        """
        AUTOSAR-compliant getter for vLan.

        Returns:
            The vLan value

        Note:
            Delegates to v_lan property (CODING_RULE_V2_00017)
        """
        return self.v_lan  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_length(self, value: Optional["PositiveInteger"]) -> "CouplingPortRatePolicy":
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

    def with_policy_action(self, value: Optional["CouplingPortRatePolicy"]) -> "CouplingPortRatePolicy":
        """
        Set policyAction and return self for chaining.

        Args:
            value: The policyAction to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_policy_action("value")
        """
        self.policy_action = value  # Use property setter (gets validation)
        return self

    def with_priority(self, value: Optional["PositiveInteger"]) -> "CouplingPortRatePolicy":
        """
        Set priority and return self for chaining.

        Args:
            value: The priority to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_priority("value")
        """
        self.priority = value  # Use property setter (gets validation)
        return self

    def with_time_interval(self, value: Optional["TimeValue"]) -> "CouplingPortRatePolicy":
        """
        Set timeInterval and return self for chaining.

        Args:
            value: The timeInterval to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_interval("value")
        """
        self.time_interval = value  # Use property setter (gets validation)
        return self
