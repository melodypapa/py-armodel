from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class EcucQueryExpression(ARObject):
    """
    Defines a query expression to the ECUC Description and output the result as
    an numerical value. Due to the "mixedString" nature of the formula there can
    be several EcuQueryExpressions used.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 89, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The EcucQueryExpression points to an EcucDefinition that is used to find an
                # element in the Ecuc order to find the right element in the Ecuc search is
                # necessary.
        # If the search is of the same module that contains the local reference shall
                # be used.
        # Due to the of the EcucQueryExpression several EcucDefintionElements can be
                # used in one.
        self._configElement: Optional["EcucDefinitionElement"] = None

    @property
    def config_element(self) -> Optional["EcucDefinitionElement"]:
        """Get configElement (Pythonic accessor)."""
        return self._configElement

    @config_element.setter
    def config_element(self, value: Optional["EcucDefinitionElement"]) -> None:
        """
        Set configElement with validation.

        Args:
            value: The configElement to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._configElement = None
            return

        if not isinstance(value, EcucDefinitionElement):
            raise TypeError(
                f"configElement must be EcucDefinitionElement or None, got {type(value).__name__}"
            )
        self._configElement = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConfigElement(self) -> "EcucDefinitionElement":
        """
        AUTOSAR-compliant getter for configElement.

        Returns:
            The configElement value

        Note:
            Delegates to config_element property (CODING_RULE_V2_00017)
        """
        return self.config_element  # Delegates to property

    def setConfigElement(self, value: "EcucDefinitionElement") -> "EcucQueryExpression":
        """
        AUTOSAR-compliant setter for configElement with method chaining.

        Args:
            value: The configElement to set

        Returns:
            self for method chaining

        Note:
            Delegates to config_element property setter (gets validation automatically)
        """
        self.config_element = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_config_element(self, value: Optional["EcucDefinitionElement"]) -> "EcucQueryExpression":
        """
        Set configElement and return self for chaining.

        Args:
            value: The configElement to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_config_element("value")
        """
        self.config_element = value  # Use property setter (gets validation)
        return self
