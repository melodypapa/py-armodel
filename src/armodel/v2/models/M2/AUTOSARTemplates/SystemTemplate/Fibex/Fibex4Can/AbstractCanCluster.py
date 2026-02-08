from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    CanClusterBusOff,
    PositiveUnlimitedInteger,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class AbstractCanCluster(ARObject, ABC):
    """
    Abstract class that is used to collect the common TtCAN, J1939 and CAN
    Cluster attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology::AbstractCanCluster

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 62, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is AbstractCanCluster:
            raise TypeError("AbstractCanCluster is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # CAN bus off monitoring / recovery at system level.
        self._busOffRecovery: Optional["CanClusterBusOff"] = None

    @property
    def bus_off_recovery(self) -> Optional["CanClusterBusOff"]:
        """Get busOffRecovery (Pythonic accessor)."""
        return self._busOffRecovery

    @bus_off_recovery.setter
    def bus_off_recovery(self, value: Optional["CanClusterBusOff"]) -> None:
        """
        Set busOffRecovery with validation.

        Args:
            value: The busOffRecovery to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._busOffRecovery = None
            return

        if not isinstance(value, CanClusterBusOff):
            raise TypeError(
                f"busOffRecovery must be CanClusterBusOff or None, got {type(value).__name__}"
            )
        self._busOffRecovery = value
        # Specifies the data segment baud rate of the controller in.
        self._canFdBaudrate: Optional["PositiveUnlimitedInteger"] = None

    @property
    def can_fd_baudrate(self) -> Optional["PositiveUnlimitedInteger"]:
        """Get canFdBaudrate (Pythonic accessor)."""
        return self._canFdBaudrate

    @can_fd_baudrate.setter
    def can_fd_baudrate(self, value: Optional["PositiveUnlimitedInteger"]) -> None:
        """
        Set canFdBaudrate with validation.

        Args:
            value: The canFdBaudrate to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._canFdBaudrate = None
            return

        if not isinstance(value, PositiveUnlimitedInteger):
            raise TypeError(
                f"canFdBaudrate must be PositiveUnlimitedInteger or None, got {type(value).__name__}"
            )
        self._canFdBaudrate = value
        # Specifies the data segment baud rate of the CAN XL bits/s.
        self._canXlBaudrate: Optional["PositiveUnlimitedInteger"] = None

    @property
    def can_xl_baudrate(self) -> Optional["PositiveUnlimitedInteger"]:
        """Get canXlBaudrate (Pythonic accessor)."""
        return self._canXlBaudrate

    @can_xl_baudrate.setter
    def can_xl_baudrate(self, value: Optional["PositiveUnlimitedInteger"]) -> None:
        """
        Set canXlBaudrate with validation.

        Args:
            value: The canXlBaudrate to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._canXlBaudrate = None
            return

        if not isinstance(value, PositiveUnlimitedInteger):
            raise TypeError(
                f"canXlBaudrate must be PositiveUnlimitedInteger or None, got {type(value).__name__}"
            )
        self._canXlBaudrate = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBusOffRecovery(self) -> "CanClusterBusOff":
        """
        AUTOSAR-compliant getter for busOffRecovery.

        Returns:
            The busOffRecovery value

        Note:
            Delegates to bus_off_recovery property (CODING_RULE_V2_00017)
        """
        return self.bus_off_recovery  # Delegates to property

    def setBusOffRecovery(self, value: "CanClusterBusOff") -> "AbstractCanCluster":
        """
        AUTOSAR-compliant setter for busOffRecovery with method chaining.

        Args:
            value: The busOffRecovery to set

        Returns:
            self for method chaining

        Note:
            Delegates to bus_off_recovery property setter (gets validation automatically)
        """
        self.bus_off_recovery = value  # Delegates to property setter
        return self

    def getCanFdBaudrate(self) -> "PositiveUnlimitedInteger":
        """
        AUTOSAR-compliant getter for canFdBaudrate.

        Returns:
            The canFdBaudrate value

        Note:
            Delegates to can_fd_baudrate property (CODING_RULE_V2_00017)
        """
        return self.can_fd_baudrate  # Delegates to property

    def setCanFdBaudrate(self, value: "PositiveUnlimitedInteger") -> "AbstractCanCluster":
        """
        AUTOSAR-compliant setter for canFdBaudrate with method chaining.

        Args:
            value: The canFdBaudrate to set

        Returns:
            self for method chaining

        Note:
            Delegates to can_fd_baudrate property setter (gets validation automatically)
        """
        self.can_fd_baudrate = value  # Delegates to property setter
        return self

    def getCanXlBaudrate(self) -> "PositiveUnlimitedInteger":
        """
        AUTOSAR-compliant getter for canXlBaudrate.

        Returns:
            The canXlBaudrate value

        Note:
            Delegates to can_xl_baudrate property (CODING_RULE_V2_00017)
        """
        return self.can_xl_baudrate  # Delegates to property

    def setCanXlBaudrate(self, value: "PositiveUnlimitedInteger") -> "AbstractCanCluster":
        """
        AUTOSAR-compliant setter for canXlBaudrate with method chaining.

        Args:
            value: The canXlBaudrate to set

        Returns:
            self for method chaining

        Note:
            Delegates to can_xl_baudrate property setter (gets validation automatically)
        """
        self.can_xl_baudrate = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bus_off_recovery(self, value: Optional["CanClusterBusOff"]) -> "AbstractCanCluster":
        """
        Set busOffRecovery and return self for chaining.

        Args:
            value: The busOffRecovery to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bus_off_recovery("value")
        """
        self.bus_off_recovery = value  # Use property setter (gets validation)
        return self

    def with_can_fd_baudrate(self, value: Optional["PositiveUnlimitedInteger"]) -> "AbstractCanCluster":
        """
        Set canFdBaudrate and return self for chaining.

        Args:
            value: The canFdBaudrate to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_can_fd_baudrate("value")
        """
        self.can_fd_baudrate = value  # Use property setter (gets validation)
        return self

    def with_can_xl_baudrate(self, value: Optional["PositiveUnlimitedInteger"]) -> "AbstractCanCluster":
        """
        Set canXlBaudrate and return self for chaining.

        Args:
            value: The canXlBaudrate to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_can_xl_baudrate("value")
        """
        self.can_xl_baudrate = value  # Use property setter (gets validation)
        return self
