"""Parser tests for getLinSlaveConfig (Table 3.39, p.95).

Shared fixtures (``parser``) are provided by ``conftest.py``; the ``_snip``
helper lives in ``_helpers.py``.
"""

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import LinErrorResponse
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import LinSlaveConfig, LinSlaveConfigIdent
from tests.test_armodel.parser._helpers import _snip

_FULL = (
    "<LIN-SLAVE-CONFIG>"
    "<CONFIGURED-NAD>3</CONFIGURED-NAD>"
    "<FUNCTION-ID>24</FUNCTION-ID>"
    "<IDENT><SHORT-NAME>SlaveIdent</SHORT-NAME></IDENT>"
    "<INITIAL-NAD>1</INITIAL-NAD>"
    "<LIN-CONFIGURABLE-FRAMES>"
    "<LIN-CONFIGURABLE-FRAME><FRAME-REF>/System/LinFrame</FRAME-REF><MESSAGE-ID>42</MESSAGE-ID></LIN-CONFIGURABLE-FRAME>"
    "</LIN-CONFIGURABLE-FRAMES>"
    "<LIN-ERROR-RESPONSE><RESPONSE-ERROR-REF>/System/ISignalTriggering</RESPONSE-ERROR-REF></LIN-ERROR-RESPONSE>"
    "<LIN-ORDERED-CONFIGURABLE-FRAMES>"
    "<LIN-ORDERED-CONFIGURABLE-FRAME><FRAME-REF>/System/LinFrame2</FRAME-REF><INDEX>7</INDEX></LIN-ORDERED-CONFIGURABLE-FRAME>"
    "</LIN-ORDERED-CONFIGURABLE-FRAMES>"
    "<PROTOCOL-VERSION>2.1</PROTOCOL-VERSION>"
    "<SUPPLIER-ID>17</SUPPLIER-ID>"
    "<VARIANT-ID>9</VARIANT-ID>"
    "</LIN-SLAVE-CONFIG>"
)


class TestGetLinSlaveConfig:
    def test_returns_none_when_child_absent(self, parser):
        element = _snip("<OTHER/>")
        assert parser.getLinSlaveConfig(element, "LIN-SLAVE-CONFIG") is None

    def test_reads_all_fields(self, parser):
        element = _snip(_FULL)
        config = parser.getLinSlaveConfig(element, "LIN-SLAVE-CONFIG")

        assert isinstance(config, LinSlaveConfig)
        assert config.getConfiguredNad().getValue() == 3
        assert config.getFunctionId().getValue() == 24

        ident = config.getIdent()
        assert isinstance(ident, LinSlaveConfigIdent)
        assert ident.getShortName() == "SlaveIdent"
        assert ident.getParent() == config

        assert config.getInitialNad().getValue() == 1

        frames = config.getLinConfigurableFrames()
        assert len(frames) == 1
        assert frames[0].getFrameRef().getValue() == "/System/LinFrame"
        assert frames[0].getMessageId().getValue() == 42

        response = config.getLinErrorResponse()
        assert isinstance(response, LinErrorResponse)
        assert response.getResponseErrorRef().getValue() == "/System/ISignalTriggering"

        ordered = config.getLinOrderedConfigurableFrames()
        assert len(ordered) == 1
        assert ordered[0].getFrameRef().getValue() == "/System/LinFrame2"
        assert ordered[0].getIndex().getValue() == 7

        assert config.getProtocolVersion().getValue() == "2.1"
        assert config.getSupplierId().getValue() == 17
        assert config.getVariantId().getValue() == 9

    def test_empty_wrapper_lists_yield_empty_lists(self, parser):
        element = _snip("<LIN-SLAVE-CONFIG><LIN-CONFIGURABLE-FRAMES/><LIN-ORDERED-CONFIGURABLE-FRAMES/></LIN-SLAVE-CONFIG>")
        config = parser.getLinSlaveConfig(element, "LIN-SLAVE-CONFIG")

        assert isinstance(config, LinSlaveConfig)
        assert config.getLinConfigurableFrames() == []
        assert config.getLinOrderedConfigurableFrames() == []
        assert config.getConfiguredNad() is None
