"""
Writer tests for RESOURCE-LIMITS elements — DdsResourceLimits, Table 6.200 (p.538, R23-11).

writeDdsResourceLimits creates the RESOURCE-LIMITS element, emits the AR-OBJECT level
(writeARObject — S/T) and the group members MAX-INSTANCES, MAX-SAMPLES,
MAX-SAMPLES-PER-INSTANCE in XSD sequenceOffset order (group DDS-RESOURCE-LIMITS,
AUTOSAR_00052.xsd l.30104).

Round-trip counterpart: tests/test_armodel/parser/test_dds_resource_limits.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DdsResourceLimits
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _new_resource_limits() -> DdsResourceLimits:
    resource_limits = DdsResourceLimits()
    resource_limits.setMaxInstances(PositiveInteger().setValue("1"))
    resource_limits.setMaxSamples(PositiveInteger().setValue("2"))
    resource_limits.setMaxSamplesPerInstance(PositiveInteger().setValue("4"))
    return resource_limits


class TestWriteDdsResourceLimits:
    def test_write_emits_members_in_xsd_order(self):
        """Test that the writer emits the three members with their values in XSD order."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsResourceLimits(parent, _new_resource_limits())

        child = parent.find("RESOURCE-LIMITS")
        assert child is not None
        children = [c.tag for c in child]
        assert children.index("MAX-INSTANCES") < children.index("MAX-SAMPLES")
        assert children.index("MAX-SAMPLES") < children.index("MAX-SAMPLES-PER-INSTANCE")
        assert child.find("MAX-INSTANCES").text == "1"
        assert child.find("MAX-SAMPLES").text == "2"
        assert child.find("MAX-SAMPLES-PER-INSTANCE").text == "4"

    def test_write_empty_omits_members(self):
        """Test that an empty resource limits element emits no members."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsResourceLimits(parent, DdsResourceLimits())
        child = parent.find("RESOURCE-LIMITS")
        assert child is not None
        assert len(list(child)) == 0

    def test_round_trip_via_file(self, tmp_path):
        """Element-level round-trip: write, reload, read back via readDdsResourceLimits, assert field values."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsResourceLimits(parent, _new_resource_limits())
        inner = ET.tostring(parent[0]).decode("utf-8")

        out_file = str(tmp_path / "dds_resource_limits.arxml")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(f"<AUTOSAR xmlns='{NS}'>{inner}</AUTOSAR>")

        AUTOSAR.getInstance().new()
        re_document = AUTOSAR.getInstance()
        re_document.setARRelease("R23-11")
        parser = ARXMLParser(options={"warning": True})
        re_resource_limits = DdsResourceLimits()
        parser.readDdsResourceLimits(ET.parse(out_file).getroot()[0], re_resource_limits)

        assert re_resource_limits.getMaxInstances().getValue() == 1
        assert re_resource_limits.getMaxSamples().getValue() == 2
        assert re_resource_limits.getMaxSamplesPerInstance().getValue() == 4
