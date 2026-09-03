"""
This module contains classes for representing AUTOSAR service mapping elements
in software component internal behavior templates.
"""

from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    ComMgrUserNeeds,
    CryptoServiceNeeds,
    DiagnosticCommunicationManagerNeeds,
    DiagnosticEnableConditionNeeds,
    DiagnosticEventInfoNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import DiagnosticIoControlNeeds
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import DltUserNeeds
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    DiagnosticEventNeeds,
    DiagnosticOperationCycleNeeds,
    DiagnosticRoutineNeeds,
    DiagnosticStorageConditionNeeds,
    DiagnosticValueNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    DtcStatusChangeNotificationNeeds,
    DoIpRoutingActivationAuthenticationNeeds,
    DoIpRoutingActivationConfirmationNeeds,
    EcuStateMgrUserNeeds,
    ErrorTracerNeeds,
    FunctionInhibitionAvailabilityNeeds,
    IdsMgrNeeds,
    IndicatorStatusNeeds,
    NvBlockNeeds,
    ObdControlServiceNeeds,
    ObdInfoServiceNeeds,
    ObdMonitorServiceNeeds,
    ObdPidServiceNeeds,
    ObdRatioDenominatorNeeds,
    ObdRatioServiceNeeds,
    SecureOnBoardCommunicationNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import RoleBasedDataAssignment, ServiceNeeds, ServiceDependency
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, RefType


class RoleBasedPortAssignment(ARObject, VariationPointCapable):
    """
    A role-based port assignment that links a port prototype to a specific
    role within a service dependency.
    """

    # RoleBasedPortAssignment method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getPortPrototypeRef          [x] impl  [x] docstring  [ ] test
    # [ ] setPortPrototypeRef          [x] impl  [x] docstring  [ ] test
    # [ ] getRole                      [x] impl  [x] docstring  [ ] test
    # [ ] setRole                      [x] impl  [x] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.portPrototypeRef: "RefType" = None
        self.role: "Identifier" = None

    def getPortPrototypeRef(self):
        """
        Gets the port prototype reference.

        Returns:
            RefType: The port prototype reference
        """
        return self.portPrototypeRef

    def setPortPrototypeRef(self, value):
        """
        Sets the port prototype reference.

        Args:
            value: The port prototype reference to set

        Returns:
            self for method chaining
        """
        self.portPrototypeRef = value
        return self

    def getRole(self):
        """
        Gets the role identifier.

        Returns:
            Identifier: The role identifier
        """
        return self.role

    def setRole(self, value):
        """
        Sets the role identifier.

        Args:
            value: The role identifier to set

        Returns:
            self for method chaining
        """
        self.role = value
        return self


