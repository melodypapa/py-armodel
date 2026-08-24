from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, ARNumerical, Integer, PositiveInteger, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import Frame, FrameTriggering


class LinErrorResponse(ARObject):
    """Each slave node shall publish a one bit signal, named response_error, to the master node in one of its transmitted unconditional frames. The response_error signal shall be set whenever a frame (except for event triggered frame responses) that is transmitted or received by the slave node contains an error in the frame response. The response_error signal shall be cleared when the unconditional frame containing the response_error signal is successfully transmitted."""

    # LinErrorResponse method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.42, p.97
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getResponseErrorRef          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setResponseErrorRef          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This ISignal shall be taken to transport the responseError bit.
        self.responseErrorRef: Optional[RefType] = None

    def getResponseErrorRef(self) -> Optional[RefType]:
        """This ISignal shall be taken to transport the responseError bit."""
        return self.responseErrorRef

    def setResponseErrorRef(self, value: Optional[RefType]) -> "LinErrorResponse":
        """
        This ISignal shall be taken to transport the responseError bit.
        A None value is a no-op and does not overwrite an existing responseErrorRef.
        """
        if value is not None:
            self.responseErrorRef = value
        return self


class LinFrame(Frame, ABC):
    """
    Lin specific Frame element.
    """

    # LinFrame method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.87, p.428
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # (no own attributes; Base = ARObject, CollectableElement, FibexElement, Frame, Identifiable, MultilanguageReferrable, PackageableElement, Referrable)

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is LinFrame:
            raise TypeError("LinFrame is an abstract class.")

        super().__init__(parent, short_name)


