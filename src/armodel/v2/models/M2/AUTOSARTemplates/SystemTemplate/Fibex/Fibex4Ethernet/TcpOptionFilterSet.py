from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class TcpOptionFilterSet(ARElement):
    """
    Set of TcpOptionFilterLists.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::TcpOptionFilterSet::TcpOptionFilterSet

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 457, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Collection of permitted lists for the filtering of TCP options.
        self._tcpOptionFilter: List[RefType] = []

    @property
    def tcp_option_filter(self) -> List[RefType]:
        """Get tcpOptionFilter (Pythonic accessor)."""
        return self._tcpOptionFilter

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTcpOptionFilter(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for tcpOptionFilter.

        Returns:
            The tcpOptionFilter value

        Note:
            Delegates to tcp_option_filter property (CODING_RULE_V2_00017)
        """
        return self.tcp_option_filter  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
