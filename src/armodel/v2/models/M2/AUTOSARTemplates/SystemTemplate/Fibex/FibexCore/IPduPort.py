from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommConnectorPort


class IPduPort(CommConnectorPort):
    """
    Connectors reception or send port on the referenced channel referenced by a
    PduTriggering.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::IPduPort

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 304, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Definition of the two signal processing modes Immediate and Deferred for both
        # Tx and Rx IPdus.
        self._iPduSignal: Optional["IPduSignalProcessing"] = None

    @property
    def i_pdu_signal(self) -> Optional["IPduSignalProcessing"]:
        """Get iPduSignal (Pythonic accessor)."""
        return self._iPduSignal

    @i_pdu_signal.setter
    def i_pdu_signal(self, value: Optional["IPduSignalProcessing"]) -> None:
        """
        Set iPduSignal with validation.

        Args:
            value: The iPduSignal to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._iPduSignal = None
            return

        if not isinstance(value, IPduSignalProcessing):
            raise TypeError(
                f"iPduSignal must be IPduSignalProcessing or None, got {type(value).__name__}"
            )
        self._iPduSignal = value
        # This attribute defines the bypassing of signature or MAC verification in the
                # receiving ECU.
        # If or set to true the signature authentication or shall be performed for the
                # SecuredIPdu.
        # to false the signature authentication or MAC not be performed for the
                # SecuredIPdu.
        self._rxSecurity: Optional["Boolean"] = None

    @property
    def rx_security(self) -> Optional["Boolean"]:
        """Get rxSecurity (Pythonic accessor)."""
        return self._rxSecurity

    @rx_security.setter
    def rx_security(self, value: Optional["Boolean"]) -> None:
        """
        Set rxSecurity with validation.

        Args:
            value: The rxSecurity to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rxSecurity = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"rxSecurity must be Boolean or None, got {type(value).__name__}"
            )
        self._rxSecurity = value
        # This attribute is used to define the maximum allowed in seconds from the
                # expected timestamp for a SecuredIPdu is still deemed authentic.
        # Please this attribute is for documentation only to allow of required
                # freshness value manager upstream mapping is defined for it.
        self._timestampRx: Optional["TimeValue"] = None

    @property
    def timestamp_rx(self) -> Optional["TimeValue"]:
        """Get timestampRx (Pythonic accessor)."""
        return self._timestampRx

    @timestamp_rx.setter
    def timestamp_rx(self, value: Optional["TimeValue"]) -> None:
        """
        Set timestampRx with validation.

        Args:
            value: The timestampRx to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timestampRx = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timestampRx must be TimeValue or None, got {type(value).__name__}"
            )
        self._timestampRx = value
        # This attribute describes whether a part of AuthenticPdu in a SecuredIPdu
                # shall be passed on to the verifies and generates the Freshness.
        # The part Authentic-PDU is defined by the authData authDataFreshnessLength.
        self._useAuthData: Optional["Boolean"] = None

    @property
    def use_auth_data(self) -> Optional["Boolean"]:
        """Get useAuthData (Pythonic accessor)."""
        return self._useAuthData

    @use_auth_data.setter
    def use_auth_data(self, value: Optional["Boolean"]) -> None:
        """
        Set useAuthData with validation.

        Args:
            value: The useAuthData to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._useAuthData = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"useAuthData must be Boolean or None, got {type(value).__name__}"
            )
        self._useAuthData = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIPduSignal(self) -> "IPduSignalProcessing":
        """
        AUTOSAR-compliant getter for iPduSignal.

        Returns:
            The iPduSignal value

        Note:
            Delegates to i_pdu_signal property (CODING_RULE_V2_00017)
        """
        return self.i_pdu_signal  # Delegates to property

    def setIPduSignal(self, value: "IPduSignalProcessing") -> "IPduPort":
        """
        AUTOSAR-compliant setter for iPduSignal with method chaining.

        Args:
            value: The iPduSignal to set

        Returns:
            self for method chaining

        Note:
            Delegates to i_pdu_signal property setter (gets validation automatically)
        """
        self.i_pdu_signal = value  # Delegates to property setter
        return self

    def getRxSecurity(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for rxSecurity.

        Returns:
            The rxSecurity value

        Note:
            Delegates to rx_security property (CODING_RULE_V2_00017)
        """
        return self.rx_security  # Delegates to property

    def setRxSecurity(self, value: "Boolean") -> "IPduPort":
        """
        AUTOSAR-compliant setter for rxSecurity with method chaining.

        Args:
            value: The rxSecurity to set

        Returns:
            self for method chaining

        Note:
            Delegates to rx_security property setter (gets validation automatically)
        """
        self.rx_security = value  # Delegates to property setter
        return self

    def getTimestampRx(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for timestampRx.

        Returns:
            The timestampRx value

        Note:
            Delegates to timestamp_rx property (CODING_RULE_V2_00017)
        """
        return self.timestamp_rx  # Delegates to property

    def setTimestampRx(self, value: "TimeValue") -> "IPduPort":
        """
        AUTOSAR-compliant setter for timestampRx with method chaining.

        Args:
            value: The timestampRx to set

        Returns:
            self for method chaining

        Note:
            Delegates to timestamp_rx property setter (gets validation automatically)
        """
        self.timestamp_rx = value  # Delegates to property setter
        return self

    def getUseAuthData(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for useAuthData.

        Returns:
            The useAuthData value

        Note:
            Delegates to use_auth_data property (CODING_RULE_V2_00017)
        """
        return self.use_auth_data  # Delegates to property

    def setUseAuthData(self, value: "Boolean") -> "IPduPort":
        """
        AUTOSAR-compliant setter for useAuthData with method chaining.

        Args:
            value: The useAuthData to set

        Returns:
            self for method chaining

        Note:
            Delegates to use_auth_data property setter (gets validation automatically)
        """
        self.use_auth_data = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_i_pdu_signal(self, value: Optional["IPduSignalProcessing"]) -> "IPduPort":
        """
        Set iPduSignal and return self for chaining.

        Args:
            value: The iPduSignal to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_i_pdu_signal("value")
        """
        self.i_pdu_signal = value  # Use property setter (gets validation)
        return self

    def with_rx_security(self, value: Optional["Boolean"]) -> "IPduPort":
        """
        Set rxSecurity and return self for chaining.

        Args:
            value: The rxSecurity to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rx_security("value")
        """
        self.rx_security = value  # Use property setter (gets validation)
        return self

    def with_timestamp_rx(self, value: Optional["TimeValue"]) -> "IPduPort":
        """
        Set timestampRx and return self for chaining.

        Args:
            value: The timestampRx to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timestamp_rx("value")
        """
        self.timestamp_rx = value  # Use property setter (gets validation)
        return self

    def with_use_auth_data(self, value: Optional["Boolean"]) -> "IPduPort":
        """
        Set useAuthData and return self for chaining.

        Args:
            value: The useAuthData to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_use_auth_data("value")
        """
        self.use_auth_data = value  # Use property setter (gets validation)
        return self
