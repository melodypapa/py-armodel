# This module contains AUTOSAR System Template classes for network management
# It defines CAN, FlexRay, J1939, and UDP network management configurations

from abc import ABC
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import RxIdentifierRange
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore import FibexElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, Boolean, Integer, PositiveInteger, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable


class NmClusterCoupling(ARObject, VariationPointCapable, ABC):
    """
    Attributes that are valid for each of the referenced (coupled) clusters.
    """

    # NmClusterCoupling method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.305, p.676
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

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


class NmNode(Identifiable, VariationPointCapable, ABC):
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
    FlexRay specific NM Node attributes.
    """

    # FlexrayNmNode method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.309, p.679
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

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
    FlexRay specific attributes.
    """

    # FlexrayNmEcu method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.307, p.679
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getNmHwVoteEnabled              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmHwVoteEnabled              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmMainFunctionAcrossFrCycle  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmMainFunctionAcrossFrCycle  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Switch for enabling the processing of FlexRay Hardware aggregated NM-Votes.
        self.nmHwVoteEnabled: Optional[Boolean] = None

        # Parameter describing if the execution of the FrNm_Main function crosses theFlexRay cycle boundary or not.
        self.nmMainFunctionAcrossFrCycle: Optional[Boolean] = None

    def getNmHwVoteEnabled(self) -> Optional[Boolean]:
        """
        Switch for enabling the processing of FlexRay Hardware aggregated NM-Votes.
        """
        return self.nmHwVoteEnabled

    def setNmHwVoteEnabled(self, value: Optional[Boolean]) -> "FlexrayNmEcu":
        """
        Switch for enabling the processing of FlexRay Hardware aggregated NM-Votes.
        A None value is a no-op and does not overwrite an existing nmHwVoteEnabled.
        """
        if value is not None:
            self.nmHwVoteEnabled = value
        return self

    def getNmMainFunctionAcrossFrCycle(self) -> Optional[Boolean]:
        """
        Parameter describing if the execution of the FrNm_Main function crosses theFlexRay cycle boundary or not.
        """
        return self.nmMainFunctionAcrossFrCycle

    def setNmMainFunctionAcrossFrCycle(self, value: Optional[Boolean]) -> "FlexrayNmEcu":
        """
        Parameter describing if the execution of the FrNm_Main function crosses theFlexRay cycle boundary or not.
        A None value is a no-op and does not overwrite an existing nmMainFunctionAcrossFrCycle.
        """
        if value is not None:
            self.nmMainFunctionAcrossFrCycle = value
        return self


class J1939NmEcu(BusspecificNmEcu):
    """
    J1939 NmEcu specific attributes.
    """

    # J1939NmEcu method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.323, p.694
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # (no own attributes; reader/writer coverage via BUS-DEPENDENT-NM-ECUS dispatch)

    def __init__(self):
        super().__init__()


class UdpNmEcu(BusspecificNmEcu):
    """
    Udp NM specific ECU attributes.
    """

    # UdpNmEcu method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.316, p.688 (R23-11)
    # Spec: AUTOSAR_TPS_SystemTemplate.pdf (R4.3.1), Table 6.238, p.431 (R4.3.1)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getNmSynchronizationPointEnabled [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1 (legacy)
    # [x] setNmSynchronizationPointEnabled [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1 (legacy)

    def __init__(self):
        super().__init__()

        # Enable/disable the NM Coordination algorithm to being able to initiate the synchronization algorithm.
        self.nmSynchronizationPointEnabled: Optional[Boolean] = None

    def getNmSynchronizationPointEnabled(self) -> Optional[Boolean]:
        """
        Enable/disable the NM Coordination algorithm to being able to initiate the synchronization algorithm.
        """
        return self.nmSynchronizationPointEnabled

    def setNmSynchronizationPointEnabled(self, value: Optional[Boolean]) -> "UdpNmEcu":
        """
        Enable/disable the NM Coordination algorithm to being able to initiate the synchronization algorithm.
        A None value is a no-op and does not overwrite an existing nmSynchronizationPointEnabled.
        """
        if value is not None:
            self.nmSynchronizationPointEnabled = value
        return self


