"""
This module contains classes for representing AUTOSAR keyword structures
in the StandardizationTemplate module. Keywords are used for standardization
and classification purposes in AUTOSAR models.
"""

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameToken
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import AtpBlueprintable


class Keyword(Identifiable):
    """
    This meta-class represents the ability to predefine keywords which may subsequently be used to construct names following a given naming convention, e.g. the AUTOSAR naming conventions.

    Note that such names is not only shortName. It could be symbol, or even longName. Application of keywords is not limited to particular names.
    """

    # Keyword method parity checklist:
    # Spec: AUTOSAR_TPS_StandardizationTemplate.pdf (R4.3.1), Table 6.2, p.91
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R4.3.1
    # [x] getAbbrName              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] setAbbrName              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # [x] getClassifications       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] addClassification        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # This attribute specifies an abbreviated name of a keyword. This abbreviation may e.g. be used for constructing valid shortNames according to  the AUTOSAR naming conventions.
        #
        # Unlike shortName, it may contain any name token. E.g. it may consist of digits only.
        self.abbrName: Optional[NameToken] = None

        # This attribute allows to attach classification to the Keyword such as MEAN, ACTION, CONDITION, INDEX, PREPOSITION
        self.classifications: List[NameToken] = []

    def getAbbrName(self) -> Optional[NameToken]:
        """
        This attribute specifies an abbreviated name of a keyword. This abbreviation may e.g. be used for constructing valid shortNames according to  the AUTOSAR naming conventions.

        Unlike shortName, it may contain any name token. E.g. it may consist of digits only.
        """
        return self.abbrName

    def setAbbrName(self, value: Optional[NameToken]) -> "Keyword":
        """
        This attribute specifies an abbreviated name of a keyword. This abbreviation may e.g. be used for constructing valid shortNames according to  the AUTOSAR naming conventions.

        Unlike shortName, it may contain any name token. E.g. it may consist of digits only.
        A None value is a no-op and does not overwrite an existing abbrName.
        """
        if value is not None:
            self.abbrName = value
        return self

    def getClassifications(self) -> List[NameToken]:
        """
        This attribute allows to attach classification to the Keyword such as MEAN, ACTION, CONDITION, INDEX, PREPOSITION
        """
        return self.classifications

    def addClassification(self, value: Optional[NameToken]) -> "Keyword":
        """
        This attribute allows to attach classification to the Keyword such as MEAN, ACTION, CONDITION, INDEX, PREPOSITION
        A None value is a no-op and does not extend the classification list.
        """
        if value is not None:
            self.classifications.append(value)
        return self


class KeywordSet(AtpBlueprintable):
    """
    Represents a set of keywords in AUTOSAR models for standardization and classification purposes.
    This class contains multiple keywords that are grouped together for organizational purposes.
    """

    # KeywordSet method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getKeywords                  [x] impl  [x] docstring  [x] test
    # [x] createKeyword                [x] impl  [x] docstring  [x] test

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
        if not self.IsElementExists(short_name, Keyword):
            keyword = Keyword(self, short_name)
            self.addElement(keyword)
            self.keywords.append(keyword)
        return self.getElement(short_name, Keyword)
