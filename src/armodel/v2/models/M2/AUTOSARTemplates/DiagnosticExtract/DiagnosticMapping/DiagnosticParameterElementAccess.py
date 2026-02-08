from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import DiagnosticParameter
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class DiagnosticParameterElementAccess(ARObject):
    """
    This meta-class acts as a single point for defining structured references to
    a specific Diagnostic ParameterElement.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::ServiceMapping::DiagnosticParameterElementAccess

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 229, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the context of an applicable payload that corresponds to the
        # referenced DataPrototype in the role.
        self._contextElement: List["DiagnosticParameter"] = []

    @property
    def context_element(self) -> List["DiagnosticParameter"]:
        """Get contextElement (Pythonic accessor)."""
        return self._contextElement
        # This represents the target reference of an applicable that corresponds to the
        # referenced Data the role mappedDataElement.
        self._targetElement: Optional["DiagnosticParameter"] = None

    @property
    def target_element(self) -> Optional["DiagnosticParameter"]:
        """Get targetElement (Pythonic accessor)."""
        return self._targetElement

    @target_element.setter
    def target_element(self, value: Optional["DiagnosticParameter"]) -> None:
        """
        Set targetElement with validation.

        Args:
            value: The targetElement to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetElement = None
            return

        if not isinstance(value, DiagnosticParameter):
            raise TypeError(
                f"targetElement must be DiagnosticParameter or None, got {type(value).__name__}"
            )
        self._targetElement = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getContextElement(self) -> List["DiagnosticParameter"]:
        """
        AUTOSAR-compliant getter for contextElement.

        Returns:
            The contextElement value

        Note:
            Delegates to context_element property (CODING_RULE_V2_00017)
        """
        return self.context_element  # Delegates to property

    def getTargetElement(self) -> "DiagnosticParameter":
        """
        AUTOSAR-compliant getter for targetElement.

        Returns:
            The targetElement value

        Note:
            Delegates to target_element property (CODING_RULE_V2_00017)
        """
        return self.target_element  # Delegates to property

    def setTargetElement(self, value: "DiagnosticParameter") -> "DiagnosticParameterElementAccess":
        """
        AUTOSAR-compliant setter for targetElement with method chaining.

        Args:
            value: The targetElement to set

        Returns:
            self for method chaining

        Note:
            Delegates to target_element property setter (gets validation automatically)
        """
        self.target_element = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_target_element(self, value: Optional["DiagnosticParameter"]) -> "DiagnosticParameterElementAccess":
        """
        Set targetElement and return self for chaining.

        Args:
            value: The targetElement to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target_element("value")
        """
        self.target_element = value  # Use property setter (gets validation)
        return self
