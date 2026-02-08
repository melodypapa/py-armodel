from abc import ABC
from typing import List, Optional


class DiagnosticCapabilityElement(ServiceNeeds, ABC):
    """
    that with the implementation of a generic tracing concept in AUTOSAR this
    attribute might become obsolete. (cid:53) 236 of 381 Document ID 89:
    AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Basic Software Module
    Description Template AUTOSAR CP R23-11 (cid:52)

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DiagnosticCapabilityElement

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 236, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 753, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is DiagnosticCapabilityElement:
            raise TypeError("DiagnosticCapabilityElement is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This specifies the intended audience for the diagnostic Note that this is not
        # only for the documentation but audience specific implementation.
        self._audience: List["DiagnosticAudience"] = []

    @property
    def audience(self) -> List["DiagnosticAudience"]:
        """Get audience (Pythonic accessor)."""
        return self._audience
        # This denotes the requirement identifier to which the object can be linked to.
        self._diag: Optional["DiagRequirementId"] = None

    @property
    def diag(self) -> Optional["DiagRequirementId"]:
        """Get diag (Pythonic accessor)."""
        return self._diag

    @diag.setter
    def diag(self, value: Optional["DiagRequirementId"]) -> None:
        """
        Set diag with validation.

        Args:
            value: The diag to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._diag = None
            return

        if not isinstance(value, DiagRequirementId):
            raise TypeError(
                f"diag must be DiagRequirementId or None, got {type(value).__name__}"
            )
        self._diag = value
        # This attribute denotes the level of security which is by the diagnostic
                # object.
        # The higher the level the for the security exists.
        # shall be mapped to the security level in the.
        self._securityAccess: Optional["PositiveInteger"] = None

    @property
    def security_access(self) -> Optional["PositiveInteger"]:
        """Get securityAccess (Pythonic accessor)."""
        return self._securityAccess

    @security_access.setter
    def security_access(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set securityAccess with validation.

        Args:
            value: The securityAccess to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._securityAccess = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"securityAccess must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._securityAccess = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAudience(self) -> List["DiagnosticAudience"]:
        """
        AUTOSAR-compliant getter for audience.

        Returns:
            The audience value

        Note:
            Delegates to audience property (CODING_RULE_V2_00017)
        """
        return self.audience  # Delegates to property

    def getDiag(self) -> "DiagRequirementId":
        """
        AUTOSAR-compliant getter for diag.

        Returns:
            The diag value

        Note:
            Delegates to diag property (CODING_RULE_V2_00017)
        """
        return self.diag  # Delegates to property

    def setDiag(self, value: "DiagRequirementId") -> "DiagnosticCapabilityElement":
        """
        AUTOSAR-compliant setter for diag with method chaining.

        Args:
            value: The diag to set

        Returns:
            self for method chaining

        Note:
            Delegates to diag property setter (gets validation automatically)
        """
        self.diag = value  # Delegates to property setter
        return self

    def getSecurityAccess(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for securityAccess.

        Returns:
            The securityAccess value

        Note:
            Delegates to security_access property (CODING_RULE_V2_00017)
        """
        return self.security_access  # Delegates to property

    def setSecurityAccess(self, value: "PositiveInteger") -> "DiagnosticCapabilityElement":
        """
        AUTOSAR-compliant setter for securityAccess with method chaining.

        Args:
            value: The securityAccess to set

        Returns:
            self for method chaining

        Note:
            Delegates to security_access property setter (gets validation automatically)
        """
        self.security_access = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_diag(self, value: Optional["DiagRequirementId"]) -> "DiagnosticCapabilityElement":
        """
        Set diag and return self for chaining.

        Args:
            value: The diag to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_diag("value")
        """
        self.diag = value  # Use property setter (gets validation)
        return self

    def with_security_access(self, value: Optional["PositiveInteger"]) -> "DiagnosticCapabilityElement":
        """
        Set securityAccess and return self for chaining.

        Args:
            value: The securityAccess to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_security_access("value")
        """
        self.security_access = value  # Use property setter (gets validation)
        return self
