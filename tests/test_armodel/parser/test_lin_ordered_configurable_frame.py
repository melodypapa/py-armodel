"""Parser tests for getLinOrderedConfigurableFrame (Table 3.45, p.99).

LIN-ORDERED-CONFIGURABLE-FRAME has no standalone element dispatch: it serializes only
as a choice of LIN-ORDERED-CONFIGURABLE-FRAME elements under the LIN-ORDERED-CONFIGURABLE-FRAMES
wrapper inside LIN-SLAVE-CONFIG (Table 3.39) and LIN-COMMUNICATION-CONNECTOR
(Table 3.43) — consumer path, Rule 0001.7 (see test_lin_slave_config.py /
test_lin_communication_connector.py). The XSD complexType (AUTOSAR_00052.xsd
line 77531) = AR-OBJECT group + LIN-ORDERED-CONFIGURABLE-FRAME group + AR-OBJECT
attributeGroup, so getLinOrderedConfigurableFrame (the class's reader entry point)
calls readARObject exactly once and the inherited S/T attributes round-trip.

Shared fixtures (``parser``) are provided by ``conftest.py``; the ``_snip``
helper lives in ``_helpers.py``.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import LinOrderedConfigurableFrame, LinSlaveConfig
from tests.test_armodel.parser._helpers import _snip

_ST_FRAME = '<LIN-ORDERED-CONFIGURABLE-FRAME S="chk-1" T="2009-07-23T13:38:00Z">' "<FRAME-REF>/System/LinFrame</FRAME-REF>" "<INDEX>3</INDEX>" "</LIN-ORDERED-CONFIGURABLE-FRAME>"

_ST_FRAME_IN_CONFIG = (
    "<LIN-SLAVE-CONFIG><LIN-ORDERED-CONFIGURABLE-FRAMES>"
    '<LIN-ORDERED-CONFIGURABLE-FRAME S="chk-1" T="2009-07-23T13:38:00Z">'
    "<FRAME-REF>/System/LinFrame</FRAME-REF>"
    "<INDEX>3</INDEX>"
    "</LIN-ORDERED-CONFIGURABLE-FRAME>"
    "</LIN-ORDERED-CONFIGURABLE-FRAMES></LIN-SLAVE-CONFIG>"
)


class TestGetLinOrderedConfigurableFrame:
    def test_returns_none_when_child_absent(self, parser):
        element = _snip("<OTHER/>")
        result = parser.getLinOrderedConfigurableFrame(element, "LIN-ORDERED-CONFIGURABLE-FRAME")
        assert result is None

    def test_returns_frame_when_child_present(self, parser):
        element = _snip("<LIN-ORDERED-CONFIGURABLE-FRAME>" "<FRAME-REF>/System/LinFrame</FRAME-REF>" "<INDEX>3</INDEX>" "</LIN-ORDERED-CONFIGURABLE-FRAME>")
        result = parser.getLinOrderedConfigurableFrame(element, "LIN-ORDERED-CONFIGURABLE-FRAME")
        assert isinstance(result, LinOrderedConfigurableFrame)
        ref = result.getFrameRef()
        assert isinstance(ref, RefType)
        assert ref.getValue() == "/System/LinFrame"
        assert result.getIndex().getValue() == 3

    def test_reads_checksum_and_timestamp_attributes(self, parser):
        element = _snip(_ST_FRAME)
        result = parser.getLinOrderedConfigurableFrame(element, "LIN-ORDERED-CONFIGURABLE-FRAME")

        assert isinstance(result, LinOrderedConfigurableFrame)
        assert result.getChecksum() is not None
        assert result.getChecksum().getValue() == "chk-1"
        assert result.getTimestamp() is not None
        assert result.getTimestamp().getValue() == "2009-07-23T13:38:00Z"

    def test_reads_empty_frame_to_default_fields(self, parser):
        element = _snip("<LIN-ORDERED-CONFIGURABLE-FRAME/>")
        result = parser.getLinOrderedConfigurableFrame(element, "LIN-ORDERED-CONFIGURABLE-FRAME")

        assert isinstance(result, LinOrderedConfigurableFrame)
        assert result.getFrameRef() is None
        assert result.getIndex() is None

    def test_reads_frame_st_through_lin_slave_config_consumer(self, parser):
        element = _snip(_ST_FRAME_IN_CONFIG)
        config = parser.getLinSlaveConfig(element, "LIN-SLAVE-CONFIG")

        assert isinstance(config, LinSlaveConfig)
        frames = config.getLinOrderedConfigurableFrames()
        assert len(frames) == 1
        frame = frames[0]
        assert isinstance(frame, LinOrderedConfigurableFrame)
        assert frame.getFrameRef().getValue() == "/System/LinFrame"
        assert frame.getIndex().getValue() == 3
        assert frame.getChecksum() is not None
        assert frame.getChecksum().getValue() == "chk-1"
        assert frame.getTimestamp() is not None
        assert frame.getTimestamp().getValue() == "2009-07-23T13:38:00Z"
