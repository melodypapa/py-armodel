"""
Writer tests for DDS-CP-PARTITION elements — DdsCpPartition, Table 6.178 (p.527, R23-11).

writeDdsCpPartition creates the DDS-CP-PARTITION element, emits the IDENTIFIABLE level
(SHORT-NAME, UUID — writeIdentifiable, called exactly once, Rule 0013.1/0025), then its own
group member PARTITION-NAME (group DDS-CP-PARTITION, AUTOSAR_00052.xsd l.28823).

Round-trip counterpart: tests/test_armodel/parser/test_dds_cp_partition.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DdsCpPartition
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _new_partition() -> DdsCpPartition:
    partition = DdsCpPartition(AUTOSAR.getInstance(), "Partition1")
    partition.setPartitionName(String().setValue("Partition_A"))
    return partition


class TestWriteDdsCpPartition:
    def test_write_emits_partition_name(self):
        """Test that the writer emits SHORT-NAME then PARTITION-NAME with its value."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpPartition(parent, _new_partition())

        child = parent.find("DDS-CP-PARTITION")
        assert child is not None
        children = [c.tag for c in child]
        assert children[0] == "SHORT-NAME"
        assert child.find("SHORT-NAME").text == "Partition1"
        assert child.find("PARTITION-NAME").text == "Partition_A"

    def test_write_empty_omits_members(self):
        """Test that an empty partition emits only the SHORT-NAME (Identifiable level)."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpPartition(parent, DdsCpPartition(AUTOSAR.getInstance(), "Empty"))
        child = parent.find("DDS-CP-PARTITION")
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_round_trip_via_file(self, tmp_path):
        """Element-level round-trip: write, reload, read back via readDdsCpPartition, assert field values."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpPartition(parent, _new_partition())
        inner = ET.tostring(parent[0]).decode("utf-8")

        out_file = str(tmp_path / "dds_cp_partition.arxml")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(f"<AUTOSAR xmlns='{NS}'>{inner}</AUTOSAR>")

        AUTOSAR.getInstance().new()
        re_document = AUTOSAR.getInstance()
        re_document.setARRelease("R23-11")
        parser = ARXMLParser(options={"warning": True})
        re_partition = DdsCpPartition(re_document, "Partition1")
        parser.readDdsCpPartition(ET.parse(out_file).getroot()[0], re_partition)

        assert re_partition.getShortName() == "Partition1"
        assert re_partition.getPartitionName().getValue() == "Partition_A"
