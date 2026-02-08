from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class BlueprintPolicy(ARObject, ABC):
    """
    This meta-class represents the ability to indicate whether blueprintable
    elements will be modifiable or not modifiable. (cid:53) 163 of 238 Document
    ID 535: AUTOSAR_FO_TPS_StandardizationTemplate Standardization Template
    AUTOSAR FO R23-11 (cid:52)

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::AbstractBlueprintStructure::BlueprintPolicy

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 163, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is BlueprintPolicy:
            raise TypeError("BlueprintPolicy is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This identifies the related attribute of a BlueprintPolicy.
        # over the model a subset of xpath used.
        self._attributeName: "String" = None

    @property
    def attribute_name(self) -> "String":
        """Get attributeName (Pythonic accessor)."""
        return self._attributeName

    @attribute_name.setter
    def attribute_name(self, value: "String") -> None:
        """
        Set attributeName with validation.

        Args:
            value: The attributeName to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, String):
            raise TypeError(
                f"attributeName must be String, got {type(value).__name__}"
            )
        self._attributeName = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAttributeName(self) -> "String":
        """
        AUTOSAR-compliant getter for attributeName.

        Returns:
            The attributeName value

        Note:
            Delegates to attribute_name property (CODING_RULE_V2_00017)
        """
        return self.attribute_name  # Delegates to property

    def setAttributeName(self, value: "String") -> "BlueprintPolicy":
        """
        AUTOSAR-compliant setter for attributeName with method chaining.

        Args:
            value: The attributeName to set

        Returns:
            self for method chaining

        Note:
            Delegates to attribute_name property setter (gets validation automatically)
        """
        self.attribute_name = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_attribute_name(self, value: "String") -> "BlueprintPolicy":
        """
        Set attributeName and return self for chaining.

        Args:
            value: The attributeName to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_attribute_name("value")
        """
        self.attribute_name = value  # Use property setter (gets validation)
        return self
