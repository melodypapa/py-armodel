from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class EcucAbstractConfigurationClass(ARObject, ABC):
    """
    Specifies the ValueConfigurationClass of a parameter/reference or the
    MultiplicityConfigurationClass of a parameter/reference or a container for
    each ConfigurationVariant of the EcucModuleDef.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucAbstractConfigurationClass

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 51, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is EcucAbstractConfigurationClass:
            raise TypeError("EcucAbstractConfigurationClass is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the ConfigurationClass for the given.
        self._configClass: Optional["EcucConfigurationClass"] = None

    @property
    def config_class(self) -> Optional["EcucConfigurationClass"]:
        """Get configClass (Pythonic accessor)."""
        return self._configClass

    @config_class.setter
    def config_class(self, value: Optional["EcucConfigurationClass"]) -> None:
        """
        Set configClass with validation.

        Args:
            value: The configClass to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._configClass = None
            return

        if not isinstance(value, EcucConfigurationClass):
            raise TypeError(
                f"configClass must be EcucConfigurationClass or None, got {type(value).__name__}"
            )
        self._configClass = value
        # Specifies the ConfigurationVariant the ConfigurationClass specified for.
        self._configVariant: Optional["EcucConfiguration"] = None

    @property
    def config_variant(self) -> Optional["EcucConfiguration"]:
        """Get configVariant (Pythonic accessor)."""
        return self._configVariant

    @config_variant.setter
    def config_variant(self, value: Optional["EcucConfiguration"]) -> None:
        """
        Set configVariant with validation.

        Args:
            value: The configVariant to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._configVariant = None
            return

        if not isinstance(value, EcucConfiguration):
            raise TypeError(
                f"configVariant must be EcucConfiguration or None, got {type(value).__name__}"
            )
        self._configVariant = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConfigClass(self) -> "EcucConfigurationClass":
        """
        AUTOSAR-compliant getter for configClass.

        Returns:
            The configClass value

        Note:
            Delegates to config_class property (CODING_RULE_V2_00017)
        """
        return self.config_class  # Delegates to property

    def setConfigClass(self, value: "EcucConfigurationClass") -> "EcucAbstractConfigurationClass":
        """
        AUTOSAR-compliant setter for configClass with method chaining.

        Args:
            value: The configClass to set

        Returns:
            self for method chaining

        Note:
            Delegates to config_class property setter (gets validation automatically)
        """
        self.config_class = value  # Delegates to property setter
        return self

    def getConfigVariant(self) -> "EcucConfiguration":
        """
        AUTOSAR-compliant getter for configVariant.

        Returns:
            The configVariant value

        Note:
            Delegates to config_variant property (CODING_RULE_V2_00017)
        """
        return self.config_variant  # Delegates to property

    def setConfigVariant(self, value: "EcucConfiguration") -> "EcucAbstractConfigurationClass":
        """
        AUTOSAR-compliant setter for configVariant with method chaining.

        Args:
            value: The configVariant to set

        Returns:
            self for method chaining

        Note:
            Delegates to config_variant property setter (gets validation automatically)
        """
        self.config_variant = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_config_class(self, value: Optional["EcucConfigurationClass"]) -> "EcucAbstractConfigurationClass":
        """
        Set configClass and return self for chaining.

        Args:
            value: The configClass to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_config_class("value")
        """
        self.config_class = value  # Use property setter (gets validation)
        return self

    def with_config_variant(self, value: Optional["EcucConfiguration"]) -> "EcucAbstractConfigurationClass":
        """
        Set configVariant and return self for chaining.

        Args:
            value: The configVariant to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_config_variant("value")
        """
        self.config_variant = value  # Use property setter (gets validation)
        return self
