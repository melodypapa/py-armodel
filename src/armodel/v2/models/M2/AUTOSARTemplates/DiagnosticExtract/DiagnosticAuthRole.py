from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class DiagnosticAuthRole(DiagnosticCommonElement):
    """
    This meta-class represents the ability to specify an authentication role
    that can be used to deliver fine-grained access rights.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticAuthRole
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 77, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute allows for the specification of the position of role in a
        # bitfield of roles.
        self._bitPosition: Optional["PositiveInteger"] = None

    @property
    def bit_position(self) -> Optional["PositiveInteger"]:
        """Get bitPosition (Pythonic accessor)."""
        return self._bitPosition

    @bit_position.setter
    def bit_position(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set bitPosition with validation.
        
        Args:
            value: The bitPosition to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bitPosition = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"bitPosition must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._bitPosition = value
        # This attribute indicates whether the enclosing role is default role.
        self._isDefault: Optional["Boolean"] = None

    @property
    def is_default(self) -> Optional["Boolean"]:
        """Get isDefault (Pythonic accessor)."""
        return self._isDefault

    @is_default.setter
    def is_default(self, value: Optional["Boolean"]) -> None:
        """
        Set isDefault with validation.
        
        Args:
            value: The isDefault to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._isDefault = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"isDefault must be Boolean or None, got {type(value).__name__}"
            )
        self._isDefault = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBitPosition(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for bitPosition.
        
        Returns:
            The bitPosition value
        
        Note:
            Delegates to bit_position property (CODING_RULE_V2_00017)
        """
        return self.bit_position  # Delegates to property

    def setBitPosition(self, value: "PositiveInteger") -> "DiagnosticAuthRole":
        """
        AUTOSAR-compliant setter for bitPosition with method chaining.
        
        Args:
            value: The bitPosition to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to bit_position property setter (gets validation automatically)
        """
        self.bit_position = value  # Delegates to property setter
        return self

    def getIsDefault(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for isDefault.
        
        Returns:
            The isDefault value
        
        Note:
            Delegates to is_default property (CODING_RULE_V2_00017)
        """
        return self.is_default  # Delegates to property

    def setIsDefault(self, value: "Boolean") -> "DiagnosticAuthRole":
        """
        AUTOSAR-compliant setter for isDefault with method chaining.
        
        Args:
            value: The isDefault to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to is_default property setter (gets validation automatically)
        """
        self.is_default = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bit_position(self, value: Optional["PositiveInteger"]) -> "DiagnosticAuthRole":
        """
        Set bitPosition and return self for chaining.
        
        Args:
            value: The bitPosition to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_bit_position("value")
        """
        self.bit_position = value  # Use property setter (gets validation)
        return self

    def with_is_default(self, value: Optional["Boolean"]) -> "DiagnosticAuthRole":
        """
        Set isDefault and return self for chaining.
        
        Args:
            value: The isDefault to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_is_default("value")
        """
        self.is_default = value  # Use property setter (gets validation)
        return self