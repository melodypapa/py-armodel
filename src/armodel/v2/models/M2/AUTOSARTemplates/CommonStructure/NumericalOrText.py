from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class NumericalOrText(ARObject):
    """
    This meta-class represents the ability to yield either a numerical or a
    string. A typical use case is that two or more instances of this meta-class
    are aggregated with a VariationPoint where some instances yield strings
    while other instances yield numerical depending on the resolution of the
    binding expression.
    
    Package: M2::AUTOSARTemplates::CommonStructure::Constants::NumericalOrText
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 323, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 455, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represents the ability to provide a numerical latest binding
        # time of the VariationPoint shall.
        self._vf: Optional["Numerical"] = None

    @property
    def vf(self) -> Optional["Numerical"]:
        """Get vf (Pythonic accessor)."""
        return self._vf

    @vf.setter
    def vf(self, value: Optional["Numerical"]) -> None:
        """
        Set vf with validation.
        
        Args:
            value: The vf to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._vf = None
            return

        if not isinstance(value, Numerical):
            raise TypeError(
                f"vf must be Numerical or None, got {type(value).__name__}"
            )
        self._vf = value
        # This attribute represents the ability to provide a textual.
        self._vt: Optional["String"] = None

    @property
    def vt(self) -> Optional["String"]:
        """Get vt (Pythonic accessor)."""
        return self._vt

    @vt.setter
    def vt(self, value: Optional["String"]) -> None:
        """
        Set vt with validation.
        
        Args:
            value: The vt to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._vt = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"vt must be String or None, got {type(value).__name__}"
            )
        self._vt = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getVf(self) -> "Numerical":
        """
        AUTOSAR-compliant getter for vf.
        
        Returns:
            The vf value
        
        Note:
            Delegates to vf property (CODING_RULE_V2_00017)
        """
        return self.vf  # Delegates to property

    def setVf(self, value: "Numerical") -> "NumericalOrText":
        """
        AUTOSAR-compliant setter for vf with method chaining.
        
        Args:
            value: The vf to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to vf property setter (gets validation automatically)
        """
        self.vf = value  # Delegates to property setter
        return self

    def getVt(self) -> "String":
        """
        AUTOSAR-compliant getter for vt.
        
        Returns:
            The vt value
        
        Note:
            Delegates to vt property (CODING_RULE_V2_00017)
        """
        return self.vt  # Delegates to property

    def setVt(self, value: "String") -> "NumericalOrText":
        """
        AUTOSAR-compliant setter for vt with method chaining.
        
        Args:
            value: The vt to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to vt property setter (gets validation automatically)
        """
        self.vt = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_vf(self, value: Optional["Numerical"]) -> "NumericalOrText":
        """
        Set vf and return self for chaining.
        
        Args:
            value: The vf to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_vf("value")
        """
        self.vf = value  # Use property setter (gets validation)
        return self

    def with_vt(self, value: Optional["String"]) -> "NumericalOrText":
        """
        Set vt and return self for chaining.
        
        Args:
            value: The vt to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_vt("value")
        """
        self.vt = value  # Use property setter (gets validation)
        return self