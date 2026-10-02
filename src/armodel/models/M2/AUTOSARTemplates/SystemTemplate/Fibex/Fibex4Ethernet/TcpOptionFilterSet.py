# This module contains the TcpOptionFilterSet package classes for Fibex4Ethernet
# (M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::TcpOptionFilterSet).

from typing import List

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger


class TcpOptionFilterList(Identifiable):
    """
    Permitted list for the filtering of TCP options.
    """

    # TcpOptionFilterList method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.123, p.457 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAllowedTcpOptions   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addAllowedTcpOption    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # (serialized as TCP-OPTION-FILTER-LIST within TcpOptionFilterSet; prior R4.3.1 sync Table 6.131 p.326 upgraded per Rule 0016.3)

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # TCP option kind allowed by this filter.
        self.allowedTcpOptions: List[PositiveInteger] = []

    def getAllowedTcpOptions(self) -> List[PositiveInteger]:
        """TCP option kind allowed by this filter."""
        return self.allowedTcpOptions

    def addAllowedTcpOption(self, value: PositiveInteger) -> "TcpOptionFilterList":
        """
        TCP option kind allowed by this filter.
        A None value is a no-op and does not extend allowedTcpOptions.
        """
        if value is not None:
            self.allowedTcpOptions.append(value)
        return self


class TcpOptionFilterSet(ARElement):
    """
    Set of TcpOptionFilterLists. Tags: atp.recommendedPackage=TcpOptionFilterSets
    """

    # TcpOptionFilterSet method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.122, p.457 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createTcpOptionFilterList  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTcpOptionFilterLists    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Collection of permitted lists for the filtering of TCP options.
        self.tcpOptionFilterLists: List[TcpOptionFilterList] = []

    def createTcpOptionFilterList(self, short_name: str) -> TcpOptionFilterList:
        """
        Collection of permitted lists for the filtering of TCP options.
        Creates and appends a new TcpOptionFilterList; an existing list with the same
        short name is returned unchanged.
        """
        if not self.IsReferrableElementExists(short_name, TcpOptionFilterList):
            tcp_filter_list = TcpOptionFilterList(self, short_name)
            self.addReferrableElement(tcp_filter_list)
            self.tcpOptionFilterLists.append(tcp_filter_list)
        return self.getReferrableElement(short_name, TcpOptionFilterList)

    def getTcpOptionFilterLists(self) -> List[TcpOptionFilterList]:
        """Collection of permitted lists for the filtering of TCP options."""
        return self.tcpOptionFilterLists
