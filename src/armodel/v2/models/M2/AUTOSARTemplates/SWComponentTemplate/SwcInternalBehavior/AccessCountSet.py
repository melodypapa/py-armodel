from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class AccessCountSet(ARObject):
    """
    This meta-class provides a set of count values evaluated according to the
    rules of a specific countProfile.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::AccessCount::AccessCountSet
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 57, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Count value for a AbstractAccessPoint.
        # atpVariation.
        self._accessCount: List["AccessCount"] = []

    @property
    def access_count(self) -> List["AccessCount"]:
        """Get accessCount (Pythonic accessor)."""
        return self._accessCount
        # This attribute defines the name of the count profile used the AccessCount.
        # value numbers.
        self._countProfile: Optional["NameToken"] = None

    @property
    def count_profile(self) -> Optional["NameToken"]:
        """Get countProfile (Pythonic accessor)."""
        return self._countProfile

    @count_profile.setter
    def count_profile(self, value: Optional["NameToken"]) -> None:
        """
        Set countProfile with validation.
        
        Args:
            value: The countProfile to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._countProfile = None
            return

        if not isinstance(value, NameToken):
            raise TypeError(
                f"countProfile must be NameToken or None, got {type(value).__name__}"
            )
        self._countProfile = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAccessCount(self) -> List["AccessCount"]:
        """
        AUTOSAR-compliant getter for accessCount.
        
        Returns:
            The accessCount value
        
        Note:
            Delegates to access_count property (CODING_RULE_V2_00017)
        """
        return self.access_count  # Delegates to property

    def getCountProfile(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for countProfile.
        
        Returns:
            The countProfile value
        
        Note:
            Delegates to count_profile property (CODING_RULE_V2_00017)
        """
        return self.count_profile  # Delegates to property

    def setCountProfile(self, value: "NameToken") -> "AccessCountSet":
        """
        AUTOSAR-compliant setter for countProfile with method chaining.
        
        Args:
            value: The countProfile to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to count_profile property setter (gets validation automatically)
        """
        self.count_profile = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_count_profile(self, value: Optional["NameToken"]) -> "AccessCountSet":
        """
        Set countProfile and return self for chaining.
        
        Args:
            value: The countProfile to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_count_profile("value")
        """
        self.count_profile = value  # Use property setter (gets validation)
        return self