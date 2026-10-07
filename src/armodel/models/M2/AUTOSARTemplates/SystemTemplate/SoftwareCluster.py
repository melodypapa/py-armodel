from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import ComponentInSystemInstanceRef


class SwComponentPrototypeAssignment(ARObject, VariationPointCapable):
    """
    This meta-class is only required to allow for the variant modeling of an instanceRef.
    """

    # SwComponentPrototypeAssignment method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 11.2, p.894 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getSwComponentIRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwComponentIRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # hierarchical tree(s) of Software Components belonging to this CP Software Cluster. This reference is used to describe the belonging SWCs if the CP Software Cluster is described in the context of a System, InstanceRef implemented by: ComponentInSystemInstanceRef
        self.swComponentIRef: Optional[ComponentInSystemInstanceRef] = None

    def getSwComponentIRef(self) -> Optional[ComponentInSystemInstanceRef]:
        """
        hierarchical tree(s) of Software Components belonging to this CP Software Cluster. This reference is used to describe the belonging SWCs if the CP Software Cluster is described in the context of a System, InstanceRef implemented by: ComponentInSystemInstanceRef
        """
        return self.swComponentIRef

    def setSwComponentIRef(self, value: Optional[ComponentInSystemInstanceRef]) -> "SwComponentPrototypeAssignment":
        """
        hierarchical tree(s) of Software Components belonging to this CP Software Cluster. This reference is used to describe the belonging SWCs if the CP Software Cluster is described in the context of a System, InstanceRef implemented by: ComponentInSystemInstanceRef

        A None value is a no-op and does not overwrite an existing swComponentIRef.
        """
        if value is not None:
            self.swComponentIRef = value
        return self


class CpSoftwareCluster(ARElement):
    """
    This meta class provides the ability to define a CP Software Cluster. Each CP Software Cluster can be integrated and build individually. It defines the sub-set of hierarchical tree(s) of Software Components belonging to this CP Software Cluster. Resources required or provided by this CP Software Cluster are given in the according mappings. Tags: atp.recommendedPackage=CpSoftwareClusters
    """

    # CpSoftwareCluster method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 11.1, p.894 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getSoftwareClusterId         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSoftwareClusterId         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwComponentAssignments    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addSwComponentAssignment     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createSwComponentAssignment  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwCompositionRefs         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addSwCompositionRef          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute represents the value of the id of the corresponding CP software cluster.
        self.softwareClusterId: Optional[PositiveInteger] = None

        # This is the collection of SwComponentPrototypeAssignments
        self.swComponentAssignments: List[SwComponentPrototypeAssignment] = []

        # Software Components in the context of a CompositionSwComponentType belonging to this CP Software Cluster. This reference can be used to describe the belonging SWCs when the CP Software Cluster is described out of the context of a System, e.g. reusable CP Software Cluster.
        self.swCompositionRefs: List[RefType] = []

    def getSoftwareClusterId(self) -> Optional[PositiveInteger]:
        """
        This attribute represents the value of the id of the corresponding CP software cluster.
        """
        return self.softwareClusterId

    def setSoftwareClusterId(self, value: Optional[PositiveInteger]) -> "CpSoftwareCluster":
        """
        This attribute represents the value of the id of the corresponding CP software cluster.

        A None value is a no-op and does not overwrite an existing softwareClusterId.
        """
        if value is not None:
            self.softwareClusterId = value
        return self

    def getSwComponentAssignments(self) -> List[SwComponentPrototypeAssignment]:
        """
        This is the collection of SwComponentPrototypeAssignments
        """
        return self.swComponentAssignments

    def addSwComponentAssignment(self, value: SwComponentPrototypeAssignment) -> "CpSoftwareCluster":
        """
        This is the collection of SwComponentPrototypeAssignments
        """
        self.swComponentAssignments.append(value)
        return self

    def createSwComponentAssignment(self) -> SwComponentPrototypeAssignment:
        """
        This is the collection of SwComponentPrototypeAssignments
        """
        assignment = SwComponentPrototypeAssignment()
        self.swComponentAssignments.append(assignment)
        return assignment

    def getSwCompositionRefs(self) -> List[RefType]:
        """
        Software Components in the context of a CompositionSwComponentType belonging to this CP Software Cluster. This reference can be used to describe the belonging SWCs when the CP Software Cluster is described out of the context of a System, e.g. reusable CP Software Cluster.
        """
        return self.swCompositionRefs

    def addSwCompositionRef(self, value: Optional[RefType]) -> "CpSoftwareCluster":
        """
        Software Components in the context of a CompositionSwComponentType belonging to this CP Software Cluster. This reference can be used to describe the belonging SWCs when the CP Software Cluster is described out of the context of a System, e.g. reusable CP Software Cluster.

        A None value is a no-op and does not add to swCompositionRefs.
        """
        if value is not None:
            self.swCompositionRefs.append(value)
        return self


