# This module contains AUTOSAR System Template IEEE1722TpAcf classes
# (spec package M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp::IEEE1722TpAcf)

from __future__ import annotations

from typing import List, Optional, cast

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, PositiveInteger
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable


class IEEE1722TpAcfCanMessageTypeEnum(AREnum):
    """
    Definition of the ACF CAN stream message type. Tags: atp.Status=candidate
    """

    # IEEE1722TpAcfCanMessageTypeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.295, p.662
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — serialized as value form on IEEE1722TpAcfCan.messageType
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # Defines the ACF CAN stream to use the ACF_CAN message type. Tags: atp.EnumerationLiteralIndex=0
    ENUM_CAN = "CAN"

    # Defines the ACF CAN stream to use the ACF_CAN_BRIEF message type. Tags: atp.EnumerationLiteralIndex=1
    ENUM_CAN_BRIEF = "CAN-BRIEF"

    def __init__(self):
        super().__init__(
            [
                IEEE1722TpAcfCanMessageTypeEnum.ENUM_CAN,
                IEEE1722TpAcfCanMessageTypeEnum.ENUM_CAN_BRIEF,
            ]
        )


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
            self.acfParts.append(part)
        return cast(IEEE1722TpAcfCanPart, self.getReferrableElement(short_name, IEEE1722TpAcfCanPart))

    def createIEEE1722TpAcfLinPart(self, short_name: str) -> IEEE1722TpAcfLinPart:
        """
        One part transported over IEEE1722Tp channel. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=acfPart.shortName, acfPart.variation Point.shortLabel atp.Status=candidate vh.latestBindingTime=postBuild
        """
        if not self.IsReferrableElementExists(short_name, IEEE1722TpAcfLinPart):
            part = IEEE1722TpAcfLinPart(self, short_name)
            self.addReferrableElement(part)
            self.acfParts.append(part)
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


class IEEE1722TpAcfBusPart(Identifiable, VariationPointCapable):
    """
    Definition of one IEEE1722Tp ACF part transported over the IEEE1722Tp channel. Tags: atp.Status=candidate
    """

    # IEEE1722TpAcfBusPart method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.292, p.658
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCollectionTrigger  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCollectionTrigger  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # (Abstract; Base = ARObject, Identifiable, MultilanguageReferrable, Referrable; XSD group
    # IEEE-1722-TP-ACF-BUS-PART carries VARIATION-POINT — getVariationPoint/setVariationPoint provided
    # by the VariationPointCapable base (mixin), no spec rows)

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is IEEE1722TpAcfBusPart:
            raise TypeError("IEEE1722TpAcfBusPart is an abstract class.")

        super().__init__(parent, short_name)

        # Defines whether putting this AcfPart to the IEEE1722Tp ACF message triggers immediate sending of the IEEE1722Tp ACF message.
        self.collectionTrigger: Optional[PduCollectionTriggerEnum] = None

    def getCollectionTrigger(self) -> Optional[PduCollectionTriggerEnum]:
        """
        Defines whether putting this AcfPart to the IEEE1722Tp ACF message triggers immediate sending of the IEEE1722Tp ACF message.
        """
        return self.collectionTrigger

    def setCollectionTrigger(self, value: Optional[PduCollectionTriggerEnum]) -> IEEE1722TpAcfBusPart:
        """
        Defines whether putting this AcfPart to the IEEE1722Tp ACF message triggers immediate sending of the IEEE1722Tp ACF message.
        A None value is a no-op and does not overwrite an existing collectionTrigger.
        """
        if value is not None:
            self.collectionTrigger = value
        return self


class IEEE1722TpAcfCanPart(IEEE1722TpAcfBusPart):
    pass


class IEEE1722TpAcfLinPart(IEEE1722TpAcfBusPart):
    pass


class IEEE1722TpAcfCan(IEEE1722TpAcfBus):
    """
    ACF IEEE1722Tp bus used for CAN transport. Tags: atp.Status=candidate atp.recommendedPackage=IEEE1722TpConnections
    """

    # IEEE1722TpAcfCan method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.293, p.661
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getMessageType  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMessageType  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # (Base = ARObject, IEEE1722TpAcfBus, Identifiable, MultilanguageReferrable, Referrable — most-derived
    # base IEEE1722TpAcfBus; concrete (XSD abstract="false"); XSD group IEEE-1722-TP-ACF-BUS carries
    # VARIATION-POINT — getVariationPoint/setVariationPoint provided by the VariationPointCapable base
    # (mixin), no spec rows; aggregated by IEEE1722TpAcfConnection.acfTransportedBus only)

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Definition of the ACF CAN stream message type.
        self.messageType: Optional[IEEE1722TpAcfCanMessageTypeEnum] = None

    def getMessageType(self) -> Optional[IEEE1722TpAcfCanMessageTypeEnum]:
        """
        Definition of the ACF CAN stream message type.
        """
        return self.messageType

    def setMessageType(self, value: Optional[IEEE1722TpAcfCanMessageTypeEnum]) -> IEEE1722TpAcfCan:
        """
        Definition of the ACF CAN stream message type.
        A None value is a no-op and does not overwrite an existing messageType.
        """
        if value is not None:
            self.messageType = value
        return self


class IEEE1722TpAcfLin(IEEE1722TpAcfBus):
    pass


from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (  # noqa: E402
    PduCollectionTriggerEnum as PduCollectionTriggerEnum,
)
