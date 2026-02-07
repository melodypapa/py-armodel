from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class TimingExtensionResource(Identifiable):
    """
    A TimingExtensionResource provides the capability to contain instance
    references referred from within a timing condition formula.
    
    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingCondition::TimingExtensionResource
    
    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 35, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This refers to an instance reference of an argument of an call.
        # atpVariation 277 Document ID 411: AUTOSAR_CP_TPS_TimingExtensions Timing
                # Extensions for Classic R23-11.
        self._timingArgument: List["AutosarOperation"] = []

    @property
    def timing_argument(self) -> List["AutosarOperation"]:
        """Get timingArgument (Pythonic accessor)."""
        return self._timingArgument
        # This refers to an instance reference of a mode atpVariation.
        self._timingMode: List["TimingModeInstance"] = []

    @property
    def timing_mode(self) -> List["TimingModeInstance"]:
        """Get timingMode (Pythonic accessor)."""
        return self._timingMode
        # This refers to an instance reference of a variable.
        # atpSplitable; atpVariation.
        self._timingVariable: List["AutosarVariable"] = []

    @property
    def timing_variable(self) -> List["AutosarVariable"]:
        """Get timingVariable (Pythonic accessor)."""
        return self._timingVariable

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTimingArgument(self) -> List["AutosarOperation"]:
        """
        AUTOSAR-compliant getter for timingArgument.
        
        Returns:
            The timingArgument value
        
        Note:
            Delegates to timing_argument property (CODING_RULE_V2_00017)
        """
        return self.timing_argument  # Delegates to property

    def getTimingMode(self) -> List["TimingModeInstance"]:
        """
        AUTOSAR-compliant getter for timingMode.
        
        Returns:
            The timingMode value
        
        Note:
            Delegates to timing_mode property (CODING_RULE_V2_00017)
        """
        return self.timing_mode  # Delegates to property

    def getTimingVariable(self) -> List["AutosarVariable"]:
        """
        AUTOSAR-compliant getter for timingVariable.
        
        Returns:
            The timingVariable value
        
        Note:
            Delegates to timing_variable property (CODING_RULE_V2_00017)
        """
        return self.timing_variable  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====