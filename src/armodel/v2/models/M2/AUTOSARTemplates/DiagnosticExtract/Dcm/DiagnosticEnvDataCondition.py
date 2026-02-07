from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class DiagnosticEnvDataCondition(DiagnosticEnvCompareCondition):
    """
    A DiagnosticEnvDataCondition is an atomic condition that compares the
    current value of the referenced DiagnosticDataElement with a constant value
    defined by the ValueSpecification. All compareTypes are supported.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::EnvironmentalCondition::DiagnosticEnvDataCondition
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 84, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represents a fixed compare value taken to compare condition.
        self._compareValue: Optional["ValueSpecification"] = None

    @property
    def compare_value(self) -> Optional["ValueSpecification"]:
        """Get compareValue (Pythonic accessor)."""
        return self._compareValue

    @compare_value.setter
    def compare_value(self, value: Optional["ValueSpecification"]) -> None:
        """
        Set compareValue with validation.
        
        Args:
            value: The compareValue to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._compareValue = None
            return

        if not isinstance(value, ValueSpecification):
            raise TypeError(
                f"compareValue must be ValueSpecification or None, got {type(value).__name__}"
            )
        self._compareValue = value
        # This reference represents the related diagnostic data.
        self._dataElement: Optional["DiagnosticDataElement"] = None

    @property
    def data_element(self) -> Optional["DiagnosticDataElement"]:
        """Get dataElement (Pythonic accessor)."""
        return self._dataElement

    @data_element.setter
    def data_element(self, value: Optional["DiagnosticDataElement"]) -> None:
        """
        Set dataElement with validation.
        
        Args:
            value: The dataElement to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataElement = None
            return

        if not isinstance(value, DiagnosticDataElement):
            raise TypeError(
                f"dataElement must be DiagnosticDataElement or None, got {type(value).__name__}"
            )
        self._dataElement = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCompareValue(self) -> "ValueSpecification":
        """
        AUTOSAR-compliant getter for compareValue.
        
        Returns:
            The compareValue value
        
        Note:
            Delegates to compare_value property (CODING_RULE_V2_00017)
        """
        return self.compare_value  # Delegates to property

    def setCompareValue(self, value: "ValueSpecification") -> "DiagnosticEnvDataCondition":
        """
        AUTOSAR-compliant setter for compareValue with method chaining.
        
        Args:
            value: The compareValue to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to compare_value property setter (gets validation automatically)
        """
        self.compare_value = value  # Delegates to property setter
        return self

    def getDataElement(self) -> "DiagnosticDataElement":
        """
        AUTOSAR-compliant getter for dataElement.
        
        Returns:
            The dataElement value
        
        Note:
            Delegates to data_element property (CODING_RULE_V2_00017)
        """
        return self.data_element  # Delegates to property

    def setDataElement(self, value: "DiagnosticDataElement") -> "DiagnosticEnvDataCondition":
        """
        AUTOSAR-compliant setter for dataElement with method chaining.
        
        Args:
            value: The dataElement to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to data_element property setter (gets validation automatically)
        """
        self.data_element = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_compare_value(self, value: Optional["ValueSpecification"]) -> "DiagnosticEnvDataCondition":
        """
        Set compareValue and return self for chaining.
        
        Args:
            value: The compareValue to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_compare_value("value")
        """
        self.compare_value = value  # Use property setter (gets validation)
        return self

    def with_data_element(self, value: Optional["DiagnosticDataElement"]) -> "DiagnosticEnvDataCondition":
        """
        Set dataElement and return self for chaining.
        
        Args:
            value: The dataElement to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_data_element("value")
        """
        self.data_element = value  # Use property setter (gets validation)
        return self