class NmEcu(Identifiable, VariationPointCapable):
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
    Contains the all configuration elements for AUTOSAR Nm. Tags: atp.recommendedPackage=NmConfigs
    """

    # NmConfig method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.298, p.672
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getNmClusters           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createCanNmCluster      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createUdpNmCluster      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createFlexrayNmCluster  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createJ1939NmCluster    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCanNmClusters        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getUdpNmClusters        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getNmClusterCouplings   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addNmClusterCouplings   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmIfEcus             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createNmEcu             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Collection of NM Clusters atpVariation: Derived, because cluster can be variable. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=nmCluster.shortName, nmCluster.variationPoint.shortLabel vh.latestBindingTime=postBuild
        self.nmClusters: List[NmCluster] = []

        # Collection of NmClusterCouplings atpVariation: Derived, because NmCluster can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=nmClusterCoupling, nmClusterCoupling.variationPoint.shortLabel vh.latestBindingTime=postBuild
        self.nmClusterCouplings: List[NmClusterCoupling] = []

        # Collection of NM ECUs atpVariation: Derived, because EcuInstance can be variable. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=nmIfEcu.shortName, nmIfEcu.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.nmIfEcus: List[NmEcu] = []

    def getNmClusters(self) -> List["NmCluster"]:
        """
        Collection of NM Clusters atpVariation: Derived, because cluster can be variable. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=nmCluster.shortName, nmCluster.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        return self.nmClusters

    def createCanNmCluster(self, short_name: str) -> "CanNmCluster":
        if not self.IsElementExists(short_name, CanNmCluster):
            cluster = CanNmCluster(self, short_name)
            self.addElement(cluster)
            self.nmClusters.append(cluster)
        return self.getElement(short_name, CanNmCluster)

    def createUdpNmCluster(self, short_name: str) -> "UdpNmCluster":
        if not self.IsElementExists(short_name, UdpNmCluster):
            cluster = UdpNmCluster(self, short_name)
            self.addElement(cluster)
            self.nmClusters.append(cluster)
        return self.getElement(short_name, UdpNmCluster)

    def createFlexrayNmCluster(self, short_name: str) -> "FlexrayNmCluster":
        if not self.IsElementExists(short_name, FlexrayNmCluster):
            cluster = FlexrayNmCluster(self, short_name)
            self.addElement(cluster)
            self.nmClusters.append(cluster)
        return self.getElement(short_name, FlexrayNmCluster)

    def createJ1939NmCluster(self, short_name: str) -> "J1939NmCluster":
        if not self.IsElementExists(short_name, J1939NmCluster):
            cluster = J1939NmCluster(self, short_name)
            self.addElement(cluster)
            self.nmClusters.append(cluster)
        return self.getElement(short_name, J1939NmCluster)

    def getCanNmClusters(self) -> List["CanNmCluster"]:
        return [cluster for cluster in self.nmClusters if isinstance(cluster, CanNmCluster)]

    def getUdpNmClusters(self) -> List["UdpNmCluster"]:
        return [cluster for cluster in self.nmClusters if isinstance(cluster, UdpNmCluster)]

    def getNmClusterCouplings(self) -> List[NmClusterCoupling]:
        """
        Collection of NmClusterCouplings atpVariation: Derived, because NmCluster can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=nmClusterCoupling, nmClusterCoupling.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        return self.nmClusterCouplings

    def addNmClusterCouplings(self, value: Optional[NmClusterCoupling]) -> "NmConfig":
        """
        Collection of NmClusterCouplings atpVariation: Derived, because NmCluster can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=nmClusterCoupling, nmClusterCoupling.variationPoint.shortLabel vh.latestBindingTime=postBuild
        A None value is a no-op and does not extend the nmClusterCoupling list.
        """
        if value is not None:
            self.nmClusterCouplings.append(value)
        return self

    def getNmIfEcus(self) -> List[NmEcu]:
        """
        Collection of NM ECUs atpVariation: Derived, because EcuInstance can be variable. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=nmIfEcu.shortName, nmIfEcu.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """
        return self.nmIfEcus

    def createNmEcu(self, short_name: str) -> NmEcu:
        if not self.IsElementExists(short_name, NmEcu):
            cluster = NmEcu(self, short_name)
            self.addElement(cluster)
            self.nmIfEcus.append(cluster)
        return self.getElement(short_name, NmEcu)


class NmCluster(Identifiable, VariationPointCapable, ABC):
    """
    Set of NM nodes coordinated with use of the NM algorithm.
    """

    # NmCluster method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.299, p.673
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCommunicationClusterRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCommunicationClusterRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmChannelSleepMaster     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmChannelSleepMaster     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createCanNmNode             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createUdpNmNode             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createJ1939NmNode           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCanNmNodes               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getUdpNmNodes               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getJ1939NmNodes             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getNmNodes                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getNmNodeDetectionEnabled   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmNodeDetectionEnabled   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmNodeIdEnabled          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmNodeIdEnabled          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmPncParticipation       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmPncParticipation       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmRepeatMsgIndEnabled    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmRepeatMsgIndEnabled    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmSynchronizingNetwork   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmSynchronizingNetwork   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPncClusterVectorLength   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPncClusterVectorLength   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmChannelId              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11 (legacy: removed, XSD-only; see deviation note)
    # [x] setNmChannelId              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11 (legacy: removed, XSD-only; see deviation note)

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is NmCluster:
            raise TypeError("NmCluster is an abstract class.")
        super().__init__(parent, short_name)

        # Association to a CommunicationCluster in the topology description.
        self.communicationClusterRef: Optional[RefType] = None

        # This parameter shall be set to indicate if the sleep of this network can be absolutely decided by the local node only and that no other nodes can oppose that decision.
        self.nmChannelSleepMaster: Optional[Boolean] = None

        # Collection of NmNodes of the NmCluster. atpVariation: Derived, because NmNode can be variable. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=nmNode.shortName, nmNode.variationPoint.shortLabel vh.latestBindingTime=postBuild
        self.nmNodes: List[NmNode] = []

        # Enables the Request Repeat Message Request support. Only valid if nmNodeIdEnabled is set to true.
        self.nmNodeDetectionEnabled: Optional[Boolean] = None

        # Enables the source node identifier.
        self.nmNodeIdEnabled: Optional[Boolean] = None

        # Defines whether this NmCluster contributes to the partial network mechanism.
        self.nmPncParticipation: Optional[Boolean] = None

        # Switch for enabling the Repeat Message Bit Indication.
        self.nmRepeatMsgIndEnabled: Optional[Boolean] = None

        # If this parameter is true, then this network is a synchronizing network for the NM coordination cluster which it belongs to. The network is expected to call Nm_SynchronizationPoint() at regular intervals.
        self.nmSynchronizingNetwork: Optional[Boolean] = None

        # Optionally defines the length of the PNC Vector per CommunicationCluster (and VLAN in case of UdpNm). If not defined then System.pncVectorLength applies. Should only make the PNC Vector shorter (or same length as defined in System.pncVectorLength).
        self.pncClusterVectorLength: Optional[PositiveInteger] = None

        # This attribute has the status "removed" and shall not be used any longer. Old description: Channel identification number of the corresponding channel. Must be unique over all NmClusters.
        self.nmChannelId: Optional[Integer] = None

    def getCommunicationClusterRef(self) -> Optional[RefType]:
        """
        Association to a CommunicationCluster in the topology description.
        """
        return self.communicationClusterRef

    def setCommunicationClusterRef(self, value: Optional[RefType]) -> "NmCluster":
        """
        Association to a CommunicationCluster in the topology description.
        A None value is a no-op and does not overwrite an existing communicationClusterRef.
        """
        if value is not None:
            self.communicationClusterRef = value
        return self

    def getNmChannelSleepMaster(self) -> Optional[Boolean]:
        """
        This parameter shall be set to indicate if the sleep of this network can be absolutely decided by the local node only and that no other nodes can oppose that decision.
        """
        return self.nmChannelSleepMaster

    def setNmChannelSleepMaster(self, value: Optional[Boolean]) -> "NmCluster":
        """
        This parameter shall be set to indicate if the sleep of this network can be absolutely decided by the local node only and that no other nodes can oppose that decision.
        A None value is a no-op and does not overwrite an existing nmChannelSleepMaster.
        """
        if value is not None:
            self.nmChannelSleepMaster = value
        return self

    def createCanNmNode(self, short_name: str) -> CanNmNode:
        if not self.IsElementExists(short_name, CanNmNode):
            node = CanNmNode(self, short_name)
            self.addElement(node)
            self.nmNodes.append(node)
        return self.getElement(short_name, CanNmNode)

    def createUdpNmNode(self, short_name: str) -> UdpNmNode:
        if not self.IsElementExists(short_name, UdpNmNode):
            node = UdpNmNode(self, short_name)
            self.addElement(node)
            self.nmNodes.append(node)
        return self.getElement(short_name, UdpNmNode)

    def createFlexrayNmNode(self, short_name: str) -> "FlexrayNmNode":
        if not self.IsElementExists(short_name, FlexrayNmNode):
            node = FlexrayNmNode(self, short_name)
            self.addElement(node)
            self.nmNodes.append(node)
        return self.getElement(short_name, FlexrayNmNode)

    def createJ1939NmNode(self, short_name: str) -> J1939NmNode:
        if not self.IsElementExists(short_name, J1939NmNode):
            node = J1939NmNode(self, short_name)
            self.addElement(node)
            self.nmNodes.append(node)
        return self.getElement(short_name, J1939NmNode)

    def getCanNmNodes(self) -> List[CanNmNode]:
        return [node for node in self.nmNodes if isinstance(node, CanNmNode)]

    def getUdpNmNodes(self) -> List[UdpNmNode]:
        return [node for node in self.nmNodes if isinstance(node, UdpNmNode)]

    def getJ1939NmNodes(self) -> List[J1939NmNode]:
        return [node for node in self.nmNodes if isinstance(node, J1939NmNode)]

    def getNmNodes(self) -> List[NmNode]:
        return self.nmNodes

    def getNmNodeDetectionEnabled(self) -> Optional[Boolean]:
        """
        Enables the Request Repeat Message Request support. Only valid if nmNodeIdEnabled is set to true.
        """
        return self.nmNodeDetectionEnabled

    def setNmNodeDetectionEnabled(self, value: Optional[Boolean]) -> "NmCluster":
        """
        Enables the Request Repeat Message Request support. Only valid if nmNodeIdEnabled is set to true.
        A None value is a no-op and does not overwrite an existing nmNodeDetectionEnabled.
        """
        if value is not None:
            self.nmNodeDetectionEnabled = value
        return self

    def getNmNodeIdEnabled(self) -> Optional[Boolean]:
        """
        Enables the source node identifier.
        """
        return self.nmNodeIdEnabled

    def setNmNodeIdEnabled(self, value: Optional[Boolean]) -> "NmCluster":
        """
        Enables the source node identifier.
        A None value is a no-op and does not overwrite an existing nmNodeIdEnabled.
        """
        if value is not None:
            self.nmNodeIdEnabled = value
        return self

    def getNmPncParticipation(self) -> Optional[Boolean]:
        """
        Defines whether this NmCluster contributes to the partial network mechanism.
        """
        return self.nmPncParticipation

    def setNmPncParticipation(self, value: Optional[Boolean]) -> "NmCluster":
        """
        Defines whether this NmCluster contributes to the partial network mechanism.
        A None value is a no-op and does not overwrite an existing nmPncParticipation.
        """
        if value is not None:
            self.nmPncParticipation = value
        return self

    def getNmRepeatMsgIndEnabled(self) -> Optional[Boolean]:
        """
        Switch for enabling the Repeat Message Bit Indication.
        """
        return self.nmRepeatMsgIndEnabled

    def setNmRepeatMsgIndEnabled(self, value: Optional[Boolean]) -> "NmCluster":
        """
        Switch for enabling the Repeat Message Bit Indication.
        A None value is a no-op and does not overwrite an existing nmRepeatMsgIndEnabled.
        """
        if value is not None:
            self.nmRepeatMsgIndEnabled = value
        return self

    def getNmSynchronizingNetwork(self) -> Optional[Boolean]:
        """
        If this parameter is true, then this network is a synchronizing network for the NM coordination cluster which it belongs to. The network is expected to call Nm_SynchronizationPoint() at regular intervals.
        """
        return self.nmSynchronizingNetwork

    def setNmSynchronizingNetwork(self, value: Optional[Boolean]) -> "NmCluster":
        """
        If this parameter is true, then this network is a synchronizing network for the NM coordination cluster which it belongs to. The network is expected to call Nm_SynchronizationPoint() at regular intervals.
        A None value is a no-op and does not overwrite an existing nmSynchronizingNetwork.
        """
        if value is not None:
            self.nmSynchronizingNetwork = value
        return self

    def getPncClusterVectorLength(self) -> Optional[PositiveInteger]:
        """
        Optionally defines the length of the PNC Vector per CommunicationCluster (and VLAN in case of UdpNm). If not defined then System.pncVectorLength applies. Should only make the PNC Vector shorter (or same length as defined in System.pncVectorLength).
        """
        return self.pncClusterVectorLength

    def setPncClusterVectorLength(self, value: Optional[PositiveInteger]) -> "NmCluster":
        """
        Optionally defines the length of the PNC Vector per CommunicationCluster (and VLAN in case of UdpNm). If not defined then System.pncVectorLength applies. Should only make the PNC Vector shorter (or same length as defined in System.pncVectorLength).
        A None value is a no-op and does not overwrite an existing pncClusterVectorLength.
        """
        if value is not None:
            self.pncClusterVectorLength = value
        return self

    def getNmChannelId(self) -> Optional[Integer]:
        """
        This attribute has the status "removed" and shall not be used any longer. Old description: Channel identification number of the corresponding channel. Must be unique over all NmClusters.
        """
        return self.nmChannelId

    def setNmChannelId(self, value: Optional[Integer]) -> "NmCluster":
        """
        This attribute has the status "removed" and shall not be used any longer. Old description: Channel identification number of the corresponding channel. Must be unique over all NmClusters.
        A None value is a no-op and does not overwrite an existing nmChannelId.
        """
        if value is not None:
            self.nmChannelId = value
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
    FlexRay specific NM cluster attributes.
    """

    # FlexrayNmCluster method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.306, p.678
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getNmCarWakeUpBitPosition       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmCarWakeUpBitPosition       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmCarWakeUpFilterEnabled     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmCarWakeUpFilterEnabled     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmCarWakeUpFilterNodeId      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmCarWakeUpFilterNodeId      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmCarWakeUpRxEnabled         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmCarWakeUpRxEnabled         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmDataCycle                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmDataCycle                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmMainFunctionPeriod         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmMainFunctionPeriod         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmRemoteSleepIndicationTime  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmRemoteSleepIndicationTime  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmRepeatMessageTime          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmRepeatMessageTime          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmRepetitionCycle            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmRepetitionCycle            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmVotingCycle                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmVotingCycle                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Specifies the bit position of the CarWakeUp within the NmPdu.
        self.nmCarWakeUpBitPosition: Optional[PositiveInteger] = None

        # If this attribute is set to true the CareWakeUp filtering is supported. In this case only the CarWakeUp bit within the NmPdu with source node identifier nmCarWakeUpFilterNodeId is considered as CarWakeUp request.
        self.nmCarWakeUpFilterEnabled: Optional[Boolean] = None

        # Source node identifier for CarWakeUp filtering. If CarWakeUp filtering is supported (nmCarWakeUpFilterEnabled), only the CarWakeUp bit within the NmPdu with source node identifier nmCarWakeUpFilterNodeId is considered as CarWakeUp request.
        self.nmCarWakeUpFilterNodeId: Optional[PositiveInteger] = None

        # If set to true this attribute enables the support of CarWakeUp bit evaluation in received NmPdus.
        self.nmCarWakeUpRxEnabled: Optional[Boolean] = None

        # Number of FlexRay Communication Cycles needed to transmit the Nm Data PDUs of all FlexRay Nm Ecus of this FlexRayNmCluster.
        self.nmDataCycle: Optional[Integer] = None

        # Defines the processing cycle of the main function of FrNm module.
        self.nmMainFunctionPeriod: Optional[TimeValue] = None

        # Timeout for Remote Sleep Indication in seconds. It defines the time how long it shall take to recognize that all other nodes are ready to sleep.
        self.nmRemoteSleepIndicationTime: Optional[TimeValue] = None

        # Timeout for Repeat Message State in seconds. Defines the time how long the NM shall stay in the Repeat Message State.
        self.nmRepeatMessageTime: Optional[TimeValue] = None

        # Number of FlexRay Communication Cycles used to repeat the transmission of the Nm vote Pdus of all FlexRay NmEcus of this FlexRayNmCluster. This value shall be an integral multiple of nmVotingCycle.
        self.nmRepetitionCycle: Optional[Integer] = None

        # Number of FlexRay CommunicationCycles needed to transmit the Nm vote of Pdus of all FlexRay NmEcus of this FlexRayNmCluster.
        self.nmVotingCycle: Optional[Integer] = None

    def getNmCarWakeUpBitPosition(self) -> Optional[PositiveInteger]:
        """
        Specifies the bit position of the CarWakeUp within the NmPdu.
        """
        return self.nmCarWakeUpBitPosition

    def setNmCarWakeUpBitPosition(self, value: Optional[PositiveInteger]) -> "FlexrayNmCluster":
        """
        Specifies the bit position of the CarWakeUp within the NmPdu.
        A None value is a no-op and does not overwrite an existing nmCarWakeUpBitPosition.
        """
        if value is not None:
            self.nmCarWakeUpBitPosition = value
        return self

    def getNmCarWakeUpFilterEnabled(self) -> Optional[Boolean]:
        """
        If this attribute is set to true the CareWakeUp filtering is supported. In this case only the CarWakeUp bit within the NmPdu with source node identifier nmCarWakeUpFilterNodeId is considered as CarWakeUp request.
        """
        return self.nmCarWakeUpFilterEnabled

    def setNmCarWakeUpFilterEnabled(self, value: Optional[Boolean]) -> "FlexrayNmCluster":
        """
        If this attribute is set to true the CareWakeUp filtering is supported. In this case only the CarWakeUp bit within the NmPdu with source node identifier nmCarWakeUpFilterNodeId is considered as CarWakeUp request.
        A None value is a no-op and does not overwrite an existing nmCarWakeUpFilterEnabled.
        """
        if value is not None:
            self.nmCarWakeUpFilterEnabled = value
        return self

    def getNmCarWakeUpFilterNodeId(self) -> Optional[PositiveInteger]:
        """
        Source node identifier for CarWakeUp filtering. If CarWakeUp filtering is supported (nmCarWakeUpFilterEnabled), only the CarWakeUp bit within the NmPdu with source node identifier nmCarWakeUpFilterNodeId is considered as CarWakeUp request.
        """
        return self.nmCarWakeUpFilterNodeId

    def setNmCarWakeUpFilterNodeId(self, value: Optional[PositiveInteger]) -> "FlexrayNmCluster":
        """
        Source node identifier for CarWakeUp filtering. If CarWakeUp filtering is supported (nmCarWakeUpFilterEnabled), only the CarWakeUp bit within the NmPdu with source node identifier nmCarWakeUpFilterNodeId is considered as CarWakeUp request.
        A None value is a no-op and does not overwrite an existing nmCarWakeUpFilterNodeId.
        """
        if value is not None:
            self.nmCarWakeUpFilterNodeId = value
        return self

    def getNmCarWakeUpRxEnabled(self) -> Optional[Boolean]:
        """
        If set to true this attribute enables the support of CarWakeUp bit evaluation in received NmPdus.
        """
        return self.nmCarWakeUpRxEnabled

    def setNmCarWakeUpRxEnabled(self, value: Optional[Boolean]) -> "FlexrayNmCluster":
        """
        If set to true this attribute enables the support of CarWakeUp bit evaluation in received NmPdus.
        A None value is a no-op and does not overwrite an existing nmCarWakeUpRxEnabled.
        """
        if value is not None:
            self.nmCarWakeUpRxEnabled = value
        return self

    def getNmDataCycle(self) -> Optional[Integer]:
        """
        Number of FlexRay Communication Cycles needed to transmit the Nm Data PDUs of all FlexRay Nm Ecus of this FlexRayNmCluster.
        """
        return self.nmDataCycle

    def setNmDataCycle(self, value: Optional[Integer]) -> "FlexrayNmCluster":
        """
        Number of FlexRay Communication Cycles needed to transmit the Nm Data PDUs of all FlexRay Nm Ecus of this FlexRayNmCluster.
        A None value is a no-op and does not overwrite an existing nmDataCycle.
        """
        if value is not None:
            self.nmDataCycle = value
        return self

    def getNmMainFunctionPeriod(self) -> Optional[TimeValue]:
        """
        Defines the processing cycle of the main function of FrNm module.
        """
        return self.nmMainFunctionPeriod

    def setNmMainFunctionPeriod(self, value: Optional[TimeValue]) -> "FlexrayNmCluster":
        """
        Defines the processing cycle of the main function of FrNm module.
        A None value is a no-op and does not overwrite an existing nmMainFunctionPeriod.
        """
        if value is not None:
            self.nmMainFunctionPeriod = value
        return self

    def getNmRemoteSleepIndicationTime(self) -> Optional[TimeValue]:
        """
        Timeout for Remote Sleep Indication in seconds. It defines the time how long it shall take to recognize that all other nodes are ready to sleep.
        """
        return self.nmRemoteSleepIndicationTime

    def setNmRemoteSleepIndicationTime(self, value: Optional[TimeValue]) -> "FlexrayNmCluster":
        """
        Timeout for Remote Sleep Indication in seconds. It defines the time how long it shall take to recognize that all other nodes are ready to sleep.
        A None value is a no-op and does not overwrite an existing nmRemoteSleepIndicationTime.
        """
        if value is not None:
            self.nmRemoteSleepIndicationTime = value
        return self

    def getNmRepeatMessageTime(self) -> Optional[TimeValue]:
        """
        Timeout for Repeat Message State in seconds. Defines the time how long the NM shall stay in the Repeat Message State.
        """
        return self.nmRepeatMessageTime

    def setNmRepeatMessageTime(self, value: Optional[TimeValue]) -> "FlexrayNmCluster":
        """
        Timeout for Repeat Message State in seconds. Defines the time how long the NM shall stay in the Repeat Message State.
        A None value is a no-op and does not overwrite an existing nmRepeatMessageTime.
        """
        if value is not None:
            self.nmRepeatMessageTime = value
        return self

    def getNmRepetitionCycle(self) -> Optional[Integer]:
        """
        Number of FlexRay Communication Cycles used to repeat the transmission of the Nm vote Pdus of all FlexRay NmEcus of this FlexRayNmCluster. This value shall be an integral multiple of nmVotingCycle.
        """
        return self.nmRepetitionCycle

    def setNmRepetitionCycle(self, value: Optional[Integer]) -> "FlexrayNmCluster":
        """
        Number of FlexRay Communication Cycles used to repeat the transmission of the Nm vote Pdus of all FlexRay NmEcus of this FlexRayNmCluster. This value shall be an integral multiple of nmVotingCycle.
        A None value is a no-op and does not overwrite an existing nmRepetitionCycle.
        """
        if value is not None:
            self.nmRepetitionCycle = value
        return self

    def getNmVotingCycle(self) -> Optional[Integer]:
        """
        Number of FlexRay CommunicationCycles needed to transmit the Nm vote of Pdus of all FlexRay NmEcus of this FlexRayNmCluster.
        """
        return self.nmVotingCycle

    def setNmVotingCycle(self, value: Optional[Integer]) -> "FlexrayNmCluster":
        """
        Number of FlexRay CommunicationCycles needed to transmit the Nm vote of Pdus of all FlexRay NmEcus of this FlexRayNmCluster.
        A None value is a no-op and does not overwrite an existing nmVotingCycle.
        """
        if value is not None:
            self.nmVotingCycle = value
        return self


