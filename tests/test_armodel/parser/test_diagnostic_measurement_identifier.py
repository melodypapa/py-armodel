"""
Tests for reading the DIAGNOSTIC-MEASUREMENT-IDENTIFIER element —
DiagnosticMeasurementIdentifier, Table 4.204 (p.206, R23-11).

DiagnosticMeasurementIdentifier (Base most-derived ARElement) carries one own
Attribute row: obdMid (kind attr, multiplicity 0..1). The markdown Type column
PositiveInteger wins over the XSD element type
POSITIVE-INTEGER-VALUE-VARIATION-POINT (Rule 0015); the value round-trips
flattened as the OBD-MID element text (XSD group DIAGNOSTIC-MEASUREMENT-IDENTIFIER,
AUTOSAR_00052.xsd l.39378, mixed content; DiagnosticAging THRESHOLD precedent).

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_measurement_identifier.py
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticMeasurementIdentifier:
    """Tests for readDiagnosticMeasurementIdentifier — own element field values (Table 4.204)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticMeasurementIdentifier

        identifier = DiagnosticMeasurementIdentifier(AUTOSAR.getInstance(), "MeasurementIdentifier1")
        parser.readDiagnosticMeasurementIdentifier(_snip(inner, root_tag="DIAGNOSTIC-MEASUREMENT-IDENTIFIER"), identifier)
        return identifier

    def test_read_sets_obd_mid(self, parser):
        """Test that the OBD-MID element text is read into obdMid as a PositiveInteger."""
        identifier = self._read(
            parser,
            "<SHORT-NAME>MeasurementIdentifier1</SHORT-NAME>" "<OBD-MID>300</OBD-MID>",
        )
        assert identifier.getShortName() == "MeasurementIdentifier1"
        obd_mid = identifier.getObdMid()
        assert obd_mid is not None
        assert obd_mid.value == 300

    def test_read_empty_obd_mid_element_leaves_none(self, parser):
        """Test that an empty OBD-MID element leaves obdMid None (empty wrapper case)."""
        identifier = self._read(parser, "<SHORT-NAME>MeasurementIdentifier1</SHORT-NAME><OBD-MID></OBD-MID>")
        assert identifier.getObdMid() is None

    def test_read_without_obd_mid_leaves_default(self, parser):
        """Test that an element without OBD-MID leaves obdMid None."""
        identifier = self._read(parser, "<SHORT-NAME>MeasurementIdentifier1</SHORT-NAME>")
        assert identifier.getObdMid() is None
