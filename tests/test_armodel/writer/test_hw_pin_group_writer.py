"""
Writer tests for HwPinGroup.hwPinGroupContent (AUTOSAR_CP_TPS_ECUResourceTemplate Table 2.5).

The writer emits unprefixed child elements; structure checks inspect the in-memory tree
with unprefixed names. The round-trip serializes + reparses so the default AUTOSAR
namespace applies (the parser's find() is namespace-aware), then re-reads the model.

Round-trip counterpart: tests/test_armodel/parser/test_hw_pin_group_parser.py
"""

import logging
import xml.etree.ElementTree as ET

from armodel.models import AUTOSAR, HwPinGroup
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import HwPinGroupContent
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

QNS = "http://autosar.org/schema/r4.0"


def _make_writer() -> ARXMLWriter:
    writer = ARXMLWriter.__new__(ARXMLWriter)
    writer.logger = logging.getLogger("test.writer")
    return writer


class TestWriteHwPinGroupContent:
    def test_write_content_with_pin(self):
        writer = _make_writer()
        group = HwPinGroup(AUTOSAR.getInstance(), "Group1")
        content = HwPinGroupContent()
        pin = content.createHwPin("P1")
        pin.addFunctionName("CLK")
        group.setHwPinGroupContent(content)

        root = ET.Element("AR-PACKAGE")
        writer.writeHwPinGroup(root, group)

        hw_pin_group_el = root.find("HW-PIN-GROUP")
        assert hw_pin_group_el is not None
        content_el = hw_pin_group_el.find("HW-PIN-GROUP-CONTENT")
        assert content_el is not None
        pin_el = content_el.find("HW-PIN")
        assert pin_el is not None
        assert pin_el.find("SHORT-NAME").text == "P1"
        assert pin_el.find("FUNCTION-NAMES/FUNCTION-NAME").text == "CLK"

    def test_write_no_content(self):
        writer = _make_writer()
        group = HwPinGroup(AUTOSAR.getInstance(), "Group1")
        root = ET.Element("AR-PACKAGE")
        writer.writeHwPinGroup(root, group)
        hw_pin_group_el = root.find("HW-PIN-GROUP")
        assert hw_pin_group_el.find("HW-PIN-GROUP-CONTENT") is None

    def test_write_and_reparse_round_trip(self):
        writer = _make_writer()
        group = HwPinGroup(AUTOSAR.getInstance(), "Group1")
        content = HwPinGroupContent()
        pin = content.createHwPin("P1")
        pin.addFunctionName("CLK")
        group.setHwPinGroupContent(content)

        root = ET.Element("AR-PACKAGE")
        root.set("xmlns", QNS)
        writer.writeHwPinGroup(root, group)

        # serialize + reparse so the default namespace applies (parser find() is ns-aware)
        reparsed_root = ET.fromstring(ET.tostring(root))
        hw_pin_group_el = reparsed_root.find("{%s}HW-PIN-GROUP" % QNS)
        assert hw_pin_group_el is not None

        parser = ARXMLParser(options={"warning": True})
        reparsed = HwPinGroup(AUTOSAR.getInstance(), "Group1")
        parser.readHwPinGroup(hw_pin_group_el, reparsed)

        reparsed_content = reparsed.getHwPinGroupContent()
        assert reparsed_content is not None
        assert reparsed_content.getHwPin() is not None
        assert reparsed_content.getHwPin().getShortName() == "P1"
        assert "CLK" in reparsed_content.getHwPin().getFunctionNames()
