"""
This module contains classes for representing AUTOSAR keyword structures
in the StandardizationTemplate module. Keywords are used for standardization
and classification purposes in AUTOSAR models.
"""

from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure.AtpBlueprint import (
    AtpBlueprintable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
)


class Keyword(Identifiable):
    """
    Represents a keyword in AUTOSAR models for standardization and classification purposes.
    Keywords can have abbreviated names and classifications for organizing and categorizing elements.
    """

    def __init__(self, parent, short_name):
        """
        Initializes the Keyword with a parent and short name.

        Args:
            parent: The parent ARObject that contains this keyword
            short_name: The unique short name of this keyword
        """
        super().__init__(parent, short_name)

        # Abbreviated name for this keyword
        self.abbrName: NameToken = None
        # List of classifications for this keyword
        self.classifications: List[NameToken] = []

    def getAbbrName(self):
        """
        Gets the abbreviated name for this keyword.

        Returns:
            NameToken: The abbreviated name
        """
        return self.abbrName

    def setAbbrName(self, value):
        """
        Sets the abbreviated name for this keyword.
        Only sets the value if it is not None.

        Args:
            value: The abbreviated name to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.abbrName = value
        return self

    def getClassifications(self):
        """
        Gets the list of classifications for this keyword.

        Returns:
            List of NameToken instances
        """
        return self.classifications

    def addClassification(self, value):
        """
        Adds a classification to this keyword.
        Only adds the value if it is not None.

        Args:
            value: The classification to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.classifications.append(value)
        return self


class KeywordSet(AtpBlueprintable):
    """
    Represents a set of keywords in AUTOSAR models for standardization and classification purposes.
    This class contains multiple keywords that are grouped together for organizational purposes.
    """

    def __init__(self, parent, short_name):
        """
        Initializes the KeywordSet with a parent and short name.

        Args:
            parent: The parent ARObject that contains this keyword set
            short_name: The unique short name of this keyword set
        """
        super().__init__(parent, short_name)

        # List of keywords in this keyword set
        self.keywords: List[Keyword] = []

    def getKeywords(self):
        """
        Gets the list of keywords in this keyword set.

        Returns:
            List of Keyword instances
        """
        return self.keywords

    def createKeyword(self, short_name: str) -> Keyword:
        """
        Creates and adds a Keyword to this keyword set.

        Args:
            short_name: The short name for the new keyword

        Returns:
            The created Keyword instance
        """
        if (not self.IsElementExists(short_name)):
            keyword = Keyword(self, short_name)
            self.addElement(keyword)
            self.keywords.append(keyword)
        return self.getElement(short_name)
