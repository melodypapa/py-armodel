from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class ClientServerApplicationErrorMapping(ARObject):
    """
    This meta-class represents the ability to map ApplicationErrors onto each
    other.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::ClientServerApplicationErrorMapping
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 129, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the first ApplicationError in the context of
        # ClientServerApplicationErrorMapping.
        self._firstApplication: Optional["ApplicationError"] = None

    @property
    def first_application(self) -> Optional["ApplicationError"]:
        """Get firstApplication (Pythonic accessor)."""
        return self._firstApplication

    @first_application.setter
    def first_application(self, value: Optional["ApplicationError"]) -> None:
        """
        Set firstApplication with validation.
        
        Args:
            value: The firstApplication to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._firstApplication = None
            return

        if not isinstance(value, ApplicationError):
            raise TypeError(
                f"firstApplication must be ApplicationError or None, got {type(value).__name__}"
            )
        self._firstApplication = value
        # This represents the second ApplicationError in the of the
        # ClientServerApplicationErrorMapping.
        self._second: Optional["ApplicationError"] = None

    @property
    def second(self) -> Optional["ApplicationError"]:
        """Get second (Pythonic accessor)."""
        return self._second

    @second.setter
    def second(self, value: Optional["ApplicationError"]) -> None:
        """
        Set second with validation.
        
        Args:
            value: The second to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._second = None
            return

        if not isinstance(value, ApplicationError):
            raise TypeError(
                f"second must be ApplicationError or None, got {type(value).__name__}"
            )
        self._second = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFirstApplication(self) -> "ApplicationError":
        """
        AUTOSAR-compliant getter for firstApplication.
        
        Returns:
            The firstApplication value
        
        Note:
            Delegates to first_application property (CODING_RULE_V2_00017)
        """
        return self.first_application  # Delegates to property

    def setFirstApplication(self, value: "ApplicationError") -> "ClientServerApplicationErrorMapping":
        """
        AUTOSAR-compliant setter for firstApplication with method chaining.
        
        Args:
            value: The firstApplication to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to first_application property setter (gets validation automatically)
        """
        self.first_application = value  # Delegates to property setter
        return self

    def getSecond(self) -> "ApplicationError":
        """
        AUTOSAR-compliant getter for second.
        
        Returns:
            The second value
        
        Note:
            Delegates to second property (CODING_RULE_V2_00017)
        """
        return self.second  # Delegates to property

    def setSecond(self, value: "ApplicationError") -> "ClientServerApplicationErrorMapping":
        """
        AUTOSAR-compliant setter for second with method chaining.
        
        Args:
            value: The second to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to second property setter (gets validation automatically)
        """
        self.second = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_first_application(self, value: Optional["ApplicationError"]) -> "ClientServerApplicationErrorMapping":
        """
        Set firstApplication and return self for chaining.
        
        Args:
            value: The firstApplication to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_first_application("value")
        """
        self.first_application = value  # Use property setter (gets validation)
        return self

    def with_second(self, value: Optional["ApplicationError"]) -> "ClientServerApplicationErrorMapping":
        """
        Set second and return self for chaining.
        
        Args:
            value: The second to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_second("value")
        """
        self.second = value  # Use property setter (gets validation)
        return self