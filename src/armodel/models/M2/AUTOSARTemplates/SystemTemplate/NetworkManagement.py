from __future__ import annotations

# This module contains AUTOSAR System Template classes for network management
# It defines CAN, FlexRay, J1939, and UDP network management configurations

from abc import ABC
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from typing import List, Optional, cast
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
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        if type(self) is NmClusterCoupling:
            raise TypeError("NmClusterCoupling is an abstract class.")

        super().__init__()


class CanNmClusterCoupling(NmClusterCoupling):
    """
    CAN attributes that are valid for each of the referenced (coupled) CAN clusters.
    """

    # CanNmClusterCoupling method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.313, p.684
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addCoupledClusterRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCoupledClusterRefs          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getNmBusloadReductionEnabled   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmBusloadReductionEnabled   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmImmediateRestartEnabled   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmImmediateRestartEnabled   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Reference to coupled CAN Clusters.
        self.coupledClusterRefs: List[RefType] = []

        # Enables busload reduction support
        self.nmBusloadReductionEnabled: Optional[Boolean] = None

        # Enables the asynchronous transmission of a CanNm PDU upon bus-communication request in Prepare-Bus-Sleep mode.
        self.nmImmediateRestartEnabled: Optional[Boolean] = None

    def addCoupledClusterRef(self, ref: RefType) -> CanNmClusterCoupling:
        """
        Reference to coupled CAN Clusters.
        """
        self.coupledClusterRefs.append(ref)
        return self

    def getCoupledClusterRefs(self) -> List[RefType]:
        """
        Reference to coupled CAN Clusters.
        """
        return self.coupledClusterRefs

    def getNmBusloadReductionEnabled(self) -> Optional[Boolean]:
        """
        Enables busload reduction support
        """
        return self.nmBusloadReductionEnabled

    def setNmBusloadReductionEnabled(self, value: Optional[Boolean]) -> CanNmClusterCoupling:
        """
        Enables busload reduction support
        A None value is a no-op and does not overwrite an existing nmBusloadReductionEnabled.
        """
        if value is not None:
            self.nmBusloadReductionEnabled = value
        return self

    def getNmImmediateRestartEnabled(self) -> Optional[Boolean]:
        """
        Enables the asynchronous transmission of a CanNm PDU upon bus-communication request in Prepare-Bus-Sleep mode.
        """
        return self.nmImmediateRestartEnabled

    def setNmImmediateRestartEnabled(self, value: Optional[Boolean]) -> CanNmClusterCoupling:
        """
        Enables the asynchronous transmission of a CanNm PDU upon bus-communication request in Prepare-Bus-Sleep mode.
        A None value is a no-op and does not overwrite an existing nmImmediateRestartEnabled.
        """
        if value is not None:
            self.nmImmediateRestartEnabled = value
        return self


class FlexrayNmClusterCoupling(NmClusterCoupling):
    """
    FlexRay attributes that are valid for each of the referenced (coupled) FlexRay clusters.
    """

    # FlexrayNmClusterCoupling method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.308, p.679
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addCoupledClusterRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCoupledClusterRefs          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getNmScheduleVariant           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmScheduleVariant           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Reference to coupled FlexRay Clusters.
        self.coupledClusterRefs: List[RefType] = []

        # FrNm schedule variant according to FrNm SWS.
        self.nmScheduleVariant: Optional[FlexrayNmScheduleVariant] = None

    def addCoupledClusterRef(self, ref: RefType) -> FlexrayNmClusterCoupling:
        """
        Reference to coupled FlexRay Clusters.
        """
        self.coupledClusterRefs.append(ref)
        return self

    def getCoupledClusterRefs(self) -> List[RefType]:
        """
        Reference to coupled FlexRay Clusters.
        """
        return self.coupledClusterRefs

    def getNmScheduleVariant(self) -> Optional[FlexrayNmScheduleVariant]:
        """
        FrNm schedule variant according to FrNm SWS.
        """
        return self.nmScheduleVariant

    def setNmScheduleVariant(self, value: Optional[FlexrayNmScheduleVariant]) -> FlexrayNmClusterCoupling:
        """
        FrNm schedule variant according to FrNm SWS.
        A None value is a no-op and does not overwrite an existing nmScheduleVariant.
        """
        if value is not None:
            self.nmScheduleVariant = value
        return self


class FlexrayNmScheduleVariant(AREnum):
    """
    FrNm schedule variant according to FrNm SWS.
    """

    # FlexrayNmScheduleVariant method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.310, p.680
    # (no methods)

    # NM-Vote and NM Data transmitted within one PDU in static segment. The NM-Vote has to be realized as separate bit within the PDU. Tags: atp.EnumerationLiteralIndex=0
    SCHEDULE_VARIANT_1 = "SCHEDULE-VARIANT-1"

    # NM-Vote and NM-Data transmitted within one PDU in dynamic segment. The presence (or non-presence) of the PDU corresponds to the NM-Vote Tags: atp.EnumerationLiteralIndex=1
    SCHEDULE_VARIANT_2 = "SCHEDULE-VARIANT-2"

    # NM-Vote and NM-Data are transmitted in the static segment in separate PDUs. This alternative is not recommended => Alternative 1 should be used instead. Tags: atp.EnumerationLiteralIndex=2
    SCHEDULE_VARIANT_3 = "SCHEDULE-VARIANT-3"

    # NM-Vote transmitted in static and NM-Data transmitted in dynamic segment. Tags: atp.EnumerationLiteralIndex=3
    SCHEDULE_VARIANT_4 = "SCHEDULE-VARIANT-4"

    # NM-Vote is transmitted in dynamic and NM-Data is transmitted in static segment. This alternative is not recommended => Variants 2 or 6 should be used instead. Tags: atp.EnumerationLiteralIndex=4
    SCHEDULE_VARIANT_5 = "SCHEDULE-VARIANT-5"

    # NM-Vote and NM-Data are transmitted in dynamic segment in separate PDUs. Tags: atp.EnumerationLiteralIndex=5
    SCHEDULE_VARIANT_6 = "SCHEDULE-VARIANT-6"

    # NM-Vote and a copy of the CBV are transmitted in the static segment (using the FlexRay NM Vector support) and NM-Data is transmitted in the dynamic segment Tags: atp.EnumerationLiteralIndex=6
    SCHEDULE_VARIANT_7 = "SCHEDULE-VARIANT-7"

    def __init__(self):
        super().__init__(
            [
                FlexrayNmScheduleVariant.SCHEDULE_VARIANT_1,
                FlexrayNmScheduleVariant.SCHEDULE_VARIANT_2,
                FlexrayNmScheduleVariant.SCHEDULE_VARIANT_3,
                FlexrayNmScheduleVariant.SCHEDULE_VARIANT_4,
                FlexrayNmScheduleVariant.SCHEDULE_VARIANT_5,
                FlexrayNmScheduleVariant.SCHEDULE_VARIANT_6,
                FlexrayNmScheduleVariant.SCHEDULE_VARIANT_7,
            ]
        )


