from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class BswModeSenderPolicy(ARObject):
    """
    Specifies the details for the sending of a mode switch for the referred mode
    group.
    
    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswModeSenderPolicy
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 102, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Request for acknowledgement.
        self._ackRequestRequest: Optional["BswModeSwitchAck"] = None

    @property
    def ack_request_request(self) -> Optional["BswModeSwitchAck"]:
        """Get ackRequestRequest (Pythonic accessor)."""
        return self._ackRequestRequest

    @ack_request_request.setter
    def ack_request_request(self, value: Optional["BswModeSwitchAck"]) -> None:
        """
        Set ackRequestRequest with validation.
        
        Args:
            value: The ackRequestRequest to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ackRequestRequest = None
            return

        if not isinstance(value, BswModeSwitchAck):
            raise TypeError(
                f"ackRequestRequest must be BswModeSwitchAck or None, got {type(value).__name__}"
            )
        self._ackRequestRequest = value
        # This controls the creation of the enhanced mode API that information about
                # the previous mode and the next set to TRUE the enhanced mode API is be
                # generated.
        # For more details please refer SWS_RTE.
        self._enhancedMode: Optional["Boolean"] = None

    @property
    def enhanced_mode(self) -> Optional["Boolean"]:
        """Get enhancedMode (Pythonic accessor)."""
        return self._enhancedMode

    @enhanced_mode.setter
    def enhanced_mode(self, value: Optional["Boolean"]) -> None:
        """
        Set enhancedMode with validation.
        
        Args:
            value: The enhancedMode to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._enhancedMode = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"enhancedMode must be Boolean or None, got {type(value).__name__}"
            )
        self._enhancedMode = value
        # The provided mode group for which the policy is specified.
        # 381 Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module
                # Description Template R23-11.
        self._providedMode: RefType = None

    @property
    def provided_mode(self) -> RefType:
        """Get providedMode (Pythonic accessor)."""
        return self._providedMode

    @provided_mode.setter
    def provided_mode(self, value: RefType) -> None:
        """
        Set providedMode with validation.
        
        Args:
            value: The providedMode to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._providedMode = None
            return

        self._providedMode = value
        # Length of call queue on the sender side.
        # The queue is the RTE resp.
        # BswScheduler.
        # The value greater or equal to 0.
        # Setting the value of queue 0 implies non-queued communication.
        self._queueLength: Optional["PositiveInteger"] = None

    @property
    def queue_length(self) -> Optional["PositiveInteger"]:
        """Get queueLength (Pythonic accessor)."""
        return self._queueLength

    @queue_length.setter
    def queue_length(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set queueLength with validation.
        
        Args:
            value: The queueLength to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._queueLength = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"queueLength must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._queueLength = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAckRequestRequest(self) -> "BswModeSwitchAck":
        """
        AUTOSAR-compliant getter for ackRequestRequest.
        
        Returns:
            The ackRequestRequest value
        
        Note:
            Delegates to ack_request_request property (CODING_RULE_V2_00017)
        """
        return self.ack_request_request  # Delegates to property

    def setAckRequestRequest(self, value: "BswModeSwitchAck") -> "BswModeSenderPolicy":
        """
        AUTOSAR-compliant setter for ackRequestRequest with method chaining.
        
        Args:
            value: The ackRequestRequest to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to ack_request_request property setter (gets validation automatically)
        """
        self.ack_request_request = value  # Delegates to property setter
        return self

    def getEnhancedMode(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for enhancedMode.
        
        Returns:
            The enhancedMode value
        
        Note:
            Delegates to enhanced_mode property (CODING_RULE_V2_00017)
        """
        return self.enhanced_mode  # Delegates to property

    def setEnhancedMode(self, value: "Boolean") -> "BswModeSenderPolicy":
        """
        AUTOSAR-compliant setter for enhancedMode with method chaining.
        
        Args:
            value: The enhancedMode to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to enhanced_mode property setter (gets validation automatically)
        """
        self.enhanced_mode = value  # Delegates to property setter
        return self

    def getProvidedMode(self) -> RefType:
        """
        AUTOSAR-compliant getter for providedMode.
        
        Returns:
            The providedMode value
        
        Note:
            Delegates to provided_mode property (CODING_RULE_V2_00017)
        """
        return self.provided_mode  # Delegates to property

    def setProvidedMode(self, value: RefType) -> "BswModeSenderPolicy":
        """
        AUTOSAR-compliant setter for providedMode with method chaining.
        
        Args:
            value: The providedMode to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to provided_mode property setter (gets validation automatically)
        """
        self.provided_mode = value  # Delegates to property setter
        return self

    def getQueueLength(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for queueLength.
        
        Returns:
            The queueLength value
        
        Note:
            Delegates to queue_length property (CODING_RULE_V2_00017)
        """
        return self.queue_length  # Delegates to property

    def setQueueLength(self, value: "PositiveInteger") -> "BswModeSenderPolicy":
        """
        AUTOSAR-compliant setter for queueLength with method chaining.
        
        Args:
            value: The queueLength to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to queue_length property setter (gets validation automatically)
        """
        self.queue_length = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ack_request_request(self, value: Optional["BswModeSwitchAck"]) -> "BswModeSenderPolicy":
        """
        Set ackRequestRequest and return self for chaining.
        
        Args:
            value: The ackRequestRequest to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_ack_request_request("value")
        """
        self.ack_request_request = value  # Use property setter (gets validation)
        return self

    def with_enhanced_mode(self, value: Optional["Boolean"]) -> "BswModeSenderPolicy":
        """
        Set enhancedMode and return self for chaining.
        
        Args:
            value: The enhancedMode to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_enhanced_mode("value")
        """
        self.enhanced_mode = value  # Use property setter (gets validation)
        return self

    def with_provided_mode(self, value: Optional[RefType]) -> "BswModeSenderPolicy":
        """
        Set providedMode and return self for chaining.
        
        Args:
            value: The providedMode to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_provided_mode("value")
        """
        self.provided_mode = value  # Use property setter (gets validation)
        return self

    def with_queue_length(self, value: Optional["PositiveInteger"]) -> "BswModeSenderPolicy":
        """
        Set queueLength and return self for chaining.
        
        Args:
            value: The queueLength to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_queue_length("value")
        """
        self.queue_length = value  # Use property setter (gets validation)
        return self