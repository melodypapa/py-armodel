"""Writer round-trip tests for LinSlaveConfig (Table 3.39, p.95).

Verifies that ``setLinSlaveConfig`` serializes every attribute into a
``LIN-SLAVE-CONFIG`` element tree in the XSD LIN-SLAVE-CONFIG group order
(AUTOSAR_00052.xsd line 77742), omits empty wrapper lists, skips the whole
element when the config is absent, and calls writeARObject exactly once so the
inherited S/T attributes round-trip.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ShortNameFragment
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, DateTime, Identifier, Integer, PositiveInteger, RefType, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import LinErrorResponse
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import LinConfigurableFrame, LinOrderedConfigurableFrame, LinSlaveConfig, LinSlaveConfigIdent
from armodel.parser.arxml_parser import ARXMLParser
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


NS = "http://autosar.org/schema/r4.0"


def _namespaced_first_child(parent):
    xml_text = ET.tostring(parent, encoding="unicode")
    namespaced = ET.fromstring(xml_text.replace(parent[0].tag, "%s xmlns='%s'" % (parent[0].tag, NS), 1))
    return namespaced[0]


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


def _stamped_config():
    config = _full_config()
    config.setChecksum(String().setValue("chk-1"))
    config.setTimestamp(DateTime().setValue("2009-07-23T13:38:00Z"))
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

    def test_writes_checksum_and_timestamp_attributes(self, writer):
        parent = _parent()
        writer.setLinSlaveConfig(parent, "LIN-SLAVE-CONFIG", _stamped_config())

        el = parent.find("LIN-SLAVE-CONFIG")
        assert el is not None
        assert el.attrib["S"] == "chk-1"
        assert el.attrib["T"] == "2009-07-23T13:38:00Z"

    def test_write_without_checksum_omits_st_attributes(self, writer):
        parent = _parent()
        writer.setLinSlaveConfig(parent, "LIN-SLAVE-CONFIG", LinSlaveConfig())

        el = parent.find("LIN-SLAVE-CONFIG")
        assert el is not None
        assert "S" not in el.attrib
        assert "T" not in el.attrib

    def test_round_trip_through_set_lin_slave_config(self, writer):
        parent = _parent()
        writer.setLinSlaveConfig(parent, "LIN-SLAVE-CONFIG", _stamped_config())

        reloaded = ARXMLParser().getLinSlaveConfig(_namespaced_first_child(parent), ".")
        assert isinstance(reloaded, LinSlaveConfig)
        assert reloaded.getConfiguredNad().getValue() == 3
        assert reloaded.getFunctionId().getValue() == 24
        assert reloaded.getIdent().getShortName() == "SlaveIdent"
        assert reloaded.getInitialNad().getValue() == 1
        frames = reloaded.getLinConfigurableFrames()
        assert len(frames) == 1
        assert frames[0].getFrameRef().getValue() == "/System/LinFrame"
        assert frames[0].getMessageId().getValue() == 42
        assert reloaded.getLinErrorResponse().getResponseErrorRef().getValue() == "/System/ISignalTriggering"
        ordered = reloaded.getLinOrderedConfigurableFrames()
        assert len(ordered) == 1
        assert ordered[0].getFrameRef().getValue() == "/System/LinFrame2"
        assert ordered[0].getIndex().getValue() == 7
        assert reloaded.getProtocolVersion().getValue() == "2.1"
        assert reloaded.getSupplierId().getValue() == 17
        assert reloaded.getVariantId().getValue() == 9
        assert reloaded.getChecksum().getValue() == "chk-1"
        assert reloaded.getTimestamp().getValue() == "2009-07-23T13:38:00Z"

    @staticmethod
    def _config_with_referrable_ident():
        config = LinSlaveConfig()
        ident = LinSlaveConfigIdent(config, "SlaveIdent")
        fragment = ShortNameFragment()
        fragment.setRole(String().setValue("prefix"))
        fragment.setFragment(Identifier().setValue("PFX"))
        ident.addShortNameFragment(fragment)
        config.setIdent(ident)
        return config

    def test_write_ident_referrable_payload(self, writer):
        parent = _parent()
        writer.setLinSlaveConfig(parent, "LIN-SLAVE-CONFIG", self._config_with_referrable_ident())

        el = parent.find("LIN-SLAVE-CONFIG")
        ident_el = el.find("IDENT")
        assert ident_el is not None
        assert ident_el.find("SHORT-NAME").text == "SlaveIdent"
        fragments_el = ident_el.find("SHORT-NAME-FRAGMENTS")
        assert fragments_el is not None
        fragment_el = fragments_el.find("SHORT-NAME-FRAGMENT")
        assert fragment_el is not None
        assert fragment_el.find("ROLE").text == "prefix"
        assert fragment_el.find("FRAGMENT").text == "PFX"

    def test_round_trip_ident_referrable_payload(self, writer):
        parent = _parent()
        writer.setLinSlaveConfig(parent, "LIN-SLAVE-CONFIG", self._config_with_referrable_ident())

        reloaded = ARXMLParser().getLinSlaveConfig(_namespaced_first_child(parent), ".")
        ident = reloaded.getIdent()
        assert isinstance(ident, LinSlaveConfigIdent)
        assert ident.getShortName() == "SlaveIdent"
        fragments = ident.getShortNameFragments()
        assert len(fragments) == 1
        assert fragments[0].getRole().getValue() == "prefix"
        assert fragments[0].getFragment().getValue() == "PFX"

    def test_write_ident_st_attributes(self, writer):
        parent = _parent()
        config = self._config_with_referrable_ident()
        ident = config.getIdent()
        ident.setChecksum(String().setValue("id-chk"))
        ident.setTimestamp(DateTime().setValue("2009-07-23T13:38:00Z"))
        writer.setLinSlaveConfig(parent, "LIN-SLAVE-CONFIG", config)

        ident_el = parent.find("LIN-SLAVE-CONFIG").find("IDENT")
        assert ident_el is not None
        assert ident_el.attrib["S"] == "id-chk"
        assert ident_el.attrib["T"] == "2009-07-23T13:38:00Z"

    def test_round_trip_ident_st_attributes(self, writer):
        parent = _parent()
        config = self._config_with_referrable_ident()
        ident = config.getIdent()
        ident.setChecksum(String().setValue("id-chk"))
        ident.setTimestamp(DateTime().setValue("2009-07-23T13:38:00Z"))
        writer.setLinSlaveConfig(parent, "LIN-SLAVE-CONFIG", config)

        reloaded = ARXMLParser().getLinSlaveConfig(_namespaced_first_child(parent), ".")
        reloaded_ident = reloaded.getIdent()
        assert reloaded_ident.getChecksum().getValue() == "id-chk"
        assert reloaded_ident.getTimestamp().getValue() == "2009-07-23T13:38:00Z"
