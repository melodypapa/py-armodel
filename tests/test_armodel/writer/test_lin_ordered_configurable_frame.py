"""Writer round-trip tests for LinOrderedConfigurableFrame (Table 3.45, p.99).

Verifies that the singleton wrapper serializes its ``frameRef`` and
``index`` into a ``LIN-ORDERED-CONFIGURABLE-FRAME`` / ``FRAME-REF`` /
``INDEX`` element tree and is skipped when the frame is absent.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import LinOrderedConfigurableFrame
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


def test_write_lin_ordered_configurable_frame_none(writer):
    parent = _parent()
    writer.setLinOrderedConfigurableFrame(parent, "LIN-ORDERED-CONFIGURABLE-FRAME", None)
    assert parent.find("LIN-ORDERED-CONFIGURABLE-FRAME") is None
