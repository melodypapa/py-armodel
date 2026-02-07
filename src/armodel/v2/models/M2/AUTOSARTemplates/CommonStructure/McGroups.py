"""
This module defines measurement and calibration group classes in AUTOSAR.
"""

from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class McGroup(ARObject):
    """
    Represents a measurement and calibration group in AUTOSAR.
    This class defines a group of MC elements.
    """


    def __init__(self) -> None:
        """
        Initializes the McGroup with default values.
        """
        super().__init__()
        self.groupName: Union[str, None] = None
        self.groupId: Union[str, None] = None

    def getGroupName(self) -> Union[str, None]:
        return self.groupName

    def setGroupName(self, value: Union[str, None]) -> "McGroup":
        self.groupName = value
        return self

    def getGroupId(self) -> Union[str, None]:
        return self.groupId

    def setGroupId(self, value: Union[str, None]) -> "McGroup":
        self.groupId = value
        return self


class McGroupDataRefSet(ARObject):
    """
    Represents a set of MC group data references.
    """


    def __init__(self) -> None:
        """
        Initializes the McGroupDataRefSet with default values.
        """
        super().__init__()
        self.dataRefs = []

    def addDataRef(self, ref: str) -> None:
        self.dataRefs.append(ref)

    def getDataRefs(self) -> list:
        return self.dataRefs
