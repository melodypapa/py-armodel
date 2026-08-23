"""Writer round-trip tests for CanXlFrameTriggeringProps (Table F.27, p.447).

Verifies that the singleton wrapper serializes its four PositiveInteger
attributes into a ``CAN-XL-FRAME-TRIGGERING-PROPS`` element tree and is
skipped when the props are absent.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import CanXlFrameTriggeringProps
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


def test_write_can_xl_frame_triggering_props_all_fields(writer):
    parent = _parent()
    props = CanXlFrameTriggeringProps()
    props.setAcceptanceField(PositiveInteger().setValue(0))
    props.setPriorityId(PositiveInteger().setValue(7))
    props.setSduType(PositiveInteger().setValue(8))
    props.setVcid(PositiveInteger().setValue(10))

    writer.setCanXlFrameTriggeringProps(parent, "CAN-XL-FRAME-TRIGGERING-PROPS", props)

    el = parent.find("CAN-XL-FRAME-TRIGGERING-PROPS")
    assert el is not None
    assert el.find("ACCEPTANCE-FIELD").text == "0"
    assert el.find("PRIORITY-ID").text == "7"
    assert el.find("SDU-TYPE").text == "8"
    assert el.find("VCID").text == "10"


def test_write_can_xl_frame_triggering_props_none(writer):
    parent = _parent()
    writer.setCanXlFrameTriggeringProps(parent, "CAN-XL-FRAME-TRIGGERING-PROPS", None)
    assert parent.find("CAN-XL-FRAME-TRIGGERING-PROPS") is None
