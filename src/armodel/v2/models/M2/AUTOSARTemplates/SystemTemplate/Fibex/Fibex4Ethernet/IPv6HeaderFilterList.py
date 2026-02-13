"""
AUTOSAR Package - IPv6HeaderFilterList

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::IPv6HeaderFilterList
"""

from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    RefType,
)


class IPv6ExtHeaderFilterSet(ARElement):
    """
    Set of IPv6 Extension Header Filters.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::IPv6HeaderFilterList::IPv6ExtHeaderFilterSet

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 455, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # In order to permit or deny certain types of IPv6 extension a permitted list
        # of IPv6 extension headers can be.
        self._extHeaderFilter: List[RefType] = []

    @property
    def ext_header_filter(self) -> List[RefType]:
        """Get extHeaderFilter (Pythonic accessor)."""
        return self._extHeaderFilter

    def with_ext_header_filter(self, value):
        """
        Set ext_header_filter and return self for chaining.

        Args:
            value: The ext_header_filter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ext_header_filter("value")
        """
        self.ext_header_filter = value  # Use property setter (gets validation)
        return self

    def with_allowed_i_pv6_ext(self, value):
        """
        Set allowed_i_pv6_ext and return self for chaining.

        Args:
            value: The allowed_i_pv6_ext to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_allowed_i_pv6_ext("value")
        """
        self.allowed_i_pv6_ext = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getExtHeaderFilter(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for extHeaderFilter.

        Returns:
            The extHeaderFilter value

        Note:
            Delegates to ext_header_filter property (CODING_RULE_V2_00017)
        """
        return self.ext_header_filter  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



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
        self._allowedIPv6Ext: List[PositiveInteger] = []

    @property
    def allowed_i_pv6_ext(self) -> List[PositiveInteger]:
        """Get allowedIPv6Ext (Pythonic accessor)."""
        return self._allowedIPv6Ext

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAllowedIPv6Ext(self) -> List[PositiveInteger]:
        """
        AUTOSAR-compliant getter for allowedIPv6Ext.

        Returns:
            The allowedIPv6Ext value

        Note:
            Delegates to allowed_i_pv6_ext property (CODING_RULE_V2_00017)
        """
        return self.allowed_i_pv6_ext  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
