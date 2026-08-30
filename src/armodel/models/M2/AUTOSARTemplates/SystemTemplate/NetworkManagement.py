# This module contains AUTOSAR System Template classes for network management
# It defines CAN, FlexRay, J1939, and UDP network management configurations

from abc import ABC
from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import RxIdentifierRange
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore import FibexElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, Boolean, Integer, PositiveInteger, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable


class NmClusterCoupling(ARObject, ABC):
    """
    Abstract base class for network management cluster coupling,
    defining common properties for connecting different types of
    network management clusters for coordinated network management.
    """

    # NmClusterCoupling method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        if type(self) is NmClusterCoupling:
            raise TypeError("NmClusterCoupling is an abstract class.")

        super().__init__()


class CanNmClusterCoupling(NmClusterCoupling):
    """
    Defines coupling properties for CAN network management clusters,
    specifying coupled cluster references and CAN-specific NM features
    like busload reduction and immediate restart capabilities.
    """

    # CanNmClusterCoupling method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getCoupledClusterRefs        [x] impl  [ ] docstring  [ ] test
    # [ ] addCoupledClusterRef         [x] impl  [ ] docstring  [ ] test
    # [ ] getNmBusloadReductionEnabled [x] impl  [ ] docstring  [ ] test
    # [ ] setNmBusloadReductionEnabled [x] impl  [ ] docstring  [ ] test
    # [ ] getNmImmediateRestartEnabled [x] impl  [ ] docstring  [ ] test
    # [ ] setNmImmediateRestartEnabled [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.coupledClusterRefs = []
        self.nmBusloadReductionEnabled = None
        self.nmImmediateRestartEnabled = None

    def getCoupledClusterRefs(self):
        return self.coupledClusterRefs

    def addCoupledClusterRef(self, value):
        self.coupledClusterRefs.append(value)
        return self

    def getNmBusloadReductionEnabled(self):
        return self.nmBusloadReductionEnabled

    def setNmBusloadReductionEnabled(self, value):
        self.nmBusloadReductionEnabled = value
        return self

    def getNmImmediateRestartEnabled(self):
        return self.nmImmediateRestartEnabled

    def setNmImmediateRestartEnabled(self, value):
        self.nmImmediateRestartEnabled = value
        return self


class FlexrayNmClusterCoupling(NmClusterCoupling):
    """
    Defines coupling properties for FlexRay network management clusters,
    specifying coupled cluster references and FlexRay-specific NM
    schedule variant configurations.
    """

    # FlexrayNmClusterCoupling method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getCoupledClusterRefs        [x] impl  [ ] docstring  [ ] test
    # [ ] addCoupledClusterRef         [x] impl  [ ] docstring  [ ] test
    # [ ] getNmScheduleVariant         [x] impl  [ ] docstring  [ ] test
    # [ ] setNmScheduleVariant         [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.coupledClusterRefs = []
        self.nmScheduleVariant = None

    def getCoupledClusterRefs(self):
        return self.coupledClusterRefs

    def addCoupledClusterRef(self, value):
        self.coupledClusterRefs.append(value)
        return self

    def getNmScheduleVariant(self):
        return self.nmScheduleVariant

    def setNmScheduleVariant(self, value):
        self.nmScheduleVariant = value
        return self


class NmCoordinatorRoleEnum(AREnum):
    """
    Supported NmCoordinator roles.
    """

    # NmCoordinatorRoleEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.304, p.676
    # Spec verified: R23-11
    # (no methods)

    # Coordinator which "actively" performs NmCoordinator functionality at this channel Tags: atp.EnumerationLiteralIndex=0
    ACTIVE = "active"

    # Coordinator which "passively" performs NmCoordinator functionality at this channel - used at Nm CoordinatorSync use case. Tags: atp.EnumerationLiteralIndex=1
    PASSIVE = "passive"

    def __init__(self):
        super().__init__(
            [
                NmCoordinatorRoleEnum.ACTIVE,
                NmCoordinatorRoleEnum.PASSIVE,
            ]
        )


