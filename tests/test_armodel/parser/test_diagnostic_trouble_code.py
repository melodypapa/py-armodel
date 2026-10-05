"""
Tests for reading the DIAGNOSTIC-TROUBLE-CODE element —
DiagnosticTroubleCode, Table 4.161 (p.176, R23-11).

DiagnosticTroubleCode is abstract and carries no Attribute rows — its XSD group
DIAGNOSTIC-TROUBLE-CODE (AUTOSAR_00052.xsd l.46194) is an empty sequence, so the
reader is readDiagnosticTroubleCode = readIdentifiable and the concrete subclass
readDiagnosticTroubleCodeJ1939 reuses it for the shared IDENTIFIABLE content.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_trouble_code.py
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticTroubleCode:
    """Tests for readDiagnosticTroubleCode — own element field values (Table 4.161)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticTroubleCode

        trouble_code = DiagnosticTroubleCode(AUTOSAR.getInstance(), "TroubleCode1")
        parser.readDiagnosticTroubleCode(_snip(inner, root_tag="DIAGNOSTIC-TROUBLE-CODE"), trouble_code)
        return trouble_code

    def test_read_sets_short_name(self, parser):
        """Test that the IDENTIFIABLE SHORT-NAME is read into the short name."""
        trouble_code = self._read(parser, "<SHORT-NAME>TroubleCode1</SHORT-NAME>")
        assert trouble_code.getShortName() == "TroubleCode1"

    def test_read_sets_category(self, parser):
        """Test that the inherited IDENTIFIABLE CATEGORY is read into category."""
        trouble_code = self._read(parser, "<SHORT-NAME>TroubleCode1</SHORT-NAME><CATEGORY>TROUBLE_CODE</CATEGORY>")
        assert trouble_code.getCategory() is not None
        assert trouble_code.getCategory().getValue() == "TROUBLE_CODE"

    def test_read_empty_wrapper_leaves_category_none(self, parser):
        """Test that an element without optional IDENTIFIABLE children leaves them None (empty wrapper case)."""
        trouble_code = self._read(parser, "<SHORT-NAME>TroubleCode1</SHORT-NAME>")
        assert trouble_code.getCategory() is None