class CpSoftwareClusterToEcuInstanceMapping(Identifiable):
    """
    This meta class maps a CpSoftwareCluster to a EcuInstance.
    """

    # CpSoftwareClusterToEcuInstanceMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.47, p.283
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getEcuInstanceRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setEcuInstanceRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMachineId       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMachineId       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwClusterRefs   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addSwClusterRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Reference to a specific ECU Instance description.
        self.ecuInstanceRef: Optional[RefType] = None

        # Unique number of the (virtual or physical) machine to which the Software Cluster is mapped.
        self.machineId: Optional[PositiveInteger] = None

        # The mapped CP Software Cluster Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=swCluster.cpSoftwareCluster, sw Cluster.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime
        self.swClusterRefs: List[RefType] = []

    def getEcuInstanceRef(self) -> Optional[RefType]:
        """
        Reference to a specific ECU Instance description.
        """
        return self.ecuInstanceRef

    def setEcuInstanceRef(self, value: Optional[RefType]) -> "CpSoftwareClusterToEcuInstanceMapping":
        """
        Reference to a specific ECU Instance description.

        A None value is a no-op and does not overwrite an existing ecuInstanceRef.
        """
        if value is not None:
            self.ecuInstanceRef = value
        return self

    def getMachineId(self) -> Optional[PositiveInteger]:
        """
        Unique number of the (virtual or physical) machine to which the Software Cluster is mapped.
        """
        return self.machineId

    def setMachineId(self, value: Optional[PositiveInteger]) -> "CpSoftwareClusterToEcuInstanceMapping":
        """
        Unique number of the (virtual or physical) machine to which the Software Cluster is mapped.

        A None value is a no-op and does not overwrite an existing machineId.
        """
        if value is not None:
            self.machineId = value
        return self

    def getSwClusterRefs(self) -> List[RefType]:
        """
        The mapped CP Software Cluster Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=swCluster.cpSoftwareCluster, sw Cluster.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime
        """
        return self.swClusterRefs

    def addSwClusterRef(self, value: Optional[RefType]) -> "CpSoftwareClusterToEcuInstanceMapping":
        """
        The mapped CP Software Cluster Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=swCluster.cpSoftwareCluster, sw Cluster.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime

        A None value is a no-op and does not add to swClusterRefs.
        """
        if value is not None:
            self.swClusterRefs.append(value)
        return self


class CpSoftwareClusterResourceToApplicationPartitionMapping(Identifiable):
    """
    This meta class maps a Software Cluster resource to an Application Partition to restrict the usage.
    """

    # CpSoftwareClusterResourceToApplicationPartitionMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.48, p.284
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getApplicationPartitionRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setApplicationPartitionRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getResourceRef               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setResourceRef               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # ApplicationPartition for which the mapping applies.
        self.applicationPartitionRef: Optional[RefType] = None

        # Software Cluster Resource for which the mapping applies.
        self.resourceRef: Optional[RefType] = None

    def getApplicationPartitionRef(self) -> Optional[RefType]:
        """
        ApplicationPartition for which the mapping applies.
        """
        return self.applicationPartitionRef

    def setApplicationPartitionRef(self, value: Optional[RefType]) -> "CpSoftwareClusterResourceToApplicationPartitionMapping":
        """
        ApplicationPartition for which the mapping applies.

        A None value is a no-op and does not overwrite an existing applicationPartitionRef.
        """
        if value is not None:
            self.applicationPartitionRef = value
        return self

    def getResourceRef(self) -> Optional[RefType]:
        """
        Software Cluster Resource for which the mapping applies.
        """
        return self.resourceRef

    def setResourceRef(self, value: Optional[RefType]) -> "CpSoftwareClusterResourceToApplicationPartitionMapping":
        """
        Software Cluster Resource for which the mapping applies.

        A None value is a no-op and does not overwrite an existing resourceRef.
        """
        if value is not None:
            self.resourceRef = value
        return self


class CpSoftwareClusterToApplicationPartitionMapping(Identifiable):
    """
    This meta class defines ApplicationPartitions that are applicable for the CpSoftwareCluster.
    """

    # CpSoftwareClusterToApplicationPartitionMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.50, p.287
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getApplicationPartitionRefs     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addApplicationPartitionRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSoftwareClusterRef           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSoftwareClusterRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Collection of ApplicationPartitions available in the Cp SoftwareCluster
        self.applicationPartitionRefs: List[RefType] = []

        # Software Cluster Resource for which the mapping applies
        self.softwareClusterRef: Optional[RefType] = None

    def getApplicationPartitionRefs(self) -> List[RefType]:
        """
        Collection of ApplicationPartitions available in the Cp SoftwareCluster
        """
        return self.applicationPartitionRefs

    def addApplicationPartitionRef(self, value: Optional[RefType]) -> "CpSoftwareClusterToApplicationPartitionMapping":
        """
        Collection of ApplicationPartitions available in the Cp SoftwareCluster

        A None value is a no-op and does not add to applicationPartitionRefs.
        """
        if value is not None:
            self.applicationPartitionRefs.append(value)
        return self

    def getSoftwareClusterRef(self) -> Optional[RefType]:
        """
        Software Cluster Resource for which the mapping applies
        """
        return self.softwareClusterRef

    def setSoftwareClusterRef(self, value: Optional[RefType]) -> "CpSoftwareClusterToApplicationPartitionMapping":
        """
        Software Cluster Resource for which the mapping applies

        A None value is a no-op and does not overwrite an existing softwareClusterRef.
        """
        if value is not None:
            self.softwareClusterRef = value
        return self
