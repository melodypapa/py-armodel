"""
AUTOSAR Package - DocumentationOnM1

Package: M2::AUTOSARTemplates::GenericStructure::DocumentationOnM1
"""

from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    MultilanguageReferrable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
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

    def with_context(self, value):
        """
        Set context and return self for chaining.

        Args:
            value: The context to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context("value")
        """
        self.context = value  # Use property setter (gets validation)
        return self

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


class StandardNameEnum(AREnum):
    """
    StandardNameEnum enumeration

This enumeration lists all allowed standard abbreviations. Aggregated by AppliedStandard.appliesTo, StructuredReq.appliesTo

Package: M2::AUTOSARTemplates::GenericStructure::DocumentationOnM1
    """
    # Extract Template
    Diagnostic = "None"

    # CP R23-11
    AUTOSARAP = "0"

    # This Value represents the Classic Platform.
    CP = "1"

    # This values represents the Foundation.
    FO = "2"

    # This Values represents the Testing of the Adaptive Platform.
    TA = "3"

    # This values represents the Testing of the Classic Platform.
    TC = "4"
