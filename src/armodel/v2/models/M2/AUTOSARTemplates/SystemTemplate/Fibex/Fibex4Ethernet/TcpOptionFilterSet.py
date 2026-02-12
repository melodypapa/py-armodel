"""
AUTOSAR Package - TcpOptionFilterSet

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::TcpOptionFilterSet
"""

from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
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
        self._tcpOptionFilter: List["RefType"] = []

    @property
    def tcp_option_filter(self) -> List["RefType"]:
        """Get tcpOptionFilter (Pythonic accessor)."""
        return self._tcpOptionFilter

    def with_tcp_option_filter(self, value):
        """
        Set tcp_option_filter and return self for chaining.

        Args:
            value: The tcp_option_filter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_option_filter("value")
        """
        self.tcp_option_filter = value  # Use property setter (gets validation)
        return self

    def with_allowed_tcp_option(self, value):
        """
        Set allowed_tcp_option and return self for chaining.

        Args:
            value: The allowed_tcp_option to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_allowed_tcp_option("value")
        """
        self.allowed_tcp_option = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTcpOptionFilter(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for tcpOptionFilter.

        Returns:
            The tcpOptionFilter value

        Note:
            Delegates to tcp_option_filter property (CODING_RULE_V2_00017)
        """
        return self.tcp_option_filter  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class TcpOptionFilterList(Identifiable):
    """
    Permitted list for the filtering of TCP options.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::TcpOptionFilterSet::TcpOptionFilterList

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 457, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # TCP option kind allowed by this filter.
        self._allowedTcpOption: List["PositiveInteger"] = []

    @property
    def allowed_tcp_option(self) -> List["PositiveInteger"]:
        """Get allowedTcpOption (Pythonic accessor)."""
        return self._allowedTcpOption

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAllowedTcpOption(self) -> List["PositiveInteger"]:
        """
        AUTOSAR-compliant getter for allowedTcpOption.

        Returns:
            The allowedTcpOption value

        Note:
            Delegates to allowed_tcp_option property (CODING_RULE_V2_00017)
        """
        return self.allowed_tcp_option  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
