from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class TlsCryptoCipherSuiteProps(Identifiable):
    """
    This meta-class provides attributes to specify details of TLS Cipher Suites.

    Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication

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

        if not isinstance(value, Boolean):
            raise TypeError(
                f"tcpIpTlsUse must be Boolean or None, got {type(value).__name__}"
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
