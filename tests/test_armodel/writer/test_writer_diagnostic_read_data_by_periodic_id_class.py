"""
Tests for writing DIAGNOSTIC-READ-DATA-BY-PERIODIC-ID-CLASS elements —
DiagnosticReadDataByPeriodicIDClass, Table 4.98 (p.130, R23-11).

DiagnosticReadDataByPeriodicIDClass (concrete DiagnosticServiceClass, Aggregated
by ARPackage.element) defines three attributes in displayed order:
maxPeriodicDidToRead (MAX-PERIODIC-DID-TO-READ), periodicRate (PERIODIC-RATES
wrapper of DIAGNOSTIC-PERIODIC-RATE) and schedulerMaxNumber
(SCHEDULER-MAX-NUMBER) — AUTOSAR_00052.xsd group
DIAGNOSTIC-READ-DATA-BY-PERIODIC-ID-CLASS l.41290 / complexType l.41323.
The writer emits the children in XSD sequence order. The dispatch entry is
writeARPackageElement → writeDiagnosticReadDataByPeriodicIDClass.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_read_data_by_periodic_id_class.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticReadDataByPeriodicIDClass
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticPeriodicRate
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DiagnosticPeriodicRateCategoryEnum,
    PositiveInteger,
    TimeValue,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _rate(period_value, category_value) -> DiagnosticPeriodicRate:
    rate = DiagnosticPeriodicRate()
    if period_value is not None:
        period = TimeValue()
        period.setValue(period_value)
        rate.setPeriod(period)
    if category_value is not None:
        rate.setPeriodicRateCategory(DiagnosticPeriodicRateCategoryEnum().setValue(category_value))
    return rate


class TestWriteDiagnosticReadDataByPeriodicIDClass:
    """Tests for writeDiagnosticReadDataByPeriodicIDClass — own element field values (Table 4.98)."""

    def _write(self, cls: DiagnosticReadDataByPeriodicIDClass) -> ET.Element:
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticReadDataByPeriodicIDClass(parent, cls)
        return parent.find("DIAGNOSTIC-READ-DATA-BY-PERIODIC-ID-CLASS")

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticReadDataByPeriodicIDClass without attributes emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticReadDataByPeriodicIds")
        package.createDiagnosticReadDataByPeriodicIDClass("Rdbpidc1")

        child = self._write(package.getReferrableElement("Rdbpidc1", DiagnosticReadDataByPeriodicIDClass))
        assert child is not None
        assert child.find("SHORT-NAME").text == "Rdbpidc1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_max_periodic_did_to_read(self):
        """Test that the MAX-PERIODIC-DID-TO-READ is emitted from maxPeriodicDidToRead."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticReadDataByPeriodicIds")
        cls = package.createDiagnosticReadDataByPeriodicIDClass("Rdbpidc1")
        cls.setMaxPeriodicDidToRead(PositiveInteger().setValue("42"))

        child = self._write(cls)
        assert child is not None
        element = child.find("MAX-PERIODIC-DID-TO-READ")
        assert element is not None
        assert element.text == "42"

    def test_write_periodic_rates(self):
        """Test that the PERIODIC-RATES wrapper emits one DIAGNOSTIC-PERIODIC-RATE per aggregated rate."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticReadDataByPeriodicIds")
        cls = package.createDiagnosticReadDataByPeriodicIDClass("Rdbpidc1")
        cls.addPeriodicRate(_rate(0.5, DiagnosticPeriodicRateCategoryEnum.PERIODIC_RATE_FAST))
        cls.addPeriodicRate(_rate(None, DiagnosticPeriodicRateCategoryEnum.PERIODIC_RATE_SLOW))

        child = self._write(cls)
        assert child is not None
        rates_wrapper = child.find("PERIODIC-RATES")
        assert rates_wrapper is not None
        rates = rates_wrapper.findall("DIAGNOSTIC-PERIODIC-RATE")
        assert len(rates) == 2
        assert rates[0].find("PERIOD").text == "0.5"
        assert rates[0].find("PERIODIC-RATE-CATEGORY").text == "PERIODIC-RATE-FAST"
        assert rates[1].find("PERIOD") is None
        assert rates[1].find("PERIODIC-RATE-CATEGORY").text == "PERIODIC-RATE-SLOW"

    def test_write_scheduler_max_number(self):
        """Test that the SCHEDULER-MAX-NUMBER is emitted from schedulerMaxNumber."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticReadDataByPeriodicIds")
        cls = package.createDiagnosticReadDataByPeriodicIDClass("Rdbpidc1")
        cls.setSchedulerMaxNumber(PositiveInteger().setValue("3"))

        child = self._write(cls)
        assert child is not None
        element = child.find("SCHEDULER-MAX-NUMBER")
        assert element is not None
        assert element.text == "3"

    def test_write_children_follow_xsd_sequence(self):
        """Test that the children are emitted in XSD sequence order (MAX-PERIODIC-DID-TO-READ, PERIODIC-RATES, SCHEDULER-MAX-NUMBER)."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticReadDataByPeriodicIds")
        cls = package.createDiagnosticReadDataByPeriodicIDClass("Rdbpidc1")
        cls.setSchedulerMaxNumber(PositiveInteger().setValue("3"))
        cls.addPeriodicRate(_rate(0.5, DiagnosticPeriodicRateCategoryEnum.PERIODIC_RATE_MEDIUM))
        cls.setMaxPeriodicDidToRead(PositiveInteger().setValue("42"))

        child = self._write(cls)
        assert [c.tag for c in child if c.tag != "SHORT-NAME"] == ["MAX-PERIODIC-DID-TO-READ", "PERIODIC-RATES", "SCHEDULER-MAX-NUMBER"]

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticReadDataByPeriodicIDClass to a DIAGNOSTIC-READ-DATA-BY-PERIODIC-ID-CLASS element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticReadDataByPeriodicIds")
        package.createDiagnosticReadDataByPeriodicIDClass("Rdbpidc1")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, package.getReferrableElement("Rdbpidc1", DiagnosticReadDataByPeriodicIDClass))

        child = parent.find("DIAGNOSTIC-READ-DATA-BY-PERIODIC-ID-CLASS")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Rdbpidc1"

    def test_round_trip_preserves_field_values(self):
        """Test the full create → save → reload → assert cycle preserving the field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticReadDataByPeriodicIds")
        cls = package.createDiagnosticReadDataByPeriodicIDClass("Rdbpidc1")
        cls.setMaxPeriodicDidToRead(PositiveInteger().setValue("42"))
        cls.addPeriodicRate(_rate(0.5, DiagnosticPeriodicRateCategoryEnum.PERIODIC_RATE_FAST))
        cls.addPeriodicRate(_rate(None, DiagnosticPeriodicRateCategoryEnum.PERIODIC_RATE_SLOW))
        cls.setSchedulerMaxNumber(PositiveInteger().setValue("3"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            cls_2 = package_2.getReferrableElement("Rdbpidc1", DiagnosticReadDataByPeriodicIDClass)
            assert cls_2 is not None
            assert cls_2.getShortName() == "Rdbpidc1"
            assert cls_2.getMaxPeriodicDidToRead() is not None
            assert cls_2.getMaxPeriodicDidToRead().getValue() == 42
            rates = cls_2.getPeriodicRates()
            assert len(rates) == 2
            assert rates[0].getPeriod().getValue() == 0.5
            assert rates[0].getPeriodicRateCategory().getValue() == DiagnosticPeriodicRateCategoryEnum.PERIODIC_RATE_FAST
            assert rates[1].getPeriod() is None
            assert rates[1].getPeriodicRateCategory().getValue() == DiagnosticPeriodicRateCategoryEnum.PERIODIC_RATE_SLOW
            assert cls_2.getSchedulerMaxNumber() is not None
            assert cls_2.getSchedulerMaxNumber().getValue() == 3
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
