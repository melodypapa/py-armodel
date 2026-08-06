"""
This module contains classes for representing AUTOSAR engineering objects
in the GenericStructure module.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameToken, RevisionLabelString
from abc import ABC
from typing import List, Optional


class EngineeringObject(ARObject, ABC):
    """
    This class specifies an engineering object. Usually such an object is represented by a
    file artifact. The properties of engineering object are such that the artifact can be
    found by querying an ASAM catalog file. The engineering object is uniquely identified
    by domain+category+shortLabel+revisionLabel.
    """

    # EngineeringObject method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 7.6, p.132
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getShortLabel                [x] impl  [x] docstring  [x] test
    # [x] setShortLabel                [x] impl  [x] docstring  [x] test
    # [x] getCategory                  [x] impl  [x] docstring  [x] test
    # [x] setCategory                  [x] impl  [x] docstring  [x] test
    # [x] addRevisionLabel             [x] impl  [x] docstring  [x] test
    # [x] getRevisionLabels            [x] impl  [x] docstring  [x] test
    # [x] getDomain                    [x] impl  [x] docstring  [x] test
    # [x] setDomain                    [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the EngineeringObject.
        Raises TypeError if this abstract class is instantiated directly.
        """
        if type(self) is EngineeringObject:
            raise TypeError("EngineeringObject is an abstract class.")

        super().__init__()

        # This is the short name of the engineering object. Note that it is modeled as
        # NameToken and not as Identifier since in ASAM-CC it is also a NameToken.
        self.shortLabel: Optional[NameToken] = None

        # This denotes the role of the engineering object in the development cycle.
        # Categories are such as SWSRC for source code, SWOBJ for object code,
        # SWHDR for a C-header file. Further roles need to be defined via Methodology.
        self.category: Optional[NameToken] = None

        # This is a revision label denoting a particular version of the engineering object.
        self.revisionLabels: List[RevisionLabelString] = []

        # This denotes the domain in which the engineering object is stored. This allows to
        # indicate various segments in the repository keeping the engineering objects.
        # Attribute is optional to support a default domain.
        self.domain: Optional[NameToken] = None

    def getShortLabel(self) -> Optional[NameToken]:
        """
        Gets the short name of the engineering object.

        Returns:
            NameToken representing the short label, or None if not set
        """
        return self.shortLabel

    def setShortLabel(self, label: Optional[NameToken]) -> "EngineeringObject":
        """
        Sets the short name of the engineering object.
        A None value is a no-op and does not overwrite an existing short label.

        Args:
            label: The short label to set

        Returns:
            self for method chaining
        """
        if label is not None:
            self.shortLabel = label
        return self

    def getCategory(self) -> Optional[NameToken]:
        """
        Gets the role of the engineering object in the development cycle.

        Returns:
            NameToken representing the category, or None if not set
        """
        return self.category

    def setCategory(self, category: Optional[NameToken]) -> "EngineeringObject":
        """
        Sets the role of the engineering object in the development cycle.
        A None value is a no-op and does not overwrite an existing category.

        Args:
            category: The category to set

        Returns:
            self for method chaining
        """
        if category is not None:
            self.category = category
        return self

    def addRevisionLabel(self, revision_label: Optional[RevisionLabelString]) -> "EngineeringObject":
        """
        Adds a revision label denoting a particular version of the engineering object.
        A None value is a no-op and is not appended.

        Args:
            revision_label: The revision label to add

        Returns:
            self for method chaining
        """
        if revision_label is not None:
            self.revisionLabels.append(revision_label)
        return self

    def getRevisionLabels(self) -> List[RevisionLabelString]:
        """
        Gets the list of revision labels denoting particular versions of the engineering object.

        Returns:
            List of RevisionLabelString instances
        """
        return self.revisionLabels

    def getDomain(self) -> Optional[NameToken]:
        """
        Gets the domain in which the engineering object is stored.

        Returns:
            NameToken representing the domain, or None if not set
        """
        return self.domain

    def setDomain(self, domain: Optional[NameToken]) -> "EngineeringObject":
        """
        Sets the domain in which the engineering object is stored.
        A None value is a no-op and does not overwrite an existing domain.

        Args:
            domain: The domain to set

        Returns:
            self for method chaining
        """
        if domain is not None:
            self.domain = domain
        return self


class AutosarEngineeringObject(EngineeringObject):
    """
    This denotes an engineering object being part of the process. It is a specialization
    of the abstract class EngineeringObject for usage within AUTOSAR.
    """

    # AutosarEngineeringObject method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 7.5, p.132
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the AutosarEngineeringObject.
        """
        super().__init__()
