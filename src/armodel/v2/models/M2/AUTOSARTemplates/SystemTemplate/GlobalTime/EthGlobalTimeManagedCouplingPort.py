from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    CouplingPort,
    GlobalTimePortRole,
    TimeValue,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class EthGlobalTimeManagedCouplingPort(ARObject):
    """
    Specifies a CouplingPort which is managed by an Ethernet Global Time Domain.

    Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime::ETH::EthGlobalTimeManagedCouplingPort

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 874, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines which CouplingPort is managed by this EthGlobal.
        self._couplingPort: Optional["CouplingPort"] = None

    @property
    def coupling_port(self) -> Optional["CouplingPort"]:
        """Get couplingPort (Pythonic accessor)."""
        return self._couplingPort

    @coupling_port.setter
    def coupling_port(self, value: Optional["CouplingPort"]) -> None:
        """
        Set couplingPort with validation.

        Args:
            value: The couplingPort to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._couplingPort = None
            return

        if not isinstance(value, CouplingPort):
            raise TypeError(
                f"couplingPort must be CouplingPort or None, got {type(value).__name__}"
            )
        self._couplingPort = value
        # This attribute defines the port behavior.
        self._globalTimePort: Optional["GlobalTimePortRole"] = None

    @property
    def global_time_port(self) -> Optional["GlobalTimePortRole"]:
        """Get globalTimePort (Pythonic accessor)."""
        return self._globalTimePort

    @global_time_port.setter
    def global_time_port(self, value: Optional["GlobalTimePortRole"]) -> None:
        """
        Set globalTimePort with validation.

        Args:
            value: The globalTimePort to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._globalTimePort = None
            return

        if not isinstance(value, GlobalTimePortRole):
            raise TypeError(
                f"globalTimePort must be GlobalTimePortRole or None, got {type(value).__name__}"
            )
        self._globalTimePort = value
        # This attribute defines the TX period in seconds 2090 Document ID 63:
        # AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._globalTimeTxPeriod: Optional["TimeValue"] = None

    @property
    def global_time_tx_period(self) -> Optional["TimeValue"]:
        """Get globalTimeTxPeriod (Pythonic accessor)."""
        return self._globalTimeTxPeriod

    @global_time_tx_period.setter
    def global_time_tx_period(self, value: Optional["TimeValue"]) -> None:
        """
        Set globalTimeTxPeriod with validation.

        Args:
            value: The globalTimeTxPeriod to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._globalTimeTxPeriod = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"globalTimeTxPeriod must be TimeValue or None, got {type(value).__name__}"
            )
        self._globalTimeTxPeriod = value
        # Threshold for calculated Pdelay.
        # If a measured Pdelay pdelayLatencyThreshold, the measured Pdelay discarded.
        self._pdelayLatency: Optional["TimeValue"] = None

    @property
    def pdelay_latency(self) -> Optional["TimeValue"]:
        """Get pdelayLatency (Pythonic accessor)."""
        return self._pdelayLatency

    @pdelay_latency.setter
    def pdelay_latency(self, value: Optional["TimeValue"]) -> None:
        """
        Set pdelayLatency with validation.

        Args:
            value: The pdelayLatency to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pdelayLatency = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"pdelayLatency must be TimeValue or None, got {type(value).__name__}"
            )
        self._pdelayLatency = value
        # Defines the period for the pdelay request messages.
        self._pdelayRequest: Optional["TimeValue"] = None

    @property
    def pdelay_request(self) -> Optional["TimeValue"]:
        """Get pdelayRequest (Pythonic accessor)."""
        return self._pdelayRequest

    @pdelay_request.setter
    def pdelay_request(self, value: Optional["TimeValue"]) -> None:
        """
        Set pdelayRequest with validation.

        Args:
            value: The pdelayRequest to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pdelayRequest = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"pdelayRequest must be TimeValue or None, got {type(value).__name__}"
            )
        self._pdelayRequest = value
        # Timeout value for Pdelay_Resp and Pdelay_Resp_ after a Pdelay_Req has been
                # transmitted resp.
        # Pdelay_Resp has been received.
        # A value of 0 or not attribute deactivates this timeout observation.
        self._pdelayRespAnd: Optional["TimeValue"] = None

    @property
    def pdelay_resp_and(self) -> Optional["TimeValue"]:
        """Get pdelayRespAnd (Pythonic accessor)."""
        return self._pdelayRespAnd

    @pdelay_resp_and.setter
    def pdelay_resp_and(self, value: Optional["TimeValue"]) -> None:
        """
        Set pdelayRespAnd with validation.

        Args:
            value: The pdelayRespAnd to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pdelayRespAnd = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"pdelayRespAnd must be TimeValue or None, got {type(value).__name__}"
            )
        self._pdelayRespAnd = value
        # Defines whether PDELAY RESPONSE and PDELAY FOLLOW UP shall be sent on this
        # Coupling.
        self._pdelay: Optional["Boolean"] = None

    @property
    def pdelay(self) -> Optional["Boolean"]:
        """Get pdelay (Pythonic accessor)."""
        return self._pdelay

    @pdelay.setter
    def pdelay(self, value: Optional["Boolean"]) -> None:
        """
        Set pdelay with validation.

        Args:
            value: The pdelay to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pdelay = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"pdelay must be Boolean or None, got {type(value).__name__}"
            )
        self._pdelay = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCouplingPort(self) -> "CouplingPort":
        """
        AUTOSAR-compliant getter for couplingPort.

        Returns:
            The couplingPort value

        Note:
            Delegates to coupling_port property (CODING_RULE_V2_00017)
        """
        return self.coupling_port  # Delegates to property

    def setCouplingPort(self, value: "CouplingPort") -> "EthGlobalTimeManagedCouplingPort":
        """
        AUTOSAR-compliant setter for couplingPort with method chaining.

        Args:
            value: The couplingPort to set

        Returns:
            self for method chaining

        Note:
            Delegates to coupling_port property setter (gets validation automatically)
        """
        self.coupling_port = value  # Delegates to property setter
        return self

    def getGlobalTimePort(self) -> "GlobalTimePortRole":
        """
        AUTOSAR-compliant getter for globalTimePort.

        Returns:
            The globalTimePort value

        Note:
            Delegates to global_time_port property (CODING_RULE_V2_00017)
        """
        return self.global_time_port  # Delegates to property

    def setGlobalTimePort(self, value: "GlobalTimePortRole") -> "EthGlobalTimeManagedCouplingPort":
        """
        AUTOSAR-compliant setter for globalTimePort with method chaining.

        Args:
            value: The globalTimePort to set

        Returns:
            self for method chaining

        Note:
            Delegates to global_time_port property setter (gets validation automatically)
        """
        self.global_time_port = value  # Delegates to property setter
        return self

    def getGlobalTimeTxPeriod(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for globalTimeTxPeriod.

        Returns:
            The globalTimeTxPeriod value

        Note:
            Delegates to global_time_tx_period property (CODING_RULE_V2_00017)
        """
        return self.global_time_tx_period  # Delegates to property

    def setGlobalTimeTxPeriod(self, value: "TimeValue") -> "EthGlobalTimeManagedCouplingPort":
        """
        AUTOSAR-compliant setter for globalTimeTxPeriod with method chaining.

        Args:
            value: The globalTimeTxPeriod to set

        Returns:
            self for method chaining

        Note:
            Delegates to global_time_tx_period property setter (gets validation automatically)
        """
        self.global_time_tx_period = value  # Delegates to property setter
        return self

    def getPdelayLatency(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for pdelayLatency.

        Returns:
            The pdelayLatency value

        Note:
            Delegates to pdelay_latency property (CODING_RULE_V2_00017)
        """
        return self.pdelay_latency  # Delegates to property

    def setPdelayLatency(self, value: "TimeValue") -> "EthGlobalTimeManagedCouplingPort":
        """
        AUTOSAR-compliant setter for pdelayLatency with method chaining.

        Args:
            value: The pdelayLatency to set

        Returns:
            self for method chaining

        Note:
            Delegates to pdelay_latency property setter (gets validation automatically)
        """
        self.pdelay_latency = value  # Delegates to property setter
        return self

    def getPdelayRequest(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for pdelayRequest.

        Returns:
            The pdelayRequest value

        Note:
            Delegates to pdelay_request property (CODING_RULE_V2_00017)
        """
        return self.pdelay_request  # Delegates to property

    def setPdelayRequest(self, value: "TimeValue") -> "EthGlobalTimeManagedCouplingPort":
        """
        AUTOSAR-compliant setter for pdelayRequest with method chaining.

        Args:
            value: The pdelayRequest to set

        Returns:
            self for method chaining

        Note:
            Delegates to pdelay_request property setter (gets validation automatically)
        """
        self.pdelay_request = value  # Delegates to property setter
        return self

    def getPdelayRespAnd(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for pdelayRespAnd.

        Returns:
            The pdelayRespAnd value

        Note:
            Delegates to pdelay_resp_and property (CODING_RULE_V2_00017)
        """
        return self.pdelay_resp_and  # Delegates to property

    def setPdelayRespAnd(self, value: "TimeValue") -> "EthGlobalTimeManagedCouplingPort":
        """
        AUTOSAR-compliant setter for pdelayRespAnd with method chaining.

        Args:
            value: The pdelayRespAnd to set

        Returns:
            self for method chaining

        Note:
            Delegates to pdelay_resp_and property setter (gets validation automatically)
        """
        self.pdelay_resp_and = value  # Delegates to property setter
        return self

    def getPdelay(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for pdelay.

        Returns:
            The pdelay value

        Note:
            Delegates to pdelay property (CODING_RULE_V2_00017)
        """
        return self.pdelay  # Delegates to property

    def setPdelay(self, value: "Boolean") -> "EthGlobalTimeManagedCouplingPort":
        """
        AUTOSAR-compliant setter for pdelay with method chaining.

        Args:
            value: The pdelay to set

        Returns:
            self for method chaining

        Note:
            Delegates to pdelay property setter (gets validation automatically)
        """
        self.pdelay = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_coupling_port(self, value: Optional["CouplingPort"]) -> "EthGlobalTimeManagedCouplingPort":
        """
        Set couplingPort and return self for chaining.

        Args:
            value: The couplingPort to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_coupling_port("value")
        """
        self.coupling_port = value  # Use property setter (gets validation)
        return self

    def with_global_time_port(self, value: Optional["GlobalTimePortRole"]) -> "EthGlobalTimeManagedCouplingPort":
        """
        Set globalTimePort and return self for chaining.

        Args:
            value: The globalTimePort to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_global_time_port("value")
        """
        self.global_time_port = value  # Use property setter (gets validation)
        return self

    def with_global_time_tx_period(self, value: Optional["TimeValue"]) -> "EthGlobalTimeManagedCouplingPort":
        """
        Set globalTimeTxPeriod and return self for chaining.

        Args:
            value: The globalTimeTxPeriod to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_global_time_tx_period("value")
        """
        self.global_time_tx_period = value  # Use property setter (gets validation)
        return self

    def with_pdelay_latency(self, value: Optional["TimeValue"]) -> "EthGlobalTimeManagedCouplingPort":
        """
        Set pdelayLatency and return self for chaining.

        Args:
            value: The pdelayLatency to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pdelay_latency("value")
        """
        self.pdelay_latency = value  # Use property setter (gets validation)
        return self

    def with_pdelay_request(self, value: Optional["TimeValue"]) -> "EthGlobalTimeManagedCouplingPort":
        """
        Set pdelayRequest and return self for chaining.

        Args:
            value: The pdelayRequest to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pdelay_request("value")
        """
        self.pdelay_request = value  # Use property setter (gets validation)
        return self

    def with_pdelay_resp_and(self, value: Optional["TimeValue"]) -> "EthGlobalTimeManagedCouplingPort":
        """
        Set pdelayRespAnd and return self for chaining.

        Args:
            value: The pdelayRespAnd to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pdelay_resp_and("value")
        """
        self.pdelay_resp_and = value  # Use property setter (gets validation)
        return self

    def with_pdelay(self, value: Optional["Boolean"]) -> "EthGlobalTimeManagedCouplingPort":
        """
        Set pdelay and return self for chaining.

        Args:
            value: The pdelay to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pdelay("value")
        """
        self.pdelay = value  # Use property setter (gets validation)
        return self
