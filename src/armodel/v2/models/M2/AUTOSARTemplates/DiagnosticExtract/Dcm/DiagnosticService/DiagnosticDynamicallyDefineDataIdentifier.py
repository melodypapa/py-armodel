from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class DiagnosticDynamicallyDefineDataIdentifier(DiagnosticServiceInstance):
    """
    This represents an instance of the "Dynamically Define Data Identifier"
    diagnostic service.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::DynamicallyDefineDataIdentifier::DiagnosticDynamicallyDefineDataIdentifier
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 127, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the applicable DiagnosticDynamicData.
        self._dataIdentifier: Optional["DiagnosticDynamicData"] = None

    @property
    def data_identifier(self) -> Optional["DiagnosticDynamicData"]:
        """Get dataIdentifier (Pythonic accessor)."""
        return self._dataIdentifier

    @data_identifier.setter
    def data_identifier(self, value: Optional["DiagnosticDynamicData"]) -> None:
        """
        Set dataIdentifier with validation.
        
        Args:
            value: The dataIdentifier to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataIdentifier = None
            return

        if not isinstance(value, DiagnosticDynamicData):
            raise TypeError(
                f"dataIdentifier must be DiagnosticDynamicData or None, got {type(value).__name__}"
            )
        self._dataIdentifier = value
        # This reference substantiates that abstract reference in the role serviceClass
                # for this specific concrete class.
        # Thereby, the reference represents the ability to access among all
                # DiagnosticDynamicallyDefine the given context.
        self._dynamically: Optional["DiagnosticDynamically"] = None

    @property
    def dynamically(self) -> Optional["DiagnosticDynamically"]:
        """Get dynamically (Pythonic accessor)."""
        return self._dynamically

    @dynamically.setter
    def dynamically(self, value: Optional["DiagnosticDynamically"]) -> None:
        """
        Set dynamically with validation.
        
        Args:
            value: The dynamically to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dynamically = None
            return

        if not isinstance(value, DiagnosticDynamically):
            raise TypeError(
                f"dynamically must be DiagnosticDynamically or None, got {type(value).__name__}"
            )
        self._dynamically = value
        # This represents the maximum number of source elements the dynamically created
        # DID.
        self._maxSource: Optional["PositiveInteger"] = None

    @property
    def max_source(self) -> Optional["PositiveInteger"]:
        """Get maxSource (Pythonic accessor)."""
        return self._maxSource

    @max_source.setter
    def max_source(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxSource with validation.
        
        Args:
            value: The maxSource to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxSource = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"maxSource must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._maxSource = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataIdentifier(self) -> "DiagnosticDynamicData":
        """
        AUTOSAR-compliant getter for dataIdentifier.
        
        Returns:
            The dataIdentifier value
        
        Note:
            Delegates to data_identifier property (CODING_RULE_V2_00017)
        """
        return self.data_identifier  # Delegates to property

    def setDataIdentifier(self, value: "DiagnosticDynamicData") -> "DiagnosticDynamicallyDefineDataIdentifier":
        """
        AUTOSAR-compliant setter for dataIdentifier with method chaining.
        
        Args:
            value: The dataIdentifier to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to data_identifier property setter (gets validation automatically)
        """
        self.data_identifier = value  # Delegates to property setter
        return self

    def getDynamically(self) -> "DiagnosticDynamically":
        """
        AUTOSAR-compliant getter for dynamically.
        
        Returns:
            The dynamically value
        
        Note:
            Delegates to dynamically property (CODING_RULE_V2_00017)
        """
        return self.dynamically  # Delegates to property

    def setDynamically(self, value: "DiagnosticDynamically") -> "DiagnosticDynamicallyDefineDataIdentifier":
        """
        AUTOSAR-compliant setter for dynamically with method chaining.
        
        Args:
            value: The dynamically to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to dynamically property setter (gets validation automatically)
        """
        self.dynamically = value  # Delegates to property setter
        return self

    def getMaxSource(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxSource.
        
        Returns:
            The maxSource value
        
        Note:
            Delegates to max_source property (CODING_RULE_V2_00017)
        """
        return self.max_source  # Delegates to property

    def setMaxSource(self, value: "PositiveInteger") -> "DiagnosticDynamicallyDefineDataIdentifier":
        """
        AUTOSAR-compliant setter for maxSource with method chaining.
        
        Args:
            value: The maxSource to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to max_source property setter (gets validation automatically)
        """
        self.max_source = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_identifier(self, value: Optional["DiagnosticDynamicData"]) -> "DiagnosticDynamicallyDefineDataIdentifier":
        """
        Set dataIdentifier and return self for chaining.
        
        Args:
            value: The dataIdentifier to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_data_identifier("value")
        """
        self.data_identifier = value  # Use property setter (gets validation)
        return self

    def with_dynamically(self, value: Optional["DiagnosticDynamically"]) -> "DiagnosticDynamicallyDefineDataIdentifier":
        """
        Set dynamically and return self for chaining.
        
        Args:
            value: The dynamically to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_dynamically("value")
        """
        self.dynamically = value  # Use property setter (gets validation)
        return self

    def with_max_source(self, value: Optional["PositiveInteger"]) -> "DiagnosticDynamicallyDefineDataIdentifier":
        """
        Set maxSource and return self for chaining.
        
        Args:
            value: The maxSource to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_max_source("value")
        """
        self.max_source = value  # Use property setter (gets validation)
        return self