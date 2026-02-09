"""
AUTOSAR Package - Keyword

Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::Keyword
"""

from typing import List

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class Keyword(Identifiable):
    """
    that such names is not only shortName. It could be symbol, or even longName.
    Application of keywords is not limited to particular names.
    
    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::Keyword::Keyword
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 454, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 194, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute specifies an abbreviated name of a abbreviation may e.
        # g.
        # be used for shortNames according to the conventions.
        # it may contain any name token.
        # E.
        # g.
        # it of digits only.
        # 535 Document ID 202: AUTOSAR_FO_TPS_GenericStructureTemplate Template R23-11.
        self._abbrName: "NameToken" = None

    @property
    def abbr_name(self) -> "NameToken":
        """Get abbrName (Pythonic accessor)."""
        return self._abbrName

    @abbr_name.setter
    def abbr_name(self, value: "NameToken") -> None:
        """
        Set abbrName with validation.
        
        Args:
            value: The abbrName to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (NameToken, str)):
            raise TypeError(
                f"abbrName must be NameToken or str, got {type(value).__name__}"
            )
        self._abbrName = value
        # CONDITION, INDEX,.
        self._classification: List["NameToken"] = []

    @property
    def classification(self) -> List["NameToken"]:
        """Get classification (Pythonic accessor)."""
        return self._classification

    def with_classification(self, value):
        """
        Set classification and return self for chaining.

        Args:
            value: The classification to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_classification("value")
        """
        self.classification = value  # Use property setter (gets validation)
        return self

    def with_keyword(self, value):
        """
        Set keyword and return self for chaining.

        Args:
            value: The keyword to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_keyword("value")
        """
        self.keyword = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAbbrName(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for abbrName.
        
        Returns:
            The abbrName value
        
        Note:
            Delegates to abbr_name property (CODING_RULE_V2_00017)
        """
        return self.abbr_name  # Delegates to property

    def setAbbrName(self, value: "NameToken") -> "Keyword":
        """
        AUTOSAR-compliant setter for abbrName with method chaining.
        
        Args:
            value: The abbrName to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to abbr_name property setter (gets validation automatically)
        """
        self.abbr_name = value  # Delegates to property setter
        return self

    def getClassification(self) -> List["NameToken"]:
        """
        AUTOSAR-compliant getter for classification.
        
        Returns:
            The classification value
        
        Note:
            Delegates to classification property (CODING_RULE_V2_00017)
        """
        return self.classification  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_abbr_name(self, value: "NameToken") -> "Keyword":
        """
        Set abbrName and return self for chaining.
        
        Args:
            value: The abbrName to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_abbr_name("value")
        """
        self.abbr_name = value  # Use property setter (gets validation)
        return self



class KeywordSet(ARElement):
    """
    This meta–class represents the ability to collect a set of predefined
    keywords.
    
    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::Keyword::KeywordSet
    
    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 194, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is one particular keyword in the keyword set.
        self._keyword: List["Keyword"] = []

    @property
    def keyword(self) -> List["Keyword"]:
        """Get keyword (Pythonic accessor)."""
        return self._keyword

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getKeyword(self) -> List["Keyword"]:
        """
        AUTOSAR-compliant getter for keyword.
        
        Returns:
            The keyword value
        
        Note:
            Delegates to keyword property (CODING_RULE_V2_00017)
        """
        return self.keyword  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
