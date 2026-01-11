from typing import List
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, String, TimeValue
from .......models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationConnector, CommunicationController


class LinCommunicationController(CommunicationController):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.protocolVersion: String = None

    def getProtocolVersion(self):
        return self.protocolVersion

    def setProtocolVersion(self, value):
        if value is not None:
            self.protocolVersion = value
        return self

class LinMaster(LinCommunicationController):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.linSlaves: List[LinSlaveConfig] = []
        self.timeBase: TimeValue = None
        self.timeBaseJitter: TimeValue = None

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
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.initialNad: Integer = None
        self.linConfigurableFrames: List[LinConfigurableFrame] = []
        self.linOrderedConfigurableFrames: List[LinOrderedConfigurableFrame] = []
        self.scheduleChangeNextTimeBase: Boolean = None

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
