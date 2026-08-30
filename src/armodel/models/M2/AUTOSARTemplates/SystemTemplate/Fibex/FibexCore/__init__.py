"""
This module contains the direct members of the FibexCore package.
"""

from abc import ABC

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import PackageableElement


class FibexElement(PackageableElement, ABC):
    """
    ASAM FIBEX elements specifying Communication and Topology.
    """

    # FibexElement method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table F.64, p.2026
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is FibexElement:
            raise TypeError("FibexElement is an abstract class.")

        super().__init__(parent, short_name)
