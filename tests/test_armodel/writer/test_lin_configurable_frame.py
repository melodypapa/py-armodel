"""Writer round-trip tests for LinConfigurableFrame (Table 3.44, p.99).

Verifies that the singleton wrapper serializes its ``frameRef`` and
``messageId`` into a ``LIN-CONFIGURABLE-FRAME`` / ``FRAME-REF`` /
``MESSAGE-ID`` element tree and is skipped when the frame is absent. The XSD
complexType (AUTOSAR_00052.xsd line 77104) = AR-OBJECT group +
LIN-CONFIGURABLE-FRAME group + AR-OBJECT attributeGroup, so
setLinConfigurableFrame calls writeARObject exactly once and the inherited
S/T attributes round-trip — also through the LIN-SLAVE-CONFIG consumer path
(Rule 0001.7, see test_lin_slave_config.py).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, PositiveInteger, RefType, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import LinConfigurableFrame, LinSlaveConfig
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


def _stamped_frame():
    frame = LinConfigurableFrame()
    frame.setFrameRef(RefType().setValue("/System/LinFrame"))
    frame.setMessageId(PositiveInteger().setValue(42))
    frame.setChecksum(String().setValue("chk-1"))
    frame.setTimestamp(DateTime().setValue("2009-07-23T13:38:00Z"))
    return frame


def test_write_lin_configurable_frame_all_fields(writer):
    parent = _parent()
    frame = LinConfigurableFrame()
    ref = RefType().setValue("/System/LinFrame")
    frame.setFrameRef(ref)
    frame.setMessageId(PositiveInteger().setValue(42))

    writer.setLinConfigurableFrame(parent, "LIN-CONFIGURABLE-FRAME", frame)

    el = parent.find("LIN-CONFIGURABLE-FRAME")
    assert el is not None
    assert el.find("FRAME-REF").text == "/System/LinFrame"
    assert el.find("MESSAGE-ID").text == "42"


def test_write_checksum_and_timestamp_attributes(writer):
    parent = _parent()
    writer.setLinConfigurableFrame(parent, "LIN-CONFIGURABLE-FRAME", _stamped_frame())

    el = parent.find("LIN-CONFIGURABLE-FRAME")
    assert el is not None
    assert el.attrib["S"] == "chk-1"
    assert el.attrib["T"] == "2009-07-23T13:38:00Z"


def test_write_empty_frame_emits_element_without_children(writer):
    parent = _parent()
    writer.setLinConfigurableFrame(parent, "LIN-CONFIGURABLE-FRAME", LinConfigurableFrame())

    el = parent.find("LIN-CONFIGURABLE-FRAME")
    assert el is not None
    assert el.find("FRAME-REF") is None
    assert el.find("MESSAGE-ID") is None


def test_write_lin_configurable_frame_none(writer):
    parent = _parent()
    writer.setLinConfigurableFrame(parent, "LIN-CONFIGURABLE-FRAME", None)
    assert parent.find("LIN-CONFIGURABLE-FRAME") is None


def test_write_frame_st_through_set_lin_slave_config(writer):
    config = LinSlaveConfig()
    config.addLinConfigurableFrame(_stamped_frame())

    parent = _parent()
    writer.setLinSlaveConfig(parent, "LIN-SLAVE-CONFIG", config)

    el = parent.find("LIN-SLAVE-CONFIG")
    assert el is not None
    frames_wrapper = el.find("LIN-CONFIGURABLE-FRAMES")
    assert frames_wrapper is not None
    frame_el = frames_wrapper.find("LIN-CONFIGURABLE-FRAME")
    assert frame_el is not None
    assert frame_el.find("FRAME-REF").text == "/System/LinFrame"
    assert frame_el.find("MESSAGE-ID").text == "42"
    assert frame_el.attrib["S"] == "chk-1"
    assert frame_el.attrib["T"] == "2009-07-23T13:38:00Z"
