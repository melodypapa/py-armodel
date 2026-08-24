"""
This module defines BSW interrupt event in AUTOSAR.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswEvent


class BswInterruptEvent(BswEvent):
    """
    This meta-class represents an event triggered by an interrupt.
    """

    # BswInterruptEvent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 5.24, p.88
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
