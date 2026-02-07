from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class RxIdentifierRange(ARObject):
    """
    Optional definition of a CanId range to reduce the effort of specifying
    every possible FrameTriggering within the defined Id range during reception.
    All frames received within a range are mapped to the same Pdu that is passed
    to a upper layer module (e.g. Nm, CDD, PduR).
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanCommunication::RxIdentifierRange
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 444, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute can be used together with the upperCanId define a range of
        # CanIds.
        self._lowerCanId: Optional["PositiveInteger"] = None

    @property
    def lower_can_id(self) -> Optional["PositiveInteger"]:
        """Get lowerCanId (Pythonic accessor)."""
        return self._lowerCanId

    @lower_can_id.setter
    def lower_can_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set lowerCanId with validation.
        
        Args:
            value: The lowerCanId to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._lowerCanId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"lowerCanId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._lowerCanId = value
        # This attribute can be used together with the lowerCanId define a range of
        # CanIds.
        self._upperCanId: Optional["PositiveInteger"] = None

    @property
    def upper_can_id(self) -> Optional["PositiveInteger"]:
        """Get upperCanId (Pythonic accessor)."""
        return self._upperCanId

    @upper_can_id.setter
    def upper_can_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set upperCanId with validation.
        
        Args:
            value: The upperCanId to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._upperCanId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"upperCanId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._upperCanId = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getLowerCanId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for lowerCanId.
        
        Returns:
            The lowerCanId value
        
        Note:
            Delegates to lower_can_id property (CODING_RULE_V2_00017)
        """
        return self.lower_can_id  # Delegates to property

    def setLowerCanId(self, value: "PositiveInteger") -> "RxIdentifierRange":
        """
        AUTOSAR-compliant setter for lowerCanId with method chaining.
        
        Args:
            value: The lowerCanId to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to lower_can_id property setter (gets validation automatically)
        """
        self.lower_can_id = value  # Delegates to property setter
        return self

    def getUpperCanId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for upperCanId.
        
        Returns:
            The upperCanId value
        
        Note:
            Delegates to upper_can_id property (CODING_RULE_V2_00017)
        """
        return self.upper_can_id  # Delegates to property

    def setUpperCanId(self, value: "PositiveInteger") -> "RxIdentifierRange":
        """
        AUTOSAR-compliant setter for upperCanId with method chaining.
        
        Args:
            value: The upperCanId to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to upper_can_id property setter (gets validation automatically)
        """
        self.upper_can_id = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_lower_can_id(self, value: Optional["PositiveInteger"]) -> "RxIdentifierRange":
        """
        Set lowerCanId and return self for chaining.
        
        Args:
            value: The lowerCanId to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_lower_can_id("value")
        """
        self.lower_can_id = value  # Use property setter (gets validation)
        return self

    def with_upper_can_id(self, value: Optional["PositiveInteger"]) -> "RxIdentifierRange":
        """
        Set upperCanId and return self for chaining.
        
        Args:
            value: The upperCanId to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_upper_can_id("value")
        """
        self.upper_can_id = value  # Use property setter (gets validation)
        return self