"""
This module contains classes for representing AUTOSAR service mapping elements
in software component internal behavior templates.
"""

from __future__ import annotations
from typing import List, Optional, cast
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    ComMgrUserNeeds,
    CryptoKeyManagementNeeds,
    CryptoServiceJobNeeds,
    CryptoServiceNeeds,
    DiagnosticCommunicationManagerNeeds,
    DiagnosticComponentNeeds,
    DiagnosticControlNeeds,
    DiagnosticEnableConditionNeeds,
    DiagnosticEventManagerNeeds,
    DiagnosticEventInfoNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import DiagnosticIoControlNeeds
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import DltUserNeeds
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    DiagnosticEventNeeds,
    DiagnosticOperationCycleNeeds,
    DiagnosticRequestFileTransferNeeds,
    DiagnosticRoutineNeeds,
    DiagnosticStorageConditionNeeds,
    DiagnosticUploadDownloadNeeds,
    DiagnosticValueNeeds,
    DiagnosticsCommunicationSecurityNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    DtcStatusChangeNotificationNeeds,
    DoIpActivationLineNeeds,
    DoIpGidNeeds,
    DoIpGidSynchronizationNeeds,
    DoIpPowerModeStatusNeeds,
    DoIpRoutingActivationAuthenticationNeeds,
    DoIpRoutingActivationConfirmationNeeds,
    EcuStateMgrUserNeeds,
    ErrorTracerNeeds,
    FunctionInhibitionAvailabilityNeeds,
    FunctionInhibitionNeeds,
    FurtherActionByteNeeds,
    GlobalSupervisionNeeds,
    HardwareTestNeeds,
    IdsMgrCustomTimestampNeeds,
    IdsMgrNeeds,
    IndicatorStatusNeeds,
    J1939DcmDm19Support,
    J1939RmIncomingRequestServiceNeeds,
    J1939RmOutgoingRequestServiceNeeds,
    NvBlockNeeds,
    ObdControlServiceNeeds,
    ObdInfoServiceNeeds,
    ObdMonitorServiceNeeds,
    ObdPidServiceNeeds,
    ObdRatioDenominatorNeeds,
    ObdRatioServiceNeeds,
    SecureOnBoardCommunicationNeeds,
    SupervisedEntityCheckpointNeeds,
    SyncTimeBaseMgrUserNeeds,
    V2xDataManagerNeeds,
    V2xFacUserNeeds,
    V2xMUserNeeds,
    VendorSpecificServiceNeeds,
    WarningIndicatorRequestedBitNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import RoleBasedDataAssignment, ServiceNeeds, ServiceDependency
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, RefType


class RoleBasedPortAssignment(ARObject, VariationPointCapable):
    """
    This class specifies an assignment of a role to a particular service port (RPortPrototype or PPortPrototype) of an AtomicSwComponentType. With this assignment, the role of the service port can be mapped to a specific ServiceNeeds element, so that a tool is able to create the correct connector.
    """

    # RoleBasedPortAssignment method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.54, p.605
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getPortPrototypeRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPortPrototypeRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRole             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRole             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Service PortPrototype used in the assigned role. This PortPrototype shall either belong to the same AtomicSwComponentType as the SwcInternalBehavior which owns the ServiceDependency or to the same NvBlockSwComponentType as the NvBlockDescriptor.
        self.portPrototypeRef: Optional[RefType] = None

        # This is the role of the assigned Port in the given context. The value shall be a shortName of the Blueprint of a PortInterface as standardized in the Software Specification of the related AUTOSAR Service.
        self.role: Optional[Identifier] = None

    def getPortPrototypeRef(self) -> Optional[RefType]:
        """
        Service PortPrototype used in the assigned role. This PortPrototype shall either belong to the same AtomicSwComponentType as the SwcInternalBehavior which owns the ServiceDependency or to the same NvBlockSwComponentType as the NvBlockDescriptor.
        """
        return self.portPrototypeRef

    def setPortPrototypeRef(self, value: Optional[RefType]) -> RoleBasedPortAssignment:
        """
        Service PortPrototype used in the assigned role. This PortPrototype shall either belong to the same AtomicSwComponentType as the SwcInternalBehavior which owns the ServiceDependency or to the same NvBlockSwComponentType as the NvBlockDescriptor. A None value is a no-op and does not overwrite an existing portPrototypeRef.
        """
        if value is not None:
            self.portPrototypeRef = value
        return self

    def getRole(self) -> Optional[Identifier]:
        """
        This is the role of the assigned Port in the given context. The value shall be a shortName of the Blueprint of a PortInterface as standardized in the Software Specification of the related AUTOSAR Service.
        """
        return self.role

    def setRole(self, value: Optional[Identifier]) -> RoleBasedPortAssignment:
        """
        This is the role of the assigned Port in the given context. The value shall be a shortName of the Blueprint of a PortInterface as standardized in the Software Specification of the related AUTOSAR Service. A None value is a no-op and does not overwrite an existing role.
        """
        if value is not None:
            self.role = value
        return self


