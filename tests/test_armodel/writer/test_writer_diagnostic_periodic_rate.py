"""
Tests for writing DIAGNOSTIC-PERIODIC-RATE elements —
DiagnosticPeriodicRate, Table 4.99 (p.131, R23-11).

DiagnosticPeriodicRate (concrete ARObject, Aggregated by
DiagnosticReadDataByPeriodicIDClass.periodicRate) defines two 0..1 attributes:
period (PERIOD) and periodicRateCategory (PERIODIC-RATE-CATEGORY) —
AUTOSAR_00052.xsd group DIAGNOSTIC-PERIODIC-RATE l.40879 / complexType l.40901.
The reusable writeDiagnosticPeriodicRate helper is verified directly; the
aggregator dispatch is wired with the DiagnosticReadDataByPeriodicIDClass pass.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_periodic_rate.py
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticPeriodicRate
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DiagnosticPeriodicRateCategoryEnum,
    TimeValue,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestWriteDiagnosticPeriodicRate:
    """Tests for writeDiagnosticPeriodicRate — own element field values (Table 4.99)."""

    def _write(self, rate: DiagnosticPeriodicRate) -> ET.Element:
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticPeriodicRate(parent, rate)
        return parent.find("DIAGNOSTIC-PERIODIC-RATE")

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticPeriodicRate without attributes emits an empty DIAGNOSTIC-PERIODIC-RATE element."""
        rate = DiagnosticPeriodicRate()

        child = self._write(rate)
        assert child is not None
        assert len(child) == 0

    def test_write_period(self):
        """Test that the PERIOD is emitted from period."""
        rate = DiagnosticPeriodicRate()
        period = TimeValue()
        period.setValue(0.5)
        rate.setPeriod(period)

        child = self._write(rate)
        assert child is not None
        element = child.find("PERIOD")
        assert element is not None
        assert element.text == "0.5"

    def test_write_periodic_rate_category(self):
        """Test that the PERIODIC-RATE-CATEGORY is emitted as its enum XML token."""
        rate = DiagnosticPeriodicRate()
        rate.setPeriodicRateCategory(DiagnosticPeriodicRateCategoryEnum().setValue(DiagnosticPeriodicRateCategoryEnum.PERIODIC_RATE_FAST))

        child = self._write(rate)
        assert child is not None
        element = child.find("PERIODIC-RATE-CATEGORY")
        assert element is not None
        assert element.text == "PERIODIC-RATE-FAST"

    def test_write_children_follow_xsd_sequence(self):
        """Test that the children are emitted in XSD sequence order (PERIOD, PERIODIC-RATE-CATEGORY)."""
        rate = DiagnosticPeriodicRate()
        rate.setPeriodicRateCategory(DiagnosticPeriodicRateCategoryEnum().setValue(DiagnosticPeriodicRateCategoryEnum.PERIODIC_RATE_SLOW))
        period = TimeValue()
        period.setValue(1.0)
        rate.setPeriod(period)

        child = self._write(rate)
        assert [c.tag for c in child] == ["PERIOD", "PERIODIC-RATE-CATEGORY"]

    def test_round_trip_preserves_field_values(self):
        """Test the full write → re-read cycle preserving the field values (nested ARObject — no document dispatch)."""
        rate = DiagnosticPeriodicRate()
        period = TimeValue()
        period.setValue(0.5)
        rate.setPeriod(period)
        rate.setPeriodicRateCategory(DiagnosticPeriodicRateCategoryEnum().setValue(DiagnosticPeriodicRateCategoryEnum.PERIODIC_RATE_MEDIUM))

        root = self._write(rate)
        wrapped = ET.fromstring("<PARENT xmlns='http://autosar.org/schema/r4.0'>%s</PARENT>" % ET.tostring(root, encoding="unicode"))

        parser = ARXMLParser()
        parser.detectNamespace(wrapped)
        rate_2 = DiagnosticPeriodicRate()
        parser.readDiagnosticPeriodicRate(wrapped.find("{http://autosar.org/schema/r4.0}DIAGNOSTIC-PERIODIC-RATE"), rate_2)
        assert rate_2.getPeriod() is not None
        assert rate_2.getPeriod().getValue() == 0.5
        assert rate_2.getPeriodicRateCategory() is not None
        assert rate_2.getPeriodicRateCategory().getValue() == "periodicRateMedium"
