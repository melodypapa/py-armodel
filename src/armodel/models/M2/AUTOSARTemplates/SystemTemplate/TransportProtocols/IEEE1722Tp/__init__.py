# This module contains AUTOSAR System Template IEEE1722Tp transport protocol classes
# (spec package M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp)

from __future__ import annotations

from abc import ABC
from typing import List, Optional, cast

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf import (
    IEEE1722TpAcfBus,
    IEEE1722TpAcfCan,
    IEEE1722TpAcfLin,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    MacAddressString,
    PositiveInteger,
    RefType,
    TimeValue,
)
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


class IEEE1722TpConnection(ARElement, ABC):
    """
    Definition of the IEEE1722Tp protocol. Tags: atp.Status=candidate
    """

    # IEEE1722TpConnection method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.275, p.637
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDestinationMacAddress  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDestinationMacAddress  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMacAddressStreamId     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMacAddressStreamId     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPduRef                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPduRef                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getUniqueStreamId         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setUniqueStreamId         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getVersion                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setVersion                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getVlanPriority           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setVlanPriority           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # (Abstract; XSD-only COMMUNICATION-DIRECTION (mmt.RestrictToStandards=AP) not modeled — PDF table omits it, Rule 0015)

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is IEEE1722TpConnection:
            raise TypeError("IEEE1722TpConnection is an abstract class.")

        super().__init__(parent, short_name)

        # Optional definition of the destination MAC address for this stream. If no given then macAddressStreamId is used as destination MAC address. Tags: atp.Status=candidate
        self.destinationMacAddress: Optional[MacAddressString] = None

        # MAC Address part of the Stream Id. Tags: atp.Status=candidate
        self.macAddressStreamId: Optional[MacAddressString] = None

        # Reference to the lower layer Pdu used for the IEEE1722Tp protocol transport. Tags: atp.Status=candidate
        self.pduRef: Optional[RefType] = None

        # Unique Id part of the Stream Id. Tags: atp.Status=candidate
        self.uniqueStreamId: Optional[PositiveInteger] = None

        # Version of the IEEE1722TP stream. Tags: atp.Status=candidate
        self.version: Optional[PositiveInteger] = None

        # Optional definition of the VLAN priority for this stream.
        self.vlanPriority: Optional[PositiveInteger] = None

    def getDestinationMacAddress(self) -> Optional[MacAddressString]:
        """
        Optional definition of the destination MAC address for this stream. If no given then macAddressStreamId is used as destination MAC address. Tags: atp.Status=candidate
        """
        return self.destinationMacAddress

    def setDestinationMacAddress(self, value: Optional[MacAddressString]) -> IEEE1722TpConnection:
        """
        Optional definition of the destination MAC address for this stream. If no given then macAddressStreamId is used as destination MAC address. Tags: atp.Status=candidate
        A None value is a no-op and does not overwrite an existing destinationMacAddress.
        """
        if value is not None:
            self.destinationMacAddress = value
        return self

    def getMacAddressStreamId(self) -> Optional[MacAddressString]:
        """
        MAC Address part of the Stream Id. Tags: atp.Status=candidate
        """
        return self.macAddressStreamId

    def setMacAddressStreamId(self, value: Optional[MacAddressString]) -> IEEE1722TpConnection:
        """
        MAC Address part of the Stream Id. Tags: atp.Status=candidate
        A None value is a no-op and does not overwrite an existing macAddressStreamId.
        """
        if value is not None:
            self.macAddressStreamId = value
        return self

    def getPduRef(self) -> Optional[RefType]:
        """
        Reference to the lower layer Pdu used for the IEEE1722Tp protocol transport. Tags: atp.Status=candidate
        """
        return self.pduRef

    def setPduRef(self, value: Optional[RefType]) -> IEEE1722TpConnection:
        """
        Reference to the lower layer Pdu used for the IEEE1722Tp protocol transport. Tags: atp.Status=candidate
        A None value is a no-op and does not overwrite an existing pduRef.
        """
        if value is not None:
            self.pduRef = value
        return self

    def getUniqueStreamId(self) -> Optional[PositiveInteger]:
        """
        Unique Id part of the Stream Id. Tags: atp.Status=candidate
        """
        return self.uniqueStreamId

    def setUniqueStreamId(self, value: Optional[PositiveInteger]) -> IEEE1722TpConnection:
        """
        Unique Id part of the Stream Id. Tags: atp.Status=candidate
        A None value is a no-op and does not overwrite an existing uniqueStreamId.
        """
        if value is not None:
            self.uniqueStreamId = value
        return self

    def getVersion(self) -> Optional[PositiveInteger]:
        """
        Version of the IEEE1722TP stream. Tags: atp.Status=candidate
        """
        return self.version

    def setVersion(self, value: Optional[PositiveInteger]) -> IEEE1722TpConnection:
        """
        Version of the IEEE1722TP stream. Tags: atp.Status=candidate
        A None value is a no-op and does not overwrite an existing version.
        """
        if value is not None:
            self.version = value
        return self

    def getVlanPriority(self) -> Optional[PositiveInteger]:
        """
        Optional definition of the VLAN priority for this stream.
        """
        return self.vlanPriority

    def setVlanPriority(self, value: Optional[PositiveInteger]) -> IEEE1722TpConnection:
        """
        Optional definition of the VLAN priority for this stream.
        A None value is a no-op and does not overwrite an existing vlanPriority.
        """
        if value is not None:
            self.vlanPriority = value
        return self


