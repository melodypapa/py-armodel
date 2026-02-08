from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import UriString
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    ARElement,
)


class AclRole(ARElement):
    """
    This meta class represents the ability to specify a particular role which is
    used to grant access rights to AUTOSAR model. The purpose of this meta-class
    is to support the mutual agreements between the involved parties.

    Package: M2::AUTOSARTemplates::GenericStructure::RolesAndRights::AclRole

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 384, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 159, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is an URL which allows to represent users or the particular role.
        self._ldapUrl: Optional["UriString"] = None

    @property
    def ldap_url(self) -> Optional["UriString"]:
        """Get ldapUrl (Pythonic accessor)."""
        return self._ldapUrl

    @ldap_url.setter
    def ldap_url(self, value: Optional["UriString"]) -> None:
        """
        Set ldapUrl with validation.

        Args:
            value: The ldapUrl to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ldapUrl = None
            return

        if not isinstance(value, UriString):
            raise TypeError(
                f"ldapUrl must be UriString or None, got {type(value).__name__}"
            )
        self._ldapUrl = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getLdapUrl(self) -> "UriString":
        """
        AUTOSAR-compliant getter for ldapUrl.

        Returns:
            The ldapUrl value

        Note:
            Delegates to ldap_url property (CODING_RULE_V2_00017)
        """
        return self.ldap_url  # Delegates to property

    def setLdapUrl(self, value: "UriString") -> "AclRole":
        """
        AUTOSAR-compliant setter for ldapUrl with method chaining.

        Args:
            value: The ldapUrl to set

        Returns:
            self for method chaining

        Note:
            Delegates to ldap_url property setter (gets validation automatically)
        """
        self.ldap_url = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ldap_url(self, value: Optional["UriString"]) -> "AclRole":
        """
        Set ldapUrl and return self for chaining.

        Args:
            value: The ldapUrl to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ldap_url("value")
        """
        self.ldap_url = value  # Use property setter (gets validation)
        return self
