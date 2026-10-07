"""
Tests for reading DDS-LIFESPAN elements — DdsLifespan, Table 6.195 (p.536, R23-11).

The class is a nested non-top-level element (aggregated by DdsCpQosProfile.lifespan as the
<LIFESPAN> element), so the reusable helper readDdsLifespan is exercised directly on a standalone
XML subtree (XSD group DDS-LIFESPAN, AUTOSAR_00052.xsd l.29768: AR-OBJECT group + attributeGroup —
S/T round-trip; group member LIFESPAN-DURATION typed AR:FLOAT).

Round-trip counterpart: tests/test_armodel/writer/test_writer_dds_lifespan.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DdsLifespan

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<LIFESPAN xmlns='{NS}'>{inner}</LIFESPAN>")


class TestReadDdsLifespan:
    """Tests for readDdsLifespan — own group field values (Table 6.195)."""

    def _read(self, parser, inner):
        lifespan = DdsLifespan()
        parser.readDdsLifespan(_snip(inner), lifespan)
        return lifespan

    def test_read_sets_member(self, parser):
        """Test that the group member is read with its value."""
        lifespan = self._read(parser, "<LIFESPAN-DURATION>10.0</LIFESPAN-DURATION>")
        assert lifespan.getLifespanDuration() is not None
        assert lifespan.getLifespanDuration().getValue() == 10.0

    def test_read_empty(self, parser):
        """Test that the absent member leaves the field None."""
        lifespan = self._read(parser, "")
        assert lifespan.getLifespanDuration() is None

    def test_read_ar_object_attributes(self, parser):
        """Test that the AR-OBJECT attributeGroup (S/T) is read via the base helper."""
        element = ET.fromstring("<LIFESPAN xmlns='%s' S='5' T='2025-04-04T00:00:00Z'><LIFESPAN-DURATION>2.5</LIFESPAN-DURATION></LIFESPAN>" % NS)
        lifespan = DdsLifespan()
        parser.readDdsLifespan(element, lifespan)
        assert lifespan.getChecksum() is not None
        assert lifespan.getChecksum().getValue() == "5"
        assert lifespan.getTimestamp() is not None
        assert lifespan.getTimestamp().getValue() == "2025-04-04T00:00:00Z"
        assert lifespan.getLifespanDuration().getValue() == 2.5
