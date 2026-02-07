from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class DiagnosticValueNeeds(DiagnosticCapabilityElement):
    """
    Specifies the general needs on the configuration of the Diagnostic
    Communication Manager (DCM) which are not related to a particular item (e.g.
    a PID). The main use case is the mapping of service ports to the DCM which
    are not related to a particular item. In the case of using a sender receiver
    communicated value, the related value shall be taken via assigned Data in
    the role "signalBasedDiagnostics". In case of using a client/server
    communicated value, the related value shall be communicated via the port
    referenced by assignedPort. The details of this communication (e.g.
    appropriate naming conventions) are specified in the related software
    specifications (SWS). (cid:53) 245 of 381 Document ID 89:
    AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Basic Software Module
    Description Template AUTOSAR CP R23-11 (cid:52)
    
    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DiagnosticValueNeeds
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 245, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 114, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 782, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute is applicable only if the DiagnosticValue aggregated within a
                # BswModuleDependency.
        # represents the length of data (in bytes) this particular PID signal.
        self._dataLength: Optional["PositiveInteger"] = None

    @property
    def data_length(self) -> Optional["PositiveInteger"]:
        """Get dataLength (Pythonic accessor)."""
        return self._dataLength

    @data_length.setter
    def data_length(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set dataLength with validation.
        
        Args:
            value: The dataLength to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataLength = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"dataLength must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._dataLength = value
        # This attribute is applicable only if the DiagnosticValue Needs is aggregated
                # within a BswModuleDependency.
        # controls whether the data can be read and whether it is to be handled
                # read-only.
        self._diagnosticValue: Optional["DiagnosticValueAccess"] = None

    @property
    def diagnostic_value(self) -> Optional["DiagnosticValueAccess"]:
        """Get diagnosticValue (Pythonic accessor)."""
        return self._diagnosticValue

    @diagnostic_value.setter
    def diagnostic_value(self, value: Optional["DiagnosticValueAccess"]) -> None:
        """
        Set diagnosticValue with validation.
        
        Args:
            value: The diagnosticValue to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._diagnosticValue = None
            return

        if not isinstance(value, DiagnosticValueAccess):
            raise TypeError(
                f"diagnosticValue must be DiagnosticValueAccess or None, got {type(value).__name__}"
            )
        self._diagnosticValue = value
        # This attribute is applicable only if the DiagnosticValue aggregated within a
                # BswModuleDependency.
        # controls whether the data length of the data.
        self._fixedLength: Optional["Boolean"] = None

    @property
    def fixed_length(self) -> Optional["Boolean"]:
        """Get fixedLength (Pythonic accessor)."""
        return self._fixedLength

    @fixed_length.setter
    def fixed_length(self, value: Optional["Boolean"]) -> None:
        """
        Set fixedLength with validation.
        
        Args:
            value: The fixedLength to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._fixedLength = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"fixedLength must be Boolean or None, got {type(value).__name__}"
            )
        self._fixedLength = value
        # This attribute controls whether interaction requires the to react
        # synchronously on a request it processes the request in background but still
        # has to issue the call again to eventually obtain of the request.
        self._processingStyle: Optional["DiagnosticProcessing"] = None

    @property
    def processing_style(self) -> Optional["DiagnosticProcessing"]:
        """Get processingStyle (Pythonic accessor)."""
        return self._processingStyle

    @processing_style.setter
    def processing_style(self, value: Optional["DiagnosticProcessing"]) -> None:
        """
        Set processingStyle with validation.
        
        Args:
            value: The processingStyle to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._processingStyle = None
            return

        if not isinstance(value, DiagnosticProcessing):
            raise TypeError(
                f"processingStyle must be DiagnosticProcessing or None, got {type(value).__name__}"
            )
        self._processingStyle = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataLength(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for dataLength.
        
        Returns:
            The dataLength value
        
        Note:
            Delegates to data_length property (CODING_RULE_V2_00017)
        """
        return self.data_length  # Delegates to property

    def setDataLength(self, value: "PositiveInteger") -> "DiagnosticValueNeeds":
        """
        AUTOSAR-compliant setter for dataLength with method chaining.
        
        Args:
            value: The dataLength to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to data_length property setter (gets validation automatically)
        """
        self.data_length = value  # Delegates to property setter
        return self

    def getDiagnosticValue(self) -> "DiagnosticValueAccess":
        """
        AUTOSAR-compliant getter for diagnosticValue.
        
        Returns:
            The diagnosticValue value
        
        Note:
            Delegates to diagnostic_value property (CODING_RULE_V2_00017)
        """
        return self.diagnostic_value  # Delegates to property

    def setDiagnosticValue(self, value: "DiagnosticValueAccess") -> "DiagnosticValueNeeds":
        """
        AUTOSAR-compliant setter for diagnosticValue with method chaining.
        
        Args:
            value: The diagnosticValue to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to diagnostic_value property setter (gets validation automatically)
        """
        self.diagnostic_value = value  # Delegates to property setter
        return self

    def getFixedLength(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for fixedLength.
        
        Returns:
            The fixedLength value
        
        Note:
            Delegates to fixed_length property (CODING_RULE_V2_00017)
        """
        return self.fixed_length  # Delegates to property

    def setFixedLength(self, value: "Boolean") -> "DiagnosticValueNeeds":
        """
        AUTOSAR-compliant setter for fixedLength with method chaining.
        
        Args:
            value: The fixedLength to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to fixed_length property setter (gets validation automatically)
        """
        self.fixed_length = value  # Delegates to property setter
        return self

    def getProcessingStyle(self) -> "DiagnosticProcessing":
        """
        AUTOSAR-compliant getter for processingStyle.
        
        Returns:
            The processingStyle value
        
        Note:
            Delegates to processing_style property (CODING_RULE_V2_00017)
        """
        return self.processing_style  # Delegates to property

    def setProcessingStyle(self, value: "DiagnosticProcessing") -> "DiagnosticValueNeeds":
        """
        AUTOSAR-compliant setter for processingStyle with method chaining.
        
        Args:
            value: The processingStyle to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to processing_style property setter (gets validation automatically)
        """
        self.processing_style = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_length(self, value: Optional["PositiveInteger"]) -> "DiagnosticValueNeeds":
        """
        Set dataLength and return self for chaining.
        
        Args:
            value: The dataLength to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_data_length("value")
        """
        self.data_length = value  # Use property setter (gets validation)
        return self

    def with_diagnostic_value(self, value: Optional["DiagnosticValueAccess"]) -> "DiagnosticValueNeeds":
        """
        Set diagnosticValue and return self for chaining.
        
        Args:
            value: The diagnosticValue to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_diagnostic_value("value")
        """
        self.diagnostic_value = value  # Use property setter (gets validation)
        return self

    def with_fixed_length(self, value: Optional["Boolean"]) -> "DiagnosticValueNeeds":
        """
        Set fixedLength and return self for chaining.
        
        Args:
            value: The fixedLength to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_fixed_length("value")
        """
        self.fixed_length = value  # Use property setter (gets validation)
        return self

    def with_processing_style(self, value: Optional["DiagnosticProcessing"]) -> "DiagnosticValueNeeds":
        """
        Set processingStyle and return self for chaining.
        
        Args:
            value: The processingStyle to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_processing_style("value")
        """
        self.processing_style = value  # Use property setter (gets validation)
        return self