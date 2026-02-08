"""
AUTOSAR Package - DataExchange

Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchange
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common import (
    SpecElementReference,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)




class SpecificationScope(ARObject):
    """
    Specification of the relevant subset of Autosar specifications.
    
    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchange::SpecificationScope
    
    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 96, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The Autosar or custom specifications that contain that are considered in this
        # Data Exchange Point.
        self._specification: List["SpecificationDocument"] = []

    @property
    def specification(self) -> List["SpecificationDocument"]:
        """Get specification (Pythonic accessor)."""
        return self._specification

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSpecification(self) -> List["SpecificationDocument"]:
        """
        AUTOSAR-compliant getter for specification.
        
        Returns:
            The specification value
        
        Note:
            Delegates to specification property (CODING_RULE_V2_00017)
        """
        return self.specification  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



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



class DocumentElementScope(SpecElementReference):
    """
    Specifies if a specification element such as a requirement, specification,
    deliverable, artifact, task definition or activity is in scope of this data
    exchange point. The DocumentElementScope may reference all specification
    elements that have a name or ID. The only exception are Meta Classes, Meta
    Attribute and constraints which are handled in the Data Format Tailoring
    section of the Profile of Data Exchange Point. Elements of Autosar
    specification documents are referenced via their ID (requirement,
    specification items) or name (deliverable, artifact, task definition or
    activity)
    
    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchange::DocumentElementScope
    
    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 97, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to a custom defined specification element.
        self._custom: Optional["Traceable"] = None

    @property
    def custom(self) -> Optional["Traceable"]:
        """Get custom (Pythonic accessor)."""
        return self._custom

    @custom.setter
    def custom(self, value: Optional["Traceable"]) -> None:
        """
        Set custom with validation.
        
        Args:
            value: The custom to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._custom = None
            return

        if not isinstance(value, Traceable):
            raise TypeError(
                f"custom must be Traceable or None, got {type(value).__name__}"
            )
        self._custom = value
        # Data Format Element that is implied by this element in the Used to share one
        # rationale for more.
        self._tailoring: List["DataFormatElement"] = []

    @property
    def tailoring(self) -> List["DataFormatElement"]:
        """Get tailoring (Pythonic accessor)."""
        return self._tailoring

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCustom(self) -> "Traceable":
        """
        AUTOSAR-compliant getter for custom.
        
        Returns:
            The custom value
        
        Note:
            Delegates to custom property (CODING_RULE_V2_00017)
        """
        return self.custom  # Delegates to property

    def setCustom(self, value: "Traceable") -> "DocumentElementScope":
        """
        AUTOSAR-compliant setter for custom with method chaining.
        
        Args:
            value: The custom to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to custom property setter (gets validation automatically)
        """
        self.custom = value  # Delegates to property setter
        return self

    def getTailoring(self) -> List["DataFormatElement"]:
        """
        AUTOSAR-compliant getter for tailoring.
        
        Returns:
            The tailoring value
        
        Note:
            Delegates to tailoring property (CODING_RULE_V2_00017)
        """
        return self.tailoring  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_custom(self, value: Optional["Traceable"]) -> "DocumentElementScope":
        """
        Set custom and return self for chaining.
        
        Args:
            value: The custom to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_custom("value")
        """
        self.custom = value  # Use property setter (gets validation)
        return self