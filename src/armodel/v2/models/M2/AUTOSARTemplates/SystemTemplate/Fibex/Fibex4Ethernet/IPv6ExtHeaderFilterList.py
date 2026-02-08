from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class IPv6ExtHeaderFilterList(Identifiable):
    """
    Permitted list for the filtering of IPv6 extension headers.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::IPv6HeaderFilterList::IPv6ExtHeaderFilterList

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 455, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # IPv6 Extension Header type allowed by this filter.
        self._allowedIPv6Ext: List["PositiveInteger"] = []

    @property
    def allowed_i_pv6_ext(self) -> List["PositiveInteger"]:
        """Get allowedIPv6Ext (Pythonic accessor)."""
        return self._allowedIPv6Ext

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAllowedIPv6Ext(self) -> List["PositiveInteger"]:
        """
        AUTOSAR-compliant getter for allowedIPv6Ext.

        Returns:
            The allowedIPv6Ext value

        Note:
            Delegates to allowed_i_pv6_ext property (CODING_RULE_V2_00017)
        """
        return self.allowed_i_pv6_ext  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
