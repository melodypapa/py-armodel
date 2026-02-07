# This module contains AUTOSAR System Template classes for software component mapping
# It defines mappings between software components and their implementations or partitions

from typing import List, Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import (
    ComponentInSystemInstanceRef,
)


class SwcToEcuMapping(Identifiable):
    """
    Represents the mapping between software components and ECU instances
    in the system, defining how components are assigned to specific
    ECUs including hardware element and processing unit references.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.componentIRefs: List[ComponentInSystemInstanceRef] = []
        self.controlledHwElementRef: Union[Union[RefType, None] , None] = None
        self.ecuInstanceRef: Union[Union[RefType, None] , None] = None
        self.processingUnitRef: Union[Union[RefType, None] , None] = None

    def getComponentIRefs(self):
        return self.componentIRefs

    def addComponentIRef(self, value):
        self.componentIRefs.append(value)
        return self

    def getControlledHwElementRef(self):
        return self.controlledHwElementRef

    def setControlledHwElementRef(self, value):
        self.controlledHwElementRef = value
        return self

    def getEcuInstanceRef(self):
        return self.ecuInstanceRef

    def setEcuInstanceRef(self, value):
        self.ecuInstanceRef = value
        return self

    def getProcessingUnitRef(self):
        return self.processingUnitRef

    def setProcessingUnitRef(self, value):
        self.processingUnitRef = value
        return self



class SwcToImplMapping(Identifiable):
    """
    Represents a mapping between software components and their implementations,
    defining how software component instances in the system are connected to
    their specific implementation references and instance references.
    """
    def __init__(self, parent, short_name) -> None:
        super().__init__(parent, short_name)

        self.componentIRefs: List[ComponentInSystemInstanceRef] = []
        self.componentImplementationRef: Union[Union[RefType, None] , None] = None

    def getComponentIRefs(self):
        return self.componentIRefs

    def addComponentIRef(self, value):
        if value is not None:
            self.componentIRefs.append(value)
        return self

    def getComponentImplementationRef(self):
        return self.componentImplementationRef

    def setComponentImplementationRef(self, value):
        if value is not None:
            self.componentImplementationRef = value
        return self


class ApplicationPartitionToEcuPartitionMapping(Identifiable):
    """
    Represents a mapping between application partitions and ECU partitions,
    defining how application-level partitions are mapped to ECU-level
    partitions for resource allocation and execution management.
    """
    def __init__(self, parent, short_name) -> None:
        super().__init__(parent, short_name)

        self.applicationPartitionRefs: List[RefType] = []
        self.ecuPartitionRef: Union[Union[RefType, None] , None] = None

    def getApplicationPartitionRefs(self):
        return self.applicationPartitionRefs

    def addApplicationPartitionRef(self, value):
        if value is not None:
            self.applicationPartitionRefs.append(value)
        return self

    def getEcuPartitionRef(self):
        return self.ecuPartitionRef

    def setEcuPartitionRef(self, value):
        if value is not None:
            self.ecuPartitionRef = value
        return self
