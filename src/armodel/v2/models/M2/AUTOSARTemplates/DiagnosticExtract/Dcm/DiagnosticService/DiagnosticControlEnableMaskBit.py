from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class DiagnosticControlEnableMaskBit(ARObject):
    """
    This meta-class has the ability to represent one bit in the control enable
    mask record.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::IOControl::DiagnosticControlEnableMaskBit
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 119, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represents the bit number of the bit in the record.
        # Bit number 0 is the most significant in the first byte of the CEMR in the
                # network.
        self._bitNumber: Optional["PositiveInteger"] = None

    @property
    def bit_number(self) -> Optional["PositiveInteger"]:
        """Get bitNumber (Pythonic accessor)."""
        return self._bitNumber

    @bit_number.setter
    def bit_number(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set bitNumber with validation.
        
        Args:
            value: The bitNumber to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bitNumber = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"bitNumber must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._bitNumber = value
        # This reference represents the collection of Diagnostic that are controlled by
        # this bit of the control.
        self._controlledData: List["DiagnosticDataElement"] = []

    @property
    def controlled_data(self) -> List["DiagnosticDataElement"]:
        """Get controlledData (Pythonic accessor)."""
        return self._controlledData

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBitNumber(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for bitNumber.
        
        Returns:
            The bitNumber value
        
        Note:
            Delegates to bit_number property (CODING_RULE_V2_00017)
        """
        return self.bit_number  # Delegates to property

    def setBitNumber(self, value: "PositiveInteger") -> "DiagnosticControlEnableMaskBit":
        """
        AUTOSAR-compliant setter for bitNumber with method chaining.
        
        Args:
            value: The bitNumber to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to bit_number property setter (gets validation automatically)
        """
        self.bit_number = value  # Delegates to property setter
        return self

    def getControlledData(self) -> List["DiagnosticDataElement"]:
        """
        AUTOSAR-compliant getter for controlledData.
        
        Returns:
            The controlledData value
        
        Note:
            Delegates to controlled_data property (CODING_RULE_V2_00017)
        """
        return self.controlled_data  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bit_number(self, value: Optional["PositiveInteger"]) -> "DiagnosticControlEnableMaskBit":
        """
        Set bitNumber and return self for chaining.
        
        Args:
            value: The bitNumber to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_bit_number("value")
        """
        self.bit_number = value  # Use property setter (gets validation)
        return self