class IEEE1722TpAvConnection(IEEE1722TpConnection, ABC):
    """
    AV IEEE1722Tp connection. Tags: atp.Status=candidate
    """

    # IEEE1722TpAvConnection method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.276, p.639
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getMaxTransitTime     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMaxTransitTime     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addSduRef             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSduRefs            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # (Abstract; Base row: ARElement, ARObject, CollectableElement, IEEE1722TpConnection, Identifiable, MultilanguageReferrable, PackageableElement, Referrable)

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is IEEE1722TpAvConnection:
            raise TypeError("IEEE1722TpAvConnection is an abstract class.")

        super().__init__(parent, short_name)

        # Defines the time offset that is added to the current time at the producer in order to get the "presentation time" (in seconds) when content shall be presented at the consumers.
        self.maxTransitTime: Optional[TimeValue] = None

        # Reference to the upper layer Sdu used for the transport of the payload of the IEEE1722Tp. Tags: atp.Status=candidate
        self.sduRefs: List[RefType] = []

    def getMaxTransitTime(self) -> Optional[TimeValue]:
        """
        Defines the time offset that is added to the current time at the producer in order to get the "presentation time" (in seconds) when content shall be presented at the consumers.
        """
        return self.maxTransitTime

    def setMaxTransitTime(self, value: Optional[TimeValue]) -> IEEE1722TpAvConnection:
        """
        Defines the time offset that is added to the current time at the producer in order to get the "presentation time" (in seconds) when content shall be presented at the consumers.
        A None value is a no-op and does not overwrite an existing maxTransitTime.
        """
        if value is not None:
            self.maxTransitTime = value
        return self

    def addSduRef(self, value: Optional[RefType]) -> IEEE1722TpAvConnection:
        """
        Reference to the upper layer Sdu used for the transport of the payload of the IEEE1722Tp. Tags: atp.Status=candidate
        A None value is a no-op and is not appended to sduRefs.
        """
        if value is not None:
            self.sduRefs.append(value)
        return self

    def getSduRefs(self) -> List[RefType]:
        """
        Reference to the upper layer Sdu used for the transport of the payload of the IEEE1722Tp. Tags: atp.Status=candidate
        """
        return self.sduRefs


