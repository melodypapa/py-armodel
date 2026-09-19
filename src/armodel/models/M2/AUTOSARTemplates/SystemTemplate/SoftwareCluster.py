from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import ComponentInSystemInstanceRef


class SwComponentPrototypeAssignment(ARObject, VariationPointCapable):
    """
    This meta-class is only required to allow for the variant modeling of an instanceRef.
    """

    # SwComponentPrototypeAssignment method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 11.2, p.894 (R23-11)
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
