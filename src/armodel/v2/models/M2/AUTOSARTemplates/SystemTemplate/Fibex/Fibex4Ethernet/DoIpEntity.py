from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class DoIpEntity(ARObject):
    """
    ECU providing this infrastructure service is a DoIP-Entity.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 471, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Identifies the role in terms of DoIP this network-node has.
        self._doIpEntityRole: Optional["DoIpEntityRoleEnum"] = None

    @property
    def do_ip_entity_role(self) -> Optional["DoIpEntityRoleEnum"]:
        """Get doIpEntityRole (Pythonic accessor)."""
        return self._doIpEntityRole

    @do_ip_entity_role.setter
    def do_ip_entity_role(self, value: Optional["DoIpEntityRoleEnum"]) -> None:
        """
        Set doIpEntityRole with validation.

        Args:
            value: The doIpEntityRole to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._doIpEntityRole = None
            return

        if not isinstance(value, DoIpEntityRoleEnum):
            raise TypeError(
                f"doIpEntityRole must be DoIpEntityRoleEnum or None, got {type(value).__name__}"
            )
        self._doIpEntityRole = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDoIpEntityRole(self) -> "DoIpEntityRoleEnum":
        """
        AUTOSAR-compliant getter for doIpEntityRole.

        Returns:
            The doIpEntityRole value

        Note:
            Delegates to do_ip_entity_role property (CODING_RULE_V2_00017)
        """
        return self.do_ip_entity_role  # Delegates to property

    def setDoIpEntityRole(self, value: "DoIpEntityRoleEnum") -> "DoIpEntity":
        """
        AUTOSAR-compliant setter for doIpEntityRole with method chaining.

        Args:
            value: The doIpEntityRole to set

        Returns:
            self for method chaining

        Note:
            Delegates to do_ip_entity_role property setter (gets validation automatically)
        """
        self.do_ip_entity_role = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_do_ip_entity_role(self, value: Optional["DoIpEntityRoleEnum"]) -> "DoIpEntity":
        """
        Set doIpEntityRole and return self for chaining.

        Args:
            value: The doIpEntityRole to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_do_ip_entity_role("value")
        """
        self.do_ip_entity_role = value  # Use property setter (gets validation)
        return self
