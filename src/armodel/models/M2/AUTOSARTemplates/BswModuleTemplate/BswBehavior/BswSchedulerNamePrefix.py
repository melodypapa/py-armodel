"""
This module defines BSW scheduler name prefix in AUTOSAR.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation import ImplementationProps
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class BswSchedulerNamePrefix(ImplementationProps):
    """
    A prefix to be used in names of generated code artifacts which make up the
    interface of a BSW module to the BswScheduler.
    """

    # BswSchedulerNamePrefix method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 5.20, p.86
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
