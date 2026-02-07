from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class ApplicationRuleBasedValueSpecification(CompositeRuleBasedValueArgument):
    """
    This meta-class represents rule based values for DataPrototypes typed by
    ApplicationDataTypes (ApplicationArrayDataType or a compound
    ApplicationPrimitiveDataType which also boils down to an array-nature).
    
    Package: M2::AUTOSARTemplates::CommonStructure::Constants::ApplicationRuleBasedValueSpecification
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 302, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 462, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the category of the RuleBasedValue.
        self._category: Optional["Identifier"] = None

    @property
    def category(self) -> Optional["Identifier"]:
        """Get category (Pythonic accessor)."""
        return self._category

    @category.setter
    def category(self, value: Optional["Identifier"]) -> None:
        """
        Set category with validation.
        
        Args:
            value: The category to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._category = None
            return

        if not isinstance(value, Identifier):
            raise TypeError(
                f"category must be Identifier or None, got {type(value).__name__}"
            )
        self._category = value
        # This represents the axis values of a Compound Primitive Type (curve or map).
        # swAxisCont describes the x-axis, the second sw the y-axis, the third
                # swAxisCont z-axis.
        # In addition to this, the axis can be swAxisIndex.
        self._swAxisCont: List["RuleBasedAxisCont"] = []

    @property
    def sw_axis_cont(self) -> List["RuleBasedAxisCont"]:
        """Get swAxisCont (Pythonic accessor)."""
        return self._swAxisCont
        # This represents the values of an array or Compound.
        self._swValueCont: Optional["RuleBasedValueCont"] = None

    @property
    def sw_value_cont(self) -> Optional["RuleBasedValueCont"]:
        """Get swValueCont (Pythonic accessor)."""
        return self._swValueCont

    @sw_value_cont.setter
    def sw_value_cont(self, value: Optional["RuleBasedValueCont"]) -> None:
        """
        Set swValueCont with validation.
        
        Args:
            value: The swValueCont to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swValueCont = None
            return

        if not isinstance(value, RuleBasedValueCont):
            raise TypeError(
                f"swValueCont must be RuleBasedValueCont or None, got {type(value).__name__}"
            )
        self._swValueCont = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCategory(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for category.
        
        Returns:
            The category value
        
        Note:
            Delegates to category property (CODING_RULE_V2_00017)
        """
        return self.category  # Delegates to property

    def setCategory(self, value: "Identifier") -> "ApplicationRuleBasedValueSpecification":
        """
        AUTOSAR-compliant setter for category with method chaining.
        
        Args:
            value: The category to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to category property setter (gets validation automatically)
        """
        self.category = value  # Delegates to property setter
        return self

    def getSwAxisCont(self) -> List["RuleBasedAxisCont"]:
        """
        AUTOSAR-compliant getter for swAxisCont.
        
        Returns:
            The swAxisCont value
        
        Note:
            Delegates to sw_axis_cont property (CODING_RULE_V2_00017)
        """
        return self.sw_axis_cont  # Delegates to property

    def getSwValueCont(self) -> "RuleBasedValueCont":
        """
        AUTOSAR-compliant getter for swValueCont.
        
        Returns:
            The swValueCont value
        
        Note:
            Delegates to sw_value_cont property (CODING_RULE_V2_00017)
        """
        return self.sw_value_cont  # Delegates to property

    def setSwValueCont(self, value: "RuleBasedValueCont") -> "ApplicationRuleBasedValueSpecification":
        """
        AUTOSAR-compliant setter for swValueCont with method chaining.
        
        Args:
            value: The swValueCont to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sw_value_cont property setter (gets validation automatically)
        """
        self.sw_value_cont = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_category(self, value: Optional["Identifier"]) -> "ApplicationRuleBasedValueSpecification":
        """
        Set category and return self for chaining.
        
        Args:
            value: The category to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_category("value")
        """
        self.category = value  # Use property setter (gets validation)
        return self

    def with_sw_value_cont(self, value: Optional["RuleBasedValueCont"]) -> "ApplicationRuleBasedValueSpecification":
        """
        Set swValueCont and return self for chaining.
        
        Args:
            value: The swValueCont to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sw_value_cont("value")
        """
        self.sw_value_cont = value  # Use property setter (gets validation)
        return self