class NmNode(Identifiable, ABC):
    """
    The linking of NmEcus to NmClusters is realized via the NmNodes.
    """

    # NmNode method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.303, p.676
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                                          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getControllerRef                                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setControllerRef                                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getNmCoordCluster                                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setNmCoordCluster                                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getNmCoordinatorRole                               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setNmCoordinatorRole                               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getNmIfEcuRef                                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setNmIfEcuRef                                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getNmNodeId                                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setNmNodeId                                        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getNmPassiveModeEnabled                            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setNmPassiveModeEnabled                            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addRxNmPduRef                                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRxNmPduRefs                                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addTxNmPduRef                                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTxNmPduRefs                                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is NmNode:
            raise TypeError("NmNode is an abstract class.")

        super().__init__(parent, short_name)

        # Association to an CommunicationController in the topology description.
        self.controllerRef: Optional[RefType] = None

        # NmCoordinationCluster identification number.
        self.nmCoordCluster: Optional[PositiveInteger] = None

        # This attribute indicates the role the NM Coordinator will have on this channel.
        self.nmCoordinatorRole: Optional[NmCoordinatorRoleEnum] = None

        # Reference to the NmEcu that contains this NmNode. (CommunicationController that is referenced by the Nm Node shall be contained in the EcuInstance that is referenced by the NmEcu).
        self.nmIfEcuRef: Optional[RefType] = None

        # Node identifier of local NmNode. Shall be unique in the NmCluster.
        self.nmNodeId: Optional[Integer] = None

        # Enables support of the Passive Mode. The passive mode is configurable per channel.
        self.nmPassiveModeEnabled: Optional[Boolean] = None

        # receive NM Pdu.
        self.rxNmPduRefs: List[RefType] = []

        # transmit NM Pdu
        self.txNmPduRefs: List[RefType] = []

    def getControllerRef(self) -> Optional[RefType]:
        """
        Association to an CommunicationController in the topology description.
        """
        return self.controllerRef

    def setControllerRef(self, value: Optional[RefType]) -> "NmNode":
        """
        Association to an CommunicationController in the topology description.
        A None value is a no-op and does not overwrite an existing controllerRef.
        """
        if value is not None:
            self.controllerRef = value
        return self

    def getNmCoordCluster(self) -> Optional[PositiveInteger]:
        """
        NmCoordinationCluster identification number.
        """
        return self.nmCoordCluster

    def setNmCoordCluster(self, value: Optional[PositiveInteger]) -> "NmNode":
        """
        NmCoordinationCluster identification number.
        A None value is a no-op and does not overwrite an existing nmCoordCluster.
        """
        if value is not None:
            self.nmCoordCluster = value
        return self

    def getNmCoordinatorRole(self) -> Optional[NmCoordinatorRoleEnum]:
        """
        This attribute indicates the role the NM Coordinator will have on this channel.
        """
        return self.nmCoordinatorRole

    def setNmCoordinatorRole(self, value: Optional[NmCoordinatorRoleEnum]) -> "NmNode":
        """
        This attribute indicates the role the NM Coordinator will have on this channel.
        A None value is a no-op and does not overwrite an existing nmCoordinatorRole.
        """
        if value is not None:
            self.nmCoordinatorRole = value
        return self

    def getNmIfEcuRef(self) -> Optional[RefType]:
        """
        Reference to the NmEcu that contains this NmNode. (CommunicationController that is referenced by the Nm Node shall be contained in the EcuInstance that is referenced by the NmEcu).
        """
        return self.nmIfEcuRef

    def setNmIfEcuRef(self, value: Optional[RefType]) -> "NmNode":
        """
        Reference to the NmEcu that contains this NmNode. (CommunicationController that is referenced by the Nm Node shall be contained in the EcuInstance that is referenced by the NmEcu).
        A None value is a no-op and does not overwrite an existing nmIfEcuRef.
        """
        if value is not None:
            self.nmIfEcuRef = value
        return self

    def getNmNodeId(self) -> Optional[Integer]:
        """
        Node identifier of local NmNode. Shall be unique in the NmCluster.
        """
        return self.nmNodeId

    def setNmNodeId(self, value: Optional[Integer]) -> "NmNode":
        """
        Node identifier of local NmNode. Shall be unique in the NmCluster.
        A None value is a no-op and does not overwrite an existing nmNodeId.
        """
        if value is not None:
            self.nmNodeId = value
        return self

    def getNmPassiveModeEnabled(self) -> Optional[Boolean]:
        """
        Enables support of the Passive Mode. The passive mode is configurable per channel.
        """
        return self.nmPassiveModeEnabled

    def setNmPassiveModeEnabled(self, value: Optional[Boolean]) -> "NmNode":
        """
        Enables support of the Passive Mode. The passive mode is configurable per channel.
        A None value is a no-op and does not overwrite an existing nmPassiveModeEnabled.
        """
        if value is not None:
            self.nmPassiveModeEnabled = value
        return self

    def addRxNmPduRef(self, ref: RefType) -> "NmNode":
        """
        receive NM Pdu.
        """
        self.rxNmPduRefs.append(ref)
        return self

    def getRxNmPduRefs(self) -> List[RefType]:
        """
        receive NM Pdu.
        """
        return self.rxNmPduRefs

    def addTxNmPduRef(self, ref: RefType) -> "NmNode":
        """
        transmit NM Pdu
        """
        self.txNmPduRefs.append(ref)
        return self

    def getTxNmPduRefs(self) -> List[RefType]:
        """
        transmit NM Pdu
        """
        return self.txNmPduRefs


class CanNmNode(NmNode):
    """
    Represents a CAN network management node in the system,
    defining CAN-specific NM properties including message
    cycle offsets, timing configurations, and range settings.
    """

    # CanNmNode method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getAllNmMessagesKeepAwake    [x] impl  [ ] docstring  [ ] test
    # [ ] setAllNmMessagesKeepAwake    [x] impl  [ ] docstring  [ ] test
    # [ ] getNmCarWakeUpFilterEnabled  [x] impl  [ ] docstring  [ ] test
    # [ ] setNmCarWakeUpFilterEnabled  [x] impl  [ ] docstring  [ ] test
    # [ ] getNmCarWakeUpRxEnabled      [x] impl  [ ] docstring  [ ] test
    # [ ] setNmCarWakeUpRxEnabled      [x] impl  [ ] docstring  [ ] test
    # [ ] getNmMsgCycleOffset          [x] impl  [ ] docstring  [ ] test
    # [ ] setNmMsgCycleOffset          [x] impl  [ ] docstring  [ ] test
    # [ ] getNmMsgReducedTime          [x] impl  [ ] docstring  [ ] test
    # [ ] setNmMsgReducedTime          [x] impl  [ ] docstring  [ ] test
    # [ ] getNmRangeConfig             [x] impl  [ ] docstring  [ ] test
    # [ ] setNmRangeConfig             [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.allNmMessagesKeepAwake = None
        self.nmCarWakeUpFilterEnabled = None
        self.nmCarWakeUpRxEnabled = None
        self.nmMsgCycleOffset = None
        self.nmMsgReducedTime = None
        self.nmRangeConfig: RxIdentifierRange = None

    def getAllNmMessagesKeepAwake(self):
        return self.allNmMessagesKeepAwake

    def setAllNmMessagesKeepAwake(self, value):
        self.allNmMessagesKeepAwake = value
        return self

    def getNmCarWakeUpFilterEnabled(self):
        return self.nmCarWakeUpFilterEnabled

    def setNmCarWakeUpFilterEnabled(self, value):
        self.nmCarWakeUpFilterEnabled = value
        return self

    def getNmCarWakeUpRxEnabled(self):
        return self.nmCarWakeUpRxEnabled

    def setNmCarWakeUpRxEnabled(self, value):
        self.nmCarWakeUpRxEnabled = value
        return self

    def getNmMsgCycleOffset(self):
        return self.nmMsgCycleOffset

    def setNmMsgCycleOffset(self, value):
        self.nmMsgCycleOffset = value
        return self

    def getNmMsgReducedTime(self):
        return self.nmMsgReducedTime

    def setNmMsgReducedTime(self, value):
        self.nmMsgReducedTime = value
        return self

    def getNmRangeConfig(self) -> RxIdentifierRange:
        return self.nmRangeConfig

    def setNmRangeConfig(self, value: RxIdentifierRange):
        self.nmRangeConfig = value


