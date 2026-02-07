from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class InstantiationRTEEventProps(ARObject, ABC):
    """
    This meta-class represents the ability to refine the properties of RTEEvents
    for particular instances of a software component.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::Composition::InstantiationRTEEventProps
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 85, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is InstantiationRTEEventProps:
            raise TypeError("InstantiationRTEEventProps is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # be refined on an instance level.
        # by: InstanceEventIn.
        self._refinedEvent: Optional["RTEEvent"] = None

    @property
    def refined_event(self) -> Optional["RTEEvent"]:
        """Get refinedEvent (Pythonic accessor)."""
        return self._refinedEvent

    @refined_event.setter
    def refined_event(self, value: Optional["RTEEvent"]) -> None:
        """
        Set refinedEvent with validation.
        
        Args:
            value: The refinedEvent to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._refinedEvent = None
            return

        if not isinstance(value, RTEEvent):
            raise TypeError(
                f"refinedEvent must be RTEEvent or None, got {type(value).__name__}"
            )
        self._refinedEvent = value
        # The main purpose of the shortLabel is to contribute to the aggregations that
        # are <<atpSplitable>>.
        self._shortLabel: Optional["Identifier"] = None

    @property
    def short_label(self) -> Optional["Identifier"]:
        """Get shortLabel (Pythonic accessor)."""
        return self._shortLabel

    @short_label.setter
    def short_label(self, value: Optional["Identifier"]) -> None:
        """
        Set shortLabel with validation.
        
        Args:
            value: The shortLabel to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._shortLabel = None
            return

        if not isinstance(value, Identifier):
            raise TypeError(
                f"shortLabel must be Identifier or None, got {type(value).__name__}"
            )
        self._shortLabel = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRefinedEvent(self) -> "RTEEvent":
        """
        AUTOSAR-compliant getter for refinedEvent.
        
        Returns:
            The refinedEvent value
        
        Note:
            Delegates to refined_event property (CODING_RULE_V2_00017)
        """
        return self.refined_event  # Delegates to property

    def setRefinedEvent(self, value: "RTEEvent") -> "InstantiationRTEEventProps":
        """
        AUTOSAR-compliant setter for refinedEvent with method chaining.
        
        Args:
            value: The refinedEvent to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to refined_event property setter (gets validation automatically)
        """
        self.refined_event = value  # Delegates to property setter
        return self

    def getShortLabel(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for shortLabel.
        
        Returns:
            The shortLabel value
        
        Note:
            Delegates to short_label property (CODING_RULE_V2_00017)
        """
        return self.short_label  # Delegates to property

    def setShortLabel(self, value: "Identifier") -> "InstantiationRTEEventProps":
        """
        AUTOSAR-compliant setter for shortLabel with method chaining.
        
        Args:
            value: The shortLabel to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to short_label property setter (gets validation automatically)
        """
        self.short_label = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_refined_event(self, value: Optional["RTEEvent"]) -> "InstantiationRTEEventProps":
        """
        Set refinedEvent and return self for chaining.
        
        Args:
            value: The refinedEvent to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_refined_event("value")
        """
        self.refined_event = value  # Use property setter (gets validation)
        return self

    def with_short_label(self, value: Optional["Identifier"]) -> "InstantiationRTEEventProps":
        """
        Set shortLabel and return self for chaining.
        
        Args:
            value: The shortLabel to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_short_label("value")
        """
        self.short_label = value  # Use property setter (gets validation)
        return self