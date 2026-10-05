"""
Tests for writing DIAGNOSTIC-MEASUREMENT-IDENTIFIER elements —
DiagnosticMeasurementIdentifier, Table 4.204 (p.206, R23-11).

The XSD group DIAGNOSTIC-MEASUREMENT-IDENTIFIER (AUTOSAR_00052.xsd l.39378)
fixes the element structure: the optional OBD-MID element
(POSITIVE-INTEGER-VALUE-VARIATION-POINT, mixed content) is the only own child
after the Identifiable groups; it is emitted only when obdMid is present. The
markdown Type column PositiveInteger wins over the XSD element type (Rule
0015); the value round-trips flattened as the OBD-MID element text
(DiagnosticAging THRESHOLD precedent).
The dispatch entry is writeARPackageElement → writeDiagnosticMeasurementIdentifier.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_measurement_identifier.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticMeasurementIdentifier
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset the AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticMeasurementIdentifier:
    """Tests for writeDiagnosticMeasurementIdentifier — own element field values (Table 4.204)."""

    def _make_identifier(self, short_name: str = "MeasurementIdentifier1") -> DiagnosticMeasurementIdentifier:
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMeasurementIdentifiers")
        return package.createDiagnosticMeasurementIdentifier(short_name)

    def _populate(self, identifier: DiagnosticMeasurementIdentifier) -> DiagnosticMeasurementIdentifier:
        obd_mid = PositiveInteger()
        obd_mid.setValue(300)
        identifier.setObdMid(obd_mid)
        return identifier

    def test_write_obd_mid_element(self):
        """Test that a populated obdMid is emitted as the OBD-MID element after SHORT-NAME with the spec value."""
        identifier = self._populate(self._make_identifier())

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticMeasurementIdentifier(parent, identifier)

        child = parent.find("DIAGNOSTIC-MEASUREMENT-IDENTIFIER")
        assert child is not None
        assert [c.tag for c in child] == ["SHORT-NAME", "OBD-MID"]
        assert child.find("OBD-MID").text == "300"

    def test_write_unset_own_field_emits_no_obd_mid(self):
        """Test that an unpopulated identifier emits no OBD-MID element (empty wrapper case)."""
        self._make_identifier()

        parent = ET.Element("PARENT")
        identifier = AUTOSAR.getInstance().getARPackages()[0].getReferrableElement("MeasurementIdentifier1", DiagnosticMeasurementIdentifier)
        ARXMLWriter().writeDiagnosticMeasurementIdentifier(parent, identifier)

        child = parent.find("DIAGNOSTIC-MEASUREMENT-IDENTIFIER")
        assert child is not None
        assert [c.tag for c in child] == ["SHORT-NAME"]
        assert child.find("OBD-MID") is None

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticMeasurementIdentifier to a DIAGNOSTIC-MEASUREMENT-IDENTIFIER element."""
        identifier = self._populate(self._make_identifier())

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, identifier)

        child = parent.find("DIAGNOSTIC-MEASUREMENT-IDENTIFIER")
        assert child is not None
        assert child.find("SHORT-NAME").text == "MeasurementIdentifier1"
        assert child.find("OBD-MID").text == "300"

    def test_round_trip_preserves_field_values(self):
        """Test the full set → save → reload → assert cycle over an ARPackage with field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticMeasurementIdentifiers")
        self._populate(package.createDiagnosticMeasurementIdentifier("MeasurementIdentifier1"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            identifier_2 = package_2.getReferrableElement("MeasurementIdentifier1", DiagnosticMeasurementIdentifier)
            assert identifier_2 is not None
            assert identifier_2.getShortName() == "MeasurementIdentifier1"
            obd_mid = identifier_2.getObdMid()
            assert obd_mid is not None
            assert obd_mid.value == 300
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_empty(self):
        """Test that a DiagnosticMeasurementIdentifier without own fields round-trips with obdMid None."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticMeasurementIdentifiers")
        package.createDiagnosticMeasurementIdentifier("MeasurementIdentifier1")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            identifier_2 = package_2.getReferrableElement("MeasurementIdentifier1", DiagnosticMeasurementIdentifier)
            assert identifier_2 is not None
            assert identifier_2.getObdMid() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
