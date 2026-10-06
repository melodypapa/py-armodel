"""Writer round-trip tests for LinOrderedConfigurableFrame (Table 3.45, p.99).

Verifies that the singleton wrapper serializes its ``frameRef`` and
``index`` into a ``LIN-ORDERED-CONFIGURABLE-FRAME`` / ``FRAME-REF`` /
``INDEX`` element tree and is skipped when the frame is absent. The XSD
complexType (AUTOSAR_00052.xsd line 77531) = AR-OBJECT group +
LIN-ORDERED-CONFIGURABLE-FRAME group + AR-OBJECT attributeGroup, so
setLinOrderedConfigurableFrame calls writeARObject exactly once and the inherited
S/T attributes round-trip — also through the LIN-SLAVE-CONFIG consumer path
(Rule 0001.7, see test_lin_slave_config.py).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, Integer, RefType, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import LinOrderedConfigurableFrame, LinSlaveConfig
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
    frame = LinOrderedConfigurableFrame()
    frame.setFrameRef(RefType().setValue("/System/LinFrame"))
    frame.setIndex(Integer().setValue(3))
    frame.setChecksum(String().setValue("chk-1"))
    frame.setTimestamp(DateTime().setValue("2009-07-23T13:38:00Z"))
    return frame


def test_write_lin_ordered_configurable_frame_all_fields(writer):
    parent = _parent()
    frame = LinOrderedConfigurableFrame()
    ref = RefType().setValue("/System/LinFrame")
    frame.setFrameRef(ref)
    frame.setIndex(Integer().setValue(3))

    writer.setLinOrderedConfigurableFrame(parent, "LIN-ORDERED-CONFIGURABLE-FRAME", frame)

    el = parent.find("LIN-ORDERED-CONFIGURABLE-FRAME")
    assert el is not None
    assert el.find("FRAME-REF").text == "/System/LinFrame"
    assert el.find("INDEX").text == "3"


def test_write_checksum_and_timestamp_attributes(writer):
    parent = _parent()
    writer.setLinOrderedConfigurableFrame(parent, "LIN-ORDERED-CONFIGURABLE-FRAME", _stamped_frame())

    el = parent.find("LIN-ORDERED-CONFIGURABLE-FRAME")
    assert el is not None
    assert el.attrib["S"] == "chk-1"
    assert el.attrib["T"] == "2009-07-23T13:38:00Z"


def test_write_empty_frame_emits_element_without_children(writer):
    parent = _parent()
    writer.setLinOrderedConfigurableFrame(parent, "LIN-ORDERED-CONFIGURABLE-FRAME", LinOrderedConfigurableFrame())

    el = parent.find("LIN-ORDERED-CONFIGURABLE-FRAME")
    assert el is not None
    assert el.find("FRAME-REF") is None
    assert el.find("INDEX") is None


def test_write_frame_st_through_set_lin_slave_config(writer):
    config = LinSlaveConfig()
    config.addLinOrderedConfigurableFrame(_stamped_frame())

    parent = _parent()
    writer.setLinSlaveConfig(parent, "LIN-SLAVE-CONFIG", config)

    el = parent.find("LIN-SLAVE-CONFIG")
    assert el is not None
    frames_wrapper = el.find("LIN-ORDERED-CONFIGURABLE-FRAMES")
    assert frames_wrapper is not None
    frame_el = frames_wrapper.find("LIN-ORDERED-CONFIGURABLE-FRAME")
    assert frame_el is not None
    assert frame_el.find("FRAME-REF").text == "/System/LinFrame"
    assert frame_el.find("INDEX").text == "3"
    assert frame_el.attrib["S"] == "chk-1"
    assert frame_el.attrib["T"] == "2009-07-23T13:38:00Z"


def test_write_lin_ordered_configurable_frame_none(writer):
    parent = _parent()
    writer.setLinOrderedConfigurableFrame(parent, "LIN-ORDERED-CONFIGURABLE-FRAME", None)
    assert parent.find("LIN-ORDERED-CONFIGURABLE-FRAME") is None
