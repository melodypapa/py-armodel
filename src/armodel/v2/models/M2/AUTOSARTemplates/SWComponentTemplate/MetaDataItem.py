from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class MetaDataItem(ARObject):
    """
    This meta-class represents a single meta-data item.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::MetaDataItem
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 98, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2037, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute determines the length of the MetaDataItem.
        self._length: Optional["PositiveInteger"] = None

    @property
    def length(self) -> Optional["PositiveInteger"]:
        """Get length (Pythonic accessor)."""
        return self._length

    @length.setter
    def length(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set length with validation.
        
        Args:
            value: The length to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._length = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"length must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._length = value
        # This aggregation contributes the specification of the meta-data item type.
        self._metaDataItem: Optional["TextValueSpecification"] = None

    @property
    def meta_data_item(self) -> Optional["TextValueSpecification"]:
        """Get metaDataItem (Pythonic accessor)."""
        return self._metaDataItem

    @meta_data_item.setter
    def meta_data_item(self, value: Optional["TextValueSpecification"]) -> None:
        """
        Set metaDataItem with validation.
        
        Args:
            value: The metaDataItem to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._metaDataItem = None
            return

        if not isinstance(value, TextValueSpecification):
            raise TypeError(
                f"metaDataItem must be TextValueSpecification or None, got {type(value).__name__}"
            )
        self._metaDataItem = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getLength(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for length.
        
        Returns:
            The length value
        
        Note:
            Delegates to length property (CODING_RULE_V2_00017)
        """
        return self.length  # Delegates to property

    def setLength(self, value: "PositiveInteger") -> "MetaDataItem":
        """
        AUTOSAR-compliant setter for length with method chaining.
        
        Args:
            value: The length to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to length property setter (gets validation automatically)
        """
        self.length = value  # Delegates to property setter
        return self

    def getMetaDataItem(self) -> "TextValueSpecification":
        """
        AUTOSAR-compliant getter for metaDataItem.
        
        Returns:
            The metaDataItem value
        
        Note:
            Delegates to meta_data_item property (CODING_RULE_V2_00017)
        """
        return self.meta_data_item  # Delegates to property

    def setMetaDataItem(self, value: "TextValueSpecification") -> "MetaDataItem":
        """
        AUTOSAR-compliant setter for metaDataItem with method chaining.
        
        Args:
            value: The metaDataItem to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to meta_data_item property setter (gets validation automatically)
        """
        self.meta_data_item = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_length(self, value: Optional["PositiveInteger"]) -> "MetaDataItem":
        """
        Set length and return self for chaining.
        
        Args:
            value: The length to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_length("value")
        """
        self.length = value  # Use property setter (gets validation)
        return self

    def with_meta_data_item(self, value: Optional["TextValueSpecification"]) -> "MetaDataItem":
        """
        Set metaDataItem and return self for chaining.
        
        Args:
            value: The metaDataItem to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_meta_data_item("value")
        """
        self.meta_data_item = value  # Use property setter (gets validation)
        return self