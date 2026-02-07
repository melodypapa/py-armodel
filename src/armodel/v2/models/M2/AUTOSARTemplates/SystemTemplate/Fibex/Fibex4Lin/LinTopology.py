from abc import ABC
from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    String,
    TimeValue,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import (
    CommunicationConnector,
    CommunicationController,
)


class LinCommunicationController(CommunicationController, ABC):
    """
    Represents a LIN communication controller in the system,
    defining properties for LIN network communication including
    protocol version specifications.
    """

    def __init__(self, parent: ARObject, short_name: str) -> None:
        if type(self) is LinCommunicationController:
            raise TypeError("LinCommunicationController is an abstract class.")
        super().__init__(parent, short_name)

        self.protocolVersion: Union[Union[String, None] , None] = None

    def getProtocolVersion(self):
        return self.protocolVersion

    def setProtocolVersion(self, value):
        if value is not None:
            self.protocolVersion = value
        return self

class LinMaster(LinCommunicationController):
    """
    Defines a LIN master node in the network topology, specifying
    slave configurations, time base settings, and timing jitter
    properties for LIN master communication management.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.linSlaves = []
        self.timeBase: Union[Union[TimeValue, None] , None] = None
        self.timeBaseJitter: Union[Union[TimeValue, None] , None] = None

    def getLinSlaves(self):
        return self.linSlaves

    def addLinSlaves(self, value):
        if value is not None:
            self.linSlaves.append(value)
        return self

    def getTimeBase(self):
        return self.timeBase

    def setTimeBase(self, value):
        if value is not None:
            self.timeBase = value
        return self

    def getTimeBaseJitter(self):
        return self.timeBaseJitter

    def setTimeBaseJitter(self, value):
        if value is not None:
            self.timeBaseJitter = value
        return self

class LinCommunicationConnector(CommunicationConnector):
    """
    Defines a LIN communication connector that links LIN controllers
    to communication channels, specifying initial NAD (Node Address),
    configurable frames, and schedule change properties for LIN communication.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.initialNad: Union[Union[Integer, None] , None] = None
        self.linConfigurableFrames = []
        self.linOrderedConfigurableFrames = []
        self.scheduleChangeNextTimeBase: Union[Union[Boolean, None] , None] = None

    def getInitialNad(self):
        return self.initialNad

    def setInitialNad(self, value):
        if value is not None:
            self.initialNad = value
        return self

    def getLinConfigurableFrames(self):
        return self.linConfigurableFrames

    def addLinConfigurableFrame(self, value):
        if value is not None:
            self.linConfigurableFrames.append(value)
        return self

    def getLinOrderedConfigurableFrames(self):
        return self.linOrderedConfigurableFrames

    def addLinOrderedConfigurableFrame(self, value):
        if value is not None:
            self.linOrderedConfigurableFrames.append(value)
        return self

    def getScheduleChangeNextTimeBase(self):
        return self.scheduleChangeNextTimeBase

    def setScheduleChangeNextTimeBase(self, value):
        if value is not None:
            self.scheduleChangeNextTimeBase = value
        return self
