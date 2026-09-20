# This module contains AUTOSAR System Template classes for software component mapping
# It defines mappings between software components and their implementations or partitions

from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import ComponentInSystemInstanceRef


class SwcToImplMapping(Identifiable, VariationPointCapable):
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


class ApplicationPartitionToEcuPartitionMapping(Identifiable, VariationPointCapable):
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


class EcuPartition(Identifiable):
    """
    Partitions are used as error containment regions. They permit the grouping of SWCs and resources and allow to describe recovery policies individually for each partition. Partitions can be terminated or restarted during run-time as a result of a detected error.
    """

    # EcuPartition method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.7, p.201 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getExecInUserMode  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setExecInUserMode  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # A partition can execute either in CPU user mode (execInUserMode = TRUE) or supervisor mode (execInUserMode = FALSE). In user mode, the partition has a limited access to memory, to memory mapped hardware and to CPU. In user mode, the partition is mapped to a non-trusted OS-Application.
        self.execInUserMode: Optional[Boolean] = None

    def getExecInUserMode(self) -> Optional[Boolean]:
        """
        A partition can execute either in CPU user mode (execInUserMode = TRUE) or supervisor mode (execInUserMode = FALSE). In user mode, the partition has a limited access to memory, to memory mapped hardware and to CPU. In user mode, the partition is mapped to a non-trusted OS-Application.
        """
        return self.execInUserMode

    def setExecInUserMode(self, value: Optional[Boolean]) -> "EcuPartition":
        """
        A partition can execute either in CPU user mode (execInUserMode = TRUE) or supervisor mode (execInUserMode = FALSE). In user mode, the partition has a limited access to memory, to memory mapped hardware and to CPU. In user mode, the partition is mapped to a non-trusted OS-Application.

        A None value is a no-op and does not overwrite an existing execInUserMode.
        """
        if value is not None:
            self.execInUserMode = value
        return self
