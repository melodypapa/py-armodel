# This module contains AUTOSAR System Template IEEE1722Tp transport protocol classes
# (spec package M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp)

from __future__ import annotations

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import TpConfig


class IEEE1722TpConfig(TpConfig):
    """
    Definition of the IEEE1722Tp protocol.
    """

    # IEEE1722TpConfig method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.274, p.637
    # Note: class Note taken from XSD IEEE-1722-TP-CONFIG group documentation (PDF table has no Note row)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addTpConnectionRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTpConnectionRefs  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # (Base row absent from the table; XSD complexType IEEE-1722-TP-CONFIG groups FIBEX-ELEMENT + TP-CONFIG -> TpConfig)

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Collection of IEEE1722Tp connections. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpConnection.ieeE1722TpConnection, tp Connection.variationPoint.shortLabel atp.Status=candidate vh.latestBindingTime=postBuild
        self.tpConnectionRefs: List[RefType] = []

    def addTpConnectionRef(self, value: Optional[RefType]) -> IEEE1722TpConfig:
        """
        Collection of IEEE1722Tp connections. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpConnection.ieeE1722TpConnection, tp Connection.variationPoint.shortLabel atp.Status=candidate vh.latestBindingTime=postBuild
        A None value is a no-op and is not appended to tpConnectionRefs.
        """
        if value is not None:
            self.tpConnectionRefs.append(value)
        return self

    def getTpConnectionRefs(self) -> List[RefType]:
        """
        Collection of IEEE1722Tp connections. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=tpConnection.ieeE1722TpConnection, tp Connection.variationPoint.shortLabel atp.Status=candidate vh.latestBindingTime=postBuild
        """
        return self.tpConnectionRefs