class LinUnconditionalFrame(LinFrame):
    """
    Unconditional frames carry signals. The master sends a frame header in a scheduled frame slot and the designated slave node fills the frame with data. Tags: atp.recommendedPackage=Frames
    """

    # LinUnconditionalFrame method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.90, p.429
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # (no own attributes; Base = ARObject, CollectableElement, FibexElement, Frame, Identifiable, LinFrame, MultilanguageReferrable, PackageableElement, Referrable)

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
        super().__init__((ResumePosition.CONTINUE_AT_IT_POSITION, ResumePosition.START_FROM_BEGINNING))


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
        self.introduction = None  # type: DocumentationBlock
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
    FreeFormat transmits a fixed master request frame with the eight data bytes provided. This may for instance be used to issue user specific fixed frames.
    """

    # FreeFormatEntry method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.98, p.434
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # (no own attributes; Base = ARObject, ScheduleTableEntry; serialized through concrete subclass FreeFormat)

    def __init__(self):
        if type(self) is FreeFormatEntry:
            raise TypeError("FreeFormatEntry is an abstract class.")
        super().__init__()


class FreeFormat(FreeFormatEntry):
    """
    Representing freely defined data.
    """

    # FreeFormat method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.108, p.439
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getByteValues    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addByteValue     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # (Base = ARObject, FreeFormatEntry, ScheduleTableEntry)

    def __init__(self):
        super().__init__()

        # The integer Value of a freely defined data byte.
        self.byteValues: List[Integer] = []

    def getByteValues(self) -> List[Integer]:
        """
        The integer Value of a freely defined data byte.
        """
        return self.byteValues

    def addByteValue(self, value: Optional[Integer]) -> "FreeFormat":
        """
        The integer Value of a freely defined data byte.
        A None value is a no-op.
        """
        if value is not None:
            self.byteValues.append(value)
        return self


class LinConfigurationEntry(ScheduleTableEntry, ABC):
    """
    A ScheduleTableEntry which contains LIN specific assignments.
    """

    # LinConfigurationEntry method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.99, p.434
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getAssignedControllerRef       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAssignedControllerRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getAssignedLinSlaveConfigRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAssignedLinSlaveConfigRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # (Base = ARObject, ScheduleTableEntry; abstract — no own XML tag; ASSIGNED-CONTROLLER-REF/ASSIGNED-LIN-SLAVE-CONFIG-REF round-trip via the concrete subclass dispatch in readLinScheduleTableTableEntries/writeLinScheduleTableTableEntries)

    def __init__(self):

        if type(self) is LinConfigurationEntry:
            raise TypeError("LinConfigurationEntry is an abstract class.")

        super().__init__()

        # The LIN slaves controller who is target of this assignment. Optional in case LinConfigurationEntry.assignedLinSlaveConfig exists.
        self.assignedControllerRef: Optional[RefType] = None

        # The LIN slave that is target of this assignment. Please note that this reference is redundant to the assignedController reference. In an Ecu Extract of the LinMaster the LinSlave Ecus shall not be available. The information that is described here is necessary in the ECU Extract for the configuration of the LinMaster.
        self.assignedLinSlaveConfigRef: Optional[RefType] = None

    def getAssignedControllerRef(self) -> Optional[RefType]:
        """
        The LIN slaves controller who is target of this assignment. Optional in case LinConfigurationEntry.assignedLinSlaveConfig exists.
        """
        return self.assignedControllerRef

    def setAssignedControllerRef(self, value: Optional[RefType]) -> "LinConfigurationEntry":
        """
        The LIN slaves controller who is target of this assignment. Optional in case LinConfigurationEntry.assignedLinSlaveConfig exists.
        A None value is a no-op and does not overwrite an existing assignedControllerRef.
        """
        if value is not None:
            self.assignedControllerRef = value
        return self

    def getAssignedLinSlaveConfigRef(self) -> Optional[RefType]:
        """
        The LIN slave that is target of this assignment. Please note that this reference is redundant to the assignedController reference. In an Ecu Extract of the LinMaster the LinSlave Ecus shall not be available. The information that is described here is necessary in the ECU Extract for the configuration of the LinMaster.
        """
        return self.assignedLinSlaveConfigRef

    def setAssignedLinSlaveConfigRef(self, value: Optional[RefType]) -> "LinConfigurationEntry":
        """
        The LIN slave that is target of this assignment. Please note that this reference is redundant to the assignedController reference. In an Ecu Extract of the LinMaster the LinSlave Ecus shall not be available. The information that is described here is necessary in the ECU Extract for the configuration of the LinMaster.
        A None value is a no-op and does not overwrite an existing assignedLinSlaveConfigRef.
        """
        if value is not None:
            self.assignedLinSlaveConfigRef = value
        return self


class FramePid(ARObject):
    """
    Frame_PIDs that are included in the request. The "pid" attribute describes the value and the "index" attribute the position of the frame_PID in the request.
    """

    # FramePid method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.103, p.437
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getIndex      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setIndex      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPid        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPid        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # (Base = ARObject; aggregated by AssignFrameIdRange.framePid)

    def __init__(self):
        super().__init__()

        # This attribute is used to order the frame_PIDs. The values of index shall be unique within one AssignFrameIdRange.
        self.index: Optional[Integer] = None
        # Frame_PID value.
        self.pid: Optional[PositiveInteger] = None

    def getIndex(self) -> Optional[Integer]:
        """
        This attribute is used to order the frame_PIDs. The values of index shall be unique within one AssignFrameIdRange.
        """
        return self.index

    def setIndex(self, value: Optional[Integer]) -> "FramePid":
        """
        This attribute is used to order the frame_PIDs. The values of index shall be unique within one AssignFrameIdRange.
        A None value is a no-op and does not overwrite an existing index.
        """
        if value is not None:
            self.index = value
        return self

    def getPid(self) -> Optional[PositiveInteger]:
        """
        Frame_PID value.
        """
        return self.pid

    def setPid(self, value: Optional[PositiveInteger]) -> "FramePid":
        """
        Frame_PID value.
        A None value is a no-op and does not overwrite an existing pid.
        """
        if value is not None:
            self.pid = value
        return self


class AssignFrameId(LinConfigurationEntry):
    """
    Schedule entry for an Assign Frame Id master request.
    """

    # AssignFrameId method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.100, p.436
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getAssignedFrameTriggeringRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAssignedFrameTriggeringRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # (Base = ARObject, LinConfigurationEntry, ScheduleTableEntry; messageId present in XSD with atp.Status="removed" — not modeled)

    def __init__(self):
        super().__init__()

        # The frame whose identifier is set by this assignment.
        self.assignedFrameTriggeringRef: Optional[RefType] = None

    def getAssignedFrameTriggeringRef(self) -> Optional[RefType]:
        """
        The frame whose identifier is set by this assignment.
        """
        return self.assignedFrameTriggeringRef

    def setAssignedFrameTriggeringRef(self, value: Optional[RefType]) -> "AssignFrameId":
        """
        The frame whose identifier is set by this assignment.
        A None value is a no-op and does not overwrite an existing assignedFrameTriggeringRef.
        """
        if value is not None:
            self.assignedFrameTriggeringRef = value
        return self


class UnassignFrameId(LinConfigurationEntry):
    """
    Schedule entry for an Unassign Frame Id master request where the protected identifier is assigned the value 0x40. This will disable reception/transmission of a previously dynamically assigned frame identifier.
    """

    # UnassignFrameId method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.101, p.436
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getUnassignedFrameTriggeringRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setUnassignedFrameTriggeringRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # (Base = ARObject, LinConfigurationEntry, ScheduleTableEntry; messageId present in XSD with atp.Status="removed" — not modeled)

    def __init__(self):
        super().__init__()

        # The frame whose identifier is reset by this assignment.
        self.unassignedFrameTriggeringRef: Optional[RefType] = None

    def getUnassignedFrameTriggeringRef(self) -> Optional[RefType]:
        """
        The frame whose identifier is reset by this assignment.
        """
        return self.unassignedFrameTriggeringRef

    def setUnassignedFrameTriggeringRef(self, value: Optional[RefType]) -> "UnassignFrameId":
        """
        The frame whose identifier is reset by this assignment.
        A None value is a no-op and does not overwrite an existing unassignedFrameTriggeringRef.
        """
        if value is not None:
            self.unassignedFrameTriggeringRef = value
        return self


class AssignFrameIdRange(LinConfigurationEntry):
    """
    AssignFrameIdRange generates an assign frame PID range request.
    """

    # AssignFrameIdRange method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.102, p.437
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getFramePids           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addFramePid            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getStartIndex          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setStartIndex          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # (Base = ARObject, LinConfigurationEntry, ScheduleTableEntry)

    def __init__(self):
        super().__init__()

        # Optional assignment of frame_PID values that are included in the request. The frame_PIDs are ordered.
        self.framePids: List[FramePid] = []
        # The startIndex sets the index to the first frame to assign a PID.
        self.startIndex: Optional[Integer] = None

    def getFramePids(self) -> List[FramePid]:
        """
        Optional assignment of frame_PID values that are included in the request. The frame_PIDs are ordered.
        """
        return self.framePids

    def addFramePid(self, value: Optional[FramePid]) -> "AssignFrameIdRange":
        """
        Optional assignment of frame_PID values that are included in the request. The frame_PIDs are ordered.
        A None value is a no-op.
        """
        if value is not None:
            self.framePids.append(value)
        return self

    def getStartIndex(self) -> Optional[Integer]:
        """
        The startIndex sets the index to the first frame to assign a PID.
        """
        return self.startIndex

    def setStartIndex(self, value: Optional[Integer]) -> "AssignFrameIdRange":
        """
        The startIndex sets the index to the first frame to assign a PID.
        A None value is a no-op and does not overwrite an existing startIndex.
        """
        if value is not None:
            self.startIndex = value
        return self


class AssignNad(LinConfigurationEntry):
    """
    Schedule entry for an Assign NAD master request.
    """

    # AssignNad method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.104, p.438
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getNewNad       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setNewNad       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # (Base = ARObject, LinConfigurationEntry, ScheduleTableEntry)

    def __init__(self):
        super().__init__()

        # The newly assigned NAD value.
        self.newNad: Optional[Integer] = None

    def getNewNad(self) -> Optional[Integer]:
        """
        The newly assigned NAD value.
        """
        return self.newNad

    def setNewNad(self, value: Optional[Integer]) -> "AssignNad":
        """
        The newly assigned NAD value.
        A None value is a no-op and does not overwrite an existing newNad.
        """
        if value is not None:
            self.newNad = value
        return self


class ConditionalChangeNad(LinConfigurationEntry):
    """
    Generates an conditional change NAD request. See ISO 17987 protocol specification for more information.
    """

    # ConditionalChangeNad method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.105, p.438
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getByte         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setByte         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getId           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setId           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getInvert       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setInvert       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMask         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMask         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getNewNad       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setNewNad       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # (Base = ARObject, LinConfigurationEntry, ScheduleTableEntry)

    def __init__(self):
        super().__init__()

        # Byte Position of Data Byte that should be used for the bitwise XOR with Invert and the bitwise AND with Mask.
        self.byte: Optional[Integer] = None
        # Byte Position of Id.
        self.id: Optional[PositiveInteger] = None
        # Byte Position of Invert.
        self.invert: Optional[Integer] = None
        # Byte Position of Mask.
        self.mask: Optional[Integer] = None
        # The newly assigned NAD value (Byte Position).
        self.newNad: Optional[Integer] = None

    def getByte(self) -> Optional[Integer]:
        """
        Byte Position of Data Byte that should be used for the bitwise XOR with Invert and the bitwise AND with Mask.
        """
        return self.byte

    def setByte(self, value: Optional[Integer]) -> "ConditionalChangeNad":
        """
        Byte Position of Data Byte that should be used for the bitwise XOR with Invert and the bitwise AND with Mask.
        A None value is a no-op and does not overwrite an existing byte.
        """
        if value is not None:
            self.byte = value
        return self

    def getId(self) -> Optional[PositiveInteger]:
        """
        Byte Position of Id.
        """
        return self.id

    def setId(self, value: Optional[PositiveInteger]) -> "ConditionalChangeNad":
        """
        Byte Position of Id.
        A None value is a no-op and does not overwrite an existing id.
        """
        if value is not None:
            self.id = value
        return self

    def getInvert(self) -> Optional[Integer]:
        """
        Byte Position of Invert.
        """
        return self.invert

    def setInvert(self, value: Optional[Integer]) -> "ConditionalChangeNad":
        """
        Byte Position of Invert.
        A None value is a no-op and does not overwrite an existing invert.
        """
        if value is not None:
            self.invert = value
        return self

    def getMask(self) -> Optional[Integer]:
        """
        Byte Position of Mask.
        """
        return self.mask

    def setMask(self, value: Optional[Integer]) -> "ConditionalChangeNad":
        """
        Byte Position of Mask.
        A None value is a no-op and does not overwrite an existing mask.
        """
        if value is not None:
            self.mask = value
        return self

    def getNewNad(self) -> Optional[Integer]:
        """
        The newly assigned NAD value (Byte Position).
        """
        return self.newNad

    def setNewNad(self, value: Optional[Integer]) -> "ConditionalChangeNad":
        """
        The newly assigned NAD value (Byte Position).
        A None value is a no-op and does not overwrite an existing newNad.
        """
        if value is not None:
            self.newNad = value
        return self


class SaveConfigurationEntry(LinConfigurationEntry):
    """
    This service is used to notify a slave node to store its configuration.
    """

    # SaveConfigurationEntry method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.106, p.439
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # (no own attributes; Base = ARObject, LinConfigurationEntry, ScheduleTableEntry)

    def __init__(self):
        super().__init__()


class DataDumpEntry(LinConfigurationEntry):
    """
    This service is reserved for initial configuration of a slave node by the slave node supplier and the format of this message is supplier specific.
    """

    # DataDumpEntry method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.107, p.439
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getByteValues    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addByteValue     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # (Base = ARObject, LinConfigurationEntry, ScheduleTableEntry)

    def __init__(self):
        super().__init__()

        # Supplier specific format.
        self.byteValues: List[Integer] = []

    def getByteValues(self) -> List[Integer]:
        """
        Supplier specific format.
        """
        return self.byteValues

    def addByteValue(self, value: Optional[Integer]) -> "DataDumpEntry":
        """
        Supplier specific format.
        A None value is a no-op.
        """
        if value is not None:
            self.byteValues.append(value)
        return self


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

        self.resumePosition = None  # type: ResumePosition
        self.runMode = None  # type: RunMode
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
