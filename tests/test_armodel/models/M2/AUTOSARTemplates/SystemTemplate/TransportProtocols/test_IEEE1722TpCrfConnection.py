import typing
from inspect import cleandoc
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp import (
    IEEE1722TpAvConnection,
    IEEE1722TpCrfConnection,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAv import (
    IEEE1722TpCrfPullEnum,
    IEEE1722TpCrfTypeEnum,
)


def _pos_int(value):
    integer = PositiveInteger()
    integer.setValue(value)
    return integer


class TestIEEE1722TpCrfConnection:
    def test_docstring_is_spec_note_verbatim(self):
        # Table 6.277, p.640 — class Note verbatim from the markdown
        assert cleandoc(IEEE1722TpCrfConnection.__doc__) == "AV IEEE1722Tp CRF connection. Tags: atp.Status=candidate atp.recommendedPackage=IEEE1722TpConnections"

    def test_heritage(self):
        assert issubclass(IEEE1722TpCrfConnection, IEEE1722TpAvConnection)

    def test_initialization(self):
        connection = IEEE1722TpCrfConnection(None, "CrfConn")
        assert connection.getMaxTransitTime() is None
        assert connection.getSduRefs() == []
        assert connection.getBaseFrequency() is None
        assert connection.getCrfPull() is None
        assert connection.getCrfType() is None
        assert connection.getFrameSyncEnabled() is None
        assert connection.getTimestampInterval() is None

    def test_get_set_own_attributes(self):
        connection = IEEE1722TpCrfConnection(None, "CrfConn")

        base_frequency = _pos_int(8000)
        assert connection.setBaseFrequency(base_frequency) is connection
        assert connection.getBaseFrequency() is base_frequency
        assert connection.setBaseFrequency(None) is connection
        assert connection.getBaseFrequency() is base_frequency

        crf_pull = IEEE1722TpCrfPullEnum()
        crf_pull.setValue(IEEE1722TpCrfPullEnum.ENUM_1_0)
        assert connection.setCrfPull(crf_pull) is connection
        assert connection.getCrfPull() is crf_pull
        assert connection.setCrfPull(None) is connection
        assert connection.getCrfPull() is crf_pull

        crf_type = IEEE1722TpCrfTypeEnum()
        crf_type.setValue(IEEE1722TpCrfTypeEnum.ENUM_VIDEO_FRAME)
        assert connection.setCrfType(crf_type) is connection
        assert connection.getCrfType() is crf_type
        assert connection.setCrfType(None) is connection
        assert connection.getCrfType() is crf_type

        frame_sync = Boolean()
        frame_sync.setValue(True)
        assert connection.setFrameSyncEnabled(frame_sync) is connection
        assert connection.getFrameSyncEnabled() is frame_sync
        assert connection.setFrameSyncEnabled(None) is connection
        assert connection.getFrameSyncEnabled() is frame_sync

        timestamp_interval = _pos_int(4)
        assert connection.setTimestampInterval(timestamp_interval) is connection
        assert connection.getTimestampInterval() is timestamp_interval
        assert connection.setTimestampInterval(None) is connection
        assert connection.getTimestampInterval() is timestamp_interval

    def test_annotations(self):
        hints = typing.get_type_hints(IEEE1722TpCrfConnection.getCrfPull)
        assert hints["return"] == Optional[IEEE1722TpCrfPullEnum]
        hints = typing.get_type_hints(IEEE1722TpCrfConnection.setCrfType)
        assert hints["value"] == Optional[IEEE1722TpCrfTypeEnum]
