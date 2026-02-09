from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class AttributeValueVariationPoint(ARObject, ABC):
    """
    This class represents the ability to derive the value of the Attribute from
    a system constant (by Sw SystemconstDependentFormula). It also provides a
    bindingTime.

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::AttributeValueVariationPoints

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 617, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 209, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 41, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is AttributeValueVariationPoint:
            raise TypeError("AttributeValueVariationPoint is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the binding time in which the attribute value needs bound.
        # attribute is missing, the attribute is not a variation particular this means
                # that It needs to be a single to the type specified in the pure model.
        # It error if it is still a formula.
        self._bindingTime: Optional["BindingTimeEnum"] = None

    @property
    def binding_time(self) -> Optional["BindingTimeEnum"]:
        """Get bindingTime (Pythonic accessor)."""
        return self._bindingTime

    @binding_time.setter
    def binding_time(self, value: Optional["BindingTimeEnum"]) -> None:
        """
        Set bindingTime with validation.

        Args:
            value: The bindingTime to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bindingTime = None
            return

        if not isinstance(value, BindingTimeEnum):
            raise TypeError(
                f"bindingTime must be BindingTimeEnum or None, got {type(value).__name__}"
            )
        self._bindingTime = value
        # objects from the.
        self._blueprintValue: Optional["String"] = None

    @property
    def blueprint_value(self) -> Optional["String"]:
        """Get blueprintValue (Pythonic accessor)."""
        return self._blueprintValue

    @blueprint_value.setter
    def blueprint_value(self, value: Optional["String"]) -> None:
        """
        Set blueprintValue with validation.

        Args:
            value: The blueprintValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._blueprintValue = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"blueprintValue must be String or None, got {type(value).__name__}"
            )
        self._blueprintValue = value
        # with variant management usage is subject of agreement between the.
        self._sd: Optional["String"] = None

    @property
    def sd(self) -> Optional["String"]:
        """Get sd (Pythonic accessor)."""
        return self._sd

    @sd.setter
    def sd(self, value: Optional["String"]) -> None:
        """
        Set sd with validation.

        Args:
            value: The sd to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sd = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"sd must be String or None, got {type(value).__name__}"
            )
        self._sd = value
        # It is also allow RTE support for CompileTime Variation.
        self._shortLabel: Optional["PrimitiveIdentifier"] = None

    @property
    def short_label(self) -> Optional["PrimitiveIdentifier"]:
        """Get shortLabel (Pythonic accessor)."""
        return self._shortLabel

    @short_label.setter
    def short_label(self, value: Optional["PrimitiveIdentifier"]) -> None:
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

        if not isinstance(value, PrimitiveIdentifier):
            raise TypeError(
                f"shortLabel must be PrimitiveIdentifier or None, got {type(value).__name__}"
            )
        self._shortLabel = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBindingTime(self) -> "BindingTimeEnum":
        """
        AUTOSAR-compliant getter for bindingTime.

        Returns:
            The bindingTime value

        Note:
            Delegates to binding_time property (CODING_RULE_V2_00017)
        """
        return self.binding_time  # Delegates to property

    def setBindingTime(self, value: "BindingTimeEnum") -> "AttributeValueVariationPoint":
        """
        AUTOSAR-compliant setter for bindingTime with method chaining.

        Args:
            value: The bindingTime to set

        Returns:
            self for method chaining

        Note:
            Delegates to binding_time property setter (gets validation automatically)
        """
        self.binding_time = value  # Delegates to property setter
        return self

    def getBlueprintValue(self) -> "String":
        """
        AUTOSAR-compliant getter for blueprintValue.

        Returns:
            The blueprintValue value

        Note:
            Delegates to blueprint_value property (CODING_RULE_V2_00017)
        """
        return self.blueprint_value  # Delegates to property

    def setBlueprintValue(self, value: "String") -> "AttributeValueVariationPoint":
        """
        AUTOSAR-compliant setter for blueprintValue with method chaining.

        Args:
            value: The blueprintValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to blueprint_value property setter (gets validation automatically)
        """
        self.blueprint_value = value  # Delegates to property setter
        return self

    def getSd(self) -> "String":
        """
        AUTOSAR-compliant getter for sd.

        Returns:
            The sd value

        Note:
            Delegates to sd property (CODING_RULE_V2_00017)
        """
        return self.sd  # Delegates to property

    def setSd(self, value: "String") -> "AttributeValueVariationPoint":
        """
        AUTOSAR-compliant setter for sd with method chaining.

        Args:
            value: The sd to set

        Returns:
            self for method chaining

        Note:
            Delegates to sd property setter (gets validation automatically)
        """
        self.sd = value  # Delegates to property setter
        return self

    def getShortLabel(self) -> "PrimitiveIdentifier":
        """
        AUTOSAR-compliant getter for shortLabel.

        Returns:
            The shortLabel value

        Note:
            Delegates to short_label property (CODING_RULE_V2_00017)
        """
        return self.short_label  # Delegates to property

    def setShortLabel(self, value: "PrimitiveIdentifier") -> "AttributeValueVariationPoint":
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

    def with_binding_time(self, value: Optional["BindingTimeEnum"]) -> "AttributeValueVariationPoint":
        """
        Set bindingTime and return self for chaining.

        Args:
            value: The bindingTime to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_binding_time("value")
        """
        self.binding_time = value  # Use property setter (gets validation)
        return self

    def with_blueprint_value(self, value: Optional["String"]) -> "AttributeValueVariationPoint":
        """
        Set blueprintValue and return self for chaining.

        Args:
            value: The blueprintValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_blueprint_value("value")
        """
        self.blueprint_value = value  # Use property setter (gets validation)
        return self

    def with_sd(self, value: Optional["String"]) -> "AttributeValueVariationPoint":
        """
        Set sd and return self for chaining.

        Args:
            value: The sd to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sd("value")
        """
        self.sd = value  # Use property setter (gets validation)
        return self

    def with_short_label(self, value: Optional["PrimitiveIdentifier"]) -> "AttributeValueVariationPoint":
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
