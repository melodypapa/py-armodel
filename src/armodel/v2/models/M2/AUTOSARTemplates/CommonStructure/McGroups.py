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


    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        """
        Initializes the McGroup with default values.
        """
        super().__init__()
        self.groupName: Union[str, None] = None
        self.groupId: Union[str, None] = None

    def getGroupName(self):
        return self.groupName

    def setGroupName(self, value):
        self.groupName = value
        return self

    def getGroupId(self):
        return self.groupId

    def setGroupId(self, value):
        self.groupId = value
        return self


class McGroupDataRefSet(ARObject):
    """
    Represents a set of MC group data references.
    """


    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        """
        Initializes the McGroupDataRefSet with default values.
        """
        super().__init__()
        self.dataRefs = []

    def addDataRef(self, ref):
        self.dataRefs.append(ref)

    def getDataRefs(self):
        return self.dataRefs
