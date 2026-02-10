"""
AUTOSAR Package - SecureCommunication

Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication
"""

from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    String,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class CryptoServiceCertificate(ARElement):
    """
    This meta-class represents the ability to model a cryptographic certificate.

    Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication::CryptoServiceCertificate

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 310, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 565, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represents a description of the family of algorithm used to
        # generate public key and the cryptographic certificate.
        self._algorithmFamily: Optional["CryptoCertificate"] = None

    @property
    def algorithm_family(self) -> Optional["CryptoCertificate"]:
        """Get algorithmFamily (Pythonic accessor)."""
        return self._algorithmFamily

    @algorithm_family.setter
    def algorithm_family(self, value: Optional["CryptoCertificate"]) -> None:
        """
        Set algorithmFamily with validation.

        Args:
            value: The algorithmFamily to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._algorithmFamily = None
            return

        if not isinstance(value, CryptoCertificate):
            raise TypeError(
                f"algorithmFamily must be CryptoCertificate or None, got {type(value).__name__}"
            )
        self._algorithmFamily = value
        # the certificate.
        self._format: Optional["CryptoCertificateFormat"] = None

    @property
    def format(self) -> Optional["CryptoCertificateFormat"]:
        """Get format (Pythonic accessor)."""
        return self._format

    @format.setter
    def format(self, value: Optional["CryptoCertificateFormat"]) -> None:
        """
        Set format with validation.

        Args:
            value: The format to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._format = None
            return

        if not isinstance(value, CryptoCertificateFormat):
            raise TypeError(
                f"format must be CryptoCertificateFormat or None, got {type(value).__name__}"
            )
        self._format = value
        # in bytes.
        self._maximum: Optional["PositiveInteger"] = None

    @property
    def maximum(self) -> Optional["PositiveInteger"]:
        """Get maximum (Pythonic accessor)."""
        return self._maximum

    @maximum.setter
    def maximum(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maximum with validation.

        Args:
            value: The maximum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maximum = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"maximum must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._maximum = value
        # chain.
        self._nextHigher: Optional["CryptoService"] = None

    @property
    def next_higher(self) -> Optional["CryptoService"]:
        """Get nextHigher (Pythonic accessor)."""
        return self._nextHigher

    @next_higher.setter
    def next_higher(self, value: Optional["CryptoService"]) -> None:
        """
        Set nextHigher with validation.

        Args:
            value: The nextHigher to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nextHigher = None
            return

        if not isinstance(value, CryptoService):
            raise TypeError(
                f"nextHigher must be CryptoService or None, got {type(value).__name__}"
            )
        self._nextHigher = value
                # the same port), each of them different certificate.
        # client sends the SNI to the Server in the client hello, looks the SNI up in
                # its certificate list and uses identified by the SNI.
        self._serverName: Optional["String"] = None

    @property
    def server_name(self) -> Optional["String"]:
        """Get serverName (Pythonic accessor)."""
        return self._serverName

    @server_name.setter
    def server_name(self, value: Optional["String"]) -> None:
        """
        Set serverName with validation.

        Args:
            value: The serverName to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._serverName = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"serverName must be String or str or None, got {type(value).__name__}"
            )
        self._serverName = value

    def with_mka_participant(self, value):
        """
        Set mka_participant and return self for chaining.

        Args:
            value: The mka_participant to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mka_participant("value")
        """
        self.mka_participant = value  # Use property setter (gets validation)
        return self

    def with_mka_participant(self, value):
        """
        Set mka_participant and return self for chaining.

        Args:
            value: The mka_participant to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mka_participant("value")
        """
        self.mka_participant = value  # Use property setter (gets validation)
        return self

    def with_elliptic_curve(self, value):
        """
        Set elliptic_curve and return self for chaining.

        Args:
            value: The elliptic_curve to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_elliptic_curve("value")
        """
        self.elliptic_curve = value  # Use property setter (gets validation)
        return self

    def with_key_exchange(self, value):
        """
        Set key_exchange and return self for chaining.

        Args:
            value: The key_exchange to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_key_exchange("value")
        """
        self.key_exchange = value  # Use property setter (gets validation)
        return self

    def with_ip_sec_rule(self, value):
        """
        Set ip_sec_rule and return self for chaining.

        Args:
            value: The ip_sec_rule to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ip_sec_rule("value")
        """
        self.ip_sec_rule = value  # Use property setter (gets validation)
        return self

    def with_local_certificate(self, value):
        """
        Set local_certificate and return self for chaining.

        Args:
            value: The local_certificate to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_local_certificate("value")
        """
        self.local_certificate = value  # Use property setter (gets validation)
        return self

    def with_remote_ip(self, value):
        """
        Set remote_ip and return self for chaining.

        Args:
            value: The remote_ip to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_remote_ip("value")
        """
        self.remote_ip = value  # Use property setter (gets validation)
        return self

    def with_ah_cipher_suite(self, value):
        """
        Set ah_cipher_suite and return self for chaining.

        Args:
            value: The ah_cipher_suite to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ah_cipher_suite("value")
        """
        self.ah_cipher_suite = value  # Use property setter (gets validation)
        return self

    def with_esp_cipher_suite(self, value):
        """
        Set esp_cipher_suite and return self for chaining.

        Args:
            value: The esp_cipher_suite to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_esp_cipher_suite("value")
        """
        self.esp_cipher_suite = value  # Use property setter (gets validation)
        return self

    def with_key_exchange(self, value):
        """
        Set key_exchange and return self for chaining.

        Args:
            value: The key_exchange to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_key_exchange("value")
        """
        self.key_exchange = value  # Use property setter (gets validation)
        return self

    def with_tls_cipher_suite(self, value):
        """
        Set tls_cipher_suite and return self for chaining.

        Args:
            value: The tls_cipher_suite to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tls_cipher_suite("value")
        """
        self.tls_cipher_suite = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAlgorithmFamily(self) -> "CryptoCertificate":
        """
        AUTOSAR-compliant getter for algorithmFamily.

        Returns:
            The algorithmFamily value

        Note:
            Delegates to algorithm_family property (CODING_RULE_V2_00017)
        """
        return self.algorithm_family  # Delegates to property

    def setAlgorithmFamily(self, value: "CryptoCertificate") -> "CryptoServiceCertificate":
        """
        AUTOSAR-compliant setter for algorithmFamily with method chaining.

        Args:
            value: The algorithmFamily to set

        Returns:
            self for method chaining

        Note:
            Delegates to algorithm_family property setter (gets validation automatically)
        """
        self.algorithm_family = value  # Delegates to property setter
        return self

    def getFormat(self) -> "CryptoCertificateFormat":
        """
        AUTOSAR-compliant getter for format.

        Returns:
            The format value

        Note:
            Delegates to format property (CODING_RULE_V2_00017)
        """
        return self.format  # Delegates to property

    def setFormat(self, value: "CryptoCertificateFormat") -> "CryptoServiceCertificate":
        """
        AUTOSAR-compliant setter for format with method chaining.

        Args:
            value: The format to set

        Returns:
            self for method chaining

        Note:
            Delegates to format property setter (gets validation automatically)
        """
        self.format = value  # Delegates to property setter
        return self

    def getMaximum(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maximum.

        Returns:
            The maximum value

        Note:
            Delegates to maximum property (CODING_RULE_V2_00017)
        """
        return self.maximum  # Delegates to property

    def setMaximum(self, value: "PositiveInteger") -> "CryptoServiceCertificate":
        """
        AUTOSAR-compliant setter for maximum with method chaining.

        Args:
            value: The maximum to set

        Returns:
            self for method chaining

        Note:
            Delegates to maximum property setter (gets validation automatically)
        """
        self.maximum = value  # Delegates to property setter
        return self

    def getNextHigher(self) -> "CryptoService":
        """
        AUTOSAR-compliant getter for nextHigher.

        Returns:
            The nextHigher value

        Note:
            Delegates to next_higher property (CODING_RULE_V2_00017)
        """
        return self.next_higher  # Delegates to property

    def setNextHigher(self, value: "CryptoService") -> "CryptoServiceCertificate":
        """
        AUTOSAR-compliant setter for nextHigher with method chaining.

        Args:
            value: The nextHigher to set

        Returns:
            self for method chaining

        Note:
            Delegates to next_higher property setter (gets validation automatically)
        """
        self.next_higher = value  # Delegates to property setter
        return self

    def getServerName(self) -> "String":
        """
        AUTOSAR-compliant getter for serverName.

        Returns:
            The serverName value

        Note:
            Delegates to server_name property (CODING_RULE_V2_00017)
        """
        return self.server_name  # Delegates to property

    def setServerName(self, value: "String") -> "CryptoServiceCertificate":
        """
        AUTOSAR-compliant setter for serverName with method chaining.

        Args:
            value: The serverName to set

        Returns:
            self for method chaining

        Note:
            Delegates to server_name property setter (gets validation automatically)
        """
        self.server_name = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_algorithm_family(self, value: Optional["CryptoCertificate"]) -> "CryptoServiceCertificate":
        """
        Set algorithmFamily and return self for chaining.

        Args:
            value: The algorithmFamily to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_algorithm_family("value")
        """
        self.algorithm_family = value  # Use property setter (gets validation)
        return self

    def with_format(self, value: Optional["CryptoCertificateFormat"]) -> "CryptoServiceCertificate":
        """
        Set format and return self for chaining.

        Args:
            value: The format to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_format("value")
        """
        self.format = value  # Use property setter (gets validation)
        return self

    def with_maximum(self, value: Optional["PositiveInteger"]) -> "CryptoServiceCertificate":
        """
        Set maximum and return self for chaining.

        Args:
            value: The maximum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_maximum("value")
        """
        self.maximum = value  # Use property setter (gets validation)
        return self

    def with_next_higher(self, value: Optional["CryptoService"]) -> "CryptoServiceCertificate":
        """
        Set nextHigher and return self for chaining.

        Args:
            value: The nextHigher to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_next_higher("value")
        """
        self.next_higher = value  # Use property setter (gets validation)
        return self

    def with_server_name(self, value: Optional["String"]) -> "CryptoServiceCertificate":
        """
        Set serverName and return self for chaining.

        Args:
            value: The serverName to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_server_name("value")
        """
        self.server_name = value  # Use property setter (gets validation)
        return self



