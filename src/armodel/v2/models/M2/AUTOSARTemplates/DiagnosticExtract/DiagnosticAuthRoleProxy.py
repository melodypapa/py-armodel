from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class DiagnosticAuthRoleProxy(ARObject):
    """
    This meta-class indicates that an authentication is generally foreseen. The
    question whether the authentication is done in general or whether it is done
    role-specific depends on the existence of references to DiagAuthRole.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 76, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference identifies the authenticationRole applicable the enclosing
        # DiagnosticAccessPermission.
        self._authentication: List["DiagnosticAuthRole"] = []

    @property
    def authentication(self) -> List["DiagnosticAuthRole"]:
        """Get authentication (Pythonic accessor)."""
        return self._authentication

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAuthentication(self) -> List["DiagnosticAuthRole"]:
        """
        AUTOSAR-compliant getter for authentication.

        Returns:
            The authentication value

        Note:
            Delegates to authentication property (CODING_RULE_V2_00017)
        """
        return self.authentication  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