class J1939NmCluster(NmCluster):
    """
    J1939 specific NmCluster attributes
    """

    # J1939NmCluster method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.319, p.691
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAddressClaimEnabled      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAddressClaimEnabled      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getUsesDynamicAddressing    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setUsesDynamicAddressing    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute specifies whether the J1939Nm Bsw module is used or not. If this attribute is set to false then the J1939Nm configuration shall not be derived from the system description. But even in this case the nmNodeId might still be necessary for the J1939Rm and J1939Tp.
        self.addressClaimEnabled: Optional[Boolean] = None

        # Defines whether fully dynamic address resolution according to SAE J1939-81 shall be supported on this J1939NmCluster. • True: The dynamically allocated addresses on the bus are matched at runtime to the configured addresses. • False: The addresses on the bus resemble the configured addresses.
        self.usesDynamicAddressing: Optional[Boolean] = None

    def getAddressClaimEnabled(self) -> Optional[Boolean]:
        """
        This attribute specifies whether the J1939Nm Bsw module is used or not. If this attribute is set to false then the J1939Nm configuration shall not be derived from the system description. But even in this case the nmNodeId might still be necessary for the J1939Rm and J1939Tp.
        """
        return self.addressClaimEnabled

    def setAddressClaimEnabled(self, value: Optional[Boolean]) -> "J1939NmCluster":
        """
        This attribute specifies whether the J1939Nm Bsw module is used or not. If this attribute is set to false then the J1939Nm configuration shall not be derived from the system description. But even in this case the nmNodeId might still be necessary for the J1939Rm and J1939Tp.
        A None value is a no-op and does not overwrite an existing addressClaimEnabled.
        """
        if value is not None:
            self.addressClaimEnabled = value
        return self

    def getUsesDynamicAddressing(self) -> Optional[Boolean]:
        """
        Defines whether fully dynamic address resolution according to SAE J1939-81 shall be supported on this J1939NmCluster. • True: The dynamically allocated addresses on the bus are matched at runtime to the configured addresses. • False: The addresses on the bus resemble the configured addresses.
        """
        return self.usesDynamicAddressing

    def setUsesDynamicAddressing(self, value: Optional[Boolean]) -> "J1939NmCluster":
        """
        Defines whether fully dynamic address resolution according to SAE J1939-81 shall be supported on this J1939NmCluster. • True: The dynamically allocated addresses on the bus are matched at runtime to the configured addresses. • False: The addresses on the bus resemble the configured addresses.
        A None value is a no-op and does not overwrite an existing usesDynamicAddressing.
        """
        if value is not None:
            self.usesDynamicAddressing = value
        return self


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
