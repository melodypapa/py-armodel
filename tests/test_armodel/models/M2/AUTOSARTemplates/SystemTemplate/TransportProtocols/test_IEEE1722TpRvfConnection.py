import typing
from inspect import cleandoc
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp import (
    IEEE1722TpAvConnection,
    IEEE1722TpRvfConnection,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAv import (
    IEEE1722TpRvfColorSpaceEnum,
    IEEE1722TpRvfFrameRateEnum,
    IEEE1722TpRvfPixelDepthEnum,
    IEEE1722TpRvfPixelFormatEnum,
)


def _pos_int(value):
    integer = PositiveInteger()
    integer.setValue(value)
    return integer


def _enum(enum_class, member):
    enum = enum_class()
    enum.setValue(member)
    return enum


class TestIEEE1722TpRvfConnection:
    def test_docstring_is_spec_note_verbatim(self):
        # Table 6.285, p.650 — class Note verbatim from the markdown
        assert cleandoc(IEEE1722TpRvfConnection.__doc__) == "AV IEEE1722Tp RVF connection. Tags: atp.Status=candidate atp.recommendedPackage=IEEE1722TpConnections"

    def test_heritage(self):
        assert issubclass(IEEE1722TpRvfConnection, IEEE1722TpAvConnection)

    def test_initialization(self):
        connection = IEEE1722TpRvfConnection(None, "RvfStream")
        assert connection.getMaxTransitTime() is None
        assert connection.getSduRefs() == []
        assert connection.getRvfActivePixels() is None
        assert connection.getRvfColorSpace() is None
        assert connection.getRvfEventDefault() is None
        assert connection.getRvfFrameRate() is None
        assert connection.getRvfInterlaced() is None
        assert connection.getRvfPixelDepth() is None
        assert connection.getRvfPixelFormat() is None
        assert connection.getRvfTotalLines() is None

    def test_get_set_own_attributes(self):
        connection = IEEE1722TpRvfConnection(None, "RvfStream")

        active_pixels = _pos_int(1920)
        assert connection.setRvfActivePixels(active_pixels) is connection
        assert connection.getRvfActivePixels() is active_pixels
        assert connection.setRvfActivePixels(None) is connection
        assert connection.getRvfActivePixels() is active_pixels

        color_space = _enum(IEEE1722TpRvfColorSpaceEnum, IEEE1722TpRvfColorSpaceEnum.ENUM_YCBCR)
        assert connection.setRvfColorSpace(color_space) is connection
        assert connection.getRvfColorSpace() is color_space
        assert connection.setRvfColorSpace(None) is connection
        assert connection.getRvfColorSpace() is color_space

        event_default = _pos_int(8)
        assert connection.setRvfEventDefault(event_default) is connection
        assert connection.getRvfEventDefault() is event_default
        assert connection.setRvfEventDefault(None) is connection
        assert connection.getRvfEventDefault() is event_default

        frame_rate = _enum(IEEE1722TpRvfFrameRateEnum, IEEE1722TpRvfFrameRateEnum.ENUM_60)
        assert connection.setRvfFrameRate(frame_rate) is connection
        assert connection.getRvfFrameRate() is frame_rate
        assert connection.setRvfFrameRate(None) is connection
        assert connection.getRvfFrameRate() is frame_rate

        interlaced = Boolean()
        interlaced.setValue(True)
        assert connection.setRvfInterlaced(interlaced) is connection
        assert connection.getRvfInterlaced() is interlaced
        assert connection.setRvfInterlaced(None) is connection
        assert connection.getRvfInterlaced() is interlaced

        pixel_depth = _enum(IEEE1722TpRvfPixelDepthEnum, IEEE1722TpRvfPixelDepthEnum.ENUM_10)
        assert connection.setRvfPixelDepth(pixel_depth) is connection
        assert connection.getRvfPixelDepth() is pixel_depth
        assert connection.setRvfPixelDepth(None) is connection
        assert connection.getRvfPixelDepth() is pixel_depth

        pixel_format = _enum(IEEE1722TpRvfPixelFormatEnum, IEEE1722TpRvfPixelFormatEnum.ENUM_4_2_0)
        assert connection.setRvfPixelFormat(pixel_format) is connection
        assert connection.getRvfPixelFormat() is pixel_format
        assert connection.setRvfPixelFormat(None) is connection
        assert connection.getRvfPixelFormat() is pixel_format

        total_lines = _pos_int(1080)
        assert connection.setRvfTotalLines(total_lines) is connection
        assert connection.getRvfTotalLines() is total_lines
        assert connection.setRvfTotalLines(None) is connection
        assert connection.getRvfTotalLines() is total_lines

    def test_annotations(self):
        hints = typing.get_type_hints(IEEE1722TpRvfConnection.setRvfActivePixels)
        assert hints["value"] == Optional[PositiveInteger]
        hints = typing.get_type_hints(IEEE1722TpRvfConnection.getRvfColorSpace)
        assert hints["return"] == Optional[IEEE1722TpRvfColorSpaceEnum]
        hints = typing.get_type_hints(IEEE1722TpRvfConnection.getRvfInterlaced)
        assert hints["return"] == Optional[Boolean]