class NmCoordinatorRoleEnum(AREnum):
    """
    Supported NmCoordinator roles.
    """

    # NmCoordinatorRoleEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.304, p.676
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — serialized as value form on NmNode.nmCoordinatorRole
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # Coordinator which "actively" performs NmCoordinator functionality at this channel Tags: atp.EnumerationLiteralIndex=0
    ACTIVE = "ACTIVE"

    # Coordinator which "passively" performs NmCoordinator functionality at this channel - used at Nm CoordinatorSync use case. Tags: atp.EnumerationLiteralIndex=1
    PASSIVE = "PASSIVE"

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
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                                          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getControllerRef                                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setControllerRef                                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmCoordCluster                                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmCoordCluster                                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmCoordinatorRole                              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmCoordinatorRole                              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmIfEcuRef                                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmIfEcuRef                                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmNodeId                                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmNodeId                                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmPassiveModeEnabled                           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmPassiveModeEnabled                           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addRxNmPduRef                                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRxNmPduRefs                                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addTxNmPduRef                                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTxNmPduRefs                                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

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

    def setControllerRef(self, value: Optional[RefType]) -> NmNode:
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

    def setNmCoordCluster(self, value: Optional[PositiveInteger]) -> NmNode:
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

    def setNmCoordinatorRole(self, value: Optional[NmCoordinatorRoleEnum]) -> NmNode:
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

    def setNmIfEcuRef(self, value: Optional[RefType]) -> NmNode:
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

    def setNmNodeId(self, value: Optional[Integer]) -> NmNode:
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

    def setNmPassiveModeEnabled(self, value: Optional[Boolean]) -> NmNode:
        """
        Enables support of the Passive Mode. The passive mode is configurable per channel.
        A None value is a no-op and does not overwrite an existing nmPassiveModeEnabled.
        """
        if value is not None:
            self.nmPassiveModeEnabled = value
        return self

    def addRxNmPduRef(self, ref: RefType) -> NmNode:
        """
        receive NM Pdu.
        A None value is a no-op and does not extend the rxNmPduRefs list.
        """
        if ref is not None:
            self.rxNmPduRefs.append(ref)
        return self

    def getRxNmPduRefs(self) -> List[RefType]:
        """
        receive NM Pdu.
        """
        return self.rxNmPduRefs

    def addTxNmPduRef(self, ref: RefType) -> NmNode:
        """
        transmit NM Pdu
        A None value is a no-op and does not extend the txNmPduRefs list.
        """
        if ref is not None:
            self.txNmPduRefs.append(ref)
        return self

    def getTxNmPduRefs(self) -> List[RefType]:
        """
        transmit NM Pdu
        """
        return self.txNmPduRefs


class CanNmNode(NmNode):
    """
    CAN specific NM Node attributes.
    """

    # CanNmNode method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.314, p.684
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAllNmMessagesKeepAwake    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAllNmMessagesKeepAwake    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmCarWakeUpFilterEnabled  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmCarWakeUpFilterEnabled  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmCarWakeUpRxEnabled      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmCarWakeUpRxEnabled      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmMsgCycleOffset          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmMsgCycleOffset          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmMsgReducedTime          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmMsgReducedTime          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Specifies if Nm drops irrelevant NM PDUs. false: Only NM PDUs with a Partial Network Information Bit (PNI) = true and containing a Partial Network request for this ECU trigger the standard RX indication handling and thus keep the ECU awake true: Every NM PDU triggers the standard RX indication handling and keeps the ECU awake
        self.allNmMessagesKeepAwake: Optional[Boolean] = None

        # If this attribute is set to true the CareWakeUp filtering is supported.
        self.nmCarWakeUpFilterEnabled: Optional[Boolean] = None

        # If set to true this attribute enables the support of CarWake Up bit evaluation in received NmPdus.
        self.nmCarWakeUpRxEnabled: Optional[Boolean] = None

        # Node specific time offset in the periodic transmission node. It determines the start delay of the transmission. Specified in seconds.
        self.nmMsgCycleOffset: Optional[TimeValue] = None

        # Node specific bus cycle time in the periodic transmission mode with bus load reduction. Specified in seconds.
        self.nmMsgReducedTime: Optional[TimeValue] = None

    def getAllNmMessagesKeepAwake(self) -> Optional[Boolean]:
        """
        Specifies if Nm drops irrelevant NM PDUs. false: Only NM PDUs with a Partial Network Information Bit (PNI) = true and containing a Partial Network request for this ECU trigger the standard RX indication handling and thus keep the ECU awake true: Every NM PDU triggers the standard RX indication handling and keeps the ECU awake
        """
        return self.allNmMessagesKeepAwake

    def setAllNmMessagesKeepAwake(self, value: Optional[Boolean]) -> CanNmNode:
        """
        Specifies if Nm drops irrelevant NM PDUs. false: Only NM PDUs with a Partial Network Information Bit (PNI) = true and containing a Partial Network request for this ECU trigger the standard RX indication handling and thus keep the ECU awake true: Every NM PDU triggers the standard RX indication handling and keeps the ECU awake

        A None value is a no-op and does not overwrite an existing allNmMessagesKeepAwake.
        """
        if value is not None:
            self.allNmMessagesKeepAwake = value
        return self

    def getNmCarWakeUpFilterEnabled(self) -> Optional[Boolean]:
        """
        If this attribute is set to true the CareWakeUp filtering is supported.
        """
        return self.nmCarWakeUpFilterEnabled

    def setNmCarWakeUpFilterEnabled(self, value: Optional[Boolean]) -> CanNmNode:
        """
        If this attribute is set to true the CareWakeUp filtering is supported.
        A None value is a no-op and does not overwrite an existing nmCarWakeUpFilterEnabled.
        """
        if value is not None:
            self.nmCarWakeUpFilterEnabled = value
        return self

    def getNmCarWakeUpRxEnabled(self) -> Optional[Boolean]:
        """
        If set to true this attribute enables the support of CarWake Up bit evaluation in received NmPdus.
        """
        return self.nmCarWakeUpRxEnabled

    def setNmCarWakeUpRxEnabled(self, value: Optional[Boolean]) -> CanNmNode:
        """
        If set to true this attribute enables the support of CarWake Up bit evaluation in received NmPdus.
        A None value is a no-op and does not overwrite an existing nmCarWakeUpRxEnabled.
        """
        if value is not None:
            self.nmCarWakeUpRxEnabled = value
        return self

    def getNmMsgCycleOffset(self) -> Optional[TimeValue]:
        """
        Node specific time offset in the periodic transmission node. It determines the start delay of the transmission. Specified in seconds.
        """
        return self.nmMsgCycleOffset

    def setNmMsgCycleOffset(self, value: Optional[TimeValue]) -> CanNmNode:
        """
        Node specific time offset in the periodic transmission node. It determines the start delay of the transmission. Specified in seconds.
        A None value is a no-op and does not overwrite an existing nmMsgCycleOffset.
        """
        if value is not None:
            self.nmMsgCycleOffset = value
        return self

    def getNmMsgReducedTime(self) -> Optional[TimeValue]:
        """
        Node specific bus cycle time in the periodic transmission mode with bus load reduction. Specified in seconds.
        """
        return self.nmMsgReducedTime

    def setNmMsgReducedTime(self, value: Optional[TimeValue]) -> CanNmNode:
        """
        Node specific bus cycle time in the periodic transmission mode with bus load reduction. Specified in seconds.
        A None value is a no-op and does not overwrite an existing nmMsgReducedTime.
        """
        if value is not None:
            self.nmMsgReducedTime = value
        return self


class FlexrayNmNode(NmNode):
    """
    FlexRay specific NM Node attributes.
    """

    # FlexrayNmNode method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.309, p.679
    # Spec verified: R23-11
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
    J1939NM_AAC = "J-1939-NM--AAC"

    # Command Configurable Address CA. Tags: atp.EnumerationLiteralIndex=3 xml.name=J-1939-NM-CCA
    J1939NM_CCA = "J-1939-NM--CCA"

    # Non-Configurable Address CA. Tags: atp.EnumerationLiteralIndex=0 xml.name=J-1939-NM-NCA
    J1939NM_NCA = "J-1939-NM--NCA"

    # Self-Configurable Address CA. Tags: atp.EnumerationLiteralIndex=2 xml.name=J-1939-NM-SCA
    J1939NM_SCA = "J-1939-NM--SCA"

    # Service Configurable Address CA. Tags: atp.EnumerationLiteralIndex=1 xml.name=J-1939-NM-SVCA
    J1939NM_SVCA = "J-1939-NM--SVCA"

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

    def setArbitraryAddressCapable(self, value: Optional[Boolean]) -> J1939NodeName:
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

    def setEcuInstance(self, value: Optional[Integer]) -> J1939NodeName:
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

    def setFunction(self, value: Optional[Integer]) -> J1939NodeName:
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

    def setFunctionInstance(self, value: Optional[Integer]) -> J1939NodeName:
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

    def setIdentitiyNumber(self, value: Optional[Integer]) -> J1939NodeName:
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

    def setIndustryGroup(self, value: Optional[Integer]) -> J1939NodeName:
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

    def setManufacturerCode(self, value: Optional[Integer]) -> J1939NodeName:
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

    def setVehicleSystem(self, value: Optional[Integer]) -> J1939NodeName:
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

    def setVehicleSystemInstance(self, value: Optional[Integer]) -> J1939NodeName:
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

    def setAddressConfigurationCapability(self, value: Optional[J1939NmAddressConfigurationCapabilityEnum]) -> J1939NmNode:
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

    def setNodeName(self, value: Optional[J1939NodeName]) -> J1939NmNode:
        """
        NodeName configuration.
        A None value is a no-op and does not overwrite an existing nodeName.
        """
        if value is not None:
            self.nodeName = value
        return self


