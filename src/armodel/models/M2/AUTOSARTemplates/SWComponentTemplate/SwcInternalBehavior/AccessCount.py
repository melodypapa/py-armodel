"""
This module contains classes for representing AUTOSAR access count elements
in software component internal behavior templates.
"""

from abc import ABC

from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, NameToken, PositiveInteger, RefType
from typing import List, Optional


class RteApiReturnValueProvisionEnum(AREnum):
    """
    This meta-class provides values to control how return values from RTE APIs are provided.
    """

    # RteApiReturnValueProvisionEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.32, p.562
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    # The RTE API shall not provide a return value. atp.EnumerationLiteralIndex=1
    NO_RETURN_VALUE_PROVIDED = "noReturnValueProvided"

    # The RTE API shall provide a return value. atp.EnumerationLiteralIndex=0
    RETURN_VALUE_PROVIDED = "returnValueProvided"

    def __init__(self):
        super().__init__(
            [
                RteApiReturnValueProvisionEnum.NO_RETURN_VALUE_PROVIDED,
                RteApiReturnValueProvisionEnum.RETURN_VALUE_PROVIDED,
            ]
        )


class AbstractAccessPoint(AtpStructureElement, ABC):
    """
    Abstract class indicating an access point from an ExecutableEntity.
    """

    # AbstractAccessPoint method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 4.24, p.57
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getReturnValueProvision      [x] impl  [x] docstring  [x] test
    # [x] setReturnValueProvision      [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AbstractAccessPoint:
            raise TypeError("AbstractAccessPoint is an abstract class.")

        super().__init__(parent, short_name)

        # This attribute controls the provision of return values for RTE APIs
        # that correspond to the enclosing access point.
        self.returnValueProvision: Optional[RteApiReturnValueProvisionEnum] = None

    def getReturnValueProvision(self) -> Optional[RteApiReturnValueProvisionEnum]:
        """
        Gets the return value provision of the enclosing access point.
        This controls the provision of return values for the RTE APIs that
        correspond to the access point.

        Returns:
            RteApiReturnValueProvisionEnum controlling return value provision, or None if not set
        """
        return self.returnValueProvision

    def setReturnValueProvision(self, value: Optional[RteApiReturnValueProvisionEnum]) -> "AbstractAccessPoint":
        """
        Sets the return value provision of the enclosing access point.
        A None value is a no-op and does not overwrite an existing provision.

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
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getAccessPointRef            [x] impl  [x] docstring  [x] test
    # [x] setAccessPointRef            [x] impl  [x] docstring  [x] test
    # [x] getValue                     [x] impl  [x] docstring  [x] test
    # [x] setValue                     [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the AccessCount.
        """
        super().__init__()

        # AbstractAccessPoint for which the count value is applicable.
        self.accessPointRef: Optional[RefType] = None

        # This attribute represents the number of determined accesses.
        # The value shall exist at the time when the configuration of the BSW module is finished (constr_10271).
        self.value: Optional[PositiveInteger] = None

    def getAccessPointRef(self) -> Optional[RefType]:
        """
        Gets the reference to the AbstractAccessPoint for which the count value is applicable.

        Returns:
            RefType referencing the access point, or None if not set
        """
        return self.accessPointRef

    def setAccessPointRef(self, value: Optional[RefType]) -> "AccessCount":
        """
        Sets the reference to the AbstractAccessPoint for which the count value is applicable.
        A None value is a no-op and does not overwrite an existing reference.

        Args:
            value: The access point reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.accessPointRef = value
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
        The value shall exist at the time when the configuration of the BSW module is finished (constr_10271).
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
    # Spec verified: R23-11
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

        # Count values for the AbstractAccessPoints of an ExecutableEntity.
        self.accessCounts: List[AccessCount] = []

        # This attribute defines the name of the count profile used to determine the AccessCount.value numbers.
        # The countProfile shall exist at the time when the configuration of the BSW module is finished (constr_10270).
        self.countProfile: Optional[NameToken] = None

    def addAccessCount(self, value: Optional[AccessCount]) -> "AccessCountSet":
        """
        Adds an AccessCount to this access count set.
        A None value is a no-op and does not append anything.

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
        The countProfile shall exist at the time when the configuration of the BSW module is finished (constr_10270).
        A None value is a no-op and does not overwrite an existing profile.

        Args:
            value: The count profile to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.countProfile = value
        return self
