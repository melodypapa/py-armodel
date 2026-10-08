# This module contains AUTOSAR System Template IEEE1722TpAcf classes
# (spec package M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp::IEEE1722TpAcf)

from __future__ import annotations

from typing import List, Optional, cast

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
    IEEE1722TpAcfBusPart,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
    IEEE1722TpAcfCanPart,
    IEEE1722TpAcfLinPart,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable


class IEEE1722TpAcfBus(Identifiable, VariationPointCapable):
    """
    Abstract class to define various busses to be transported over a IEEE1722TP ACF connection. Tags: atp.Status=candidate
    """

    # IEEE1722TpAcfBus method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.291, p.657
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createIEEE1722TpAcfCanPart  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createIEEE1722TpAcfLinPart  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getAcfParts                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getBusId                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setBusId                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # (Abstract; Base = ARObject, Identifiable, MultilanguageReferrable, Referrable; XSD group
    # IEEE-1722-TP-ACF-BUS carries VARIATION-POINT — getVariationPoint/setVariationPoint provided by
    # the VariationPointCapable base (mixin), no spec rows)

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is IEEE1722TpAcfBus:
            raise TypeError("IEEE1722TpAcfBus is an abstract class.")

        super().__init__(parent, short_name)

        # One part transported over IEEE1722Tp channel. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=acfPart.shortName, acfPart.variation Point.shortLabel atp.Status=candidate vh.latestBindingTime=postBuild
        self.acfParts: List[IEEE1722TpAcfBusPart] = []

        # Id of the transported bus over the ACF connection.
        self.busId: Optional[PositiveInteger] = None

    def createIEEE1722TpAcfCanPart(self, short_name: str) -> IEEE1722TpAcfCanPart:
        """
        One part transported over IEEE1722Tp channel. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=acfPart.shortName, acfPart.variation Point.shortLabel atp.Status=candidate vh.latestBindingTime=postBuild
        """
        if not self.IsReferrableElementExists(short_name, IEEE1722TpAcfCanPart):
            part = IEEE1722TpAcfCanPart(self, short_name)
            self.addReferrableElement(part)
            self.acfParts.append(cast(IEEE1722TpAcfBusPart, part))
        return cast(IEEE1722TpAcfCanPart, self.getReferrableElement(short_name, IEEE1722TpAcfCanPart))

    def createIEEE1722TpAcfLinPart(self, short_name: str) -> IEEE1722TpAcfLinPart:
        """
        One part transported over IEEE1722Tp channel. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=acfPart.shortName, acfPart.variation Point.shortLabel atp.Status=candidate vh.latestBindingTime=postBuild
        """
        if not self.IsReferrableElementExists(short_name, IEEE1722TpAcfLinPart):
            part = IEEE1722TpAcfLinPart(self, short_name)
            self.addReferrableElement(part)
            self.acfParts.append(cast(IEEE1722TpAcfBusPart, part))
        return cast(IEEE1722TpAcfLinPart, self.getReferrableElement(short_name, IEEE1722TpAcfLinPart))

    def getAcfParts(self) -> List[IEEE1722TpAcfBusPart]:
        """
        One part transported over IEEE1722Tp channel. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=acfPart.shortName, acfPart.variation Point.shortLabel atp.Status=candidate vh.latestBindingTime=postBuild
        """
        return self.acfParts

    def getBusId(self) -> Optional[PositiveInteger]:
        """
        Id of the transported bus over the ACF connection.
        """
        return self.busId

    def setBusId(self, value: Optional[PositiveInteger]) -> IEEE1722TpAcfBus:
        """
        Id of the transported bus over the ACF connection.
        A None value is a no-op and does not overwrite an existing busId.
        """
        if value is not None:
            self.busId = value
        return self


class IEEE1722TpAcfCan(IEEE1722TpAcfBus):
    pass


class IEEE1722TpAcfLin(IEEE1722TpAcfBus):
    pass
