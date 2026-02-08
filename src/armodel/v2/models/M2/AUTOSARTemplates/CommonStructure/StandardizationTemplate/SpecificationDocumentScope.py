from typing import List, Optional
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common import SpecElementReference


class SpecificationDocumentScope(SpecElementReference):
    """
    Represents a standardized or custom specification document such as Software
    Component Template, Main Requirements, Specification of Communication, etc.
    Autosar specifications are referenced via their title.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchange::SpecificationDocumentScope

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 97, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # reference to a custom defined specification.
        self._customDocumentation: Optional["Documentation"] = None

    @property
    def custom_documentation(self) -> Optional["Documentation"]:
        """Get customDocumentation (Pythonic accessor)."""
        return self._customDocumentation

    @custom_documentation.setter
    def custom_documentation(self, value: Optional["Documentation"]) -> None:
        """
        Set customDocumentation with validation.

        Args:
            value: The customDocumentation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._customDocumentation = None
            return

        if not isinstance(value, Documentation):
            raise TypeError(
                f"customDocumentation must be Documentation or None, got {type(value).__name__}"
            )
        self._customDocumentation = value
        # An element with a name or ID that is specified in the Specification Document.
        self._document: List["DocumentElement"] = []

    @property
    def document(self) -> List["DocumentElement"]:
        """Get document (Pythonic accessor)."""
        return self._document

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCustomDocumentation(self) -> "Documentation":
        """
        AUTOSAR-compliant getter for customDocumentation.

        Returns:
            The customDocumentation value

        Note:
            Delegates to custom_documentation property (CODING_RULE_V2_00017)
        """
        return self.custom_documentation  # Delegates to property

    def setCustomDocumentation(self, value: "Documentation") -> "SpecificationDocumentScope":
        """
        AUTOSAR-compliant setter for customDocumentation with method chaining.

        Args:
            value: The customDocumentation to set

        Returns:
            self for method chaining

        Note:
            Delegates to custom_documentation property setter (gets validation automatically)
        """
        self.custom_documentation = value  # Delegates to property setter
        return self

    def getDocument(self) -> List["DocumentElement"]:
        """
        AUTOSAR-compliant getter for document.

        Returns:
            The document value

        Note:
            Delegates to document property (CODING_RULE_V2_00017)
        """
        return self.document  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_custom_documentation(self, value: Optional["Documentation"]) -> "SpecificationDocumentScope":
        """
        Set customDocumentation and return self for chaining.

        Args:
            value: The customDocumentation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_custom_documentation("value")
        """
        self.custom_documentation = value  # Use property setter (gets validation)
        return self
