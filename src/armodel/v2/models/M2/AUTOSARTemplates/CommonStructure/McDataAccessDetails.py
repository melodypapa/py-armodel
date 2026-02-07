from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class McDataAccessDetails(ARObject):
    """
    that the SwComponentPrototype, the RunnableEntity and the
    VariableDataPrototype are implicitly given be the referred instances of
    RTEEvent and VariableAccess.
    
    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::McDataAccessDetails
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 195, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # by: RteEventInEcuInstance.
        self._rteEventRef: List["RTEEvent"] = []

    @property
    def rte_event_ref(self) -> List["RTEEvent"]:
        """Get rteEventRef (Pythonic accessor)."""
        return self._rteEventRef
        # by: VariableAccessInEcu.
        self._variableAccessInstanceRef: List["VariableAccess"] = []

    @property
    def variable_access_instance_ref(self) -> List["VariableAccess"]:
        """Get variableAccessInstanceRef (Pythonic accessor)."""
        return self._variableAccessInstanceRef

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRteEventRef(self) -> List["RTEEvent"]:
        """
        AUTOSAR-compliant getter for rteEventRef.
        
        Returns:
            The rteEventRef value
        
        Note:
            Delegates to rte_event_ref property (CODING_RULE_V2_00017)
        """
        return self.rte_event_ref  # Delegates to property

    def getVariableAccessInstanceRef(self) -> List["VariableAccess"]:
        """
        AUTOSAR-compliant getter for variableAccessInstanceRef.
        
        Returns:
            The variableAccessInstanceRef value
        
        Note:
            Delegates to variable_access_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.variable_access_instance_ref  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====