class IEEE1722TpAcfConnection(IEEE1722TpConnection):
    """
    ACF IEEE1722Tp connection. Tags: atp.Status=candidate atp.recommendedPackage=IEEE1722TpConnections
    """

    # IEEE1722TpAcfConnection method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.290, p.657
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createIEEE1722TpAcfCan    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createIEEE1722TpAcfLin    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getAcfTransportedBuses    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getCollectionThreshold    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCollectionThreshold    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCollectionTimeout      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCollectionTimeout      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMixedBusTypeCollection [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMixedBusTypeCollection [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # (Base row: ARElement, ARObject, CollectableElement, IEEE1722TpConnection, Identifiable, MultilanguageReferrable, PackageableElement, Referrable)

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Definition of the transported busses over this ACF connection. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=acfTransportedBus.shortName, acf TransportedBus.variationPoint.shortLabel atp.Status=candidate vh.latestBindingTime=postBuild
        self.acfTransportedBuses: List[IEEE1722TpAcfBus] = []

        # Defines the size threshold in bytes which, when exceeded, triggers the sending of the IEEE1722Tp ACF message, even when the maxium IEEE1722Tp ACF message size has not been reached yet.
        self.collectionThreshold: Optional[PositiveInteger] = None

        # When this timeout expires the IEEE1722Tp ACF message is triggered for sending. The respective timer is started when the first Pdu is put into the IEEE1722Tp ACF message. Defined in seconds.
        self.collectionTimeout: Optional[TimeValue] = None

        # Defines if this ACF-stream is allowed to collect ACF-messages of different bus kinds (i.e. whether it is allowed to collect CAN and LIN ACF-messages in one ACF-stream message).
        self.mixedBusTypeCollection: Optional[Boolean] = None

    def createIEEE1722TpAcfCan(self, short_name: str) -> IEEE1722TpAcfCan:
        """
        Definition of the transported busses over this ACF connection. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=acfTransportedBus.shortName, acf TransportedBus.variationPoint.shortLabel atp.Status=candidate vh.latestBindingTime=postBuild
        """
        if not self.IsReferrableElementExists(short_name, IEEE1722TpAcfCan):
            bus = IEEE1722TpAcfCan(self, short_name)
            self.addReferrableElement(bus)
            self.acfTransportedBuses.append(bus)
        return cast(IEEE1722TpAcfCan, self.getReferrableElement(short_name, IEEE1722TpAcfCan))

    def createIEEE1722TpAcfLin(self, short_name: str) -> IEEE1722TpAcfLin:
        """
        Definition of the transported busses over this ACF connection. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=acfTransportedBus.shortName, acf TransportedBus.variationPoint.shortLabel atp.Status=candidate vh.latestBindingTime=postBuild
        """
        if not self.IsReferrableElementExists(short_name, IEEE1722TpAcfLin):
            bus = IEEE1722TpAcfLin(self, short_name)
            self.addReferrableElement(bus)
            self.acfTransportedBuses.append(bus)
        return cast(IEEE1722TpAcfLin, self.getReferrableElement(short_name, IEEE1722TpAcfLin))

    def getAcfTransportedBuses(self) -> List[IEEE1722TpAcfBus]:
        """
        Definition of the transported busses over this ACF connection. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=acfTransportedBus.shortName, acf TransportedBus.variationPoint.shortLabel atp.Status=candidate vh.latestBindingTime=postBuild
        """
        return self.acfTransportedBuses

    def getCollectionThreshold(self) -> Optional[PositiveInteger]:
        """
        Defines the size threshold in bytes which, when exceeded, triggers the sending of the IEEE1722Tp ACF message, even when the maxium IEEE1722Tp ACF message size has not been reached yet.
        """
        return self.collectionThreshold

    def setCollectionThreshold(self, value: Optional[PositiveInteger]) -> IEEE1722TpAcfConnection:
        """
        Defines the size threshold in bytes which, when exceeded, triggers the sending of the IEEE1722Tp ACF message, even when the maxium IEEE1722Tp ACF message size has not been reached yet.
        A None value is a no-op and does not overwrite an existing collectionThreshold.
        """
        if value is not None:
            self.collectionThreshold = value
        return self

    def getCollectionTimeout(self) -> Optional[TimeValue]:
        """
        When this timeout expires the IEEE1722Tp ACF message is triggered for sending. The respective timer is started when the first Pdu is put into the IEEE1722Tp ACF message. Defined in seconds.
        """
        return self.collectionTimeout

    def setCollectionTimeout(self, value: Optional[TimeValue]) -> IEEE1722TpAcfConnection:
        """
        When this timeout expires the IEEE1722Tp ACF message is triggered for sending. The respective timer is started when the first Pdu is put into the IEEE1722Tp ACF message. Defined in seconds.
        A None value is a no-op and does not overwrite an existing collectionTimeout.
        """
        if value is not None:
            self.collectionTimeout = value
        return self

    def getMixedBusTypeCollection(self) -> Optional[Boolean]:
        """
        Defines if this ACF-stream is allowed to collect ACF-messages of different bus kinds (i.e. whether it is allowed to collect CAN and LIN ACF-messages in one ACF-stream message).
        """
        return self.mixedBusTypeCollection

    def setMixedBusTypeCollection(self, value: Optional[Boolean]) -> IEEE1722TpAcfConnection:
        """
        Defines if this ACF-stream is allowed to collect ACF-messages of different bus kinds (i.e. whether it is allowed to collect CAN and LIN ACF-messages in one ACF-stream message).
        A None value is a no-op and does not overwrite an existing mixedBusTypeCollection.
        """
        if value is not None:
            self.mixedBusTypeCollection = value
        return self


from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAv import (  # noqa: E402
    IEEE1722TpAafAes3DataTypeEnum as IEEE1722TpAafAes3DataTypeEnum,
    IEEE1722TpAafConnection as IEEE1722TpAafConnection,
    IEEE1722TpAafFormatEnum as IEEE1722TpAafFormatEnum,
    IEEE1722TpAafNominalRateEnum as IEEE1722TpAafNominalRateEnum,
    IEEE1722TpCrfConnection as IEEE1722TpCrfConnection,
    IEEE1722TpCrfPullEnum as IEEE1722TpCrfPullEnum,
    IEEE1722TpCrfTypeEnum as IEEE1722TpCrfTypeEnum,
    IEEE1722TpIidcConnection as IEEE1722TpIidcConnection,
    IEEE1722TpRvfConnection as IEEE1722TpRvfConnection,
    IEEE1722TpRvfPixelDepthEnum as IEEE1722TpRvfPixelDepthEnum,
    IEEE1722TpRvfPixelFormatEnum as IEEE1722TpRvfPixelFormatEnum,
    IEEE1722TpRvfColorSpaceEnum as IEEE1722TpRvfColorSpaceEnum,
    IEEE1722TpRvfFrameRateEnum as IEEE1722TpRvfFrameRateEnum,
)