class UdpNmNode(NmNode):
    """
    Udp specific NM Node attributes.

    [constr_5223] Mandatory elements of UdpNmNode: The following attributes shall always be defined for the UdpNmNode: nmMsgCycleOffset.

    [constr_5224] UdpNmNode.nmMsgCycleOffset < UdpNmCluster.nmMsgCycleTime: The value of UdpNmNode.nmMsgCycleOffset shall be smaller than the value of UdpNmCluster.nmMsgCycleTime.
    """

    # UdpNmNode method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.318, p.689
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAllNmMessagesKeepAwake    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAllNmMessagesKeepAwake    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmMsgCycleOffset          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmMsgCycleOffset          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Specifies if Nm drops irrelevant NM PDUs. false: Only NM PDUs with a Partial Network Information Bit (PNI) = true and containing a Partial Network request for this ECU trigger the standard RX indication handling and thus keep the ECU awake true: Every NM PDU triggers the standard RX indication handling and keeps the ECU awake
        self.allNmMessagesKeepAwake: Optional[Boolean] = None

        # Node specific time offset in the periodic transmission node. It determines the start delay of the transmission. Specified in seconds.
        self.nmMsgCycleOffset: Optional[TimeValue] = None

    def getAllNmMessagesKeepAwake(self) -> Optional[Boolean]:
        """
        Specifies if Nm drops irrelevant NM PDUs. false: Only NM PDUs with a Partial Network Information Bit (PNI) = true and containing a Partial Network request for this ECU trigger the standard RX indication handling and thus keep the ECU awake true: Every NM PDU triggers the standard RX indication handling and keeps the ECU awake
        """
        return self.allNmMessagesKeepAwake

    def setAllNmMessagesKeepAwake(self, value: Optional[Boolean]) -> UdpNmNode:
        """
        Specifies if Nm drops irrelevant NM PDUs. false: Only NM PDUs with a Partial Network Information Bit (PNI) = true and containing a Partial Network request for this ECU trigger the standard RX indication handling and thus keep the ECU awake true: Every NM PDU triggers the standard RX indication handling and keeps the ECU awake

        A None value is a no-op and does not overwrite an existing allNmMessagesKeepAwake.
        """
        if value is not None:
            self.allNmMessagesKeepAwake = value
        return self

    def getNmMsgCycleOffset(self) -> Optional[TimeValue]:
        """
        Node specific time offset in the periodic transmission node. It determines the start delay of the transmission. Specified in seconds.
        """
        return self.nmMsgCycleOffset

    def setNmMsgCycleOffset(self, value: Optional[TimeValue]) -> UdpNmNode:
        """
        Node specific time offset in the periodic transmission node. It determines the start delay of the transmission. Specified in seconds.
        A None value is a no-op and does not overwrite an existing nmMsgCycleOffset.
        """
        if value is not None:
            self.nmMsgCycleOffset = value
        return self


class BusspecificNmEcu(ARObject, ABC):
    """
    Busspecific NmEcu attributes.
    """

    # BusspecificNmEcu method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.301, p.675
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

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
    # Spec verified: R23-11
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

    def setNmHwVoteEnabled(self, value: Optional[Boolean]) -> FlexrayNmEcu:
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

    def setNmMainFunctionAcrossFrCycle(self, value: Optional[Boolean]) -> FlexrayNmEcu:
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
    # Spec verified: R23-11
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
    # Spec verified: R23-11
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

    def setNmSynchronizationPointEnabled(self, value: Optional[Boolean]) -> UdpNmEcu:
        """
        Enable/disable the NM Coordination algorithm to being able to initiate the synchronization algorithm.
        A None value is a no-op and does not overwrite an existing nmSynchronizationPointEnabled.
        """
        if value is not None:
            self.nmSynchronizationPointEnabled = value
        return self


class NmCoordinator(ARObject):
    """
    A NM coordinator is an ECU, which is connected to at least two busses, and where the requirement exists that shutdown of NM of at least two of these busses (also referred to as coordinated busses) has to be performed synchronously.
    """

    # NmCoordinator method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.302, p.675
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getIndex                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIndex                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmCoordSyncSupport       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmCoordSyncSupport       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmGlobalCoordinatorTime  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmGlobalCoordinatorTime  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addNmNodeRef                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmNodeRefs                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # Identification of the NMCoordinator.
        self.index: Optional[Integer] = None

        # Switch for enabling NmCoordinatorSync (coordination of nested busses) support.
        self.nmCoordSyncSupport: Optional[Boolean] = None

        # This attribute defines the maximum shutdown time (in seconds) of a connected and coordinated NM-Cluster.
        self.nmGlobalCoordinatorTime: Optional[TimeValue] = None

        # reference to busses (via NmNodes) that are coordinated by the NmCoordinator.
        self.nmNodeRefs: List[RefType] = []

    def getIndex(self) -> Optional[Integer]:
        """
        Identification of the NMCoordinator.
        """
        return self.index

    def setIndex(self, value: Optional[Integer]) -> NmCoordinator:
        """
        Identification of the NMCoordinator.
        A None value is a no-op and does not overwrite an existing index.
        """
        if value is not None:
            self.index = value
        return self

    def getNmCoordSyncSupport(self) -> Optional[Boolean]:
        """
        Switch for enabling NmCoordinatorSync (coordination of nested busses) support.
        """
        return self.nmCoordSyncSupport

    def setNmCoordSyncSupport(self, value: Optional[Boolean]) -> NmCoordinator:
        """
        Switch for enabling NmCoordinatorSync (coordination of nested busses) support.
        A None value is a no-op and does not overwrite an existing nmCoordSyncSupport.
        """
        if value is not None:
            self.nmCoordSyncSupport = value
        return self

    def getNmGlobalCoordinatorTime(self) -> Optional[TimeValue]:
        """
        This attribute defines the maximum shutdown time (in seconds) of a connected and coordinated NM-Cluster.
        """
        return self.nmGlobalCoordinatorTime

    def setNmGlobalCoordinatorTime(self, value: Optional[TimeValue]) -> NmCoordinator:
        """
        This attribute defines the maximum shutdown time (in seconds) of a connected and coordinated NM-Cluster.
        A None value is a no-op and does not overwrite an existing nmGlobalCoordinatorTime.
        """
        if value is not None:
            self.nmGlobalCoordinatorTime = value
        return self

    def addNmNodeRef(self, value: Optional[RefType]) -> NmCoordinator:
        """
        reference to busses (via NmNodes) that are coordinated by the NmCoordinator.
        A None value is a no-op and does not extend the nmNodeRefs list.
        """
        if value is not None:
            self.nmNodeRefs.append(value)
        return self

    def getNmNodeRefs(self) -> List[RefType]:
        """
        reference to busses (via NmNodes) that are coordinated by the NmCoordinator.
        """
        return self.nmNodeRefs


