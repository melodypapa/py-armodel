"""
This module contains classes for representing AUTOSAR service mapping elements
in software component internal behavior templates.
"""

from typing import List
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import CryptoServiceNeeds, DiagnosticCommunicationManagerNeeds, DiagnosticEventInfoNeeds
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import DltUserNeeds
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import DiagnosticEventNeeds, DiagnosticRoutineNeeds, DiagnosticValueNeeds
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import DtcStatusChangeNotificationNeeds, EcuStateMgrUserNeeds, NvBlockNeeds
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import RoleBasedDataAssignment, ServiceNeeds, ServiceDependency
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, RefType


class RoleBasedPortAssignment(ARObject):
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

        self.portPrototypeRef: 'RefType' = None
        self.role: 'Identifier' = None

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


class SwcServiceDependency(ServiceDependency):
    """
    A service dependency for an atomic software component that defines the
    required services and their assignments.
    """
    # SwcServiceDependency method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] AddAssignedData              [x] impl  [x] docstring  [ ] test
    # [ ] getAssignedData              [x] impl  [x] docstring  [ ] test
    # [ ] AddAssignedPort              [x] impl  [x] docstring  [ ] test
    # [ ] getAssignedPorts             [x] impl  [x] docstring  [ ] test
    # [ ] createNvBlockNeeds           [x] impl  [x] docstring  [ ] test
    # [ ] createDiagnosticCommunicationManagerNeeds [x] impl  [x] docstring  [ ] test
    # [ ] createDiagnosticRoutineNeeds [x] impl  [x] docstring  [ ] test
    # [ ] createDiagnosticValueNeeds   [x] impl  [x] docstring  [ ] test
    # [ ] createDiagnosticEventNeeds   [x] impl  [x] docstring  [ ] test
    # [ ] createDiagnosticEventInfoNeeds [x] impl  [x] docstring  [ ] test
    # [ ] createCryptoServiceNeeds     [x] impl  [x] docstring  [ ] test
    # [ ] createEcuStateMgrUserNeeds   [x] impl  [x] docstring  [ ] test
    # [ ] createDtcStatusChangeNotificationNeeds [x] impl  [x] docstring  [ ] test
    # [ ] createDltUserNeeds           [x] impl  [x] docstring  [ ] test
    # [ ] getNvBlockNeeds              [x] impl  [x] docstring  [ ] test
    # [ ] getDiagnosticCommunicationManagerNeeds [x] impl  [x] docstring  [ ] test
    # [ ] getDiagnosticRoutineNeeds    [x] impl  [x] docstring  [ ] test
    # [ ] getDiagnosticValueNeeds      [x] impl  [x] docstring  [ ] test
    # [ ] getDiagnosticEventNeeds      [x] impl  [x] docstring  [ ] test
    # [ ] getDiagnosticEventInfoNeeds  [x] impl  [x] docstring  [ ] test
    # [ ] getCryptoServiceNeeds        [x] impl  [x] docstring  [ ] test
    # [ ] getEcuStateMgrUserNeeds      [x] impl  [x] docstring  [ ] test
    # [ ] getDtcStatusChangeNotificationNeeds [x] impl  [x] docstring  [ ] test
    # [ ] getDltUserNeeds              [x] impl  [x] docstring  [ ] test
    # [ ] getServiceNeeds              [x] impl  [x] docstring  [ ] test


    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self._assigned_data: List['RoleBasedDataAssignment'] = []
        self._assigned_ports: List['RoleBasedPortAssignment'] = []

    def AddAssignedData(self, data: RoleBasedDataAssignment):
        """
        Adds assigned data to this service dependency.

        Args:
            data: The role-based data assignment to add
        """
        self._assigned_data.append(data)

    def getAssignedData(self) -> List[RoleBasedDataAssignment]:
        """
        Gets the list of assigned data.

        Returns:
            List[RoleBasedDataAssignment]: The assigned data list
        """
        return self._assigned_data

    def AddAssignedPort(self, data: RoleBasedPortAssignment):
        """
        Adds an assigned port to this service dependency.

        Args:
            data: The role-based port assignment to add
        """
        self._assigned_ports.append(data)

    def getAssignedPorts(self) -> List[RoleBasedPortAssignment]:
        """
        Gets the list of assigned ports.

        Returns:
            List[RoleBasedPortAssignment]: The assigned ports list
        """
        return self._assigned_ports

    def createNvBlockNeeds(self, short_name: str) -> NvBlockNeeds:
        """
        Creates or retrieves an NvBlockNeeds element.

        Args:
            short_name: The short name for the needs element

        Returns:
            NvBlockNeeds: The created or existing needs element
        """
        if (not self.IsElementExists(short_name)):
            needs = NvBlockNeeds(self, short_name)
            self.addElement(needs)
        return self.getElement(short_name)

    def createDiagnosticCommunicationManagerNeeds(self, short_name: str) -> DiagnosticCommunicationManagerNeeds:
        """
        Creates or retrieves a DiagnosticCommunicationManagerNeeds element.

        Args:
            short_name: The short name for the needs element

        Returns:
            DiagnosticCommunicationManagerNeeds: The created or existing needs
                element
        """
        if (not self.IsElementExists(short_name)):
            needs = DiagnosticCommunicationManagerNeeds(self, short_name)
            self.addElement(needs)
        return self.getElement(short_name)

    def createDiagnosticRoutineNeeds(self, short_name: str) -> DiagnosticRoutineNeeds:
        """
        Creates or retrieves a DiagnosticRoutineNeeds element.

        Args:
            short_name: The short name for the needs element

        Returns:
            DiagnosticRoutineNeeds: The created or existing needs element
        """
        if (not self.IsElementExists(short_name)):
            needs = DiagnosticRoutineNeeds(self, short_name)
            self.addElement(needs)
        return self.getElement(short_name)

    def createDiagnosticValueNeeds(self, short_name: str) -> DiagnosticValueNeeds:
        """
        Creates or retrieves a DiagnosticValueNeeds element.

        Args:
            short_name: The short name for the needs element

        Returns:
            DiagnosticValueNeeds: The created or existing needs element
        """
        if (not self.IsElementExists(short_name)):
            needs = DiagnosticValueNeeds(self, short_name)
            self.addElement(needs)
        return self.getElement(short_name)

    def createDiagnosticEventNeeds(self, short_name: str) -> DiagnosticEventNeeds:
        """
        Creates or retrieves a DiagnosticEventNeeds element.

        Args:
            short_name: The short name for the needs element

        Returns:
            DiagnosticEventNeeds: The created or existing needs element
        """
        if (not self.IsElementExists(short_name)):
            needs = DiagnosticEventNeeds(self, short_name)
            self.addElement(needs)
        return self.getElement(short_name)

    def createDiagnosticEventInfoNeeds(self, short_name: str) -> DiagnosticEventInfoNeeds:
        """
        Creates or retrieves a DiagnosticEventInfoNeeds element.

        Args:
            short_name: The short name for the needs element

        Returns:
            DiagnosticEventInfoNeeds: The created or existing needs element
        """
        if (not self.IsElementExists(short_name)):
            needs = DiagnosticEventInfoNeeds(self, short_name)
            self.addElement(needs)
        return self.getElement(short_name)

    def createCryptoServiceNeeds(self, short_name: str) -> CryptoServiceNeeds:
        """
        Creates or retrieves a CryptoServiceNeeds element.

        Args:
            short_name: The short name for the needs element

        Returns:
            CryptoServiceNeeds: The created or existing needs element
        """
        if (not self.IsElementExists(short_name)):
            needs = CryptoServiceNeeds(self, short_name)
            self.addElement(needs)
        return self.getElement(short_name)

    def createEcuStateMgrUserNeeds(self, short_name: str) -> EcuStateMgrUserNeeds:
        """
        Creates or retrieves an EcuStateMgrUserNeeds element.

        Args:
            short_name: The short name for the needs element

        Returns:
            EcuStateMgrUserNeeds: The created or existing needs element
        """
        if (not self.IsElementExists(short_name)):
            needs = EcuStateMgrUserNeeds(self, short_name)
            self.addElement(needs)
        return self.getElement(short_name)

    def createDtcStatusChangeNotificationNeeds(self, short_name: str) -> DtcStatusChangeNotificationNeeds:
        """
        Creates or retrieves a DtcStatusChangeNotificationNeeds element.

        Args:
            short_name: The short name for the needs element

        Returns:
            DtcStatusChangeNotificationNeeds: The created or existing needs
                element
        """
        if (not self.IsElementExists(short_name)):
            needs = DtcStatusChangeNotificationNeeds(self, short_name)
            self.addElement(needs)
        return self.getElement(short_name)

    def createDltUserNeeds(self, short_name: str) -> DltUserNeeds:
        """
        Creates or retrieves a DltUserNeeds element.

        Args:
            short_name: The short name for the needs element

        Returns:
            DltUserNeeds: The created or existing needs element
        """
        if (not self.IsElementExists(short_name)):
            needs = DltUserNeeds(self, short_name)
            self.addElement(needs)
        return self.getElement(short_name)

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

    def getDltUserNeeds(self) -> List[DltUserNeeds]:
        """
        Gets sorted DltUserNeeds elements.

        Returns:
            List[DltUserNeeds]: Sorted list of DltUserNeeds
        """
        return sorted(filter(lambda c: isinstance(c, DltUserNeeds), self.elements), key=lambda e: e.short_name)

    def getServiceNeeds(self) -> List[ServiceNeeds]:
        """
        Gets sorted ServiceNeeds elements.

        Returns:
            List[ServiceNeeds]: Sorted list of ServiceNeeds
        """
        return sorted(filter(lambda c: isinstance(c, ServiceNeeds), self.elements), key=lambda e: e.short_name)
