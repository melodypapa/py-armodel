from typing import List
from .....M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import NvBlockNeeds, RoleBasedDataAssignment, ServiceNeeds


from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import ServiceDependency
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
        if (short_name not in self.elements):
            event = NvBlockNeeds(self, short_name)
            self.elements[short_name] = event
        return self.elements[short_name]

    def getNvBlockNeeds(self) -> List[NvBlockNeeds]:
        return sorted(filter(lambda c: isinstance(c, NvBlockNeeds), self.elements.values()), key=lambda e: e.short_name)

    def getServiceNeeds(self) -> List[ServiceNeeds]:
        return sorted(filter(lambda c: isinstance(c, ServiceNeeds), self.elements.values()), key=lambda e: e.short_name)
