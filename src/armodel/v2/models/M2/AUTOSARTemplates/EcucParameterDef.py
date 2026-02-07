from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class EcucParameterDef(EcucCommonAttributes, ABC):
    """
    Abstract class used to define the similarities of all ECU Configuration
    Parameter types defined as subclasses.
    
    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucParameterDef
    
    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 57, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 188, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is EcucParameterDef:
            raise TypeError("EcucParameterDef is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # A derivation of a Configuration Parameter value can be by an informal
        # Calculation Formula or by a that can be used to specify the.
        self._derivation: Optional["EcucDerivation"] = None

    @property
    def derivation(self) -> Optional["EcucDerivation"]:
        """Get derivation (Pythonic accessor)."""
        return self._derivation

    @derivation.setter
    def derivation(self, value: Optional["EcucDerivation"]) -> None:
        """
        Set derivation with validation.
        
        Args:
            value: The derivation to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._derivation = None
            return

        if not isinstance(value, EcucDerivation):
            raise TypeError(
                f"derivation must be EcucDerivation or None, got {type(value).__name__}"
            )
        self._derivation = value
        # Specifies that this parameter’s value is used, together the aggregating
        # container, to derive a symbolic name chapter "Representation of Symbolic Ecuc
        # specification for more details.
        self._symbolicName: Optional["Boolean"] = None

    @property
    def symbolic_name(self) -> Optional["Boolean"]:
        """Get symbolicName (Pythonic accessor)."""
        return self._symbolicName

    @symbolic_name.setter
    def symbolic_name(self, value: Optional["Boolean"]) -> None:
        """
        Set symbolicName with validation.
        
        Args:
            value: The symbolicName to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._symbolicName = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"symbolicName must be Boolean or None, got {type(value).__name__}"
            )
        self._symbolicName = value
        # Specifies whether it shall be allowed on the value side to parameter value as
                # "AUTO".
        # is "true" it shall be possible to set the "isAuto of the respective parameter
                # to "true".
        # This the actual value will not be considered during but will be
                # (re-)calculated by the code stored in the value attribute afterwards.
        # updated values might require a other modules which reference these is "false"
                # it shall not be possible to set the "is of the respective parameter to
                # "true".
        # is not present the default is "false".
        self._withAuto: Optional["Boolean"] = None

    @property
    def with_auto(self) -> Optional["Boolean"]:
        """Get withAuto (Pythonic accessor)."""
        return self._withAuto

    @with_auto.setter
    def with_auto(self, value: Optional["Boolean"]) -> None:
        """
        Set withAuto with validation.
        
        Args:
            value: The withAuto to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._withAuto = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"withAuto must be Boolean or None, got {type(value).__name__}"
            )
        self._withAuto = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDerivation(self) -> "EcucDerivation":
        """
        AUTOSAR-compliant getter for derivation.
        
        Returns:
            The derivation value
        
        Note:
            Delegates to derivation property (CODING_RULE_V2_00017)
        """
        return self.derivation  # Delegates to property

    def setDerivation(self, value: "EcucDerivation") -> "EcucParameterDef":
        """
        AUTOSAR-compliant setter for derivation with method chaining.
        
        Args:
            value: The derivation to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to derivation property setter (gets validation automatically)
        """
        self.derivation = value  # Delegates to property setter
        return self

    def getSymbolicName(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for symbolicName.
        
        Returns:
            The symbolicName value
        
        Note:
            Delegates to symbolic_name property (CODING_RULE_V2_00017)
        """
        return self.symbolic_name  # Delegates to property

    def setSymbolicName(self, value: "Boolean") -> "EcucParameterDef":
        """
        AUTOSAR-compliant setter for symbolicName with method chaining.
        
        Args:
            value: The symbolicName to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to symbolic_name property setter (gets validation automatically)
        """
        self.symbolic_name = value  # Delegates to property setter
        return self

    def getWithAuto(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for withAuto.
        
        Returns:
            The withAuto value
        
        Note:
            Delegates to with_auto property (CODING_RULE_V2_00017)
        """
        return self.with_auto  # Delegates to property

    def setWithAuto(self, value: "Boolean") -> "EcucParameterDef":
        """
        AUTOSAR-compliant setter for withAuto with method chaining.
        
        Args:
            value: The withAuto to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to with_auto property setter (gets validation automatically)
        """
        self.with_auto = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_derivation(self, value: Optional["EcucDerivation"]) -> "EcucParameterDef":
        """
        Set derivation and return self for chaining.
        
        Args:
            value: The derivation to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_derivation("value")
        """
        self.derivation = value  # Use property setter (gets validation)
        return self

    def with_symbolic_name(self, value: Optional["Boolean"]) -> "EcucParameterDef":
        """
        Set symbolicName and return self for chaining.
        
        Args:
            value: The symbolicName to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_symbolic_name("value")
        """
        self.symbolic_name = value  # Use property setter (gets validation)
        return self

    def with_with_auto(self, value: Optional["Boolean"]) -> "EcucParameterDef":
        """
        Set withAuto and return self for chaining.
        
        Args:
            value: The withAuto to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_with_auto("value")
        """
        self.with_auto = value  # Use property setter (gets validation)
        return self