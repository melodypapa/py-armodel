import typing
from inspect import cleandoc
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    IEEE1722TpAcfBus,
    IEEE1722TpAcfCan,
    IEEE1722TpAcfLin,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp import (
    IEEE1722TpAcfConnection,
    IEEE1722TpConnection,
)


def _pos_int(value):
    integer = PositiveInteger()
    integer.setValue(value)
    return integer


def _time(value):
    t = TimeValue()
    t.setValue(value)
    return t


def _bool(value):
    b = Boolean()
    b.setValue(value)
    return b


class TestIEEE1722TpAcfConnection:
    def test_docstring_is_spec_note(self):
        assert cleandoc(IEEE1722TpAcfConnection.__doc__) == "ACF IEEE1722Tp connection. Tags: atp.Status=candidate atp.recommendedPackage=IEEE1722TpConnections"

    def test_heritage(self):
        assert issubclass(IEEE1722TpAcfConnection, IEEE1722TpConnection)

    def test_initialization(self):
        connection = IEEE1722TpAcfConnection(None, "AcfConnection")
        assert connection.getAcfTransportedBuses() == []
        assert connection.getCollectionThreshold() is None
        assert connection.getCollectionTimeout() is None
        assert connection.getMixedBusTypeCollection() is None

    def test_create_acf_transported_buses(self):
        connection = IEEE1722TpAcfConnection(None, "AcfConnection")

        can_bus = connection.createIEEE1722TpAcfCan("CanBus")
        assert isinstance(can_bus, IEEE1722TpAcfCan)
        assert isinstance(can_bus, IEEE1722TpAcfBus)
        assert can_bus.getShortName() == "CanBus"
        assert connection.createIEEE1722TpAcfCan("CanBus") is can_bus

        lin_bus = connection.createIEEE1722TpAcfLin("LinBus")
        assert isinstance(lin_bus, IEEE1722TpAcfLin)
        assert isinstance(lin_bus, IEEE1722TpAcfBus)
        assert lin_bus.getShortName() == "LinBus"
        assert connection.createIEEE1722TpAcfLin("LinBus") is lin_bus

        buses = connection.getAcfTransportedBuses()
        assert len(buses) == 2
        assert buses[0] is can_bus
        assert buses[1] is lin_bus

    def test_get_set_collection_threshold(self):
        connection = IEEE1722TpAcfConnection(None, "AcfConnection")

        result = connection.setCollectionThreshold(_pos_int(900))
        assert result is connection
        assert connection.getCollectionThreshold().getValue() == 900

        connection.setCollectionThreshold(None)
        assert connection.getCollectionThreshold().getValue() == 900

    def test_get_set_collection_timeout(self):
        connection = IEEE1722TpAcfConnection(None, "AcfConnection")

        result = connection.setCollectionTimeout(_time(0.01))
        assert result is connection
        assert connection.getCollectionTimeout().getValue() == 0.01

        connection.setCollectionTimeout(None)
        assert connection.getCollectionTimeout().getValue() == 0.01

    def test_get_set_mixed_bus_type_collection(self):
        connection = IEEE1722TpAcfConnection(None, "AcfConnection")

        result = connection.setMixedBusTypeCollection(_bool(True))
        assert result is connection
        assert connection.getMixedBusTypeCollection().getValue() is True

        connection.setMixedBusTypeCollection(None)
        assert connection.getMixedBusTypeCollection().getValue() is True

    def test_annotations(self):
        hints = typing.get_type_hints(IEEE1722TpAcfConnection.getAcfTransportedBuses)
        assert hints["return"] == List[IEEE1722TpAcfBus]
        hints = typing.get_type_hints(IEEE1722TpAcfConnection.createIEEE1722TpAcfCan)
        assert hints["short_name"] is str
        assert hints["return"] == IEEE1722TpAcfCan
        hints = typing.get_type_hints(IEEE1722TpAcfConnection.createIEEE1722TpAcfLin)
        assert hints["short_name"] is str
        assert hints["return"] == IEEE1722TpAcfLin
        hints = typing.get_type_hints(IEEE1722TpAcfConnection.getCollectionThreshold)
        assert hints["return"] == Optional[PositiveInteger]
        hints = typing.get_type_hints(IEEE1722TpAcfConnection.setCollectionThreshold)
        assert hints["value"] == Optional[PositiveInteger]
        hints = typing.get_type_hints(IEEE1722TpAcfConnection.getCollectionTimeout)
        assert hints["return"] == Optional[TimeValue]
        hints = typing.get_type_hints(IEEE1722TpAcfConnection.setCollectionTimeout)
        assert hints["value"] == Optional[TimeValue]
        hints = typing.get_type_hints(IEEE1722TpAcfConnection.getMixedBusTypeCollection)
        assert hints["return"] == Optional[Boolean]
        hints = typing.get_type_hints(IEEE1722TpAcfConnection.setMixedBusTypeCollection)
        assert hints["value"] == Optional[Boolean]
