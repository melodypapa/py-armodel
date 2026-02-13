"""
AUTOSAR Package - AnyInstanceRef

Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::AnyInstanceRef
"""


from __future__ import annotations
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import (
    AtpClassifier,
    AtpFeature,
)


class AnyInstanceRef(ARObject):
    """
    Describes a reference to any instance in an AUTOSAR model. This is the most
    generic form of an instance ref. Refer to the superclass notes for more
    details.

    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::AnyInstanceRef::AnyInstanceRef

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 289, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 970, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 1995, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 328, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

        # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the base from which navigation path begins.
        self._base: Optional[AtpClassifier] = None
        # This is the context element for the instance ref.
        self._contextElement: List[AtpFeature] = []
        # This is the target of the instance ref.
        self._target: Optional[AtpFeature] = None

    @property
    def base(self) -> Optional[AtpClassifier]:
        """Get base (Pythonic accessor)."""
        return self._base

    @base.setter
    def base(self, value: Optional[AtpClassifier]) -> None:
        """
        Set base with validation.

        Args:
            value: The base to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._base = None
            return

        if not isinstance(value, AtpClassifier):
            raise TypeError(
                f"base must be AtpClassifier or None, got {type(value).__name__}"
            )
        self._base = value

    @property
    def context_element(self) -> List[AtpFeature]:
        """Get contextElement (Pythonic accessor)."""
        return self._contextElement

    @property
    def target(self) -> Optional[AtpFeature]:
        """Get target (Pythonic accessor)."""
        return self._target

    @target.setter
    def target(self, value: Optional[AtpFeature]) -> None:
        """
        Set target with validation.

        Args:
            value: The target to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._target = None
            return

        if not isinstance(value, AtpFeature):
            raise TypeError(
                f"target must be AtpFeature or None, got {type(value).__name__}"
            )
        self._target = value

    def with_context_element(self, value):
        """
        Set context_element and return self for chaining.

        Args:
            value: The context_element to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context_element("value")
        """
        self.context_element = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBase(self) -> Optional[AtpClassifier]:
        """
        AUTOSAR-compliant getter for base.

        Returns:
            The base value

        Note:
            Delegates to base property (CODING_RULE_V2_00017)
        """
        return self.base  # Delegates to property

    def setBase(self, value: Optional[AtpClassifier]) -> AnyInstanceRef:
        """
        AUTOSAR-compliant setter for base with method chaining.

        Args:
            value: The base to set

        Returns:
            self for method chaining

        Note:
            Delegates to base property setter (gets validation automatically)
        """
        self.base = value  # Delegates to property setter
        return self

    def getContextElement(self) -> List[AtpFeature]:
        """
        AUTOSAR-compliant getter for contextElement.

        Returns:
            The contextElement value

        Note:
            Delegates to context_element property (CODING_RULE_V2_00017)
        """
        return self.context_element  # Delegates to property

    def getTarget(self) -> Optional[AtpFeature]:
        """
        AUTOSAR-compliant getter for target.

        Returns:
            The target value

        Note:
            Delegates to target property (CODING_RULE_V2_00017)
        """
        return self.target  # Delegates to property

    def setTarget(self, value: Optional[AtpFeature]) -> AnyInstanceRef:
        """
        AUTOSAR-compliant setter for target with method chaining.

        Args:
            value: The target to set

        Returns:
            self for method chaining

        Note:
            Delegates to target property setter (gets validation automatically)
        """
        self.target = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_base(self, value: Optional[AtpClassifier]) -> AnyInstanceRef:
        """
        Set base and return self for chaining.

        Args:
            value: The base to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_base("value")
        """
        self.base = value  # Use property setter (gets validation)
        return self

    def with_target(self, value: Optional[AtpFeature]) -> AnyInstanceRef:
        """
        Set target and return self for chaining.

        Args:
            value: The target to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target("value")
        """
        self.target = value  # Use property setter (gets validation)
        return self