class NmEcu(Identifiable, VariationPointCapable):
    """
    ECU on which NM is running.
    """

    # NmEcu method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.300, p.674
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addBusDependentNmEcu           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getBusDependentNmEcus          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getEcuInstanceRef              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setEcuInstanceRef              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmBusSynchronizationEnabled [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmBusSynchronizationEnabled [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmComControlEnabled         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmComControlEnabled         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmCoordinator               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmCoordinator               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmCycletimeMainFunction     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmCycletimeMainFunction     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmPduRxIndicationEnabled    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmPduRxIndicationEnabled    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmRemoteSleepIndEnabled     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmRemoteSleepIndEnabled     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmStateChangeIndEnabled     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmStateChangeIndEnabled     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmUserDataEnabled           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmUserDataEnabled           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Cluster specific NmEcu attributes
        self.busDependentNmEcus: List[BusspecificNmEcu] = []

        # Association to an ECUInstance in the topology description.
        self.ecuInstanceRef: Optional[RefType] = None

        # Enables bus synchronization support.
        self.nmBusSynchronizationEnabled: Optional[Boolean] = None

        # Enables the Communication Control support.
        self.nmComControlEnabled: Optional[Boolean] = None

        # Nm ECU may coordinate different clusters.
        self.nmCoordinator: Optional[NmCoordinator] = None

        # The period between successive calls to the Main Function of the NM Interface in seconds.
        self.nmCycletimeMainFunction: Optional[TimeValue] = None

        # Switch for enabling the PDU Rx Indication.
        self.nmPduRxIndicationEnabled: Optional[Boolean] = None

        # Switch for enabling remote sleep indication support.
        self.nmRemoteSleepIndEnabled: Optional[Boolean] = None

        # Enables the CAN Network Management state change notification.
        self.nmStateChangeIndEnabled: Optional[Boolean] = None

        # Switch for enabling user data support.
        self.nmUserDataEnabled: Optional[Boolean] = None

    def addBusDependentNmEcu(self, value: Optional[BusspecificNmEcu]) -> NmEcu:
        """
        Cluster specific NmEcu attributes
        A None value is a no-op and does not extend the busDependentNmEcus list.
        """
        if value is not None:
            self.busDependentNmEcus.append(value)
        return self

    def getBusDependentNmEcus(self) -> List[BusspecificNmEcu]:
        """
        Cluster specific NmEcu attributes
        """
        return self.busDependentNmEcus

    def getEcuInstanceRef(self) -> Optional[RefType]:
        """
        Association to an ECUInstance in the topology description.
        """
        return self.ecuInstanceRef

    def setEcuInstanceRef(self, value: Optional[RefType]) -> NmEcu:
        """
        Association to an ECUInstance in the topology description.
        A None value is a no-op and does not overwrite an existing ecuInstanceRef.
        """
        if value is not None:
            self.ecuInstanceRef = value
        return self

    def getNmBusSynchronizationEnabled(self) -> Optional[Boolean]:
        """
        Enables bus synchronization support.
        """
        return self.nmBusSynchronizationEnabled

    def setNmBusSynchronizationEnabled(self, value: Optional[Boolean]) -> NmEcu:
        """
        Enables bus synchronization support.
        A None value is a no-op and does not overwrite an existing nmBusSynchronizationEnabled.
        """
        if value is not None:
            self.nmBusSynchronizationEnabled = value
        return self

    def getNmComControlEnabled(self) -> Optional[Boolean]:
        """
        Enables the Communication Control support.
        """
        return self.nmComControlEnabled

    def setNmComControlEnabled(self, value: Optional[Boolean]) -> NmEcu:
        """
        Enables the Communication Control support.
        A None value is a no-op and does not overwrite an existing nmComControlEnabled.
        """
        if value is not None:
            self.nmComControlEnabled = value
        return self

    def getNmCoordinator(self) -> Optional[NmCoordinator]:
        """
        Nm ECU may coordinate different clusters.
        """
        return self.nmCoordinator

    def setNmCoordinator(self, value: Optional[NmCoordinator]) -> NmEcu:
        """
        Nm ECU may coordinate different clusters.
        A None value is a no-op and does not overwrite an existing nmCoordinator.
        """
        if value is not None:
            self.nmCoordinator = value
        return self

    def getNmCycletimeMainFunction(self) -> Optional[TimeValue]:
        """
        The period between successive calls to the Main Function of the NM Interface in seconds.
        """
        return self.nmCycletimeMainFunction

    def setNmCycletimeMainFunction(self, value: Optional[TimeValue]) -> NmEcu:
        """
        The period between successive calls to the Main Function of the NM Interface in seconds.
        A None value is a no-op and does not overwrite an existing nmCycletimeMainFunction.
        """
        if value is not None:
            self.nmCycletimeMainFunction = value
        return self

    def getNmPduRxIndicationEnabled(self) -> Optional[Boolean]:
        """
        Switch for enabling the PDU Rx Indication.
        """
        return self.nmPduRxIndicationEnabled

    def setNmPduRxIndicationEnabled(self, value: Optional[Boolean]) -> NmEcu:
        """
        Switch for enabling the PDU Rx Indication.
        A None value is a no-op and does not overwrite an existing nmPduRxIndicationEnabled.
        """
        if value is not None:
            self.nmPduRxIndicationEnabled = value
        return self

    def getNmRemoteSleepIndEnabled(self) -> Optional[Boolean]:
        """
        Switch for enabling remote sleep indication support.
        """
        return self.nmRemoteSleepIndEnabled

    def setNmRemoteSleepIndEnabled(self, value: Optional[Boolean]) -> NmEcu:
        """
        Switch for enabling remote sleep indication support.
        A None value is a no-op and does not overwrite an existing nmRemoteSleepIndEnabled.
        """
        if value is not None:
            self.nmRemoteSleepIndEnabled = value
        return self

    def getNmStateChangeIndEnabled(self) -> Optional[Boolean]:
        """
        Enables the CAN Network Management state change notification.
        """
        return self.nmStateChangeIndEnabled

    def setNmStateChangeIndEnabled(self, value: Optional[Boolean]) -> NmEcu:
        """
        Enables the CAN Network Management state change notification.
        A None value is a no-op and does not overwrite an existing nmStateChangeIndEnabled.
        """
        if value is not None:
            self.nmStateChangeIndEnabled = value
        return self

    def getNmUserDataEnabled(self) -> Optional[Boolean]:
        """
        Switch for enabling user data support.
        """
        return self.nmUserDataEnabled

    def setNmUserDataEnabled(self, value: Optional[Boolean]) -> NmEcu:
        """
        Switch for enabling user data support.
        A None value is a no-op and does not overwrite an existing nmUserDataEnabled.
        """
        if value is not None:
            self.nmUserDataEnabled = value
        return self


class NmConfig(FibexElement):
    """
    Contains the all configuration elements for AUTOSAR Nm. Tags: atp.recommendedPackage=NmConfigs
    """

    # NmConfig method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.298, p.672
    # Spec verified: R23-11
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

    def getNmClusters(self) -> List[NmCluster]:
        """
        Collection of NM Clusters atpVariation: Derived, because cluster can be variable. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=nmCluster.shortName, nmCluster.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        return self.nmClusters

    def createCanNmCluster(self, short_name: str) -> CanNmCluster:
        if not self.IsReferrableElementExists(short_name, CanNmCluster):
            cluster = CanNmCluster(self, short_name)
            self.addReferrableElement(cluster)
            self.nmClusters.append(cluster)
        return cast(CanNmCluster, self.getReferrableElement(short_name, CanNmCluster))

    def createUdpNmCluster(self, short_name: str) -> UdpNmCluster:
        if not self.IsReferrableElementExists(short_name, UdpNmCluster):
            cluster = UdpNmCluster(self, short_name)
            self.addReferrableElement(cluster)
            self.nmClusters.append(cluster)
        return cast(UdpNmCluster, self.getReferrableElement(short_name, UdpNmCluster))

    def createFlexrayNmCluster(self, short_name: str) -> FlexrayNmCluster:
        if not self.IsReferrableElementExists(short_name, FlexrayNmCluster):
            cluster = FlexrayNmCluster(self, short_name)
            self.addReferrableElement(cluster)
            self.nmClusters.append(cluster)
        return cast(FlexrayNmCluster, self.getReferrableElement(short_name, FlexrayNmCluster))

    def createJ1939NmCluster(self, short_name: str) -> J1939NmCluster:
        if not self.IsReferrableElementExists(short_name, J1939NmCluster):
            cluster = J1939NmCluster(self, short_name)
            self.addReferrableElement(cluster)
            self.nmClusters.append(cluster)
        return cast(J1939NmCluster, self.getReferrableElement(short_name, J1939NmCluster))

    def getCanNmClusters(self) -> List[CanNmCluster]:
        return [cluster for cluster in self.nmClusters if isinstance(cluster, CanNmCluster)]

    def getUdpNmClusters(self) -> List[UdpNmCluster]:
        return [cluster for cluster in self.nmClusters if isinstance(cluster, UdpNmCluster)]

    def getNmClusterCouplings(self) -> List[NmClusterCoupling]:
        """
        Collection of NmClusterCouplings atpVariation: Derived, because NmCluster can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=nmClusterCoupling, nmClusterCoupling.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        return self.nmClusterCouplings

    def addNmClusterCouplings(self, value: Optional[NmClusterCoupling]) -> NmConfig:
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
        if not self.IsReferrableElementExists(short_name, NmEcu):
            cluster = NmEcu(self, short_name)
            self.addReferrableElement(cluster)
            self.nmIfEcus.append(cluster)
        return cast(NmEcu, self.getReferrableElement(short_name, NmEcu))


class NmCluster(Identifiable, VariationPointCapable, ABC):
    """
    Set of NM nodes coordinated with use of the NM algorithm.
    """

    # NmCluster method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.299, p.673
    # Spec verified: R23-11
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

    def setCommunicationClusterRef(self, value: Optional[RefType]) -> NmCluster:
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

    def setNmChannelSleepMaster(self, value: Optional[Boolean]) -> NmCluster:
        """
        This parameter shall be set to indicate if the sleep of this network can be absolutely decided by the local node only and that no other nodes can oppose that decision.
        A None value is a no-op and does not overwrite an existing nmChannelSleepMaster.
        """
        if value is not None:
            self.nmChannelSleepMaster = value
        return self

    def createCanNmNode(self, short_name: str) -> CanNmNode:
        if not self.IsReferrableElementExists(short_name, CanNmNode):
            node = CanNmNode(self, short_name)
            self.addReferrableElement(node)
            self.nmNodes.append(node)
        return cast(CanNmNode, self.getReferrableElement(short_name, CanNmNode))

    def createUdpNmNode(self, short_name: str) -> UdpNmNode:
        if not self.IsReferrableElementExists(short_name, UdpNmNode):
            node = UdpNmNode(self, short_name)
            self.addReferrableElement(node)
            self.nmNodes.append(node)
        return cast(UdpNmNode, self.getReferrableElement(short_name, UdpNmNode))

    def createFlexrayNmNode(self, short_name: str) -> FlexrayNmNode:
        if not self.IsReferrableElementExists(short_name, FlexrayNmNode):
            node = FlexrayNmNode(self, short_name)
            self.addReferrableElement(node)
            self.nmNodes.append(node)
        return cast(FlexrayNmNode, self.getReferrableElement(short_name, FlexrayNmNode))

    def createJ1939NmNode(self, short_name: str) -> J1939NmNode:
        if not self.IsReferrableElementExists(short_name, J1939NmNode):
            node = J1939NmNode(self, short_name)
            self.addReferrableElement(node)
            self.nmNodes.append(node)
        return cast(J1939NmNode, self.getReferrableElement(short_name, J1939NmNode))

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

    def setNmNodeDetectionEnabled(self, value: Optional[Boolean]) -> NmCluster:
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

    def setNmNodeIdEnabled(self, value: Optional[Boolean]) -> NmCluster:
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

    def setNmPncParticipation(self, value: Optional[Boolean]) -> NmCluster:
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

    def setNmRepeatMsgIndEnabled(self, value: Optional[Boolean]) -> NmCluster:
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

    def setNmSynchronizingNetwork(self, value: Optional[Boolean]) -> NmCluster:
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

    def setPncClusterVectorLength(self, value: Optional[PositiveInteger]) -> NmCluster:
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

    def setNmChannelId(self, value: Optional[Integer]) -> NmCluster:
        """
        This attribute has the status "removed" and shall not be used any longer. Old description: Channel identification number of the corresponding channel. Must be unique over all NmClusters.
        A None value is a no-op and does not overwrite an existing nmChannelId.
        """
        if value is not None:
            self.nmChannelId = value
        return self


class CanNmCluster(NmCluster):
    """
    Can specific NmCluster attributes

    [constr_3069] Allowed CanNmCluster.nmNidPosition values: If defined, the value of CanNmCluster.nmNidPosition shall only be set to either 0 or 1.

    [constr_3070] Allowed CanNmCluster.nmCbvPosition values: If defined, the value of CanNmCluster.nmCbvPosition shall only be set to either 0 or 1.

    [constr_3071] CanNmCluster.nmCbvPosition and CanNmCluster.nmNidPosition shall never have the same value: CanNmCluster.nmCbvPosition and CanNmCluster.nmNidPosition shall never have the same value.

    [constr_9157] Existence of nmBusloadReductionActive: For each CanNmCluster, the attribute nmBusloadReductionActive shall exist at the time when the System Description is complete.

    [constr_9158] Existence of nmImmediateNmTransmissions: For each CanNmCluster, the attribute nmImmediateNmTransmissions shall exist at the time when the System Description is complete.

    [constr_9159] Existence of nmMessageTimeoutTime: For each CanNmCluster, the attribute nmMessageTimeoutTime shall exist at the time when the System Description is complete.

    [constr_9160] Existence of nmMsgCycleTime: For each CanNmCluster the attribute nmMsgCycleTime shall exist at the time when the System Description is complete.

    [constr_9161] Existence of nmNetworkTimeout: For each CanNmCluster, the attribute nmNetworkTimeout shall exist at the time when the System Description is complete.

    [constr_9162] Existence of nmRemoteSleepIndicationTime: For each CanNmCluster, the attribute nmRemoteSleepIndicationTime shall exist at the time when the System Description is complete.

    [constr_9163] Existence of nmRepeatMessageTime: For each CanNmCluster, the attribute nmRepeatMessageTime shall exist at the time when the System Description is complete.

    [constr_9164] Existence of nmWaitBusSleepTime: For each CanNmCluster, the attribute nmWaitBusSleepTime shall exist at the time when the System Description is complete.
    """

    # CanNmCluster method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.311, p.682
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getNmBusloadReductionActive     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmBusloadReductionActive     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmCarWakeUpBitPosition       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmCarWakeUpBitPosition       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmCarWakeUpFilterNodeId      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmCarWakeUpFilterNodeId      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmCbvPosition                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmCbvPosition                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmImmediateNmCycleTime       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmImmediateNmCycleTime       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmImmediateNmTransmissions   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmImmediateNmTransmissions   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmMessageTimeoutTime         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmMessageTimeoutTime         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmMsgCycleTime               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmMsgCycleTime               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmNetworkTimeout             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmNetworkTimeout             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmNidPosition                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmNidPosition                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmRemoteSleepIndicationTime  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmRemoteSleepIndicationTime  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmRepeatMessageTime          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmRepeatMessageTime          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmWaitBusSleepTime           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmWaitBusSleepTime           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # It determines if bus load reduction for the respective Can Nm channel is active or not.
        self.nmBusloadReductionActive: Optional[Boolean] = None

        # Specifies the bit position of the CarWakeUp within the Nm Pdu.
        self.nmCarWakeUpBitPosition: Optional[PositiveInteger] = None

        # Source node identifier for CarWakeUp filtering.
        self.nmCarWakeUpFilterNodeId: Optional[PositiveInteger] = None

        # Defines the position of the control bit vector within the Nm Pdu (Byte position). If this attribute is not configured, the Control Bit Vector is not used.
        self.nmCbvPosition: Optional[Integer] = None

        # Defines the immediate NmPdu cycle time in seconds which is used for nmImmediateNmTransmissions NmPdu transmissions. This parameter is only valid if CanNm ImmediateNmTransmissions is greater one.
        self.nmImmediateNmCycleTime: Optional[TimeValue] = None

        # Defines the number of immediate NmPdus which shall be transmitted. If the value is zero no immediate NmPdus are transmitted. The cycle time of immediate NmPdus is defined by nmImmediateNmCycleTime.
        self.nmImmediateNmTransmissions: Optional[PositiveInteger] = None

        # Timeout of an NmPdu in seconds. It determines how long the NM shall wait with notification of transmission failure while communication errors occur on the bus.
        self.nmMessageTimeoutTime: Optional[TimeValue] = None

        # Period of a NmPdu in seconds. It determines the periodic rate in the periodic transmission mode with bus load reduction and is the basis for transmit scheduling in the periodic transmission mode without bus load reduction.
        self.nmMsgCycleTime: Optional[TimeValue] = None

        # Network Timeout for NmPdus in seconds It denotes the time how long the CanNm shall stay in the Network Mode before transition into Prepare Bus-Sleep Mode shall take place.
        self.nmNetworkTimeout: Optional[TimeValue] = None

        # Defines the byte position of the source node identifier within the NmPdu. If this attribute is not configured, the Node Identification is not used.
        self.nmNidPosition: Optional[Integer] = None

        # Timeout for Remote Sleep Indication in seconds. It defines the time how long it shall take to recognize that all other nodes are ready to sleep.
        self.nmRemoteSleepIndicationTime: Optional[TimeValue] = None

        # Timeout for Repeat Message State in seconds. Defines the time how long the NM shall stay in the Repeat Message State.
        self.nmRepeatMessageTime: Optional[TimeValue] = None

        # Timeout for bus calm down phase in seconds. It denotes the time how long the CanNm shall stay in the Prepare Bus-Sleep Mode before transition into Bus-Sleep Mode shall take place.
        self.nmWaitBusSleepTime: Optional[TimeValue] = None

    def getNmBusloadReductionActive(self) -> Optional[Boolean]:
        """
        It determines if bus load reduction for the respective Can Nm channel is active or not.
        """
        return self.nmBusloadReductionActive

    def setNmBusloadReductionActive(self, value: Optional[Boolean]) -> CanNmCluster:
        """
        It determines if bus load reduction for the respective Can Nm channel is active or not.
        A None value is a no-op and does not overwrite an existing nmBusloadReductionActive.
        """
        if value is not None:
            self.nmBusloadReductionActive = value
        return self

    def getNmCarWakeUpBitPosition(self) -> Optional[PositiveInteger]:
        """
        Specifies the bit position of the CarWakeUp within the Nm Pdu.
        """
        return self.nmCarWakeUpBitPosition

    def setNmCarWakeUpBitPosition(self, value: Optional[PositiveInteger]) -> CanNmCluster:
        """
        Specifies the bit position of the CarWakeUp within the Nm Pdu.
        A None value is a no-op and does not overwrite an existing nmCarWakeUpBitPosition.
        """
        if value is not None:
            self.nmCarWakeUpBitPosition = value
        return self

    def getNmCarWakeUpFilterNodeId(self) -> Optional[PositiveInteger]:
        """
        Source node identifier for CarWakeUp filtering.
        """
        return self.nmCarWakeUpFilterNodeId

    def setNmCarWakeUpFilterNodeId(self, value: Optional[PositiveInteger]) -> CanNmCluster:
        """
        Source node identifier for CarWakeUp filtering.
        A None value is a no-op and does not overwrite an existing nmCarWakeUpFilterNodeId.
        """
        if value is not None:
            self.nmCarWakeUpFilterNodeId = value
        return self

    def getNmCbvPosition(self) -> Optional[Integer]:
        """
        Defines the position of the control bit vector within the Nm Pdu (Byte position). If this attribute is not configured, the Control Bit Vector is not used.
        """
        return self.nmCbvPosition

    def setNmCbvPosition(self, value: Optional[Integer]) -> CanNmCluster:
        """
        Defines the position of the control bit vector within the Nm Pdu (Byte position). If this attribute is not configured, the Control Bit Vector is not used.
        A None value is a no-op and does not overwrite an existing nmCbvPosition.
        """
        if value is not None:
            self.nmCbvPosition = value
        return self

    def getNmImmediateNmCycleTime(self) -> Optional[TimeValue]:
        """
        Defines the immediate NmPdu cycle time in seconds which is used for nmImmediateNmTransmissions NmPdu transmissions. This parameter is only valid if CanNm ImmediateNmTransmissions is greater one.
        """
        return self.nmImmediateNmCycleTime

    def setNmImmediateNmCycleTime(self, value: Optional[TimeValue]) -> CanNmCluster:
        """
        Defines the immediate NmPdu cycle time in seconds which is used for nmImmediateNmTransmissions NmPdu transmissions. This parameter is only valid if CanNm ImmediateNmTransmissions is greater one.
        A None value is a no-op and does not overwrite an existing nmImmediateNmCycleTime.
        """
        if value is not None:
            self.nmImmediateNmCycleTime = value
        return self

    def getNmImmediateNmTransmissions(self) -> Optional[PositiveInteger]:
        """
        Defines the number of immediate NmPdus which shall be transmitted. If the value is zero no immediate NmPdus are transmitted. The cycle time of immediate NmPdus is defined by nmImmediateNmCycleTime.
        """
        return self.nmImmediateNmTransmissions

    def setNmImmediateNmTransmissions(self, value: Optional[PositiveInteger]) -> CanNmCluster:
        """
        Defines the number of immediate NmPdus which shall be transmitted. If the value is zero no immediate NmPdus are transmitted. The cycle time of immediate NmPdus is defined by nmImmediateNmCycleTime.
        A None value is a no-op and does not overwrite an existing nmImmediateNmTransmissions.
        """
        if value is not None:
            self.nmImmediateNmTransmissions = value
        return self

    def getNmMessageTimeoutTime(self) -> Optional[TimeValue]:
        """
        Timeout of an NmPdu in seconds. It determines how long the NM shall wait with notification of transmission failure while communication errors occur on the bus.
        """
        return self.nmMessageTimeoutTime

    def setNmMessageTimeoutTime(self, value: Optional[TimeValue]) -> CanNmCluster:
        """
        Timeout of an NmPdu in seconds. It determines how long the NM shall wait with notification of transmission failure while communication errors occur on the bus.
        A None value is a no-op and does not overwrite an existing nmMessageTimeoutTime.
        """
        if value is not None:
            self.nmMessageTimeoutTime = value
        return self

    def getNmMsgCycleTime(self) -> Optional[TimeValue]:
        """
        Period of a NmPdu in seconds. It determines the periodic rate in the periodic transmission mode with bus load reduction and is the basis for transmit scheduling in the periodic transmission mode without bus load reduction.
        """
        return self.nmMsgCycleTime

    def setNmMsgCycleTime(self, value: Optional[TimeValue]) -> CanNmCluster:
        """
        Period of a NmPdu in seconds. It determines the periodic rate in the periodic transmission mode with bus load reduction and is the basis for transmit scheduling in the periodic transmission mode without bus load reduction.
        A None value is a no-op and does not overwrite an existing nmMsgCycleTime.
        """
        if value is not None:
            self.nmMsgCycleTime = value
        return self

    def getNmNetworkTimeout(self) -> Optional[TimeValue]:
        """
        Network Timeout for NmPdus in seconds It denotes the time how long the CanNm shall stay in the Network Mode before transition into Prepare Bus-Sleep Mode shall take place.
        """
        return self.nmNetworkTimeout

    def setNmNetworkTimeout(self, value: Optional[TimeValue]) -> CanNmCluster:
        """
        Network Timeout for NmPdus in seconds It denotes the time how long the CanNm shall stay in the Network Mode before transition into Prepare Bus-Sleep Mode shall take place.
        A None value is a no-op and does not overwrite an existing nmNetworkTimeout.
        """
        if value is not None:
            self.nmNetworkTimeout = value
        return self

    def getNmNidPosition(self) -> Optional[Integer]:
        """
        Defines the byte position of the source node identifier within the NmPdu. If this attribute is not configured, the Node Identification is not used.
        """
        return self.nmNidPosition

    def setNmNidPosition(self, value: Optional[Integer]) -> CanNmCluster:
        """
        Defines the byte position of the source node identifier within the NmPdu. If this attribute is not configured, the Node Identification is not used.
        A None value is a no-op and does not overwrite an existing nmNidPosition.
        """
        if value is not None:
            self.nmNidPosition = value
        return self

    def getNmRemoteSleepIndicationTime(self) -> Optional[TimeValue]:
        """
        Timeout for Remote Sleep Indication in seconds. It defines the time how long it shall take to recognize that all other nodes are ready to sleep.
        """
        return self.nmRemoteSleepIndicationTime

    def setNmRemoteSleepIndicationTime(self, value: Optional[TimeValue]) -> CanNmCluster:
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

    def setNmRepeatMessageTime(self, value: Optional[TimeValue]) -> CanNmCluster:
        """
        Timeout for Repeat Message State in seconds. Defines the time how long the NM shall stay in the Repeat Message State.
        A None value is a no-op and does not overwrite an existing nmRepeatMessageTime.
        """
        if value is not None:
            self.nmRepeatMessageTime = value
        return self

    def getNmWaitBusSleepTime(self) -> Optional[TimeValue]:
        """
        Timeout for bus calm down phase in seconds. It denotes the time how long the CanNm shall stay in the Prepare Bus-Sleep Mode before transition into Bus-Sleep Mode shall take place.
        """
        return self.nmWaitBusSleepTime

    def setNmWaitBusSleepTime(self, value: Optional[TimeValue]) -> CanNmCluster:
        """
        Timeout for bus calm down phase in seconds. It denotes the time how long the CanNm shall stay in the Prepare Bus-Sleep Mode before transition into Bus-Sleep Mode shall take place.
        A None value is a no-op and does not overwrite an existing nmWaitBusSleepTime.
        """
        if value is not None:
            self.nmWaitBusSleepTime = value
        return self


class FlexrayNmCluster(NmCluster):
    """
    FlexRay specific NM cluster attributes.
    """

    # FlexrayNmCluster method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.306, p.678
    # Spec verified: R23-11
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

    def setNmCarWakeUpBitPosition(self, value: Optional[PositiveInteger]) -> FlexrayNmCluster:
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

    def setNmCarWakeUpFilterEnabled(self, value: Optional[Boolean]) -> FlexrayNmCluster:
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

    def setNmCarWakeUpFilterNodeId(self, value: Optional[PositiveInteger]) -> FlexrayNmCluster:
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

    def setNmCarWakeUpRxEnabled(self, value: Optional[Boolean]) -> FlexrayNmCluster:
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

    def setNmDataCycle(self, value: Optional[Integer]) -> FlexrayNmCluster:
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

    def setNmMainFunctionPeriod(self, value: Optional[TimeValue]) -> FlexrayNmCluster:
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

    def setNmRemoteSleepIndicationTime(self, value: Optional[TimeValue]) -> FlexrayNmCluster:
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

    def setNmRepeatMessageTime(self, value: Optional[TimeValue]) -> FlexrayNmCluster:
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

    def setNmRepetitionCycle(self, value: Optional[Integer]) -> FlexrayNmCluster:
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

    def setNmVotingCycle(self, value: Optional[Integer]) -> FlexrayNmCluster:
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
    # Spec verified: R23-11
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

    def setAddressClaimEnabled(self, value: Optional[Boolean]) -> J1939NmCluster:
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

    def setUsesDynamicAddressing(self, value: Optional[Boolean]) -> J1939NmCluster:
        """
        Defines whether fully dynamic address resolution according to SAE J1939-81 shall be supported on this J1939NmCluster. • True: The dynamically allocated addresses on the bus are matched at runtime to the configured addresses. • False: The addresses on the bus resemble the configured addresses.
        A None value is a no-op and does not overwrite an existing usesDynamicAddressing.
        """
        if value is not None:
            self.usesDynamicAddressing = value
        return self


class UdpNmClusterCoupling(NmClusterCoupling):
    """
    Udp attributes that are valid for each of the referenced (coupled) UdpNm clusters.
    """

    # UdpNmClusterCoupling method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.317, p.688
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addCoupledClusterRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCoupledClusterRefs          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getNmImmediateRestartEnabled   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmImmediateRestartEnabled   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Reference to coupled UdpNm Clusters.
        self.coupledClusterRefs: List[RefType] = []

        # Enables the asynchronous transmission of a CanNm PDU upon bus-communication request in Prepare-Bus-Sleep mode.
        self.nmImmediateRestartEnabled: Optional[Boolean] = None

    def addCoupledClusterRef(self, ref: RefType) -> UdpNmClusterCoupling:
        """
        Reference to coupled UdpNm Clusters.
        """
        self.coupledClusterRefs.append(ref)
        return self

    def getCoupledClusterRefs(self) -> List[RefType]:
        """
        Reference to coupled UdpNm Clusters.
        """
        return self.coupledClusterRefs

    def getNmImmediateRestartEnabled(self) -> Optional[Boolean]:
        """
        Enables the asynchronous transmission of a CanNm PDU upon bus-communication request in Prepare-Bus-Sleep mode.
        """
        return self.nmImmediateRestartEnabled

    def setNmImmediateRestartEnabled(self, value: Optional[Boolean]) -> UdpNmClusterCoupling:
        """
        Enables the asynchronous transmission of a CanNm PDU upon bus-communication request in Prepare-Bus-Sleep mode.
        A None value is a no-op and does not overwrite an existing nmImmediateRestartEnabled.
        """
        if value is not None:
            self.nmImmediateRestartEnabled = value
        return self


class UdpNmCluster(NmCluster):
    """
    Udp specific NmCluster attributes

    [constr_3078] Allowed UdpNmCluster.nmNidPosition values: If defined, the value of UdpNmCluster.nmNidPosition shall only be set to either 0 or 1.

    [constr_3079] Allowed UdpNmCluster.nmCbvPosition values: If defined, the value of UdpNmCluster.nmCbvPosition shall only be set to either 0 or 1.

    [constr_3080] UdpNmCluster.nmCbvPosition and UdpNmCluster.nmNidPosition shall never have the same value: UdpNmCluster.nmCbvPosition and UdpNmCluster.nmNidPosition shall never have the same value.

    [constr_5222] Mandatory elements of UdpNmCluster: The following attributes shall always be defined for the UdpNmCluster: nmMsgCycleTime, nmMessageTimeoutTime, nmNetworkTimeout, nmRemoteSleepIndicationTime, nmRepeatMessageTime, nmWaitBusSleepTime, communicationCluster.
    """

    # UdpNmCluster method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.315, p.687
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getNmCbvPosition                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmCbvPosition                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmImmediateNmCycleTime       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmImmediateNmCycleTime       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmImmediateNmTransmissions   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmImmediateNmTransmissions   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmMessageTimeoutTime         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmMessageTimeoutTime         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmMsgCycleTime               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmMsgCycleTime               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmNetworkTimeout             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmNetworkTimeout             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmNidPosition                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmNidPosition                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmRemoteSleepIndicationTime  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmRemoteSleepIndicationTime  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmRepeatMessageTime          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmRepeatMessageTime          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmWaitBusSleepTime           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNmWaitBusSleepTime           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getVlanRef                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setVlanRef                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Defines the position of the control bit vector within the Nm Pdu (Byte position). If this attribute is not configured, the Control Bit Vector is not used.
        self.nmCbvPosition: Optional[Integer] = None

        # Defines the immediate NmPdu cycle time in seconds which is used for nmImmediateNmTransmissions NmPdu transmissions. This attribute is only valid if nmImmediate NmTransmissions is greater one.
        self.nmImmediateNmCycleTime: Optional[TimeValue] = None

        # Defines the number of immediate NmPdus which shall be transmitted. If the value is zero no immediate NmPdus are transmitted. The cycle time of immediate NmPdus is defined by nmImmediateNmCycleTime.
        self.nmImmediateNmTransmissions: Optional[PositiveInteger] = None

        # Timeout of a NmPdu in seconds. It determines how long the NM shall wait with notification of transmission failure while communication errors occur on the bus.
        self.nmMessageTimeoutTime: Optional[TimeValue] = None

        # Period of a NmPdu in seconds. It determines the periodic rate in the periodic transmission mode with bus load reduction and is the basis for transmit scheduling in the periodic transmission mode without bus load reduction.
        self.nmMsgCycleTime: Optional[TimeValue] = None

        # Network Timeout for NmPdus in seconds. It denotes the time how long the UdpNm shall stay in the Network Mode before transition into Prepare Bus-Sleep Mode shall take place.
        self.nmNetworkTimeout: Optional[TimeValue] = None

        # Defines the byte position of the source node identifier within the NmPdu. If this attribute is not configured, the Node Identification is not used.
        self.nmNidPosition: Optional[Integer] = None

        # Timeout for Remote Sleep Indication in seconds. It defines the time how long it shall take to recognize that all other nodes are ready to sleep.
        self.nmRemoteSleepIndicationTime: Optional[TimeValue] = None

        # Timeout for Repeat Message State in seconds. Defines the time how long the NM shall stay in the Repeat Message State.
        self.nmRepeatMessageTime: Optional[TimeValue] = None

        # Timeout for bus calm down phase in seconds. It denotes the time how long the CanNm shall stay in the Prepare Bus-Sleep Mode before transition into Bus-Sleep Mode shall take place.
        self.nmWaitBusSleepTime: Optional[TimeValue] = None

        # Reference to the vlan (represented by the Ethernet PhysicalChannel) this UdpNmCluster shall apply to.
        self.vlanRef: Optional[RefType] = None

    def getNmCbvPosition(self) -> Optional[Integer]:
        """
        Defines the position of the control bit vector within the Nm Pdu (Byte position). If this attribute is not configured, the Control Bit Vector is not used.
        """
        return self.nmCbvPosition

    def setNmCbvPosition(self, value: Optional[Integer]) -> UdpNmCluster:
        """
        Defines the position of the control bit vector within the Nm Pdu (Byte position). If this attribute is not configured, the Control Bit Vector is not used.
        A None value is a no-op and does not overwrite an existing nmCbvPosition.
        """
        if value is not None:
            self.nmCbvPosition = value
        return self

    def getNmImmediateNmCycleTime(self) -> Optional[TimeValue]:
        """
        Defines the immediate NmPdu cycle time in seconds which is used for nmImmediateNmTransmissions NmPdu transmissions. This attribute is only valid if nmImmediate NmTransmissions is greater one.
        """
        return self.nmImmediateNmCycleTime

    def setNmImmediateNmCycleTime(self, value: Optional[TimeValue]) -> UdpNmCluster:
        """
        Defines the immediate NmPdu cycle time in seconds which is used for nmImmediateNmTransmissions NmPdu transmissions. This attribute is only valid if nmImmediate NmTransmissions is greater one.
        A None value is a no-op and does not overwrite an existing nmImmediateNmCycleTime.
        """
        if value is not None:
            self.nmImmediateNmCycleTime = value
        return self

    def getNmImmediateNmTransmissions(self) -> Optional[PositiveInteger]:
        """
        Defines the number of immediate NmPdus which shall be transmitted. If the value is zero no immediate NmPdus are transmitted. The cycle time of immediate NmPdus is defined by nmImmediateNmCycleTime.
        """
        return self.nmImmediateNmTransmissions

    def setNmImmediateNmTransmissions(self, value: Optional[PositiveInteger]) -> UdpNmCluster:
        """
        Defines the number of immediate NmPdus which shall be transmitted. If the value is zero no immediate NmPdus are transmitted. The cycle time of immediate NmPdus is defined by nmImmediateNmCycleTime.
        A None value is a no-op and does not overwrite an existing nmImmediateNmTransmissions.
        """
        if value is not None:
            self.nmImmediateNmTransmissions = value
        return self

    def getNmMessageTimeoutTime(self) -> Optional[TimeValue]:
        """
        Timeout of a NmPdu in seconds. It determines how long the NM shall wait with notification of transmission failure while communication errors occur on the bus.
        """
        return self.nmMessageTimeoutTime

    def setNmMessageTimeoutTime(self, value: Optional[TimeValue]) -> UdpNmCluster:
        """
        Timeout of a NmPdu in seconds. It determines how long the NM shall wait with notification of transmission failure while communication errors occur on the bus.
        A None value is a no-op and does not overwrite an existing nmMessageTimeoutTime.
        """
        if value is not None:
            self.nmMessageTimeoutTime = value
        return self

    def getNmMsgCycleTime(self) -> Optional[TimeValue]:
        """
        Period of a NmPdu in seconds. It determines the periodic rate in the periodic transmission mode with bus load reduction and is the basis for transmit scheduling in the periodic transmission mode without bus load reduction.
        """
        return self.nmMsgCycleTime

    def setNmMsgCycleTime(self, value: Optional[TimeValue]) -> UdpNmCluster:
        """
        Period of a NmPdu in seconds. It determines the periodic rate in the periodic transmission mode with bus load reduction and is the basis for transmit scheduling in the periodic transmission mode without bus load reduction.
        A None value is a no-op and does not overwrite an existing nmMsgCycleTime.
        """
        if value is not None:
            self.nmMsgCycleTime = value
        return self

    def getNmNetworkTimeout(self) -> Optional[TimeValue]:
        """
        Network Timeout for NmPdus in seconds. It denotes the time how long the UdpNm shall stay in the Network Mode before transition into Prepare Bus-Sleep Mode shall take place.
        """
        return self.nmNetworkTimeout

    def setNmNetworkTimeout(self, value: Optional[TimeValue]) -> UdpNmCluster:
        """
        Network Timeout for NmPdus in seconds. It denotes the time how long the UdpNm shall stay in the Network Mode before transition into Prepare Bus-Sleep Mode shall take place.
        A None value is a no-op and does not overwrite an existing nmNetworkTimeout.
        """
        if value is not None:
            self.nmNetworkTimeout = value
        return self

    def getNmNidPosition(self) -> Optional[Integer]:
        """
        Defines the byte position of the source node identifier within the NmPdu. If this attribute is not configured, the Node Identification is not used.
        """
        return self.nmNidPosition

    def setNmNidPosition(self, value: Optional[Integer]) -> UdpNmCluster:
        """
        Defines the byte position of the source node identifier within the NmPdu. If this attribute is not configured, the Node Identification is not used.
        A None value is a no-op and does not overwrite an existing nmNidPosition.
        """
        if value is not None:
            self.nmNidPosition = value
        return self

    def getNmRemoteSleepIndicationTime(self) -> Optional[TimeValue]:
        """
        Timeout for Remote Sleep Indication in seconds. It defines the time how long it shall take to recognize that all other nodes are ready to sleep.
        """
        return self.nmRemoteSleepIndicationTime

    def setNmRemoteSleepIndicationTime(self, value: Optional[TimeValue]) -> UdpNmCluster:
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

    def setNmRepeatMessageTime(self, value: Optional[TimeValue]) -> UdpNmCluster:
        """
        Timeout for Repeat Message State in seconds. Defines the time how long the NM shall stay in the Repeat Message State.
        A None value is a no-op and does not overwrite an existing nmRepeatMessageTime.
        """
        if value is not None:
            self.nmRepeatMessageTime = value
        return self

    def getNmWaitBusSleepTime(self) -> Optional[TimeValue]:
        """
        Timeout for bus calm down phase in seconds. It denotes the time how long the CanNm shall stay in the Prepare Bus-Sleep Mode before transition into Bus-Sleep Mode shall take place.
        """
        return self.nmWaitBusSleepTime

    def setNmWaitBusSleepTime(self, value: Optional[TimeValue]) -> UdpNmCluster:
        """
        Timeout for bus calm down phase in seconds. It denotes the time how long the CanNm shall stay in the Prepare Bus-Sleep Mode before transition into Bus-Sleep Mode shall take place.
        A None value is a no-op and does not overwrite an existing nmWaitBusSleepTime.
        """
        if value is not None:
            self.nmWaitBusSleepTime = value
        return self

    def getVlanRef(self) -> Optional[RefType]:
        """
        Reference to the vlan (represented by the Ethernet PhysicalChannel) this UdpNmCluster shall apply to.
        """
        return self.vlanRef

    def setVlanRef(self, value: Optional[RefType]) -> UdpNmCluster:
        """
        Reference to the vlan (represented by the Ethernet PhysicalChannel) this UdpNmCluster shall apply to.
        A None value is a no-op and does not overwrite an existing vlanRef.
        """
        if value is not None:
            self.vlanRef = value
        return self
