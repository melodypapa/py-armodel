from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class McParameterElementGroup(ARObject):
    """
    Denotes a group of calibration parameters which are handled by the RTE as
    one data structure.
    
    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::McParameterElementGroup
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 181, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Refers to the RAM location of this parameter group.
        # To be the init-RAM method.
        self._ramLocation: RefType = None

    @property
    def ram_location(self) -> RefType:
        """Get ramLocation (Pythonic accessor)."""
        return self._ramLocation

    @ram_location.setter
    def ram_location(self, value: RefType) -> None:
        """
        Set ramLocation with validation.
        
        Args:
            value: The ramLocation to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ramLocation = None
            return

        self._ramLocation = value
        # Refers to the ROM location of this parameter group.
        # To used for the init-RAM method.
        self._romLocation: Optional["ParameterData"] = None

    @property
    def rom_location(self) -> Optional["ParameterData"]:
        """Get romLocation (Pythonic accessor)."""
        return self._romLocation

    @rom_location.setter
    def rom_location(self, value: Optional["ParameterData"]) -> None:
        """
        Set romLocation with validation.
        
        Args:
            value: The romLocation to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._romLocation = None
            return

        if not isinstance(value, ParameterData):
            raise TypeError(
                f"romLocation must be ParameterData or None, got {type(value).__name__}"
            )
        self._romLocation = value
        # Assigns a name to this element.
        self._shortLabel: Optional["Identifier"] = None

    @property
    def short_label(self) -> Optional["Identifier"]:
        """Get shortLabel (Pythonic accessor)."""
        return self._shortLabel

    @short_label.setter
    def short_label(self, value: Optional["Identifier"]) -> None:
        """
        Set shortLabel with validation.
        
        Args:
            value: The shortLabel to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._shortLabel = None
            return

        if not isinstance(value, Identifier):
            raise TypeError(
                f"shortLabel must be Identifier or None, got {type(value).__name__}"
            )
        self._shortLabel = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRamLocation(self) -> RefType:
        """
        AUTOSAR-compliant getter for ramLocation.
        
        Returns:
            The ramLocation value
        
        Note:
            Delegates to ram_location property (CODING_RULE_V2_00017)
        """
        return self.ram_location  # Delegates to property

    def setRamLocation(self, value: RefType) -> "McParameterElementGroup":
        """
        AUTOSAR-compliant setter for ramLocation with method chaining.
        
        Args:
            value: The ramLocation to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to ram_location property setter (gets validation automatically)
        """
        self.ram_location = value  # Delegates to property setter
        return self

    def getRomLocation(self) -> "ParameterData":
        """
        AUTOSAR-compliant getter for romLocation.
        
        Returns:
            The romLocation value
        
        Note:
            Delegates to rom_location property (CODING_RULE_V2_00017)
        """
        return self.rom_location  # Delegates to property

    def setRomLocation(self, value: "ParameterData") -> "McParameterElementGroup":
        """
        AUTOSAR-compliant setter for romLocation with method chaining.
        
        Args:
            value: The romLocation to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to rom_location property setter (gets validation automatically)
        """
        self.rom_location = value  # Delegates to property setter
        return self

    def getShortLabel(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for shortLabel.
        
        Returns:
            The shortLabel value
        
        Note:
            Delegates to short_label property (CODING_RULE_V2_00017)
        """
        return self.short_label  # Delegates to property

    def setShortLabel(self, value: "Identifier") -> "McParameterElementGroup":
        """
        AUTOSAR-compliant setter for shortLabel with method chaining.
        
        Args:
            value: The shortLabel to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to short_label property setter (gets validation automatically)
        """
        self.short_label = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ram_location(self, value: Optional[RefType]) -> "McParameterElementGroup":
        """
        Set ramLocation and return self for chaining.
        
        Args:
            value: The ramLocation to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_ram_location("value")
        """
        self.ram_location = value  # Use property setter (gets validation)
        return self

    def with_rom_location(self, value: Optional["ParameterData"]) -> "McParameterElementGroup":
        """
        Set romLocation and return self for chaining.
        
        Args:
            value: The romLocation to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_rom_location("value")
        """
        self.rom_location = value  # Use property setter (gets validation)
        return self

    def with_short_label(self, value: Optional["Identifier"]) -> "McParameterElementGroup":
        """
        Set shortLabel and return self for chaining.
        
        Args:
            value: The shortLabel to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_short_label("value")
        """
        self.short_label = value  # Use property setter (gets validation)
        return self