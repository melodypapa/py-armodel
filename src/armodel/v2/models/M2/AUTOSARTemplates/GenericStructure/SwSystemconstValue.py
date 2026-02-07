from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class SwSystemconstValue(ARObject):
    """
    This meta-class assigns a particular value to a system constant.
    
    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::SwSystemconstValue
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2068, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 80, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 235, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This provides the ability to add information why the value like it is.
        self._annotation: List["Annotation"] = []

    @property
    def annotation(self) -> List["Annotation"]:
        """Get annotation (Pythonic accessor)."""
        return self._annotation
        # This is the system constant to which the value applies.
        self._swSystemconst: "SwSystemconst" = None

    @property
    def sw_systemconst(self) -> "SwSystemconst":
        """Get swSystemconst (Pythonic accessor)."""
        return self._swSystemconst

    @sw_systemconst.setter
    def sw_systemconst(self, value: "SwSystemconst") -> None:
        """
        Set swSystemconst with validation.
        
        Args:
            value: The swSystemconst to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, SwSystemconst):
            raise TypeError(
                f"swSystemconst must be SwSystemconst, got {type(value).__name__}"
            )
        self._swSystemconst = value
        # This is the particular value of a system constant.
        # It is Numerical.
        # Further restrictions may apply by of the system constant.
        # attribute defines the internal value of the Sw it is processed in the Formula
                # Language.
        self._value: "Numerical" = None

    @property
    def value(self) -> "Numerical":
        """Get value (Pythonic accessor)."""
        return self._value

    @value.setter
    def value(self, value: "Numerical") -> None:
        """
        Set value with validation.
        
        Args:
            value: The value to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, Numerical):
            raise TypeError(
                f"value must be Numerical, got {type(value).__name__}"
            )
        self._value = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAnnotation(self) -> List["Annotation"]:
        """
        AUTOSAR-compliant getter for annotation.
        
        Returns:
            The annotation value
        
        Note:
            Delegates to annotation property (CODING_RULE_V2_00017)
        """
        return self.annotation  # Delegates to property

    def getSwSystemconst(self) -> "SwSystemconst":
        """
        AUTOSAR-compliant getter for swSystemconst.
        
        Returns:
            The swSystemconst value
        
        Note:
            Delegates to sw_systemconst property (CODING_RULE_V2_00017)
        """
        return self.sw_systemconst  # Delegates to property

    def setSwSystemconst(self, value: "SwSystemconst") -> "SwSystemconstValue":
        """
        AUTOSAR-compliant setter for swSystemconst with method chaining.
        
        Args:
            value: The swSystemconst to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sw_systemconst property setter (gets validation automatically)
        """
        self.sw_systemconst = value  # Delegates to property setter
        return self

    def getValue(self) -> "Numerical":
        """
        AUTOSAR-compliant getter for value.
        
        Returns:
            The value value
        
        Note:
            Delegates to value property (CODING_RULE_V2_00017)
        """
        return self.value  # Delegates to property

    def setValue(self, value: "Numerical") -> "SwSystemconstValue":
        """
        AUTOSAR-compliant setter for value with method chaining.
        
        Args:
            value: The value to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to value property setter (gets validation automatically)
        """
        self.value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sw_systemconst(self, value: "SwSystemconst") -> "SwSystemconstValue":
        """
        Set swSystemconst and return self for chaining.
        
        Args:
            value: The swSystemconst to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sw_systemconst("value")
        """
        self.sw_systemconst = value  # Use property setter (gets validation)
        return self

    def with_value(self, value: "Numerical") -> "SwSystemconstValue":
        """
        Set value and return self for chaining.
        
        Args:
            value: The value to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_value("value")
        """
        self.value = value  # Use property setter (gets validation)
        return self