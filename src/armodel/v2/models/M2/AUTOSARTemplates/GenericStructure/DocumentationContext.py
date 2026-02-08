from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import AtpFeature
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultilanguageReferrable import (
    MultilanguageReferrable,
)


class DocumentationContext(MultilanguageReferrable):
    """
    This class represents the ability to denote a context of a so called
    standalone documentation. Note that this is an <<atpMixed>>. The contents
    needs to be considered as ordered.

    Package: M2::AUTOSARTemplates::GenericStructure::DocumentationOnM1::DocumentationContext

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 327, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # which is the context of the documentation.
        # by: AnyInstanceRef.
        self._feature: Optional["AtpFeature"] = None

    @property
    def feature(self) -> Optional["AtpFeature"]:
        """Get feature (Pythonic accessor)."""
        return self._feature

    @feature.setter
    def feature(self, value: Optional["AtpFeature"]) -> None:
        """
        Set feature with validation.

        Args:
            value: The feature to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._feature = None
            return

        if not isinstance(value, AtpFeature):
            raise TypeError(
                f"feature must be AtpFeature or None, got {type(value).__name__}"
            )
        self._feature = value
        # This is an identifiable object which is part of the context of.
        self._identifiable: Optional["Identifiable"] = None

    @property
    def identifiable(self) -> Optional["Identifiable"]:
        """Get identifiable (Pythonic accessor)."""
        return self._identifiable

    @identifiable.setter
    def identifiable(self, value: Optional["Identifiable"]) -> None:
        """
        Set identifiable with validation.

        Args:
            value: The identifiable to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._identifiable = None
            return

        if not isinstance(value, Identifiable):
            raise TypeError(
                f"identifiable must be Identifiable or None, got {type(value).__name__}"
            )
        self._identifiable = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFeature(self) -> "AtpFeature":
        """
        AUTOSAR-compliant getter for feature.

        Returns:
            The feature value

        Note:
            Delegates to feature property (CODING_RULE_V2_00017)
        """
        return self.feature  # Delegates to property

    def setFeature(self, value: "AtpFeature") -> "DocumentationContext":
        """
        AUTOSAR-compliant setter for feature with method chaining.

        Args:
            value: The feature to set

        Returns:
            self for method chaining

        Note:
            Delegates to feature property setter (gets validation automatically)
        """
        self.feature = value  # Delegates to property setter
        return self

    def getIdentifiable(self) -> "Identifiable":
        """
        AUTOSAR-compliant getter for identifiable.

        Returns:
            The identifiable value

        Note:
            Delegates to identifiable property (CODING_RULE_V2_00017)
        """
        return self.identifiable  # Delegates to property

    def setIdentifiable(self, value: "Identifiable") -> "DocumentationContext":
        """
        AUTOSAR-compliant setter for identifiable with method chaining.

        Args:
            value: The identifiable to set

        Returns:
            self for method chaining

        Note:
            Delegates to identifiable property setter (gets validation automatically)
        """
        self.identifiable = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_feature(self, value: Optional["AtpFeature"]) -> "DocumentationContext":
        """
        Set feature and return self for chaining.

        Args:
            value: The feature to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_feature("value")
        """
        self.feature = value  # Use property setter (gets validation)
        return self

    def with_identifiable(self, value: Optional["Identifiable"]) -> "DocumentationContext":
        """
        Set identifiable and return self for chaining.

        Args:
            value: The identifiable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_identifiable("value")
        """
        self.identifiable = value  # Use property setter (gets validation)
        return self
