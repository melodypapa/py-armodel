from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class DiagnosticAuthRoleProxy(ARObject):
    """This meta-class indicates that an authentication is generally foreseen. The question whether the authentication is done in general or whether it is done role-specific depends on the existence of references to DiagAuthRole."""

    # DiagnosticAuthRoleProxy method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.33, p.76
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11  (writer emits the DIAGNOSTIC-AUTH-ROLE-PROXY tag; reader construction via DiagnosticAccessPermission)
    # [x] getAuthenticationRoleRefs    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addAuthenticationRoleRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This reference identifies the authenticationRole applicable for the enclosing DiagnosticAccessPermission.
        self.authenticationRoleRefs: List[RefType] = []

    def getAuthenticationRoleRefs(self) -> List[RefType]:
        """
        This reference identifies the authenticationRole applicable for the enclosing DiagnosticAccessPermission.
        """
        return self.authenticationRoleRefs

    def addAuthenticationRoleRef(self, ref: Optional[RefType]):
        """
        This reference identifies the authenticationRole applicable for the enclosing DiagnosticAccessPermission.

        A None value is a no-op and does not extend the authenticationRoleRefs list.
        """
        if ref is not None:
            self.authenticationRoleRefs.append(ref)
        return self
