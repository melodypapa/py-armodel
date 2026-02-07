from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class ExecutableEntityActivationReason(ImplementationProps):
    """
    This meta-class represents the ability to define the reason for the
    activation of the enclosing Executable Entity.
    
    Package: M2::AUTOSARTemplates::CommonStructure::InternalBehavior::ExecutableEntityActivationReason
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 315, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 538, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute allows for defining the position of the in the.
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

    def setBitPosition(self, value: "PositiveInteger") -> "ExecutableEntityActivationReason":
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bit_position(self, value: Optional["PositiveInteger"]) -> "ExecutableEntityActivationReason":
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