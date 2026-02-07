from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class AbstractEnumerationValueVariationPoint(ARObject, ABC):
    """
    This is an abstract EnumerationValueVariationPoint. It is introduced to
    support the case that additional attributes are required for particular
    purposes.
    
    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::AttributeValueVariationPoints::AbstractEnumerationValueVariationPoint
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 421, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is AbstractEnumerationValueVariationPoint:
            raise TypeError("AbstractEnumerationValueVariationPoint is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute reflects the base to be used in context of this reference.
        self._base: Optional["Identifier"] = None

    @property
    def base(self) -> Optional["Identifier"]:
        """Get base (Pythonic accessor)."""
        return self._base

    @base.setter
    def base(self, value: Optional["Identifier"]) -> None:
        """
        Set base with validation.
        
        Args:
            value: The base to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._base = None
            return

        if not isinstance(value, Identifier):
            raise TypeError(
                f"base must be Identifier or None, got {type(value).__name__}"
            )
        self._base = value
        # This represents the assigned enumeration table.
        self._enumTable: RefType = None

    @property
    def enum_table(self) -> RefType:
        """Get enumTable (Pythonic accessor)."""
        return self._enumTable

    @enum_table.setter
    def enum_table(self, value: RefType) -> None:
        """
        Set enumTable with validation.
        
        Args:
            value: The enumTable to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._enumTable = None
            return

        self._enumTable = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBase(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for base.
        
        Returns:
            The base value
        
        Note:
            Delegates to base property (CODING_RULE_V2_00017)
        """
        return self.base  # Delegates to property

    def setBase(self, value: "Identifier") -> "AbstractEnumerationValueVariationPoint":
        """
        AUTOSAR-compliant setter for base with method chaining.
        
        Args:
            value: The base to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to base property setter (gets validation automatically)
        """
        self.base = value  # Delegates to property setter
        return self

    def getEnumTable(self) -> RefType:
        """
        AUTOSAR-compliant getter for enumTable.
        
        Returns:
            The enumTable value
        
        Note:
            Delegates to enum_table property (CODING_RULE_V2_00017)
        """
        return self.enum_table  # Delegates to property

    def setEnumTable(self, value: RefType) -> "AbstractEnumerationValueVariationPoint":
        """
        AUTOSAR-compliant setter for enumTable with method chaining.
        
        Args:
            value: The enumTable to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to enum_table property setter (gets validation automatically)
        """
        self.enum_table = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_base(self, value: Optional["Identifier"]) -> "AbstractEnumerationValueVariationPoint":
        """
        Set base and return self for chaining.
        
        Args:
            value: The base to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_base("value")
        """
        self.base = value  # Use property setter (gets validation)
        return self

    def with_enum_table(self, value: Optional[RefType]) -> "AbstractEnumerationValueVariationPoint":
        """
        Set enumTable and return self for chaining.
        
        Args:
            value: The enumTable to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_enum_table("value")
        """
        self.enum_table = value  # Use property setter (gets validation)
        return self