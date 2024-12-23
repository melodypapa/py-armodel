
from abc import ABCMeta
from typing import List

from ......M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, ARNumerical, Integer, RefType, TimeValue
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral
from ......M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import Frame, FrameTriggering

class LinFrame(Frame, metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == LinFrame:
            raise NotImplementedError("LinFrame is an abstract class.")
        
        super().__init__(parent, short_name)

class LinUnconditionalFrame(LinFrame):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class LinFrameTriggering(FrameTriggering):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.identifier = None                          # type: ARNumerical
        self.linChecksum = None                         # type: ARLiteral

    def getIdentifier(self):
        return self.identifier

    def setIdentifier(self, value):
        if value is not None:
            self.identifier = value
        return self

    def getLinChecksum(self):
        return self.linChecksum

    def setLinChecksum(self, value):
        if value is not None:
            self.linChecksum = value
        return self

class ResumePosition(AREnum):
    CONTINUE_AT_IT_POSITION = "continueAtItPosition"
    START_FROM_BEGINNING = "startFromBeginning"

    def __init__(self):
        super().__init__((
            ResumePosition.CONTINUE_AT_IT_POSITION,
            ResumePosition.START_FROM_BEGINNING
        ))

class ScheduleTableEntry(ARObject, metaclass = ABCMeta):
    def __init__(self):
        
        if type(self) == ScheduleTableEntry:
            raise NotImplementedError("ScheduleTableEntry is an abstract class.")
        
        super().__init__()

        self.delay = None                                       # type: TimeValue
        self.introduction = None                                # type: DocumentationBlock
        self.positionInTable = None                             # type: Integer

    def getDelay(self):
        return self.delay

    def setDelay(self, value):
        if value is not None:
            self.delay = value
        return self

    def getIntroduction(self):
        return self.introduction

    def setIntroduction(self, value):
        if value is not None:
            self.introduction = value
        return self

    def getPositionInTable(self):
        return self.positionInTable

    def setPositionInTable(self, value):
        if value is not None:
            self.positionInTable = value
        return self

class ApplicationEntry(ScheduleTableEntry):
    def __init__(self):
        super().__init__()

        self.frameTriggeringRef = None                              # type: RefType

    def getFrameTriggeringRef(self):
        return self.frameTriggeringRef

    def setFrameTriggeringRef(self, value):
        if value is not None:
            self.frameTriggeringRef = value
        return self

class FreeFormatEntry(ScheduleTableEntry):
    def __init__(self):
        super().__init__()

class LinConfigurationEntry(ScheduleTableEntry, metaclass = ABCMeta):
    def __init__(self):

        if type(self) == LinConfigurationEntry:
            raise NotImplementedError("LinConfigurationEntry is an abstract class.")
        
        super().__init__()


class LinScheduleTable(Identifiable):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.resumePosition = None                              # type: ResumePosition
        self.runMode = None                                     # type: RunMode
        self.tableEntries = []                                  # type: List[ScheduleTableEntry]

    def getResumePosition(self):
        return self.resumePosition

    def setResumePosition(self, value):
        if value is not None:
            self.resumePosition = value
        return self

    def getRunMode(self):
        return self.runMode

    def setRunMode(self, value):
        if value is not None:
            self.runMode = value
        return self
    
    def getTableEntries(self):
        return self.tableEntries

    def addTableEntry(self, value):
        if value is not None:
            self.tableEntries.append(value)
        return self
