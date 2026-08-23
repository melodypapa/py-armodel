"""Writer round-trip tests for LinSlaveConfig (Table 3.39, p.95).

Verifies that ``setLinSlaveConfig`` serializes every attribute into a
``LIN-SLAVE-CONFIG`` element tree, omits empty wrapper lists, and skips
the whole element when the config is absent.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, Integer, PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import LinErrorResponse
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import LinConfigurableFrame, LinOrderedConfigurableFrame, LinSlaveConfig, LinSlaveConfigIdent
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    return ARXMLWriter()


def _parent():
    return ET.Element("PARENT")


def _int(value):
    n = Integer()
    n.setValue(value)
    return n


def _pint(value):
    n = PositiveInteger()
    n.setValue(value)
    return n


def _ref(value):
    return RefType().setValue(value)


def _literal(value):
    lit = ARLiteral()
    lit.setValue(value)
    return lit


def _full_config():
    config = LinSlaveConfig()
    config.setConfiguredNad(_int(3))
    config.setFunctionId(_pint(24))
    ident = LinSlaveConfigIdent(config, "SlaveIdent")
    config.setIdent(ident)
    config.setInitialNad(_int(1))

    frame = LinConfigurableFrame()
    frame.setFrameRef(_ref("/System/LinFrame"))
    frame.setMessageId(_pint(42))
    config.addLinConfigurableFrame(frame)

    response = LinErrorResponse()
    response.setResponseErrorRef(_ref("/System/ISignalTriggering"))
    config.setLinErrorResponse(response)

    ordered = LinOrderedConfigurableFrame()
    ordered.setFrameRef(_ref("/System/LinFrame2"))
    ordered.setIndex(_int(7))
    config.addLinOrderedConfigurableFrame(ordered)

    config.setProtocolVersion(_literal("2.1"))
    config.setSupplierId(_pint(17))
    config.setVariantId(_pint(9))
    return config


class TestSetLinSlaveConfig:
    def test_write_all_fields(self, writer):
        parent = _parent()
        writer.setLinSlaveConfig(parent, "LIN-SLAVE-CONFIG", _full_config())

        el = parent.find("LIN-SLAVE-CONFIG")
        assert el is not None
        assert el.find("CONFIGURED-NAD").text == "3"
        assert el.find("FUNCTION-ID").text == "24"

        ident_el = el.find("IDENT")
        assert ident_el is not None
        assert ident_el.find("SHORT-NAME").text == "SlaveIdent"

        assert el.find("INITIAL-NAD").text == "1"

        frames_wrapper = el.find("LIN-CONFIGURABLE-FRAMES")
        assert frames_wrapper is not None
        frame_el = frames_wrapper.find("LIN-CONFIGURABLE-FRAME")
        assert frame_el is not None
        assert frame_el.find("FRAME-REF").text == "/System/LinFrame"
        assert frame_el.find("MESSAGE-ID").text == "42"

        response_el = el.find("LIN-ERROR-RESPONSE")
        assert response_el is not None
        assert response_el.find("RESPONSE-ERROR-REF").text == "/System/ISignalTriggering"

        ordered_wrapper = el.find("LIN-ORDERED-CONFIGURABLE-FRAMES")
        assert ordered_wrapper is not None
        ordered_el = ordered_wrapper.find("LIN-ORDERED-CONFIGURABLE-FRAME")
        assert ordered_el is not None
        assert ordered_el.find("FRAME-REF").text == "/System/LinFrame2"
        assert ordered_el.find("INDEX").text == "7"

        assert el.find("PROTOCOL-VERSION").text == "2.1"
        assert el.find("SUPPLIER-ID").text == "17"
        assert el.find("VARIANT-ID").text == "9"

    def test_empty_wrapper_lists_are_omitted(self, writer):
        parent = _parent()
        config = LinSlaveConfig()
        config.setConfiguredNad(_int(3))

        writer.setLinSlaveConfig(parent, "LIN-SLAVE-CONFIG", config)

        el = parent.find("LIN-SLAVE-CONFIG")
        assert el is not None
        assert el.find("LIN-CONFIGURABLE-FRAMES") is None
        assert el.find("LIN-ORDERED-CONFIGURABLE-FRAMES") is None

    def test_write_none_skips_element(self, writer):
        parent = _parent()
        writer.setLinSlaveConfig(parent, "LIN-SLAVE-CONFIG", None)
        assert parent.find("LIN-SLAVE-CONFIG") is None
