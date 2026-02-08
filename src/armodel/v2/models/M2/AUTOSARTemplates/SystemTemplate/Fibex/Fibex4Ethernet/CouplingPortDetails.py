from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    CouplingPortRatePolicy,
    CouplingPortScheduler,
    CouplingPortStructural,
    CouplingPortTraffic,
    EthernetPriority,
    GlobalTimeCoupling,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class CouplingPortDetails(ARObject):
    """
    Defines details of a CouplingPort. May be used to configure the structures
    of a switch.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::CouplingPortDetails

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 121, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Collects all the structural parts at which a CouplingPort may be
        # configurable.
        self._couplingPort: List["CouplingPortStructural"] = []

    @property
    def coupling_port(self) -> List["CouplingPortStructural"]:
        """Get couplingPort (Pythonic accessor)."""
        return self._couplingPort
        # is replaced by regenerated priority.
        self._ethernetPriority: "EthernetPriority" = None

    @property
    def ethernet_priority(self) -> "EthernetPriority":
        """Get ethernetPriority (Pythonic accessor)."""
        return self._ethernetPriority

    @ethernet_priority.setter
    def ethernet_priority(self, value: "EthernetPriority") -> None:
        """
        Set ethernetPriority with validation.

        Args:
            value: The ethernetPriority to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, EthernetPriority):
            raise TypeError(
                f"ethernetPriority must be EthernetPriority, got {type(value).__name__}"
            )
        self._ethernetPriority = value
        self._ethernetTraffic: "CouplingPortTraffic" = None

    @property
    def ethernet_traffic(self) -> "CouplingPortTraffic":
        """Get ethernetTraffic (Pythonic accessor)."""
        return self._ethernetTraffic

    @ethernet_traffic.setter
    def ethernet_traffic(self, value: "CouplingPortTraffic") -> None:
        """
        Set ethernetTraffic with validation.

        Args:
            value: The ethernetTraffic to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, CouplingPortTraffic):
            raise TypeError(
                f"ethernetTraffic must be CouplingPortTraffic, got {type(value).__name__}"
            )
        self._ethernetTraffic = value
        # Specifies properties for the usage of the CouplingPort in the scope of Global
                # Time Sync.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._globalTime: Optional["GlobalTimeCoupling"] = None

    @property
    def global_time(self) -> Optional["GlobalTimeCoupling"]:
        """Get globalTime (Pythonic accessor)."""
        return self._globalTime

    @global_time.setter
    def global_time(self, value: Optional["GlobalTimeCoupling"]) -> None:
        """
        Set globalTime with validation.

        Args:
            value: The globalTime to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._globalTime = None
            return

        if not isinstance(value, GlobalTimeCoupling):
            raise TypeError(
                f"globalTime must be GlobalTimeCoupling or None, got {type(value).__name__}"
            )
        self._globalTime = value
        # Defines which CouplingPortScheduler is the last in the port structure.
        self._lastEgress: Optional["CouplingPortScheduler"] = None

    @property
    def last_egress(self) -> Optional["CouplingPortScheduler"]:
        """Get lastEgress (Pythonic accessor)."""
        return self._lastEgress

    @last_egress.setter
    def last_egress(self, value: Optional["CouplingPortScheduler"]) -> None:
        """
        Set lastEgress with validation.

        Args:
            value: The lastEgress to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._lastEgress = None
            return

        if not isinstance(value, CouplingPortScheduler):
            raise TypeError(
                f"lastEgress must be CouplingPortScheduler or None, got {type(value).__name__}"
            )
        self._lastEgress = value
        # Rate policies to be applied for this CouplingPort.
        self._ratePolicy: List["CouplingPortRatePolicy"] = []

    @property
    def rate_policy(self) -> List["CouplingPortRatePolicy"]:
        """Get ratePolicy (Pythonic accessor)."""
        return self._ratePolicy

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCouplingPort(self) -> List["CouplingPortStructural"]:
        """
        AUTOSAR-compliant getter for couplingPort.

        Returns:
            The couplingPort value

        Note:
            Delegates to coupling_port property (CODING_RULE_V2_00017)
        """
        return self.coupling_port  # Delegates to property

    def getEthernetPriority(self) -> "EthernetPriority":
        """
        AUTOSAR-compliant getter for ethernetPriority.

        Returns:
            The ethernetPriority value

        Note:
            Delegates to ethernet_priority property (CODING_RULE_V2_00017)
        """
        return self.ethernet_priority  # Delegates to property

    def setEthernetPriority(self, value: "EthernetPriority") -> "CouplingPortDetails":
        """
        AUTOSAR-compliant setter for ethernetPriority with method chaining.

        Args:
            value: The ethernetPriority to set

        Returns:
            self for method chaining

        Note:
            Delegates to ethernet_priority property setter (gets validation automatically)
        """
        self.ethernet_priority = value  # Delegates to property setter
        return self

    def getEthernetTraffic(self) -> "CouplingPortTraffic":
        """
        AUTOSAR-compliant getter for ethernetTraffic.

        Returns:
            The ethernetTraffic value

        Note:
            Delegates to ethernet_traffic property (CODING_RULE_V2_00017)
        """
        return self.ethernet_traffic  # Delegates to property

    def setEthernetTraffic(self, value: "CouplingPortTraffic") -> "CouplingPortDetails":
        """
        AUTOSAR-compliant setter for ethernetTraffic with method chaining.

        Args:
            value: The ethernetTraffic to set

        Returns:
            self for method chaining

        Note:
            Delegates to ethernet_traffic property setter (gets validation automatically)
        """
        self.ethernet_traffic = value  # Delegates to property setter
        return self

    def getGlobalTime(self) -> "GlobalTimeCoupling":
        """
        AUTOSAR-compliant getter for globalTime.

        Returns:
            The globalTime value

        Note:
            Delegates to global_time property (CODING_RULE_V2_00017)
        """
        return self.global_time  # Delegates to property

    def setGlobalTime(self, value: "GlobalTimeCoupling") -> "CouplingPortDetails":
        """
        AUTOSAR-compliant setter for globalTime with method chaining.

        Args:
            value: The globalTime to set

        Returns:
            self for method chaining

        Note:
            Delegates to global_time property setter (gets validation automatically)
        """
        self.global_time = value  # Delegates to property setter
        return self

    def getLastEgress(self) -> "CouplingPortScheduler":
        """
        AUTOSAR-compliant getter for lastEgress.

        Returns:
            The lastEgress value

        Note:
            Delegates to last_egress property (CODING_RULE_V2_00017)
        """
        return self.last_egress  # Delegates to property

    def setLastEgress(self, value: "CouplingPortScheduler") -> "CouplingPortDetails":
        """
        AUTOSAR-compliant setter for lastEgress with method chaining.

        Args:
            value: The lastEgress to set

        Returns:
            self for method chaining

        Note:
            Delegates to last_egress property setter (gets validation automatically)
        """
        self.last_egress = value  # Delegates to property setter
        return self

    def getRatePolicy(self) -> List["CouplingPortRatePolicy"]:
        """
        AUTOSAR-compliant getter for ratePolicy.

        Returns:
            The ratePolicy value

        Note:
            Delegates to rate_policy property (CODING_RULE_V2_00017)
        """
        return self.rate_policy  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ethernet_priority(self, value: "EthernetPriority") -> "CouplingPortDetails":
        """
        Set ethernetPriority and return self for chaining.

        Args:
            value: The ethernetPriority to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ethernet_priority("value")
        """
        self.ethernet_priority = value  # Use property setter (gets validation)
        return self

    def with_ethernet_traffic(self, value: "CouplingPortTraffic") -> "CouplingPortDetails":
        """
        Set ethernetTraffic and return self for chaining.

        Args:
            value: The ethernetTraffic to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ethernet_traffic("value")
        """
        self.ethernet_traffic = value  # Use property setter (gets validation)
        return self

    def with_global_time(self, value: Optional["GlobalTimeCoupling"]) -> "CouplingPortDetails":
        """
        Set globalTime and return self for chaining.

        Args:
            value: The globalTime to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_global_time("value")
        """
        self.global_time = value  # Use property setter (gets validation)
        return self

    def with_last_egress(self, value: Optional["CouplingPortScheduler"]) -> "CouplingPortDetails":
        """
        Set lastEgress and return self for chaining.

        Args:
            value: The lastEgress to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_last_egress("value")
        """
        self.last_egress = value  # Use property setter (gets validation)
        return self
