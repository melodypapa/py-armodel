"""
Writer tests for DDS-LATENCY-BUDGET elements — DdsLatencyBudget, Table 6.186 (p.532, R23-11).

writeDdsLatencyBudget emits <LATENCY-BUDGET> (the object element, per the
DdsCpQosProfile.latencyBudget aggregation) with the AR-OBJECT S/T attributes and the
LATENCY-BUDGET-DURATION member (XSD group DDS-LATENCY-BUDGET, AUTOSAR_00052.xsd l.29737).

Round-trip counterpart: tests/test_armodel/parser/test_dds_latency_budget.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DdsLatencyBudget
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, Float, String
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _new_latency_budget() -> DdsLatencyBudget:
    latency_budget = DdsLatencyBudget()
    latency_budget.setLatencyBudgetDuration(Float().setValue("0.1"))
    latency_budget.setChecksum(String().setValue("5"))
    latency_budget.setTimestamp(DateTime().setValue("2025-04-04T00:00:00Z"))
    return latency_budget


class TestWriteDdsLatencyBudget:
    def test_write_emits_element_and_member(self):
        """Test that the writer emits the object element with the LATENCY-BUDGET-DURATION member."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsLatencyBudget(parent, _new_latency_budget())
        node = parent.find("LATENCY-BUDGET")
        assert node is not None
        assert node.find("LATENCY-BUDGET-DURATION").text == "0.1"

    def test_write_emits_ar_object_attributes(self):
        """Test that the S/T attributeGroup is emitted via the base helper."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsLatencyBudget(parent, _new_latency_budget())
        node = parent.find("LATENCY-BUDGET")
        assert node.attrib["S"] == "5"
        assert node.attrib["T"] == "2025-04-04T00:00:00Z"

    def test_write_empty_omits_member(self):
        """Test that an empty object emits no member element."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsLatencyBudget(parent, DdsLatencyBudget())
        node = parent.find("LATENCY-BUDGET")
        assert node is not None
        assert node.find("LATENCY-BUDGET-DURATION") is None

    def test_round_trip_preserves_values(self):
        """Test the full write → parse round-trip preserves field values."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsLatencyBudget(parent, _new_latency_budget())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reloaded = DdsLatencyBudget()
        ARXMLParser().readDdsLatencyBudget(root.find("{%s}LATENCY-BUDGET" % NS), reloaded)
        assert reloaded.getLatencyBudgetDuration().getValue() == 0.1
        assert reloaded.getChecksum().getValue() == "5"
        assert reloaded.getTimestamp().getValue() == "2025-04-04T00:00:00Z"
