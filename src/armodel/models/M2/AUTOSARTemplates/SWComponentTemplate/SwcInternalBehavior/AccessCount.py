"""
This module contains classes for representing AUTOSAR access count elements
in software component internal behavior templates.
"""

from abc import ABC

from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameToken, PositiveInteger, RefType
from typing import List, Optional


class AbstractAccessPoint(AtpStructureElement, ABC):
    """
    Abstract class indicating an access point from an ExecutableEntity.
    """

    # AbstractAccessPoint method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getReturnValueProvision      [x] impl  [x] docstring  [ ] test
    # [ ] setReturnValueProvision      [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AbstractAccessPoint:
            raise TypeError("ARObject is an abstract class.")

        super().__init__(parent, short_name)

        self.returnValueProvision = None

    def getReturnValueProvision(self):
        """
        Gets the return value provision.

        Returns:
            The return value provision
        """
        return self.returnValueProvision

    def setReturnValueProvision(self, value):
        """
        Sets the return value provision.
        Only sets the value if it is not None.

        Args:
            value: The return value provision to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.returnValueProvision = value
        return self


class AccessCount(ARObject):
    """
    This meta-class provides one count value for a AbstractAccessPoint.
    """

    # AccessCount method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 4.23, p.57
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getAccessPoint               [x] impl  [x] docstring  [x] test
    # [x] setAccessPoint               [x] impl  [x] docstring  [x] test
    # [x] getValue                     [x] impl  [x] docstring  [x] test
    # [x] setValue                     [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the AccessCount.
        """
        super().__init__()

        # Reference to the AbstractAccessPoint for which the count value is applicable.
        self.accessPoint: Optional[RefType] = None

        # The number of determined accesses for the referenced access point.
        self.value: Optional[PositiveInteger] = None

    def getAccessPoint(self) -> Optional[RefType]:
        """
        Gets the reference to the AbstractAccessPoint for which the count value is applicable.

        Returns:
            RefType referencing the access point, or None if not set
        """
        return self.accessPoint

    def setAccessPoint(self, value: Optional[RefType]) -> "AccessCount":
        """
        Sets the reference to the AbstractAccessPoint for which the count value is applicable.
        A None value is a no-op and does not overwrite an existing reference.

        Args:
            value: The access point reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.accessPoint = value
        return self

    def getValue(self) -> Optional[PositiveInteger]:
        """
        Gets the number of determined accesses for the referenced access point.

        Returns:
            PositiveInteger representing the access count, or None if not set
        """
        return self.value

    def setValue(self, value: Optional[PositiveInteger]) -> "AccessCount":
        """
        Sets the number of determined accesses for the referenced access point.
        A None value is a no-op and does not overwrite an existing value.

        Args:
            value: The access count to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.value = value
        return self


class AccessCountSet(ARObject):
    """
    This meta-class provides a set of count values evaluated according to the
    rules of a specific countProfile.
    """

    # AccessCountSet method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 4.22, p.57
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] addAccessCount                [x] impl  [x] docstring  [x] test
    # [x] getAccessCounts              [x] impl  [x] docstring  [x] test
    # [x] getCountProfile              [x] impl  [x] docstring  [x] test
    # [x] setCountProfile              [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the AccessCountSet.
        """
        super().__init__()

        # The count values for the AbstractAccessPoints of an ExecutableEntity.
        self.accessCounts: List[AccessCount] = []

        # The name of the count profile used to determine the AccessCount.value numbers.
        self.countProfile: Optional[NameToken] = None

    def addAccessCount(self, value: Optional[AccessCount]) -> "AccessCountSet":
        """
        Adds an AccessCount to this access count set.

        Args:
            value: The access count to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.accessCounts.append(value)
        return self

    def getAccessCounts(self) -> List[AccessCount]:
        """
        Gets all AccessCount instances aggregated by this access count set.

        Returns:
            List of AccessCount instances
        """
        return self.accessCounts

    def getCountProfile(self) -> Optional[NameToken]:
        """
        Gets the name of the count profile used to determine the AccessCount.value numbers.

        Returns:
            NameToken representing the count profile, or None if not set
        """
        return self.countProfile

    def setCountProfile(self, value: Optional[NameToken]) -> "AccessCountSet":
        """
        Sets the name of the count profile used to determine the AccessCount.value numbers.
        A None value is a no-op and does not overwrite an existing profile.

        Args:
            value: The count profile to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.countProfile = value
        return self
