from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

class SecuredIPdu(IPdu):
    """
    If useAsCryptographicPdu is not set or set to false this IPdu contains the
    payload of an Authentic IPdu supplemented by additional Authentication
    Information (Freshness Counter and an Authenticator). If
    useAsCryptographicPdu is set to true this IPdu contains the Authenticator
    for a payload that is transported in a separate message. The separate
    Authentic IPdu is described by the Pdu that is referenced with the payload
    reference from this SecuredIPdu.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::SecuredIPdu
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 367, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to authentication properties that are valid for this SecuredIPdu.
        self._authentication: Optional["SecureCommunication"] = None

    @property
    def authentication(self) -> Optional["SecureCommunication"]:
        """Get authentication (Pythonic accessor)."""
        return self._authentication

    @authentication.setter
    def authentication(self, value: Optional["SecureCommunication"]) -> None:
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

        if not isinstance(value, SecureCommunication):
            raise TypeError(
                f"authentication must be SecureCommunication or None, got {type(value).__name__}"
            )
        self._authentication = value
        # Defines whether the length information for handling this with SecuredIPdu.
        # useSecuredPdu is taken from the configuration or from provided length
                # information during runtime.
        # length information is taken from the length information during runtime.
        # length information is taken from the.
        self._dynamic: Optional["Boolean"] = None

    @property
    def dynamic(self) -> Optional["Boolean"]:
        """Get dynamic (Pythonic accessor)."""
        return self._dynamic

    @dynamic.setter
    def dynamic(self, value: Optional["Boolean"]) -> None:
        """
        Set dynamic with validation.
        
        Args:
            value: The dynamic to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dynamic = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"dynamic must be Boolean or None, got {type(value).__name__}"
            )
        self._dynamic = value
        # Reference to freshness properties that are valid for this.
        self._freshnessProps: Optional["SecureCommunication"] = None

    @property
    def freshness_props(self) -> Optional["SecureCommunication"]:
        """Get freshnessProps (Pythonic accessor)."""
        return self._freshnessProps

    @freshness_props.setter
    def freshness_props(self, value: Optional["SecureCommunication"]) -> None:
        """
        Set freshnessProps with validation.
        
        Args:
            value: The freshnessProps to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._freshnessProps = None
            return

        if not isinstance(value, SecureCommunication):
            raise TypeError(
                f"freshnessProps must be SecureCommunication or None, got {type(value).__name__}"
            )
        self._freshnessProps = value
        # Reference to a Pdu that will be protected against and replay attacks.
        self._payload: RefType = None

    @property
    def payload(self) -> RefType:
        """Get payload (Pythonic accessor)."""
        return self._payload

    @payload.setter
    def payload(self, value: RefType) -> None:
        """
        Set payload with validation.
        
        Args:
            value: The payload to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._payload = None
            return

        self._payload = value
        # Specific configuration properties for this SecuredIPdu.
        self._secure: Optional["SecureCommunication"] = None

    @property
    def secure(self) -> Optional["SecureCommunication"]:
        """Get secure (Pythonic accessor)."""
        return self._secure

    @secure.setter
    def secure(self, value: Optional["SecureCommunication"]) -> None:
        """
        Set secure with validation.
        
        Args:
            value: The secure to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._secure = None
            return

        if not isinstance(value, SecureCommunication):
            raise TypeError(
                f"secure must be SecureCommunication or None, got {type(value).__name__}"
            )
        self._secure = value
        # If this attribute is set to true the SecuredIPdu contains the Information for
                # an AuthenticIPdu that is in a separate message.
        # The AuthenticIPdu original payload, i.
        # e.
        # the secured data.
        # attribute is set to false this SecuredIPdu contains of an Authentic IPdu
                # supplemented by Information.
        self._useAs: Optional["Boolean"] = None

    @property
    def use_as(self) -> Optional["Boolean"]:
        """Get useAs (Pythonic accessor)."""
        return self._useAs

    @use_as.setter
    def use_as(self, value: Optional["Boolean"]) -> None:
        """
        Set useAs with validation.
        
        Args:
            value: The useAs to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._useAs = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"useAs must be Boolean or None, got {type(value).__name__}"
            )
        self._useAs = value
        # This attribute defines the size of the header which is inserted into the
                # SecuredIPdu.
        # If this attribute is set to noHeader, the SecuredIPdu contains the Header to
                # indicate the length of the AuthenticIPdu contains the original the secured
                # data.
        self._useSecuredPdu: Optional["SecuredPduHeader"] = None

    @property
    def use_secured_pdu(self) -> Optional["SecuredPduHeader"]:
        """Get useSecuredPdu (Pythonic accessor)."""
        return self._useSecuredPdu

    @use_secured_pdu.setter
    def use_secured_pdu(self, value: Optional["SecuredPduHeader"]) -> None:
        """
        Set useSecuredPdu with validation.
        
        Args:
            value: The useSecuredPdu to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._useSecuredPdu = None
            return

        if not isinstance(value, SecuredPduHeader):
            raise TypeError(
                f"useSecuredPdu must be SecuredPduHeader or None, got {type(value).__name__}"
            )
        self._useSecuredPdu = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAuthentication(self) -> "SecureCommunication":
        """
        AUTOSAR-compliant getter for authentication.
        
        Returns:
            The authentication value
        
        Note:
            Delegates to authentication property (CODING_RULE_V2_00017)
        """
        return self.authentication  # Delegates to property

    def setAuthentication(self, value: "SecureCommunication") -> "SecuredIPdu":
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

    def getDynamic(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for dynamic.
        
        Returns:
            The dynamic value
        
        Note:
            Delegates to dynamic property (CODING_RULE_V2_00017)
        """
        return self.dynamic  # Delegates to property

    def setDynamic(self, value: "Boolean") -> "SecuredIPdu":
        """
        AUTOSAR-compliant setter for dynamic with method chaining.
        
        Args:
            value: The dynamic to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to dynamic property setter (gets validation automatically)
        """
        self.dynamic = value  # Delegates to property setter
        return self

    def getFreshnessProps(self) -> "SecureCommunication":
        """
        AUTOSAR-compliant getter for freshnessProps.
        
        Returns:
            The freshnessProps value
        
        Note:
            Delegates to freshness_props property (CODING_RULE_V2_00017)
        """
        return self.freshness_props  # Delegates to property

    def setFreshnessProps(self, value: "SecureCommunication") -> "SecuredIPdu":
        """
        AUTOSAR-compliant setter for freshnessProps with method chaining.
        
        Args:
            value: The freshnessProps to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to freshness_props property setter (gets validation automatically)
        """
        self.freshness_props = value  # Delegates to property setter
        return self

    def getPayload(self) -> RefType:
        """
        AUTOSAR-compliant getter for payload.
        
        Returns:
            The payload value
        
        Note:
            Delegates to payload property (CODING_RULE_V2_00017)
        """
        return self.payload  # Delegates to property

    def setPayload(self, value: RefType) -> "SecuredIPdu":
        """
        AUTOSAR-compliant setter for payload with method chaining.
        
        Args:
            value: The payload to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to payload property setter (gets validation automatically)
        """
        self.payload = value  # Delegates to property setter
        return self

    def getSecure(self) -> "SecureCommunication":
        """
        AUTOSAR-compliant getter for secure.
        
        Returns:
            The secure value
        
        Note:
            Delegates to secure property (CODING_RULE_V2_00017)
        """
        return self.secure  # Delegates to property

    def setSecure(self, value: "SecureCommunication") -> "SecuredIPdu":
        """
        AUTOSAR-compliant setter for secure with method chaining.
        
        Args:
            value: The secure to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to secure property setter (gets validation automatically)
        """
        self.secure = value  # Delegates to property setter
        return self

    def getUseAs(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for useAs.
        
        Returns:
            The useAs value
        
        Note:
            Delegates to use_as property (CODING_RULE_V2_00017)
        """
        return self.use_as  # Delegates to property

    def setUseAs(self, value: "Boolean") -> "SecuredIPdu":
        """
        AUTOSAR-compliant setter for useAs with method chaining.
        
        Args:
            value: The useAs to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to use_as property setter (gets validation automatically)
        """
        self.use_as = value  # Delegates to property setter
        return self

    def getUseSecuredPdu(self) -> "SecuredPduHeader":
        """
        AUTOSAR-compliant getter for useSecuredPdu.
        
        Returns:
            The useSecuredPdu value
        
        Note:
            Delegates to use_secured_pdu property (CODING_RULE_V2_00017)
        """
        return self.use_secured_pdu  # Delegates to property

    def setUseSecuredPdu(self, value: "SecuredPduHeader") -> "SecuredIPdu":
        """
        AUTOSAR-compliant setter for useSecuredPdu with method chaining.
        
        Args:
            value: The useSecuredPdu to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to use_secured_pdu property setter (gets validation automatically)
        """
        self.use_secured_pdu = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_authentication(self, value: Optional["SecureCommunication"]) -> "SecuredIPdu":
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

    def with_dynamic(self, value: Optional["Boolean"]) -> "SecuredIPdu":
        """
        Set dynamic and return self for chaining.
        
        Args:
            value: The dynamic to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_dynamic("value")
        """
        self.dynamic = value  # Use property setter (gets validation)
        return self

    def with_freshness_props(self, value: Optional["SecureCommunication"]) -> "SecuredIPdu":
        """
        Set freshnessProps and return self for chaining.
        
        Args:
            value: The freshnessProps to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_freshness_props("value")
        """
        self.freshness_props = value  # Use property setter (gets validation)
        return self

    def with_payload(self, value: Optional[RefType]) -> "SecuredIPdu":
        """
        Set payload and return self for chaining.
        
        Args:
            value: The payload to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_payload("value")
        """
        self.payload = value  # Use property setter (gets validation)
        return self

    def with_secure(self, value: Optional["SecureCommunication"]) -> "SecuredIPdu":
        """
        Set secure and return self for chaining.
        
        Args:
            value: The secure to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_secure("value")
        """
        self.secure = value  # Use property setter (gets validation)
        return self

    def with_use_as(self, value: Optional["Boolean"]) -> "SecuredIPdu":
        """
        Set useAs and return self for chaining.
        
        Args:
            value: The useAs to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_use_as("value")
        """
        self.use_as = value  # Use property setter (gets validation)
        return self

    def with_use_secured_pdu(self, value: Optional["SecuredPduHeader"]) -> "SecuredIPdu":
        """
        Set useSecuredPdu and return self for chaining.
        
        Args:
            value: The useSecuredPdu to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_use_secured_pdu("value")
        """
        self.use_secured_pdu = value  # Use property setter (gets validation)
        return self