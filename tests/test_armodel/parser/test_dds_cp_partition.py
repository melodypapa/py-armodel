"""
Tests for reading DDS-CP-PARTITION elements — DdsCpPartition, Table 6.178 (p.527, R23-11).

The class is a nested Identifiable element (aggregated by DdsCpDomain.ddsPartition, Table 6.176),
so the reusable helper readDdsCpPartition is exercised directly on a standalone XML subtree
(XSD complexType DDS-CP-PARTITION, AUTOSAR_00052.xsd l.28839: group sequence AR-OBJECT,
REFERRABLE, MULTILANGUAGE-REFERRABLE, IDENTIFIABLE, DDS-CP-PARTITION — the helper calls
readIdentifiable once for the inherited levels and reads its own group member PARTITION-NAME).

Round-trip counterpart: tests/test_armodel/writer/test_writer_dds_cp_partition.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DdsCpPartition

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<DDS-CP-PARTITION xmlns='{NS}'>{inner}</DDS-CP-PARTITION>")


class TestReadDdsCpPartition:
    """Tests for readDdsCpPartition — own group field values (Table 6.178)."""

    def _read(self, parser, inner):
        partition = DdsCpPartition(AUTOSAR.getInstance(), "Partition1")
        parser.readDdsCpPartition(_snip(inner), partition)
        return partition

    def test_read_sets_partition_name(self, parser):
        """Test that PARTITION-NAME is read with its value."""
        partition = self._read(parser, "<PARTITION-NAME>Partition_A</PARTITION-NAME>")
        assert partition.getShortName() == "Partition1"
        assert partition.getPartitionName() is not None
        assert partition.getPartitionName().getValue() == "Partition_A"

    def test_read_default_partition_wildcard(self, parser):
        """Test that the '*' default-partition name round-trips (spec Note, Table 6.178)."""
        partition = self._read(parser, "<PARTITION-NAME>*</PARTITION-NAME>")
        assert partition.getPartitionName().getValue() == "*"

    def test_read_empty(self, parser):
        """Test that the absent element leaves the field None."""
        partition = self._read(parser, "")
        assert partition.getPartitionName() is None
