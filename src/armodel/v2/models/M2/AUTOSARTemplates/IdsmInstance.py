from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class IdsmInstance(IdsCommonElement):
    """
    This meta-class provides the ability to create a relation between an
    EcuInstance and a specific class of filters for security events that apply
    for all security events reported on the referenced EcuInstance.
    
    Package: M2::AUTOSARTemplates::SecurityExtractTemplate::IdsmInstance
    
    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 44, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference defines the BlockState in the collection.
        self._blockState: List["BlockState"] = []

    @property
    def block_state(self) -> List["BlockState"]:
        """Get blockState (Pythonic accessor)."""
        return self._blockState
        # This reference identifies the EcuInstance whose security any type) shall be
        # limited by the specific class atpVariation.
        self._ecuInstance: Optional["EcuInstance"] = None

    @property
    def ecu_instance(self) -> Optional["EcuInstance"]:
        """Get ecuInstance (Pythonic accessor)."""
        return self._ecuInstance

    @ecu_instance.setter
    def ecu_instance(self, value: Optional["EcuInstance"]) -> None:
        """
        Set ecuInstance with validation.
        
        Args:
            value: The ecuInstance to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ecuInstance = None
            return

        if not isinstance(value, EcuInstance):
            raise TypeError(
                f"ecuInstance must be EcuInstance or None, got {type(value).__name__}"
            )
        self._ecuInstance = value
        # This attribute is used to provide a source identification in of reporting
        # security events.
        self._idsmInstanceId: Optional["PositiveInteger"] = None

    @property
    def idsm_instance_id(self) -> Optional["PositiveInteger"]:
        """Get idsmInstanceId (Pythonic accessor)."""
        return self._idsmInstanceId

    @idsm_instance_id.setter
    def idsm_instance_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set idsmInstanceId with validation.
        
        Args:
            value: The idsmInstanceId to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._idsmInstanceId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"idsmInstanceId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._idsmInstanceId = value
        # This reference identifies the meta-class that defines the attributes for the
        # IdsM configuration on a specific.
        self._idsmModule: Optional["IdsmModule"] = None

    @property
    def idsm_module(self) -> Optional["IdsmModule"]:
        """Get idsmModule (Pythonic accessor)."""
        return self._idsmModule

    @idsm_module.setter
    def idsm_module(self, value: Optional["IdsmModule"]) -> None:
        """
        Set idsmModule with validation.
        
        Args:
            value: The idsmModule to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._idsmModule = None
            return

        if not isinstance(value, IdsmModule):
            raise TypeError(
                f"idsmModule must be IdsmModule or None, got {type(value).__name__}"
            )
        self._idsmModule = value
        # This reference identifies the applicable rate limitation filter all security
                # events on the related EcuInstance.
        # atpVariation.
        self._rateLimitation: Optional["IdsmRateLimitation"] = None

    @property
    def rate_limitation(self) -> Optional["IdsmRateLimitation"]:
        """Get rateLimitation (Pythonic accessor)."""
        return self._rateLimitation

    @rate_limitation.setter
    def rate_limitation(self, value: Optional["IdsmRateLimitation"]) -> None:
        """
        Set rateLimitation with validation.
        
        Args:
            value: The rateLimitation to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rateLimitation = None
            return

        if not isinstance(value, IdsmRateLimitation):
            raise TypeError(
                f"rateLimitation must be IdsmRateLimitation or None, got {type(value).__name__}"
            )
        self._rateLimitation = value
        # The existence of this aggregation specifies that the IdsM shall add a
                # signature to the QSEv messages it sends network.
        # The cryptographic algorithm and key to for this signature is further
                # specified by the specifically for the Classic.
        self._signature: Optional["IdsmSignatureSupport"] = None

    @property
    def signature(self) -> Optional["IdsmSignatureSupport"]:
        """Get signature (Pythonic accessor)."""
        return self._signature

    @signature.setter
    def signature(self, value: Optional["IdsmSignatureSupport"]) -> None:
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

        if not isinstance(value, IdsmSignatureSupport):
            raise TypeError(
                f"signature must be IdsmSignatureSupport or None, got {type(value).__name__}"
            )
        self._signature = value
        # The existence of this attribute specifies that the IdsM shall a timestamp to
                # the QSEv messages it sends onto the if this attribute does not exist, no
                # timestamp added to the QSEv messages.
        # of this attribute further specifies the as follows: - "AUTOSAR" defines
                # timestamp format according to Time-Base Manager - Any other string
                # proprietary timestamp format.
        # string defining a proprietary timestamp format prefixed by a company-specific
                # name fragment to.
        self._timestamp: Optional["String"] = None

    @property
    def timestamp(self) -> Optional["String"]:
        """Get timestamp (Pythonic accessor)."""
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value: Optional["String"]) -> None:
        """
        Set timestamp with validation.
        
        Args:
            value: The timestamp to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timestamp = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"timestamp must be String or None, got {type(value).__name__}"
            )
        self._timestamp = value
        # This reference identifies the applicable traffic limitation for all security
                # events on the related EcuInstance.
        # atpVariation.
        self._trafficLimitation: Optional["IdsmTrafficLimitation"] = None

    @property
    def traffic_limitation(self) -> Optional["IdsmTrafficLimitation"]:
        """Get trafficLimitation (Pythonic accessor)."""
        return self._trafficLimitation

    @traffic_limitation.setter
    def traffic_limitation(self, value: Optional["IdsmTrafficLimitation"]) -> None:
        """
        Set trafficLimitation with validation.
        
        Args:
            value: The trafficLimitation to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._trafficLimitation = None
            return

        if not isinstance(value, IdsmTrafficLimitation):
            raise TypeError(
                f"trafficLimitation must be IdsmTrafficLimitation or None, got {type(value).__name__}"
            )
        self._trafficLimitation = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBlockState(self) -> List["BlockState"]:
        """
        AUTOSAR-compliant getter for blockState.
        
        Returns:
            The blockState value
        
        Note:
            Delegates to block_state property (CODING_RULE_V2_00017)
        """
        return self.block_state  # Delegates to property

    def getEcuInstance(self) -> "EcuInstance":
        """
        AUTOSAR-compliant getter for ecuInstance.
        
        Returns:
            The ecuInstance value
        
        Note:
            Delegates to ecu_instance property (CODING_RULE_V2_00017)
        """
        return self.ecu_instance  # Delegates to property

    def setEcuInstance(self, value: "EcuInstance") -> "IdsmInstance":
        """
        AUTOSAR-compliant setter for ecuInstance with method chaining.
        
        Args:
            value: The ecuInstance to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to ecu_instance property setter (gets validation automatically)
        """
        self.ecu_instance = value  # Delegates to property setter
        return self

    def getIdsmInstanceId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for idsmInstanceId.
        
        Returns:
            The idsmInstanceId value
        
        Note:
            Delegates to idsm_instance_id property (CODING_RULE_V2_00017)
        """
        return self.idsm_instance_id  # Delegates to property

    def setIdsmInstanceId(self, value: "PositiveInteger") -> "IdsmInstance":
        """
        AUTOSAR-compliant setter for idsmInstanceId with method chaining.
        
        Args:
            value: The idsmInstanceId to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to idsm_instance_id property setter (gets validation automatically)
        """
        self.idsm_instance_id = value  # Delegates to property setter
        return self

    def getIdsmModule(self) -> "IdsmModule":
        """
        AUTOSAR-compliant getter for idsmModule.
        
        Returns:
            The idsmModule value
        
        Note:
            Delegates to idsm_module property (CODING_RULE_V2_00017)
        """
        return self.idsm_module  # Delegates to property

    def setIdsmModule(self, value: "IdsmModule") -> "IdsmInstance":
        """
        AUTOSAR-compliant setter for idsmModule with method chaining.
        
        Args:
            value: The idsmModule to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to idsm_module property setter (gets validation automatically)
        """
        self.idsm_module = value  # Delegates to property setter
        return self

    def getRateLimitation(self) -> "IdsmRateLimitation":
        """
        AUTOSAR-compliant getter for rateLimitation.
        
        Returns:
            The rateLimitation value
        
        Note:
            Delegates to rate_limitation property (CODING_RULE_V2_00017)
        """
        return self.rate_limitation  # Delegates to property

    def setRateLimitation(self, value: "IdsmRateLimitation") -> "IdsmInstance":
        """
        AUTOSAR-compliant setter for rateLimitation with method chaining.
        
        Args:
            value: The rateLimitation to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to rate_limitation property setter (gets validation automatically)
        """
        self.rate_limitation = value  # Delegates to property setter
        return self

    def getSignature(self) -> "IdsmSignatureSupport":
        """
        AUTOSAR-compliant getter for signature.
        
        Returns:
            The signature value
        
        Note:
            Delegates to signature property (CODING_RULE_V2_00017)
        """
        return self.signature  # Delegates to property

    def setSignature(self, value: "IdsmSignatureSupport") -> "IdsmInstance":
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

    def getTimestamp(self) -> "String":
        """
        AUTOSAR-compliant getter for timestamp.
        
        Returns:
            The timestamp value
        
        Note:
            Delegates to timestamp property (CODING_RULE_V2_00017)
        """
        return self.timestamp  # Delegates to property

    def setTimestamp(self, value: "String") -> "IdsmInstance":
        """
        AUTOSAR-compliant setter for timestamp with method chaining.
        
        Args:
            value: The timestamp to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to timestamp property setter (gets validation automatically)
        """
        self.timestamp = value  # Delegates to property setter
        return self

    def getTrafficLimitation(self) -> "IdsmTrafficLimitation":
        """
        AUTOSAR-compliant getter for trafficLimitation.
        
        Returns:
            The trafficLimitation value
        
        Note:
            Delegates to traffic_limitation property (CODING_RULE_V2_00017)
        """
        return self.traffic_limitation  # Delegates to property

    def setTrafficLimitation(self, value: "IdsmTrafficLimitation") -> "IdsmInstance":
        """
        AUTOSAR-compliant setter for trafficLimitation with method chaining.
        
        Args:
            value: The trafficLimitation to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to traffic_limitation property setter (gets validation automatically)
        """
        self.traffic_limitation = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ecu_instance(self, value: Optional["EcuInstance"]) -> "IdsmInstance":
        """
        Set ecuInstance and return self for chaining.
        
        Args:
            value: The ecuInstance to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_ecu_instance("value")
        """
        self.ecu_instance = value  # Use property setter (gets validation)
        return self

    def with_idsm_instance_id(self, value: Optional["PositiveInteger"]) -> "IdsmInstance":
        """
        Set idsmInstanceId and return self for chaining.
        
        Args:
            value: The idsmInstanceId to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_idsm_instance_id("value")
        """
        self.idsm_instance_id = value  # Use property setter (gets validation)
        return self

    def with_idsm_module(self, value: Optional["IdsmModule"]) -> "IdsmInstance":
        """
        Set idsmModule and return self for chaining.
        
        Args:
            value: The idsmModule to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_idsm_module("value")
        """
        self.idsm_module = value  # Use property setter (gets validation)
        return self

    def with_rate_limitation(self, value: Optional["IdsmRateLimitation"]) -> "IdsmInstance":
        """
        Set rateLimitation and return self for chaining.
        
        Args:
            value: The rateLimitation to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_rate_limitation("value")
        """
        self.rate_limitation = value  # Use property setter (gets validation)
        return self

    def with_signature(self, value: Optional["IdsmSignatureSupport"]) -> "IdsmInstance":
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

    def with_timestamp(self, value: Optional["String"]) -> "IdsmInstance":
        """
        Set timestamp and return self for chaining.
        
        Args:
            value: The timestamp to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_timestamp("value")
        """
        self.timestamp = value  # Use property setter (gets validation)
        return self

    def with_traffic_limitation(self, value: Optional["IdsmTrafficLimitation"]) -> "IdsmInstance":
        """
        Set trafficLimitation and return self for chaining.
        
        Args:
            value: The trafficLimitation to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_traffic_limitation("value")
        """
        self.traffic_limitation = value  # Use property setter (gets validation)
        return self