from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class SwcBswSynchronizedTrigger(ARObject):
    """
    Synchronizes a Trigger provided by a component via a port with a Trigger
    provided by a BSW module or cluster.
    
    Package: M2::AUTOSARTemplates::CommonStructure::SwcBswMapping::SwcBswSynchronizedTrigger
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 111, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The BSW Trigger.
        self._bswTrigger: RefType = None

    @property
    def bsw_trigger(self) -> RefType:
        """Get bswTrigger (Pythonic accessor)."""
        return self._bswTrigger

    @bsw_trigger.setter
    def bsw_trigger(self, value: RefType) -> None:
        """
        Set bswTrigger with validation.
        
        Args:
            value: The bswTrigger to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bswTrigger = None
            return

        self._bswTrigger = value
        # by: PTriggerInAtomicSwc.
        self._swcTriggerTypeInstanceRef: RefType = None

    @property
    def swc_trigger_type_instance_ref(self) -> RefType:
        """Get swcTriggerTypeInstanceRef (Pythonic accessor)."""
        return self._swcTriggerTypeInstanceRef

    @swc_trigger_type_instance_ref.setter
    def swc_trigger_type_instance_ref(self, value: RefType) -> None:
        """
        Set swcTriggerTypeInstanceRef with validation.
        
        Args:
            value: The swcTriggerTypeInstanceRef to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swcTriggerTypeInstanceRef = None
            return

        self._swcTriggerTypeInstanceRef = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBswTrigger(self) -> RefType:
        """
        AUTOSAR-compliant getter for bswTrigger.
        
        Returns:
            The bswTrigger value
        
        Note:
            Delegates to bsw_trigger property (CODING_RULE_V2_00017)
        """
        return self.bsw_trigger  # Delegates to property

    def setBswTrigger(self, value: RefType) -> "SwcBswSynchronizedTrigger":
        """
        AUTOSAR-compliant setter for bswTrigger with method chaining.
        
        Args:
            value: The bswTrigger to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to bsw_trigger property setter (gets validation automatically)
        """
        self.bsw_trigger = value  # Delegates to property setter
        return self

    def getSwcTriggerTypeInstanceRef(self) -> RefType:
        """
        AUTOSAR-compliant getter for swcTriggerTypeInstanceRef.
        
        Returns:
            The swcTriggerTypeInstanceRef value
        
        Note:
            Delegates to swc_trigger_type_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.swc_trigger_type_instance_ref  # Delegates to property

    def setSwcTriggerTypeInstanceRef(self, value: RefType) -> "SwcBswSynchronizedTrigger":
        """
        AUTOSAR-compliant setter for swcTriggerTypeInstanceRef with method chaining.
        
        Args:
            value: The swcTriggerTypeInstanceRef to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to swc_trigger_type_instance_ref property setter (gets validation automatically)
        """
        self.swc_trigger_type_instance_ref = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bsw_trigger(self, value: Optional[RefType]) -> "SwcBswSynchronizedTrigger":
        """
        Set bswTrigger and return self for chaining.
        
        Args:
            value: The bswTrigger to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_bsw_trigger("value")
        """
        self.bsw_trigger = value  # Use property setter (gets validation)
        return self

    def with_swc_trigger_type_instance_ref(self, value: Optional[RefType]) -> "SwcBswSynchronizedTrigger":
        """
        Set swcTriggerTypeInstanceRef and return self for chaining.
        
        Args:
            value: The swcTriggerTypeInstanceRef to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_swc_trigger_type_instance_ref("value")
        """
        self.swc_trigger_type_instance_ref = value  # Use property setter (gets validation)
        return self