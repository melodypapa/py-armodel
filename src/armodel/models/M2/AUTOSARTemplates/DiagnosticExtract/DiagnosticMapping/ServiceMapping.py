from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import IdentCaption


class BswServiceDependencyIdent(IdentCaption):
    """
    This meta-class is created to add the ability to become the target of a reference
    to the non-Referrable BswServiceDependency.
    """

    # BswServiceDependencyIdent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 5.16, p.240
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the BswServiceDependencyIdent with a parent and short name.

        Args:
            parent: The parent ARObject that contains this ident caption
            short_name: The unique short name of this ident caption
        """
        super().__init__(parent, short_name)


__all__ = ["BswServiceDependencyIdent"]
