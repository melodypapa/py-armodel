from abc import ABC
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Referrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Integer, PositiveInteger, RefType, String, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationConnector, CommunicationController


class LinSlaveConfigIdent(Referrable):
    """This meta-class is created to add the ability to become the target of a reference to the non-Referrable Lin SlaveConfig."""

    # LinSlaveConfigIdent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.40, p.95
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class LinCommunicationController(CommunicationController, ABC):
    """LIN bus specific communication controller attributes."""

    # LinCommunicationController method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.37, p.93
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getProtocolVersion           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setProtocolVersion           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is LinCommunicationController:
            raise TypeError("LinCommunicationController is an abstract class.")
        super().__init__(parent, short_name)

        # Version specifier for a communication protocol.
        self.protocolVersion: Optional[String] = None

    def getProtocolVersion(self) -> Optional[String]:
        """Version specifier for a communication protocol."""
        return self.protocolVersion

    def setProtocolVersion(self, value: Optional[String]) -> "LinCommunicationController":
        """
        Version specifier for a communication protocol.
        A None value is a no-op and does not overwrite an existing protocolVersion.
        """
        if value is not None:
            self.protocolVersion = value
        return self


class LinMaster(LinCommunicationController):
    """
    Defines a LIN master node in the network topology, specifying
    slave configurations, time base settings, and timing jitter
    properties for LIN master communication management.
    """

    # LinMaster method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getLinSlaves                 [x] impl  [ ] docstring  [ ] test
    # [ ] addLinSlaves                 [x] impl  [ ] docstring  [ ] test
    # [ ] getTimeBase                  [x] impl  [ ] docstring  [ ] test
    # [ ] setTimeBase                  [x] impl  [ ] docstring  [ ] test
    # [ ] getTimeBaseJitter            [x] impl  [ ] docstring  [ ] test
    # [ ] setTimeBaseJitter            [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.linSlaves = []
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
    """
    Defines a LIN communication connector that links LIN controllers
    to communication channels, specifying initial NAD (Node Address),
    configurable frames, and schedule change properties for LIN communication.
    """

    # LinCommunicationConnector method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getInitialNad                [x] impl  [ ] docstring  [ ] test
    # [ ] setInitialNad                [x] impl  [ ] docstring  [ ] test
    # [ ] getLinConfigurableFrames     [x] impl  [ ] docstring  [ ] test
    # [ ] addLinConfigurableFrame      [x] impl  [ ] docstring  [ ] test
    # [ ] getLinOrderedConfigurableFrames [x] impl  [ ] docstring  [ ] test
    # [ ] addLinOrderedConfigurableFrame [x] impl  [ ] docstring  [ ] test
    # [ ] getScheduleChangeNextTimeBase [x] impl  [ ] docstring  [ ] test
    # [ ] setScheduleChangeNextTimeBase [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.initialNad: Integer = None
        self.linConfigurableFrames = []
        self.linOrderedConfigurableFrames = []
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


class LinConfigurableFrame(ARObject):
    """Assignment of messageIds to Frames. This element shall be used for the LIN 2.0 Assign-Frame command."""

    # LinConfigurableFrame method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.44, p.99
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getFrameRef                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setFrameRef                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMessageId                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMessageId                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Reference to a Frame that is processed by the slave node.
        self.frameRef: Optional[RefType] = None

        # MessageId for the referenced frame
        self.messageId: Optional[PositiveInteger] = None

    def getFrameRef(self) -> Optional[RefType]:
        """Reference to a Frame that is processed by the slave node."""
        return self.frameRef

    def setFrameRef(self, value: Optional[RefType]) -> "LinConfigurableFrame":
        """
        Reference to a Frame that is processed by the slave node.
        A None value is a no-op and does not overwrite an existing frameRef.
        """
        if value is not None:
            self.frameRef = value
        return self

    def getMessageId(self) -> Optional[PositiveInteger]:
        """MessageId for the referenced frame"""
        return self.messageId

    def setMessageId(self, value: Optional[PositiveInteger]) -> "LinConfigurableFrame":
        """
        MessageId for the referenced frame
        A None value is a no-op and does not overwrite an existing messageId.
        """
        if value is not None:
            self.messageId = value
        return self


class LinOrderedConfigurableFrame(ARObject):
    """With the assignment of the index to a frame a mapping of Pids to Frames is possible. This element shall be used for the LIN 2.1 Assign-Frame-PID-Range command."""

    # LinOrderedConfigurableFrame method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.45, p.99
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getFrameRef                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setFrameRef                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getIndex                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setIndex                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Reference to a Frame that is processed by the slave node.
        self.frameRef: Optional[RefType] = None

        # This attribute is used to order the elements and allows an assignment of Pids to ConfigurableFrames that are defined in the slave.
        self.index: Optional[Integer] = None

    def getFrameRef(self) -> Optional[RefType]:
        """Reference to a Frame that is processed by the slave node."""
        return self.frameRef

    def setFrameRef(self, value: Optional[RefType]) -> "LinOrderedConfigurableFrame":
        """
        Reference to a Frame that is processed by the slave node.
        A None value is a no-op and does not overwrite an existing frameRef.
        """
        if value is not None:
            self.frameRef = value
        return self

    def getIndex(self) -> Optional[Integer]:
        """This attribute is used to order the elements and allows an assignment of Pids to ConfigurableFrames that are defined in the slave."""
        return self.index

    def setIndex(self, value: Optional[Integer]) -> "LinOrderedConfigurableFrame":
        """
        This attribute is used to order the elements and allows an assignment of Pids to ConfigurableFrames that are defined in the slave.
        A None value is a no-op and does not overwrite an existing index.
        """
        if value is not None:
            self.index = value
        return self
