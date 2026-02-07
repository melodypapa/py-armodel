from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class BusMirrorLinPidToCanIdMapping(ARObject):
    """
    This element defines a rule for remapping a single LIN Frame.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::BusMirror::BusMirrorLinPidToCanIdMapping
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 702, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the CanId on the targetChannel.
        self._remappedCanId: Optional["PositiveInteger"] = None

    @property
    def remapped_can_id(self) -> Optional["PositiveInteger"]:
        """Get remappedCanId (Pythonic accessor)."""
        return self._remappedCanId

    @remapped_can_id.setter
    def remapped_can_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set remappedCanId with validation.
        
        Args:
            value: The remappedCanId to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._remappedCanId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"remappedCanId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._remappedCanId = value
        # This reference points to the sourceFrame with sourceCan the sourceChannel.
        self._sourceLinPid: RefType = None

    @property
    def source_lin_pid(self) -> RefType:
        """Get sourceLinPid (Pythonic accessor)."""
        return self._sourceLinPid

    @source_lin_pid.setter
    def source_lin_pid(self, value: RefType) -> None:
        """
        Set sourceLinPid with validation.
        
        Args:
            value: The sourceLinPid to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sourceLinPid = None
            return

        self._sourceLinPid = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRemappedCanId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for remappedCanId.
        
        Returns:
            The remappedCanId value
        
        Note:
            Delegates to remapped_can_id property (CODING_RULE_V2_00017)
        """
        return self.remapped_can_id  # Delegates to property

    def setRemappedCanId(self, value: "PositiveInteger") -> "BusMirrorLinPidToCanIdMapping":
        """
        AUTOSAR-compliant setter for remappedCanId with method chaining.
        
        Args:
            value: The remappedCanId to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to remapped_can_id property setter (gets validation automatically)
        """
        self.remapped_can_id = value  # Delegates to property setter
        return self

    def getSourceLinPid(self) -> RefType:
        """
        AUTOSAR-compliant getter for sourceLinPid.
        
        Returns:
            The sourceLinPid value
        
        Note:
            Delegates to source_lin_pid property (CODING_RULE_V2_00017)
        """
        return self.source_lin_pid  # Delegates to property

    def setSourceLinPid(self, value: RefType) -> "BusMirrorLinPidToCanIdMapping":
        """
        AUTOSAR-compliant setter for sourceLinPid with method chaining.
        
        Args:
            value: The sourceLinPid to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to source_lin_pid property setter (gets validation automatically)
        """
        self.source_lin_pid = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_remapped_can_id(self, value: Optional["PositiveInteger"]) -> "BusMirrorLinPidToCanIdMapping":
        """
        Set remappedCanId and return self for chaining.
        
        Args:
            value: The remappedCanId to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_remapped_can_id("value")
        """
        self.remapped_can_id = value  # Use property setter (gets validation)
        return self

    def with_source_lin_pid(self, value: Optional[RefType]) -> "BusMirrorLinPidToCanIdMapping":
        """
        Set sourceLinPid and return self for chaining.
        
        Args:
            value: The sourceLinPid to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_source_lin_pid("value")
        """
        self.source_lin_pid = value  # Use property setter (gets validation)
        return self