class SwcServiceDependency(Identifiable, ServiceDependency, VariationPointCapable):
    """
    Specialization of ServiceDependency in the context of an SwcInternalBehavior. It allows to associate ports, port groups and (in special cases) data defined for an atomic software component to a given ServiceNeeds element.
    """

    # SwcServiceDependency method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.56, p.608
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] AddAssignedData              [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getAssignedData              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] AddAssignedPort              [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getAssignedPorts             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createNvBlockNeeds           [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] createDiagnosticCommunicationManagerNeeds [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] createDiagnosticRoutineNeeds [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] createDiagnosticValueNeeds   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] createDiagnosticEventNeeds   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] createDiagnosticEventInfoNeeds [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] createCryptoServiceNeeds     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] createEcuStateMgrUserNeeds   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] createDtcStatusChangeNotificationNeeds [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] createDiagnosticIoControlNeeds [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] createDltUserNeeds           [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] createComMgrUserNeeds        [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] createErrorTracerNeeds       [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] createDiagnosticEnableConditionNeeds [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] createDiagnosticOperationCycleNeeds [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] createDiagnosticStorageConditionNeeds [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] createFunctionInhibitionAvailabilityNeeds [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] createIndicatorStatusNeeds   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getNvBlockNeeds              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getDiagnosticCommunicationManagerNeeds [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getDiagnosticRoutineNeeds    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getDiagnosticValueNeeds      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getDiagnosticEventNeeds      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getDiagnosticEventInfoNeeds  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getCryptoServiceNeeds        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getEcuStateMgrUserNeeds      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getDtcStatusChangeNotificationNeeds [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getDiagnosticIoControlNeeds  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getDltUserNeeds              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getComMgrUserNeeds           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getErrorTracerNeeds          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createObdInfoServiceNeeds    [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] createObdMonitorServiceNeeds [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] createObdPidServiceNeeds     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getObdInfoServiceNeeds       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getObdMonitorServiceNeeds    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getObdPidServiceNeeds        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRepresentedPortGroup      [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getRepresentedPortGroup      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getServiceNeeds              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self, parent: ARObject, short_name: str):
        ServiceDependency.__init__(self)
        Identifiable.__init__(self, parent, short_name)

        # Defines the role of an associated data object of the same component.
        self.assignedData: List["RoleBasedDataAssignment"] = []

        # Defines the role of an associated port of the same component.
        self.assignedPort: List["RoleBasedPortAssignment"] = []

        # This reference specifies an association between the ServiceNeeeds and a PortGroup, for example to request a communication mode which applies for communication via these ports. The referred PortGroup shall be local to this atomic SWC, but via the links between the Port Groups, a tool can evaluate this information such that all the ports linked via this port group on the same ECU can be found.
        self.representedPortGroup: Optional["RefType"] = None

        # The associated ServiceNeeds.
        self.serviceNeeds: Optional["ServiceNeeds"] = None

    def AddAssignedData(self, data: RoleBasedDataAssignment):
        """
        Adds assigned data to this service dependency.

        Args:
            data: The role-based data assignment to add
        """
        self.assignedData.append(data)

    def getAssignedData(self) -> List[RoleBasedDataAssignment]:
        """
        Gets the list of assigned data.

        Returns:
            List[RoleBasedDataAssignment]: The assigned data list
        """
        return self.assignedData

    def AddAssignedPort(self, data: RoleBasedPortAssignment):
        """
        Adds an assigned port to this service dependency.

        Args:
            data: The role-based port assignment to add
        """
        self.assignedPort.append(data)

    def getAssignedPorts(self) -> List[RoleBasedPortAssignment]:
        """
        Gets the list of assigned ports.

        Returns:
            List[RoleBasedPortAssignment]: The assigned ports list
        """
        return self.assignedPort

    def createNvBlockNeeds(self, short_name: str) -> NvBlockNeeds:
        """
        Creates or retrieves an NvBlockNeeds element.

        Args:
            short_name: The short name for the needs element

        Returns:
            NvBlockNeeds: The created or existing needs element
        """
        if not self.IsElementExists(short_name, NvBlockNeeds):
            needs = NvBlockNeeds(self, short_name)
            self.addElement(needs)
            self.serviceNeeds = needs
        return self.getElement(short_name, NvBlockNeeds)

    def createDiagnosticCommunicationManagerNeeds(self, short_name: str) -> DiagnosticCommunicationManagerNeeds:
        """
        Creates or retrieves a DiagnosticCommunicationManagerNeeds element.

        Args:
            short_name: The short name for the needs element

        Returns:
            DiagnosticCommunicationManagerNeeds: The created or existing needs
                element
        """
        if not self.IsElementExists(short_name, DiagnosticCommunicationManagerNeeds):
            needs = DiagnosticCommunicationManagerNeeds(self, short_name)
            self.addElement(needs)
            self.serviceNeeds = needs
        return self.getElement(short_name, DiagnosticCommunicationManagerNeeds)

    def createDiagnosticRoutineNeeds(self, short_name: str) -> DiagnosticRoutineNeeds:
        """
        Creates or retrieves a DiagnosticRoutineNeeds element.

        Args:
            short_name: The short name for the needs element

        Returns:
            DiagnosticRoutineNeeds: The created or existing needs element
        """
        if not self.IsElementExists(short_name, DiagnosticRoutineNeeds):
            needs = DiagnosticRoutineNeeds(self, short_name)
            self.addElement(needs)
            self.serviceNeeds = needs
        return self.getElement(short_name, DiagnosticRoutineNeeds)

    def createDiagnosticValueNeeds(self, short_name: str) -> DiagnosticValueNeeds:
        """
        Creates or retrieves a DiagnosticValueNeeds element.

        Args:
            short_name: The short name for the needs element

        Returns:
            DiagnosticValueNeeds: The created or existing needs element
        """
        if not self.IsElementExists(short_name, DiagnosticValueNeeds):
            needs = DiagnosticValueNeeds(self, short_name)
            self.addElement(needs)
            self.serviceNeeds = needs
        return self.getElement(short_name, DiagnosticValueNeeds)

    def createDiagnosticEventNeeds(self, short_name: str) -> DiagnosticEventNeeds:
        """
        Creates or retrieves a DiagnosticEventNeeds element.

        Args:
            short_name: The short name for the needs element

        Returns:
            DiagnosticEventNeeds: The created or existing needs element
        """
        if not self.IsElementExists(short_name, DiagnosticEventNeeds):
            needs = DiagnosticEventNeeds(self, short_name)
            self.addElement(needs)
            self.serviceNeeds = needs
        return self.getElement(short_name, DiagnosticEventNeeds)

    def createDiagnosticEventInfoNeeds(self, short_name: str) -> DiagnosticEventInfoNeeds:
        """
        Creates or retrieves a DiagnosticEventInfoNeeds element.

        Args:
            short_name: The short name for the needs element

        Returns:
            DiagnosticEventInfoNeeds: The created or existing needs element
        """
        if not self.IsElementExists(short_name, DiagnosticEventInfoNeeds):
            needs = DiagnosticEventInfoNeeds(self, short_name)
            self.addElement(needs)
            self.serviceNeeds = needs
        return self.getElement(short_name, DiagnosticEventInfoNeeds)

    def createCryptoServiceNeeds(self, short_name: str) -> CryptoServiceNeeds:
        """
        Creates or retrieves a CryptoServiceNeeds element.

        Args:
            short_name: The short name for the needs element

        Returns:
            CryptoServiceNeeds: The created or existing needs element
        """
        if not self.IsElementExists(short_name, CryptoServiceNeeds):
            needs = CryptoServiceNeeds(self, short_name)
            self.addElement(needs)
            self.serviceNeeds = needs
        return self.getElement(short_name, CryptoServiceNeeds)

    def createEcuStateMgrUserNeeds(self, short_name: str) -> EcuStateMgrUserNeeds:
        """
        Creates or retrieves an EcuStateMgrUserNeeds element.

        Args:
            short_name: The short name for the needs element

        Returns:
            EcuStateMgrUserNeeds: The created or existing needs element
        """
        if not self.IsElementExists(short_name, EcuStateMgrUserNeeds):
            needs = EcuStateMgrUserNeeds(self, short_name)
            self.addElement(needs)
            self.serviceNeeds = needs
        return self.getElement(short_name, EcuStateMgrUserNeeds)

    def createDtcStatusChangeNotificationNeeds(self, short_name: str) -> DtcStatusChangeNotificationNeeds:
        """
        Creates or retrieves a DtcStatusChangeNotificationNeeds element.

        Args:
            short_name: The short name for the needs element

        Returns:
            DtcStatusChangeNotificationNeeds: The created or existing needs
                element
        """
        if not self.IsElementExists(short_name, DtcStatusChangeNotificationNeeds):
            needs = DtcStatusChangeNotificationNeeds(self, short_name)
            self.addElement(needs)
            self.serviceNeeds = needs
        return self.getElement(short_name, DtcStatusChangeNotificationNeeds)

    def createDiagnosticIoControlNeeds(self, short_name: str) -> DiagnosticIoControlNeeds:
        """
        Creates or retrieves a DiagnosticIoControlNeeds element.

        Args:
            short_name: The short name for the needs element

        Returns:
            DiagnosticIoControlNeeds: The created or existing needs element
        """
        if not self.IsElementExists(short_name, DiagnosticIoControlNeeds):
            needs = DiagnosticIoControlNeeds(self, short_name)
            self.addElement(needs)
            self.serviceNeeds = needs
        return self.getElement(short_name, DiagnosticIoControlNeeds)

    def createDiagnosticEnableConditionNeeds(self, short_name: str) -> DiagnosticEnableConditionNeeds:
        """
        Creates or retrieves a DiagnosticEnableConditionNeeds element.

        Args:
            short_name: The short name for the needs element

        Returns:
            DiagnosticEnableConditionNeeds: The created or existing needs element
        """
        if not self.IsElementExists(short_name, DiagnosticEnableConditionNeeds):
            needs = DiagnosticEnableConditionNeeds(self, short_name)
            self.addElement(needs)
            self.serviceNeeds = needs
        return self.getElement(short_name, DiagnosticEnableConditionNeeds)

    def createDiagnosticOperationCycleNeeds(self, short_name: str) -> DiagnosticOperationCycleNeeds:
        """
        Creates or retrieves a DiagnosticOperationCycleNeeds element.

        Args:
            short_name: The short name for the needs element

        Returns:
            DiagnosticOperationCycleNeeds: The created or existing needs element
        """
        if not self.IsElementExists(short_name, DiagnosticOperationCycleNeeds):
            needs = DiagnosticOperationCycleNeeds(self, short_name)
            self.addElement(needs)
            self.serviceNeeds = needs
        return self.getElement(short_name, DiagnosticOperationCycleNeeds)

    def createDiagnosticStorageConditionNeeds(self, short_name: str) -> DiagnosticStorageConditionNeeds:
        """
        Creates or retrieves a DiagnosticStorageConditionNeeds element.

        Args:
            short_name: The short name for the needs element

        Returns:
            DiagnosticStorageConditionNeeds: The created or existing needs element
        """
        if not self.IsElementExists(short_name, DiagnosticStorageConditionNeeds):
            needs = DiagnosticStorageConditionNeeds(self, short_name)
            self.addElement(needs)
            self.serviceNeeds = needs
        return self.getElement(short_name, DiagnosticStorageConditionNeeds)

    def createFunctionInhibitionAvailabilityNeeds(self, short_name: str) -> FunctionInhibitionAvailabilityNeeds:
        """
        Creates or retrieves a FunctionInhibitionAvailabilityNeeds element.

        Args:
            short_name: The short name for the needs element

        Returns:
            FunctionInhibitionAvailabilityNeeds: The created or existing needs element
        """
        if not self.IsElementExists(short_name, FunctionInhibitionAvailabilityNeeds):
            needs = FunctionInhibitionAvailabilityNeeds(self, short_name)
            self.addElement(needs)
            self.serviceNeeds = needs
        return self.getElement(short_name, FunctionInhibitionAvailabilityNeeds)

    def createIndicatorStatusNeeds(self, short_name: str) -> IndicatorStatusNeeds:
        """
        Creates or retrieves an IndicatorStatusNeeds element.

        Args:
            short_name: The short name for the needs element

        Returns:
            IndicatorStatusNeeds: The created or existing needs element
        """
        if not self.IsElementExists(short_name, IndicatorStatusNeeds):
            needs = IndicatorStatusNeeds(self, short_name)
            self.addElement(needs)
            self.serviceNeeds = needs
        return self.getElement(short_name, IndicatorStatusNeeds)

    def createDltUserNeeds(self, short_name: str) -> DltUserNeeds:
        """
        Creates or retrieves a DltUserNeeds element.

        Args:
            short_name: The short name for the needs element

        Returns:
            DltUserNeeds: The created or existing needs element
        """
        if not self.IsElementExists(short_name, DltUserNeeds):
            needs = DltUserNeeds(self, short_name)
            self.addElement(needs)
            self.serviceNeeds = needs
        return self.getElement(short_name, DltUserNeeds)

    def createComMgrUserNeeds(self, short_name: str) -> ComMgrUserNeeds:
        """
        Creates or retrieves a ComMgrUserNeeds element.

        Args:
            short_name: The short name for the needs element

        Returns:
            ComMgrUserNeeds: The created or existing needs element
        """
        if not self.IsElementExists(short_name, ComMgrUserNeeds):
            needs = ComMgrUserNeeds(self, short_name)
            self.addElement(needs)
            self.serviceNeeds = needs
        return self.getElement(short_name, ComMgrUserNeeds)

    def createErrorTracerNeeds(self, short_name: str) -> ErrorTracerNeeds:
        """
        Creates or retrieves an ErrorTracerNeeds element.

        Args:
            short_name: The short name for the needs element

        Returns:
            ErrorTracerNeeds: The created or existing needs element
        """
        if not self.IsElementExists(short_name, ErrorTracerNeeds):
            needs = ErrorTracerNeeds(self, short_name)
            self.addElement(needs)
            self.serviceNeeds = needs
        return self.getElement(short_name, ErrorTracerNeeds)

    def createObdInfoServiceNeeds(self, short_name: str) -> ObdInfoServiceNeeds:
        """
        Creates or retrieves an ObdInfoServiceNeeds element.

        Args:
            short_name: The short name for the needs element

        Returns:
            ObdInfoServiceNeeds: The created or existing needs element
        """
        if not self.IsElementExists(short_name, ObdInfoServiceNeeds):
            needs = ObdInfoServiceNeeds(self, short_name)
            self.addElement(needs)
            self.serviceNeeds = needs
        return self.getElement(short_name, ObdInfoServiceNeeds)

    def createObdMonitorServiceNeeds(self, short_name: str) -> ObdMonitorServiceNeeds:
        """
        Creates or retrieves an ObdMonitorServiceNeeds element.

        Args:
            short_name: The short name for the needs element

        Returns:
            ObdMonitorServiceNeeds: The created or existing needs element
        """
        if not self.IsElementExists(short_name, ObdMonitorServiceNeeds):
            needs = ObdMonitorServiceNeeds(self, short_name)
            self.addElement(needs)
            self.serviceNeeds = needs
        return self.getElement(short_name, ObdMonitorServiceNeeds)

    def createObdPidServiceNeeds(self, short_name: str) -> ObdPidServiceNeeds:
        """
        Creates or retrieves an ObdPidServiceNeeds element.

        Args:
            short_name: The short name for the needs element

        Returns:
            ObdPidServiceNeeds: The created or existing needs element
        """
        if not self.IsElementExists(short_name, ObdPidServiceNeeds):
            needs = ObdPidServiceNeeds(self, short_name)
            self.addElement(needs)
            self.serviceNeeds = needs
        return self.getElement(short_name, ObdPidServiceNeeds)

    def createObdControlServiceNeeds(self, short_name: str) -> ObdControlServiceNeeds:
        """
        Creates or retrieves an ObdControlServiceNeeds element.

        Args:
            short_name: The short name for the needs element

        Returns:
            ObdControlServiceNeeds: The created or existing needs element
        """
        if not self.IsElementExists(short_name, ObdControlServiceNeeds):
            needs = ObdControlServiceNeeds(self, short_name)
            self.addElement(needs)
            self.serviceNeeds = needs
        return self.getElement(short_name, ObdControlServiceNeeds)

    def createObdRatioServiceNeeds(self, short_name: str) -> ObdRatioServiceNeeds:
        """
        Creates or retrieves an ObdRatioServiceNeeds element.

        Args:
            short_name: The short name for the needs element

        Returns:
            ObdRatioServiceNeeds: The created or existing needs element
        """
        if not self.IsElementExists(short_name, ObdRatioServiceNeeds):
            needs = ObdRatioServiceNeeds(self, short_name)
            self.addElement(needs)
            self.serviceNeeds = needs
        return self.getElement(short_name, ObdRatioServiceNeeds)

    def createObdRatioDenominatorNeeds(self, short_name: str) -> ObdRatioDenominatorNeeds:
        """
        Creates or retrieves an ObdRatioDenominatorNeeds element.

        Args:
            short_name: The short name for the needs element

        Returns:
            ObdRatioDenominatorNeeds: The created or existing needs element
        """
        if not self.IsElementExists(short_name, ObdRatioDenominatorNeeds):
            needs = ObdRatioDenominatorNeeds(self, short_name)
            self.addElement(needs)
            self.serviceNeeds = needs
        return self.getElement(short_name, ObdRatioDenominatorNeeds)

    def createDoIpRoutingActivationAuthenticationNeeds(self, short_name: str) -> DoIpRoutingActivationAuthenticationNeeds:
        """
        Creates or retrieves a DoIpRoutingActivationAuthenticationNeeds element.

        Args:
            short_name: The short name for the needs element

        Returns:
            DoIpRoutingActivationAuthenticationNeeds: The created or existing needs element
        """
        if not self.IsElementExists(short_name, DoIpRoutingActivationAuthenticationNeeds):
            needs = DoIpRoutingActivationAuthenticationNeeds(self, short_name)
            self.addElement(needs)
            self.serviceNeeds = needs
        return self.getElement(short_name, DoIpRoutingActivationAuthenticationNeeds)

    def createDoIpRoutingActivationConfirmationNeeds(self, short_name: str) -> DoIpRoutingActivationConfirmationNeeds:
        """
        Creates or retrieves a DoIpRoutingActivationConfirmationNeeds element.

        Args:
            short_name: The short name for the needs element

        Returns:
            DoIpRoutingActivationConfirmationNeeds: The created or existing needs element
        """
        if not self.IsElementExists(short_name, DoIpRoutingActivationConfirmationNeeds):
            needs = DoIpRoutingActivationConfirmationNeeds(self, short_name)
            self.addElement(needs)
            self.serviceNeeds = needs
        return self.getElement(short_name, DoIpRoutingActivationConfirmationNeeds)

    def createSecureOnBoardCommunicationNeeds(self, short_name: str) -> SecureOnBoardCommunicationNeeds:
        """
        Creates or retrieves a SecureOnBoardCommunicationNeeds element.

        Args:
            short_name: The short name for the needs element

        Returns:
            SecureOnBoardCommunicationNeeds: The created or existing needs element
        """
        if not self.IsElementExists(short_name, SecureOnBoardCommunicationNeeds):
            needs = SecureOnBoardCommunicationNeeds(self, short_name)
            self.addElement(needs)
            self.serviceNeeds = needs
        return self.getElement(short_name, SecureOnBoardCommunicationNeeds)

    def createIdsMgrNeeds(self, short_name: str) -> IdsMgrNeeds:
        """
        Creates or retrieves an IdsMgrNeeds element.

        Args:
            short_name: The short name for the needs element

        Returns:
            IdsMgrNeeds: The created or existing needs element
        """
        if not self.IsElementExists(short_name, IdsMgrNeeds):
            needs = IdsMgrNeeds(self, short_name)
            self.addElement(needs)
            self.serviceNeeds = needs
        return self.getElement(short_name, IdsMgrNeeds)

    def getNvBlockNeeds(self) -> List[NvBlockNeeds]:
        """
        Gets sorted NvBlockNeeds elements.

        Returns:
            List[NvBlockNeeds]: Sorted list of NvBlockNeeds
        """
        return sorted(filter(lambda c: isinstance(c, NvBlockNeeds), self.elements), key=lambda e: e.short_name)

    def getDiagnosticCommunicationManagerNeeds(self) -> List[DiagnosticCommunicationManagerNeeds]:
        """
        Gets sorted DiagnosticCommunicationManagerNeeds elements.

        Returns:
            List[DiagnosticCommunicationManagerNeeds]: Sorted list of
                DiagnosticCommunicationManagerNeeds
        """
        return sorted(filter(lambda c: isinstance(c, DiagnosticCommunicationManagerNeeds), self.elements), key=lambda e: e.short_name)

    def getDiagnosticRoutineNeeds(self) -> List[DiagnosticRoutineNeeds]:
        """
        Gets sorted DiagnosticRoutineNeeds elements.

        Returns:
            List[DiagnosticRoutineNeeds]: Sorted list of
                DiagnosticRoutineNeeds
        """
        return sorted(filter(lambda c: isinstance(c, DiagnosticRoutineNeeds), self.elements), key=lambda e: e.short_name)

    def getDiagnosticValueNeeds(self) -> List[DiagnosticValueNeeds]:
        """
        Gets sorted DiagnosticValueNeeds elements.

        Returns:
            List[DiagnosticValueNeeds]: Sorted list of DiagnosticValueNeeds
        """
        return sorted(filter(lambda c: isinstance(c, DiagnosticValueNeeds), self.elements), key=lambda e: e.short_name)

    def getDiagnosticEventNeeds(self) -> List[DiagnosticEventNeeds]:
        """
        Gets sorted DiagnosticEventNeeds elements.

        Returns:
            List[DiagnosticEventNeeds]: Sorted list of DiagnosticEventNeeds
        """
        return sorted(filter(lambda c: isinstance(c, DiagnosticEventNeeds), self.elements), key=lambda e: e.short_name)

    def getDiagnosticEventInfoNeeds(self) -> List[DiagnosticEventInfoNeeds]:
        """
        Gets sorted DiagnosticEventInfoNeeds elements.

        Returns:
            List[DiagnosticEventInfoNeeds]: Sorted list of
                DiagnosticEventInfoNeeds
        """
        return sorted(filter(lambda c: isinstance(c, DiagnosticEventInfoNeeds), self.elements), key=lambda e: e.short_name)

    def getCryptoServiceNeeds(self) -> List[CryptoServiceNeeds]:
        """
        Gets sorted CryptoServiceNeeds elements.

        Returns:
            List[CryptoServiceNeeds]: Sorted list of CryptoServiceNeeds
        """
        return sorted(filter(lambda c: isinstance(c, CryptoServiceNeeds), self.elements), key=lambda e: e.short_name)

    def getEcuStateMgrUserNeeds(self) -> List[EcuStateMgrUserNeeds]:
        """
        Gets sorted EcuStateMgrUserNeeds elements.

        Returns:
            List[EcuStateMgrUserNeeds]: Sorted list of EcuStateMgrUserNeeds
        """
        return sorted(filter(lambda c: isinstance(c, EcuStateMgrUserNeeds), self.elements), key=lambda e: e.short_name)

    def getDtcStatusChangeNotificationNeeds(self) -> List[DtcStatusChangeNotificationNeeds]:
        """
        Gets sorted DtcStatusChangeNotificationNeeds elements.

        Returns:
            List[DtcStatusChangeNotificationNeeds]: Sorted list of
                DtcStatusChangeNotificationNeeds
        """
        return sorted(filter(lambda c: isinstance(c, DtcStatusChangeNotificationNeeds), self.elements), key=lambda e: e.short_name)

    def getDiagnosticIoControlNeeds(self) -> List[DiagnosticIoControlNeeds]:
        """
        Gets sorted DiagnosticIoControlNeeds elements.

        Returns:
            List[DiagnosticIoControlNeeds]: Sorted list of
                DiagnosticIoControlNeeds
        """
        return sorted(filter(lambda c: isinstance(c, DiagnosticIoControlNeeds), self.elements), key=lambda e: e.short_name)

    def getDltUserNeeds(self) -> List[DltUserNeeds]:
        """
        Gets sorted DltUserNeeds elements.

        Returns:
            List[DltUserNeeds]: Sorted list of DltUserNeeds
        """
        return sorted(filter(lambda c: isinstance(c, DltUserNeeds), self.elements), key=lambda e: e.short_name)

    def getComMgrUserNeeds(self) -> List[ComMgrUserNeeds]:
        """
        Gets sorted ComMgrUserNeeds elements.

        Returns:
            List[ComMgrUserNeeds]: Sorted list of ComMgrUserNeeds
        """
        return sorted(filter(lambda c: isinstance(c, ComMgrUserNeeds), self.elements), key=lambda e: e.short_name)

    def getErrorTracerNeeds(self) -> List[ErrorTracerNeeds]:
        """
        Gets sorted ErrorTracerNeeds elements.

        Returns:
            List[ErrorTracerNeeds]: Sorted list of ErrorTracerNeeds
        """
        return sorted(filter(lambda c: isinstance(c, ErrorTracerNeeds), self.elements), key=lambda e: e.short_name)

    def getObdInfoServiceNeeds(self) -> List[ObdInfoServiceNeeds]:
        """
        Gets sorted ObdInfoServiceNeeds elements.

        Returns:
            List[ObdInfoServiceNeeds]: Sorted list of ObdInfoServiceNeeds
        """
        return sorted(filter(lambda c: isinstance(c, ObdInfoServiceNeeds), self.elements), key=lambda e: e.short_name)

    def getObdMonitorServiceNeeds(self) -> List[ObdMonitorServiceNeeds]:
        """
        Gets sorted ObdMonitorServiceNeeds elements.

        Returns:
            List[ObdMonitorServiceNeeds]: Sorted list of ObdMonitorServiceNeeds
        """
        return sorted(filter(lambda c: isinstance(c, ObdMonitorServiceNeeds), self.elements), key=lambda e: e.short_name)

    def getObdPidServiceNeeds(self) -> List[ObdPidServiceNeeds]:
        """
        Gets sorted ObdPidServiceNeeds elements.

        Returns:
            List[ObdPidServiceNeeds]: Sorted list of ObdPidServiceNeeds
        """
        return sorted(filter(lambda c: isinstance(c, ObdPidServiceNeeds), self.elements), key=lambda e: e.short_name)

    def getObdControlServiceNeeds(self) -> List[ObdControlServiceNeeds]:
        """
        Gets sorted ObdControlServiceNeeds elements.

        Returns:
            List[ObdControlServiceNeeds]: Sorted list of ObdControlServiceNeeds
        """
        return sorted(filter(lambda c: isinstance(c, ObdControlServiceNeeds), self.elements), key=lambda e: e.short_name)

    def getServiceNeeds(self) -> List[ServiceNeeds]:
        """
        Gets sorted ServiceNeeds elements.

        Returns:
            List[ServiceNeeds]: Sorted list of ServiceNeeds
        """
        return sorted(filter(lambda c: isinstance(c, ServiceNeeds), self.elements), key=lambda e: e.short_name)

    def setRepresentedPortGroup(self, value: Optional["RefType"]) -> "SwcServiceDependency":
        """
        This reference specifies an association between the ServiceNeeeds and a PortGroup, for example to request a communication mode which applies for communication via these ports. The referred PortGroup shall be local to this atomic SWC, but via the links between the Port Groups, a tool can evaluate this information such that all the ports linked via this port group on the same ECU can be found.
        A None value is a no-op and does not overwrite an existing representedPortGroup.

        Args:
            value: The represented port group reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.representedPortGroup = value
        return self

    def getRepresentedPortGroup(self) -> Optional["RefType"]:
        """
        This reference specifies an association between the ServiceNeeeds and a PortGroup, for example to request a communication mode which applies for communication via these ports. The referred PortGroup shall be local to this atomic SWC, but via the links between the Port Groups, a tool can evaluate this information such that all the ports linked via this port group on the same ECU can be found.

        Returns:
            RefType: The represented port group reference
        """
        return self.representedPortGroup


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

    def setRole(self, value: Optional[Identifier]) -> "RoleBasedDataTypeAssignment":
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

    def setUsedImplementationDataTypeRef(self, value: Optional[RefType]) -> "RoleBasedDataTypeAssignment":
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
