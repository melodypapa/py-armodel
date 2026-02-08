"""
AUTOSAR Package - MultidimensionalTime

Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::MultidimensionalTime
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)




class MultidimensionalTime(ARObject):
    """
    Specifies a time value based on [20] see [TPS_GST_00354].
    
    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::MultidimensionalTime::MultidimensionalTime
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 164, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 109, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 165, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the time base by means of CSE codes.
        self._cseCode: Optional["CseCodeType"] = None

    @property
    def cse_code(self) -> Optional["CseCodeType"]:
        """Get cseCode (Pythonic accessor)."""
        return self._cseCode

    @cse_code.setter
    def cse_code(self, value: Optional["CseCodeType"]) -> None:
        """
        Set cseCode with validation.
        
        Args:
            value: The cseCode to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cseCode = None
            return

        if not isinstance(value, CseCodeType):
            raise TypeError(
                f"cseCode must be CseCodeType or None, got {type(value).__name__}"
            )
        self._cseCode = value
        # The scaling factor for the time value based on the code.
        self._cseCodeFactor: Optional["Integer"] = None

    @property
    def cse_code_factor(self) -> Optional["Integer"]:
        """Get cseCodeFactor (Pythonic accessor)."""
        return self._cseCodeFactor

    @cse_code_factor.setter
    def cse_code_factor(self, value: Optional["Integer"]) -> None:
        """
        Set cseCodeFactor with validation.
        
        Args:
            value: The cseCodeFactor to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cseCodeFactor = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"cseCodeFactor must be Integer or int or None, got {type(value).__name__}"
            )
        self._cseCodeFactor = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCseCode(self) -> "CseCodeType":
        """
        AUTOSAR-compliant getter for cseCode.
        
        Returns:
            The cseCode value
        
        Note:
            Delegates to cse_code property (CODING_RULE_V2_00017)
        """
        return self.cse_code  # Delegates to property

    def setCseCode(self, value: "CseCodeType") -> "MultidimensionalTime":
        """
        AUTOSAR-compliant setter for cseCode with method chaining.
        
        Args:
            value: The cseCode to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to cse_code property setter (gets validation automatically)
        """
        self.cse_code = value  # Delegates to property setter
        return self

    def getCseCodeFactor(self) -> "Integer":
        """
        AUTOSAR-compliant getter for cseCodeFactor.
        
        Returns:
            The cseCodeFactor value
        
        Note:
            Delegates to cse_code_factor property (CODING_RULE_V2_00017)
        """
        return self.cse_code_factor  # Delegates to property

    def setCseCodeFactor(self, value: "Integer") -> "MultidimensionalTime":
        """
        AUTOSAR-compliant setter for cseCodeFactor with method chaining.
        
        Args:
            value: The cseCodeFactor to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to cse_code_factor property setter (gets validation automatically)
        """
        self.cse_code_factor = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_cse_code(self, value: Optional["CseCodeType"]) -> "MultidimensionalTime":
        """
        Set cseCode and return self for chaining.
        
        Args:
            value: The cseCode to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_cse_code("value")
        """
        self.cse_code = value  # Use property setter (gets validation)
        return self

    def with_cse_code_factor(self, value: Optional["Integer"]) -> "MultidimensionalTime":
        """
        Set cseCodeFactor and return self for chaining.
        
        Args:
            value: The cseCodeFactor to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_cse_code_factor("value")
        """
        self.cse_code_factor = value  # Use property setter (gets validation)
        return self