class SwcServiceDependency(AtpStructureElement, ServiceDependency):
    """Specialization of ServiceDependency in the context of an SwcInternalBehavior. It allows to associate ports, port groups and (in special cases) data defined for an atomic software component to a given ServiceNeeds element."""

    # SwcServiceDependency method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.56, p.609
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] AddAssignedData                              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getAssignedData                              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] AddAssignedPort                              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getAssignedPorts                             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getRepresentedPortGroupRef                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRepresentedPortGroupRef                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createNvBlockNeeds                           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createDiagnosticCommunicationManagerNeeds    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createDiagnosticComponentNeeds               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createDiagnosticControlNeeds                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createDiagnosticUploadDownloadNeeds          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createDiagnosticsCommunicationSecurityNeeds  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createDiagnosticRoutineNeeds                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createDiagnosticValueNeeds                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createDiagnosticEventNeeds                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createDiagnosticEventInfoNeeds               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createCryptoKeyManagementNeeds               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createCryptoServiceJobNeeds                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createCryptoServiceNeeds                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createEcuStateMgrUserNeeds                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createDtcStatusChangeNotificationNeeds       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createDiagnosticIoControlNeeds               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createDiagnosticEnableConditionNeeds         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createDiagnosticEventManagerNeeds            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createDiagnosticOperationCycleNeeds          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createDiagnosticRequestFileTransferNeeds     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createDiagnosticStorageConditionNeeds        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createFunctionInhibitionAvailabilityNeeds    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createFunctionInhibitionNeeds                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createFurtherActionByteNeeds                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createGlobalSupervisionNeeds                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createHardwareTestNeeds                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createIdsMgrCustomTimestampNeeds             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createIndicatorStatusNeeds                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createJ1939DcmDm19Support                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createJ1939RmIncomingRequestServiceNeeds     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createJ1939RmOutgoingRequestServiceNeeds     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createDltUserNeeds                           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createComMgrUserNeeds                        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createErrorTracerNeeds                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createObdInfoServiceNeeds                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createObdMonitorServiceNeeds                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createObdPidServiceNeeds                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createObdControlServiceNeeds                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createObdRatioServiceNeeds                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createObdRatioDenominatorNeeds               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createDoIpActivationLineNeeds                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createDoIpGidNeeds                           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createDoIpGidSynchronizationNeeds            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createDoIpPowerModeStatusNeeds               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createDoIpRoutingActivationAuthenticationNeeds  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createDoIpRoutingActivationConfirmationNeeds  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createSecureOnBoardCommunicationNeeds        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createSupervisedEntityCheckpointNeeds        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createSyncTimeBaseMgrUserNeeds               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createV2xDataManagerNeeds                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createV2xFacUserNeeds                        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createV2xMUserNeeds                          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createVendorSpecificServiceNeeds             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createWarningIndicatorRequestedBitNeeds      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createIdsMgrNeeds                            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNvBlockNeeds                              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDiagnosticCommunicationManagerNeeds       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDiagnosticRoutineNeeds                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDiagnosticValueNeeds                      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDiagnosticEventNeeds                      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDiagnosticEventInfoNeeds                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCryptoServiceNeeds                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getEcuStateMgrUserNeeds                      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDtcStatusChangeNotificationNeeds          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDiagnosticIoControlNeeds                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDltUserNeeds                              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getComMgrUserNeeds                           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getErrorTracerNeeds                          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getObdInfoServiceNeeds                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getObdMonitorServiceNeeds                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getObdPidServiceNeeds                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getObdControlServiceNeeds                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getServiceNeeds                              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    def __init__(self, parent: ARObject, short_name: str):
        ServiceDependency.__init__(self)
        AtpStructureElement.__init__(self, parent, short_name)

        # Defines the role of an associated data object of the same component. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=assignedData, assignedData.variation Point.shortLabel vh.latestBindingTime=preCompileTime
        self.assignedData: List[RoleBasedDataAssignment] = []

        # Defines the role of an associated port of the same component. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=assignedPort, assignedPort.variation Point.shortLabel vh.latestBindingTime=preCompileTime
        self.assignedPort: List[RoleBasedPortAssignment] = []

        # This reference specifies an association between the ServiceNeeeds and a PortGroup, for example to request a communication mode which applies for communication via these ports. The referred PortGroup shall be local to this atomic SWC, but via the links between the Port Groups, a tool can evaluate this information such that all the ports linked via this port group on the same ECU can be found.
        self.representedPortGroupRef: Optional[RefType] = None

        # The associated ServiceNeeds.
        self.serviceNeeds: Optional[ServiceNeeds] = None

    def AddAssignedData(self, data: Optional[RoleBasedDataAssignment]) -> SwcServiceDependency:
        """Defines the role of an associated data object of the same component. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=assignedData, assignedData.variation Point.shortLabel vh.latestBindingTime=preCompileTime A None value is a no-op and does not append anything."""
        if data is not None:
            self.assignedData.append(data)
        return self

    def getAssignedData(self) -> List[RoleBasedDataAssignment]:
        """Defines the role of an associated data object of the same component. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=assignedData, assignedData.variation Point.shortLabel vh.latestBindingTime=preCompileTime"""
        return self.assignedData

    def AddAssignedPort(self, data: Optional[RoleBasedPortAssignment]) -> SwcServiceDependency:
        """Defines the role of an associated port of the same component. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=assignedPort, assignedPort.variation Point.shortLabel vh.latestBindingTime=preCompileTime A None value is a no-op and does not append anything."""
        if data is not None:
            self.assignedPort.append(data)
        return self

    def getAssignedPorts(self) -> List[RoleBasedPortAssignment]:
        """Defines the role of an associated port of the same component. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=assignedPort, assignedPort.variation Point.shortLabel vh.latestBindingTime=preCompileTime"""
        return self.assignedPort

    def getRepresentedPortGroupRef(self) -> Optional[RefType]:
        """This reference specifies an association between the ServiceNeeeds and a PortGroup, for example to request a communication mode which applies for communication via these ports. The referred PortGroup shall be local to this atomic SWC, but via the links between the Port Groups, a tool can evaluate this information such that all the ports linked via this port group on the same ECU can be found."""
        return self.representedPortGroupRef

    def setRepresentedPortGroupRef(self, value: Optional[RefType]) -> SwcServiceDependency:
        """This reference specifies an association between the ServiceNeeeds and a PortGroup, for example to request a communication mode which applies for communication via these ports. The referred PortGroup shall be local to this atomic SWC, but via the links between the Port Groups, a tool can evaluate this information such that all the ports linked via this port group on the same ECU can be found. A None value is a no-op and does not overwrite an existing representedPortGroupRef."""
        if value is not None:
            self.representedPortGroupRef = value
        return self

    def createNvBlockNeeds(self, short_name: str) -> NvBlockNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, NvBlockNeeds):
            needs = NvBlockNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(NvBlockNeeds, self.getReferrableElement(short_name, NvBlockNeeds))

    def createDiagnosticCommunicationManagerNeeds(self, short_name: str) -> DiagnosticCommunicationManagerNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, DiagnosticCommunicationManagerNeeds):
            needs = DiagnosticCommunicationManagerNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(DiagnosticCommunicationManagerNeeds, self.getReferrableElement(short_name, DiagnosticCommunicationManagerNeeds))

    def createDiagnosticComponentNeeds(self, short_name: str) -> DiagnosticComponentNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, DiagnosticComponentNeeds):
            needs = DiagnosticComponentNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(DiagnosticComponentNeeds, self.getReferrableElement(short_name, DiagnosticComponentNeeds))

    def createDiagnosticControlNeeds(self, short_name: str) -> DiagnosticControlNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, DiagnosticControlNeeds):
            needs = DiagnosticControlNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(DiagnosticControlNeeds, self.getReferrableElement(short_name, DiagnosticControlNeeds))

    def createDiagnosticUploadDownloadNeeds(self, short_name: str) -> DiagnosticUploadDownloadNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, DiagnosticUploadDownloadNeeds):
            needs = DiagnosticUploadDownloadNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(DiagnosticUploadDownloadNeeds, self.getReferrableElement(short_name, DiagnosticUploadDownloadNeeds))

    def createDiagnosticsCommunicationSecurityNeeds(self, short_name: str) -> DiagnosticsCommunicationSecurityNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, DiagnosticsCommunicationSecurityNeeds):
            needs = DiagnosticsCommunicationSecurityNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(DiagnosticsCommunicationSecurityNeeds, self.getReferrableElement(short_name, DiagnosticsCommunicationSecurityNeeds))

    def createDiagnosticRoutineNeeds(self, short_name: str) -> DiagnosticRoutineNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, DiagnosticRoutineNeeds):
            needs = DiagnosticRoutineNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(DiagnosticRoutineNeeds, self.getReferrableElement(short_name, DiagnosticRoutineNeeds))

    def createDiagnosticValueNeeds(self, short_name: str) -> DiagnosticValueNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, DiagnosticValueNeeds):
            needs = DiagnosticValueNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(DiagnosticValueNeeds, self.getReferrableElement(short_name, DiagnosticValueNeeds))

    def createDiagnosticEventNeeds(self, short_name: str) -> DiagnosticEventNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, DiagnosticEventNeeds):
            needs = DiagnosticEventNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(DiagnosticEventNeeds, self.getReferrableElement(short_name, DiagnosticEventNeeds))

    def createDiagnosticEventInfoNeeds(self, short_name: str) -> DiagnosticEventInfoNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, DiagnosticEventInfoNeeds):
            needs = DiagnosticEventInfoNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(DiagnosticEventInfoNeeds, self.getReferrableElement(short_name, DiagnosticEventInfoNeeds))

    def createCryptoKeyManagementNeeds(self, short_name: str) -> CryptoKeyManagementNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, CryptoKeyManagementNeeds):
            needs = CryptoKeyManagementNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(CryptoKeyManagementNeeds, self.getReferrableElement(short_name, CryptoKeyManagementNeeds))

    def createCryptoServiceJobNeeds(self, short_name: str) -> CryptoServiceJobNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, CryptoServiceJobNeeds):
            needs = CryptoServiceJobNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(CryptoServiceJobNeeds, self.getReferrableElement(short_name, CryptoServiceJobNeeds))

    def createCryptoServiceNeeds(self, short_name: str) -> CryptoServiceNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, CryptoServiceNeeds):
            needs = CryptoServiceNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(CryptoServiceNeeds, self.getReferrableElement(short_name, CryptoServiceNeeds))

    def createEcuStateMgrUserNeeds(self, short_name: str) -> EcuStateMgrUserNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, EcuStateMgrUserNeeds):
            needs = EcuStateMgrUserNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(EcuStateMgrUserNeeds, self.getReferrableElement(short_name, EcuStateMgrUserNeeds))

    def createDtcStatusChangeNotificationNeeds(self, short_name: str) -> DtcStatusChangeNotificationNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, DtcStatusChangeNotificationNeeds):
            needs = DtcStatusChangeNotificationNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(DtcStatusChangeNotificationNeeds, self.getReferrableElement(short_name, DtcStatusChangeNotificationNeeds))

    def createDiagnosticIoControlNeeds(self, short_name: str) -> DiagnosticIoControlNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, DiagnosticIoControlNeeds):
            needs = DiagnosticIoControlNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(DiagnosticIoControlNeeds, self.getReferrableElement(short_name, DiagnosticIoControlNeeds))

    def createDiagnosticEnableConditionNeeds(self, short_name: str) -> DiagnosticEnableConditionNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, DiagnosticEnableConditionNeeds):
            needs = DiagnosticEnableConditionNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(DiagnosticEnableConditionNeeds, self.getReferrableElement(short_name, DiagnosticEnableConditionNeeds))

    def createDiagnosticEventManagerNeeds(self, short_name: str) -> DiagnosticEventManagerNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, DiagnosticEventManagerNeeds):
            needs = DiagnosticEventManagerNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(DiagnosticEventManagerNeeds, self.getReferrableElement(short_name, DiagnosticEventManagerNeeds))

    def createDiagnosticOperationCycleNeeds(self, short_name: str) -> DiagnosticOperationCycleNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, DiagnosticOperationCycleNeeds):
            needs = DiagnosticOperationCycleNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(DiagnosticOperationCycleNeeds, self.getReferrableElement(short_name, DiagnosticOperationCycleNeeds))

    def createDiagnosticRequestFileTransferNeeds(self, short_name: str) -> DiagnosticRequestFileTransferNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, DiagnosticRequestFileTransferNeeds):
            needs = DiagnosticRequestFileTransferNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(DiagnosticRequestFileTransferNeeds, self.getReferrableElement(short_name, DiagnosticRequestFileTransferNeeds))

    def createDiagnosticStorageConditionNeeds(self, short_name: str) -> DiagnosticStorageConditionNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, DiagnosticStorageConditionNeeds):
            needs = DiagnosticStorageConditionNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(DiagnosticStorageConditionNeeds, self.getReferrableElement(short_name, DiagnosticStorageConditionNeeds))

    def createFunctionInhibitionAvailabilityNeeds(self, short_name: str) -> FunctionInhibitionAvailabilityNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, FunctionInhibitionAvailabilityNeeds):
            needs = FunctionInhibitionAvailabilityNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(FunctionInhibitionAvailabilityNeeds, self.getReferrableElement(short_name, FunctionInhibitionAvailabilityNeeds))

    def createFunctionInhibitionNeeds(self, short_name: str) -> FunctionInhibitionNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, FunctionInhibitionNeeds):
            needs = FunctionInhibitionNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(FunctionInhibitionNeeds, self.getReferrableElement(short_name, FunctionInhibitionNeeds))

    def createFurtherActionByteNeeds(self, short_name: str) -> FurtherActionByteNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, FurtherActionByteNeeds):
            needs = FurtherActionByteNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(FurtherActionByteNeeds, self.getReferrableElement(short_name, FurtherActionByteNeeds))

    def createGlobalSupervisionNeeds(self, short_name: str) -> GlobalSupervisionNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, GlobalSupervisionNeeds):
            needs = GlobalSupervisionNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(GlobalSupervisionNeeds, self.getReferrableElement(short_name, GlobalSupervisionNeeds))

    def createHardwareTestNeeds(self, short_name: str) -> HardwareTestNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, HardwareTestNeeds):
            needs = HardwareTestNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(HardwareTestNeeds, self.getReferrableElement(short_name, HardwareTestNeeds))

    def createIdsMgrCustomTimestampNeeds(self, short_name: str) -> IdsMgrCustomTimestampNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, IdsMgrCustomTimestampNeeds):
            needs = IdsMgrCustomTimestampNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(IdsMgrCustomTimestampNeeds, self.getReferrableElement(short_name, IdsMgrCustomTimestampNeeds))

    def createIndicatorStatusNeeds(self, short_name: str) -> IndicatorStatusNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, IndicatorStatusNeeds):
            needs = IndicatorStatusNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(IndicatorStatusNeeds, self.getReferrableElement(short_name, IndicatorStatusNeeds))

    def createJ1939DcmDm19Support(self, short_name: str) -> J1939DcmDm19Support:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, J1939DcmDm19Support):
            needs = J1939DcmDm19Support(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(J1939DcmDm19Support, self.getReferrableElement(short_name, J1939DcmDm19Support))

    def createJ1939RmIncomingRequestServiceNeeds(self, short_name: str) -> J1939RmIncomingRequestServiceNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, J1939RmIncomingRequestServiceNeeds):
            needs = J1939RmIncomingRequestServiceNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(J1939RmIncomingRequestServiceNeeds, self.getReferrableElement(short_name, J1939RmIncomingRequestServiceNeeds))

    def createJ1939RmOutgoingRequestServiceNeeds(self, short_name: str) -> J1939RmOutgoingRequestServiceNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, J1939RmOutgoingRequestServiceNeeds):
            needs = J1939RmOutgoingRequestServiceNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(J1939RmOutgoingRequestServiceNeeds, self.getReferrableElement(short_name, J1939RmOutgoingRequestServiceNeeds))

    def createDltUserNeeds(self, short_name: str) -> DltUserNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, DltUserNeeds):
            needs = DltUserNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(DltUserNeeds, self.getReferrableElement(short_name, DltUserNeeds))

    def createComMgrUserNeeds(self, short_name: str) -> ComMgrUserNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, ComMgrUserNeeds):
            needs = ComMgrUserNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(ComMgrUserNeeds, self.getReferrableElement(short_name, ComMgrUserNeeds))

    def createErrorTracerNeeds(self, short_name: str) -> ErrorTracerNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, ErrorTracerNeeds):
            needs = ErrorTracerNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(ErrorTracerNeeds, self.getReferrableElement(short_name, ErrorTracerNeeds))

    def createObdInfoServiceNeeds(self, short_name: str) -> ObdInfoServiceNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, ObdInfoServiceNeeds):
            needs = ObdInfoServiceNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(ObdInfoServiceNeeds, self.getReferrableElement(short_name, ObdInfoServiceNeeds))

    def createObdMonitorServiceNeeds(self, short_name: str) -> ObdMonitorServiceNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, ObdMonitorServiceNeeds):
            needs = ObdMonitorServiceNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(ObdMonitorServiceNeeds, self.getReferrableElement(short_name, ObdMonitorServiceNeeds))

    def createObdPidServiceNeeds(self, short_name: str) -> ObdPidServiceNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, ObdPidServiceNeeds):
            needs = ObdPidServiceNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(ObdPidServiceNeeds, self.getReferrableElement(short_name, ObdPidServiceNeeds))

    def createObdControlServiceNeeds(self, short_name: str) -> ObdControlServiceNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, ObdControlServiceNeeds):
            needs = ObdControlServiceNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(ObdControlServiceNeeds, self.getReferrableElement(short_name, ObdControlServiceNeeds))

    def createObdRatioServiceNeeds(self, short_name: str) -> ObdRatioServiceNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, ObdRatioServiceNeeds):
            needs = ObdRatioServiceNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(ObdRatioServiceNeeds, self.getReferrableElement(short_name, ObdRatioServiceNeeds))

    def createObdRatioDenominatorNeeds(self, short_name: str) -> ObdRatioDenominatorNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, ObdRatioDenominatorNeeds):
            needs = ObdRatioDenominatorNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(ObdRatioDenominatorNeeds, self.getReferrableElement(short_name, ObdRatioDenominatorNeeds))

    def createDoIpActivationLineNeeds(self, short_name: str) -> DoIpActivationLineNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, DoIpActivationLineNeeds):
            needs = DoIpActivationLineNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(DoIpActivationLineNeeds, self.getReferrableElement(short_name, DoIpActivationLineNeeds))

    def createDoIpGidNeeds(self, short_name: str) -> DoIpGidNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, DoIpGidNeeds):
            needs = DoIpGidNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(DoIpGidNeeds, self.getReferrableElement(short_name, DoIpGidNeeds))

    def createDoIpGidSynchronizationNeeds(self, short_name: str) -> DoIpGidSynchronizationNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, DoIpGidSynchronizationNeeds):
            needs = DoIpGidSynchronizationNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(DoIpGidSynchronizationNeeds, self.getReferrableElement(short_name, DoIpGidSynchronizationNeeds))

    def createDoIpPowerModeStatusNeeds(self, short_name: str) -> DoIpPowerModeStatusNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, DoIpPowerModeStatusNeeds):
            needs = DoIpPowerModeStatusNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(DoIpPowerModeStatusNeeds, self.getReferrableElement(short_name, DoIpPowerModeStatusNeeds))

    def createDoIpRoutingActivationAuthenticationNeeds(self, short_name: str) -> DoIpRoutingActivationAuthenticationNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, DoIpRoutingActivationAuthenticationNeeds):
            needs = DoIpRoutingActivationAuthenticationNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(DoIpRoutingActivationAuthenticationNeeds, self.getReferrableElement(short_name, DoIpRoutingActivationAuthenticationNeeds))

    def createDoIpRoutingActivationConfirmationNeeds(self, short_name: str) -> DoIpRoutingActivationConfirmationNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, DoIpRoutingActivationConfirmationNeeds):
            needs = DoIpRoutingActivationConfirmationNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(DoIpRoutingActivationConfirmationNeeds, self.getReferrableElement(short_name, DoIpRoutingActivationConfirmationNeeds))

    def createSecureOnBoardCommunicationNeeds(self, short_name: str) -> SecureOnBoardCommunicationNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, SecureOnBoardCommunicationNeeds):
            needs = SecureOnBoardCommunicationNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(SecureOnBoardCommunicationNeeds, self.getReferrableElement(short_name, SecureOnBoardCommunicationNeeds))

    def createSupervisedEntityCheckpointNeeds(self, short_name: str) -> SupervisedEntityCheckpointNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, SupervisedEntityCheckpointNeeds):
            needs = SupervisedEntityCheckpointNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(SupervisedEntityCheckpointNeeds, self.getReferrableElement(short_name, SupervisedEntityCheckpointNeeds))

    def createSyncTimeBaseMgrUserNeeds(self, short_name: str) -> SyncTimeBaseMgrUserNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, SyncTimeBaseMgrUserNeeds):
            needs = SyncTimeBaseMgrUserNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(SyncTimeBaseMgrUserNeeds, self.getReferrableElement(short_name, SyncTimeBaseMgrUserNeeds))

    def createV2xDataManagerNeeds(self, short_name: str) -> V2xDataManagerNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, V2xDataManagerNeeds):
            needs = V2xDataManagerNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(V2xDataManagerNeeds, self.getReferrableElement(short_name, V2xDataManagerNeeds))

    def createV2xFacUserNeeds(self, short_name: str) -> V2xFacUserNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, V2xFacUserNeeds):
            needs = V2xFacUserNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(V2xFacUserNeeds, self.getReferrableElement(short_name, V2xFacUserNeeds))

    def createV2xMUserNeeds(self, short_name: str) -> V2xMUserNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, V2xMUserNeeds):
            needs = V2xMUserNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(V2xMUserNeeds, self.getReferrableElement(short_name, V2xMUserNeeds))

    def createVendorSpecificServiceNeeds(self, short_name: str) -> VendorSpecificServiceNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, VendorSpecificServiceNeeds):
            needs = VendorSpecificServiceNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(VendorSpecificServiceNeeds, self.getReferrableElement(short_name, VendorSpecificServiceNeeds))

    def createWarningIndicatorRequestedBitNeeds(self, short_name: str) -> WarningIndicatorRequestedBitNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, WarningIndicatorRequestedBitNeeds):
            needs = WarningIndicatorRequestedBitNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(WarningIndicatorRequestedBitNeeds, self.getReferrableElement(short_name, WarningIndicatorRequestedBitNeeds))

    def createIdsMgrNeeds(self, short_name: str) -> IdsMgrNeeds:
        """The associated ServiceNeeds."""
        if not self.IsReferrableElementExists(short_name, IdsMgrNeeds):
            needs = IdsMgrNeeds(self, short_name)
            self.addReferrableElement(needs)
            self.serviceNeeds = needs
        return cast(IdsMgrNeeds, self.getReferrableElement(short_name, IdsMgrNeeds))

    def getNvBlockNeeds(self) -> List[NvBlockNeeds]:
        """The associated ServiceNeeds."""
        return sorted([c for c in self.referrableElements if isinstance(c, NvBlockNeeds)], key=lambda e: e.short_name)

    def getDiagnosticCommunicationManagerNeeds(self) -> List[DiagnosticCommunicationManagerNeeds]:
        """The associated ServiceNeeds."""
        return sorted([c for c in self.referrableElements if isinstance(c, DiagnosticCommunicationManagerNeeds)], key=lambda e: e.short_name)

    def getDiagnosticRoutineNeeds(self) -> List[DiagnosticRoutineNeeds]:
        """The associated ServiceNeeds."""
        return sorted([c for c in self.referrableElements if isinstance(c, DiagnosticRoutineNeeds)], key=lambda e: e.short_name)

    def getDiagnosticValueNeeds(self) -> List[DiagnosticValueNeeds]:
        """The associated ServiceNeeds."""
        return sorted([c for c in self.referrableElements if isinstance(c, DiagnosticValueNeeds)], key=lambda e: e.short_name)

    def getDiagnosticEventNeeds(self) -> List[DiagnosticEventNeeds]:
        """The associated ServiceNeeds."""
        return sorted([c for c in self.referrableElements if isinstance(c, DiagnosticEventNeeds)], key=lambda e: e.short_name)

    def getDiagnosticEventInfoNeeds(self) -> List[DiagnosticEventInfoNeeds]:
        """The associated ServiceNeeds."""
        return sorted([c for c in self.referrableElements if isinstance(c, DiagnosticEventInfoNeeds)], key=lambda e: e.short_name)

    def getCryptoServiceNeeds(self) -> List[CryptoServiceNeeds]:
        """The associated ServiceNeeds."""
        return sorted([c for c in self.referrableElements if isinstance(c, CryptoServiceNeeds)], key=lambda e: e.short_name)

    def getEcuStateMgrUserNeeds(self) -> List[EcuStateMgrUserNeeds]:
        """The associated ServiceNeeds."""
        return sorted([c for c in self.referrableElements if isinstance(c, EcuStateMgrUserNeeds)], key=lambda e: e.short_name)

    def getDtcStatusChangeNotificationNeeds(self) -> List[DtcStatusChangeNotificationNeeds]:
        """The associated ServiceNeeds."""
        return sorted([c for c in self.referrableElements if isinstance(c, DtcStatusChangeNotificationNeeds)], key=lambda e: e.short_name)

    def getDiagnosticIoControlNeeds(self) -> List[DiagnosticIoControlNeeds]:
        """The associated ServiceNeeds."""
        return sorted([c for c in self.referrableElements if isinstance(c, DiagnosticIoControlNeeds)], key=lambda e: e.short_name)

    def getDltUserNeeds(self) -> List[DltUserNeeds]:
        """The associated ServiceNeeds."""
        return sorted([c for c in self.referrableElements if isinstance(c, DltUserNeeds)], key=lambda e: e.short_name)

    def getComMgrUserNeeds(self) -> List[ComMgrUserNeeds]:
        """The associated ServiceNeeds."""
        return sorted([c for c in self.referrableElements if isinstance(c, ComMgrUserNeeds)], key=lambda e: e.short_name)

    def getErrorTracerNeeds(self) -> List[ErrorTracerNeeds]:
        """The associated ServiceNeeds."""
        return sorted([c for c in self.referrableElements if isinstance(c, ErrorTracerNeeds)], key=lambda e: e.short_name)

    def getObdInfoServiceNeeds(self) -> List[ObdInfoServiceNeeds]:
        """The associated ServiceNeeds."""
        return sorted([c for c in self.referrableElements if isinstance(c, ObdInfoServiceNeeds)], key=lambda e: e.short_name)

    def getObdMonitorServiceNeeds(self) -> List[ObdMonitorServiceNeeds]:
        """The associated ServiceNeeds."""
        return sorted([c for c in self.referrableElements if isinstance(c, ObdMonitorServiceNeeds)], key=lambda e: e.short_name)

    def getObdPidServiceNeeds(self) -> List[ObdPidServiceNeeds]:
        """The associated ServiceNeeds."""
        return sorted([c for c in self.referrableElements if isinstance(c, ObdPidServiceNeeds)], key=lambda e: e.short_name)

    def getObdControlServiceNeeds(self) -> List[ObdControlServiceNeeds]:
        """The associated ServiceNeeds."""
        return sorted([c for c in self.referrableElements if isinstance(c, ObdControlServiceNeeds)], key=lambda e: e.short_name)

    def getServiceNeeds(self) -> Optional[ServiceNeeds]:
        """The associated ServiceNeeds."""
        return self.serviceNeeds


