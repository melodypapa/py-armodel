"""
Tests for reading the DIAGNOSTIC-CUSTOM-SERVICE-CLASS element —
DiagnosticCustomServiceClass, Table 4.28 (p.71, R23-11).

DiagnosticCustomServiceClass (Base chain reaches DiagnosticServiceClass) carries
its own 0..1 CUSTOM-SERVICE-ID (PositiveInteger) — XSD group
DIAGNOSTIC-CUSTOM-SERVICE-CLASS, AUTOSAR_00052.xsd l.33976. The base group
DIAGNOSTIC-SERVICE-CLASS holds only an atp.Status="removed"
ACCESS-PERMISSION-REF (not modeled).

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_custom_service_class.py
"""

from unittest.mock import MagicMock

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticCustomServiceClass:
    """Tests for readDiagnosticCustomServiceClass — own element field values (Table 4.28)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticCustomServiceClass

        service_class = DiagnosticCustomServiceClass(parent=MagicMock(), short_name="Csc")
        element = _snip(inner, root_tag="DIAGNOSTIC-CUSTOM-SERVICE-CLASS")
        parser.readDiagnosticCustomServiceClass(element, service_class)
        return service_class

    def test_with_custom_service_id(self, parser):
        """Test that CUSTOM-SERVICE-ID is read into a PositiveInteger with the spec value."""
        inner = "<SHORT-NAME>Csc</SHORT-NAME><CUSTOM-SERVICE-ID>5</CUSTOM-SERVICE-ID>"
        service_class = self._read(parser, inner)
        assert service_class.getShortName() == "Csc"
        custom_service_id = service_class.getCustomServiceId()
        assert custom_service_id is not None
        assert custom_service_id.getValue() == 5

    def test_without_custom_service_id(self, parser):
        """Test that an absent CUSTOM-SERVICE-ID leaves customServiceId None."""
        service_class = self._read(parser, "<SHORT-NAME>Csc</SHORT-NAME>")
        assert service_class.getCustomServiceId() is None
