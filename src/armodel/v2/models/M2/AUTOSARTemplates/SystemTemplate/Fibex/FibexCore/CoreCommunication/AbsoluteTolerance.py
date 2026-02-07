from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class AbsoluteTolerance(ARObject):
    """
    Maximum allowable deviation
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::Timing::AbsoluteTolerance
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 398, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Maximum allowable deviation in duration (in seconds).
        self._absolute: Optional["TimeValue"] = None

    @property
    def absolute(self) -> Optional["TimeValue"]:
        """Get absolute (Pythonic accessor)."""
        return self._absolute

    @absolute.setter
    def absolute(self, value: Optional["TimeValue"]) -> None:
        """
        Set absolute with validation.
        
        Args:
            value: The absolute to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._absolute = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"absolute must be TimeValue or None, got {type(value).__name__}"
            )
        self._absolute = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAbsolute(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for absolute.
        
        Returns:
            The absolute value
        
        Note:
            Delegates to absolute property (CODING_RULE_V2_00017)
        """
        return self.absolute  # Delegates to property

    def setAbsolute(self, value: "TimeValue") -> "AbsoluteTolerance":
        """
        AUTOSAR-compliant setter for absolute with method chaining.
        
        Args:
            value: The absolute to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to absolute property setter (gets validation automatically)
        """
        self.absolute = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_absolute(self, value: Optional["TimeValue"]) -> "AbsoluteTolerance":
        """
        Set absolute and return self for chaining.
        
        Args:
            value: The absolute to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_absolute("value")
        """
        self.absolute = value  # Use property setter (gets validation)
        return self