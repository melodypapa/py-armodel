from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class BusMirrorCanIdToCanIdMapping(ARObject):
    """
    This element defines a rule for remapping a single CAN ID.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::BusMirror::BusMirrorCanIdToCanIdMapping
    
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
        self._souceCanId: RefType = None

    @property
    def souce_can_id(self) -> RefType:
        """Get souceCanId (Pythonic accessor)."""
        return self._souceCanId

    @souce_can_id.setter
    def souce_can_id(self, value: RefType) -> None:
        """
        Set souceCanId with validation.
        
        Args:
            value: The souceCanId to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._souceCanId = None
            return

        self._souceCanId = value

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

    def setRemappedCanId(self, value: "PositiveInteger") -> "BusMirrorCanIdToCanIdMapping":
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

    def getSouceCanId(self) -> RefType:
        """
        AUTOSAR-compliant getter for souceCanId.
        
        Returns:
            The souceCanId value
        
        Note:
            Delegates to souce_can_id property (CODING_RULE_V2_00017)
        """
        return self.souce_can_id  # Delegates to property

    def setSouceCanId(self, value: RefType) -> "BusMirrorCanIdToCanIdMapping":
        """
        AUTOSAR-compliant setter for souceCanId with method chaining.
        
        Args:
            value: The souceCanId to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to souce_can_id property setter (gets validation automatically)
        """
        self.souce_can_id = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_remapped_can_id(self, value: Optional["PositiveInteger"]) -> "BusMirrorCanIdToCanIdMapping":
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

    def with_souce_can_id(self, value: Optional[RefType]) -> "BusMirrorCanIdToCanIdMapping":
        """
        Set souceCanId and return self for chaining.
        
        Args:
            value: The souceCanId to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_souce_can_id("value")
        """
        self.souce_can_id = value  # Use property setter (gets validation)
        return self