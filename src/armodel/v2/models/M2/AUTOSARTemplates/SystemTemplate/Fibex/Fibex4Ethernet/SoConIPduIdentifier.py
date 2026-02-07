from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Referrable import Referrable

class SoConIPduIdentifier(Referrable):
    """
    Identification of Pdu content on a socket connection. This Identifier is
    required in case that multiple Pdus are transmitted over the same socket
    connection.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances::SoConIPduIdentifier
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 489, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # If multiple Pdus are transmitted over the same connection can be used to
        # distinguish between the constraints on constructing the headerId for see
        # PRS_SOMEIP_00245.
        self._headerId: Optional["PositiveInteger"] = None

    @property
    def header_id(self) -> Optional["PositiveInteger"]:
        """Get headerId (Pythonic accessor)."""
        return self._headerId

    @header_id.setter
    def header_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set headerId with validation.
        
        Args:
            value: The headerId to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._headerId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"headerId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._headerId = value
        # Defines whether the referenced Pdu contributes to the triggering of the
        # socket transmission if Pdu collection is this socket.
        self._pduCollection: RefType = None

    @property
    def pdu_collection(self) -> RefType:
        """Get pduCollection (Pythonic accessor)."""
        return self._pduCollection

    @pdu_collection.setter
    def pdu_collection(self, value: RefType) -> None:
        """
        Set pduCollection with validation.
        
        Args:
            value: The pduCollection to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pduCollection = None
            return

        self._pduCollection = value
        # Reference to a Pdu that is transmitted over a socket.
        self._pduTriggering: RefType = None

    @property
    def pdu_triggering(self) -> RefType:
        """Get pduTriggering (Pythonic accessor)."""
        return self._pduTriggering

    @pdu_triggering.setter
    def pdu_triggering(self, value: RefType) -> None:
        """
        Set pduTriggering with validation.
        
        Args:
            value: The pduTriggering to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pduTriggering = None
            return

        self._pduTriggering = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getHeaderId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for headerId.
        
        Returns:
            The headerId value
        
        Note:
            Delegates to header_id property (CODING_RULE_V2_00017)
        """
        return self.header_id  # Delegates to property

    def setHeaderId(self, value: "PositiveInteger") -> "SoConIPduIdentifier":
        """
        AUTOSAR-compliant setter for headerId with method chaining.
        
        Args:
            value: The headerId to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to header_id property setter (gets validation automatically)
        """
        self.header_id = value  # Delegates to property setter
        return self

    def getPduCollection(self) -> RefType:
        """
        AUTOSAR-compliant getter for pduCollection.
        
        Returns:
            The pduCollection value
        
        Note:
            Delegates to pdu_collection property (CODING_RULE_V2_00017)
        """
        return self.pdu_collection  # Delegates to property

    def setPduCollection(self, value: RefType) -> "SoConIPduIdentifier":
        """
        AUTOSAR-compliant setter for pduCollection with method chaining.
        
        Args:
            value: The pduCollection to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to pdu_collection property setter (gets validation automatically)
        """
        self.pdu_collection = value  # Delegates to property setter
        return self

    def getPduTriggering(self) -> RefType:
        """
        AUTOSAR-compliant getter for pduTriggering.
        
        Returns:
            The pduTriggering value
        
        Note:
            Delegates to pdu_triggering property (CODING_RULE_V2_00017)
        """
        return self.pdu_triggering  # Delegates to property

    def setPduTriggering(self, value: RefType) -> "SoConIPduIdentifier":
        """
        AUTOSAR-compliant setter for pduTriggering with method chaining.
        
        Args:
            value: The pduTriggering to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to pdu_triggering property setter (gets validation automatically)
        """
        self.pdu_triggering = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_header_id(self, value: Optional["PositiveInteger"]) -> "SoConIPduIdentifier":
        """
        Set headerId and return self for chaining.
        
        Args:
            value: The headerId to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_header_id("value")
        """
        self.header_id = value  # Use property setter (gets validation)
        return self

    def with_pdu_collection(self, value: Optional[RefType]) -> "SoConIPduIdentifier":
        """
        Set pduCollection and return self for chaining.
        
        Args:
            value: The pduCollection to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_pdu_collection("value")
        """
        self.pdu_collection = value  # Use property setter (gets validation)
        return self

    def with_pdu_triggering(self, value: Optional[RefType]) -> "SoConIPduIdentifier":
        """
        Set pduTriggering and return self for chaining.
        
        Args:
            value: The pduTriggering to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_pdu_triggering("value")
        """
        self.pdu_triggering = value  # Use property setter (gets validation)
        return self