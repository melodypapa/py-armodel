from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import IdentCaption


class BswServiceDependencyIdent(IdentCaption):
    """This meta-class is created to add the ability to become the target of a reference to the non-Referrable BswServiceDependency."""

    # BswServiceDependencyIdent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.16, p.240
# Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


__all__ = ["BswServiceDependencyIdent"]
