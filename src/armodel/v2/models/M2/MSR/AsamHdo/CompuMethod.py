from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class CompuMethod(ARElement):
    """
    that this is still independent of the technical implementation in data
    types. It only specifies the formula how the internal value corresponds to
    its physical pendant.
    
    Package: M2::MSR::AsamHdo::ComputationMethod::CompuMethod
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 310, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 308, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 380, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2010, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 436, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (Page 30, Foundation R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 176, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This specifies the computation from internal values to values.
        self._compuInternal: Optional["Compu"] = None

    @property
    def compu_internal(self) -> Optional["Compu"]:
        """Get compuInternal (Pythonic accessor)."""
        return self._compuInternal

    @compu_internal.setter
    def compu_internal(self, value: Optional["Compu"]) -> None:
        """
        Set compuInternal with validation.
        
        Args:
            value: The compuInternal to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._compuInternal = None
            return

        if not isinstance(value, Compu):
            raise TypeError(
                f"compuInternal must be Compu or None, got {type(value).__name__}"
            )
        self._compuInternal = value
        # This represents the computation from physical values to internal values.
        self._compuPhysTo: Optional["Compu"] = None

    @property
    def compu_phys_to(self) -> Optional["Compu"]:
        """Get compuPhysTo (Pythonic accessor)."""
        return self._compuPhysTo

    @compu_phys_to.setter
    def compu_phys_to(self, value: Optional["Compu"]) -> None:
        """
        Set compuPhysTo with validation.
        
        Args:
            value: The compuPhysTo to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._compuPhysTo = None
            return

        if not isinstance(value, Compu):
            raise TypeError(
                f"compuPhysTo must be Compu or None, got {type(value).__name__}"
            )
        self._compuPhysTo = value
        # This property specifies, how the physical value shall be in documents or
        # measurement and.
        self._displayFormat: Optional["DisplayFormatString"] = None

    @property
    def display_format(self) -> Optional["DisplayFormatString"]:
        """Get displayFormat (Pythonic accessor)."""
        return self._displayFormat

    @display_format.setter
    def display_format(self, value: Optional["DisplayFormatString"]) -> None:
        """
        Set displayFormat with validation.
        
        Args:
            value: The displayFormat to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._displayFormat = None
            return

        if not isinstance(value, DisplayFormatString):
            raise TypeError(
                f"displayFormat must be DisplayFormatString or None, got {type(value).__name__}"
            )
        self._displayFormat = value
        # This is the physical unit of the Physical values for which applies.
        self._unit: Optional["Unit"] = None

    @property
    def unit(self) -> Optional["Unit"]:
        """Get unit (Pythonic accessor)."""
        return self._unit

    @unit.setter
    def unit(self, value: Optional["Unit"]) -> None:
        """
        Set unit with validation.
        
        Args:
            value: The unit to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._unit = None
            return

        if not isinstance(value, Unit):
            raise TypeError(
                f"unit must be Unit or None, got {type(value).__name__}"
            )
        self._unit = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCompuInternal(self) -> "Compu":
        """
        AUTOSAR-compliant getter for compuInternal.
        
        Returns:
            The compuInternal value
        
        Note:
            Delegates to compu_internal property (CODING_RULE_V2_00017)
        """
        return self.compu_internal  # Delegates to property

    def setCompuInternal(self, value: "Compu") -> "CompuMethod":
        """
        AUTOSAR-compliant setter for compuInternal with method chaining.
        
        Args:
            value: The compuInternal to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to compu_internal property setter (gets validation automatically)
        """
        self.compu_internal = value  # Delegates to property setter
        return self

    def getCompuPhysTo(self) -> "Compu":
        """
        AUTOSAR-compliant getter for compuPhysTo.
        
        Returns:
            The compuPhysTo value
        
        Note:
            Delegates to compu_phys_to property (CODING_RULE_V2_00017)
        """
        return self.compu_phys_to  # Delegates to property

    def setCompuPhysTo(self, value: "Compu") -> "CompuMethod":
        """
        AUTOSAR-compliant setter for compuPhysTo with method chaining.
        
        Args:
            value: The compuPhysTo to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to compu_phys_to property setter (gets validation automatically)
        """
        self.compu_phys_to = value  # Delegates to property setter
        return self

    def getDisplayFormat(self) -> "DisplayFormatString":
        """
        AUTOSAR-compliant getter for displayFormat.
        
        Returns:
            The displayFormat value
        
        Note:
            Delegates to display_format property (CODING_RULE_V2_00017)
        """
        return self.display_format  # Delegates to property

    def setDisplayFormat(self, value: "DisplayFormatString") -> "CompuMethod":
        """
        AUTOSAR-compliant setter for displayFormat with method chaining.
        
        Args:
            value: The displayFormat to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to display_format property setter (gets validation automatically)
        """
        self.display_format = value  # Delegates to property setter
        return self

    def getUnit(self) -> "Unit":
        """
        AUTOSAR-compliant getter for unit.
        
        Returns:
            The unit value
        
        Note:
            Delegates to unit property (CODING_RULE_V2_00017)
        """
        return self.unit  # Delegates to property

    def setUnit(self, value: "Unit") -> "CompuMethod":
        """
        AUTOSAR-compliant setter for unit with method chaining.
        
        Args:
            value: The unit to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to unit property setter (gets validation automatically)
        """
        self.unit = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_compu_internal(self, value: Optional["Compu"]) -> "CompuMethod":
        """
        Set compuInternal and return self for chaining.
        
        Args:
            value: The compuInternal to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_compu_internal("value")
        """
        self.compu_internal = value  # Use property setter (gets validation)
        return self

    def with_compu_phys_to(self, value: Optional["Compu"]) -> "CompuMethod":
        """
        Set compuPhysTo and return self for chaining.
        
        Args:
            value: The compuPhysTo to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_compu_phys_to("value")
        """
        self.compu_phys_to = value  # Use property setter (gets validation)
        return self

    def with_display_format(self, value: Optional["DisplayFormatString"]) -> "CompuMethod":
        """
        Set displayFormat and return self for chaining.
        
        Args:
            value: The displayFormat to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_display_format("value")
        """
        self.display_format = value  # Use property setter (gets validation)
        return self

    def with_unit(self, value: Optional["Unit"]) -> "CompuMethod":
        """
        Set unit and return self for chaining.
        
        Args:
            value: The unit to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_unit("value")
        """
        self.unit = value  # Use property setter (gets validation)
        return self