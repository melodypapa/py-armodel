"""
AUTOSAR Package - DiagnosticConditionGroup

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticConditionGroup
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import (
    DiagnosticCommonElement,
)




class DiagnosticConditionGroup(DiagnosticCommonElement, ABC):
    """
    Abstract element for StorageConditionGroups and EnableConditionGroups.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticConditionGroup::DiagnosticConditionGroup
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 200, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is DiagnosticConditionGroup:
            raise TypeError("DiagnosticConditionGroup is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagnosticEnableConditionGroup(DiagnosticConditionGroup):
    """
    Enable condition group which includes one or several enable conditions.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticConditionGroup::DiagnosticEnableConditionGroup
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 200, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to enableConditions that are part of the Enable atpVariation.
        self._enableCondition: List["DiagnosticEnable"] = []

    @property
    def enable_condition(self) -> List["DiagnosticEnable"]:
        """Get enableCondition (Pythonic accessor)."""
        return self._enableCondition

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEnableCondition(self) -> List["DiagnosticEnable"]:
        """
        AUTOSAR-compliant getter for enableCondition.
        
        Returns:
            The enableCondition value
        
        Note:
            Delegates to enable_condition property (CODING_RULE_V2_00017)
        """
        return self.enable_condition  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagnosticStorageConditionGroup(DiagnosticConditionGroup):
    """
    Storage condition group which includes one or several storage conditions.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticConditionGroup::DiagnosticStorageConditionGroup
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 200, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to storageConditions that are part of the StorageConditionGroup.
        # atpVariation.
        self._storage: List["DiagnosticStorage"] = []

    @property
    def storage(self) -> List["DiagnosticStorage"]:
        """Get storage (Pythonic accessor)."""
        return self._storage

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getStorage(self) -> List["DiagnosticStorage"]:
        """
        AUTOSAR-compliant getter for storage.
        
        Returns:
            The storage value
        
        Note:
            Delegates to storage property (CODING_RULE_V2_00017)
        """
        return self.storage  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====