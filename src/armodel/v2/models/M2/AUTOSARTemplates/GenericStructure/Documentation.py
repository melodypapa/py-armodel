from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    DocumentationContext,
    PredefinedChapter,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    ARElement,
)


class Documentation(ARElement):
    """
    This meta-class represents the ability to handle a so called standalone
    documentation. Standalone means, that such a documentation is not embedded
    in another ARElement or identifiable object. The standalone documentation is
    an entity of its own which denotes its context by reference to other objects
    and instances.

    Package: M2::AUTOSARTemplates::GenericStructure::DocumentationOnM1::Documentation

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 294, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 439, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 181, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the context of the particular documentation.
        self._context: List["DocumentationContext"] = []

    @property
    def context(self) -> List["DocumentationContext"]:
        """Get context (Pythonic accessor)."""
        return self._context
        # This is the content of the documentation related to the contexts.
        self._documentation: Optional["PredefinedChapter"] = None

    @property
    def documentation(self) -> Optional["PredefinedChapter"]:
        """Get documentation (Pythonic accessor)."""
        return self._documentation

    @documentation.setter
    def documentation(self, value: Optional["PredefinedChapter"]) -> None:
        """
        Set documentation with validation.

        Args:
            value: The documentation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._documentation = None
            return

        if not isinstance(value, PredefinedChapter):
            raise TypeError(
                f"documentation must be PredefinedChapter or None, got {type(value).__name__}"
            )
        self._documentation = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getContext(self) -> List["DocumentationContext"]:
        """
        AUTOSAR-compliant getter for context.

        Returns:
            The context value

        Note:
            Delegates to context property (CODING_RULE_V2_00017)
        """
        return self.context  # Delegates to property

    def getDocumentation(self) -> "PredefinedChapter":
        """
        AUTOSAR-compliant getter for documentation.

        Returns:
            The documentation value

        Note:
            Delegates to documentation property (CODING_RULE_V2_00017)
        """
        return self.documentation  # Delegates to property

    def setDocumentation(self, value: "PredefinedChapter") -> "Documentation":
        """
        AUTOSAR-compliant setter for documentation with method chaining.

        Args:
            value: The documentation to set

        Returns:
            self for method chaining

        Note:
            Delegates to documentation property setter (gets validation automatically)
        """
        self.documentation = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_documentation(self, value: Optional["PredefinedChapter"]) -> "Documentation":
        """
        Set documentation and return self for chaining.

        Args:
            value: The documentation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_documentation("value")
        """
        self.documentation = value  # Use property setter (gets validation)
        return self
