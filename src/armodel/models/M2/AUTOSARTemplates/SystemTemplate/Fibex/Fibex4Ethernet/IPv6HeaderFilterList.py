# This module contains the IPv6HeaderFilterList package classes for Fibex4Ethernet
# (M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::IPv6HeaderFilterList).

from typing import List

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger


class IPv6ExtHeaderFilterList(Identifiable):
    """
    White list for the filtering of IPv6 extension headers.
    """

    # IPv6ExtHeaderFilterList method parity checklist:
    # Spec: AUTOSAR_TPS_SystemTemplate.pdf (R4.3.1), Table 6.129, p.325
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R4.3.1
    # [x] getAllowedIPv6ExtHeaders  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R4.3.1
    # [x] addAllowedIPv6ExtHeader   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R4.3.1
    # (reader/writer N/A: consumed as ref target on SocketConnection.allowedIPv6ExtHeaders)

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # IPv6 Extension Header type allowed by this filter.
        self.allowedIPv6ExtHeaders: List[PositiveInteger] = []

    def getAllowedIPv6ExtHeaders(self) -> List[PositiveInteger]:
        """IPv6 Extension Header type allowed by this filter."""
        return self.allowedIPv6ExtHeaders

    def addAllowedIPv6ExtHeader(self, value: PositiveInteger) -> "IPv6ExtHeaderFilterList":
        """
        IPv6 Extension Header type allowed by this filter.
        A None value is a no-op and does not extend allowedIPv6ExtHeaders.
        """
        if value is not None:
            self.allowedIPv6ExtHeaders.append(value)
        return self
