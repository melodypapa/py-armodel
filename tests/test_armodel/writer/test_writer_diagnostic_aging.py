"""
Tests for writing DIAGNOSTIC-AGING elements —
DiagnosticAging, Table 4.198 (p.202, R23-11).

DiagnosticAging (Base most-derived ARElement) carries two 0..1 attributes —
agingCycle (ref, XSD wrapper AGING-CYCLES/DIAGNOSTIC-OPERATION-CYCLE-REF-CONDITIONAL/
DIAGNOSTIC-OPERATION-CYCLE-REF) and threshold (attr, XSD element THRESHOLD of type
POSITIVE-INTEGER-VALUE-VARIATION-POINT, value carried as element text) — XSD group
DIAGNOSTIC-AGING, AUTOSAR_00052.xsd l.31615. The writer reads the model via the
get* getters; the dispatch entry is writeARPackageElement → writeDiagnosticAging.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_aging.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticAging
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _aging_cycle_ref() -> RefType:
    ref = RefType()
    ref.setDest("DIAGNOSTIC-OPERATION-CYCLE")
    ref.setValue("/AUTOSAR/DiagnosticOperationCycles/Cycle1")
    return ref


def _threshold(value: str) -> PositiveInteger:
    threshold = PositiveInteger()
    threshold.setValue(value)
    return threshold


class TestWriteDiagnosticAging:
    """Tests for writeDiagnosticAging — own element field values (Table 4.198)."""

    def test_write_field_values_in_xsd_order(self):
        """Test that AGING-CYCLES and THRESHOLD are emitted with field values in XSD order."""
        package = AUTOSAR.getInstance().createARPackage("Agings")
        aging = package.createDiagnosticAging("Aging1")
        aging.setAgingCycleRef(_aging_cycle_ref())
        aging.setThreshold(_threshold("5"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticAging(parent, aging)

        child = parent.find("DIAGNOSTIC-AGING")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Aging1"
        assert child.find("AGING-CYCLES/DIAGNOSTIC-OPERATION-CYCLE-REF-CONDITIONAL/DIAGNOSTIC-OPERATION-CYCLE-REF").text == "/AUTOSAR/DiagnosticOperationCycles/Cycle1"
        ref_element = child.find("AGING-CYCLES/DIAGNOSTIC-OPERATION-CYCLE-REF-CONDITIONAL/DIAGNOSTIC-OPERATION-CYCLE-REF")
        assert ref_element.get("DEST") == "DIAGNOSTIC-OPERATION-CYCLE"
        assert child.find("THRESHOLD").text == "5"
        tags = [c.tag for c in child if c.tag != "SHORT-NAME"]
        assert tags == ["AGING-CYCLES", "THRESHOLD"]

    def test_write_unset_fields_omits_tags(self):
        """Test that unset fields emit no elements beyond SHORT-NAME (no empty AGING-CYCLES wrapper)."""
        package = AUTOSAR.getInstance().createARPackage("Agings")
        package.createDiagnosticAging("Aging1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticAging(parent, package.getReferrableElement("Aging1", DiagnosticAging))

        child = parent.find("DIAGNOSTIC-AGING")
        assert child is not None
        assert [c.tag for c in child] == ["SHORT-NAME"]
        assert child.find("AGING-CYCLES") is None
        assert child.find("THRESHOLD") is None

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticAging to a DIAGNOSTIC-AGING element."""
        package = AUTOSAR.getInstance().createARPackage("Agings")
        aging = package.createDiagnosticAging("Aging1")
        aging.setThreshold(_threshold("5"))

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, aging)

        child = parent.find("DIAGNOSTIC-AGING")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Aging1"
        assert child.find("THRESHOLD").text == "5"

    def test_round_trip(self):
        """Test the full set → save → reload → assert cycle over an ARPackage with field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("Agings")
        aging = package.createDiagnosticAging("Aging1")
        aging.setAgingCycleRef(_aging_cycle_ref())
        aging.setThreshold(_threshold("5"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            aging_2 = package_2.getReferrableElement("Aging1", DiagnosticAging)
            assert aging_2 is not None
            assert aging_2.getAgingCycleRef() is not None
            assert aging_2.getAgingCycleRef().getDest() == "DIAGNOSTIC-OPERATION-CYCLE"
            assert aging_2.getAgingCycleRef().getValue() == "/AUTOSAR/DiagnosticOperationCycles/Cycle1"
            assert aging_2.getThreshold() is not None
            assert aging_2.getThreshold().getValue() == 5
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_empty(self):
        """Test that a DiagnosticAging without field values round-trips with all fields empty."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("Agings")
        package.createDiagnosticAging("Aging1")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            aging_2 = package_2.getReferrableElement("Aging1", DiagnosticAging)
            assert aging_2 is not None
            assert aging_2.getAgingCycleRef() is None
            assert aging_2.getThreshold() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
