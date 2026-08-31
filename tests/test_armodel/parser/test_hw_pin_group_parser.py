"""
Reader tests for HwPinGroup.hwPinGroupContent (AUTOSAR_CP_TPS_ECUResourceTemplate Table 2.5).

The prior heritage-fix session covered HwPinGroup's UUID (Identifiable) regression but
never read/wrote the only own attribute, hwPinGroupContent (Rule 0001.7 silent drop).
This pins the read path for HW-PIN-GROUP-CONTENT and its HW-PIN / HW-PIN-GROUP children.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR, HwPinGroup
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import HwPinGroupContent
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<HW-PIN-GROUP xmlns='{NS}'>{inner}</HW-PIN-GROUP>")


class TestReadHwPinGroupContent:
    def test_read_content_with_pin(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip(
            "<SHORT-NAME>Group1</SHORT-NAME>"
            "<HW-PIN-GROUP-CONTENT>"
            "<HW-PIN><SHORT-NAME>P1</SHORT-NAME>"
            "<FUNCTION-NAMES><FUNCTION-NAME>CLK</FUNCTION-NAME></FUNCTION-NAMES>"
            "</HW-PIN>"
            "</HW-PIN-GROUP-CONTENT>"
        )
        group = HwPinGroup(AUTOSAR.getInstance(), "Group1")
        parser.readHwPinGroup(element, group)

        content = group.getHwPinGroupContent()
        assert isinstance(content, HwPinGroupContent)
        pin = content.getHwPin()
        assert pin is not None
        assert pin.getShortName() == "P1"
        assert "CLK" in pin.getFunctionNames()

    def test_read_content_with_nested_pin_group(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>Group1</SHORT-NAME>" "<HW-PIN-GROUP-CONTENT>" "<HW-PIN-GROUP><SHORT-NAME>SubGroup</SHORT-NAME></HW-PIN-GROUP>" "</HW-PIN-GROUP-CONTENT>")
        group = HwPinGroup(AUTOSAR.getInstance(), "Group1")
        parser.readHwPinGroup(element, group)

        content = group.getHwPinGroupContent()
        assert content.getHwPinGroup() is not None
        assert content.getHwPinGroup().getShortName() == "SubGroup"

    def test_read_no_content(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>Group1</SHORT-NAME>")
        group = HwPinGroup(AUTOSAR.getInstance(), "Group1")
        parser.readHwPinGroup(element, group)
        assert group.getHwPinGroupContent() is None
