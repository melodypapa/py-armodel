from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class SwcBswSynchronizedModeGroupPrototype(ARObject):
    """
    Synchronizes a mode group provided by a component via a port with a mode
    group provided by a BSW module or cluster.
    
    Package: M2::AUTOSARTemplates::CommonStructure::SwcBswMapping::SwcBswSynchronizedModeGroupPrototype
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 111, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The BSW mode group prototype.
        self._bswModeGroupPrototype: RefType = None

    @property
    def bsw_mode_group_prototype(self) -> RefType:
        """Get bswModeGroupPrototype (Pythonic accessor)."""
        return self._bswModeGroupPrototype

    @bsw_mode_group_prototype.setter
    def bsw_mode_group_prototype(self, value: RefType) -> None:
        """
        Set bswModeGroupPrototype with validation.
        
        Args:
            value: The bswModeGroupPrototype to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bswModeGroupPrototype = None
            return

        self._bswModeGroupPrototype = value
        # by: PModeGroupInAtomic.
        self._swcModeGroupSwcInstanceRef: RefType = None

    @property
    def swc_mode_group_swc_instance_ref(self) -> RefType:
        """Get swcModeGroupSwcInstanceRef (Pythonic accessor)."""
        return self._swcModeGroupSwcInstanceRef

    @swc_mode_group_swc_instance_ref.setter
    def swc_mode_group_swc_instance_ref(self, value: RefType) -> None:
        """
        Set swcModeGroupSwcInstanceRef with validation.
        
        Args:
            value: The swcModeGroupSwcInstanceRef to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swcModeGroupSwcInstanceRef = None
            return

        self._swcModeGroupSwcInstanceRef = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBswModeGroupPrototype(self) -> RefType:
        """
        AUTOSAR-compliant getter for bswModeGroupPrototype.
        
        Returns:
            The bswModeGroupPrototype value
        
        Note:
            Delegates to bsw_mode_group_prototype property (CODING_RULE_V2_00017)
        """
        return self.bsw_mode_group_prototype  # Delegates to property

    def setBswModeGroupPrototype(self, value: RefType) -> "SwcBswSynchronizedModeGroupPrototype":
        """
        AUTOSAR-compliant setter for bswModeGroupPrototype with method chaining.
        
        Args:
            value: The bswModeGroupPrototype to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to bsw_mode_group_prototype property setter (gets validation automatically)
        """
        self.bsw_mode_group_prototype = value  # Delegates to property setter
        return self

    def getSwcModeGroupSwcInstanceRef(self) -> RefType:
        """
        AUTOSAR-compliant getter for swcModeGroupSwcInstanceRef.
        
        Returns:
            The swcModeGroupSwcInstanceRef value
        
        Note:
            Delegates to swc_mode_group_swc_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.swc_mode_group_swc_instance_ref  # Delegates to property

    def setSwcModeGroupSwcInstanceRef(self, value: RefType) -> "SwcBswSynchronizedModeGroupPrototype":
        """
        AUTOSAR-compliant setter for swcModeGroupSwcInstanceRef with method chaining.
        
        Args:
            value: The swcModeGroupSwcInstanceRef to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to swc_mode_group_swc_instance_ref property setter (gets validation automatically)
        """
        self.swc_mode_group_swc_instance_ref = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bsw_mode_group_prototype(self, value: Optional[RefType]) -> "SwcBswSynchronizedModeGroupPrototype":
        """
        Set bswModeGroupPrototype and return self for chaining.
        
        Args:
            value: The bswModeGroupPrototype to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_bsw_mode_group_prototype("value")
        """
        self.bsw_mode_group_prototype = value  # Use property setter (gets validation)
        return self

    def with_swc_mode_group_swc_instance_ref(self, value: Optional[RefType]) -> "SwcBswSynchronizedModeGroupPrototype":
        """
        Set swcModeGroupSwcInstanceRef and return self for chaining.
        
        Args:
            value: The swcModeGroupSwcInstanceRef to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_swc_mode_group_swc_instance_ref("value")
        """
        self.swc_mode_group_swc_instance_ref = value  # Use property setter (gets validation)
        return self