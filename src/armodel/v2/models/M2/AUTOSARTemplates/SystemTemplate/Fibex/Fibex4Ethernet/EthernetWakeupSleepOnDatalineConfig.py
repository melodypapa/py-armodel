from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class EthernetWakeupSleepOnDatalineConfig(Identifiable):
    """
    EthernetWakeupSleepOnDatalineConfigSet is the main element that aggregates
    different config set regarding the wakeup and sleep on data line. An
    EthernetWakeupSleepOnDatalineConfigSet could aggregate multiple different
    configurations regarding the wakeup and sleep on dataline
    (EthernetWakeupSleepOnDatalineConfig).

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 158, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Delay in seconds to perform a sleep request if the hardware (PHY) detect a
                # pending wake-up.
        # This to avoid the race condition, if a sleep was a wake-up of a neighboring
                # PHY was a local wake-up connection (e.
        # g.
        # I/O pin).
        self._sleepMode: Optional["TimeValue"] = None

    @property
    def sleep_mode(self) -> Optional["TimeValue"]:
        """Get sleepMode (Pythonic accessor)."""
        return self._sleepMode

    @sleep_mode.setter
    def sleep_mode(self, value: Optional["TimeValue"]) -> None:
        """
        Set sleepMode with validation.

        Args:
            value: The sleepMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sleepMode = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"sleepMode must be TimeValue or None, got {type(value).__name__}"
            )
        self._sleepMode = value
        # Delay in seconds for a repetition of a sleep request.
        # This used to retry a synchronized shutdown of the Ethernet hardware (PHY) of
                # the link partner.
        self._sleepRepetition: Optional["TimeValue"] = None

    @property
    def sleep_repetition(self) -> Optional["TimeValue"]:
        """Get sleepRepetition (Pythonic accessor)."""
        return self._sleepRepetition

    @sleep_repetition.setter
    def sleep_repetition(self, value: Optional["TimeValue"]) -> None:
        """
        Set sleepRepetition with validation.

        Args:
            value: The sleepRepetition to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sleepRepetition = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"sleepRepetition must be TimeValue or None, got {type(value).__name__}"
            )
        self._sleepRepetition = value
        # Count of repetitions for a sleep on dataline.
        # If a sleep is by the linked communication partner, the sleep is until the
                # count of repetitions exceed.
        # If count of the Ethernet hardware (PHY) transit without acknowledgement of
                # the connected link.
        self._sleep: Optional["PositiveInteger"] = None

    @property
    def sleep(self) -> Optional["PositiveInteger"]:
        """Get sleep (Pythonic accessor)."""
        return self._sleep

    @sleep.setter
    def sleep(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set sleep with validation.

        Args:
            value: The sleep to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sleep = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"sleep must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._sleep = value
        # If enabled, then a local wake-up is forwarded to the dataline (e.
        # g.
        # 100BASE-T1).
        # If disabled, then a is not forwarded to the physical dataline.
        self._wakeupForward: Optional["Boolean"] = None

    @property
    def wakeup_forward(self) -> Optional["Boolean"]:
        """Get wakeupForward (Pythonic accessor)."""
        return self._wakeupForward

    @wakeup_forward.setter
    def wakeup_forward(self, value: Optional["Boolean"]) -> None:
        """
        Set wakeupForward with validation.

        Args:
            value: The wakeupForward to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._wakeupForward = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"wakeupForward must be Boolean or None, got {type(value).__name__}"
            )
        self._wakeupForward = value
        # If enabled, then a local wake-up received via a local (e.
        # g.
        # I/O pin) shall be detected by the Ethernet If disabled, Ethernet hardware is
                # not a local wake-up.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._wakeupLocal: Optional["Boolean"] = None

    @property
    def wakeup_local(self) -> Optional["Boolean"]:
        """Get wakeupLocal (Pythonic accessor)."""
        return self._wakeupLocal

    @wakeup_local.setter
    def wakeup_local(self, value: Optional["Boolean"]) -> None:
        """
        Set wakeupLocal with validation.

        Args:
            value: The wakeupLocal to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._wakeupLocal = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"wakeupLocal must be Boolean or None, got {type(value).__name__}"
            )
        self._wakeupLocal = value
        # If enabled, then a remote wake-up received via the dataline (e.
        # g.
        # 100BASE-T1) shall be detected by hardware (PHY).
        # If disabled, Ethernet not reaction on a remote wake-up.
        self._wakeupRemote: Optional["Boolean"] = None

    @property
    def wakeup_remote(self) -> Optional["Boolean"]:
        """Get wakeupRemote (Pythonic accessor)."""
        return self._wakeupRemote

    @wakeup_remote.setter
    def wakeup_remote(self, value: Optional["Boolean"]) -> None:
        """
        Set wakeupRemote with validation.

        Args:
            value: The wakeupRemote to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._wakeupRemote = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"wakeupRemote must be Boolean or None, got {type(value).__name__}"
            )
        self._wakeupRemote = value
        # Count of repetitions for a wake-up.
        # This is used to the reliability in the network, such that an ECU initiates
                # the wake-up does repeat the wake-up and the probability that affected ECUs
                # receive the.
        self._wakeup: Optional["PositiveInteger"] = None

    @property
    def wakeup(self) -> Optional["PositiveInteger"]:
        """Get wakeup (Pythonic accessor)."""
        return self._wakeup

    @wakeup.setter
    def wakeup(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set wakeup with validation.

        Args:
            value: The wakeup to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._wakeup = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"wakeup must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._wakeup = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSleepMode(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for sleepMode.

        Returns:
            The sleepMode value

        Note:
            Delegates to sleep_mode property (CODING_RULE_V2_00017)
        """
        return self.sleep_mode  # Delegates to property

    def setSleepMode(self, value: "TimeValue") -> "EthernetWakeupSleepOnDatalineConfig":
        """
        AUTOSAR-compliant setter for sleepMode with method chaining.

        Args:
            value: The sleepMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to sleep_mode property setter (gets validation automatically)
        """
        self.sleep_mode = value  # Delegates to property setter
        return self

    def getSleepRepetition(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for sleepRepetition.

        Returns:
            The sleepRepetition value

        Note:
            Delegates to sleep_repetition property (CODING_RULE_V2_00017)
        """
        return self.sleep_repetition  # Delegates to property

    def setSleepRepetition(self, value: "TimeValue") -> "EthernetWakeupSleepOnDatalineConfig":
        """
        AUTOSAR-compliant setter for sleepRepetition with method chaining.

        Args:
            value: The sleepRepetition to set

        Returns:
            self for method chaining

        Note:
            Delegates to sleep_repetition property setter (gets validation automatically)
        """
        self.sleep_repetition = value  # Delegates to property setter
        return self

    def getSleep(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for sleep.

        Returns:
            The sleep value

        Note:
            Delegates to sleep property (CODING_RULE_V2_00017)
        """
        return self.sleep  # Delegates to property

    def setSleep(self, value: "PositiveInteger") -> "EthernetWakeupSleepOnDatalineConfig":
        """
        AUTOSAR-compliant setter for sleep with method chaining.

        Args:
            value: The sleep to set

        Returns:
            self for method chaining

        Note:
            Delegates to sleep property setter (gets validation automatically)
        """
        self.sleep = value  # Delegates to property setter
        return self

    def getWakeupForward(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for wakeupForward.

        Returns:
            The wakeupForward value

        Note:
            Delegates to wakeup_forward property (CODING_RULE_V2_00017)
        """
        return self.wakeup_forward  # Delegates to property

    def setWakeupForward(self, value: "Boolean") -> "EthernetWakeupSleepOnDatalineConfig":
        """
        AUTOSAR-compliant setter for wakeupForward with method chaining.

        Args:
            value: The wakeupForward to set

        Returns:
            self for method chaining

        Note:
            Delegates to wakeup_forward property setter (gets validation automatically)
        """
        self.wakeup_forward = value  # Delegates to property setter
        return self

    def getWakeupLocal(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for wakeupLocal.

        Returns:
            The wakeupLocal value

        Note:
            Delegates to wakeup_local property (CODING_RULE_V2_00017)
        """
        return self.wakeup_local  # Delegates to property

    def setWakeupLocal(self, value: "Boolean") -> "EthernetWakeupSleepOnDatalineConfig":
        """
        AUTOSAR-compliant setter for wakeupLocal with method chaining.

        Args:
            value: The wakeupLocal to set

        Returns:
            self for method chaining

        Note:
            Delegates to wakeup_local property setter (gets validation automatically)
        """
        self.wakeup_local = value  # Delegates to property setter
        return self

    def getWakeupRemote(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for wakeupRemote.

        Returns:
            The wakeupRemote value

        Note:
            Delegates to wakeup_remote property (CODING_RULE_V2_00017)
        """
        return self.wakeup_remote  # Delegates to property

    def setWakeupRemote(self, value: "Boolean") -> "EthernetWakeupSleepOnDatalineConfig":
        """
        AUTOSAR-compliant setter for wakeupRemote with method chaining.

        Args:
            value: The wakeupRemote to set

        Returns:
            self for method chaining

        Note:
            Delegates to wakeup_remote property setter (gets validation automatically)
        """
        self.wakeup_remote = value  # Delegates to property setter
        return self

    def getWakeup(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for wakeup.

        Returns:
            The wakeup value

        Note:
            Delegates to wakeup property (CODING_RULE_V2_00017)
        """
        return self.wakeup  # Delegates to property

    def setWakeup(self, value: "PositiveInteger") -> "EthernetWakeupSleepOnDatalineConfig":
        """
        AUTOSAR-compliant setter for wakeup with method chaining.

        Args:
            value: The wakeup to set

        Returns:
            self for method chaining

        Note:
            Delegates to wakeup property setter (gets validation automatically)
        """
        self.wakeup = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sleep_mode(self, value: Optional["TimeValue"]) -> "EthernetWakeupSleepOnDatalineConfig":
        """
        Set sleepMode and return self for chaining.

        Args:
            value: The sleepMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sleep_mode("value")
        """
        self.sleep_mode = value  # Use property setter (gets validation)
        return self

    def with_sleep_repetition(self, value: Optional["TimeValue"]) -> "EthernetWakeupSleepOnDatalineConfig":
        """
        Set sleepRepetition and return self for chaining.

        Args:
            value: The sleepRepetition to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sleep_repetition("value")
        """
        self.sleep_repetition = value  # Use property setter (gets validation)
        return self

    def with_sleep(self, value: Optional["PositiveInteger"]) -> "EthernetWakeupSleepOnDatalineConfig":
        """
        Set sleep and return self for chaining.

        Args:
            value: The sleep to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sleep("value")
        """
        self.sleep = value  # Use property setter (gets validation)
        return self

    def with_wakeup_forward(self, value: Optional["Boolean"]) -> "EthernetWakeupSleepOnDatalineConfig":
        """
        Set wakeupForward and return self for chaining.

        Args:
            value: The wakeupForward to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_wakeup_forward("value")
        """
        self.wakeup_forward = value  # Use property setter (gets validation)
        return self

    def with_wakeup_local(self, value: Optional["Boolean"]) -> "EthernetWakeupSleepOnDatalineConfig":
        """
        Set wakeupLocal and return self for chaining.

        Args:
            value: The wakeupLocal to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_wakeup_local("value")
        """
        self.wakeup_local = value  # Use property setter (gets validation)
        return self

    def with_wakeup_remote(self, value: Optional["Boolean"]) -> "EthernetWakeupSleepOnDatalineConfig":
        """
        Set wakeupRemote and return self for chaining.

        Args:
            value: The wakeupRemote to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_wakeup_remote("value")
        """
        self.wakeup_remote = value  # Use property setter (gets validation)
        return self

    def with_wakeup(self, value: Optional["PositiveInteger"]) -> "EthernetWakeupSleepOnDatalineConfig":
        """
        Set wakeup and return self for chaining.

        Args:
            value: The wakeup to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_wakeup("value")
        """
        self.wakeup = value  # Use property setter (gets validation)
        return self