class FlexrayNmNode(NmNode):
    """
    Represents a FlexRay network management node in the system,
    defining FlexRay-specific NM properties for time-triggered
    network management communication.
    """

    # FlexrayNmNode method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class J1939NmAddressConfigurationCapabilityEnum(AREnum):
    """
    Defines the Address Configuration Capability options for the J1939NmNode.
    """

    # Spec verified: R23-11
    # J1939NmAddressConfigurationCapabilityEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.322, p.692
    # (no methods)

    # Arbitrary Address Capable CA Tags: atp.EnumerationLiteralIndex=4 xml.name=J-1939-NM-AAC
    J1939NM_AAC = "J-1939-NM-AAC"

    # Command Configurable Address CA. Tags: atp.EnumerationLiteralIndex=3 xml.name=J-1939-NM-CCA
    J1939NM_CCA = "J-1939-NM-CCA"

    # Non-Configurable Address CA. Tags: atp.EnumerationLiteralIndex=0 xml.name=J-1939-NM-NCA
    J1939NM_NCA = "J-1939-NM-NCA"

    # Self-Configurable Address CA. Tags: atp.EnumerationLiteralIndex=2 xml.name=J-1939-NM-SCA
    J1939NM_SCA = "J-1939-NM-SCA"

    # Service Configurable Address CA. Tags: atp.EnumerationLiteralIndex=1 xml.name=J-1939-NM-SVCA
    J1939NM_SVCA = "J-1939-NM-SVCA"

    def __init__(self):
        super().__init__(
            (
                J1939NmAddressConfigurationCapabilityEnum.J1939NM_AAC,
                J1939NmAddressConfigurationCapabilityEnum.J1939NM_CCA,
                J1939NmAddressConfigurationCapabilityEnum.J1939NM_NCA,
                J1939NmAddressConfigurationCapabilityEnum.J1939NM_SCA,
                J1939NmAddressConfigurationCapabilityEnum.J1939NM_SVCA,
            )
        )


class J1939NodeName(ARObject):
    """
    This element contains attributes to configure the J1939NmNode NAME.
    """

    # Spec verified: R23-11
    # J1939NodeName method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.321, p.691
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                                          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getArbitraryAddressCapable                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setArbitraryAddressCapable                        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getEcuInstance                                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setEcuInstance                                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getFunction                                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setFunction                                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getFunctionInstance                               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setFunctionInstance                               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getIdentitiyNumber                                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setIdentitiyNumber                                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getIndustryGroup                                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setIndustryGroup                                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getManufacturerCode                               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setManufacturerCode                               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getVehicleSystem                                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setVehicleSystem                                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getVehicleSystemInstance                          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setVehicleSystemInstance                          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Arbitrary Address Capable field of the NAME of this node.
        self.arbitraryAddressCapable: Optional[Boolean] = None

        # ECU Instance field of the NAME of this node.
        self.ecuInstance: Optional[Integer] = None

        # Function field of the NAME of this node.
        self.function: Optional[Integer] = None

        # Function Instance field of the NAME of this node.
        self.functionInstance: Optional[Integer] = None

        # Identity Number field of the NAME of this node.
        self.identitiyNumber: Optional[Integer] = None

        # Industry Group field of the NAME of this node.
        self.industryGroup: Optional[Integer] = None

        # Manufacturer Code field of the NAME of this node.
        self.manufacturerCode: Optional[Integer] = None

        # Vehicle System field of the NAME of this node.
        self.vehicleSystem: Optional[Integer] = None

        # Vehicle System Instance field of the NAME of this node.
        self.vehicleSystemInstance: Optional[Integer] = None

    def getArbitraryAddressCapable(self) -> Optional[Boolean]:
        """
        Arbitrary Address Capable field of the NAME of this node.
        """
        return self.arbitraryAddressCapable

    def setArbitraryAddressCapable(self, value: Optional[Boolean]) -> "J1939NodeName":
        """
        Arbitrary Address Capable field of the NAME of this node.
        A None value is a no-op and does not overwrite an existing arbitraryAddressCapable.
        """
        if value is not None:
            self.arbitraryAddressCapable = value
        return self

    def getEcuInstance(self) -> Optional[Integer]:
        """
        ECU Instance field of the NAME of this node.
        """
        return self.ecuInstance

    def setEcuInstance(self, value: Optional[Integer]) -> "J1939NodeName":
        """
        ECU Instance field of the NAME of this node.
        A None value is a no-op and does not overwrite an existing ecuInstance.
        """
        if value is not None:
            self.ecuInstance = value
        return self

    def getFunction(self) -> Optional[Integer]:
        """
        Function field of the NAME of this node.
        """
        return self.function

    def setFunction(self, value: Optional[Integer]) -> "J1939NodeName":
        """
        Function field of the NAME of this node.
        A None value is a no-op and does not overwrite an existing function.
        """
        if value is not None:
            self.function = value
        return self

    def getFunctionInstance(self) -> Optional[Integer]:
        """
        Function Instance field of the NAME of this node.
        """
        return self.functionInstance

    def setFunctionInstance(self, value: Optional[Integer]) -> "J1939NodeName":
        """
        Function Instance field of the NAME of this node.
        A None value is a no-op and does not overwrite an existing functionInstance.
        """
        if value is not None:
            self.functionInstance = value
        return self

    def getIdentitiyNumber(self) -> Optional[Integer]:
        """
        Identity Number field of the NAME of this node.
        """
        return self.identitiyNumber

    def setIdentitiyNumber(self, value: Optional[Integer]) -> "J1939NodeName":
        """
        Identity Number field of the NAME of this node.
        A None value is a no-op and does not overwrite an existing identitiyNumber.
        """
        if value is not None:
            self.identitiyNumber = value
        return self

    def getIndustryGroup(self) -> Optional[Integer]:
        """
        Industry Group field of the NAME of this node.
        """
        return self.industryGroup

    def setIndustryGroup(self, value: Optional[Integer]) -> "J1939NodeName":
        """
        Industry Group field of the NAME of this node.
        A None value is a no-op and does not overwrite an existing industryGroup.
        """
        if value is not None:
            self.industryGroup = value
        return self

    def getManufacturerCode(self) -> Optional[Integer]:
        """
        Manufacturer Code field of the NAME of this node.
        """
        return self.manufacturerCode

    def setManufacturerCode(self, value: Optional[Integer]) -> "J1939NodeName":
        """
        Manufacturer Code field of the NAME of this node.
        A None value is a no-op and does not overwrite an existing manufacturerCode.
        """
        if value is not None:
            self.manufacturerCode = value
        return self

    def getVehicleSystem(self) -> Optional[Integer]:
        """
        Vehicle System field of the NAME of this node.
        """
        return self.vehicleSystem

    def setVehicleSystem(self, value: Optional[Integer]) -> "J1939NodeName":
        """
        Vehicle System field of the NAME of this node.
        A None value is a no-op and does not overwrite an existing vehicleSystem.
        """
        if value is not None:
            self.vehicleSystem = value
        return self

    def getVehicleSystemInstance(self) -> Optional[Integer]:
        """
        Vehicle System Instance field of the NAME of this node.
        """
        return self.vehicleSystemInstance

    def setVehicleSystemInstance(self, value: Optional[Integer]) -> "J1939NodeName":
        """
        Vehicle System Instance field of the NAME of this node.
        A None value is a no-op and does not overwrite an existing vehicleSystemInstance.
        """
        if value is not None:
            self.vehicleSystemInstance = value
        return self


