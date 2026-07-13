# This module contains AUTOSAR System Template classes for software component mapping
# It defines mappings between software components and their implementations or partitions

from typing import List
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import ComponentInSystemInstanceRef


class SwcToImplMapping(Identifiable):
    """
    Represents a mapping between software components and their implementations,
    defining how software component instances in the system are connected to
    their specific implementation references and instance references.
    """
    # SwcToImplMapping method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getComponentIRefs            [x] impl  [ ] docstring  [ ] test
    # [ ] addComponentIRef             [x] impl  [ ] docstring  [ ] test
    # [ ] getComponentImplementationRef [x] impl  [ ] docstring  [ ] test
    # [ ] setComponentImplementationRef [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.componentIRefs: List[ComponentInSystemInstanceRef] = []
        self.componentImplementationRef: RefType = None

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
    # ApplicationPartitionToEcuPartitionMapping method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getApplicationPartitionRefs  [x] impl  [ ] docstring  [ ] test
    # [ ] addApplicationPartitionRef   [x] impl  [ ] docstring  [ ] test
    # [ ] getEcuPartitionRef           [x] impl  [ ] docstring  [ ] test
    # [ ] setEcuPartitionRef           [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.applicationPartitionRefs: List[RefType] = []
        self.ecuPartitionRef: RefType = None

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