class RoleBasedDataTypeAssignment(ARObject, VariationPointCapable):
    """
    This class specifies an assignment of a role to a particular data type of
    a software component (or in the BswModuleBehavior of a module or cluster)
    in the context of an AUTOSAR Service. With this assignment, the role of
    the data type can be mapped to a specific ServiceNeeds element, so that a
    tool is able to create the correct access.
    """

    # RoleBasedDataTypeAssignment method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 12.5, p.227
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getRole                          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRole                          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getUsedImplementationDataTypeRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setUsedImplementationDataTypeRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This is the role of the associated data type in the given context.
        self.role: Optional[Identifier] = None

        # This represents the associated ImplementationDataType.
        self.usedImplementationDataTypeRef: Optional[RefType] = None

    def getRole(self) -> Optional[Identifier]:
        """
        This is the role of the associated data type in the given context.
        """
        return self.role

    def setRole(self, value: Optional[Identifier]) -> RoleBasedDataTypeAssignment:
        """
        This is the role of the associated data type in the given context.
        Only sets the value if it is not None.

        Args:
            value: The role of the associated data type

        Returns:
            self for method chaining
        """
        if value is not None:
            self.role = value
        return self

    def getUsedImplementationDataTypeRef(self) -> Optional[RefType]:
        """
        This represents the associated ImplementationDataType.
        """
        return self.usedImplementationDataTypeRef

    def setUsedImplementationDataTypeRef(self, value: Optional[RefType]) -> RoleBasedDataTypeAssignment:
        """
        This represents the associated ImplementationDataType.
        Only sets the value if it is not None.

        Args:
            value: The reference to the associated ImplementationDataType

        Returns:
            self for method chaining
        """
        if value is not None:
            self.usedImplementationDataTypeRef = value
        return self
