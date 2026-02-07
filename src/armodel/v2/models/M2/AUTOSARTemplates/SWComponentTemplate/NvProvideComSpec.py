from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

class NvProvideComSpec(PPortComSpec):
    """
    Communication attributes of PPortPrototypes with respect to Nv data
    communication on the provided side.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication::NvProvideComSpec
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 195, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the initial value of the RAM Block that to the referenced
        # variable.
        self._ramBlockInit: Optional["ValueSpecification"] = None

    @property
    def ram_block_init(self) -> Optional["ValueSpecification"]:
        """Get ramBlockInit (Pythonic accessor)."""
        return self._ramBlockInit

    @ram_block_init.setter
    def ram_block_init(self, value: Optional["ValueSpecification"]) -> None:
        """
        Set ramBlockInit with validation.
        
        Args:
            value: The ramBlockInit to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ramBlockInit = None
            return

        if not isinstance(value, ValueSpecification):
            raise TypeError(
                f"ramBlockInit must be ValueSpecification or None, got {type(value).__name__}"
            )
        self._ramBlockInit = value
        # This represents the initial value of the ROM block that to the referenced
        # variable.
        self._romBlockInit: Optional["ValueSpecification"] = None

    @property
    def rom_block_init(self) -> Optional["ValueSpecification"]:
        """Get romBlockInit (Pythonic accessor)."""
        return self._romBlockInit

    @rom_block_init.setter
    def rom_block_init(self, value: Optional["ValueSpecification"]) -> None:
        """
        Set romBlockInit with validation.
        
        Args:
            value: The romBlockInit to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._romBlockInit = None
            return

        if not isinstance(value, ValueSpecification):
            raise TypeError(
                f"romBlockInit must be ValueSpecification or None, got {type(value).__name__}"
            )
        self._romBlockInit = value
        # This represents the variable for which the ComSpec is.
        self._variable: RefType = None

    @property
    def variable(self) -> RefType:
        """Get variable (Pythonic accessor)."""
        return self._variable

    @variable.setter
    def variable(self, value: RefType) -> None:
        """
        Set variable with validation.
        
        Args:
            value: The variable to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._variable = None
            return

        self._variable = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRamBlockInit(self) -> "ValueSpecification":
        """
        AUTOSAR-compliant getter for ramBlockInit.
        
        Returns:
            The ramBlockInit value
        
        Note:
            Delegates to ram_block_init property (CODING_RULE_V2_00017)
        """
        return self.ram_block_init  # Delegates to property

    def setRamBlockInit(self, value: "ValueSpecification") -> "NvProvideComSpec":
        """
        AUTOSAR-compliant setter for ramBlockInit with method chaining.
        
        Args:
            value: The ramBlockInit to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to ram_block_init property setter (gets validation automatically)
        """
        self.ram_block_init = value  # Delegates to property setter
        return self

    def getRomBlockInit(self) -> "ValueSpecification":
        """
        AUTOSAR-compliant getter for romBlockInit.
        
        Returns:
            The romBlockInit value
        
        Note:
            Delegates to rom_block_init property (CODING_RULE_V2_00017)
        """
        return self.rom_block_init  # Delegates to property

    def setRomBlockInit(self, value: "ValueSpecification") -> "NvProvideComSpec":
        """
        AUTOSAR-compliant setter for romBlockInit with method chaining.
        
        Args:
            value: The romBlockInit to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to rom_block_init property setter (gets validation automatically)
        """
        self.rom_block_init = value  # Delegates to property setter
        return self

    def getVariable(self) -> RefType:
        """
        AUTOSAR-compliant getter for variable.
        
        Returns:
            The variable value
        
        Note:
            Delegates to variable property (CODING_RULE_V2_00017)
        """
        return self.variable  # Delegates to property

    def setVariable(self, value: RefType) -> "NvProvideComSpec":
        """
        AUTOSAR-compliant setter for variable with method chaining.
        
        Args:
            value: The variable to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to variable property setter (gets validation automatically)
        """
        self.variable = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ram_block_init(self, value: Optional["ValueSpecification"]) -> "NvProvideComSpec":
        """
        Set ramBlockInit and return self for chaining.
        
        Args:
            value: The ramBlockInit to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_ram_block_init("value")
        """
        self.ram_block_init = value  # Use property setter (gets validation)
        return self

    def with_rom_block_init(self, value: Optional["ValueSpecification"]) -> "NvProvideComSpec":
        """
        Set romBlockInit and return self for chaining.
        
        Args:
            value: The romBlockInit to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_rom_block_init("value")
        """
        self.rom_block_init = value  # Use property setter (gets validation)
        return self

    def with_variable(self, value: Optional[RefType]) -> "NvProvideComSpec":
        """
        Set variable and return self for chaining.
        
        Args:
            value: The variable to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_variable("value")
        """
        self.variable = value  # Use property setter (gets validation)
        return self