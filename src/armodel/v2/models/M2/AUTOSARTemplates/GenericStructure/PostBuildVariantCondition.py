from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class PostBuildVariantCondition(ARObject):
    """
    This class specifies the value which shall be assigned to a particular
    variant criterion in order to bind the variation point. If multiple
    criterion/value pairs are specified, they shall all match to bind the
    variation point. In other words binding can be represented by (criterion1 ==
    value1) && (condition2 == value2) ...

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 614, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 76, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 232, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the criterion which needs to match the value in order to make the
        # PostbuildVariantCondition to be true.
        self._matching: "PostBuildVariant" = None

    @property
    def matching(self) -> "PostBuildVariant":
        """Get matching (Pythonic accessor)."""
        return self._matching

    @matching.setter
    def matching(self, value: "PostBuildVariant") -> None:
        """
        Set matching with validation.

        Args:
            value: The matching to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, PostBuildVariant):
            raise TypeError(
                f"matching must be PostBuildVariant, got {type(value).__name__}"
            )
        self._matching = value
        # This is the particular value of the post-build variant.
        self._value: "Integer" = None

    @property
    def value(self) -> "Integer":
        """Get value (Pythonic accessor)."""
        return self._value

    @value.setter
    def value(self, value: "Integer") -> None:
        """
        Set value with validation.

        Args:
            value: The value to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, Integer):
            raise TypeError(
                f"value must be Integer, got {type(value).__name__}"
            )
        self._value = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMatching(self) -> "PostBuildVariant":
        """
        AUTOSAR-compliant getter for matching.

        Returns:
            The matching value

        Note:
            Delegates to matching property (CODING_RULE_V2_00017)
        """
        return self.matching  # Delegates to property

    def setMatching(self, value: "PostBuildVariant") -> "PostBuildVariantCondition":
        """
        AUTOSAR-compliant setter for matching with method chaining.

        Args:
            value: The matching to set

        Returns:
            self for method chaining

        Note:
            Delegates to matching property setter (gets validation automatically)
        """
        self.matching = value  # Delegates to property setter
        return self

    def getValue(self) -> "Integer":
        """
        AUTOSAR-compliant getter for value.

        Returns:
            The value value

        Note:
            Delegates to value property (CODING_RULE_V2_00017)
        """
        return self.value  # Delegates to property

    def setValue(self, value: "Integer") -> "PostBuildVariantCondition":
        """
        AUTOSAR-compliant setter for value with method chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Note:
            Delegates to value property setter (gets validation automatically)
        """
        self.value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_matching(self, value: "PostBuildVariant") -> "PostBuildVariantCondition":
        """
        Set matching and return self for chaining.

        Args:
            value: The matching to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_matching("value")
        """
        self.matching = value  # Use property setter (gets validation)
        return self

    def with_value(self, value: "Integer") -> "PostBuildVariantCondition":
        """
        Set value and return self for chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_value("value")
        """
        self.value = value  # Use property setter (gets validation)
        return self
