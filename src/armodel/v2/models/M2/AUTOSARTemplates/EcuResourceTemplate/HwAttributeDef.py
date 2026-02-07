from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class HwAttributeDef(Identifiable):
    """
    This metaclass represents the ability to define a particular hardware
    attribute. The category of this element defines the type of the
    attributeValue. If the category is Enumeration the hw
    AttributeEnumerationLiterals specify the available literals.
    
    Package: M2::AUTOSARTemplates::EcuResourceTemplate::HwElementCategory::HwAttributeDef
    
    Sources:
      - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (Page 26, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The available EnumerationLiterals of the Enumeration Only applicable if the
        # category of the Hw Enumeration.
        self._hwAttribute: List["HwAttributeLiteralDef"] = []

    @property
    def hw_attribute(self) -> List["HwAttributeLiteralDef"]:
        """Get hwAttribute (Pythonic accessor)."""
        return self._hwAttribute
        # This attribute specifies if the defined attribute value is be provided.
        self._isRequired: Optional["Boolean"] = None

    @property
    def is_required(self) -> Optional["Boolean"]:
        """Get isRequired (Pythonic accessor)."""
        return self._isRequired

    @is_required.setter
    def is_required(self, value: Optional["Boolean"]) -> None:
        """
        Set isRequired with validation.
        
        Args:
            value: The isRequired to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._isRequired = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"isRequired must be Boolean or None, got {type(value).__name__}"
            )
        self._isRequired = value
        # This association specifies the physical unit of the defined This is optional
        # due to the fact that textual attributes.
        self._unit: Optional["Unit"] = None

    @property
    def unit(self) -> Optional["Unit"]:
        """Get unit (Pythonic accessor)."""
        return self._unit

    @unit.setter
    def unit(self, value: Optional["Unit"]) -> None:
        """
        Set unit with validation.
        
        Args:
            value: The unit to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._unit = None
            return

        if not isinstance(value, Unit):
            raise TypeError(
                f"unit must be Unit or None, got {type(value).__name__}"
            )
        self._unit = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getHwAttribute(self) -> List["HwAttributeLiteralDef"]:
        """
        AUTOSAR-compliant getter for hwAttribute.
        
        Returns:
            The hwAttribute value
        
        Note:
            Delegates to hw_attribute property (CODING_RULE_V2_00017)
        """
        return self.hw_attribute  # Delegates to property

    def getIsRequired(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for isRequired.
        
        Returns:
            The isRequired value
        
        Note:
            Delegates to is_required property (CODING_RULE_V2_00017)
        """
        return self.is_required  # Delegates to property

    def setIsRequired(self, value: "Boolean") -> "HwAttributeDef":
        """
        AUTOSAR-compliant setter for isRequired with method chaining.
        
        Args:
            value: The isRequired to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to is_required property setter (gets validation automatically)
        """
        self.is_required = value  # Delegates to property setter
        return self

    def getUnit(self) -> "Unit":
        """
        AUTOSAR-compliant getter for unit.
        
        Returns:
            The unit value
        
        Note:
            Delegates to unit property (CODING_RULE_V2_00017)
        """
        return self.unit  # Delegates to property

    def setUnit(self, value: "Unit") -> "HwAttributeDef":
        """
        AUTOSAR-compliant setter for unit with method chaining.
        
        Args:
            value: The unit to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to unit property setter (gets validation automatically)
        """
        self.unit = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_is_required(self, value: Optional["Boolean"]) -> "HwAttributeDef":
        """
        Set isRequired and return self for chaining.
        
        Args:
            value: The isRequired to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_is_required("value")
        """
        self.is_required = value  # Use property setter (gets validation)
        return self

    def with_unit(self, value: Optional["Unit"]) -> "HwAttributeDef":
        """
        Set unit and return self for chaining.
        
        Args:
            value: The unit to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_unit("value")
        """
        self.unit = value  # Use property setter (gets validation)
        return self