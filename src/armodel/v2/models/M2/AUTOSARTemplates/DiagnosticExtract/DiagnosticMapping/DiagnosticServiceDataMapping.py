from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

class DiagnosticServiceDataMapping(DiagnosticSwMapping):
    """
    This represents the ability to define a mapping of a diagnostic service to a
    software-component. This kind of service mapping is applicable for the usage
    of SenderReceiverInterfaces or event/notifier semantics in ServiceInterfaces
    on the adaptive platform.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::ServiceMapping::DiagnosticServiceDataMapping
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 228, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the applicable payload that corresponds the referenced
        # DataPrototype in the role mappedData (in case of a usage on the adaptive
        # platform).
        self._diagnosticData: Optional["DiagnosticDataElement"] = None

    @property
    def diagnostic_data(self) -> Optional["DiagnosticDataElement"]:
        """Get diagnosticData (Pythonic accessor)."""
        return self._diagnosticData

    @diagnostic_data.setter
    def diagnostic_data(self, value: Optional["DiagnosticDataElement"]) -> None:
        """
        Set diagnosticData with validation.
        
        Args:
            value: The diagnosticData to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._diagnosticData = None
            return

        if not isinstance(value, DiagnosticDataElement):
            raise TypeError(
                f"diagnosticData must be DiagnosticDataElement or None, got {type(value).__name__}"
            )
        self._diagnosticData = value
        # This represents the applicable payload that corresponds to the referenced
        # DataPrototype in the role mappedData.
        self._diagnostic: Optional["DiagnosticParameter"] = None

    @property
    def diagnostic(self) -> Optional["DiagnosticParameter"]:
        """Get diagnostic (Pythonic accessor)."""
        return self._diagnostic

    @diagnostic.setter
    def diagnostic(self, value: Optional["DiagnosticParameter"]) -> None:
        """
        Set diagnostic with validation.
        
        Args:
            value: The diagnostic to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._diagnostic = None
            return

        if not isinstance(value, DiagnosticParameter):
            raise TypeError(
                f"diagnostic must be DiagnosticParameter or None, got {type(value).__name__}"
            )
        self._diagnostic = value
        # that is accessed for diagnostic purpose.
        # This applicable on the classic platform.
        # by: DataPrototypeInSystem.
        self._mappedData: RefType = None

    @property
    def mapped_data(self) -> RefType:
        """Get mappedData (Pythonic accessor)."""
        return self._mappedData

    @mapped_data.setter
    def mapped_data(self, value: RefType) -> None:
        """
        Set mappedData with validation.
        
        Args:
            value: The mappedData to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mappedData = None
            return

        self._mappedData = value
        # This aggregation represents the single point of access to the reference to
        # one specific DiagnosticParameter.
        self._parameter: Optional["DiagnosticParameter"] = None

    @property
    def parameter(self) -> Optional["DiagnosticParameter"]:
        """Get parameter (Pythonic accessor)."""
        return self._parameter

    @parameter.setter
    def parameter(self, value: Optional["DiagnosticParameter"]) -> None:
        """
        Set parameter with validation.
        
        Args:
            value: The parameter to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._parameter = None
            return

        if not isinstance(value, DiagnosticParameter):
            raise TypeError(
                f"parameter must be DiagnosticParameter or None, got {type(value).__name__}"
            )
        self._parameter = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDiagnosticData(self) -> "DiagnosticDataElement":
        """
        AUTOSAR-compliant getter for diagnosticData.
        
        Returns:
            The diagnosticData value
        
        Note:
            Delegates to diagnostic_data property (CODING_RULE_V2_00017)
        """
        return self.diagnostic_data  # Delegates to property

    def setDiagnosticData(self, value: "DiagnosticDataElement") -> "DiagnosticServiceDataMapping":
        """
        AUTOSAR-compliant setter for diagnosticData with method chaining.
        
        Args:
            value: The diagnosticData to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to diagnostic_data property setter (gets validation automatically)
        """
        self.diagnostic_data = value  # Delegates to property setter
        return self

    def getDiagnostic(self) -> "DiagnosticParameter":
        """
        AUTOSAR-compliant getter for diagnostic.
        
        Returns:
            The diagnostic value
        
        Note:
            Delegates to diagnostic property (CODING_RULE_V2_00017)
        """
        return self.diagnostic  # Delegates to property

    def setDiagnostic(self, value: "DiagnosticParameter") -> "DiagnosticServiceDataMapping":
        """
        AUTOSAR-compliant setter for diagnostic with method chaining.
        
        Args:
            value: The diagnostic to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to diagnostic property setter (gets validation automatically)
        """
        self.diagnostic = value  # Delegates to property setter
        return self

    def getMappedData(self) -> RefType:
        """
        AUTOSAR-compliant getter for mappedData.
        
        Returns:
            The mappedData value
        
        Note:
            Delegates to mapped_data property (CODING_RULE_V2_00017)
        """
        return self.mapped_data  # Delegates to property

    def setMappedData(self, value: RefType) -> "DiagnosticServiceDataMapping":
        """
        AUTOSAR-compliant setter for mappedData with method chaining.
        
        Args:
            value: The mappedData to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to mapped_data property setter (gets validation automatically)
        """
        self.mapped_data = value  # Delegates to property setter
        return self

    def getParameter(self) -> "DiagnosticParameter":
        """
        AUTOSAR-compliant getter for parameter.
        
        Returns:
            The parameter value
        
        Note:
            Delegates to parameter property (CODING_RULE_V2_00017)
        """
        return self.parameter  # Delegates to property

    def setParameter(self, value: "DiagnosticParameter") -> "DiagnosticServiceDataMapping":
        """
        AUTOSAR-compliant setter for parameter with method chaining.
        
        Args:
            value: The parameter to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to parameter property setter (gets validation automatically)
        """
        self.parameter = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_diagnostic_data(self, value: Optional["DiagnosticDataElement"]) -> "DiagnosticServiceDataMapping":
        """
        Set diagnosticData and return self for chaining.
        
        Args:
            value: The diagnosticData to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_diagnostic_data("value")
        """
        self.diagnostic_data = value  # Use property setter (gets validation)
        return self

    def with_diagnostic(self, value: Optional["DiagnosticParameter"]) -> "DiagnosticServiceDataMapping":
        """
        Set diagnostic and return self for chaining.
        
        Args:
            value: The diagnostic to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_diagnostic("value")
        """
        self.diagnostic = value  # Use property setter (gets validation)
        return self

    def with_mapped_data(self, value: Optional[RefType]) -> "DiagnosticServiceDataMapping":
        """
        Set mappedData and return self for chaining.
        
        Args:
            value: The mappedData to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_mapped_data("value")
        """
        self.mapped_data = value  # Use property setter (gets validation)
        return self

    def with_parameter(self, value: Optional["DiagnosticParameter"]) -> "DiagnosticServiceDataMapping":
        """
        Set parameter and return self for chaining.
        
        Args:
            value: The parameter to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_parameter("value")
        """
        self.parameter = value  # Use property setter (gets validation)
        return self