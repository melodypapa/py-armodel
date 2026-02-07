from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class CanCommunicationConnector(AbstractCanCommunicationConnector):
    """
    CAN bus specific communication connector attributes.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology::CanCommunicationConnector
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 74, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Bit mask for CAN Identifier used to configure the CAN for partial network
        # wakeup.
        self._pncWakeupCan: Optional["PositiveInteger"] = None

    @property
    def pnc_wakeup_can(self) -> Optional["PositiveInteger"]:
        """Get pncWakeupCan (Pythonic accessor)."""
        return self._pncWakeupCan

    @pnc_wakeup_can.setter
    def pnc_wakeup_can(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set pncWakeupCan with validation.
        
        Args:
            value: The pncWakeupCan to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pncWakeupCan = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"pncWakeupCan must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._pncWakeupCan = value
        # Bit mask for CAN Payload used to configure the CAN for partial network
        # wakeup.
        self._pncWakeup: Optional["PositiveUnlimitedInteger"] = None

    @property
    def pnc_wakeup(self) -> Optional["PositiveUnlimitedInteger"]:
        """Get pncWakeup (Pythonic accessor)."""
        return self._pncWakeup

    @pnc_wakeup.setter
    def pnc_wakeup(self, value: Optional["PositiveUnlimitedInteger"]) -> None:
        """
        Set pncWakeup with validation.
        
        Args:
            value: The pncWakeup to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pncWakeup = None
            return

        if not isinstance(value, PositiveUnlimitedInteger):
            raise TypeError(
                f"pncWakeup must be PositiveUnlimitedInteger or None, got {type(value).__name__}"
            )
        self._pncWakeup = value
        # Data Length of the remote data frame used to configure Transceiver for
        # partial network wakeup in Bytes.
        self._pncWakeupDlc: Optional["PositiveInteger"] = None

    @property
    def pnc_wakeup_dlc(self) -> Optional["PositiveInteger"]:
        """Get pncWakeupDlc (Pythonic accessor)."""
        return self._pncWakeupDlc

    @pnc_wakeup_dlc.setter
    def pnc_wakeup_dlc(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set pncWakeupDlc with validation.
        
        Args:
            value: The pncWakeupDlc to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pncWakeupDlc = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"pncWakeupDlc must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._pncWakeupDlc = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPncWakeupCan(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for pncWakeupCan.
        
        Returns:
            The pncWakeupCan value
        
        Note:
            Delegates to pnc_wakeup_can property (CODING_RULE_V2_00017)
        """
        return self.pnc_wakeup_can  # Delegates to property

    def setPncWakeupCan(self, value: "PositiveInteger") -> "CanCommunicationConnector":
        """
        AUTOSAR-compliant setter for pncWakeupCan with method chaining.
        
        Args:
            value: The pncWakeupCan to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to pnc_wakeup_can property setter (gets validation automatically)
        """
        self.pnc_wakeup_can = value  # Delegates to property setter
        return self

    def getPncWakeup(self) -> "PositiveUnlimitedInteger":
        """
        AUTOSAR-compliant getter for pncWakeup.
        
        Returns:
            The pncWakeup value
        
        Note:
            Delegates to pnc_wakeup property (CODING_RULE_V2_00017)
        """
        return self.pnc_wakeup  # Delegates to property

    def setPncWakeup(self, value: "PositiveUnlimitedInteger") -> "CanCommunicationConnector":
        """
        AUTOSAR-compliant setter for pncWakeup with method chaining.
        
        Args:
            value: The pncWakeup to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to pnc_wakeup property setter (gets validation automatically)
        """
        self.pnc_wakeup = value  # Delegates to property setter
        return self

    def getPncWakeupDlc(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for pncWakeupDlc.
        
        Returns:
            The pncWakeupDlc value
        
        Note:
            Delegates to pnc_wakeup_dlc property (CODING_RULE_V2_00017)
        """
        return self.pnc_wakeup_dlc  # Delegates to property

    def setPncWakeupDlc(self, value: "PositiveInteger") -> "CanCommunicationConnector":
        """
        AUTOSAR-compliant setter for pncWakeupDlc with method chaining.
        
        Args:
            value: The pncWakeupDlc to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to pnc_wakeup_dlc property setter (gets validation automatically)
        """
        self.pnc_wakeup_dlc = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_pnc_wakeup_can(self, value: Optional["PositiveInteger"]) -> "CanCommunicationConnector":
        """
        Set pncWakeupCan and return self for chaining.
        
        Args:
            value: The pncWakeupCan to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_pnc_wakeup_can("value")
        """
        self.pnc_wakeup_can = value  # Use property setter (gets validation)
        return self

    def with_pnc_wakeup(self, value: Optional["PositiveUnlimitedInteger"]) -> "CanCommunicationConnector":
        """
        Set pncWakeup and return self for chaining.
        
        Args:
            value: The pncWakeup to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_pnc_wakeup("value")
        """
        self.pnc_wakeup = value  # Use property setter (gets validation)
        return self

    def with_pnc_wakeup_dlc(self, value: Optional["PositiveInteger"]) -> "CanCommunicationConnector":
        """
        Set pncWakeupDlc and return self for chaining.
        
        Args:
            value: The pncWakeupDlc to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_pnc_wakeup_dlc("value")
        """
        self.pnc_wakeup_dlc = value  # Use property setter (gets validation)
        return self