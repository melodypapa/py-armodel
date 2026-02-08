from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import Integer
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class TtcanCommunicationController(ARObject):
    """
    TTCAN bus specific communication port attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ttcan::TtcanTopology::TtcanCommunicationController

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 76, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The Appl_Watchdog_Limit shall be an 8-bit value the period for the
        # application watchdog in 256 NTUs.
        self._applWatchdog: Optional["Integer"] = None

    @property
    def appl_watchdog(self) -> Optional["Integer"]:
        """Get applWatchdog (Pythonic accessor)."""
        return self._applWatchdog

    @appl_watchdog.setter
    def appl_watchdog(self, value: Optional["Integer"]) -> None:
        """
        Set applWatchdog with validation.

        Args:
            value: The applWatchdog to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._applWatchdog = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"applWatchdog must be Integer or None, got {type(value).__name__}"
            )
        self._applWatchdog = value
        # The Expected_Tx_Trigger shall be an eight (8) bit value limits the number of
        # messages the FSE may try to one matrix cycle.
        self._expectedTx: Optional["Integer"] = None

    @property
    def expected_tx(self) -> Optional["Integer"]:
        """Get expectedTx (Pythonic accessor)."""
        return self._expectedTx

    @expected_tx.setter
    def expected_tx(self, value: Optional["Integer"]) -> None:
        """
        Set expectedTx with validation.

        Args:
            value: The expectedTx to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._expectedTx = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"expectedTx must be Integer or None, got {type(value).__name__}"
            )
        self._expectedTx = value
        # One bit shall be used to configure whether or not external synchronisation
        # will be allowed during runtime (only.
        self._externalClock: Optional["Boolean"] = None

    @property
    def external_clock(self) -> Optional["Boolean"]:
        """Get externalClock (Pythonic accessor)."""
        return self._externalClock

    @external_clock.setter
    def external_clock(self, value: Optional["Boolean"]) -> None:
        """
        Set externalClock with validation.

        Args:
            value: The externalClock to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._externalClock = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"externalClock must be Boolean or None, got {type(value).__name__}"
            )
        self._externalClock = value
        # The Initial_Ref_Offset shall be an eight (8) bit value for of
        # Ref_Trigger_Offset.
        self._initialRefOffset: Optional["Integer"] = None

    @property
    def initial_ref_offset(self) -> Optional["Integer"]:
        """Get initialRefOffset (Pythonic accessor)."""
        return self._initialRefOffset

    @initial_ref_offset.setter
    def initial_ref_offset(self, value: Optional["Integer"]) -> None:
        """
        Set initialRefOffset with validation.

        Args:
            value: The initialRefOffset to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._initialRefOffset = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"initialRefOffset must be Integer or None, got {type(value).__name__}"
            )
        self._initialRefOffset = value
        # One bit shall be used to distinguish between (potential) and time slaves.
        # This can be derived from triggers.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._master: Optional["Boolean"] = None

    @property
    def master(self) -> Optional["Boolean"]:
        """Get master (Pythonic accessor)."""
        return self._master

    @master.setter
    def master(self, value: Optional["Boolean"]) -> None:
        """
        Set master with validation.

        Args:
            value: The master to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._master = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"master must be Boolean or None, got {type(value).__name__}"
            )
        self._master = value
        # The time master priority shall contain a three bit value for priority of the
                # current time master (the last three bits identifier of the reference
                # message).
        # This can be the frame-triggering’s triggers.
        self._timeMaster: Optional["Integer"] = None

    @property
    def time_master(self) -> Optional["Integer"]:
        """Get timeMaster (Pythonic accessor)."""
        return self._timeMaster

    @time_master.setter
    def time_master(self, value: Optional["Integer"]) -> None:
        """
        Set timeMaster with validation.

        Args:
            value: The timeMaster to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeMaster = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"timeMaster must be Integer or None, got {type(value).__name__}"
            )
        self._timeMaster = value
        # One bit shall be used to distinguish between Level 1 and 2.
        self._timeTriggered: Optional["Integer"] = None

    @property
    def time_triggered(self) -> Optional["Integer"]:
        """Get timeTriggered (Pythonic accessor)."""
        return self._timeTriggered

    @time_triggered.setter
    def time_triggered(self, value: Optional["Integer"]) -> None:
        """
        Set timeTriggered with validation.

        Args:
            value: The timeTriggered to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeTriggered = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"timeTriggered must be Integer or None, got {type(value).__name__}"
            )
        self._timeTriggered = value
        # The length of the Tx_Enable window shall be a four (4) bit specifying the
        # length of the time period (1-16 bit times) in which a transmission may be.
        self._txEnable: Optional["Integer"] = None

    @property
    def tx_enable(self) -> Optional["Integer"]:
        """Get txEnable (Pythonic accessor)."""
        return self._txEnable

    @tx_enable.setter
    def tx_enable(self, value: Optional["Integer"]) -> None:
        """
        Set txEnable with validation.

        Args:
            value: The txEnable to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._txEnable = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"txEnable must be Integer or None, got {type(value).__name__}"
            )
        self._txEnable = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getApplWatchdog(self) -> "Integer":
        """
        AUTOSAR-compliant getter for applWatchdog.

        Returns:
            The applWatchdog value

        Note:
            Delegates to appl_watchdog property (CODING_RULE_V2_00017)
        """
        return self.appl_watchdog  # Delegates to property

    def setApplWatchdog(self, value: "Integer") -> "TtcanCommunicationController":
        """
        AUTOSAR-compliant setter for applWatchdog with method chaining.

        Args:
            value: The applWatchdog to set

        Returns:
            self for method chaining

        Note:
            Delegates to appl_watchdog property setter (gets validation automatically)
        """
        self.appl_watchdog = value  # Delegates to property setter
        return self

    def getExpectedTx(self) -> "Integer":
        """
        AUTOSAR-compliant getter for expectedTx.

        Returns:
            The expectedTx value

        Note:
            Delegates to expected_tx property (CODING_RULE_V2_00017)
        """
        return self.expected_tx  # Delegates to property

    def setExpectedTx(self, value: "Integer") -> "TtcanCommunicationController":
        """
        AUTOSAR-compliant setter for expectedTx with method chaining.

        Args:
            value: The expectedTx to set

        Returns:
            self for method chaining

        Note:
            Delegates to expected_tx property setter (gets validation automatically)
        """
        self.expected_tx = value  # Delegates to property setter
        return self

    def getExternalClock(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for externalClock.

        Returns:
            The externalClock value

        Note:
            Delegates to external_clock property (CODING_RULE_V2_00017)
        """
        return self.external_clock  # Delegates to property

    def setExternalClock(self, value: "Boolean") -> "TtcanCommunicationController":
        """
        AUTOSAR-compliant setter for externalClock with method chaining.

        Args:
            value: The externalClock to set

        Returns:
            self for method chaining

        Note:
            Delegates to external_clock property setter (gets validation automatically)
        """
        self.external_clock = value  # Delegates to property setter
        return self

    def getInitialRefOffset(self) -> "Integer":
        """
        AUTOSAR-compliant getter for initialRefOffset.

        Returns:
            The initialRefOffset value

        Note:
            Delegates to initial_ref_offset property (CODING_RULE_V2_00017)
        """
        return self.initial_ref_offset  # Delegates to property

    def setInitialRefOffset(self, value: "Integer") -> "TtcanCommunicationController":
        """
        AUTOSAR-compliant setter for initialRefOffset with method chaining.

        Args:
            value: The initialRefOffset to set

        Returns:
            self for method chaining

        Note:
            Delegates to initial_ref_offset property setter (gets validation automatically)
        """
        self.initial_ref_offset = value  # Delegates to property setter
        return self

    def getMaster(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for master.

        Returns:
            The master value

        Note:
            Delegates to master property (CODING_RULE_V2_00017)
        """
        return self.master  # Delegates to property

    def setMaster(self, value: "Boolean") -> "TtcanCommunicationController":
        """
        AUTOSAR-compliant setter for master with method chaining.

        Args:
            value: The master to set

        Returns:
            self for method chaining

        Note:
            Delegates to master property setter (gets validation automatically)
        """
        self.master = value  # Delegates to property setter
        return self

    def getTimeMaster(self) -> "Integer":
        """
        AUTOSAR-compliant getter for timeMaster.

        Returns:
            The timeMaster value

        Note:
            Delegates to time_master property (CODING_RULE_V2_00017)
        """
        return self.time_master  # Delegates to property

    def setTimeMaster(self, value: "Integer") -> "TtcanCommunicationController":
        """
        AUTOSAR-compliant setter for timeMaster with method chaining.

        Args:
            value: The timeMaster to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_master property setter (gets validation automatically)
        """
        self.time_master = value  # Delegates to property setter
        return self

    def getTimeTriggered(self) -> "Integer":
        """
        AUTOSAR-compliant getter for timeTriggered.

        Returns:
            The timeTriggered value

        Note:
            Delegates to time_triggered property (CODING_RULE_V2_00017)
        """
        return self.time_triggered  # Delegates to property

    def setTimeTriggered(self, value: "Integer") -> "TtcanCommunicationController":
        """
        AUTOSAR-compliant setter for timeTriggered with method chaining.

        Args:
            value: The timeTriggered to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_triggered property setter (gets validation automatically)
        """
        self.time_triggered = value  # Delegates to property setter
        return self

    def getTxEnable(self) -> "Integer":
        """
        AUTOSAR-compliant getter for txEnable.

        Returns:
            The txEnable value

        Note:
            Delegates to tx_enable property (CODING_RULE_V2_00017)
        """
        return self.tx_enable  # Delegates to property

    def setTxEnable(self, value: "Integer") -> "TtcanCommunicationController":
        """
        AUTOSAR-compliant setter for txEnable with method chaining.

        Args:
            value: The txEnable to set

        Returns:
            self for method chaining

        Note:
            Delegates to tx_enable property setter (gets validation automatically)
        """
        self.tx_enable = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_appl_watchdog(self, value: Optional["Integer"]) -> "TtcanCommunicationController":
        """
        Set applWatchdog and return self for chaining.

        Args:
            value: The applWatchdog to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_appl_watchdog("value")
        """
        self.appl_watchdog = value  # Use property setter (gets validation)
        return self

    def with_expected_tx(self, value: Optional["Integer"]) -> "TtcanCommunicationController":
        """
        Set expectedTx and return self for chaining.

        Args:
            value: The expectedTx to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_expected_tx("value")
        """
        self.expected_tx = value  # Use property setter (gets validation)
        return self

    def with_external_clock(self, value: Optional["Boolean"]) -> "TtcanCommunicationController":
        """
        Set externalClock and return self for chaining.

        Args:
            value: The externalClock to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_external_clock("value")
        """
        self.external_clock = value  # Use property setter (gets validation)
        return self

    def with_initial_ref_offset(self, value: Optional["Integer"]) -> "TtcanCommunicationController":
        """
        Set initialRefOffset and return self for chaining.

        Args:
            value: The initialRefOffset to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_initial_ref_offset("value")
        """
        self.initial_ref_offset = value  # Use property setter (gets validation)
        return self

    def with_master(self, value: Optional["Boolean"]) -> "TtcanCommunicationController":
        """
        Set master and return self for chaining.

        Args:
            value: The master to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_master("value")
        """
        self.master = value  # Use property setter (gets validation)
        return self

    def with_time_master(self, value: Optional["Integer"]) -> "TtcanCommunicationController":
        """
        Set timeMaster and return self for chaining.

        Args:
            value: The timeMaster to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_master("value")
        """
        self.time_master = value  # Use property setter (gets validation)
        return self

    def with_time_triggered(self, value: Optional["Integer"]) -> "TtcanCommunicationController":
        """
        Set timeTriggered and return self for chaining.

        Args:
            value: The timeTriggered to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_triggered("value")
        """
        self.time_triggered = value  # Use property setter (gets validation)
        return self

    def with_tx_enable(self, value: Optional["Integer"]) -> "TtcanCommunicationController":
        """
        Set txEnable and return self for chaining.

        Args:
            value: The txEnable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tx_enable("value")
        """
        self.tx_enable = value  # Use property setter (gets validation)
        return self
