"""Writer round-trip tests for LinConfigurableFrame (Table 3.44, p.99).

Verifies that the singleton wrapper serializes its ``frameRef`` and
``messageId`` into a ``LIN-CONFIGURABLE-FRAME`` / ``FRAME-REF`` /
``MESSAGE-ID`` element tree and is skipped when the frame is absent.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import LinConfigurableFrame
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


def test_write_lin_configurable_frame_none(writer):
    parent = _parent()
    writer.setLinConfigurableFrame(parent, "LIN-CONFIGURABLE-FRAME", None)
    assert parent.find("LIN-CONFIGURABLE-FRAME") is None
