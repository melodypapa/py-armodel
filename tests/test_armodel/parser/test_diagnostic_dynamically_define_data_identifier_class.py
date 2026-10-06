"""
Tests for reading the DIAGNOSTIC-DYNAMICALLY-DEFINE-DATA-IDENTIFIER-CLASS element —
DiagnosticDynamicallyDefineDataIdentifierClass, Table 4.94 (p.128, R23-11).

DiagnosticDynamicallyDefineDataIdentifierClass (concrete DiagnosticServiceClass,
Aggregated by ARPackage.element) defines three attributes in displayed order:
checkPerSourceId (Boolean 0..1, CHECK-PER-SOURCE-ID), configurationHandling
(DiagnosticHandleDDDIConfigurationEnum 0..1, CONFIGURATION-HANDLING) and
subfunction (DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum *,
SUBFUNCTIONS wrapper of SUBFUNCTION enum tokens) — AUTOSAR_00052.xsd group
DIAGNOSTIC-DYNAMICALLY-DEFINE-DATA-IDENTIFIER-CLASS l.35199.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_dynamically_define_data_identifier_class.py
"""

from unittest.mock import MagicMock

from tests.test_armodel.parser._helpers import _snip
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DiagnosticHandleDDDIConfigurationEnum


class TestReadDiagnosticDynamicallyDefineDataIdentifierClass:
    """Tests for readDiagnosticDynamicallyDefineDataIdentifierClass — own element field values (Table 4.94)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticDynamicallyDefineDataIdentifierClass

        dddi_class = DiagnosticDynamicallyDefineDataIdentifierClass(parent=MagicMock(), short_name="Dddic1")
        element = _snip(inner, root_tag="DIAGNOSTIC-DYNAMICALLY-DEFINE-DATA-IDENTIFIER-CLASS")
        parser.readDiagnosticDynamicallyDefineDataIdentifierClass(element, dddi_class)
        return dddi_class

    def test_read_short_name(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name)."""
        dddi_class = self._read(parser, "<SHORT-NAME>Dddic1</SHORT-NAME>")
        assert dddi_class.getShortName() == "Dddic1"

    def test_read_check_per_source_id(self, parser):
        """Test that the CHECK-PER-SOURCE-ID is read into checkPerSourceId."""
        dddi_class = self._read(parser, "<CHECK-PER-SOURCE-ID>true</CHECK-PER-SOURCE-ID>")
        assert dddi_class.getCheckPerSourceId() is not None
        assert dddi_class.getCheckPerSourceId().getValue() is True

    def test_read_configuration_handling(self, parser):
        """Test that the CONFIGURATION-HANDLING enum token is read into configurationHandling."""
        dddi_class = self._read(parser, "<CONFIGURATION-HANDLING>NON-VOLATILE</CONFIGURATION-HANDLING>")
        assert dddi_class.getConfigurationHandling() is not None
        assert dddi_class.getConfigurationHandling().getValue() == DiagnosticHandleDDDIConfigurationEnum.NON_VOLATILE

    def test_read_subfunctions(self, parser):
        """Test that the SUBFUNCTIONS wrapper enum tokens are read in document order."""
        inner = "<SUBFUNCTIONS><SUBFUNCTION>DEFINE-BY-IDENTIFIER</SUBFUNCTION><SUBFUNCTION>CLEAR-DYNAMICALLY-DEFINE-DATA-IDENTIFIER</SUBFUNCTION><SUBFUNCTION>DEFINE-BY-MEMORY-ADDRESS</SUBFUNCTION></SUBFUNCTIONS>"
        dddi_class = self._read(parser, inner)
        values = [subfunction.getValue() for subfunction in dddi_class.getSubfunctions()]
        assert values == ["DEFINE-BY-IDENTIFIER", "CLEAR-DYNAMICALLY-DEFINE-DATA-IDENTIFIER", "DEFINE-BY-MEMORY-ADDRESS"]

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving all fields unset."""
        dddi_class = self._read(parser, "<SHORT-NAME>Dddic1</SHORT-NAME>")
        assert dddi_class.getCheckPerSourceId() is None
        assert dddi_class.getConfigurationHandling() is None
        assert dddi_class.getSubfunctions() == []
