from abc import ABC
from typing import List, Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import ScheduleTableEntry
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import LinFrame

    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    ARLiteral,
    ARNumerical,
    Integer,
    RefType,
    TimeValue,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    Frame,
    FrameTriggering,
)
from armodel.v2.models.M2.MSR.Documentation.TextModel.BlockElements import (
    DocumentationBlock,
)


class LinFrame(Frame, ABC):
    """
    Abstract base class for LIN frames, extending the generic Frame class
    with LIN-specific properties and behavior. This class serves as the
    foundation for concrete LIN frame implementations.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        if type(self) is LinFrame:
            raise TypeError("LinFrame is an abstract class.")

        super().__init__(parent, short_name)

class LinUnconditionalFrame(LinFrame):
    """
    Represents an unconditional LIN frame in the AUTOSAR system,
    defining the structure and properties for LIN messages that
    are transmitted without conditional logic.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

class LinFrameTriggering(FrameTriggering):
    """
    Defines the triggering mechanism for LIN frames, specifying how and when
    LIN frames are transmitted or received on the network, including
    identifier and checksum properties.
    """
    def __init__(self, parent, short_name) -> None:
        super().__init__(parent, short_name)

        self.identifier: Union[Union[ARNumerical, None] , None] = None
        self.linChecksum: Union[Union[ARLiteral, None] , None] = None

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
    CONTINUE_AT_IT_POSITION = "continueAtItPosition"
    START_FROM_BEGINNING = "startFromBeginning"

    def __init__(self) -> None:
        super().__init__([
            ResumePosition.CONTINUE_AT_IT_POSITION,
            ResumePosition.START_FROM_BEGINNING
        ])

class ScheduleTableEntry(ARObject, ABC):
    """
    Abstract base class for schedule table entries, defining common
    properties for different types of entries in LIN schedule tables
    including timing, position, and documentation properties.
    """
    def __init__(self) -> None:

        if type(self) is ScheduleTableEntry:
            raise TypeError("ScheduleTableEntry is an abstract class.")

        super().__init__()

        self.delay: Union[Union[TimeValue, None] , None] = None
        self.introduction: Union[DocumentationBlock, None] = None
        self.positionInTable: Union[Union[Integer, None] , None] = None

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
    def __init__(self) -> None:
        super().__init__()

        self.frameTriggeringRef: Union[Union[RefType, None] , None] = None

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

    def __init__(self) -> None:
        if type(self) is FreeFormatEntry:
            raise TypeError("FreeFormatEntry is an abstract class.")
        super().__init__()

class LinConfigurationEntry(ScheduleTableEntry, ABC):
    """
    Abstract base class for LIN configuration entries in schedule tables,
    defining common properties for configuration-related schedule entries.
    """
    def __init__(self) -> None:

        if type(self) is LinConfigurationEntry:
            raise TypeError("LinConfigurationEntry is an abstract class.")

        super().__init__()


class LinScheduleTable(Identifiable):
    """
    Represents a LIN schedule table defining the timing and sequence
    of LIN frame transmissions, including resume position, run mode,
    and table entries for scheduled communication.
    """
    def __init__(self, parent, short_name) -> None:
        super().__init__(parent, short_name)

        self.resumePosition: Union[ResumePosition, None] = None
        self.runMode: Union[RunMode, None] = None
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


class RunMode(AREnum):
    """Enumeration for LIN run modes."""
    NO_MODE = "NO-MODE"
    IDLE_MODE = "IDLE-MODE"
    OPERATIONAL_MODE = "OPERATIONAL-MODE"
    SLEEP_MODE = "SLEEP-MODE"
    def __init__(self) -> None:
        super().__init__([
            RunMode.NO_MODE,
            RunMode.IDLE_MODE,
            RunMode.OPERATIONAL_MODE,
            RunMode.SLEEP_MODE
        ])

