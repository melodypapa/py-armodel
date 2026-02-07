from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

class IEEE1722TpAcfLinPart(IEEE1722TpAcfBusPart):
    """
    Definition of one LIN part transported over the IEEE1722Tp channel.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp::IEEE1722TpAcf::IEEE1722TpAcfLinPart
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 667, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Optional Lin Id defined in case the Lin Id can not be runtime.
        self._linIdentifier: Optional["PositiveInteger"] = None

    @property
    def lin_identifier(self) -> Optional["PositiveInteger"]:
        """Get linIdentifier (Pythonic accessor)."""
        return self._linIdentifier

    @lin_identifier.setter
    def lin_identifier(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set linIdentifier with validation.
        
        Args:
            value: The linIdentifier to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._linIdentifier = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"linIdentifier must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._linIdentifier = value
        # Reference to the Pdu transported in the IEEE1722Tp.
        self._sdu: RefType = None

    @property
    def sdu(self) -> RefType:
        """Get sdu (Pythonic accessor)."""
        return self._sdu

    @sdu.setter
    def sdu(self, value: RefType) -> None:
        """
        Set sdu with validation.
        
        Args:
            value: The sdu to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sdu = None
            return

        self._sdu = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getLinIdentifier(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for linIdentifier.
        
        Returns:
            The linIdentifier value
        
        Note:
            Delegates to lin_identifier property (CODING_RULE_V2_00017)
        """
        return self.lin_identifier  # Delegates to property

    def setLinIdentifier(self, value: "PositiveInteger") -> "IEEE1722TpAcfLinPart":
        """
        AUTOSAR-compliant setter for linIdentifier with method chaining.
        
        Args:
            value: The linIdentifier to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to lin_identifier property setter (gets validation automatically)
        """
        self.lin_identifier = value  # Delegates to property setter
        return self

    def getSdu(self) -> RefType:
        """
        AUTOSAR-compliant getter for sdu.
        
        Returns:
            The sdu value
        
        Note:
            Delegates to sdu property (CODING_RULE_V2_00017)
        """
        return self.sdu  # Delegates to property

    def setSdu(self, value: RefType) -> "IEEE1722TpAcfLinPart":
        """
        AUTOSAR-compliant setter for sdu with method chaining.
        
        Args:
            value: The sdu to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sdu property setter (gets validation automatically)
        """
        self.sdu = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_lin_identifier(self, value: Optional["PositiveInteger"]) -> "IEEE1722TpAcfLinPart":
        """
        Set linIdentifier and return self for chaining.
        
        Args:
            value: The linIdentifier to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_lin_identifier("value")
        """
        self.lin_identifier = value  # Use property setter (gets validation)
        return self

    def with_sdu(self, value: Optional[RefType]) -> "IEEE1722TpAcfLinPart":
        """
        Set sdu and return self for chaining.
        
        Args:
            value: The sdu to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sdu("value")
        """
        self.sdu = value  # Use property setter (gets validation)
        return self