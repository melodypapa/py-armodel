from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.SecurityExtractTemplate import (
    SecurityEventContextMapping,
)


class SecurityEventContextMappingCommConnector(SecurityEventContextMapping):
    """
    This meta-class represents the ability to associate a collection of security
    events with an IdsM instance and with the executional context related to a
    CommunicationConnector in which this IdsM instance can receive reports for
    these security events.

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 40, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference identifies the respective Communication Connector for which
        # the collection of security events can atpVariation.
        self._comm: List["Communication"] = []

    @property
    def comm(self) -> List["Communication"]:
        """Get comm (Pythonic accessor)."""
        return self._comm

    def with_comm(self, value):
        """
        Set comm and return self for chaining.

        Args:
            value: The comm to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_comm("value")
        """
        self.comm = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getComm(self) -> List["Communication"]:
        """
        AUTOSAR-compliant getter for comm.

        Returns:
            The comm value

        Note:
            Delegates to comm property (CODING_RULE_V2_00017)
        """
        return self.comm  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
