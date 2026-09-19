from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
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
