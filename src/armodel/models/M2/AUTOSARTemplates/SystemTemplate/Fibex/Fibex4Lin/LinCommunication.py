from abc import ABC
from typing import List

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, ARNumerical, Integer, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import Frame, FrameTriggering

class LinFrame(Frame, ABC):
    """
    Abstract base class for LIN frames, extending the generic Frame class
    with LIN-specific properties and behavior. This class serves as the
    foundation for concrete LIN frame implementations.
    """
    # LinFrame method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is LinFrame:
            raise TypeError("LinFrame is an abstract class.")
        
        super().__init__(parent, short_name)

class LinUnconditionalFrame(LinFrame):
    """
    Represents an unconditional LIN frame in the AUTOSAR system,
    defining the structure and properties for LIN messages that
    are transmitted without conditional logic.
    """
    # LinUnconditionalFrame method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class LinFrameTriggering(FrameTriggering):
    """
    Defines the triggering mechanism for LIN frames, specifying how and when
    LIN frames are transmitted or received on the network, including
    identifier and checksum properties.
    """
    # LinFrameTriggering method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getIdentifier                [x] impl  [ ] docstring  [ ] test
    # [ ] setIdentifier                [x] impl  [ ] docstring  [ ] test
    # [ ] getLinChecksum               [x] impl  [ ] docstring  [ ] test
    # [ ] setLinChecksum               [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.identifier: ARNumerical = None
        self.linChecksum: ARLiteral = None

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
    """
    Enumeration defining possible resume positions for LIN schedule tables,
    specifying where execution should continue after an interruption.
    """
    # ResumePosition method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    CONTINUE_AT_IT_POSITION = "continueAtItPosition"
    START_FROM_BEGINNING = "startFromBeginning"

    def __init__(self):
        super().__init__((
            ResumePosition.CONTINUE_AT_IT_POSITION,
            ResumePosition.START_FROM_BEGINNING
        ))

class ScheduleTableEntry(ARObject, ABC):
    """
    Abstract base class for schedule table entries, defining common
    properties for different types of entries in LIN schedule tables
    including timing, position, and documentation properties.
    """
    # ScheduleTableEntry method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getDelay                     [x] impl  [ ] docstring  [ ] test
    # [ ] setDelay                     [x] impl  [ ] docstring  [ ] test
    # [ ] getIntroduction              [x] impl  [ ] docstring  [ ] test
    # [ ] setIntroduction              [x] impl  [ ] docstring  [ ] test
    # [ ] getPositionInTable           [x] impl  [ ] docstring  [ ] test
    # [ ] setPositionInTable           [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        
        if type(self) is ScheduleTableEntry:
            raise TypeError("ScheduleTableEntry is an abstract class.")
        
        super().__init__()

        self.delay: TimeValue = None
        self.introduction = None                                # type: DocumentationBlock
        self.positionInTable: Integer = None

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
    """
    Defines an application entry in a LIN schedule table,
    specifying frame triggering references for application-level
    communication entries in the schedule.
    """
    # ApplicationEntry method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getFrameTriggeringRef        [x] impl  [ ] docstring  [ ] test
    # [ ] setFrameTriggeringRef        [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.frameTriggeringRef: RefType = None

    def getFrameTriggeringRef(self):
        return self.frameTriggeringRef

    def setFrameTriggeringRef(self, value):
        if value is not None:
            self.frameTriggeringRef = value
        return self

class FreeFormatEntry(ScheduleTableEntry, ABC):
    """
    Defines a free format entry in a LIN schedule table,
    allowing for flexible schedule entries without specific
    frame triggering references.
    """
    # FreeFormatEntry method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test


    def __init__(self):
        if type(self) is FreeFormatEntry:
            raise TypeError("FreeFormatEntry is an abstract class.")
        super().__init__()

class LinConfigurationEntry(ScheduleTableEntry, ABC):
    """
    Abstract base class for LIN configuration entries in schedule tables,
    defining common properties for configuration-related schedule entries.
    """
    # LinConfigurationEntry method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):

        if type(self) is LinConfigurationEntry:
            raise TypeError("LinConfigurationEntry is an abstract class.")
        
        super().__init__()


class LinScheduleTable(Identifiable):
    """
    Represents a LIN schedule table defining the timing and sequence
    of LIN frame transmissions, including resume position, run mode,
    and table entries for scheduled communication.
    """
    # LinScheduleTable method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getResumePosition            [x] impl  [ ] docstring  [ ] test
    # [ ] setResumePosition            [x] impl  [ ] docstring  [ ] test
    # [ ] getRunMode                   [x] impl  [ ] docstring  [ ] test
    # [ ] setRunMode                   [x] impl  [ ] docstring  [ ] test
    # [ ] getTableEntries              [x] impl  [ ] docstring  [ ] test
    # [ ] addTableEntry                [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.resumePosition = None                              # type: ResumePosition
        self.runMode = None                                     # type: RunMode
        self.tableEntries: List[ScheduleTableEntry] = []

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
