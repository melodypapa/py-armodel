from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Referrable import Referrable

class HwDescriptionEntity(Referrable, ABC):
    """
    This meta-class represents the ability to describe a hardware entity.
    
    Package: M2::AUTOSARTemplates::EcuResourceTemplate::HwDescriptionEntity
    
    Sources:
      - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (Page 15, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 990, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is HwDescriptionEntity:
            raise TypeError("HwDescriptionEntity is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This aggregation represents a particular hardware value.
        # atpVariation.
        self._hwAttribute: List["HwAttributeValue"] = []

    @property
    def hw_attribute(self) -> List["HwAttributeValue"]:
        """Get hwAttribute (Pythonic accessor)."""
        return self._hwAttribute
        # One of the associations representing one particular the hardware entity.
        self._hwCategory: List["HwCategory"] = []

    @property
    def hw_category(self) -> List["HwCategory"]:
        """Get hwCategory (Pythonic accessor)."""
        return self._hwCategory
        # This association is used to assign an optional HwType the common attribute
                # values for all this HwDescriptionEntity.
        # Note that Hw not be redefined and therefore shall not have a.
        self._hwType: Optional["HwType"] = None

    @property
    def hw_type(self) -> Optional["HwType"]:
        """Get hwType (Pythonic accessor)."""
        return self._hwType

    @hw_type.setter
    def hw_type(self, value: Optional["HwType"]) -> None:
        """
        Set hwType with validation.
        
        Args:
            value: The hwType to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._hwType = None
            return

        if not isinstance(value, HwType):
            raise TypeError(
                f"hwType must be HwType or None, got {type(value).__name__}"
            )
        self._hwType = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getHwAttribute(self) -> List["HwAttributeValue"]:
        """
        AUTOSAR-compliant getter for hwAttribute.
        
        Returns:
            The hwAttribute value
        
        Note:
            Delegates to hw_attribute property (CODING_RULE_V2_00017)
        """
        return self.hw_attribute  # Delegates to property

    def getHwCategory(self) -> List["HwCategory"]:
        """
        AUTOSAR-compliant getter for hwCategory.
        
        Returns:
            The hwCategory value
        
        Note:
            Delegates to hw_category property (CODING_RULE_V2_00017)
        """
        return self.hw_category  # Delegates to property

    def getHwType(self) -> "HwType":
        """
        AUTOSAR-compliant getter for hwType.
        
        Returns:
            The hwType value
        
        Note:
            Delegates to hw_type property (CODING_RULE_V2_00017)
        """
        return self.hw_type  # Delegates to property

    def setHwType(self, value: "HwType") -> "HwDescriptionEntity":
        """
        AUTOSAR-compliant setter for hwType with method chaining.
        
        Args:
            value: The hwType to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to hw_type property setter (gets validation automatically)
        """
        self.hw_type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_hw_type(self, value: Optional["HwType"]) -> "HwDescriptionEntity":
        """
        Set hwType and return self for chaining.
        
        Args:
            value: The hwType to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_hw_type("value")
        """
        self.hw_type = value  # Use property setter (gets validation)
        return self