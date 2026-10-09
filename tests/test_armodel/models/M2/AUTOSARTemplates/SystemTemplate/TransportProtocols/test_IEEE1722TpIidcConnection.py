import typing
from inspect import cleandoc
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp import (
    IEEE1722TpAvConnection,
    IEEE1722TpIidcConnection,
)


def _pos_int(value):
    integer = PositiveInteger()
    integer.setValue(value)
    return integer


class TestIEEE1722TpIidcConnection:
    def test_docstring_is_spec_note_verbatim(self):
        # Table 6.284, p.648 — class Note verbatim from the markdown
        assert cleandoc(IEEE1722TpIidcConnection.__doc__) == "AV IEEE1722Tp IIDC connection. Tags: atp.Status=candidate atp.recommendedPackage=IEEE1722TpConnections"

    def test_heritage(self):
        assert issubclass(IEEE1722TpIidcConnection, IEEE1722TpAvConnection)

    def test_initialization(self):
        connection = IEEE1722TpIidcConnection(None, "IidcStream")
        assert connection.getMaxTransitTime() is None
        assert connection.getSduRefs() == []
        assert connection.getIidcChannel() is None
        assert connection.getIidcDataBlockSize() is None
        assert connection.getIidcFractionNumber() is None
        assert connection.getIidcSourcePacketHeader() is None
        assert connection.getIidcStreamFormat() is None
        assert connection.getIidcSy() is None
        assert connection.getIidcTag() is None
        assert connection.getIidcTCode() is None

    def test_get_set_own_attributes(self):
        connection = IEEE1722TpIidcConnection(None, "IidcStream")

        channel = _pos_int(1)
        assert connection.setIidcChannel(channel) is connection
        assert connection.getIidcChannel() is channel
        assert connection.setIidcChannel(None) is connection
        assert connection.getIidcChannel() is channel

        data_block_size = _pos_int(128)
        assert connection.setIidcDataBlockSize(data_block_size) is connection
        assert connection.getIidcDataBlockSize() is data_block_size
        assert connection.setIidcDataBlockSize(None) is connection
        assert connection.getIidcDataBlockSize() is data_block_size

        fraction_number = _pos_int(2)
        assert connection.setIidcFractionNumber(fraction_number) is connection
        assert connection.getIidcFractionNumber() is fraction_number
        assert connection.setIidcFractionNumber(None) is connection
        assert connection.getIidcFractionNumber() is fraction_number

        source_packet_header = Boolean()
        source_packet_header.setValue(True)
        assert connection.setIidcSourcePacketHeader(source_packet_header) is connection
        assert connection.getIidcSourcePacketHeader() is source_packet_header
        assert connection.setIidcSourcePacketHeader(None) is connection
        assert connection.getIidcSourcePacketHeader() is source_packet_header

        stream_format = _pos_int(0)
        assert connection.setIidcStreamFormat(stream_format) is connection
        assert connection.getIidcStreamFormat() is stream_format
        assert connection.setIidcStreamFormat(None) is connection
        assert connection.getIidcStreamFormat() is stream_format

        sy = _pos_int(255)
        assert connection.setIidcSy(sy) is connection
        assert connection.getIidcSy() is sy
        assert connection.setIidcSy(None) is connection
        assert connection.getIidcSy() is sy

        tag = _pos_int(8)
        assert connection.setIidcTag(tag) is connection
        assert connection.getIidcTag() is tag
        assert connection.setIidcTag(None) is connection
        assert connection.getIidcTag() is tag

        tcode = _pos_int(16)
        assert connection.setIidcTCode(tcode) is connection
        assert connection.getIidcTCode() is tcode
        assert connection.setIidcTCode(None) is connection
        assert connection.getIidcTCode() is tcode

    def test_annotations(self):
        hints = typing.get_type_hints(IEEE1722TpIidcConnection.setIidcChannel)
        assert hints["value"] == Optional[PositiveInteger]
        hints = typing.get_type_hints(IEEE1722TpIidcConnection.getIidcSourcePacketHeader)
        assert hints["return"] == Optional[Boolean]
