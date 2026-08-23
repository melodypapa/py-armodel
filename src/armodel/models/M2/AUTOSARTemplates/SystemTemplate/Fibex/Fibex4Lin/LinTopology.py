from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Referrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Integer, PositiveInteger, RefType, String, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import LinErrorResponse
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationCluster, CommunicationConnector, CommunicationController


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
    Describing the properties of the refering ecu as a LIN master.
    """

    # LinMaster method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.38, p.94
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getLinSlaves        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addLinSlave         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimeBase         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTimeBase         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimeBaseJitter   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTimeBaseJitter   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # LinSlaves that are handled by the LinMaster.
        self.linSlaves: List["LinSlaveConfig"] = []

        # Time base is mandatory for the master. It is not used for slaves. LIN 2.0 Spec states: "The time_base value specifies the used time base in the master node to generate the maximum allowed frame transfer time." The time base shall be specified AUTOSAR conform in seconds.
        self.timeBase: Optional[TimeValue] = None

        # The attribute timeBaseJitter is a mandatory attribute for the master and not used for slaves. LIN 2.0 Spec states: "The jitter value specifies the differences between the maximum and minimum delay from time base start point to the frame header sending start point (falling edge of BREAK signal)." The jitter shall be specified AUTOSAR conform in seconds.
        self.timeBaseJitter: Optional[TimeValue] = None

    def getLinSlaves(self) -> List["LinSlaveConfig"]:
        """LinSlaves that are handled by the LinMaster."""
        return self.linSlaves

    def addLinSlave(self, value: "LinSlaveConfig") -> "LinMaster":
        """
        LinSlaves that are handled by the LinMaster.
        A None value is a no-op and does not extend linSlaves.
        """
        if value is not None:
            self.linSlaves.append(value)
        return self

    def getTimeBase(self) -> Optional[TimeValue]:
        """Time base is mandatory for the master. It is not used for slaves. LIN 2.0 Spec states: "The time_base value specifies the used time base in the master node to generate the maximum allowed frame transfer time." The time base shall be specified AUTOSAR conform in seconds."""
        return self.timeBase

    def setTimeBase(self, value: Optional[TimeValue]) -> "LinMaster":
        """
        Time base is mandatory for the master. It is not used for slaves. LIN 2.0 Spec states: "The time_base value specifies the used time base in the master node to generate the maximum allowed frame transfer time." The time base shall be specified AUTOSAR conform in seconds.
        A None value is a no-op and does not overwrite an existing timeBase.
        """
        if value is not None:
            self.timeBase = value
        return self

    def getTimeBaseJitter(self) -> Optional[TimeValue]:
        """The attribute timeBaseJitter is a mandatory attribute for the master and not used for slaves. LIN 2.0 Spec states: "The jitter value specifies the differences between the maximum and minimum delay from time base start point to the frame header sending start point (falling edge of BREAK signal)." The jitter shall be specified AUTOSAR conform in seconds."""
        return self.timeBaseJitter

    def setTimeBaseJitter(self, value: Optional[TimeValue]) -> "LinMaster":
        """
        The attribute timeBaseJitter is a mandatory attribute for the master and not used for slaves. LIN 2.0 Spec states: "The jitter value specifies the differences between the maximum and minimum delay from time base start point to the frame header sending start point (falling edge of BREAK signal)." The jitter shall be specified AUTOSAR conform in seconds.
        A None value is a no-op and does not overwrite an existing timeBaseJitter.
        """
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


class LinSlaveConfig(ARObject):
    """Node attributes of LIN slaves that are handled by the LinMaster. In the System Description LIN slaves may be described in the context of the Lin Master. In an ECU Extract of the LinMaster the LinSlave Ecus shall not be available. The information that is described here is necessary in the ECU Extract for the configuration of the Lin Master. The values of attributes of LinSlaveConfig and the corresponding LinSlave shall be identical (if both are defined in a System Description)."""

    # LinSlaveConfig method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.39, p.95
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getConfiguredNad                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setConfiguredNad                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getFunctionId                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setFunctionId                        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getIdent                             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setIdent                             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getInitialNad                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setInitialNad                        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getLinConfigurableFrames             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addLinConfigurableFrame              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getLinErrorResponse                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setLinErrorResponse                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getLinOrderedConfigurableFrames      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addLinOrderedConfigurableFrame       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getProtocolVersion                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setProtocolVersion                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSupplierId                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSupplierId                        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getVariantId                         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setVariantId                         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # To distinguish LIN slaves that are used twice or more within the same cluster.
        self.configuredNad: Optional[Integer] = None

        # LIN function ID.
        self.functionId: Optional[PositiveInteger] = None

        # This adds the ability to become referrable to LinSlaveConfig.
        self.ident: Optional[LinSlaveConfigIdent] = None

        # Initial NAD of the LIN slave.
        self.initialNad: Optional[Integer] = None

        # List of all frames that are processed by the slave node
        self.linConfigurableFrames: List[LinConfigurableFrame] = []

        # Each slave node shall publish one response error in one of its transmitted unconditional frames.
        self.linErrorResponse: Optional[LinErrorResponse] = None

        # List of all frames (unconditional frames, event-triggered frames and sporadic frames) processed by the slave node. This element is necessary for the LIN 2.1 Assign-Frame-PID-Range command.
        self.linOrderedConfigurableFrames: List[LinOrderedConfigurableFrame] = []

        # Version specifier for a communication protocol. Protocol version of the LinMaster and the LinSlaves may be different.
        self.protocolVersion: Optional[String] = None

        # LIN Supplier ID.
        self.supplierId: Optional[PositiveInteger] = None

        # Specifies the Variant ID.
        self.variantId: Optional[PositiveInteger] = None

    def getConfiguredNad(self) -> Optional[Integer]:
        """To distinguish LIN slaves that are used twice or more within the same cluster."""
        return self.configuredNad

    def setConfiguredNad(self, value: Optional[Integer]) -> "LinSlaveConfig":
        """
        To distinguish LIN slaves that are used twice or more within the same cluster.
        A None value is a no-op and does not overwrite an existing configuredNad.
        """
        if value is not None:
            self.configuredNad = value
        return self

    def getFunctionId(self) -> Optional[PositiveInteger]:
        """LIN function ID."""
        return self.functionId

    def setFunctionId(self, value: Optional[PositiveInteger]) -> "LinSlaveConfig":
        """
        LIN function ID.
        A None value is a no-op and does not overwrite an existing functionId.
        """
        if value is not None:
            self.functionId = value
        return self

    def getIdent(self) -> Optional[LinSlaveConfigIdent]:
        """This adds the ability to become referrable to LinSlaveConfig."""
        return self.ident

    def setIdent(self, value: Optional[LinSlaveConfigIdent]) -> "LinSlaveConfig":
        """
        This adds the ability to become referrable to LinSlaveConfig.
        A None value is a no-op and does not overwrite an existing ident.
        """
        if value is not None:
            self.ident = value
        return self

    def getInitialNad(self) -> Optional[Integer]:
        """Initial NAD of the LIN slave."""
        return self.initialNad

    def setInitialNad(self, value: Optional[Integer]) -> "LinSlaveConfig":
        """
        Initial NAD of the LIN slave.
        A None value is a no-op and does not overwrite an existing initialNad.
        """
        if value is not None:
            self.initialNad = value
        return self

    def getLinConfigurableFrames(self) -> List[LinConfigurableFrame]:
        """List of all frames that are processed by the slave node"""
        return self.linConfigurableFrames

    def addLinConfigurableFrame(self, value: LinConfigurableFrame) -> "LinSlaveConfig":
        """
        List of all frames that are processed by the slave node
        A None value is a no-op and does not extend linConfigurableFrames.
        """
        if value is not None:
            self.linConfigurableFrames.append(value)
        return self

    def getLinErrorResponse(self) -> Optional[LinErrorResponse]:
        """Each slave node shall publish one response error in one of its transmitted unconditional frames."""
        return self.linErrorResponse

    def setLinErrorResponse(self, value: Optional[LinErrorResponse]) -> "LinSlaveConfig":
        """
        Each slave node shall publish one response error in one of its transmitted unconditional frames.
        A None value is a no-op and does not overwrite an existing linErrorResponse.
        """
        if value is not None:
            self.linErrorResponse = value
        return self

    def getLinOrderedConfigurableFrames(self) -> List[LinOrderedConfigurableFrame]:
        """List of all frames (unconditional frames, event-triggered frames and sporadic frames) processed by the slave node. This element is necessary for the LIN 2.1 Assign-Frame-PID-Range command."""
        return self.linOrderedConfigurableFrames

    def addLinOrderedConfigurableFrame(self, value: LinOrderedConfigurableFrame) -> "LinSlaveConfig":
        """
        List of all frames (unconditional frames, event-triggered frames and sporadic frames) processed by the slave node. This element is necessary for the LIN 2.1 Assign-Frame-PID-Range command.
        A None value is a no-op and does not extend linOrderedConfigurableFrames.
        """
        if value is not None:
            self.linOrderedConfigurableFrames.append(value)
        return self

    def getProtocolVersion(self) -> Optional[String]:
        """Version specifier for a communication protocol. Protocol version of the LinMaster and the LinSlaves may be different."""
        return self.protocolVersion

    def setProtocolVersion(self, value: Optional[String]) -> "LinSlaveConfig":
        """
        Version specifier for a communication protocol. Protocol version of the LinMaster and the LinSlaves may be different.
        A None value is a no-op and does not overwrite an existing protocolVersion.
        """
        if value is not None:
            self.protocolVersion = value
        return self

    def getSupplierId(self) -> Optional[PositiveInteger]:
        """LIN Supplier ID."""
        return self.supplierId

    def setSupplierId(self, value: Optional[PositiveInteger]) -> "LinSlaveConfig":
        """
        LIN Supplier ID.
        A None value is a no-op and does not overwrite an existing supplierId.
        """
        if value is not None:
            self.supplierId = value
        return self

    def getVariantId(self) -> Optional[PositiveInteger]:
        """Specifies the Variant ID."""
        return self.variantId

    def setVariantId(self, value: Optional[PositiveInteger]) -> "LinSlaveConfig":
        """
        Specifies the Variant ID.
        A None value is a no-op and does not overwrite an existing variantId.
        """
        if value is not None:
            self.variantId = value
        return self


class LinCluster(CommunicationCluster):
    """LIN specific attributes Tags: atp.recommendedPackage=CommunicationClusters"""

    # LinCluster method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.36, p.93
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
