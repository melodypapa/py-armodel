# This module contains the IPv6HeaderFilterList package classes for Fibex4Ethernet
# (M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::IPv6HeaderFilterList).

from __future__ import annotations

from typing import List, cast

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger


class IPv6ExtHeaderFilterList(Identifiable):
    """
    Permitted list for the filtering of IPv6 extension headers.
    """

    # IPv6ExtHeaderFilterList method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.121, p.456
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addAllowedIPv6ExtHeader   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getAllowedIPv6ExtHeaders  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # IPv6 Extension Header type allowed by this filter.
        self.allowedIPv6ExtHeaders: List[PositiveInteger] = []

    def addAllowedIPv6ExtHeader(self, value: PositiveInteger) -> IPv6ExtHeaderFilterList:
        """
        IPv6 Extension Header type allowed by this filter.
        A None value is a no-op and does not extend allowedIPv6ExtHeaders.
        """
        if value is not None:
            self.allowedIPv6ExtHeaders.append(value)
        return self

    def getAllowedIPv6ExtHeaders(self) -> List[PositiveInteger]:
        """IPv6 Extension Header type allowed by this filter."""
        return self.allowedIPv6ExtHeaders


class IPv6ExtHeaderFilterSet(ARElement):
    """
    Set of IPv6 Extension Header Filters. Tags: atp.recommendedPackage=IPv6ExtHeaderFilterSets
    """

    # IPv6ExtHeaderFilterSet method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.120, p.455
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createExtHeaderFilterList     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getExtHeaderFilterLists       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # In order to permit or deny certain types of IPv6 extension headers a permitted list of IPv6 extension headers can be configured.
        self.extHeaderFilterLists: List[IPv6ExtHeaderFilterList] = []

    def createExtHeaderFilterList(self, short_name: str) -> IPv6ExtHeaderFilterList:
        """
        In order to permit or deny certain types of IPv6 extension headers a permitted list of IPv6 extension headers can be configured.
        Creates and appends a new IPv6ExtHeaderFilterList; an existing list with the same
        short name is returned unchanged.
        """
        if not self.IsReferrableElementExists(short_name, IPv6ExtHeaderFilterList):
            filter_list = IPv6ExtHeaderFilterList(self, short_name)
            self.addReferrableElement(filter_list)
            self.extHeaderFilterLists.append(filter_list)
        return cast(IPv6ExtHeaderFilterList, self.getReferrableElement(short_name, IPv6ExtHeaderFilterList))

    def getExtHeaderFilterLists(self) -> List[IPv6ExtHeaderFilterList]:
        """In order to permit or deny certain types of IPv6 extension headers a permitted list of IPv6 extension headers can be configured."""
        return self.extHeaderFilterLists