class J1939NmNode(NmNode):
    """
    J1939 specific NM Node attributes.
    """

    # Spec verified: R23-11
    # J1939NmNode method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.320, p.691
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                                          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getAddressConfigurationCapability                 [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setAddressConfigurationCapability                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getNodeName                                       [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setNodeName                                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Defines the Address Configuration Capability of the J1939NmNode (corresponding to an SAE J1939 Controller Application, CA).
        self.addressConfigurationCapability: Optional[J1939NmAddressConfigurationCapabilityEnum] = None

        # NodeName configuration.
        self.nodeName: Optional[J1939NodeName] = None

    def getAddressConfigurationCapability(self) -> Optional[J1939NmAddressConfigurationCapabilityEnum]:
        """
        Defines the Address Configuration Capability of the J1939NmNode (corresponding to an SAE J1939 Controller Application, CA).
        """
        return self.addressConfigurationCapability

    def setAddressConfigurationCapability(self, value: Optional[J1939NmAddressConfigurationCapabilityEnum]) -> "J1939NmNode":
        """
        Defines the Address Configuration Capability of the J1939NmNode (corresponding to an SAE J1939 Controller Application, CA).
        A None value is a no-op and does not overwrite an existing addressConfigurationCapability.
        """
        if value is not None:
            self.addressConfigurationCapability = value
        return self

    def getNodeName(self) -> Optional[J1939NodeName]:
        """
        NodeName configuration.
        """
        return self.nodeName

    def setNodeName(self, value: Optional[J1939NodeName]) -> "J1939NmNode":
        """
        NodeName configuration.
        A None value is a no-op and does not overwrite an existing nodeName.
        """
        if value is not None:
            self.nodeName = value
        return self


class UdpNmNode(NmNode):
    """
    Represents a UDP network management node in the system,
    defining UDP-specific NM properties including message
    timing and wake-up capabilities.
    """

    # UdpNmNode method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getAllNmMessagesKeepAwake    [x] impl  [ ] docstring  [ ] test
    # [ ] setAllNmMessagesKeepAwake    [x] impl  [ ] docstring  [ ] test
    # [ ] getNmMsgCycleOffset          [x] impl  [ ] docstring  [ ] test
    # [ ] setNmMsgCycleOffset          [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.allNmMessagesKeepAwake: Boolean = None
        self.nmMsgCycleOffset: TimeValue = None

    def getAllNmMessagesKeepAwake(self):
        return self.allNmMessagesKeepAwake

    def setAllNmMessagesKeepAwake(self, value):
        if value is not None:
            self.allNmMessagesKeepAwake = value
        return self

    def getNmMsgCycleOffset(self):
        return self.nmMsgCycleOffset

    def setNmMsgCycleOffset(self, value):
        if value is not None:
            self.nmMsgCycleOffset = value
        return self


class BusspecificNmEcu(ARObject, ABC):
    """
    Busspecific NmEcu attributes.
    """

    # BusspecificNmEcu method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.301, p.675
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        if type(self) is BusspecificNmEcu:
            raise TypeError("BusspecificNmEcu is an abstract class.")
        super().__init__()


class CanNmEcu(BusspecificNmEcu):
    """
    CAN specific attributes.
    """

    # CanNmEcu method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.312, p.683
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # (no own attributes; reader/writer coverage via BUS-DEPENDENT-NM-ECUS dispatch)

    def __init__(self):
        super().__init__()


class FlexrayNmEcu(BusspecificNmEcu):
    """
    Defines FlexRay-specific network management ECU properties,
    implementing bus-specific NM features for FlexRay communication.
    """

    # FlexrayNmEcu method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()


class J1939NmEcu(BusspecificNmEcu):
    """
    Defines J1939-specific network management ECU properties,
    implementing bus-specific NM features for J1939 communication.
    """

    # J1939NmEcu method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()


class UdpNmEcu(BusspecificNmEcu):
    """
    Defines UDP-specific network management ECU properties,
    implementing bus-specific NM features for UDP communication
    including synchronization point capabilities.
    """

    # UdpNmEcu method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getNmSynchronizationPointEnabled [x] impl  [ ] docstring  [ ] test
    # [ ] setNmSynchronizationPointEnabled [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.nmSynchronizationPointEnabled: Boolean = None

    def getNmSynchronizationPointEnabled(self):
        return self.nmSynchronizationPointEnabled

    def setNmSynchronizationPointEnabled(self, value):
        if value is not None:
            self.nmSynchronizationPointEnabled = value
        return self


class NmEcu(Identifiable):
    """
    Represents a network management ECU in the system,
    defining properties for NM coordination, node detection,
    and communication control across different bus types.
    """

    # NmEcu method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getBusDependentNmEcus        [x] impl  [ ] docstring  [ ] test
    # [ ] addBusDependentNmEcu         [x] impl  [ ] docstring  [ ] test
    # [ ] getEcuInstanceRef            [x] impl  [ ] docstring  [ ] test
    # [ ] setEcuInstanceRef            [x] impl  [ ] docstring  [ ] test
    # [ ] getNmBusSynchronizationEnabled [x] impl  [ ] docstring  [ ] test
    # [ ] setNmBusSynchronizationEnabled [x] impl  [ ] docstring  [ ] test
    # [ ] getNmComControlEnabled       [x] impl  [ ] docstring  [ ] test
    # [ ] setNmComControlEnabled       [x] impl  [ ] docstring  [ ] test
    # [ ] getNmCoordinator             [x] impl  [ ] docstring  [ ] test
    # [ ] setNmCoordinator             [x] impl  [ ] docstring  [ ] test
    # [ ] getNmCycletimeMainFunction   [x] impl  [ ] docstring  [ ] test
    # [ ] setNmCycletimeMainFunction   [x] impl  [ ] docstring  [ ] test
    # [ ] getNmNodeDetectionEnabled    [x] impl  [ ] docstring  [ ] test
    # [ ] setNmNodeDetectionEnabled    [x] impl  [ ] docstring  [ ] test
    # [ ] getNmNodeIdEnabled           [x] impl  [ ] docstring  [ ] test
    # [ ] setNmNodeIdEnabled           [x] impl  [ ] docstring  [ ] test
    # [ ] getNmPduRxIndicationEnabled  [x] impl  [ ] docstring  [ ] test
    # [ ] setNmPduRxIndicationEnabled  [x] impl  [ ] docstring  [ ] test
    # [ ] getNmRemoteSleepIndEnabled   [x] impl  [ ] docstring  [ ] test
    # [ ] setNmRemoteSleepIndEnabled   [x] impl  [ ] docstring  [ ] test
    # [ ] getNmRepeatMsgIndEnabled     [x] impl  [ ] docstring  [ ] test
    # [ ] setNmRepeatMsgIndEnabled     [x] impl  [ ] docstring  [ ] test
    # [ ] getNmStateChangeIndEnabled   [x] impl  [ ] docstring  [ ] test
    # [ ] setNmStateChangeIndEnabled   [x] impl  [ ] docstring  [ ] test
    # [ ] getNmUserDataEnabled         [x] impl  [ ] docstring  [ ] test
    # [ ] setNmUserDataEnabled         [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.busDependentNmEcus: List[BusspecificNmEcu] = []
        self.ecuInstanceRef: RefType = None
        self.nmBusSynchronizationEnabled: Boolean = None
        self.nmComControlEnabled: Boolean = None
        self.nmCoordinator = None
        self.nmCycletimeMainFunction: TimeValue = None
        self.nmNodeDetectionEnabled: Boolean = None
        self.nmNodeIdEnabled: Boolean = None
        self.nmPduRxIndicationEnabled: Boolean = None
        self.nmRemoteSleepIndEnabled: Boolean = None
        self.nmRepeatMsgIndEnabled: Boolean = None
        self.nmStateChangeIndEnabled: Boolean = None
        self.nmUserDataEnabled: Boolean = None

    def getBusDependentNmEcus(self):
        return self.busDependentNmEcus

    def addBusDependentNmEcu(self, value):
        if value is not None:
            self.busDependentNmEcus.append(value)
        return self

    def getEcuInstanceRef(self):
        return self.ecuInstanceRef

    def setEcuInstanceRef(self, value):
        if value is not None:
            self.ecuInstanceRef = value
        return self

    def getNmBusSynchronizationEnabled(self):
        return self.nmBusSynchronizationEnabled

    def setNmBusSynchronizationEnabled(self, value):
        if value is not None:
            self.nmBusSynchronizationEnabled = value
        return self

    def getNmComControlEnabled(self):
        return self.nmComControlEnabled

    def setNmComControlEnabled(self, value):
        if value is not None:
            self.nmComControlEnabled = value
        return self

    def getNmCoordinator(self):
        return self.nmCoordinator

    def setNmCoordinator(self, value):
        if value is not None:
            self.nmCoordinator = value
        return self

    def getNmCycletimeMainFunction(self):
        return self.nmCycletimeMainFunction

    def setNmCycletimeMainFunction(self, value):
        if value is not None:
            self.nmCycletimeMainFunction = value
        return self

    def getNmNodeDetectionEnabled(self):
        return self.nmNodeDetectionEnabled

    def setNmNodeDetectionEnabled(self, value):
        if value is not None:
            self.nmNodeDetectionEnabled = value
        return self

    def getNmNodeIdEnabled(self):
        return self.nmNodeIdEnabled

    def setNmNodeIdEnabled(self, value):
        if value is not None:
            self.nmNodeIdEnabled = value
        return self

    def getNmPduRxIndicationEnabled(self):
        return self.nmPduRxIndicationEnabled

    def setNmPduRxIndicationEnabled(self, value):
        if value is not None:
            self.nmPduRxIndicationEnabled = value
        return self

    def getNmRemoteSleepIndEnabled(self):
        return self.nmRemoteSleepIndEnabled

    def setNmRemoteSleepIndEnabled(self, value):
        if value is not None:
            self.nmRemoteSleepIndEnabled = value
        return self

    def getNmRepeatMsgIndEnabled(self):
        return self.nmRepeatMsgIndEnabled

    def setNmRepeatMsgIndEnabled(self, value):
        if value is not None:
            self.nmRepeatMsgIndEnabled = value
        return self

    def getNmStateChangeIndEnabled(self):
        return self.nmStateChangeIndEnabled

    def setNmStateChangeIndEnabled(self, value):
        if value is not None:
            self.nmStateChangeIndEnabled = value
        return self

    def getNmUserDataEnabled(self):
        return self.nmUserDataEnabled

    def setNmUserDataEnabled(self, value):
        if value is not None:
            self.nmUserDataEnabled = value
        return self


class NmConfig(FibexElement):
    """
    Represents network management configuration in the system,
    defining cluster couplings and ECU configurations for
    comprehensive network management setup.
    """

    # NmConfig method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] createCanNmCluster           [x] impl  [ ] docstring  [ ] test
    # [ ] createUdpNmCluster           [x] impl  [ ] docstring  [ ] test
    # [ ] getCanNmClusters             [x] impl  [ ] docstring  [ ] test
    # [ ] getUdpNmClusters             [x] impl  [ ] docstring  [ ] test
    # [ ] getNmClusters                [x] impl  [ ] docstring  [ ] test
    # [ ] getNmClusterCouplings        [x] impl  [ ] docstring  [ ] test
    # [ ] addNmClusterCouplings        [x] impl  [ ] docstring  [ ] test
    # [ ] getNmIfEcus                  [x] impl  [ ] docstring  [ ] test
    # [ ] createNmEcu                  [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.nmClusterCouplings: List[NmClusterCoupling] = []
        self.nmIfEcus: List[NmEcu] = []

    def createCanNmCluster(self, short_name: str):  # type: (str) -> CanNmCluster
        if not self.IsElementExists(short_name, CanNmCluster):
            cluster = CanNmCluster(self, short_name)
            self.addElement(cluster)
        return self.getElement(short_name, CanNmCluster)

    def createUdpNmCluster(self, short_name: str):  # type: (str) -> UdpNmCluster
        if not self.IsElementExists(short_name, UdpNmCluster):
            cluster = UdpNmCluster(self, short_name)
            self.addElement(cluster)
        return self.getElement(short_name, UdpNmCluster)

    def getCanNmClusters(self):  # type: () -> List[CanNmCluster]
        return list(sorted(filter(lambda a: isinstance(a, CanNmCluster), self.elements), key=lambda o: o.short_name))

    def getUdpNmClusters(self):  # type: () -> List[UdpNmCluster]
        return list(sorted(filter(lambda a: isinstance(a, UdpNmCluster), self.elements), key=lambda o: o.short_name))

    def getNmClusters(self):  # type: () -> List[NmCluster]
        return list(sorted(filter(lambda a: isinstance(a, NmCluster), self.elements), key=lambda o: o.short_name))

    def getNmClusterCouplings(self):
        return self.nmClusterCouplings

    def addNmClusterCouplings(self, value):
        self.nmClusterCouplings.append(value)
        return self

    def getNmIfEcus(self):
        return self.nmIfEcus

    def createNmEcu(self, short_name: str) -> NmEcu:
        if not self.IsElementExists(short_name, NmEcu):
            cluster = NmEcu(self, short_name)
            self.addElement(cluster)
            self.nmIfEcus.append(cluster)
        return self.getElement(short_name, NmEcu)


class NmCluster(Identifiable, ABC):
    """
    Abstract base class for network management clusters,
    defining common properties for different types of
    NM clusters including communication cluster references
    and node management capabilities.
    """

    # NmCluster method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getCommunicationClusterRef   [x] impl  [ ] docstring  [ ] test
    # [ ] setCommunicationClusterRef   [x] impl  [ ] docstring  [ ] test
    # [ ] getNmChannelId               [x] impl  [ ] docstring  [ ] test
    # [ ] setNmChannelId               [x] impl  [ ] docstring  [ ] test
    # [ ] getNmChannelSleepMaster      [x] impl  [ ] docstring  [ ] test
    # [ ] setNmChannelSleepMaster      [x] impl  [ ] docstring  [ ] test
    # [ ] createCanNmNode              [x] impl  [ ] docstring  [ ] test
    # [ ] readUdpNmNode                [x] impl  [ ] docstring  [ ] test
    # [ ] createJ1939NmNode            [x] impl  [ ] docstring  [ ] test
    # [ ] getCanNmNodes                [x] impl  [ ] docstring  [ ] test
    # [ ] getUdpNmNodes                [x] impl  [ ] docstring  [ ] test
    # [ ] getJ1939NmNodes              [x] impl  [ ] docstring  [ ] test
    # [ ] getNmNodes                   [x] impl  [ ] docstring  [ ] test
    # [ ] getNmNodeDetectionEnabled    [x] impl  [ ] docstring  [ ] test
    # [ ] setNmNodeDetectionEnabled    [x] impl  [ ] docstring  [ ] test
    # [ ] getNmNodeIdEnabled           [x] impl  [ ] docstring  [ ] test
    # [ ] setNmNodeIdEnabled           [x] impl  [ ] docstring  [ ] test
    # [ ] getNmPncParticipation        [x] impl  [ ] docstring  [ ] test
    # [ ] setNmPncParticipation        [x] impl  [ ] docstring  [ ] test
    # [ ] getNmRepeatMsgIndEnabled     [x] impl  [ ] docstring  [ ] test
    # [ ] setNmRepeatMsgIndEnabled     [x] impl  [ ] docstring  [ ] test
    # [ ] getNmSynchronizingNetwork    [x] impl  [ ] docstring  [ ] test
    # [ ] setNmSynchronizingNetwork    [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is NmCluster:
            raise TypeError("NmCluster is an abstract class.")
        super().__init__(parent, short_name)

        self.communicationClusterRef = None  # type: RefType
        self.nmChannelId = None
        self.nmChannelSleepMaster = None
        self.nmNodes = []  # type: List[NmNode]
        self.nmNodeDetectionEnabled = None
        self.nmNodeIdEnabled = None
        self.nmPncParticipation = None
        self.nmRepeatMsgIndEnabled = None
        self._nmSynchronizingNetwork = None

    def getCommunicationClusterRef(self):
        return self.communicationClusterRef

    def setCommunicationClusterRef(self, value):
        self.communicationClusterRef = value
        return self

    def getNmChannelId(self):
        return self.nmChannelId

    def setNmChannelId(self, value):
        self.nmChannelId = value
        return self

    def getNmChannelSleepMaster(self):
        return self.nmChannelSleepMaster

    def setNmChannelSleepMaster(self, value):
        self.nmChannelSleepMaster = value
        return self

    def createCanNmNode(self, short_name: str) -> CanNmNode:
        if not self.IsElementExists(short_name, CanNmNode):
            node = CanNmNode(self, short_name)
            self.addElement(node)
            self.nmNodes.append(node)
        return self.getElement(short_name, CanNmNode)

    def readUdpNmNode(self, short_name: str) -> UdpNmNode:
        if not self.IsElementExists(short_name, UdpNmNode):
            node = UdpNmNode(self, short_name)
            self.addElement(node)
            self.nmNodes.append(node)
        return self.getElement(short_name, UdpNmNode)

    def createJ1939NmNode(self, short_name: str) -> J1939NmNode:
        if not self.IsElementExists(short_name, J1939NmNode):
            node = J1939NmNode(self, short_name)
            self.addElement(node)
            self.nmNodes.append(node)
        return self.getElement(short_name, J1939NmNode)

    def getCanNmNodes(self) -> List[CanNmNode]:
        return list(sorted(filter(lambda a: isinstance(a, CanNmNode), self.elements), key=lambda o: o.short_name))

    def getUdpNmNodes(self) -> List[UdpNmNode]:
        return list(sorted(filter(lambda a: isinstance(a, UdpNmNode), self.elements), key=lambda o: o.short_name))

    def getJ1939NmNodes(self) -> List[J1939NmNode]:
        return list(sorted(filter(lambda a: isinstance(a, J1939NmNode), self.elements), key=lambda o: o.short_name))

    def getNmNodes(self) -> List[NmNode]:
        return list(sorted(filter(lambda a: isinstance(a, NmNode), self.elements), key=lambda o: o.short_name))

    def getNmNodeDetectionEnabled(self):
        return self.nmNodeDetectionEnabled

    def setNmNodeDetectionEnabled(self, value):
        self.nmNodeDetectionEnabled = value
        return self

    def getNmNodeIdEnabled(self):
        return self.nmNodeIdEnabled

    def setNmNodeIdEnabled(self, value):
        self.nmNodeIdEnabled = value
        return self

    def getNmPncParticipation(self):
        return self.nmPncParticipation

    def setNmPncParticipation(self, value):
        self.nmPncParticipation = value
        return self

    def getNmRepeatMsgIndEnabled(self):
        return self.nmRepeatMsgIndEnabled

    def setNmRepeatMsgIndEnabled(self, value):
        self.nmRepeatMsgIndEnabled = value
        return self

    def getNmSynchronizingNetwork(self):
        return self._nmSynchronizingNetwork

    def setNmSynchronizingNetwork(self, value):
        self._nmSynchronizingNetwork = value
        return self


class CanNmCluster(NmCluster):
    """
    Represents a CAN network management cluster in the system,
    defining CAN-specific NM properties including busload
    reduction, wake-up configurations, and message timing.
    """

    # CanNmCluster method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getNmBusloadReductionActive  [x] impl  [ ] docstring  [ ] test
    # [ ] setNmBusloadReductionActive  [x] impl  [ ] docstring  [ ] test
    # [ ] getNmCarWakeUpBitPosition    [x] impl  [ ] docstring  [ ] test
    # [ ] setNmCarWakeUpBitPosition    [x] impl  [ ] docstring  [ ] test
    # [ ] getNmCarWakeUpFilterNodeId   [x] impl  [ ] docstring  [ ] test
    # [ ] setNmCarWakeUpFilterNodeId   [x] impl  [ ] docstring  [ ] test
    # [ ] getNmCarWakeUpRxEnabled      [x] impl  [ ] docstring  [ ] test
    # [ ] setNmCarWakeUpRxEnabled      [x] impl  [ ] docstring  [ ] test
    # [ ] getNmCbvPosition             [x] impl  [ ] docstring  [ ] test
    # [ ] setNmCbvPosition             [x] impl  [ ] docstring  [ ] test
    # [ ] getNmChannelActive           [x] impl  [ ] docstring  [ ] test
    # [ ] setNmChannelActive           [x] impl  [ ] docstring  [ ] test
    # [ ] getNmImmediateNmCycleTime    [x] impl  [ ] docstring  [ ] test
    # [ ] setNmImmediateNmCycleTime    [x] impl  [ ] docstring  [ ] test
    # [ ] getNmImmediateNmTransmissions [x] impl  [ ] docstring  [ ] test
    # [ ] setNmImmediateNmTransmissions [x] impl  [ ] docstring  [ ] test
    # [ ] getNmMessageTimeoutTime      [x] impl  [ ] docstring  [ ] test
    # [ ] setNmMessageTimeoutTime      [x] impl  [ ] docstring  [ ] test
    # [ ] getNmMsgCycleTime            [x] impl  [ ] docstring  [ ] test
    # [ ] setNmMsgCycleTime            [x] impl  [ ] docstring  [ ] test
    # [ ] getNmNetworkTimeout          [x] impl  [ ] docstring  [ ] test
    # [ ] setNmNetworkTimeout          [x] impl  [ ] docstring  [ ] test
    # [ ] getNmNidPosition             [x] impl  [ ] docstring  [ ] test
    # [ ] setNmNidPosition             [x] impl  [ ] docstring  [ ] test
    # [ ] getNmRemoteSleepIndicationTime [x] impl  [ ] docstring  [ ] test
    # [ ] setNmRemoteSleepIndicationTime [x] impl  [ ] docstring  [ ] test
    # [ ] getNmRepeatMessageTime       [x] impl  [ ] docstring  [ ] test
    # [ ] setNmRepeatMessageTime       [x] impl  [ ] docstring  [ ] test
    # [ ] getNmUserDataLength          [x] impl  [ ] docstring  [ ] test
    # [ ] setNmUserDataLength          [x] impl  [ ] docstring  [ ] test
    # [ ] getNmWaitBusSleepTime        [x] impl  [ ] docstring  [ ] test
    # [ ] setNmWaitBusSleepTime        [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.nmBusloadReductionActive = None
        self.nmCarWakeUpBitPosition = None
        self.nmCarWakeUpFilterNodeId = None
        self.nmCarWakeUpRxEnabled = None
        self.nmCbvPosition = None
        self.nmChannelActive = None
        self.nmImmediateNmCycleTime = None
        self.nmImmediateNmTransmissions = None
        self.nmMessageTimeoutTime = None
        self.nmMsgCycleTime = None
        self.nmNetworkTimeout = None
        self.nmNidPosition = None
        self.nmRemoteSleepIndicationTime = None
        self.nmRepeatMessageTime = None
        self.nmUserDataLength = None
        self.nmWaitBusSleepTime = None

    def getNmBusloadReductionActive(self):
        return self.nmBusloadReductionActive

    def setNmBusloadReductionActive(self, value):
        self.nmBusloadReductionActive = value
        return self

    def getNmCarWakeUpBitPosition(self):
        return self.nmCarWakeUpBitPosition

    def setNmCarWakeUpBitPosition(self, value):
        self.nmCarWakeUpBitPosition = value
        return self

    def getNmCarWakeUpFilterNodeId(self):
        return self.nmCarWakeUpFilterNodeId

    def setNmCarWakeUpFilterNodeId(self, value):
        self.nmCarWakeUpFilterNodeId = value
        return self

    def getNmCarWakeUpRxEnabled(self):
        return self.nmCarWakeUpRxEnabled

    def setNmCarWakeUpRxEnabled(self, value):
        self.nmCarWakeUpRxEnabled = value
        return self

    def getNmCbvPosition(self):
        return self.nmCbvPosition

    def setNmCbvPosition(self, value):
        self.nmCbvPosition = value
        return self

    def getNmChannelActive(self):
        return self.nmChannelActive

    def setNmChannelActive(self, value):
        self.nmChannelActive = value
        return self

    def getNmImmediateNmCycleTime(self):
        return self.nmImmediateNmCycleTime

    def setNmImmediateNmCycleTime(self, value):
        self.nmImmediateNmCycleTime = value
        return self

    def getNmImmediateNmTransmissions(self):
        return self.nmImmediateNmTransmissions

    def setNmImmediateNmTransmissions(self, value):
        self.nmImmediateNmTransmissions = value
        return self

    def getNmMessageTimeoutTime(self):
        return self.nmMessageTimeoutTime

    def setNmMessageTimeoutTime(self, value):
        self.nmMessageTimeoutTime = value
        return self

    def getNmMsgCycleTime(self):
        return self.nmMsgCycleTime

    def setNmMsgCycleTime(self, value):
        self.nmMsgCycleTime = value
        return self

    def getNmNetworkTimeout(self):
        return self.nmNetworkTimeout

    def setNmNetworkTimeout(self, value):
        self.nmNetworkTimeout = value
        return self

    def getNmNidPosition(self):
        return self.nmNidPosition

    def setNmNidPosition(self, value):
        self.nmNidPosition = value
        return self

    def getNmRemoteSleepIndicationTime(self):
        return self.nmRemoteSleepIndicationTime

    def setNmRemoteSleepIndicationTime(self, value):
        self.nmRemoteSleepIndicationTime = value
        return self

    def getNmRepeatMessageTime(self):
        return self.nmRepeatMessageTime

    def setNmRepeatMessageTime(self, value):
        self.nmRepeatMessageTime = value
        return self

    def getNmUserDataLength(self):
        return self.nmUserDataLength

    def setNmUserDataLength(self, value):
        self.nmUserDataLength = value
        return self

    def getNmWaitBusSleepTime(self):
        return self.nmWaitBusSleepTime

    def setNmWaitBusSleepTime(self, value):
        self.nmWaitBusSleepTime = value
        return self


class FlexrayNmCluster(NmCluster):
    """
    Represents a FlexRay network management cluster in the system,
    defining FlexRay-specific NM properties for time-triggered
    network management in FlexRay communication networks.
    """

    # FlexrayNmCluster method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class J1939NmCluster(NmCluster):
    """
    Represents a J1939 network management cluster in the system,
    defining J1939-specific NM properties for heavy-duty vehicle
    network management communication.
    """

    # J1939NmCluster method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class UdpNmClusterCoupling(NmClusterCoupling):
    """
    Defines coupling properties for UDP network management clusters,
    specifying coupled cluster references and UDP-specific NM
    immediate restart capabilities.
    """

    # UdpNmClusterCoupling method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getCoupledClusterRefs        [x] impl  [ ] docstring  [ ] test
    # [ ] addCoupledClusterRef         [x] impl  [ ] docstring  [ ] test
    # [ ] getNmImmediateRestartEnabled [x] impl  [ ] docstring  [ ] test
    # [ ] setNmImmediateRestartEnabled [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.coupledClusterRefs: List[RefType] = []
        self.nmImmediateRestartEnabled: Boolean = None

    def getCoupledClusterRefs(self):
        return self.coupledClusterRefs

    def addCoupledClusterRef(self, value):
        if value is not None:
            self.coupledClusterRefs.append(value)
        return self

    def getNmImmediateRestartEnabled(self):
        return self.nmImmediateRestartEnabled

    def setNmImmediateRestartEnabled(self, value):
        if value is not None:
            self.nmImmediateRestartEnabled = value
        return self


class UdpNmCluster(NmCluster):
    """
    Represents a UDP network management cluster in the system,
    defining UDP-specific NM properties including message timing,
    CBV (Common Bit Vector) position, and VLAN references.
    """

    # UdpNmCluster method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getNmCbvPosition             [x] impl  [ ] docstring  [ ] test
    # [ ] setNmCbvPosition             [x] impl  [ ] docstring  [ ] test
    # [ ] getNmChannelActive           [x] impl  [ ] docstring  [ ] test
    # [ ] setNmChannelActive           [x] impl  [ ] docstring  [ ] test
    # [ ] getNmImmediateNmCycleTime    [x] impl  [ ] docstring  [ ] test
    # [ ] setNmImmediateNmCycleTime    [x] impl  [ ] docstring  [ ] test
    # [ ] getNmImmediateNmTransmissions [x] impl  [ ] docstring  [ ] test
    # [ ] setNmImmediateNmTransmissions [x] impl  [ ] docstring  [ ] test
    # [ ] getNmMessageTimeoutTime      [x] impl  [ ] docstring  [ ] test
    # [ ] setNmMessageTimeoutTime      [x] impl  [ ] docstring  [ ] test
    # [ ] getNmMsgCycleTime            [x] impl  [ ] docstring  [ ] test
    # [ ] setNmMsgCycleTime            [x] impl  [ ] docstring  [ ] test
    # [ ] getNmNetworkTimeout          [x] impl  [ ] docstring  [ ] test
    # [ ] setNmNetworkTimeout          [x] impl  [ ] docstring  [ ] test
    # [ ] getNmNidPosition             [x] impl  [ ] docstring  [ ] test
    # [ ] setNmNidPosition             [x] impl  [ ] docstring  [ ] test
    # [ ] getNmRemoteSleepIndicationTime [x] impl  [ ] docstring  [ ] test
    # [ ] setNmRemoteSleepIndicationTime [x] impl  [ ] docstring  [ ] test
    # [ ] getNmRepeatMessageTime       [x] impl  [ ] docstring  [ ] test
    # [ ] setNmRepeatMessageTime       [x] impl  [ ] docstring  [ ] test
    # [ ] getNmWaitBusSleepTime        [x] impl  [ ] docstring  [ ] test
    # [ ] setNmWaitBusSleepTime        [x] impl  [ ] docstring  [ ] test
    # [ ] getVlanRef                   [x] impl  [ ] docstring  [ ] test
    # [ ] setVlanRef                   [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.nmCbvPosition: Integer = None
        self.nmChannelActive: Boolean = None
        self.nmImmediateNmCycleTime: TimeValue = None
        self.nmImmediateNmTransmissions: PositiveInteger = None
        self.nmMessageTimeoutTime: TimeValue = None
        self.nmMsgCycleTime: TimeValue = None
        self.nmNetworkTimeout: TimeValue = None
        self.nmNidPosition: Integer = None
        self.nmRemoteSleepIndicationTime: TimeValue = None
        self.nmRepeatMessageTime: TimeValue = None
        self.nmWaitBusSleepTime: TimeValue = None
        self.vlanRef: RefType = None

    def getNmCbvPosition(self):
        return self.nmCbvPosition

    def setNmCbvPosition(self, value):
        if value is not None:
            self.nmCbvPosition = value
        return self

    def getNmChannelActive(self):
        return self.nmChannelActive

    def setNmChannelActive(self, value):
        if value is not None:
            self.nmChannelActive = value
        return self

    def getNmImmediateNmCycleTime(self):
        return self.nmImmediateNmCycleTime

    def setNmImmediateNmCycleTime(self, value):
        if value is not None:
            self.nmImmediateNmCycleTime = value
        return self

    def getNmImmediateNmTransmissions(self):
        return self.nmImmediateNmTransmissions

    def setNmImmediateNmTransmissions(self, value):
        if value is not None:
            self.nmImmediateNmTransmissions = value
        return self

    def getNmMessageTimeoutTime(self):
        return self.nmMessageTimeoutTime

    def setNmMessageTimeoutTime(self, value):
        if value is not None:
            self.nmMessageTimeoutTime = value
        return self

    def getNmMsgCycleTime(self):
        return self.nmMsgCycleTime

    def setNmMsgCycleTime(self, value):
        if value is not None:
            self.nmMsgCycleTime = value
        return self

    def getNmNetworkTimeout(self):
        return self.nmNetworkTimeout

    def setNmNetworkTimeout(self, value):
        if value is not None:
            self.nmNetworkTimeout = value
        return self

    def getNmNidPosition(self):
        return self.nmNidPosition

    def setNmNidPosition(self, value):
        if value is not None:
            self.nmNidPosition = value
        return self

    def getNmRemoteSleepIndicationTime(self):
        return self.nmRemoteSleepIndicationTime

    def setNmRemoteSleepIndicationTime(self, value):
        if value is not None:
            self.nmRemoteSleepIndicationTime = value
        return self

    def getNmRepeatMessageTime(self):
        return self.nmRepeatMessageTime

    def setNmRepeatMessageTime(self, value):
        if value is not None:
            self.nmRepeatMessageTime = value
        return self

    def getNmWaitBusSleepTime(self):
        return self.nmWaitBusSleepTime

    def setNmWaitBusSleepTime(self, value):
        if value is not None:
            self.nmWaitBusSleepTime = value
        return self

    def getVlanRef(self):
        return self.vlanRef

    def setVlanRef(self, value):
        if value is not None:
            self.vlanRef = value
        return self
