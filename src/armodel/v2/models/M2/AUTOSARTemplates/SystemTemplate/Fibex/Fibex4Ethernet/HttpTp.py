from typing import Optional


class HttpTp(TransportProtocolConfiguration):
    """
    Http over TCP as transport protocol.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::HttpTp

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 461, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Descriptor for the transported content.
        self._contentType: Optional["String"] = None

    @property
    def content_type(self) -> Optional["String"]:
        """Get contentType (Pythonic accessor)."""
        return self._contentType

    @content_type.setter
    def content_type(self, value: Optional["String"]) -> None:
        """
        Set contentType with validation.

        Args:
            value: The contentType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._contentType = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"contentType must be String or None, got {type(value).__name__}"
            )
        self._contentType = value
        # HTTP Protocol version (e.
        # g.
        # 1.
        # 1).
        self._protocolVersion: Optional["String"] = None

    @property
    def protocol_version(self) -> Optional["String"]:
        """Get protocolVersion (Pythonic accessor)."""
        return self._protocolVersion

    @protocol_version.setter
    def protocol_version(self, value: Optional["String"]) -> None:
        """
        Set protocolVersion with validation.

        Args:
            value: The protocolVersion to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._protocolVersion = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"protocolVersion must be String or None, got {type(value).__name__}"
            )
        self._protocolVersion = value
        # HTTP request method to be used.
        self._requestMethod: Optional["RequestMethodEnum"] = None

    @property
    def request_method(self) -> Optional["RequestMethodEnum"]:
        """Get requestMethod (Pythonic accessor)."""
        return self._requestMethod

    @request_method.setter
    def request_method(self, value: Optional["RequestMethodEnum"]) -> None:
        """
        Set requestMethod with validation.

        Args:
            value: The requestMethod to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._requestMethod = None
            return

        if not isinstance(value, RequestMethodEnum):
            raise TypeError(
                f"requestMethod must be RequestMethodEnum or None, got {type(value).__name__}"
            )
        self._requestMethod = value
        # TcpTp Configuration.
        self._tcpTpConfig: Optional["TcpTp"] = None

    @property
    def tcp_tp_config(self) -> Optional["TcpTp"]:
        """Get tcpTpConfig (Pythonic accessor)."""
        return self._tcpTpConfig

    @tcp_tp_config.setter
    def tcp_tp_config(self, value: Optional["TcpTp"]) -> None:
        """
        Set tcpTpConfig with validation.

        Args:
            value: The tcpTpConfig to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpTpConfig = None
            return

        if not isinstance(value, TcpTp):
            raise TypeError(
                f"tcpTpConfig must be TcpTp or None, got {type(value).__name__}"
            )
        self._tcpTpConfig = value
        # URI to be called.
        self._uri: Optional["UriString"] = None

    @property
    def uri(self) -> Optional["UriString"]:
        """Get uri (Pythonic accessor)."""
        return self._uri

    @uri.setter
    def uri(self, value: Optional["UriString"]) -> None:
        """
        Set uri with validation.

        Args:
            value: The uri to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._uri = None
            return

        if not isinstance(value, UriString):
            raise TypeError(
                f"uri must be UriString or None, got {type(value).__name__}"
            )
        self._uri = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getContentType(self) -> "String":
        """
        AUTOSAR-compliant getter for contentType.

        Returns:
            The contentType value

        Note:
            Delegates to content_type property (CODING_RULE_V2_00017)
        """
        return self.content_type  # Delegates to property

    def setContentType(self, value: "String") -> "HttpTp":
        """
        AUTOSAR-compliant setter for contentType with method chaining.

        Args:
            value: The contentType to set

        Returns:
            self for method chaining

        Note:
            Delegates to content_type property setter (gets validation automatically)
        """
        self.content_type = value  # Delegates to property setter
        return self

    def getProtocolVersion(self) -> "String":
        """
        AUTOSAR-compliant getter for protocolVersion.

        Returns:
            The protocolVersion value

        Note:
            Delegates to protocol_version property (CODING_RULE_V2_00017)
        """
        return self.protocol_version  # Delegates to property

    def setProtocolVersion(self, value: "String") -> "HttpTp":
        """
        AUTOSAR-compliant setter for protocolVersion with method chaining.

        Args:
            value: The protocolVersion to set

        Returns:
            self for method chaining

        Note:
            Delegates to protocol_version property setter (gets validation automatically)
        """
        self.protocol_version = value  # Delegates to property setter
        return self

    def getRequestMethod(self) -> "RequestMethodEnum":
        """
        AUTOSAR-compliant getter for requestMethod.

        Returns:
            The requestMethod value

        Note:
            Delegates to request_method property (CODING_RULE_V2_00017)
        """
        return self.request_method  # Delegates to property

    def setRequestMethod(self, value: "RequestMethodEnum") -> "HttpTp":
        """
        AUTOSAR-compliant setter for requestMethod with method chaining.

        Args:
            value: The requestMethod to set

        Returns:
            self for method chaining

        Note:
            Delegates to request_method property setter (gets validation automatically)
        """
        self.request_method = value  # Delegates to property setter
        return self

    def getTcpTpConfig(self) -> "TcpTp":
        """
        AUTOSAR-compliant getter for tcpTpConfig.

        Returns:
            The tcpTpConfig value

        Note:
            Delegates to tcp_tp_config property (CODING_RULE_V2_00017)
        """
        return self.tcp_tp_config  # Delegates to property

    def setTcpTpConfig(self, value: "TcpTp") -> "HttpTp":
        """
        AUTOSAR-compliant setter for tcpTpConfig with method chaining.

        Args:
            value: The tcpTpConfig to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_tp_config property setter (gets validation automatically)
        """
        self.tcp_tp_config = value  # Delegates to property setter
        return self

    def getUri(self) -> "UriString":
        """
        AUTOSAR-compliant getter for uri.

        Returns:
            The uri value

        Note:
            Delegates to uri property (CODING_RULE_V2_00017)
        """
        return self.uri  # Delegates to property

    def setUri(self, value: "UriString") -> "HttpTp":
        """
        AUTOSAR-compliant setter for uri with method chaining.

        Args:
            value: The uri to set

        Returns:
            self for method chaining

        Note:
            Delegates to uri property setter (gets validation automatically)
        """
        self.uri = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_content_type(self, value: Optional["String"]) -> "HttpTp":
        """
        Set contentType and return self for chaining.

        Args:
            value: The contentType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_content_type("value")
        """
        self.content_type = value  # Use property setter (gets validation)
        return self

    def with_protocol_version(self, value: Optional["String"]) -> "HttpTp":
        """
        Set protocolVersion and return self for chaining.

        Args:
            value: The protocolVersion to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_protocol_version("value")
        """
        self.protocol_version = value  # Use property setter (gets validation)
        return self

    def with_request_method(self, value: Optional["RequestMethodEnum"]) -> "HttpTp":
        """
        Set requestMethod and return self for chaining.

        Args:
            value: The requestMethod to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_request_method("value")
        """
        self.request_method = value  # Use property setter (gets validation)
        return self

    def with_tcp_tp_config(self, value: Optional["TcpTp"]) -> "HttpTp":
        """
        Set tcpTpConfig and return self for chaining.

        Args:
            value: The tcpTpConfig to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_tp_config("value")
        """
        self.tcp_tp_config = value  # Use property setter (gets validation)
        return self

    def with_uri(self, value: Optional["UriString"]) -> "HttpTp":
        """
        Set uri and return self for chaining.

        Args:
            value: The uri to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_uri("value")
        """
        self.uri = value  # Use property setter (gets validation)
        return self
