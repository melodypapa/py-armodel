"""
AUTOSAR Package - DiagnosticFreezeFrame

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticFreezeFrame
"""

from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    String,
)
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import (
    DiagnosticCommonElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class DiagnosticFreezeFrame(DiagnosticCommonElement):
    """
    This element describes combinations of DIDs for a non OBD relevant freeze
    frame.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticFreezeFrame::DiagnosticFreezeFrame
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 192, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute shall be taken to verbally describe the the custom trigger.
        self._customTrigger: Optional["String"] = None

    @property
    def custom_trigger(self) -> Optional["String"]:
        """Get customTrigger (Pythonic accessor)."""
        return self._customTrigger

    @custom_trigger.setter
    def custom_trigger(self, value: Optional["String"]) -> None:
        """
        Set customTrigger with validation.
        
        Args:
            value: The customTrigger to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._customTrigger = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"customTrigger must be String or str or None, got {type(value).__name__}"
            )
        self._customTrigger = value
        # This attribute defines a record number for a freeze frame.
        self._recordNumber: Optional["PositiveInteger"] = None

    @property
    def record_number(self) -> Optional["PositiveInteger"]:
        """Get recordNumber (Pythonic accessor)."""
        return self._recordNumber

    @record_number.setter
    def record_number(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set recordNumber with validation.
        
        Args:
            value: The recordNumber to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._recordNumber = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"recordNumber must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._recordNumber = value
        # This attribute defines the primary trigger to allocate an memory entry.
        self._trigger: Optional["DiagnosticRecord"] = None

    @property
    def trigger(self) -> Optional["DiagnosticRecord"]:
        """Get trigger (Pythonic accessor)."""
        return self._trigger

    @trigger.setter
    def trigger(self, value: Optional["DiagnosticRecord"]) -> None:
        """
        Set trigger with validation.
        
        Args:
            value: The trigger to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._trigger = None
            return

        if not isinstance(value, DiagnosticRecord):
            raise TypeError(
                f"trigger must be DiagnosticRecord or None, got {type(value).__name__}"
            )
        self._trigger = value
        # This attribute defines the approach when the freeze frame stored/updated.
        # record is captured every time.
        # record is only captured for new event.
        self._update: Optional["Boolean"] = None

    @property
    def update(self) -> Optional["Boolean"]:
        """Get update (Pythonic accessor)."""
        return self._update

    @update.setter
    def update(self, value: Optional["Boolean"]) -> None:
        """
        Set update with validation.
        
        Args:
            value: The update to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._update = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"update must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._update = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCustomTrigger(self) -> "String":
        """
        AUTOSAR-compliant getter for customTrigger.
        
        Returns:
            The customTrigger value
        
        Note:
            Delegates to custom_trigger property (CODING_RULE_V2_00017)
        """
        return self.custom_trigger  # Delegates to property

    def setCustomTrigger(self, value: "String") -> "DiagnosticFreezeFrame":
        """
        AUTOSAR-compliant setter for customTrigger with method chaining.
        
        Args:
            value: The customTrigger to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to custom_trigger property setter (gets validation automatically)
        """
        self.custom_trigger = value  # Delegates to property setter
        return self

    def getRecordNumber(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for recordNumber.
        
        Returns:
            The recordNumber value
        
        Note:
            Delegates to record_number property (CODING_RULE_V2_00017)
        """
        return self.record_number  # Delegates to property

    def setRecordNumber(self, value: "PositiveInteger") -> "DiagnosticFreezeFrame":
        """
        AUTOSAR-compliant setter for recordNumber with method chaining.
        
        Args:
            value: The recordNumber to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to record_number property setter (gets validation automatically)
        """
        self.record_number = value  # Delegates to property setter
        return self

    def getTrigger(self) -> "DiagnosticRecord":
        """
        AUTOSAR-compliant getter for trigger.
        
        Returns:
            The trigger value
        
        Note:
            Delegates to trigger property (CODING_RULE_V2_00017)
        """
        return self.trigger  # Delegates to property

    def setTrigger(self, value: "DiagnosticRecord") -> "DiagnosticFreezeFrame":
        """
        AUTOSAR-compliant setter for trigger with method chaining.
        
        Args:
            value: The trigger to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to trigger property setter (gets validation automatically)
        """
        self.trigger = value  # Delegates to property setter
        return self

    def getUpdate(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for update.
        
        Returns:
            The update value
        
        Note:
            Delegates to update property (CODING_RULE_V2_00017)
        """
        return self.update  # Delegates to property

    def setUpdate(self, value: "Boolean") -> "DiagnosticFreezeFrame":
        """
        AUTOSAR-compliant setter for update with method chaining.
        
        Args:
            value: The update to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to update property setter (gets validation automatically)
        """
        self.update = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_custom_trigger(self, value: Optional["String"]) -> "DiagnosticFreezeFrame":
        """
        Set customTrigger and return self for chaining.
        
        Args:
            value: The customTrigger to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_custom_trigger("value")
        """
        self.custom_trigger = value  # Use property setter (gets validation)
        return self

    def with_record_number(self, value: Optional["PositiveInteger"]) -> "DiagnosticFreezeFrame":
        """
        Set recordNumber and return self for chaining.
        
        Args:
            value: The recordNumber to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_record_number("value")
        """
        self.record_number = value  # Use property setter (gets validation)
        return self

    def with_trigger(self, value: Optional["DiagnosticRecord"]) -> "DiagnosticFreezeFrame":
        """
        Set trigger and return self for chaining.
        
        Args:
            value: The trigger to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_trigger("value")
        """
        self.trigger = value  # Use property setter (gets validation)
        return self

    def with_update(self, value: Optional["Boolean"]) -> "DiagnosticFreezeFrame":
        """
        Set update and return self for chaining.
        
        Args:
            value: The update to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_update("value")
        """
        self.update = value  # Use property setter (gets validation)
        return self


class DiagnosticRecordTriggerEnum(AREnum):
    """
    DiagnosticRecordTriggerEnum enumeration

Triggers to allocate an event memory entry. Aggregated by DiagnosticExtendedDataRecord.trigger, DiagnosticFreezeFrame.trigger

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticFreezeFrame
    """
    # capture on "Confirmed" custom implement custom capture fdcThreshold capture on "FDC Threshold" pending capture on "Pending" testFailed capture on "Test Failed"
    confirmed = "3"

    # Test Failed This Operation Cycle.
    testFailedThisOperationCycle = "5"

    # Capture on testFailed bit transition 1 –> 0.
    testPassed = "6"
