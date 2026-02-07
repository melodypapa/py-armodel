from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class IPSecConfigProps(ARElement):
    """
    This element holds all the attributes for configuration of IPsec that are
    independent of specific IPsec rules.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication::IPSecConfigProps
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 572, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # AH (Authentication Header) algorithm to be used for the e.
        # g.
        # HMAC/SHA2-256.
        self._ahCipherSuite: List["String"] = []

    @property
    def ah_cipher_suite(self) -> List["String"]:
        """Get ahCipherSuite (Pythonic accessor)."""
        return self._ahCipherSuite
        # This attribute defines what to do if the peer is considered configured
        # "restart" shall be assumed.
        self._dpdAction: Optional["IPsecDpdActionEnum"] = None

    @property
    def dpd_action(self) -> Optional["IPsecDpdActionEnum"]:
        """Get dpdAction (Pythonic accessor)."""
        return self._dpdAction

    @dpd_action.setter
    def dpd_action(self, value: Optional["IPsecDpdActionEnum"]) -> None:
        """
        Set dpdAction with validation.
        
        Args:
            value: The dpdAction to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dpdAction = None
            return

        if not isinstance(value, IPsecDpdActionEnum):
            raise TypeError(
                f"dpdAction must be IPsecDpdActionEnum or None, got {type(value).__name__}"
            )
        self._dpdAction = value
        # This attribute describes the interval to check the liveness peer actively
                # using IKEv2 INFORMATIONAL DPD checking is only enforced if no ESP/AH packet
                # has been received for the delay.
        # configured the value "5 minutes" shall be assumed.
        self._dpdDelay: Optional["TimeValue"] = None

    @property
    def dpd_delay(self) -> Optional["TimeValue"]:
        """Get dpdDelay (Pythonic accessor)."""
        return self._dpdDelay

    @dpd_delay.setter
    def dpd_delay(self, value: Optional["TimeValue"]) -> None:
        """
        Set dpdDelay with validation.
        
        Args:
            value: The dpdDelay to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dpdDelay = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"dpdDelay must be TimeValue or None, got {type(value).__name__}"
            )
        self._dpdDelay = value
        # ESP (Encapsulating Security Payload) algorithm that encryption and optional
        # authentication for the AES-128+SHA2-256.
        self._espCipherSuite: List["String"] = []

    @property
    def esp_cipher_suite(self) -> List["String"]:
        """Get espCipherSuite (Pythonic accessor)."""
        return self._espCipherSuite
        # IKE encryption/authentication algorithms to be used for connection.
        self._ikeCipherSuite: Optional["String"] = None

    @property
    def ike_cipher_suite(self) -> Optional["String"]:
        """Get ikeCipherSuite (Pythonic accessor)."""
        return self._ikeCipherSuite

    @ike_cipher_suite.setter
    def ike_cipher_suite(self, value: Optional["String"]) -> None:
        """
        Set ikeCipherSuite with validation.
        
        Args:
            value: The ikeCipherSuite to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ikeCipherSuite = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"ikeCipherSuite must be String or None, got {type(value).__name__}"
            )
        self._ikeCipherSuite = value
        # This attribute describes the hard deadline when an SA in percentage.
        # of max(ikeReauthTime, ikeRekey %.
        self._ikeOverTime: Optional["TimeValue"] = None

    @property
    def ike_over_time(self) -> Optional["TimeValue"]:
        """Get ikeOverTime (Pythonic accessor)."""
        return self._ikeOverTime

    @ike_over_time.setter
    def ike_over_time(self, value: Optional["TimeValue"]) -> None:
        """
        Set ikeOverTime with validation.
        
        Args:
            value: The ikeOverTime to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ikeOverTime = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"ikeOverTime must be TimeValue or None, got {type(value).__name__}"
            )
        self._ikeOverTime = value
        # This attribute defines in percentage by how long before of ikeReauthTime and
        # ikeRekeyTime will be.
        self._ikeRandTime: Optional["PositiveInteger"] = None

    @property
    def ike_rand_time(self) -> Optional["PositiveInteger"]:
        """Get ikeRandTime (Pythonic accessor)."""
        return self._ikeRandTime

    @ike_rand_time.setter
    def ike_rand_time(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set ikeRandTime with validation.
        
        Args:
            value: The ikeRandTime to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ikeRandTime = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"ikeRandTime must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._ikeRandTime = value
        # This attribute defines the absolute time after which an IKE be
                # reauthenticated.
        # reauthentication is disabled.
        self._ikeReauthTime: Optional["TimeValue"] = None

    @property
    def ike_reauth_time(self) -> Optional["TimeValue"]:
        """Get ikeReauthTime (Pythonic accessor)."""
        return self._ikeReauthTime

    @ike_reauth_time.setter
    def ike_reauth_time(self, value: Optional["TimeValue"]) -> None:
        """
        Set ikeReauthTime with validation.
        
        Args:
            value: The ikeReauthTime to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ikeReauthTime = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"ikeReauthTime must be TimeValue or None, got {type(value).__name__}"
            )
        self._ikeReauthTime = value
        # This attribute defines the absolute time after which an IKE be rekeyed.
        # rekey is disabled.
        self._ikeRekeyTime: Optional["TimeValue"] = None

    @property
    def ike_rekey_time(self) -> Optional["TimeValue"]:
        """Get ikeRekeyTime (Pythonic accessor)."""
        return self._ikeRekeyTime

    @ike_rekey_time.setter
    def ike_rekey_time(self, value: Optional["TimeValue"]) -> None:
        """
        Set ikeRekeyTime with validation.
        
        Args:
            value: The ikeRekeyTime to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ikeRekeyTime = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"ikeRekeyTime must be TimeValue or None, got {type(value).__name__}"
            )
        self._ikeRekeyTime = value
        # This attribute describes the hard deadline when an IPsec invalid in
        # percentage.
        self._saOverTime: Optional["PositiveInteger"] = None

    @property
    def sa_over_time(self) -> Optional["PositiveInteger"]:
        """Get saOverTime (Pythonic accessor)."""
        return self._saOverTime

    @sa_over_time.setter
    def sa_over_time(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set saOverTime with validation.
        
        Args:
            value: The saOverTime to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._saOverTime = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"saOverTime must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._saOverTime = value
        # This attribute defines by how long before the expiration of be rekeyed.
        self._saRandTime: Optional["TimeValue"] = None

    @property
    def sa_rand_time(self) -> Optional["TimeValue"]:
        """Get saRandTime (Pythonic accessor)."""
        return self._saRandTime

    @sa_rand_time.setter
    def sa_rand_time(self, value: Optional["TimeValue"]) -> None:
        """
        Set saRandTime with validation.
        
        Args:
            value: The saRandTime to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._saRandTime = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"saRandTime must be TimeValue or None, got {type(value).__name__}"
            )
        self._saRandTime = value
        # This attribute defines the absolute time after which an will be rekeyed.
        # rekey is disabled.
        self._saRekeyTime: Optional["TimeValue"] = None

    @property
    def sa_rekey_time(self) -> Optional["TimeValue"]:
        """Get saRekeyTime (Pythonic accessor)."""
        return self._saRekeyTime

    @sa_rekey_time.setter
    def sa_rekey_time(self, value: Optional["TimeValue"]) -> None:
        """
        Set saRekeyTime with validation.
        
        Args:
            value: The saRekeyTime to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._saRekeyTime = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"saRekeyTime must be TimeValue or None, got {type(value).__name__}"
            )
        self._saRekeyTime = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAhCipherSuite(self) -> List["String"]:
        """
        AUTOSAR-compliant getter for ahCipherSuite.
        
        Returns:
            The ahCipherSuite value
        
        Note:
            Delegates to ah_cipher_suite property (CODING_RULE_V2_00017)
        """
        return self.ah_cipher_suite  # Delegates to property

    def getDpdAction(self) -> "IPsecDpdActionEnum":
        """
        AUTOSAR-compliant getter for dpdAction.
        
        Returns:
            The dpdAction value
        
        Note:
            Delegates to dpd_action property (CODING_RULE_V2_00017)
        """
        return self.dpd_action  # Delegates to property

    def setDpdAction(self, value: "IPsecDpdActionEnum") -> "IPSecConfigProps":
        """
        AUTOSAR-compliant setter for dpdAction with method chaining.
        
        Args:
            value: The dpdAction to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to dpd_action property setter (gets validation automatically)
        """
        self.dpd_action = value  # Delegates to property setter
        return self

    def getDpdDelay(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for dpdDelay.
        
        Returns:
            The dpdDelay value
        
        Note:
            Delegates to dpd_delay property (CODING_RULE_V2_00017)
        """
        return self.dpd_delay  # Delegates to property

    def setDpdDelay(self, value: "TimeValue") -> "IPSecConfigProps":
        """
        AUTOSAR-compliant setter for dpdDelay with method chaining.
        
        Args:
            value: The dpdDelay to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to dpd_delay property setter (gets validation automatically)
        """
        self.dpd_delay = value  # Delegates to property setter
        return self

    def getEspCipherSuite(self) -> List["String"]:
        """
        AUTOSAR-compliant getter for espCipherSuite.
        
        Returns:
            The espCipherSuite value
        
        Note:
            Delegates to esp_cipher_suite property (CODING_RULE_V2_00017)
        """
        return self.esp_cipher_suite  # Delegates to property

    def getIkeCipherSuite(self) -> "String":
        """
        AUTOSAR-compliant getter for ikeCipherSuite.
        
        Returns:
            The ikeCipherSuite value
        
        Note:
            Delegates to ike_cipher_suite property (CODING_RULE_V2_00017)
        """
        return self.ike_cipher_suite  # Delegates to property

    def setIkeCipherSuite(self, value: "String") -> "IPSecConfigProps":
        """
        AUTOSAR-compliant setter for ikeCipherSuite with method chaining.
        
        Args:
            value: The ikeCipherSuite to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to ike_cipher_suite property setter (gets validation automatically)
        """
        self.ike_cipher_suite = value  # Delegates to property setter
        return self

    def getIkeOverTime(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for ikeOverTime.
        
        Returns:
            The ikeOverTime value
        
        Note:
            Delegates to ike_over_time property (CODING_RULE_V2_00017)
        """
        return self.ike_over_time  # Delegates to property

    def setIkeOverTime(self, value: "TimeValue") -> "IPSecConfigProps":
        """
        AUTOSAR-compliant setter for ikeOverTime with method chaining.
        
        Args:
            value: The ikeOverTime to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to ike_over_time property setter (gets validation automatically)
        """
        self.ike_over_time = value  # Delegates to property setter
        return self

    def getIkeRandTime(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for ikeRandTime.
        
        Returns:
            The ikeRandTime value
        
        Note:
            Delegates to ike_rand_time property (CODING_RULE_V2_00017)
        """
        return self.ike_rand_time  # Delegates to property

    def setIkeRandTime(self, value: "PositiveInteger") -> "IPSecConfigProps":
        """
        AUTOSAR-compliant setter for ikeRandTime with method chaining.
        
        Args:
            value: The ikeRandTime to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to ike_rand_time property setter (gets validation automatically)
        """
        self.ike_rand_time = value  # Delegates to property setter
        return self

    def getIkeReauthTime(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for ikeReauthTime.
        
        Returns:
            The ikeReauthTime value
        
        Note:
            Delegates to ike_reauth_time property (CODING_RULE_V2_00017)
        """
        return self.ike_reauth_time  # Delegates to property

    def setIkeReauthTime(self, value: "TimeValue") -> "IPSecConfigProps":
        """
        AUTOSAR-compliant setter for ikeReauthTime with method chaining.
        
        Args:
            value: The ikeReauthTime to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to ike_reauth_time property setter (gets validation automatically)
        """
        self.ike_reauth_time = value  # Delegates to property setter
        return self

    def getIkeRekeyTime(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for ikeRekeyTime.
        
        Returns:
            The ikeRekeyTime value
        
        Note:
            Delegates to ike_rekey_time property (CODING_RULE_V2_00017)
        """
        return self.ike_rekey_time  # Delegates to property

    def setIkeRekeyTime(self, value: "TimeValue") -> "IPSecConfigProps":
        """
        AUTOSAR-compliant setter for ikeRekeyTime with method chaining.
        
        Args:
            value: The ikeRekeyTime to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to ike_rekey_time property setter (gets validation automatically)
        """
        self.ike_rekey_time = value  # Delegates to property setter
        return self

    def getSaOverTime(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for saOverTime.
        
        Returns:
            The saOverTime value
        
        Note:
            Delegates to sa_over_time property (CODING_RULE_V2_00017)
        """
        return self.sa_over_time  # Delegates to property

    def setSaOverTime(self, value: "PositiveInteger") -> "IPSecConfigProps":
        """
        AUTOSAR-compliant setter for saOverTime with method chaining.
        
        Args:
            value: The saOverTime to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sa_over_time property setter (gets validation automatically)
        """
        self.sa_over_time = value  # Delegates to property setter
        return self

    def getSaRandTime(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for saRandTime.
        
        Returns:
            The saRandTime value
        
        Note:
            Delegates to sa_rand_time property (CODING_RULE_V2_00017)
        """
        return self.sa_rand_time  # Delegates to property

    def setSaRandTime(self, value: "TimeValue") -> "IPSecConfigProps":
        """
        AUTOSAR-compliant setter for saRandTime with method chaining.
        
        Args:
            value: The saRandTime to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sa_rand_time property setter (gets validation automatically)
        """
        self.sa_rand_time = value  # Delegates to property setter
        return self

    def getSaRekeyTime(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for saRekeyTime.
        
        Returns:
            The saRekeyTime value
        
        Note:
            Delegates to sa_rekey_time property (CODING_RULE_V2_00017)
        """
        return self.sa_rekey_time  # Delegates to property

    def setSaRekeyTime(self, value: "TimeValue") -> "IPSecConfigProps":
        """
        AUTOSAR-compliant setter for saRekeyTime with method chaining.
        
        Args:
            value: The saRekeyTime to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sa_rekey_time property setter (gets validation automatically)
        """
        self.sa_rekey_time = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_dpd_action(self, value: Optional["IPsecDpdActionEnum"]) -> "IPSecConfigProps":
        """
        Set dpdAction and return self for chaining.
        
        Args:
            value: The dpdAction to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_dpd_action("value")
        """
        self.dpd_action = value  # Use property setter (gets validation)
        return self

    def with_dpd_delay(self, value: Optional["TimeValue"]) -> "IPSecConfigProps":
        """
        Set dpdDelay and return self for chaining.
        
        Args:
            value: The dpdDelay to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_dpd_delay("value")
        """
        self.dpd_delay = value  # Use property setter (gets validation)
        return self

    def with_ike_cipher_suite(self, value: Optional["String"]) -> "IPSecConfigProps":
        """
        Set ikeCipherSuite and return self for chaining.
        
        Args:
            value: The ikeCipherSuite to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_ike_cipher_suite("value")
        """
        self.ike_cipher_suite = value  # Use property setter (gets validation)
        return self

    def with_ike_over_time(self, value: Optional["TimeValue"]) -> "IPSecConfigProps":
        """
        Set ikeOverTime and return self for chaining.
        
        Args:
            value: The ikeOverTime to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_ike_over_time("value")
        """
        self.ike_over_time = value  # Use property setter (gets validation)
        return self

    def with_ike_rand_time(self, value: Optional["PositiveInteger"]) -> "IPSecConfigProps":
        """
        Set ikeRandTime and return self for chaining.
        
        Args:
            value: The ikeRandTime to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_ike_rand_time("value")
        """
        self.ike_rand_time = value  # Use property setter (gets validation)
        return self

    def with_ike_reauth_time(self, value: Optional["TimeValue"]) -> "IPSecConfigProps":
        """
        Set ikeReauthTime and return self for chaining.
        
        Args:
            value: The ikeReauthTime to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_ike_reauth_time("value")
        """
        self.ike_reauth_time = value  # Use property setter (gets validation)
        return self

    def with_ike_rekey_time(self, value: Optional["TimeValue"]) -> "IPSecConfigProps":
        """
        Set ikeRekeyTime and return self for chaining.
        
        Args:
            value: The ikeRekeyTime to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_ike_rekey_time("value")
        """
        self.ike_rekey_time = value  # Use property setter (gets validation)
        return self

    def with_sa_over_time(self, value: Optional["PositiveInteger"]) -> "IPSecConfigProps":
        """
        Set saOverTime and return self for chaining.
        
        Args:
            value: The saOverTime to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sa_over_time("value")
        """
        self.sa_over_time = value  # Use property setter (gets validation)
        return self

    def with_sa_rand_time(self, value: Optional["TimeValue"]) -> "IPSecConfigProps":
        """
        Set saRandTime and return self for chaining.
        
        Args:
            value: The saRandTime to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sa_rand_time("value")
        """
        self.sa_rand_time = value  # Use property setter (gets validation)
        return self

    def with_sa_rekey_time(self, value: Optional["TimeValue"]) -> "IPSecConfigProps":
        """
        Set saRekeyTime and return self for chaining.
        
        Args:
            value: The saRekeyTime to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sa_rekey_time("value")
        """
        self.sa_rekey_time = value  # Use property setter (gets validation)
        return self