class MacSecProps(ARObject):
    """
    This meta-class allows to configure MACsec (Media access control security)
    and the MKA (MACsec Key Agreement) for the CouplingPort (PHY).

    Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication::MacSecProps

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

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"autoStart must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._autoStart = value
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



class MacSecLocalKayProps(ARObject):
    """
    Configuration of the MAC Security Key Agreement Entity (KaY).

    Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication::MacSecLocalKayProps

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 173, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the destination MAC Address that is to calculate the
        # ICV (Integrity Check Value).
        self._destinationMac: Optional["MacAddressString"] = None

    @property
    def destination_mac(self) -> Optional["MacAddressString"]:
        """Get destinationMac (Pythonic accessor)."""
        return self._destinationMac

    @destination_mac.setter
    def destination_mac(self, value: Optional["MacAddressString"]) -> None:
        """
        Set destinationMac with validation.

        Args:
            value: The destinationMac to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._destinationMac = None
            return

        if not isinstance(value, MacAddressString):
            raise TypeError(
                f"destinationMac must be MacAddressString or None, got {type(value).__name__}"
            )
        self._destinationMac = value
        self._globalKayProps: Optional["MacSecGlobalKay"] = None

    @property
    def global_kay_props(self) -> Optional["MacSecGlobalKay"]:
        """Get globalKayProps (Pythonic accessor)."""
        return self._globalKayProps

    @global_kay_props.setter
    def global_kay_props(self, value: Optional["MacSecGlobalKay"]) -> None:
        """
        Set globalKayProps with validation.

        Args:
            value: The globalKayProps to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._globalKayProps = None
            return

        if not isinstance(value, MacSecGlobalKay):
            raise TypeError(
                f"globalKayProps must be MacSecGlobalKay or None, got {type(value).__name__}"
            )
        self._globalKayProps = value
        # atp.
        # Status=candidate.
        self._keyServer: Optional["PositiveInteger"] = None

    @property
    def key_server(self) -> Optional["PositiveInteger"]:
        """Get keyServer (Pythonic accessor)."""
        return self._keyServer

    @key_server.setter
    def key_server(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set keyServer with validation.

        Args:
            value: The keyServer to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._keyServer = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"keyServer must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._keyServer = value
        # AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._mkaParticipant: List["MacSecKayParticipant"] = []

    @property
    def mka_participant(self) -> List["MacSecKayParticipant"]:
        """Get mkaParticipant (Pythonic accessor)."""
        return self._mkaParticipant
        # Role of the MAC Security Key Agreement Entity.
        self._role: Optional["MacSecRoleEnum"] = None

    @property
    def role(self) -> Optional["MacSecRoleEnum"]:
        """Get role (Pythonic accessor)."""
        return self._role

    @role.setter
    def role(self, value: Optional["MacSecRoleEnum"]) -> None:
        """
        Set role with validation.

        Args:
            value: The role to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._role = None
            return

        if not isinstance(value, MacSecRoleEnum):
            raise TypeError(
                f"role must be MacSecRoleEnum or None, got {type(value).__name__}"
            )
        self._role = value
        # (Integrity Check Value).
        self._sourceMac: Optional["MacAddressString"] = None

    @property
    def source_mac(self) -> Optional["MacAddressString"]:
        """Get sourceMac (Pythonic accessor)."""
        return self._sourceMac

    @source_mac.setter
    def source_mac(self, value: Optional["MacAddressString"]) -> None:
        """
        Set sourceMac with validation.

        Args:
            value: The sourceMac to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sourceMac = None
            return

        if not isinstance(value, MacAddressString):
            raise TypeError(
                f"sourceMac must be MacAddressString or None, got {type(value).__name__}"
            )
        self._sourceMac = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDestinationMac(self) -> "MacAddressString":
        """
        AUTOSAR-compliant getter for destinationMac.

        Returns:
            The destinationMac value

        Note:
            Delegates to destination_mac property (CODING_RULE_V2_00017)
        """
        return self.destination_mac  # Delegates to property

    def setDestinationMac(self, value: "MacAddressString") -> "MacSecLocalKayProps":
        """
        AUTOSAR-compliant setter for destinationMac with method chaining.

        Args:
            value: The destinationMac to set

        Returns:
            self for method chaining

        Note:
            Delegates to destination_mac property setter (gets validation automatically)
        """
        self.destination_mac = value  # Delegates to property setter
        return self

    def getGlobalKayProps(self) -> "MacSecGlobalKay":
        """
        AUTOSAR-compliant getter for globalKayProps.

        Returns:
            The globalKayProps value

        Note:
            Delegates to global_kay_props property (CODING_RULE_V2_00017)
        """
        return self.global_kay_props  # Delegates to property

    def setGlobalKayProps(self, value: "MacSecGlobalKay") -> "MacSecLocalKayProps":
        """
        AUTOSAR-compliant setter for globalKayProps with method chaining.

        Args:
            value: The globalKayProps to set

        Returns:
            self for method chaining

        Note:
            Delegates to global_kay_props property setter (gets validation automatically)
        """
        self.global_kay_props = value  # Delegates to property setter
        return self

    def getKeyServer(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for keyServer.

        Returns:
            The keyServer value

        Note:
            Delegates to key_server property (CODING_RULE_V2_00017)
        """
        return self.key_server  # Delegates to property

    def setKeyServer(self, value: "PositiveInteger") -> "MacSecLocalKayProps":
        """
        AUTOSAR-compliant setter for keyServer with method chaining.

        Args:
            value: The keyServer to set

        Returns:
            self for method chaining

        Note:
            Delegates to key_server property setter (gets validation automatically)
        """
        self.key_server = value  # Delegates to property setter
        return self

    def getMkaParticipant(self) -> List["MacSecKayParticipant"]:
        """
        AUTOSAR-compliant getter for mkaParticipant.

        Returns:
            The mkaParticipant value

        Note:
            Delegates to mka_participant property (CODING_RULE_V2_00017)
        """
        return self.mka_participant  # Delegates to property

    def getRole(self) -> "MacSecRoleEnum":
        """
        AUTOSAR-compliant getter for role.

        Returns:
            The role value

        Note:
            Delegates to role property (CODING_RULE_V2_00017)
        """
        return self.role  # Delegates to property

    def setRole(self, value: "MacSecRoleEnum") -> "MacSecLocalKayProps":
        """
        AUTOSAR-compliant setter for role with method chaining.

        Args:
            value: The role to set

        Returns:
            self for method chaining

        Note:
            Delegates to role property setter (gets validation automatically)
        """
        self.role = value  # Delegates to property setter
        return self

    def getSourceMac(self) -> "MacAddressString":
        """
        AUTOSAR-compliant getter for sourceMac.

        Returns:
            The sourceMac value

        Note:
            Delegates to source_mac property (CODING_RULE_V2_00017)
        """
        return self.source_mac  # Delegates to property

    def setSourceMac(self, value: "MacAddressString") -> "MacSecLocalKayProps":
        """
        AUTOSAR-compliant setter for sourceMac with method chaining.

        Args:
            value: The sourceMac to set

        Returns:
            self for method chaining

        Note:
            Delegates to source_mac property setter (gets validation automatically)
        """
        self.source_mac = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_destination_mac(self, value: Optional["MacAddressString"]) -> "MacSecLocalKayProps":
        """
        Set destinationMac and return self for chaining.

        Args:
            value: The destinationMac to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_destination_mac("value")
        """
        self.destination_mac = value  # Use property setter (gets validation)
        return self

    def with_global_kay_props(self, value: Optional["MacSecGlobalKay"]) -> "MacSecLocalKayProps":
        """
        Set globalKayProps and return self for chaining.

        Args:
            value: The globalKayProps to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_global_kay_props("value")
        """
        self.global_kay_props = value  # Use property setter (gets validation)
        return self

    def with_key_server(self, value: Optional["PositiveInteger"]) -> "MacSecLocalKayProps":
        """
        Set keyServer and return self for chaining.

        Args:
            value: The keyServer to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_key_server("value")
        """
        self.key_server = value  # Use property setter (gets validation)
        return self

    def with_role(self, value: Optional["MacSecRoleEnum"]) -> "MacSecLocalKayProps":
        """
        Set role and return self for chaining.

        Args:
            value: The role to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_role("value")
        """
        self.role = value  # Use property setter (gets validation)
        return self

    def with_source_mac(self, value: Optional["MacAddressString"]) -> "MacSecLocalKayProps":
        """
        Set sourceMac and return self for chaining.

        Args:
            value: The sourceMac to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_source_mac("value")
        """
        self.source_mac = value  # Use property setter (gets validation)
        return self



class MacSecGlobalKayProps(ARElement):
    """
    Configuration of the MAC Security Key Agreement Entity properties that are
    shared by different KaY configurations.

    Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication::MacSecGlobalKayProps

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 174, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # by MACsec.
        # The providedEtherType will not be.
        self._bypassEther: "PositiveInteger" = None

    @property
    def bypass_ether(self) -> "PositiveInteger":
        """Get bypassEther (Pythonic accessor)."""
        return self._bypassEther

    @bypass_ether.setter
    def bypass_ether(self, value: "PositiveInteger") -> None:
        """
        Set bypassEther with validation.

        Args:
            value: The bypassEther to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"bypassEther must be PositiveInteger or str, got {type(value).__name__}"
            )
        self._bypassEther = value
        # The provided VLAN-IDs will not be (VLAN-ID 0 is interpreted as Bypass
                # untagged traffic).
        self._bypassVlan: "PositiveInteger" = None

    @property
    def bypass_vlan(self) -> "PositiveInteger":
        """Get bypassVlan (Pythonic accessor)."""
        return self._bypassVlan

    @bypass_vlan.setter
    def bypass_vlan(self, value: "PositiveInteger") -> None:
        """
        Set bypassVlan with validation.

        Args:
            value: The bypassVlan to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"bypassVlan must be PositiveInteger or str, got {type(value).__name__}"
            )
        self._bypassVlan = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBypassEther(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for bypassEther.

        Returns:
            The bypassEther value

        Note:
            Delegates to bypass_ether property (CODING_RULE_V2_00017)
        """
        return self.bypass_ether  # Delegates to property

    def setBypassEther(self, value: "PositiveInteger") -> "MacSecGlobalKayProps":
        """
        AUTOSAR-compliant setter for bypassEther with method chaining.

        Args:
            value: The bypassEther to set

        Returns:
            self for method chaining

        Note:
            Delegates to bypass_ether property setter (gets validation automatically)
        """
        self.bypass_ether = value  # Delegates to property setter
        return self

    def getBypassVlan(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for bypassVlan.

        Returns:
            The bypassVlan value

        Note:
            Delegates to bypass_vlan property (CODING_RULE_V2_00017)
        """
        return self.bypass_vlan  # Delegates to property

    def setBypassVlan(self, value: "PositiveInteger") -> "MacSecGlobalKayProps":
        """
        AUTOSAR-compliant setter for bypassVlan with method chaining.

        Args:
            value: The bypassVlan to set

        Returns:
            self for method chaining

        Note:
            Delegates to bypass_vlan property setter (gets validation automatically)
        """
        self.bypass_vlan = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bypass_ether(self, value: "PositiveInteger") -> "MacSecGlobalKayProps":
        """
        Set bypassEther and return self for chaining.

        Args:
            value: The bypassEther to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bypass_ether("value")
        """
        self.bypass_ether = value  # Use property setter (gets validation)
        return self

    def with_bypass_vlan(self, value: "PositiveInteger") -> "MacSecGlobalKayProps":
        """
        Set bypassVlan and return self for chaining.

        Args:
            value: The bypassVlan to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bypass_vlan("value")
        """
        self.bypass_vlan = value  # Use property setter (gets validation)
        return self



class MacSecParticipantSet(ARElement):
    """
    Collection of MACsec Kay Participants on an Ethernet Link.

    Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication::MacSecParticipantSet

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 174, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the EthernetCluster (Link) on which the KaY located.
        self._ethernetCluster: Optional["EthernetCluster"] = None

    @property
    def ethernet_cluster(self) -> Optional["EthernetCluster"]:
        """Get ethernetCluster (Pythonic accessor)."""
        return self._ethernetCluster

    @ethernet_cluster.setter
    def ethernet_cluster(self, value: Optional["EthernetCluster"]) -> None:
        """
        Set ethernetCluster with validation.

        Args:
            value: The ethernetCluster to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ethernetCluster = None
            return

        if not isinstance(value, EthernetCluster):
            raise TypeError(
                f"ethernetCluster must be EthernetCluster or None, got {type(value).__name__}"
            )
        self._ethernetCluster = value
        self._mkaParticipant: List["MacSecKayParticipant"] = []

    @property
    def mka_participant(self) -> List["MacSecKayParticipant"]:
        """Get mkaParticipant (Pythonic accessor)."""
        return self._mkaParticipant

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEthernetCluster(self) -> "EthernetCluster":
        """
        AUTOSAR-compliant getter for ethernetCluster.

        Returns:
            The ethernetCluster value

        Note:
            Delegates to ethernet_cluster property (CODING_RULE_V2_00017)
        """
        return self.ethernet_cluster  # Delegates to property

    def setEthernetCluster(self, value: "EthernetCluster") -> "MacSecParticipantSet":
        """
        AUTOSAR-compliant setter for ethernetCluster with method chaining.

        Args:
            value: The ethernetCluster to set

        Returns:
            self for method chaining

        Note:
            Delegates to ethernet_cluster property setter (gets validation automatically)
        """
        self.ethernet_cluster = value  # Delegates to property setter
        return self

    def getMkaParticipant(self) -> List["MacSecKayParticipant"]:
        """
        AUTOSAR-compliant getter for mkaParticipant.

        Returns:
            The mkaParticipant value

        Note:
            Delegates to mka_participant property (CODING_RULE_V2_00017)
        """
        return self.mka_participant  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ethernet_cluster(self, value: Optional["EthernetCluster"]) -> "MacSecParticipantSet":
        """
        Set ethernetCluster and return self for chaining.

        Args:
            value: The ethernetCluster to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ethernet_cluster("value")
        """
        self.ethernet_cluster = value  # Use property setter (gets validation)
        return self



class MacSecKayParticipant(Identifiable):
    """
    This meta-class configures a MKA participant.

    Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication::MacSecKayParticipant

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 175, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the key where the ckn (Connectivity is stored.
        self._ckn: Optional["CryptoServiceKey"] = None

    @property
    def ckn(self) -> Optional["CryptoServiceKey"]:
        """Get ckn (Pythonic accessor)."""
        return self._ckn

    @ckn.setter
    def ckn(self, value: Optional["CryptoServiceKey"]) -> None:
        """
        Set ckn with validation.

        Args:
            value: The ckn to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ckn = None
            return

        if not isinstance(value, CryptoServiceKey):
            raise TypeError(
                f"ckn must be CryptoServiceKey or None, got {type(value).__name__}"
            )
        self._ckn = value
        # Tags: atp.
        # Status=candidate.
        self._cryptoAlgo: Optional["MacSecCryptoAlgo"] = None

    @property
    def crypto_algo(self) -> Optional["MacSecCryptoAlgo"]:
        """Get cryptoAlgo (Pythonic accessor)."""
        return self._cryptoAlgo

    @crypto_algo.setter
    def crypto_algo(self, value: Optional["MacSecCryptoAlgo"]) -> None:
        """
        Set cryptoAlgo with validation.

        Args:
            value: The cryptoAlgo to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cryptoAlgo = None
            return

        if not isinstance(value, MacSecCryptoAlgo):
            raise TypeError(
                f"cryptoAlgo must be MacSecCryptoAlgo or None, got {type(value).__name__}"
            )
        self._cryptoAlgo = value
        self._sak: Optional["CryptoServiceKey"] = None

    @property
    def sak(self) -> Optional["CryptoServiceKey"]:
        """Get sak (Pythonic accessor)."""
        return self._sak

    @sak.setter
    def sak(self, value: Optional["CryptoServiceKey"]) -> None:
        """
        Set sak with validation.

        Args:
            value: The sak to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sak = None
            return

        if not isinstance(value, CryptoServiceKey):
            raise TypeError(
                f"sak must be CryptoServiceKey or None, got {type(value).__name__}"
            )
        self._sak = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCkn(self) -> "CryptoServiceKey":
        """
        AUTOSAR-compliant getter for ckn.

        Returns:
            The ckn value

        Note:
            Delegates to ckn property (CODING_RULE_V2_00017)
        """
        return self.ckn  # Delegates to property

    def setCkn(self, value: "CryptoServiceKey") -> "MacSecKayParticipant":
        """
        AUTOSAR-compliant setter for ckn with method chaining.

        Args:
            value: The ckn to set

        Returns:
            self for method chaining

        Note:
            Delegates to ckn property setter (gets validation automatically)
        """
        self.ckn = value  # Delegates to property setter
        return self

    def getCryptoAlgo(self) -> "MacSecCryptoAlgo":
        """
        AUTOSAR-compliant getter for cryptoAlgo.

        Returns:
            The cryptoAlgo value

        Note:
            Delegates to crypto_algo property (CODING_RULE_V2_00017)
        """
        return self.crypto_algo  # Delegates to property

    def setCryptoAlgo(self, value: "MacSecCryptoAlgo") -> "MacSecKayParticipant":
        """
        AUTOSAR-compliant setter for cryptoAlgo with method chaining.

        Args:
            value: The cryptoAlgo to set

        Returns:
            self for method chaining

        Note:
            Delegates to crypto_algo property setter (gets validation automatically)
        """
        self.crypto_algo = value  # Delegates to property setter
        return self

    def getSak(self) -> "CryptoServiceKey":
        """
        AUTOSAR-compliant getter for sak.

        Returns:
            The sak value

        Note:
            Delegates to sak property (CODING_RULE_V2_00017)
        """
        return self.sak  # Delegates to property

    def setSak(self, value: "CryptoServiceKey") -> "MacSecKayParticipant":
        """
        AUTOSAR-compliant setter for sak with method chaining.

        Args:
            value: The sak to set

        Returns:
            self for method chaining

        Note:
            Delegates to sak property setter (gets validation automatically)
        """
        self.sak = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ckn(self, value: Optional["CryptoServiceKey"]) -> "MacSecKayParticipant":
        """
        Set ckn and return self for chaining.

        Args:
            value: The ckn to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ckn("value")
        """
        self.ckn = value  # Use property setter (gets validation)
        return self

    def with_crypto_algo(self, value: Optional["MacSecCryptoAlgo"]) -> "MacSecKayParticipant":
        """
        Set cryptoAlgo and return self for chaining.

        Args:
            value: The cryptoAlgo to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_crypto_algo("value")
        """
        self.crypto_algo = value  # Use property setter (gets validation)
        return self

    def with_sak(self, value: Optional["CryptoServiceKey"]) -> "MacSecKayParticipant":
        """
        Set sak and return self for chaining.

        Args:
            value: The sak to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sak("value")
        """
        self.sak = value  # Use property setter (gets validation)
        return self



class MacSecCryptoAlgoConfig(ARObject):
    """
    This meta-class defines the cryptography configuration for MACsec.

    Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication::MacSecCryptoAlgoConfig

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 175, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the MACsec capability.
        self._capability: Optional["MacSecCapabilityEnum"] = None

    @property
    def capability(self) -> Optional["MacSecCapabilityEnum"]:
        """Get capability (Pythonic accessor)."""
        return self._capability

    @capability.setter
    def capability(self, value: Optional["MacSecCapabilityEnum"]) -> None:
        """
        Set capability with validation.

        Args:
            value: The capability to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._capability = None
            return

        if not isinstance(value, MacSecCapabilityEnum):
            raise TypeError(
                f"capability must be MacSecCapabilityEnum or None, got {type(value).__name__}"
            )
        self._capability = value
        # Status=candidate.
        self._cipherSuite: "MacSecCipherSuite" = None

    @property
    def cipher_suite(self) -> "MacSecCipherSuite":
        """Get cipherSuite (Pythonic accessor)."""
        return self._cipherSuite

    @cipher_suite.setter
    def cipher_suite(self, value: "MacSecCipherSuite") -> None:
        """
        Set cipherSuite with validation.

        Args:
            value: The cipherSuite to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, MacSecCipherSuite):
            raise TypeError(
                f"cipherSuite must be MacSecCipherSuite, got {type(value).__name__}"
            )
        self._cipherSuite = value
                # the frame header.
        # MACsec encrypts bytes after the offset in a frame.
        self._confidentiality: Optional["MacSecConfidentiality"] = None

    @property
    def confidentiality(self) -> Optional["MacSecConfidentiality"]:
        """Get confidentiality (Pythonic accessor)."""
        return self._confidentiality

    @confidentiality.setter
    def confidentiality(self, value: Optional["MacSecConfidentiality"]) -> None:
        """
        Set confidentiality with validation.

        Args:
            value: The confidentiality to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._confidentiality = None
            return

        if not isinstance(value, MacSecConfidentiality):
            raise TypeError(
                f"confidentiality must be MacSecConfidentiality or None, got {type(value).__name__}"
            )
        self._confidentiality = value
        # window.
        self._replayProtection: Optional["PositiveInteger"] = None

    @property
    def replay_protection(self) -> Optional["PositiveInteger"]:
        """Get replayProtection (Pythonic accessor)."""
        return self._replayProtection

    @replay_protection.setter
    def replay_protection(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set replayProtection with validation.

        Args:
            value: The replayProtection to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._replayProtection = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"replayProtection must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._replayProtection = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCapability(self) -> "MacSecCapabilityEnum":
        """
        AUTOSAR-compliant getter for capability.

        Returns:
            The capability value

        Note:
            Delegates to capability property (CODING_RULE_V2_00017)
        """
        return self.capability  # Delegates to property

    def setCapability(self, value: "MacSecCapabilityEnum") -> "MacSecCryptoAlgoConfig":
        """
        AUTOSAR-compliant setter for capability with method chaining.

        Args:
            value: The capability to set

        Returns:
            self for method chaining

        Note:
            Delegates to capability property setter (gets validation automatically)
        """
        self.capability = value  # Delegates to property setter
        return self

    def getCipherSuite(self) -> "MacSecCipherSuite":
        """
        AUTOSAR-compliant getter for cipherSuite.

        Returns:
            The cipherSuite value

        Note:
            Delegates to cipher_suite property (CODING_RULE_V2_00017)
        """
        return self.cipher_suite  # Delegates to property

    def setCipherSuite(self, value: "MacSecCipherSuite") -> "MacSecCryptoAlgoConfig":
        """
        AUTOSAR-compliant setter for cipherSuite with method chaining.

        Args:
            value: The cipherSuite to set

        Returns:
            self for method chaining

        Note:
            Delegates to cipher_suite property setter (gets validation automatically)
        """
        self.cipher_suite = value  # Delegates to property setter
        return self

    def getConfidentiality(self) -> "MacSecConfidentiality":
        """
        AUTOSAR-compliant getter for confidentiality.

        Returns:
            The confidentiality value

        Note:
            Delegates to confidentiality property (CODING_RULE_V2_00017)
        """
        return self.confidentiality  # Delegates to property

    def setConfidentiality(self, value: "MacSecConfidentiality") -> "MacSecCryptoAlgoConfig":
        """
        AUTOSAR-compliant setter for confidentiality with method chaining.

        Args:
            value: The confidentiality to set

        Returns:
            self for method chaining

        Note:
            Delegates to confidentiality property setter (gets validation automatically)
        """
        self.confidentiality = value  # Delegates to property setter
        return self

    def getReplayProtection(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for replayProtection.

        Returns:
            The replayProtection value

        Note:
            Delegates to replay_protection property (CODING_RULE_V2_00017)
        """
        return self.replay_protection  # Delegates to property

    def setReplayProtection(self, value: "PositiveInteger") -> "MacSecCryptoAlgoConfig":
        """
        AUTOSAR-compliant setter for replayProtection with method chaining.

        Args:
            value: The replayProtection to set

        Returns:
            self for method chaining

        Note:
            Delegates to replay_protection property setter (gets validation automatically)
        """
        self.replay_protection = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_capability(self, value: Optional["MacSecCapabilityEnum"]) -> "MacSecCryptoAlgoConfig":
        """
        Set capability and return self for chaining.

        Args:
            value: The capability to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_capability("value")
        """
        self.capability = value  # Use property setter (gets validation)
        return self

    def with_cipher_suite(self, value: "MacSecCipherSuite") -> "MacSecCryptoAlgoConfig":
        """
        Set cipherSuite and return self for chaining.

        Args:
            value: The cipherSuite to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_cipher_suite("value")
        """
        self.cipher_suite = value  # Use property setter (gets validation)
        return self

    def with_confidentiality(self, value: Optional["MacSecConfidentiality"]) -> "MacSecCryptoAlgoConfig":
        """
        Set confidentiality and return self for chaining.

        Args:
            value: The confidentiality to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_confidentiality("value")
        """
        self.confidentiality = value  # Use property setter (gets validation)
        return self

    def with_replay_protection(self, value: Optional["PositiveInteger"]) -> "MacSecCryptoAlgoConfig":
        """
        Set replayProtection and return self for chaining.

        Args:
            value: The replayProtection to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_replay_protection("value")
        """
        self.replay_protection = value  # Use property setter (gets validation)
        return self



class MacSecCipherSuiteConfig(ARObject):
    """
    This meta-class defines the cipher suite configuration to use with MACsec.
    cipherSuitePriority is present in case the MKA instance acts as a Key Server
    to select the cipher suite to use for MACsec. (cid:53) 175 of 2090 Document
    ID 63: AUTOSAR_CP_TPS_SystemTemplate System Template AUTOSAR CP R23-11
    (cid:52)

    Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication::MacSecCipherSuiteConfig

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 175, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # In case the MKA instance acts as a Key Server, the is used to select the
        # Cipher Suite to use with the supported Ciphers.
        self._cipherSuite: Optional["PositiveInteger"] = None

    @property
    def cipher_suite(self) -> Optional["PositiveInteger"]:
        """Get cipherSuite (Pythonic accessor)."""
        return self._cipherSuite

    @cipher_suite.setter
    def cipher_suite(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set cipherSuite with validation.

        Args:
            value: The cipherSuite to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cipherSuite = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"cipherSuite must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._cipherSuite = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCipherSuite(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for cipherSuite.

        Returns:
            The cipherSuite value

        Note:
            Delegates to cipher_suite property (CODING_RULE_V2_00017)
        """
        return self.cipher_suite  # Delegates to property

    def setCipherSuite(self, value: "PositiveInteger") -> "MacSecCipherSuiteConfig":
        """
        AUTOSAR-compliant setter for cipherSuite with method chaining.

        Args:
            value: The cipherSuite to set

        Returns:
            self for method chaining

        Note:
            Delegates to cipher_suite property setter (gets validation automatically)
        """
        self.cipher_suite = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_cipher_suite(self, value: Optional["PositiveInteger"]) -> "MacSecCipherSuiteConfig":
        """
        Set cipherSuite and return self for chaining.

        Args:
            value: The cipherSuite to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_cipher_suite("value")
        """
        self.cipher_suite = value  # Use property setter (gets validation)
        return self



class CryptoServiceMapping(Identifiable, ABC):
    """
    This meta-class represents an abstract base class for specializations of
    crypto service mappings.

    Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication::CryptoServiceMapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 375, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is CryptoServiceMapping:
            raise TypeError("CryptoServiceMapping is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class CryptoServicePrimitive(ARElement):
    """
    This meta-class has the ability to represent a crypto primitive.

    Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication::CryptoServicePrimitive

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 376, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 59, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represents a description of the family (e.
        # g.
        # crypto algorithm implemented by the crypto.
        self._algorithmFamily: Optional["String"] = None

    @property
    def algorithm_family(self) -> Optional["String"]:
        """Get algorithmFamily (Pythonic accessor)."""
        return self._algorithmFamily

    @algorithm_family.setter
    def algorithm_family(self, value: Optional["String"]) -> None:
        """
        Set algorithmFamily with validation.

        Args:
            value: The algorithmFamily to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._algorithmFamily = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"algorithmFamily must be String or str or None, got {type(value).__name__}"
            )
        self._algorithmFamily = value
        # crypto primitive.
        self._algorithmMode: Optional["String"] = None

    @property
    def algorithm_mode(self) -> Optional["String"]:
        """Get algorithmMode (Pythonic accessor)."""
        return self._algorithmMode

    @algorithm_mode.setter
    def algorithm_mode(self, value: Optional["String"]) -> None:
        """
        Set algorithmMode with validation.

        Args:
            value: The algorithmMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._algorithmMode = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"algorithmMode must be String or str or None, got {type(value).__name__}"
            )
        self._algorithmMode = value
                # algorithm implemented by the primitive.
        # family is needed for the specification of algorithm for a signature check, e.
        # g.
        # using RSA.
        self._algorithm: Optional["String"] = None

    @property
    def algorithm(self) -> Optional["String"]:
        """Get algorithm (Pythonic accessor)."""
        return self._algorithm

    @algorithm.setter
    def algorithm(self, value: Optional["String"]) -> None:
        """
        Set algorithm with validation.

        Args:
            value: The algorithm to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._algorithm = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"algorithm must be String or str or None, got {type(value).__name__}"
            )
        self._algorithm = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAlgorithmFamily(self) -> "String":
        """
        AUTOSAR-compliant getter for algorithmFamily.

        Returns:
            The algorithmFamily value

        Note:
            Delegates to algorithm_family property (CODING_RULE_V2_00017)
        """
        return self.algorithm_family  # Delegates to property

    def setAlgorithmFamily(self, value: "String") -> "CryptoServicePrimitive":
        """
        AUTOSAR-compliant setter for algorithmFamily with method chaining.

        Args:
            value: The algorithmFamily to set

        Returns:
            self for method chaining

        Note:
            Delegates to algorithm_family property setter (gets validation automatically)
        """
        self.algorithm_family = value  # Delegates to property setter
        return self

    def getAlgorithmMode(self) -> "String":
        """
        AUTOSAR-compliant getter for algorithmMode.

        Returns:
            The algorithmMode value

        Note:
            Delegates to algorithm_mode property (CODING_RULE_V2_00017)
        """
        return self.algorithm_mode  # Delegates to property

    def setAlgorithmMode(self, value: "String") -> "CryptoServicePrimitive":
        """
        AUTOSAR-compliant setter for algorithmMode with method chaining.

        Args:
            value: The algorithmMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to algorithm_mode property setter (gets validation automatically)
        """
        self.algorithm_mode = value  # Delegates to property setter
        return self

    def getAlgorithm(self) -> "String":
        """
        AUTOSAR-compliant getter for algorithm.

        Returns:
            The algorithm value

        Note:
            Delegates to algorithm property (CODING_RULE_V2_00017)
        """
        return self.algorithm  # Delegates to property

    def setAlgorithm(self, value: "String") -> "CryptoServicePrimitive":
        """
        AUTOSAR-compliant setter for algorithm with method chaining.

        Args:
            value: The algorithm to set

        Returns:
            self for method chaining

        Note:
            Delegates to algorithm property setter (gets validation automatically)
        """
        self.algorithm = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_algorithm_family(self, value: Optional["String"]) -> "CryptoServicePrimitive":
        """
        Set algorithmFamily and return self for chaining.

        Args:
            value: The algorithmFamily to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_algorithm_family("value")
        """
        self.algorithm_family = value  # Use property setter (gets validation)
        return self

    def with_algorithm_mode(self, value: Optional["String"]) -> "CryptoServicePrimitive":
        """
        Set algorithmMode and return self for chaining.

        Args:
            value: The algorithmMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_algorithm_mode("value")
        """
        self.algorithm_mode = value  # Use property setter (gets validation)
        return self

    def with_algorithm(self, value: Optional["String"]) -> "CryptoServicePrimitive":
        """
        Set algorithm and return self for chaining.

        Args:
            value: The algorithm to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_algorithm("value")
        """
        self.algorithm = value  # Use property setter (gets validation)
        return self



class CryptoServiceKey(ARElement):
    """
    This meta-class has the ability to represent a crypto key.

    Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication::CryptoServiceKey

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 377, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 58, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represent the description of the family of the algorithm.
        self._algorithmFamily: Optional["String"] = None

    @property
    def algorithm_family(self) -> Optional["String"]:
        """Get algorithmFamily (Pythonic accessor)."""
        return self._algorithmFamily

    @algorithm_family.setter
    def algorithm_family(self, value: Optional["String"]) -> None:
        """
        Set algorithmFamily with validation.

        Args:
            value: The algorithmFamily to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._algorithmFamily = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"algorithmFamily must be String or str or None, got {type(value).__name__}"
            )
        self._algorithmFamily = value
        # as part of the system value can then be taken for the the respective ECU.
        self._development: Optional["ValueSpecification"] = None

    @property
    def development(self) -> Optional["ValueSpecification"]:
        """Get development (Pythonic accessor)."""
        return self._development

    @development.setter
    def development(self, value: Optional["ValueSpecification"]) -> None:
        """
        Set development with validation.

        Args:
            value: The development to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._development = None
            return

        if not isinstance(value, ValueSpecification):
            raise TypeError(
                f"development must be ValueSpecification or None, got {type(value).__name__}"
            )
        self._development = value
        self._keyGeneration: Optional["CryptoServiceKey"] = None

    @property
    def key_generation(self) -> Optional["CryptoServiceKey"]:
        """Get keyGeneration (Pythonic accessor)."""
        return self._keyGeneration

    @key_generation.setter
    def key_generation(self, value: Optional["CryptoServiceKey"]) -> None:
        """
        Set keyGeneration with validation.

        Args:
            value: The keyGeneration to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._keyGeneration = None
            return

        if not isinstance(value, CryptoServiceKey):
            raise TypeError(
                f"keyGeneration must be CryptoServiceKey or None, got {type(value).__name__}"
            )
        self._keyGeneration = value
        # AUTOSAR reserves for this attributes but it is possible to insert as well.
        self._keyStorageType: Optional["String"] = None

    @property
    def key_storage_type(self) -> Optional["String"]:
        """Get keyStorageType (Pythonic accessor)."""
        return self._keyStorageType

    @key_storage_type.setter
    def key_storage_type(self, value: Optional["String"]) -> None:
        """
        Set keyStorageType with validation.

        Args:
            value: The keyStorageType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._keyStorageType = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"keyStorageType must be String or str or None, got {type(value).__name__}"
            )
        self._keyStorageType = value
        self._length: Optional["PositiveInteger"] = None

    @property
    def length(self) -> Optional["PositiveInteger"]:
        """Get length (Pythonic accessor)."""
        return self._length

    @length.setter
    def length(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set length with validation.

        Args:
            value: The length to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._length = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"length must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._length = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAlgorithmFamily(self) -> "String":
        """
        AUTOSAR-compliant getter for algorithmFamily.

        Returns:
            The algorithmFamily value

        Note:
            Delegates to algorithm_family property (CODING_RULE_V2_00017)
        """
        return self.algorithm_family  # Delegates to property

    def setAlgorithmFamily(self, value: "String") -> "CryptoServiceKey":
        """
        AUTOSAR-compliant setter for algorithmFamily with method chaining.

        Args:
            value: The algorithmFamily to set

        Returns:
            self for method chaining

        Note:
            Delegates to algorithm_family property setter (gets validation automatically)
        """
        self.algorithm_family = value  # Delegates to property setter
        return self

    def getDevelopment(self) -> "ValueSpecification":
        """
        AUTOSAR-compliant getter for development.

        Returns:
            The development value

        Note:
            Delegates to development property (CODING_RULE_V2_00017)
        """
        return self.development  # Delegates to property

    def setDevelopment(self, value: "ValueSpecification") -> "CryptoServiceKey":
        """
        AUTOSAR-compliant setter for development with method chaining.

        Args:
            value: The development to set

        Returns:
            self for method chaining

        Note:
            Delegates to development property setter (gets validation automatically)
        """
        self.development = value  # Delegates to property setter
        return self

    def getKeyGeneration(self) -> "CryptoServiceKey":
        """
        AUTOSAR-compliant getter for keyGeneration.

        Returns:
            The keyGeneration value

        Note:
            Delegates to key_generation property (CODING_RULE_V2_00017)
        """
        return self.key_generation  # Delegates to property

    def setKeyGeneration(self, value: "CryptoServiceKey") -> "CryptoServiceKey":
        """
        AUTOSAR-compliant setter for keyGeneration with method chaining.

        Args:
            value: The keyGeneration to set

        Returns:
            self for method chaining

        Note:
            Delegates to key_generation property setter (gets validation automatically)
        """
        self.key_generation = value  # Delegates to property setter
        return self

    def getKeyStorageType(self) -> "String":
        """
        AUTOSAR-compliant getter for keyStorageType.

        Returns:
            The keyStorageType value

        Note:
            Delegates to key_storage_type property (CODING_RULE_V2_00017)
        """
        return self.key_storage_type  # Delegates to property

    def setKeyStorageType(self, value: "String") -> "CryptoServiceKey":
        """
        AUTOSAR-compliant setter for keyStorageType with method chaining.

        Args:
            value: The keyStorageType to set

        Returns:
            self for method chaining

        Note:
            Delegates to key_storage_type property setter (gets validation automatically)
        """
        self.key_storage_type = value  # Delegates to property setter
        return self

    def getLength(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for length.

        Returns:
            The length value

        Note:
            Delegates to length property (CODING_RULE_V2_00017)
        """
        return self.length  # Delegates to property

    def setLength(self, value: "PositiveInteger") -> "CryptoServiceKey":
        """
        AUTOSAR-compliant setter for length with method chaining.

        Args:
            value: The length to set

        Returns:
            self for method chaining

        Note:
            Delegates to length property setter (gets validation automatically)
        """
        self.length = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_algorithm_family(self, value: Optional["String"]) -> "CryptoServiceKey":
        """
        Set algorithmFamily and return self for chaining.

        Args:
            value: The algorithmFamily to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_algorithm_family("value")
        """
        self.algorithm_family = value  # Use property setter (gets validation)
        return self

    def with_development(self, value: Optional["ValueSpecification"]) -> "CryptoServiceKey":
        """
        Set development and return self for chaining.

        Args:
            value: The development to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_development("value")
        """
        self.development = value  # Use property setter (gets validation)
        return self

    def with_key_generation(self, value: Optional["CryptoServiceKey"]) -> "CryptoServiceKey":
        """
        Set keyGeneration and return self for chaining.

        Args:
            value: The keyGeneration to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_key_generation("value")
        """
        self.key_generation = value  # Use property setter (gets validation)
        return self

    def with_key_storage_type(self, value: Optional["String"]) -> "CryptoServiceKey":
        """
        Set keyStorageType and return self for chaining.

        Args:
            value: The keyStorageType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_key_storage_type("value")
        """
        self.key_storage_type = value  # Use property setter (gets validation)
        return self

    def with_length(self, value: Optional["PositiveInteger"]) -> "CryptoServiceKey":
        """
        Set length and return self for chaining.

        Args:
            value: The length to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_length("value")
        """
        self.length = value  # Use property setter (gets validation)
        return self



class CryptoServiceQueue(ARElement):
    """
    This meta-class has the ability to represent a crypto queue.

    Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication::CryptoServiceQueue

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 381, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the queue size of the CryptoServiceQueue.
        self._queueSize: Optional["PositiveInteger"] = None

    @property
    def queue_size(self) -> Optional["PositiveInteger"]:
        """Get queueSize (Pythonic accessor)."""
        return self._queueSize

    @queue_size.setter
    def queue_size(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set queueSize with validation.

        Args:
            value: The queueSize to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._queueSize = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"queueSize must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._queueSize = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getQueueSize(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for queueSize.

        Returns:
            The queueSize value

        Note:
            Delegates to queue_size property (CODING_RULE_V2_00017)
        """
        return self.queue_size  # Delegates to property

    def setQueueSize(self, value: "PositiveInteger") -> "CryptoServiceQueue":
        """
        AUTOSAR-compliant setter for queueSize with method chaining.

        Args:
            value: The queueSize to set

        Returns:
            self for method chaining

        Note:
            Delegates to queue_size property setter (gets validation automatically)
        """
        self.queue_size = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_queue_size(self, value: Optional["PositiveInteger"]) -> "CryptoServiceQueue":
        """
        Set queueSize and return self for chaining.

        Args:
            value: The queueSize to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_queue_size("value")
        """
        self.queue_size = value  # Use property setter (gets validation)
        return self



class TlsCryptoCipherSuite(Identifiable):
    """
    This meta-class represents a cipher suite for describing cryptographic
    operations in the context of establishing a connection of
    ApplicationEndpoints that is protected by TLS.

    Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication::TlsCryptoCipherSuite

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 562, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference identifies the crypto service primitive for and verification
        # of MACs.
        self._authentication: Optional["CryptoServicePrimitive"] = None

    @property
    def authentication(self) -> Optional["CryptoServicePrimitive"]:
        """Get authentication (Pythonic accessor)."""
        return self._authentication

    @authentication.setter
    def authentication(self, value: Optional["CryptoServicePrimitive"]) -> None:
        """
        Set authentication with validation.

        Args:
            value: The authentication to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._authentication = None
            return

        if not isinstance(value, CryptoServicePrimitive):
            raise TypeError(
                f"authentication must be CryptoServicePrimitive or None, got {type(value).__name__}"
            )
        self._authentication = value
        self._certificate: Optional["CryptoService"] = None

    @property
    def certificate(self) -> Optional["CryptoService"]:
        """Get certificate (Pythonic accessor)."""
        return self._certificate

    @certificate.setter
    def certificate(self, value: Optional["CryptoService"]) -> None:
        """
        Set certificate with validation.

        Args:
            value: The certificate to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._certificate = None
            return

        if not isinstance(value, CryptoService):
            raise TypeError(
                f"certificate must be CryptoService or None, got {type(value).__name__}"
            )
        self._certificate = value
        self._cipherSuiteId: Optional["PositiveInteger"] = None

    @property
    def cipher_suite_id(self) -> Optional["PositiveInteger"]:
        """Get cipherSuiteId (Pythonic accessor)."""
        return self._cipherSuiteId

    @cipher_suite_id.setter
    def cipher_suite_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set cipherSuiteId with validation.

        Args:
            value: The cipherSuiteId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cipherSuiteId = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"cipherSuiteId must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._cipherSuiteId = value
        self._cipherSuite: Optional["String"] = None

    @property
    def cipher_suite(self) -> Optional["String"]:
        """Get cipherSuite (Pythonic accessor)."""
        return self._cipherSuite

    @cipher_suite.setter
    def cipher_suite(self, value: Optional["String"]) -> None:
        """
        Set cipherSuite with validation.

        Args:
            value: The cipherSuite to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cipherSuite = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"cipherSuite must be String or str or None, got {type(value).__name__}"
            )
        self._cipherSuite = value
        self._ellipticCurve: List["CryptoEllipticCurve"] = []

    @property
    def elliptic_curve(self) -> List["CryptoEllipticCurve"]:
        """Get ellipticCurve (Pythonic accessor)."""
        return self._ellipticCurve
        # This reference identifies the crypto service primitive for of encryption.
        self._encryption: Optional["CryptoServicePrimitive"] = None

    @property
    def encryption(self) -> Optional["CryptoServicePrimitive"]:
        """Get encryption (Pythonic accessor)."""
        return self._encryption

    @encryption.setter
    def encryption(self, value: Optional["CryptoServicePrimitive"]) -> None:
        """
        Set encryption with validation.

        Args:
            value: The encryption to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._encryption = None
            return

        if not isinstance(value, CryptoServicePrimitive):
            raise TypeError(
                f"encryption must be CryptoServicePrimitive or None, got {type(value).__name__}"
            )
        self._encryption = value
        # verification of signatures during the algorithm.
        self._keyExchange: List["CryptoServicePrimitive"] = []

    @property
    def key_exchange(self) -> List["CryptoServicePrimitive"]:
        """Get keyExchange (Pythonic accessor)."""
        return self._keyExchange
        # This attribute identifies the priority of the cipher suite.
        # Lower values represent higher.
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

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"priority must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._priority = value
        self._props: Optional["TlsCryptoCipherSuite"] = None

    @property
    def props(self) -> Optional["TlsCryptoCipherSuite"]:
        """Get props (Pythonic accessor)."""
        return self._props

    @props.setter
    def props(self, value: Optional["TlsCryptoCipherSuite"]) -> None:
        """
        Set props with validation.

        Args:
            value: The props to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._props = None
            return

        if not isinstance(value, TlsCryptoCipherSuite):
            raise TypeError(
                f"props must be TlsCryptoCipherSuite or None, got {type(value).__name__}"
            )
        self._props = value
        # establish a TLS the handshake is based on the existence of key.
        self._pskIdentity: Optional["TlsPskIdentity"] = None

    @property
    def psk_identity(self) -> Optional["TlsPskIdentity"]:
        """Get pskIdentity (Pythonic accessor)."""
        return self._pskIdentity

    @psk_identity.setter
    def psk_identity(self, value: Optional["TlsPskIdentity"]) -> None:
        """
        Set pskIdentity with validation.

        Args:
            value: The pskIdentity to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pskIdentity = None
            return

        if not isinstance(value, TlsPskIdentity):
            raise TypeError(
                f"pskIdentity must be TlsPskIdentity or None, got {type(value).__name__}"
            )
        self._pskIdentity = value
        self._remote: Optional["CryptoService"] = None

    @property
    def remote(self) -> Optional["CryptoService"]:
        """Get remote (Pythonic accessor)."""
        return self._remote

    @remote.setter
    def remote(self, value: Optional["CryptoService"]) -> None:
        """
        Set remote with validation.

        Args:
            value: The remote to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._remote = None
            return

        if not isinstance(value, CryptoService):
            raise TypeError(
                f"remote must be CryptoService or None, got {type(value).__name__}"
            )
        self._remote = value
        self._signature: List["CryptoSignature"] = []

    @property
    def signature(self) -> List["CryptoSignature"]:
        """Get signature (Pythonic accessor)."""
        return self._signature
        # This attribute supports the definition of the applicable TLS.
        self._version: Optional["TlsVersionEnum"] = None

    @property
    def version(self) -> Optional["TlsVersionEnum"]:
        """Get version (Pythonic accessor)."""
        return self._version

    @version.setter
    def version(self, value: Optional["TlsVersionEnum"]) -> None:
        """
        Set version with validation.

        Args:
            value: The version to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._version = None
            return

        if not isinstance(value, TlsVersionEnum):
            raise TypeError(
                f"version must be TlsVersionEnum or None, got {type(value).__name__}"
            )
        self._version = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAuthentication(self) -> "CryptoServicePrimitive":
        """
        AUTOSAR-compliant getter for authentication.

        Returns:
            The authentication value

        Note:
            Delegates to authentication property (CODING_RULE_V2_00017)
        """
        return self.authentication  # Delegates to property

    def setAuthentication(self, value: "CryptoServicePrimitive") -> "TlsCryptoCipherSuite":
        """
        AUTOSAR-compliant setter for authentication with method chaining.

        Args:
            value: The authentication to set

        Returns:
            self for method chaining

        Note:
            Delegates to authentication property setter (gets validation automatically)
        """
        self.authentication = value  # Delegates to property setter
        return self

    def getCertificate(self) -> "CryptoService":
        """
        AUTOSAR-compliant getter for certificate.

        Returns:
            The certificate value

        Note:
            Delegates to certificate property (CODING_RULE_V2_00017)
        """
        return self.certificate  # Delegates to property

    def setCertificate(self, value: "CryptoService") -> "TlsCryptoCipherSuite":
        """
        AUTOSAR-compliant setter for certificate with method chaining.

        Args:
            value: The certificate to set

        Returns:
            self for method chaining

        Note:
            Delegates to certificate property setter (gets validation automatically)
        """
        self.certificate = value  # Delegates to property setter
        return self

    def getCipherSuiteId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for cipherSuiteId.

        Returns:
            The cipherSuiteId value

        Note:
            Delegates to cipher_suite_id property (CODING_RULE_V2_00017)
        """
        return self.cipher_suite_id  # Delegates to property

    def setCipherSuiteId(self, value: "PositiveInteger") -> "TlsCryptoCipherSuite":
        """
        AUTOSAR-compliant setter for cipherSuiteId with method chaining.

        Args:
            value: The cipherSuiteId to set

        Returns:
            self for method chaining

        Note:
            Delegates to cipher_suite_id property setter (gets validation automatically)
        """
        self.cipher_suite_id = value  # Delegates to property setter
        return self

    def getCipherSuite(self) -> "String":
        """
        AUTOSAR-compliant getter for cipherSuite.

        Returns:
            The cipherSuite value

        Note:
            Delegates to cipher_suite property (CODING_RULE_V2_00017)
        """
        return self.cipher_suite  # Delegates to property

    def setCipherSuite(self, value: "String") -> "TlsCryptoCipherSuite":
        """
        AUTOSAR-compliant setter for cipherSuite with method chaining.

        Args:
            value: The cipherSuite to set

        Returns:
            self for method chaining

        Note:
            Delegates to cipher_suite property setter (gets validation automatically)
        """
        self.cipher_suite = value  # Delegates to property setter
        return self

    def getEllipticCurve(self) -> List["CryptoEllipticCurve"]:
        """
        AUTOSAR-compliant getter for ellipticCurve.

        Returns:
            The ellipticCurve value

        Note:
            Delegates to elliptic_curve property (CODING_RULE_V2_00017)
        """
        return self.elliptic_curve  # Delegates to property

    def getEncryption(self) -> "CryptoServicePrimitive":
        """
        AUTOSAR-compliant getter for encryption.

        Returns:
            The encryption value

        Note:
            Delegates to encryption property (CODING_RULE_V2_00017)
        """
        return self.encryption  # Delegates to property

    def setEncryption(self, value: "CryptoServicePrimitive") -> "TlsCryptoCipherSuite":
        """
        AUTOSAR-compliant setter for encryption with method chaining.

        Args:
            value: The encryption to set

        Returns:
            self for method chaining

        Note:
            Delegates to encryption property setter (gets validation automatically)
        """
        self.encryption = value  # Delegates to property setter
        return self

    def getKeyExchange(self) -> List["CryptoServicePrimitive"]:
        """
        AUTOSAR-compliant getter for keyExchange.

        Returns:
            The keyExchange value

        Note:
            Delegates to key_exchange property (CODING_RULE_V2_00017)
        """
        return self.key_exchange  # Delegates to property

    def getPriority(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for priority.

        Returns:
            The priority value

        Note:
            Delegates to priority property (CODING_RULE_V2_00017)
        """
        return self.priority  # Delegates to property

    def setPriority(self, value: "PositiveInteger") -> "TlsCryptoCipherSuite":
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

    def getProps(self) -> "TlsCryptoCipherSuite":
        """
        AUTOSAR-compliant getter for props.

        Returns:
            The props value

        Note:
            Delegates to props property (CODING_RULE_V2_00017)
        """
        return self.props  # Delegates to property

    def setProps(self, value: "TlsCryptoCipherSuite") -> "TlsCryptoCipherSuite":
        """
        AUTOSAR-compliant setter for props with method chaining.

        Args:
            value: The props to set

        Returns:
            self for method chaining

        Note:
            Delegates to props property setter (gets validation automatically)
        """
        self.props = value  # Delegates to property setter
        return self

    def getPskIdentity(self) -> "TlsPskIdentity":
        """
        AUTOSAR-compliant getter for pskIdentity.

        Returns:
            The pskIdentity value

        Note:
            Delegates to psk_identity property (CODING_RULE_V2_00017)
        """
        return self.psk_identity  # Delegates to property

    def setPskIdentity(self, value: "TlsPskIdentity") -> "TlsCryptoCipherSuite":
        """
        AUTOSAR-compliant setter for pskIdentity with method chaining.

        Args:
            value: The pskIdentity to set

        Returns:
            self for method chaining

        Note:
            Delegates to psk_identity property setter (gets validation automatically)
        """
        self.psk_identity = value  # Delegates to property setter
        return self

    def getRemote(self) -> "CryptoService":
        """
        AUTOSAR-compliant getter for remote.

        Returns:
            The remote value

        Note:
            Delegates to remote property (CODING_RULE_V2_00017)
        """
        return self.remote  # Delegates to property

    def setRemote(self, value: "CryptoService") -> "TlsCryptoCipherSuite":
        """
        AUTOSAR-compliant setter for remote with method chaining.

        Args:
            value: The remote to set

        Returns:
            self for method chaining

        Note:
            Delegates to remote property setter (gets validation automatically)
        """
        self.remote = value  # Delegates to property setter
        return self

    def getSignature(self) -> List["CryptoSignature"]:
        """
        AUTOSAR-compliant getter for signature.

        Returns:
            The signature value

        Note:
            Delegates to signature property (CODING_RULE_V2_00017)
        """
        return self.signature  # Delegates to property

    def getVersion(self) -> "TlsVersionEnum":
        """
        AUTOSAR-compliant getter for version.

        Returns:
            The version value

        Note:
            Delegates to version property (CODING_RULE_V2_00017)
        """
        return self.version  # Delegates to property

    def setVersion(self, value: "TlsVersionEnum") -> "TlsCryptoCipherSuite":
        """
        AUTOSAR-compliant setter for version with method chaining.

        Args:
            value: The version to set

        Returns:
            self for method chaining

        Note:
            Delegates to version property setter (gets validation automatically)
        """
        self.version = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_authentication(self, value: Optional["CryptoServicePrimitive"]) -> "TlsCryptoCipherSuite":
        """
        Set authentication and return self for chaining.

        Args:
            value: The authentication to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_authentication("value")
        """
        self.authentication = value  # Use property setter (gets validation)
        return self

    def with_certificate(self, value: Optional["CryptoService"]) -> "TlsCryptoCipherSuite":
        """
        Set certificate and return self for chaining.

        Args:
            value: The certificate to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_certificate("value")
        """
        self.certificate = value  # Use property setter (gets validation)
        return self

    def with_cipher_suite_id(self, value: Optional["PositiveInteger"]) -> "TlsCryptoCipherSuite":
        """
        Set cipherSuiteId and return self for chaining.

        Args:
            value: The cipherSuiteId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_cipher_suite_id("value")
        """
        self.cipher_suite_id = value  # Use property setter (gets validation)
        return self

    def with_cipher_suite(self, value: Optional["String"]) -> "TlsCryptoCipherSuite":
        """
        Set cipherSuite and return self for chaining.

        Args:
            value: The cipherSuite to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_cipher_suite("value")
        """
        self.cipher_suite = value  # Use property setter (gets validation)
        return self

    def with_encryption(self, value: Optional["CryptoServicePrimitive"]) -> "TlsCryptoCipherSuite":
        """
        Set encryption and return self for chaining.

        Args:
            value: The encryption to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_encryption("value")
        """
        self.encryption = value  # Use property setter (gets validation)
        return self

    def with_priority(self, value: Optional["PositiveInteger"]) -> "TlsCryptoCipherSuite":
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

    def with_props(self, value: Optional["TlsCryptoCipherSuite"]) -> "TlsCryptoCipherSuite":
        """
        Set props and return self for chaining.

        Args:
            value: The props to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_props("value")
        """
        self.props = value  # Use property setter (gets validation)
        return self

    def with_psk_identity(self, value: Optional["TlsPskIdentity"]) -> "TlsCryptoCipherSuite":
        """
        Set pskIdentity and return self for chaining.

        Args:
            value: The pskIdentity to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_psk_identity("value")
        """
        self.psk_identity = value  # Use property setter (gets validation)
        return self

    def with_remote(self, value: Optional["CryptoService"]) -> "TlsCryptoCipherSuite":
        """
        Set remote and return self for chaining.

        Args:
            value: The remote to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_remote("value")
        """
        self.remote = value  # Use property setter (gets validation)
        return self

    def with_version(self, value: Optional["TlsVersionEnum"]) -> "TlsCryptoCipherSuite":
        """
        Set version and return self for chaining.

        Args:
            value: The version to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_version("value")
        """
        self.version = value  # Use property setter (gets validation)
        return self



class TlsPskIdentity(ARObject):
    """
    This element is used to describe the pre-shared key shared during the
    handshake among the communication parties, to establish a TLS connection if
    the handshake is based on the existence of a pre-shared key.

    Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication::TlsPskIdentity

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 563, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference identifies the applicable cryptographic key.
        self._preSharedKey: Optional["CryptoServiceKey"] = None

    @property
    def pre_shared_key(self) -> Optional["CryptoServiceKey"]:
        """Get preSharedKey (Pythonic accessor)."""
        return self._preSharedKey

    @pre_shared_key.setter
    def pre_shared_key(self, value: Optional["CryptoServiceKey"]) -> None:
        """
        Set preSharedKey with validation.

        Args:
            value: The preSharedKey to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._preSharedKey = None
            return

        if not isinstance(value, CryptoServiceKey):
            raise TypeError(
                f"preSharedKey must be CryptoServiceKey or None, got {type(value).__name__}"
            )
        self._preSharedKey = value
        self._pskIdentity: Optional["String"] = None

    @property
    def psk_identity(self) -> Optional["String"]:
        """Get pskIdentity (Pythonic accessor)."""
        return self._pskIdentity

    @psk_identity.setter
    def psk_identity(self, value: Optional["String"]) -> None:
        """
        Set pskIdentity with validation.

        Args:
            value: The pskIdentity to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pskIdentity = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"pskIdentity must be String or str or None, got {type(value).__name__}"
            )
        self._pskIdentity = value
        self._pskIdentityHint: Optional["String"] = None

    @property
    def psk_identity_hint(self) -> Optional["String"]:
        """Get pskIdentityHint (Pythonic accessor)."""
        return self._pskIdentityHint

    @psk_identity_hint.setter
    def psk_identity_hint(self, value: Optional["String"]) -> None:
        """
        Set pskIdentityHint with validation.

        Args:
            value: The pskIdentityHint to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pskIdentityHint = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"pskIdentityHint must be String or str or None, got {type(value).__name__}"
            )
        self._pskIdentityHint = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPreSharedKey(self) -> "CryptoServiceKey":
        """
        AUTOSAR-compliant getter for preSharedKey.

        Returns:
            The preSharedKey value

        Note:
            Delegates to pre_shared_key property (CODING_RULE_V2_00017)
        """
        return self.pre_shared_key  # Delegates to property

    def setPreSharedKey(self, value: "CryptoServiceKey") -> "TlsPskIdentity":
        """
        AUTOSAR-compliant setter for preSharedKey with method chaining.

        Args:
            value: The preSharedKey to set

        Returns:
            self for method chaining

        Note:
            Delegates to pre_shared_key property setter (gets validation automatically)
        """
        self.pre_shared_key = value  # Delegates to property setter
        return self

    def getPskIdentity(self) -> "String":
        """
        AUTOSAR-compliant getter for pskIdentity.

        Returns:
            The pskIdentity value

        Note:
            Delegates to psk_identity property (CODING_RULE_V2_00017)
        """
        return self.psk_identity  # Delegates to property

    def setPskIdentity(self, value: "String") -> "TlsPskIdentity":
        """
        AUTOSAR-compliant setter for pskIdentity with method chaining.

        Args:
            value: The pskIdentity to set

        Returns:
            self for method chaining

        Note:
            Delegates to psk_identity property setter (gets validation automatically)
        """
        self.psk_identity = value  # Delegates to property setter
        return self

    def getPskIdentityHint(self) -> "String":
        """
        AUTOSAR-compliant getter for pskIdentityHint.

        Returns:
            The pskIdentityHint value

        Note:
            Delegates to psk_identity_hint property (CODING_RULE_V2_00017)
        """
        return self.psk_identity_hint  # Delegates to property

    def setPskIdentityHint(self, value: "String") -> "TlsPskIdentity":
        """
        AUTOSAR-compliant setter for pskIdentityHint with method chaining.

        Args:
            value: The pskIdentityHint to set

        Returns:
            self for method chaining

        Note:
            Delegates to psk_identity_hint property setter (gets validation automatically)
        """
        self.psk_identity_hint = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_pre_shared_key(self, value: Optional["CryptoServiceKey"]) -> "TlsPskIdentity":
        """
        Set preSharedKey and return self for chaining.

        Args:
            value: The preSharedKey to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pre_shared_key("value")
        """
        self.pre_shared_key = value  # Use property setter (gets validation)
        return self

    def with_psk_identity(self, value: Optional["String"]) -> "TlsPskIdentity":
        """
        Set pskIdentity and return self for chaining.

        Args:
            value: The pskIdentity to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_psk_identity("value")
        """
        self.psk_identity = value  # Use property setter (gets validation)
        return self

    def with_psk_identity_hint(self, value: Optional["String"]) -> "TlsPskIdentity":
        """
        Set pskIdentityHint and return self for chaining.

        Args:
            value: The pskIdentityHint to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_psk_identity_hint("value")
        """
        self.psk_identity_hint = value  # Use property setter (gets validation)
        return self



class TlsCryptoCipherSuiteProps(Identifiable):
    """
    This meta-class provides attributes to specify details of TLS Cipher Suites.

    Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication::TlsCryptoCipherSuiteProps

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 563, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines if the security extension according to IETF RFC shall be supported.
        # This is useful for cipher suites CBC mode.
        self._tcpIpTlsUse: Optional["Boolean"] = None

    @property
    def tcp_ip_tls_use(self) -> Optional["Boolean"]:
        """Get tcpIpTlsUse (Pythonic accessor)."""
        return self._tcpIpTlsUse

    @tcp_ip_tls_use.setter
    def tcp_ip_tls_use(self, value: Optional["Boolean"]) -> None:
        """
        Set tcpIpTlsUse with validation.

        Args:
            value: The tcpIpTlsUse to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpTlsUse = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"tcpIpTlsUse must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._tcpIpTlsUse = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTcpIpTlsUse(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for tcpIpTlsUse.

        Returns:
            The tcpIpTlsUse value

        Note:
            Delegates to tcp_ip_tls_use property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_tls_use  # Delegates to property

    def setTcpIpTlsUse(self, value: "Boolean") -> "TlsCryptoCipherSuiteProps":
        """
        AUTOSAR-compliant setter for tcpIpTlsUse with method chaining.

        Args:
            value: The tcpIpTlsUse to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_tls_use property setter (gets validation automatically)
        """
        self.tcp_ip_tls_use = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_tcp_ip_tls_use(self, value: Optional["Boolean"]) -> "TlsCryptoCipherSuiteProps":
        """
        Set tcpIpTlsUse and return self for chaining.

        Args:
            value: The tcpIpTlsUse to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_tls_use("value")
        """
        self.tcp_ip_tls_use = value  # Use property setter (gets validation)
        return self



class CryptoEllipticCurveProps(ARElement):
    """
    This meta-class provides attributes to specify the properties of elliptic
    curves.

    Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication::CryptoEllipticCurveProps

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 564, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the value of one specific NamedCurve Id.
        self._namedCurveId: Optional["PositiveInteger"] = None

    @property
    def named_curve_id(self) -> Optional["PositiveInteger"]:
        """Get namedCurveId (Pythonic accessor)."""
        return self._namedCurveId

    @named_curve_id.setter
    def named_curve_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set namedCurveId with validation.

        Args:
            value: The namedCurveId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._namedCurveId = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"namedCurveId must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._namedCurveId = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getNamedCurveId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for namedCurveId.

        Returns:
            The namedCurveId value

        Note:
            Delegates to named_curve_id property (CODING_RULE_V2_00017)
        """
        return self.named_curve_id  # Delegates to property

    def setNamedCurveId(self, value: "PositiveInteger") -> "CryptoEllipticCurveProps":
        """
        AUTOSAR-compliant setter for namedCurveId with method chaining.

        Args:
            value: The namedCurveId to set

        Returns:
            self for method chaining

        Note:
            Delegates to named_curve_id property setter (gets validation automatically)
        """
        self.named_curve_id = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_named_curve_id(self, value: Optional["PositiveInteger"]) -> "CryptoEllipticCurveProps":
        """
        Set namedCurveId and return self for chaining.

        Args:
            value: The namedCurveId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_named_curve_id("value")
        """
        self.named_curve_id = value  # Use property setter (gets validation)
        return self



class CryptoSignatureScheme(ARElement):
    """
    This meta-class provides attributes to specify the TLS Signature Scheme.

    Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication::CryptoSignatureScheme

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 564, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the value of one specific TLS Signature Scheme.
        self._signature: Optional["PositiveInteger"] = None

    @property
    def signature(self) -> Optional["PositiveInteger"]:
        """Get signature (Pythonic accessor)."""
        return self._signature

    @signature.setter
    def signature(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set signature with validation.

        Args:
            value: The signature to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._signature = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"signature must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._signature = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSignature(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for signature.

        Returns:
            The signature value

        Note:
            Delegates to signature property (CODING_RULE_V2_00017)
        """
        return self.signature  # Delegates to property

    def setSignature(self, value: "PositiveInteger") -> "CryptoSignatureScheme":
        """
        AUTOSAR-compliant setter for signature with method chaining.

        Args:
            value: The signature to set

        Returns:
            self for method chaining

        Note:
            Delegates to signature property setter (gets validation automatically)
        """
        self.signature = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_signature(self, value: Optional["PositiveInteger"]) -> "CryptoSignatureScheme":
        """
        Set signature and return self for chaining.

        Args:
            value: The signature to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_signature("value")
        """
        self.signature = value  # Use property setter (gets validation)
        return self



class IPSecConfig(ARObject):
    """
    IPsec is a protocol that is designed to provide "end-to-end"
    cryptographically-based security for IP network connections.

    Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication::IPSecConfig

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 571, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Global IPsec configuration settings that are valid for all that are defined
        # on the NetworkEndpoint.
        self._ipSecConfig: Optional["IPSecConfigProps"] = None

    @property
    def ip_sec_config(self) -> Optional["IPSecConfigProps"]:
        """Get ipSecConfig (Pythonic accessor)."""
        return self._ipSecConfig

    @ip_sec_config.setter
    def ip_sec_config(self, value: Optional["IPSecConfigProps"]) -> None:
        """
        Set ipSecConfig with validation.

        Args:
            value: The ipSecConfig to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ipSecConfig = None
            return

        if not isinstance(value, IPSecConfigProps):
            raise TypeError(
                f"ipSecConfig must be IPSecConfigProps or None, got {type(value).__name__}"
            )
        self._ipSecConfig = value
        # NetworkEndpoint.
        self._ipSecRule: List["IPSecRule"] = []

    @property
    def ip_sec_rule(self) -> List["IPSecRule"]:
        """Get ipSecRule (Pythonic accessor)."""
        return self._ipSecRule

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIpSecConfig(self) -> "IPSecConfigProps":
        """
        AUTOSAR-compliant getter for ipSecConfig.

        Returns:
            The ipSecConfig value

        Note:
            Delegates to ip_sec_config property (CODING_RULE_V2_00017)
        """
        return self.ip_sec_config  # Delegates to property

    def setIpSecConfig(self, value: "IPSecConfigProps") -> "IPSecConfig":
        """
        AUTOSAR-compliant setter for ipSecConfig with method chaining.

        Args:
            value: The ipSecConfig to set

        Returns:
            self for method chaining

        Note:
            Delegates to ip_sec_config property setter (gets validation automatically)
        """
        self.ip_sec_config = value  # Delegates to property setter
        return self

    def getIpSecRule(self) -> List["IPSecRule"]:
        """
        AUTOSAR-compliant getter for ipSecRule.

        Returns:
            The ipSecRule value

        Note:
            Delegates to ip_sec_rule property (CODING_RULE_V2_00017)
        """
        return self.ip_sec_rule  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ip_sec_config(self, value: Optional["IPSecConfigProps"]) -> "IPSecConfig":
        """
        Set ipSecConfig and return self for chaining.

        Args:
            value: The ipSecConfig to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ip_sec_config("value")
        """
        self.ip_sec_config = value  # Use property setter (gets validation)
        return self



class IPSecRule(Identifiable):
    """
    This element defines an IPsec rule that describes communication traffic that
    is monitored, protected and filtered.

    Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication::IPSecRule

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 571, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the direction in which the traffic is If this
        # attribute is not set a bidirectional traffic assumed.
        self._direction: Optional["Communication"] = None

    @property
    def direction(self) -> Optional["Communication"]:
        """Get direction (Pythonic accessor)."""
        return self._direction

    @direction.setter
    def direction(self, value: Optional["Communication"]) -> None:
        """
        Set direction with validation.

        Args:
            value: The direction to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._direction = None
            return

        if not isinstance(value, Communication):
            raise TypeError(
                f"direction must be Communication or None, got {type(value).__name__}"
            )
        self._direction = value
        self._headerType: Optional["IPsecHeaderTypeEnum"] = None

    @property
    def header_type(self) -> Optional["IPsecHeaderTypeEnum"]:
        """Get headerType (Pythonic accessor)."""
        return self._headerType

    @header_type.setter
    def header_type(self, value: Optional["IPsecHeaderTypeEnum"]) -> None:
        """
        Set headerType with validation.

        Args:
            value: The headerType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._headerType = None
            return

        if not isinstance(value, IPsecHeaderTypeEnum):
            raise TypeError(
                f"headerType must be IPsecHeaderTypeEnum or None, got {type(value).__name__}"
            )
        self._headerType = value
        # entry.
        self._ipProtocol: Optional["IPsecIpProtocolEnum"] = None

    @property
    def ip_protocol(self) -> Optional["IPsecIpProtocolEnum"]:
        """Get ipProtocol (Pythonic accessor)."""
        return self._ipProtocol

    @ip_protocol.setter
    def ip_protocol(self, value: Optional["IPsecIpProtocolEnum"]) -> None:
        """
        Set ipProtocol with validation.

        Args:
            value: The ipProtocol to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ipProtocol = None
            return

        if not isinstance(value, IPsecIpProtocolEnum):
            raise TypeError(
                f"ipProtocol must be IPsecIpProtocolEnum or None, got {type(value).__name__}"
            )
        self._ipProtocol = value
        # authentication.
        self._localCertificate: List["CryptoService"] = []

    @property
    def local_certificate(self) -> List["CryptoService"]:
        """Get localCertificate (Pythonic accessor)."""
        return self._localCertificate
        # This attribute defines how the local participant should be authentication.
        self._localId: Optional["String"] = None

    @property
    def local_id(self) -> Optional["String"]:
        """Get localId (Pythonic accessor)."""
        return self._localId

    @local_id.setter
    def local_id(self, value: Optional["String"]) -> None:
        """
        Set localId with validation.

        Args:
            value: The localId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._localId = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"localId must be String or str or None, got {type(value).__name__}"
            )
        self._localId = value
                # local port range.
        # attribute is not set then this rule shall be effective local ports.
        # that port ranges are currently not supported AUTOSAR AP’s operating system
                # backend.
        # If AP involved, each IPsec rule may only contain a.
        self._localPortRange: Optional["PositiveInteger"] = None

    @property
    def local_port_range(self) -> Optional["PositiveInteger"]:
        """Get localPortRange (Pythonic accessor)."""
        return self._localPortRange

    @local_port_range.setter
    def local_port_range(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set localPortRange with validation.

        Args:
            value: The localPortRange to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._localPortRange = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"localPortRange must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._localPortRange = value
        self._mode: Optional["IPsecModeEnum"] = None

    @property
    def mode(self) -> Optional["IPsecModeEnum"]:
        """Get mode (Pythonic accessor)."""
        return self._mode

    @mode.setter
    def mode(self, value: Optional["IPsecModeEnum"]) -> None:
        """
        Set mode with validation.

        Args:
            value: The mode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mode = None
            return

        if not isinstance(value, IPsecModeEnum):
            raise TypeError(
                f"mode must be IPsecModeEnum or None, got {type(value).__name__}"
            )
        self._mode = value
        # secured using IPsec and traffic is secured.
        self._policy: Optional["IPsecPolicyEnum"] = None

    @property
    def policy(self) -> Optional["IPsecPolicyEnum"]:
        """Get policy (Pythonic accessor)."""
        return self._policy

    @policy.setter
    def policy(self, value: Optional["IPsecPolicyEnum"]) -> None:
        """
        Set policy with validation.

        Args:
            value: The policy to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._policy = None
            return

        if not isinstance(value, IPsecPolicyEnum):
            raise TypeError(
                f"policy must be IPsecPolicyEnum or None, got {type(value).__name__}"
            )
        self._policy = value
        self._preSharedKey: Optional["CryptoServiceKey"] = None

    @property
    def pre_shared_key(self) -> Optional["CryptoServiceKey"]:
        """Get preSharedKey (Pythonic accessor)."""
        return self._preSharedKey

    @pre_shared_key.setter
    def pre_shared_key(self, value: Optional["CryptoServiceKey"]) -> None:
        """
        Set preSharedKey with validation.

        Args:
            value: The preSharedKey to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._preSharedKey = None
            return

        if not isinstance(value, CryptoServiceKey):
            raise TypeError(
                f"preSharedKey must be CryptoServiceKey or None, got {type(value).__name__}"
            )
        self._preSharedKey = value
        # entries is based on priority, the highest priority "0".
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

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"priority must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._priority = value
        # authentication.
        self._remote: List["CryptoService"] = []

    @property
    def remote(self) -> List["CryptoService"]:
        """Get remote (Pythonic accessor)."""
        return self._remote
        # This attribute defines how the remote participant should for authentication.
        self._remoteId: Optional["String"] = None

    @property
    def remote_id(self) -> Optional["String"]:
        """Get remoteId (Pythonic accessor)."""
        return self._remoteId

    @remote_id.setter
    def remote_id(self, value: Optional["String"]) -> None:
        """
        Set remoteId with validation.

        Args:
            value: The remoteId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._remoteId = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"remoteId must be String or str or None, got {type(value).__name__}"
            )
        self._remoteId = value
        # With this the connection between the local Network the remote NetworkEndpoint
                # is described the traffic is monitored.
        self._remoteIp: List["NetworkEndpoint"] = []

    @property
    def remote_ip(self) -> List["NetworkEndpoint"]:
        """Get remoteIp (Pythonic accessor)."""
        return self._remoteIp
        # This attribute restricts the traffic monitoring and defines a value for the
                # remote port range.
        # attribute is not set then this rule shall be effective local ports.
        # that port ranges are currently not supported AUTOSAR AP’s operating system
                # backend.
        # If AP involved, each IPsec rule may only contain a.
        self._remotePort: Optional["PositiveInteger"] = None

    @property
    def remote_port(self) -> Optional["PositiveInteger"]:
        """Get remotePort (Pythonic accessor)."""
        return self._remotePort

    @remote_port.setter
    def remote_port(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set remotePort with validation.

        Args:
            value: The remotePort to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._remotePort = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"remotePort must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._remotePort = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDirection(self) -> "Communication":
        """
        AUTOSAR-compliant getter for direction.

        Returns:
            The direction value

        Note:
            Delegates to direction property (CODING_RULE_V2_00017)
        """
        return self.direction  # Delegates to property

    def setDirection(self, value: "Communication") -> "IPSecRule":
        """
        AUTOSAR-compliant setter for direction with method chaining.

        Args:
            value: The direction to set

        Returns:
            self for method chaining

        Note:
            Delegates to direction property setter (gets validation automatically)
        """
        self.direction = value  # Delegates to property setter
        return self

    def getHeaderType(self) -> "IPsecHeaderTypeEnum":
        """
        AUTOSAR-compliant getter for headerType.

        Returns:
            The headerType value

        Note:
            Delegates to header_type property (CODING_RULE_V2_00017)
        """
        return self.header_type  # Delegates to property

    def setHeaderType(self, value: "IPsecHeaderTypeEnum") -> "IPSecRule":
        """
        AUTOSAR-compliant setter for headerType with method chaining.

        Args:
            value: The headerType to set

        Returns:
            self for method chaining

        Note:
            Delegates to header_type property setter (gets validation automatically)
        """
        self.header_type = value  # Delegates to property setter
        return self

    def getIpProtocol(self) -> "IPsecIpProtocolEnum":
        """
        AUTOSAR-compliant getter for ipProtocol.

        Returns:
            The ipProtocol value

        Note:
            Delegates to ip_protocol property (CODING_RULE_V2_00017)
        """
        return self.ip_protocol  # Delegates to property

    def setIpProtocol(self, value: "IPsecIpProtocolEnum") -> "IPSecRule":
        """
        AUTOSAR-compliant setter for ipProtocol with method chaining.

        Args:
            value: The ipProtocol to set

        Returns:
            self for method chaining

        Note:
            Delegates to ip_protocol property setter (gets validation automatically)
        """
        self.ip_protocol = value  # Delegates to property setter
        return self

    def getLocalCertificate(self) -> List["CryptoService"]:
        """
        AUTOSAR-compliant getter for localCertificate.

        Returns:
            The localCertificate value

        Note:
            Delegates to local_certificate property (CODING_RULE_V2_00017)
        """
        return self.local_certificate  # Delegates to property

    def getLocalId(self) -> "String":
        """
        AUTOSAR-compliant getter for localId.

        Returns:
            The localId value

        Note:
            Delegates to local_id property (CODING_RULE_V2_00017)
        """
        return self.local_id  # Delegates to property

    def setLocalId(self, value: "String") -> "IPSecRule":
        """
        AUTOSAR-compliant setter for localId with method chaining.

        Args:
            value: The localId to set

        Returns:
            self for method chaining

        Note:
            Delegates to local_id property setter (gets validation automatically)
        """
        self.local_id = value  # Delegates to property setter
        return self

    def getLocalPortRange(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for localPortRange.

        Returns:
            The localPortRange value

        Note:
            Delegates to local_port_range property (CODING_RULE_V2_00017)
        """
        return self.local_port_range  # Delegates to property

    def setLocalPortRange(self, value: "PositiveInteger") -> "IPSecRule":
        """
        AUTOSAR-compliant setter for localPortRange with method chaining.

        Args:
            value: The localPortRange to set

        Returns:
            self for method chaining

        Note:
            Delegates to local_port_range property setter (gets validation automatically)
        """
        self.local_port_range = value  # Delegates to property setter
        return self

    def getMode(self) -> "IPsecModeEnum":
        """
        AUTOSAR-compliant getter for mode.

        Returns:
            The mode value

        Note:
            Delegates to mode property (CODING_RULE_V2_00017)
        """
        return self.mode  # Delegates to property

    def setMode(self, value: "IPsecModeEnum") -> "IPSecRule":
        """
        AUTOSAR-compliant setter for mode with method chaining.

        Args:
            value: The mode to set

        Returns:
            self for method chaining

        Note:
            Delegates to mode property setter (gets validation automatically)
        """
        self.mode = value  # Delegates to property setter
        return self

    def getPolicy(self) -> "IPsecPolicyEnum":
        """
        AUTOSAR-compliant getter for policy.

        Returns:
            The policy value

        Note:
            Delegates to policy property (CODING_RULE_V2_00017)
        """
        return self.policy  # Delegates to property

    def setPolicy(self, value: "IPsecPolicyEnum") -> "IPSecRule":
        """
        AUTOSAR-compliant setter for policy with method chaining.

        Args:
            value: The policy to set

        Returns:
            self for method chaining

        Note:
            Delegates to policy property setter (gets validation automatically)
        """
        self.policy = value  # Delegates to property setter
        return self

    def getPreSharedKey(self) -> "CryptoServiceKey":
        """
        AUTOSAR-compliant getter for preSharedKey.

        Returns:
            The preSharedKey value

        Note:
            Delegates to pre_shared_key property (CODING_RULE_V2_00017)
        """
        return self.pre_shared_key  # Delegates to property

    def setPreSharedKey(self, value: "CryptoServiceKey") -> "IPSecRule":
        """
        AUTOSAR-compliant setter for preSharedKey with method chaining.

        Args:
            value: The preSharedKey to set

        Returns:
            self for method chaining

        Note:
            Delegates to pre_shared_key property setter (gets validation automatically)
        """
        self.pre_shared_key = value  # Delegates to property setter
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

    def setPriority(self, value: "PositiveInteger") -> "IPSecRule":
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

    def getRemote(self) -> List["CryptoService"]:
        """
        AUTOSAR-compliant getter for remote.

        Returns:
            The remote value

        Note:
            Delegates to remote property (CODING_RULE_V2_00017)
        """
        return self.remote  # Delegates to property

    def getRemoteId(self) -> "String":
        """
        AUTOSAR-compliant getter for remoteId.

        Returns:
            The remoteId value

        Note:
            Delegates to remote_id property (CODING_RULE_V2_00017)
        """
        return self.remote_id  # Delegates to property

    def setRemoteId(self, value: "String") -> "IPSecRule":
        """
        AUTOSAR-compliant setter for remoteId with method chaining.

        Args:
            value: The remoteId to set

        Returns:
            self for method chaining

        Note:
            Delegates to remote_id property setter (gets validation automatically)
        """
        self.remote_id = value  # Delegates to property setter
        return self

    def getRemoteIp(self) -> List["NetworkEndpoint"]:
        """
        AUTOSAR-compliant getter for remoteIp.

        Returns:
            The remoteIp value

        Note:
            Delegates to remote_ip property (CODING_RULE_V2_00017)
        """
        return self.remote_ip  # Delegates to property

    def getRemotePort(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for remotePort.

        Returns:
            The remotePort value

        Note:
            Delegates to remote_port property (CODING_RULE_V2_00017)
        """
        return self.remote_port  # Delegates to property

    def setRemotePort(self, value: "PositiveInteger") -> "IPSecRule":
        """
        AUTOSAR-compliant setter for remotePort with method chaining.

        Args:
            value: The remotePort to set

        Returns:
            self for method chaining

        Note:
            Delegates to remote_port property setter (gets validation automatically)
        """
        self.remote_port = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_direction(self, value: Optional["Communication"]) -> "IPSecRule":
        """
        Set direction and return self for chaining.

        Args:
            value: The direction to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_direction("value")
        """
        self.direction = value  # Use property setter (gets validation)
        return self

    def with_header_type(self, value: Optional["IPsecHeaderTypeEnum"]) -> "IPSecRule":
        """
        Set headerType and return self for chaining.

        Args:
            value: The headerType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_header_type("value")
        """
        self.header_type = value  # Use property setter (gets validation)
        return self

    def with_ip_protocol(self, value: Optional["IPsecIpProtocolEnum"]) -> "IPSecRule":
        """
        Set ipProtocol and return self for chaining.

        Args:
            value: The ipProtocol to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ip_protocol("value")
        """
        self.ip_protocol = value  # Use property setter (gets validation)
        return self

    def with_local_id(self, value: Optional["String"]) -> "IPSecRule":
        """
        Set localId and return self for chaining.

        Args:
            value: The localId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_local_id("value")
        """
        self.local_id = value  # Use property setter (gets validation)
        return self

    def with_local_port_range(self, value: Optional["PositiveInteger"]) -> "IPSecRule":
        """
        Set localPortRange and return self for chaining.

        Args:
            value: The localPortRange to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_local_port_range("value")
        """
        self.local_port_range = value  # Use property setter (gets validation)
        return self

    def with_mode(self, value: Optional["IPsecModeEnum"]) -> "IPSecRule":
        """
        Set mode and return self for chaining.

        Args:
            value: The mode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mode("value")
        """
        self.mode = value  # Use property setter (gets validation)
        return self

    def with_policy(self, value: Optional["IPsecPolicyEnum"]) -> "IPSecRule":
        """
        Set policy and return self for chaining.

        Args:
            value: The policy to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_policy("value")
        """
        self.policy = value  # Use property setter (gets validation)
        return self

    def with_pre_shared_key(self, value: Optional["CryptoServiceKey"]) -> "IPSecRule":
        """
        Set preSharedKey and return self for chaining.

        Args:
            value: The preSharedKey to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pre_shared_key("value")
        """
        self.pre_shared_key = value  # Use property setter (gets validation)
        return self

    def with_priority(self, value: Optional["PositiveInteger"]) -> "IPSecRule":
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

    def with_remote_id(self, value: Optional["String"]) -> "IPSecRule":
        """
        Set remoteId and return self for chaining.

        Args:
            value: The remoteId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_remote_id("value")
        """
        self.remote_id = value  # Use property setter (gets validation)
        return self

    def with_remote_port(self, value: Optional["PositiveInteger"]) -> "IPSecRule":
        """
        Set remotePort and return self for chaining.

        Args:
            value: The remotePort to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_remote_port("value")
        """
        self.remote_port = value  # Use property setter (gets validation)
        return self



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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"ikeCipherSuite must be String or str or None, got {type(value).__name__}"
            )
        self._ikeCipherSuite = value
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

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"ikeRandTime must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._ikeRandTime = value
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

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"saOverTime must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._saOverTime = value
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



class SecOcCryptoServiceMapping(CryptoServiceMapping):
    """
    This meta-class has the ability to represent a crypto service mapping for
    the Pdu-based communication via SecOC.

    Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication::SecOcCryptoServiceMapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 375, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference identifies the applicable crypto primitive for.
        self._authentication: Optional["CryptoServicePrimitive"] = None

    @property
    def authentication(self) -> Optional["CryptoServicePrimitive"]:
        """Get authentication (Pythonic accessor)."""
        return self._authentication

    @authentication.setter
    def authentication(self, value: Optional["CryptoServicePrimitive"]) -> None:
        """
        Set authentication with validation.

        Args:
            value: The authentication to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._authentication = None
            return

        if not isinstance(value, CryptoServicePrimitive):
            raise TypeError(
                f"authentication must be CryptoServicePrimitive or None, got {type(value).__name__}"
            )
        self._authentication = value
        # SecOcCryptoServiceMapping shall be.
        self._cryptoService: Optional["CryptoServiceQueue"] = None

    @property
    def crypto_service(self) -> Optional["CryptoServiceQueue"]:
        """Get cryptoService (Pythonic accessor)."""
        return self._cryptoService

    @crypto_service.setter
    def crypto_service(self, value: Optional["CryptoServiceQueue"]) -> None:
        """
        Set cryptoService with validation.

        Args:
            value: The cryptoService to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cryptoService = None
            return

        if not isinstance(value, CryptoServiceQueue):
            raise TypeError(
                f"cryptoService must be CryptoServiceQueue or None, got {type(value).__name__}"
            )
        self._cryptoService = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAuthentication(self) -> "CryptoServicePrimitive":
        """
        AUTOSAR-compliant getter for authentication.

        Returns:
            The authentication value

        Note:
            Delegates to authentication property (CODING_RULE_V2_00017)
        """
        return self.authentication  # Delegates to property

    def setAuthentication(self, value: "CryptoServicePrimitive") -> "SecOcCryptoServiceMapping":
        """
        AUTOSAR-compliant setter for authentication with method chaining.

        Args:
            value: The authentication to set

        Returns:
            self for method chaining

        Note:
            Delegates to authentication property setter (gets validation automatically)
        """
        self.authentication = value  # Delegates to property setter
        return self

    def getCryptoService(self) -> "CryptoServiceQueue":
        """
        AUTOSAR-compliant getter for cryptoService.

        Returns:
            The cryptoService value

        Note:
            Delegates to crypto_service property (CODING_RULE_V2_00017)
        """
        return self.crypto_service  # Delegates to property

    def setCryptoService(self, value: "CryptoServiceQueue") -> "SecOcCryptoServiceMapping":
        """
        AUTOSAR-compliant setter for cryptoService with method chaining.

        Args:
            value: The cryptoService to set

        Returns:
            self for method chaining

        Note:
            Delegates to crypto_service property setter (gets validation automatically)
        """
        self.crypto_service = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_authentication(self, value: Optional["CryptoServicePrimitive"]) -> "SecOcCryptoServiceMapping":
        """
        Set authentication and return self for chaining.

        Args:
            value: The authentication to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_authentication("value")
        """
        self.authentication = value  # Use property setter (gets validation)
        return self

    def with_crypto_service(self, value: Optional["CryptoServiceQueue"]) -> "SecOcCryptoServiceMapping":
        """
        Set cryptoService and return self for chaining.

        Args:
            value: The cryptoService to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_crypto_service("value")
        """
        self.crypto_service = value  # Use property setter (gets validation)
        return self



class TlsCryptoServiceMapping(CryptoServiceMapping):
    """
    This meta-class has the ability to represent a crypto service mapping for
    the socket-based configuration of Transport Layer Security (TLS).

    Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication::TlsCryptoServiceMapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 559, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference identifies the shared(i.
        # e.
        # applicable for the aggregated cipher suites) crypto service the execution of
                # key exchange during the.
        self._keyExchange: List["CryptoServicePrimitive"] = []

    @property
    def key_exchange(self) -> List["CryptoServicePrimitive"]:
        """Get keyExchange (Pythonic accessor)."""
        return self._keyExchange
        # This aggregation represents the collection of supported.
        self._tlsCipherSuite: List["TlsCryptoCipherSuite"] = []

    @property
    def tls_cipher_suite(self) -> List["TlsCryptoCipherSuite"]:
        """Get tlsCipherSuite (Pythonic accessor)."""
        return self._tlsCipherSuite
        # Defines if client authentication shall be applied for this connection.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._useClient: Optional["Boolean"] = None

    @property
    def use_client(self) -> Optional["Boolean"]:
        """Get useClient (Pythonic accessor)."""
        return self._useClient

    @use_client.setter
    def use_client(self, value: Optional["Boolean"]) -> None:
        """
        Set useClient with validation.

        Args:
            value: The useClient to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._useClient = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"useClient must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._useClient = value
        # defined in IETF RFC 8449, chapter.
        self._useSecurity: Optional["Boolean"] = None

    @property
    def use_security(self) -> Optional["Boolean"]:
        """Get useSecurity (Pythonic accessor)."""
        return self._useSecurity

    @use_security.setter
    def use_security(self, value: Optional["Boolean"]) -> None:
        """
        Set useSecurity with validation.

        Args:
            value: The useSecurity to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._useSecurity = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"useSecurity must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._useSecurity = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getKeyExchange(self) -> List["CryptoServicePrimitive"]:
        """
        AUTOSAR-compliant getter for keyExchange.

        Returns:
            The keyExchange value

        Note:
            Delegates to key_exchange property (CODING_RULE_V2_00017)
        """
        return self.key_exchange  # Delegates to property

    def getTlsCipherSuite(self) -> List["TlsCryptoCipherSuite"]:
        """
        AUTOSAR-compliant getter for tlsCipherSuite.

        Returns:
            The tlsCipherSuite value

        Note:
            Delegates to tls_cipher_suite property (CODING_RULE_V2_00017)
        """
        return self.tls_cipher_suite  # Delegates to property

    def getUseClient(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for useClient.

        Returns:
            The useClient value

        Note:
            Delegates to use_client property (CODING_RULE_V2_00017)
        """
        return self.use_client  # Delegates to property

    def setUseClient(self, value: "Boolean") -> "TlsCryptoServiceMapping":
        """
        AUTOSAR-compliant setter for useClient with method chaining.

        Args:
            value: The useClient to set

        Returns:
            self for method chaining

        Note:
            Delegates to use_client property setter (gets validation automatically)
        """
        self.use_client = value  # Delegates to property setter
        return self

    def getUseSecurity(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for useSecurity.

        Returns:
            The useSecurity value

        Note:
            Delegates to use_security property (CODING_RULE_V2_00017)
        """
        return self.use_security  # Delegates to property

    def setUseSecurity(self, value: "Boolean") -> "TlsCryptoServiceMapping":
        """
        AUTOSAR-compliant setter for useSecurity with method chaining.

        Args:
            value: The useSecurity to set

        Returns:
            self for method chaining

        Note:
            Delegates to use_security property setter (gets validation automatically)
        """
        self.use_security = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_use_client(self, value: Optional["Boolean"]) -> "TlsCryptoServiceMapping":
        """
        Set useClient and return self for chaining.

        Args:
            value: The useClient to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_use_client("value")
        """
        self.use_client = value  # Use property setter (gets validation)
        return self

    def with_use_security(self, value: Optional["Boolean"]) -> "TlsCryptoServiceMapping":
        """
        Set useSecurity and return self for chaining.

        Args:
            value: The useSecurity to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_use_security("value")
        """
        self.use_security = value  # Use property setter (gets validation)
        return self


class MacSecConfidentialityOffsetEnum(AREnum):
    """
    MacSecConfidentialityOffsetEnum enumeration

This enum defines the MACsec capability options. Tags: atp.Status=candidate Aggregated by MacSecCryptoAlgoConfig.confidentialityOffset

Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication
    """
    # confidentiality offset of 0. Confidentiality confidentiality offset of 30.
    ConfidentialityOffset_0Offset_30 = "1"

    # Template
    System = "None"

    # CP R23-11 Confidentiality confidentiality offset of 50.
    AUTOSAROffset_50 = "2"



class MacSecCapabilityEnum(AREnum):
    """
    MacSecCapabilityEnum enumeration

This enum defines the MACsec capability options. Tags: atp.Status=candidate Aggregated by MacSecCryptoAlgoConfig.capability

Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication
    """
    # Option that ensures confidentiality and integrity
    intergrityAndConfidentiality = "1"

    # Option that ensures integrity without confidentiality
    intergrityWithoutConfidentiality = "0"



class MacSecRoleEnum(AREnum):
    """
    MacSecRoleEnum enumeration

This enum defines the MACsec Role options. Tags: atp.Status=candidate Aggregated by MacSecLocalKayProps.role

Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication
    """
    # Port acts in the KeyServer role
    keyServer = "1"

    # Port acts in the peer role
    peer = "0"



class MacSecFailPermissiveModeEnum(AREnum):
    """
    MacSecFailPermissiveModeEnum enumeration

Behavior options of the Port Access Entity in case MACsec does not succeed. Tags: atp.Status=candidate Aggregated by MacSecProps.onFailPermissiveMode

Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication
    """
    # The controlled port will never be set to enabled if the participants cannot establish and successfully use a MACsec Secure Channel.
    never = "0"

    # Template
    System = "None"

    # CP R23-11
    AUTOSAR = "None"

    # The controlled port will be set to enabled and MACsec will not be used in the port if the timeout value
    timeout = "1"



class CryptoServiceKeyGenerationEnum(AREnum):
    """
    CryptoServiceKeyGenerationEnum enumeration

This enumeration shall be taken to express the handling of a crypto key in terms of whether it is obtained from e.g. a diagnostic tester or whether it is created by derivation from a master key. Aggregated by CryptoServiceKey.keyGeneration

Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication
    """
    # This means that the crypto key is created by derivation from a master key.
    keyDerivation = "0"

    # This means that the crypto key is obtained from an external entity, e.g. a diagnostic tester.
    keyStorage = "1"



class TlsVersionEnum(AREnum):
    """
    TlsVersionEnum enumeration

This meta-class has the ability to identify a specific version of the transport-layer security (TLS) protocol. Aggregated by TlsCryptoCipherSuite.version

Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication
    """
    # TLS version 1.2
    tls12 = "0"

    # TLS version 1.3
    tls13 = "2"



class CryptoCertificateAlgorithmFamilyEnum(AREnum):
    """
    CryptoCertificateAlgorithmFamilyEnum enumeration

This meta-class defies possible cryptographic algorithm families used to create public keys and signatures within the certificate. Aggregated by CryptoServiceCertificate.algorithmFamily

Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication
    """
    # The cryptographic operations in the certificate are executed using elliptic curves (ecc)
    ecc = "2"

    # The cryptographic operations in the certificate are executed using the RSA approach.
    rsa = "1"



class CryptoCertificateFormatEnum(AREnum):
    """
    CryptoCertificateFormatEnum enumeration

This meta-class defines possible formats of cryptographic certificates. Aggregated by CryptoServiceCertificate.format

Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication
    """
    # The certificate has been created in Card Verifiable Certificate (CVC) format
    cvc = "2"

    # The certificate is created in X.509 format.
    x509 = "1"



class IPsecIpProtocolEnum(AREnum):
    """
    IPsecIpProtocolEnum enumeration

Definition of supported TcpIp protocols that are supported in Security Policy Database (SPD) entries in IPSec configurations. Aggregated by IPSecRule.ipProtocol

Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication
    """
    # Template
    System = "None"

    # CP R23-11
    AUTOSAR = "None"

    # ANY protocol
    any = "3"

    # Internet Control Message Protocol (ICMP)
    icmp = "2"

    # TCP Protocol
    tcp = "1"

    # UDP Protocol
    udp = "0"



class IPsecPolicyEnum(AREnum):
    """
    IPsecPolicyEnum enumeration

Defines the filter actions that are supported by IPsec. Aggregated by IPSecRule.policy

Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication
    """
    # Signifying that packets should be discarded
    drop = "3"

    # Signifying that packets should be protected.
    ipsec = "1"

    # Signifying that no IPsec processing should be done at all.
    passthrough = "2"

    # Signifying that packets should be discarded and a diagnostic ICMP returned.
    reject = "4"



class IPsecModeEnum(AREnum):
    """
    IPsecModeEnum enumeration

This enumeration describes the supported IPSec modes. Aggregated by IPSecRule.mode

Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication
    """
    # Signifying that the IPSec transport mode is used. With the transport mode the original IP header is retained and only the IP payload and ESP trailer is encrypted.
    transport = "1"

    # Signifying that the IPSec tunnel mode is used. With tunnel mode, the entire original IP packet is protected by IPSec. This means IPSec wraps the original packet, encrypts it, adds a new IP header and sends it to the other side.
    tunnel = "0"



class IPsecHeaderTypeEnum(AREnum):
    """
    IPsecHeaderTypeEnum enumeration

IPsec Header Type options Aggregated by IPSecRule.headerType

Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication
    """
    # Authentication Header (AH)
    ah = "0"

    # Encapsulating Security Payloads (ESP)
    esp = "1"

    # No header
    none = "2"



class IPsecDpdActionEnum(AREnum):
    """
    IPsecDpdActionEnum enumeration

Potential Dead Peer Detection (Dpd) Actions Aggregated by IPSecConfigProps.dpdAction

Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication
    """
    # Deletes the SA.
    clear = "0"

    # Immediately tries to establish the connection. trap tries to establish the connection after traffic is sent to the peer.
    restart = "1"
