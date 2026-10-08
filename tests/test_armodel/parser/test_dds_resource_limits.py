"""
Tests for reading RESOURCE-LIMITS elements — DdsResourceLimits, Table 6.200 (p.538, R23-11).

The class is a nested ARObject QoS policy (aggregated by DdsCpQosProfile.resourceLimits,
Table 6.179), so the reusable helper readDdsResourceLimits is exercised directly on a
standalone XML subtree (XSD complexType DDS-RESOURCE-LIMITS, AUTOSAR_00052.xsd l.30132:
AR-OBJECT attributeGroup — S/T round-trip; group members MAX-INSTANCES, MAX-SAMPLES,
MAX-SAMPLES-PER-INSTANCE in xml.sequenceOffset order).

Round-trip counterpart: tests/test_armodel/writer/test_writer_dds_resource_limits.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DdsResourceLimits

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<RESOURCE-LIMITS xmlns='{NS}'>{inner}</RESOURCE-LIMITS>")


class TestReadDdsResourceLimits:
    """Tests for readDdsResourceLimits — own group field values (Table 6.200)."""

    def _read(self, parser, inner):
        resource_limits = DdsResourceLimits()
        parser.readDdsResourceLimits(_snip(inner), resource_limits)
        return resource_limits

    def test_read_sets_all_fields(self, parser):
        """Test that the three members are read with their values in XSD order."""
        resource_limits = self._read(
            parser,
            "<MAX-INSTANCES>1</MAX-INSTANCES>" "<MAX-SAMPLES>2</MAX-SAMPLES>" "<MAX-SAMPLES-PER-INSTANCE>4</MAX-SAMPLES-PER-INSTANCE>",
        )
        assert resource_limits.getMaxInstances() is not None
        assert resource_limits.getMaxInstances().getValue() == 1
        assert resource_limits.getMaxSamples() is not None
        assert resource_limits.getMaxSamples().getValue() == 2
        assert resource_limits.getMaxSamplesPerInstance() is not None
        assert resource_limits.getMaxSamplesPerInstance().getValue() == 4

    def test_read_empty(self, parser):
        """Test that absent elements leave the fields None."""
        resource_limits = self._read(parser, "")
        assert resource_limits.getMaxInstances() is None
        assert resource_limits.getMaxSamples() is None
        assert resource_limits.getMaxSamplesPerInstance() is None

    def test_read_ar_object_attributes(self, parser):
        """Test that the AR-OBJECT attributeGroup (S/T) is read via the base helper (Rule 0025)."""
        element = ET.fromstring("<RESOURCE-LIMITS xmlns='%s' S='7' T='2025-05-05T00:00:00Z'/>" % NS)
        resource_limits = DdsResourceLimits()
        parser.readDdsResourceLimits(element, resource_limits)
        assert resource_limits.getChecksum() is not None
        assert resource_limits.getChecksum().getValue() == "7"
        assert resource_limits.getTimestamp() is not None
        assert resource_limits.getTimestamp().getValue() == "2025-05-05T00:00:00Z"
