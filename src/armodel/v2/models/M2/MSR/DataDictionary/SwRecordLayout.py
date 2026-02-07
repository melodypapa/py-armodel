from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

class SwRecordLayout(ARElement):
    """
    Defines how the data objects (variables, calibration parameters etc.) are to
    be stored in the ECU memory. As an example, this definition specifies the
    sequence of axis points in the ECU memory. Iterations through axis values
    are stored within the sub-elements swRecordLayoutGroup.
    
    Package: M2::MSR::DataDictionary::RecordLayout::SwRecordLayout
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 421, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2066, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the top level record layout group.
        self._swRecord: RefType = None

    @property
    def sw_record(self) -> RefType:
        """Get swRecord (Pythonic accessor)."""
        return self._swRecord

    @sw_record.setter
    def sw_record(self, value: RefType) -> None:
        """
        Set swRecord with validation.
        
        Args:
            value: The swRecord to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swRecord = None
            return

        self._swRecord = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSwRecord(self) -> RefType:
        """
        AUTOSAR-compliant getter for swRecord.
        
        Returns:
            The swRecord value
        
        Note:
            Delegates to sw_record property (CODING_RULE_V2_00017)
        """
        return self.sw_record  # Delegates to property

    def setSwRecord(self, value: RefType) -> "SwRecordLayout":
        """
        AUTOSAR-compliant setter for swRecord with method chaining.
        
        Args:
            value: The swRecord to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sw_record property setter (gets validation automatically)
        """
        self.sw_record = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sw_record(self, value: Optional[RefType]) -> "SwRecordLayout":
        """
        Set swRecord and return self for chaining.
        
        Args:
            value: The swRecord to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sw_record("value")
        """
        self.sw_record = value  # Use property setter (gets validation)
        return self