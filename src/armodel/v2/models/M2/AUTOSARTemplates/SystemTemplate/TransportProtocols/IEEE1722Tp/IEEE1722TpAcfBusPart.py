from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class IEEE1722TpAcfBusPart(Identifiable, ABC):
    """
    Definition of one IEEE1722Tp ACF part transported over the IEEE1722Tp
    channel.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp::IEEE1722TpAcf::IEEE1722TpAcfBusPart
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 657, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is IEEE1722TpAcfBusPart:
            raise TypeError("IEEE1722TpAcfBusPart is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines whether putting this AcfPart to the IEEE1722Tp message triggers
        # immediate sending of the message.
        self._collectionTrigger: RefType = None

    @property
    def collection_trigger(self) -> RefType:
        """Get collectionTrigger (Pythonic accessor)."""
        return self._collectionTrigger

    @collection_trigger.setter
    def collection_trigger(self, value: RefType) -> None:
        """
        Set collectionTrigger with validation.
        
        Args:
            value: The collectionTrigger to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._collectionTrigger = None
            return

        self._collectionTrigger = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCollectionTrigger(self) -> RefType:
        """
        AUTOSAR-compliant getter for collectionTrigger.
        
        Returns:
            The collectionTrigger value
        
        Note:
            Delegates to collection_trigger property (CODING_RULE_V2_00017)
        """
        return self.collection_trigger  # Delegates to property

    def setCollectionTrigger(self, value: RefType) -> "IEEE1722TpAcfBusPart":
        """
        AUTOSAR-compliant setter for collectionTrigger with method chaining.
        
        Args:
            value: The collectionTrigger to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to collection_trigger property setter (gets validation automatically)
        """
        self.collection_trigger = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_collection_trigger(self, value: Optional[RefType]) -> "IEEE1722TpAcfBusPart":
        """
        Set collectionTrigger and return self for chaining.
        
        Args:
            value: The collectionTrigger to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_collection_trigger("value")
        """
        self.collection_trigger = value  # Use property setter (gets validation)
        return self