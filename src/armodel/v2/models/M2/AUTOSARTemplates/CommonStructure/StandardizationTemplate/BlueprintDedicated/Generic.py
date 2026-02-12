"""
AUTOSAR Package - Generic

Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::BlueprintDedicated::Generic
"""


from __future__ import annotations
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class BlueprintMapping(ARObject):
    """
    This meta-class represents the ability to map two an object and its
    blueprint.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::BlueprintDedicated::Generic::BlueprintMapping

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 163, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the mapped blueprint.
        self._blueprint: "AtpBlueprint" = None

    @property
    def blueprint(self) -> "AtpBlueprint":
        """Get blueprint (Pythonic accessor)."""
        return self._blueprint

    @blueprint.setter
    def blueprint(self, value: "AtpBlueprint") -> None:
        """
        Set blueprint with validation.

        Args:
            value: The blueprint to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, AtpBlueprint):
            raise TypeError(
                f"blueprint must be AtpBlueprint, got {type(value).__name__}"
            )
        self._blueprint = value
        self._derivedObject: "AtpBlueprintable" = None

    @property
    def derived_object(self) -> "AtpBlueprintable":
        """Get derivedObject (Pythonic accessor)."""
        return self._derivedObject

    @derived_object.setter
    def derived_object(self, value: "AtpBlueprintable") -> None:
        """
        Set derivedObject with validation.

        Args:
            value: The derivedObject to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, AtpBlueprintable):
            raise TypeError(
                f"derivedObject must be AtpBlueprintable, got {type(value).__name__}"
            )
        self._derivedObject = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBlueprint(self) -> "AtpBlueprint":
        """
        AUTOSAR-compliant getter for blueprint.

        Returns:
            The blueprint value

        Note:
            Delegates to blueprint property (CODING_RULE_V2_00017)
        """
        return self.blueprint  # Delegates to property

    def setBlueprint(self, value: "AtpBlueprint") -> BlueprintMapping:
        """
        AUTOSAR-compliant setter for blueprint with method chaining.

        Args:
            value: The blueprint to set

        Returns:
            self for method chaining

        Note:
            Delegates to blueprint property setter (gets validation automatically)
        """
        self.blueprint = value  # Delegates to property setter
        return self

    def getDerivedObject(self) -> "AtpBlueprintable":
        """
        AUTOSAR-compliant getter for derivedObject.

        Returns:
            The derivedObject value

        Note:
            Delegates to derived_object property (CODING_RULE_V2_00017)
        """
        return self.derived_object  # Delegates to property

    def setDerivedObject(self, value: "AtpBlueprintable") -> BlueprintMapping:
        """
        AUTOSAR-compliant setter for derivedObject with method chaining.

        Args:
            value: The derivedObject to set

        Returns:
            self for method chaining

        Note:
            Delegates to derived_object property setter (gets validation automatically)
        """
        self.derived_object = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_blueprint(self, value: "AtpBlueprint") -> BlueprintMapping:
        """
        Set blueprint and return self for chaining.

        Args:
            value: The blueprint to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_blueprint("value")
        """
        self.blueprint = value  # Use property setter (gets validation)
        return self

    def with_derived_object(self, value: "AtpBlueprintable") -> BlueprintMapping:
        """
        Set derivedObject and return self for chaining.

        Args:
            value: The derivedObject to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_derived_object("value")
        """
        self.derived_object = value  # Use property setter (gets validation)
        return self
