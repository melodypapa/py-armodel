from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class MacSecProps(ARObject):
    """
    This meta-class allows to configure MACsec (Media access control security)
    and the MKA (MACsec Key Agreement) for the CouplingPort (PHY).

    Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 173, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines how the Port Access Entity (PAE) is := Autostart :=
        # Manual Start.
        self._autoStart: Optional["Boolean"] = None

    @property
    def auto_start(self) -> Optional["Boolean"]:
        """Get autoStart (Pythonic accessor)."""
        return self._autoStart

    @auto_start.setter
    def auto_start(self, value: Optional["Boolean"]) -> None:
        """
        Set autoStart with validation.

        Args:
            value: The autoStart to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._autoStart = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"autoStart must be Boolean or None, got {type(value).__name__}"
            )
        self._autoStart = value
        # Properties to configure the MKA instance (KaY) for a CouplingPort (PaE).
        self._macSecKay: Optional["MacSecLocalKayProps"] = None

    @property
    def mac_sec_kay(self) -> Optional["MacSecLocalKayProps"]:
        """Get macSecKay (Pythonic accessor)."""
        return self._macSecKay

    @mac_sec_kay.setter
    def mac_sec_kay(self, value: Optional["MacSecLocalKayProps"]) -> None:
        """
        Set macSecKay with validation.

        Args:
            value: The macSecKay to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._macSecKay = None
            return

        if not isinstance(value, MacSecLocalKayProps):
            raise TypeError(
                f"macSecKay must be MacSecLocalKayProps or None, got {type(value).__name__}"
            )
        self._macSecKay = value
        # Timeout in seconds to enable the controlled port in case is set to Timeout.
        # atp.
        # Status=candidate.
        self._onFail: Optional["TimeValue"] = None

    @property
    def on_fail(self) -> Optional["TimeValue"]:
        """Get onFail (Pythonic accessor)."""
        return self._onFail

    @on_fail.setter
    def on_fail(self, value: Optional["TimeValue"]) -> None:
        """
        Set onFail with validation.

        Args:
            value: The onFail to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._onFail = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"onFail must be TimeValue or None, got {type(value).__name__}"
            )
        self._onFail = value
        # Time in seconds to trigger the rekey of an in use SAK Secure Association
                # key).
        # If set to 0, the rekey will triggered after a time span.
        self._sakRekeyTime: Optional["TimeValue"] = None

    @property
    def sak_rekey_time(self) -> Optional["TimeValue"]:
        """Get sakRekeyTime (Pythonic accessor)."""
        return self._sakRekeyTime

    @sak_rekey_time.setter
    def sak_rekey_time(self, value: Optional["TimeValue"]) -> None:
        """
        Set sakRekeyTime with validation.

        Args:
            value: The sakRekeyTime to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sakRekeyTime = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"sakRekeyTime must be TimeValue or None, got {type(value).__name__}"
            )
        self._sakRekeyTime = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAutoStart(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for autoStart.

        Returns:
            The autoStart value

        Note:
            Delegates to auto_start property (CODING_RULE_V2_00017)
        """
        return self.auto_start  # Delegates to property

    def setAutoStart(self, value: "Boolean") -> "MacSecProps":
        """
        AUTOSAR-compliant setter for autoStart with method chaining.

        Args:
            value: The autoStart to set

        Returns:
            self for method chaining

        Note:
            Delegates to auto_start property setter (gets validation automatically)
        """
        self.auto_start = value  # Delegates to property setter
        return self

    def getMacSecKay(self) -> "MacSecLocalKayProps":
        """
        AUTOSAR-compliant getter for macSecKay.

        Returns:
            The macSecKay value

        Note:
            Delegates to mac_sec_kay property (CODING_RULE_V2_00017)
        """
        return self.mac_sec_kay  # Delegates to property

    def setMacSecKay(self, value: "MacSecLocalKayProps") -> "MacSecProps":
        """
        AUTOSAR-compliant setter for macSecKay with method chaining.

        Args:
            value: The macSecKay to set

        Returns:
            self for method chaining

        Note:
            Delegates to mac_sec_kay property setter (gets validation automatically)
        """
        self.mac_sec_kay = value  # Delegates to property setter
        return self

    def getOnFail(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for onFail.

        Returns:
            The onFail value

        Note:
            Delegates to on_fail property (CODING_RULE_V2_00017)
        """
        return self.on_fail  # Delegates to property

    def setOnFail(self, value: "TimeValue") -> "MacSecProps":
        """
        AUTOSAR-compliant setter for onFail with method chaining.

        Args:
            value: The onFail to set

        Returns:
            self for method chaining

        Note:
            Delegates to on_fail property setter (gets validation automatically)
        """
        self.on_fail = value  # Delegates to property setter
        return self

    def getSakRekeyTime(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for sakRekeyTime.

        Returns:
            The sakRekeyTime value

        Note:
            Delegates to sak_rekey_time property (CODING_RULE_V2_00017)
        """
        return self.sak_rekey_time  # Delegates to property

    def setSakRekeyTime(self, value: "TimeValue") -> "MacSecProps":
        """
        AUTOSAR-compliant setter for sakRekeyTime with method chaining.

        Args:
            value: The sakRekeyTime to set

        Returns:
            self for method chaining

        Note:
            Delegates to sak_rekey_time property setter (gets validation automatically)
        """
        self.sak_rekey_time = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_auto_start(self, value: Optional["Boolean"]) -> "MacSecProps":
        """
        Set autoStart and return self for chaining.

        Args:
            value: The autoStart to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_auto_start("value")
        """
        self.auto_start = value  # Use property setter (gets validation)
        return self

    def with_mac_sec_kay(self, value: Optional["MacSecLocalKayProps"]) -> "MacSecProps":
        """
        Set macSecKay and return self for chaining.

        Args:
            value: The macSecKay to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mac_sec_kay("value")
        """
        self.mac_sec_kay = value  # Use property setter (gets validation)
        return self

    def with_on_fail(self, value: Optional["TimeValue"]) -> "MacSecProps":
        """
        Set onFail and return self for chaining.

        Args:
            value: The onFail to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_on_fail("value")
        """
        self.on_fail = value  # Use property setter (gets validation)
        return self

    def with_sak_rekey_time(self, value: Optional["TimeValue"]) -> "MacSecProps":
        """
        Set sakRekeyTime and return self for chaining.

        Args:
            value: The sakRekeyTime to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sak_rekey_time("value")
        """
        self.sak_rekey_time = value  # Use property setter (gets validation)
        return self
