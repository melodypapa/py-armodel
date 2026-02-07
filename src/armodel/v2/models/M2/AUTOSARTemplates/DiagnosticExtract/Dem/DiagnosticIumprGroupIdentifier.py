from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class DiagnosticIumprGroupIdentifier(ARObject):
    """
    This meta-class provides the ability to the define the group identifier for
    an IumprGroup.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticEvent::DiagnosticIumprGroupIdentifier
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 211, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute shall be taken to define an identifier for the Please note
        # that the value of this identifier by regulations outside the scope of AUTOSAR
        # therefore not be limited to the set of characters a shortName.
        self._groupId: Optional["NameToken"] = None

    @property
    def group_id(self) -> Optional["NameToken"]:
        """Get groupId (Pythonic accessor)."""
        return self._groupId

    @group_id.setter
    def group_id(self, value: Optional["NameToken"]) -> None:
        """
        Set groupId with validation.
        
        Args:
            value: The groupId to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._groupId = None
            return

        if not isinstance(value, NameToken):
            raise TypeError(
                f"groupId must be NameToken or None, got {type(value).__name__}"
            )
        self._groupId = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getGroupId(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for groupId.
        
        Returns:
            The groupId value
        
        Note:
            Delegates to group_id property (CODING_RULE_V2_00017)
        """
        return self.group_id  # Delegates to property

    def setGroupId(self, value: "NameToken") -> "DiagnosticIumprGroupIdentifier":
        """
        AUTOSAR-compliant setter for groupId with method chaining.
        
        Args:
            value: The groupId to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to group_id property setter (gets validation automatically)
        """
        self.group_id = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_group_id(self, value: Optional["NameToken"]) -> "DiagnosticIumprGroupIdentifier":
        """
        Set groupId and return self for chaining.
        
        Args:
            value: The groupId to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_group_id("value")
        """
        self.group_id = value  # Use property setter (gets validation)
        return self