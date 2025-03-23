from typing import List
from .....M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import CryptoServiceNeeds, DiagnosticCommunicationManagerNeeds, DiagnosticEventInfoNeeds
from .....M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import DltUserNeeds
from .....M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import DiagnosticEventNeeds, DiagnosticRoutineNeeds, DiagnosticValueNeeds
from .....M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import DtcStatusChangeNotificationNeeds, EcuStateMgrUserNeeds, NvBlockNeeds
from .....M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import RoleBasedDataAssignment, ServiceNeeds, ServiceDependency
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, RefType


class RoleBasedPortAssignment(ARObject):
    def __init__(self):
        super().__init__()

        self.portPrototypeRef = None            # type: RefType
        self.role = None                        # type: Identifier

    def getPortPrototypeRef(self):
        return self.portPrototypeRef

    def setPortPrototypeRef(self, value):
        self.portPrototypeRef = value
        return self

    def getRole(self):
        return self.role

    def setRole(self, value):
        self.role = value
        return self


class SwcServiceDependency(ServiceDependency):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self._assigned_data = []
        self._assigned_ports = []

    def AddAssignedData(self, data: RoleBasedDataAssignment):
        self._assigned_data.append(data)

    def getAssignedData(self) -> List[RoleBasedDataAssignment]:
        return self._assigned_data

    def AddAssignedPort(self, data: RoleBasedPortAssignment):
        self._assigned_ports.append(data)

    def getAssignedPorts(self) -> List[RoleBasedPortAssignment]:
        return self._assigned_ports

    def createNvBlockNeeds(self, short_name: str) -> NvBlockNeeds:
        if (not self.IsElementExists(short_name)):
            needs = NvBlockNeeds(self, short_name)
            self.addElement(needs)
        return self.getElement(short_name)
    
    def createDiagnosticCommunicationManagerNeeds(self, short_name: str) -> DiagnosticCommunicationManagerNeeds:
        if (not self.IsElementExists(short_name)):
            needs = DiagnosticCommunicationManagerNeeds(self, short_name)
            self.addElement(needs)
        return self.getElement(short_name)
    
    def createDiagnosticRoutineNeeds(self, short_name: str) -> DiagnosticRoutineNeeds:
        if (not self.IsElementExists(short_name)):
            needs = DiagnosticRoutineNeeds(self, short_name)
            self.addElement(needs)
        return self.getElement(short_name)
    
    def createDiagnosticValueNeeds(self, short_name: str) -> DiagnosticValueNeeds:
        if (not self.IsElementExists(short_name)):
            needs = DiagnosticValueNeeds(self, short_name)
            self.addElement(needs)
        return self.getElement(short_name)
    
    def createDiagnosticEventNeeds(self, short_name: str) -> DiagnosticEventNeeds:
        if (not self.IsElementExists(short_name)):
            needs = DiagnosticEventNeeds(self, short_name)
            self.addElement(needs)
        return self.getElement(short_name)
    
    def createDiagnosticEventInfoNeeds(self, short_name: str) -> DiagnosticEventInfoNeeds:
        if (not self.IsElementExists(short_name)):
            needs = DiagnosticEventInfoNeeds(self, short_name)
            self.addElement(needs)
        return self.getElement(short_name)
    
    def createCryptoServiceNeeds(self, short_name: str) -> CryptoServiceNeeds:
        if (not self.IsElementExists(short_name)):
            needs = CryptoServiceNeeds(self, short_name)
            self.addElement(needs)
        return self.getElement(short_name)
    
    def createEcuStateMgrUserNeeds(self, short_name: str) -> EcuStateMgrUserNeeds:
        if (not self.IsElementExists(short_name)):
            needs = EcuStateMgrUserNeeds(self, short_name)
            self.addElement(needs)
        return self.getElement(short_name)
    
    def createDtcStatusChangeNotificationNeeds(self, short_name: str) -> DtcStatusChangeNotificationNeeds:
        if (not self.IsElementExists(short_name)):
            needs = DtcStatusChangeNotificationNeeds(self, short_name)
            self.addElement(needs)
        return self.getElement(short_name)
    
    def createDltUserNeeds(self, short_name: str) -> DltUserNeeds:
        if (not self.IsElementExists(short_name)):
            needs = DltUserNeeds(self, short_name)
            self.addElement(needs)
        return self.getElement(short_name)
    
    def getNvBlockNeeds(self) -> List[NvBlockNeeds]:
        return sorted(filter(lambda c: isinstance(c, NvBlockNeeds), self.elements), key=lambda e: e.short_name)
    
    def getDiagnosticCommunicationManagerNeeds(self) -> List[DiagnosticCommunicationManagerNeeds]:
        return sorted(filter(lambda c: isinstance(c, DiagnosticCommunicationManagerNeeds), self.elements), key=lambda e: e.short_name)
    
    def getDiagnosticRoutineNeeds(self) -> List[DiagnosticRoutineNeeds]:
        return sorted(filter(lambda c: isinstance(c, DiagnosticRoutineNeeds), self.elements), key=lambda e: e.short_name)
    
    def getDiagnosticEventNeeds(self) -> List[DiagnosticEventNeeds]:
        return sorted(filter(lambda c: isinstance(c, DiagnosticEventNeeds), self.elements), key=lambda e: e.short_name)
    
    def getCryptoServiceNeeds(self) -> List[CryptoServiceNeeds]:
        return sorted(filter(lambda c: isinstance(c, CryptoServiceNeeds), self.elements), key=lambda e: e.short_name)
    
    def getEcuStateMgrUserNeeds(self) -> List[EcuStateMgrUserNeeds]:
        return sorted(filter(lambda c: isinstance(c, EcuStateMgrUserNeeds), self.elements), key=lambda e: e.short_name)
    
    def getDtcStatusChangeNotificationNeeds(self) -> List[DtcStatusChangeNotificationNeeds]:
        return sorted(filter(lambda c: isinstance(c, DtcStatusChangeNotificationNeeds), self.elements), key=lambda e: e.short_name)
    
    def getDltUserNeeds(self) -> List[DltUserNeeds]:
        return sorted(filter(lambda c: isinstance(c, DltUserNeeds), self.elements), key=lambda e: e.short_name)

    def getServiceNeeds(self) -> List[ServiceNeeds]:
        return sorted(filter(lambda c: isinstance(c, ServiceNeeds), self.elements), key=lambda e: e.short_name)
