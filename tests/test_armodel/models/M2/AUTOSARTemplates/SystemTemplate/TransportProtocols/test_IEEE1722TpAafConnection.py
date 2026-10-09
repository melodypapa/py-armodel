import typing
from inspect import cleandoc
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp import (
    IEEE1722TpAafConnection,
    IEEE1722TpAvConnection,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAv import (
    IEEE1722TpAafAes3DataTypeEnum,
    IEEE1722TpAafFormatEnum,
    IEEE1722TpAafNominalRateEnum,
)


def _pos_int(value):
    integer = PositiveInteger()
    integer.setValue(value)
    return integer


class TestIEEE1722TpAafConnection:
    def test_docstring_is_spec_note_verbatim(self):
        # Table 6.280, p.643 — class Note verbatim from the markdown
        assert cleandoc(IEEE1722TpAafConnection.__doc__) == "AV IEEE1722Tp AAF connection. Tags: atp.Status=candidate atp.recommendedPackage=IEEE1722TpConnections"

    def test_heritage(self):
        assert issubclass(IEEE1722TpAafConnection, IEEE1722TpAvConnection)

    def test_initialization(self):
        connection = IEEE1722TpAafConnection(None, "AafStream")
        assert connection.getMaxTransitTime() is None
        assert connection.getSduRefs() == []
        assert connection.getAafAes3DataType() is None
        assert connection.getAafFormat() is None
        assert connection.getAafNominalRate() is None
        assert connection.getAes3DataTypeH() is None
        assert connection.getAes3DataTypeL() is None
        assert connection.getChannelsPerFrame() is None
        assert connection.getEventDefaultValue() is None
        assert connection.getPcmBitDepth() is None
        assert connection.getSparseTimestampEnabled() is None
        assert connection.getStreamsPerFrame() is None

    def test_get_set_own_attributes(self):
        connection = IEEE1722TpAafConnection(None, "AafStream")

        aes3_data_type = IEEE1722TpAafAes3DataTypeEnum()
        aes3_data_type.setValue(IEEE1722TpAafAes3DataTypeEnum.ENUM_PCM)
        assert connection.setAafAes3DataType(aes3_data_type) is connection
        assert connection.getAafAes3DataType() is aes3_data_type
        assert connection.setAafAes3DataType(None) is connection
        assert connection.getAafAes3DataType() is aes3_data_type

        aaf_format = IEEE1722TpAafFormatEnum()
        aaf_format.setValue(IEEE1722TpAafFormatEnum.AES3_32BIT)
        assert connection.setAafFormat(aaf_format) is connection
        assert connection.getAafFormat() is aaf_format
        assert connection.setAafFormat(None) is connection
        assert connection.getAafFormat() is aaf_format

        nominal_rate = IEEE1722TpAafNominalRateEnum()
        nominal_rate.setValue(IEEE1722TpAafNominalRateEnum.ENUM_48KHZ)
        assert connection.setAafNominalRate(nominal_rate) is connection
        assert connection.getAafNominalRate() is nominal_rate
        assert connection.setAafNominalRate(None) is connection
        assert connection.getAafNominalRate() is nominal_rate

        aes3_h = _pos_int(2)
        assert connection.setAes3DataTypeH(aes3_h) is connection
        assert connection.getAes3DataTypeH() is aes3_h
        assert connection.setAes3DataTypeH(None) is connection
        assert connection.getAes3DataTypeH() is aes3_h

        aes3_l = _pos_int(1)
        assert connection.setAes3DataTypeL(aes3_l) is connection
        assert connection.getAes3DataTypeL() is aes3_l
        assert connection.setAes3DataTypeL(None) is connection
        assert connection.getAes3DataTypeL() is aes3_l

        channels = _pos_int(2)
        assert connection.setChannelsPerFrame(channels) is connection
        assert connection.getChannelsPerFrame() is channels
        assert connection.setChannelsPerFrame(None) is connection
        assert connection.getChannelsPerFrame() is channels

        event_default = _pos_int(0)
        assert connection.setEventDefaultValue(event_default) is connection
        assert connection.getEventDefaultValue() is event_default
        assert connection.setEventDefaultValue(None) is connection
        assert connection.getEventDefaultValue() is event_default

        pcm_bit_depth = _pos_int(24)
        assert connection.setPcmBitDepth(pcm_bit_depth) is connection
        assert connection.getPcmBitDepth() is pcm_bit_depth
        assert connection.setPcmBitDepth(None) is connection
        assert connection.getPcmBitDepth() is pcm_bit_depth

        sparse = Boolean()
        sparse.setValue(True)
        assert connection.setSparseTimestampEnabled(sparse) is connection
        assert connection.getSparseTimestampEnabled() is sparse
        assert connection.setSparseTimestampEnabled(None) is connection
        assert connection.getSparseTimestampEnabled() is sparse

        streams = _pos_int(4)
        assert connection.setStreamsPerFrame(streams) is connection
        assert connection.getStreamsPerFrame() is streams
        assert connection.setStreamsPerFrame(None) is connection
        assert connection.getStreamsPerFrame() is streams

    def test_annotations(self):
        hints = typing.get_type_hints(IEEE1722TpAafConnection.getAafAes3DataType)
        assert hints["return"] == Optional[IEEE1722TpAafAes3DataTypeEnum]
        hints = typing.get_type_hints(IEEE1722TpAafConnection.setAafFormat)
        assert hints["value"] == Optional[IEEE1722TpAafFormatEnum]
        hints = typing.get_type_hints(IEEE1722TpAafConnection.setAafNominalRate)
        assert hints["value"] == Optional[IEEE1722TpAafNominalRateEnum]
