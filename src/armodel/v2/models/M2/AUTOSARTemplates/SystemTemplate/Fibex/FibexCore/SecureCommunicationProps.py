from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class SecureCommunicationProps(ARObject):
    """
    This meta-class contains configuration settings that are specific for an
    individual SecuredIPdu.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::SecureCommunicationProps
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 369, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This value determines the start position in bits of the PDU that shall be
                # passed on to the SWC that and generates the Freshness.
        # The bit counting is to TPS_SYST_01068.
        self._authData: Optional["PositiveInteger"] = None

    @property
    def auth_data(self) -> Optional["PositiveInteger"]:
        """Get authData (Pythonic accessor)."""
        return self._authData

    @auth_data.setter
    def auth_data(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set authData with validation.
        
        Args:
            value: The authData to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._authData = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"authData must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._authData = value
        # This attribute defines the additional number of attempts that are to be
                # carried out when of the authentication information failed for SecuredIPdu.
        # If zero is set than only one is done.
        self._authentication: Optional["PositiveInteger"] = None

    @property
    def authentication(self) -> Optional["PositiveInteger"]:
        """Get authentication (Pythonic accessor)."""
        return self._authentication

    @authentication.setter
    def authentication(self, value: Optional["PositiveInteger"]) -> None:
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"authentication must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._authentication = value
        # This attribute defines a numerical identifier for the.
        self._dataId: Optional["PositiveInteger"] = None

    @property
    def data_id(self) -> Optional["PositiveInteger"]:
        """Get dataId (Pythonic accessor)."""
        return self._dataId

    @data_id.setter
    def data_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set dataId with validation.
        
        Args:
            value: The dataId to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"dataId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._dataId = value
        # This attribute defines the Id of the Freshness Value.
        # The Value might be a normal counter or a time.
        self._freshnessValue: Optional["PositiveInteger"] = None

    @property
    def freshness_value(self) -> Optional["PositiveInteger"]:
        """Get freshnessValue (Pythonic accessor)."""
        return self._freshnessValue

    @freshness_value.setter
    def freshness_value(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set freshnessValue with validation.
        
        Args:
            value: The freshnessValue to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._freshnessValue = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"freshnessValue must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._freshnessValue = value
        # SecOC links an AuthenticIPdu and CryptographicIPdu by repeating a specific
                # part (Message Linker) of in the CryptographicIPdu.
        # This attribute startPosition in bits of the messageLinker.
        self._messageLink: Optional["PositiveInteger"] = None

    @property
    def message_link(self) -> Optional["PositiveInteger"]:
        """Get messageLink (Pythonic accessor)."""
        return self._messageLink

    @message_link.setter
    def message_link(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set messageLink with validation.
        
        Args:
            value: The messageLink to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._messageLink = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"messageLink must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._messageLink = value
        # This attribute defines the Id of the Secondary Freshness The Secondary
                # Freshness Value might be a counter or a time value.
        # Please note that this for documentation only to allow the required freshness
                # value manager and no is defined for it.
        self._secondary: Optional["PositiveInteger"] = None

    @property
    def secondary(self) -> Optional["PositiveInteger"]:
        """Get secondary (Pythonic accessor)."""
        return self._secondary

    @secondary.setter
    def secondary(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set secondary with validation.
        
        Args:
            value: The secondary to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._secondary = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"secondary must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._secondary = value
        # This attribute defines the start position (offset in byte) of area within the
        # payload Pdu which will be secured.
        self._securedArea: Optional["PositiveInteger"] = None

    @property
    def secured_area(self) -> Optional["PositiveInteger"]:
        """Get securedArea (Pythonic accessor)."""
        return self._securedArea

    @secured_area.setter
    def secured_area(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set securedArea with validation.
        
        Args:
            value: The securedArea to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._securedArea = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"securedArea must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._securedArea = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAuthData(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for authData.
        
        Returns:
            The authData value
        
        Note:
            Delegates to auth_data property (CODING_RULE_V2_00017)
        """
        return self.auth_data  # Delegates to property

    def setAuthData(self, value: "PositiveInteger") -> "SecureCommunicationProps":
        """
        AUTOSAR-compliant setter for authData with method chaining.
        
        Args:
            value: The authData to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to auth_data property setter (gets validation automatically)
        """
        self.auth_data = value  # Delegates to property setter
        return self

    def getAuthentication(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for authentication.
        
        Returns:
            The authentication value
        
        Note:
            Delegates to authentication property (CODING_RULE_V2_00017)
        """
        return self.authentication  # Delegates to property

    def setAuthentication(self, value: "PositiveInteger") -> "SecureCommunicationProps":
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

    def getDataId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for dataId.
        
        Returns:
            The dataId value
        
        Note:
            Delegates to data_id property (CODING_RULE_V2_00017)
        """
        return self.data_id  # Delegates to property

    def setDataId(self, value: "PositiveInteger") -> "SecureCommunicationProps":
        """
        AUTOSAR-compliant setter for dataId with method chaining.
        
        Args:
            value: The dataId to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to data_id property setter (gets validation automatically)
        """
        self.data_id = value  # Delegates to property setter
        return self

    def getFreshnessValue(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for freshnessValue.
        
        Returns:
            The freshnessValue value
        
        Note:
            Delegates to freshness_value property (CODING_RULE_V2_00017)
        """
        return self.freshness_value  # Delegates to property

    def setFreshnessValue(self, value: "PositiveInteger") -> "SecureCommunicationProps":
        """
        AUTOSAR-compliant setter for freshnessValue with method chaining.
        
        Args:
            value: The freshnessValue to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to freshness_value property setter (gets validation automatically)
        """
        self.freshness_value = value  # Delegates to property setter
        return self

    def getMessageLink(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for messageLink.
        
        Returns:
            The messageLink value
        
        Note:
            Delegates to message_link property (CODING_RULE_V2_00017)
        """
        return self.message_link  # Delegates to property

    def setMessageLink(self, value: "PositiveInteger") -> "SecureCommunicationProps":
        """
        AUTOSAR-compliant setter for messageLink with method chaining.
        
        Args:
            value: The messageLink to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to message_link property setter (gets validation automatically)
        """
        self.message_link = value  # Delegates to property setter
        return self

    def getSecondary(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for secondary.
        
        Returns:
            The secondary value
        
        Note:
            Delegates to secondary property (CODING_RULE_V2_00017)
        """
        return self.secondary  # Delegates to property

    def setSecondary(self, value: "PositiveInteger") -> "SecureCommunicationProps":
        """
        AUTOSAR-compliant setter for secondary with method chaining.
        
        Args:
            value: The secondary to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to secondary property setter (gets validation automatically)
        """
        self.secondary = value  # Delegates to property setter
        return self

    def getSecuredArea(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for securedArea.
        
        Returns:
            The securedArea value
        
        Note:
            Delegates to secured_area property (CODING_RULE_V2_00017)
        """
        return self.secured_area  # Delegates to property

    def setSecuredArea(self, value: "PositiveInteger") -> "SecureCommunicationProps":
        """
        AUTOSAR-compliant setter for securedArea with method chaining.
        
        Args:
            value: The securedArea to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to secured_area property setter (gets validation automatically)
        """
        self.secured_area = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_auth_data(self, value: Optional["PositiveInteger"]) -> "SecureCommunicationProps":
        """
        Set authData and return self for chaining.
        
        Args:
            value: The authData to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_auth_data("value")
        """
        self.auth_data = value  # Use property setter (gets validation)
        return self

    def with_authentication(self, value: Optional["PositiveInteger"]) -> "SecureCommunicationProps":
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

    def with_data_id(self, value: Optional["PositiveInteger"]) -> "SecureCommunicationProps":
        """
        Set dataId and return self for chaining.
        
        Args:
            value: The dataId to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_data_id("value")
        """
        self.data_id = value  # Use property setter (gets validation)
        return self

    def with_freshness_value(self, value: Optional["PositiveInteger"]) -> "SecureCommunicationProps":
        """
        Set freshnessValue and return self for chaining.
        
        Args:
            value: The freshnessValue to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_freshness_value("value")
        """
        self.freshness_value = value  # Use property setter (gets validation)
        return self

    def with_message_link(self, value: Optional["PositiveInteger"]) -> "SecureCommunicationProps":
        """
        Set messageLink and return self for chaining.
        
        Args:
            value: The messageLink to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_message_link("value")
        """
        self.message_link = value  # Use property setter (gets validation)
        return self

    def with_secondary(self, value: Optional["PositiveInteger"]) -> "SecureCommunicationProps":
        """
        Set secondary and return self for chaining.
        
        Args:
            value: The secondary to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_secondary("value")
        """
        self.secondary = value  # Use property setter (gets validation)
        return self

    def with_secured_area(self, value: Optional["PositiveInteger"]) -> "SecureCommunicationProps":
        """
        Set securedArea and return self for chaining.
        
        Args:
            value: The securedArea to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_secured_area("value")
        """
        self.secured_area = value  # Use property setter (gets validation)
        return self