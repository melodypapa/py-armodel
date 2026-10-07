"""
Tests for reading DDS-LATENCY-BUDGET elements — DdsLatencyBudget, Table 6.186 (p.532, R23-11).

The class is a nested non-top-level element (aggregated by DdsCpQosProfile.latencyBudget as the
<LATENCY-BUDGET> element), so the reusable helper readDdsLatencyBudget is exercised directly on a
standalone XML subtree (XSD group DDS-LATENCY-BUDGET, AUTOSAR_00052.xsd l.29737: AR-OBJECT group +
attributeGroup — S/T round-trip; group member LATENCY-BUDGET-DURATION typed AR:FLOAT).

Round-trip counterpart: tests/test_armodel/writer/test_writer_dds_latency_budget.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DdsLatencyBudget

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<LATENCY-BUDGET xmlns='{NS}'>{inner}</LATENCY-BUDGET>")


class TestReadDdsLatencyBudget:
    """Tests for readDdsLatencyBudget — own group field values (Table 6.186)."""

    def _read(self, parser, inner):
        latency_budget = DdsLatencyBudget()
        parser.readDdsLatencyBudget(_snip(inner), latency_budget)
        return latency_budget

    def test_read_sets_latency_budget_duration(self, parser):
        """Test that the LATENCY-BUDGET-DURATION float member is read with its value."""
        latency_budget = self._read(parser, "<LATENCY-BUDGET-DURATION>0.1</LATENCY-BUDGET-DURATION>")
        assert latency_budget.getLatencyBudgetDuration() is not None
        assert latency_budget.getLatencyBudgetDuration().getValue() == 0.1

    def test_read_empty(self, parser):
        """Test that an absent member leaves the field None."""
        latency_budget = self._read(parser, "")
        assert latency_budget.getLatencyBudgetDuration() is None

    def test_read_ar_object_attributes(self, parser):
        """Test that the AR-OBJECT attributeGroup (S/T) is read via the base helper."""
        element = ET.fromstring("<LATENCY-BUDGET xmlns='%s' S='5' T='2025-04-04T00:00:00Z'><LATENCY-BUDGET-DURATION>0.2</LATENCY-BUDGET-DURATION></LATENCY-BUDGET>" % NS)
        latency_budget = DdsLatencyBudget()
        parser.readDdsLatencyBudget(element, latency_budget)
        assert latency_budget.getChecksum() is not None
        assert latency_budget.getChecksum().getValue() == "5"
        assert latency_budget.getTimestamp() is not None
        assert latency_budget.getTimestamp().getValue() == "2025-04-04T00:00:00Z"
        assert latency_budget.getLatencyBudgetDuration().getValue() == 0.2
