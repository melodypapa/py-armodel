"""
Tests for reading DDS-DEADLINE elements — DdsDeadline, Table 6.185 (p.532, R23-11).

The class is a nested non-top-level element (aggregated by DdsCpQosProfile.deadline as the
<DEADLINE> element), so the reusable helper readDdsDeadline is exercised directly on a
standalone XML subtree (XSD group DDS-DEADLINE, AUTOSAR_00052.xsd l.29346: AR-OBJECT group +
attributeGroup — S/T round-trip; group member DEADLINE-PERIOD typed AR:FLOAT).

Round-trip counterpart: tests/test_armodel/writer/test_writer_dds_deadline.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DdsDeadline

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<DEADLINE xmlns='{NS}'>{inner}</DEADLINE>")


class TestReadDdsDeadline:
    """Tests for readDdsDeadline — own group field values (Table 6.185)."""

    def _read(self, parser, inner):
        deadline = DdsDeadline()
        parser.readDdsDeadline(_snip(inner), deadline)
        return deadline

    def test_read_sets_deadline_period(self, parser):
        """Test that the DEADLINE-PERIOD float member is read with its value."""
        deadline = self._read(parser, "<DEADLINE-PERIOD>0.5</DEADLINE-PERIOD>")
        assert deadline.getDeadlinePeriod() is not None
        assert deadline.getDeadlinePeriod().getValue() == 0.5

    def test_read_empty(self, parser):
        """Test that an absent member leaves the field None."""
        deadline = self._read(parser, "")
        assert deadline.getDeadlinePeriod() is None

    def test_read_ar_object_attributes(self, parser):
        """Test that the AR-OBJECT attributeGroup (S/T) is read via the base helper."""
        element = ET.fromstring("<DEADLINE xmlns='%s' S='5' T='2025-04-04T00:00:00Z'><DEADLINE-PERIOD>1.0</DEADLINE-PERIOD></DEADLINE>" % NS)
        deadline = DdsDeadline()
        parser.readDdsDeadline(element, deadline)
        assert deadline.getChecksum() is not None
        assert deadline.getChecksum().getValue() == "5"
        assert deadline.getTimestamp() is not None
        assert deadline.getTimestamp().getValue() == "2025-04-04T00:00:00Z"
        assert deadline.getDeadlinePeriod().getValue() == 1.0
