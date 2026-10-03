"""
Tests for reading the DIAGNOSTIC-CLEAR-RESET-EMISSION-RELATED-INFO-CLASS element —
DiagnosticClearResetEmissionRelatedInfoClass, Table 4.138 (p.155, R23-11).

DiagnosticClearResetEmissionRelatedInfoClass (Base most-derived
DiagnosticServiceClass, concrete) defines no own attributes — the R23-11 table's
attribute row is `-` and XSD group
DIAGNOSTIC-CLEAR-RESET-EMISSION-RELATED-INFO-CLASS, AUTOSAR_00052.xsd l.32479, is
an empty sequence. Only the IDENTIFIABLE wrapper is read. The dispatch entry is
readARPackageElementsRest → readDiagnosticClearResetEmissionRelatedInfoClass via
the ARPackage create factory.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_clear_reset_emission_related_info_class.py
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticClearResetEmissionRelatedInfoClass
from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticClearResetEmissionRelatedInfoClass:
    """Tests for readDiagnosticClearResetEmissionRelatedInfoClass — own element field values (Table 4.138)."""

    def _read(self, parser, inner):
        clear_reset_emission_related_info_class = DiagnosticClearResetEmissionRelatedInfoClass(AUTOSAR.getInstance(), "Cre1")
        element = _snip(inner, root_tag="DIAGNOSTIC-CLEAR-RESET-EMISSION-RELATED-INFO-CLASS")
        parser.readDiagnosticClearResetEmissionRelatedInfoClass(element, clear_reset_emission_related_info_class)
        return clear_reset_emission_related_info_class

    def test_read_identifiable_wrapper(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name comes from the dispatch constructor)."""
        clear_reset_emission_related_info_class = self._read(parser, "<SHORT-NAME>Cre1</SHORT-NAME>")
        assert clear_reset_emission_related_info_class.getShortName() == "Cre1"

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving the element valid."""
        clear_reset_emission_related_info_class = self._read(parser, "")
        assert clear_reset_emission_related_info_class.getShortName() == "Cre1"

    def test_arpackage_dispatch_reads_element(self, parser):
        """Test that readARPackageElementsRest dispatches DIAGNOSTIC-CLEAR-RESET-EMISSION-RELATED-INFO-CLASS through the ARPackage create factory."""
        package = AUTOSAR.getInstance().createARPackage("OBDMode04Classes")
        element = _snip("<SHORT-NAME>Cre1</SHORT-NAME>", root_tag="DIAGNOSTIC-CLEAR-RESET-EMISSION-RELATED-INFO-CLASS")
        parser.readARPackageElementsRest("DIAGNOSTIC-CLEAR-RESET-EMISSION-RELATED-INFO-CLASS", element, package)
        assert package.getReferrableElement("Cre1", DiagnosticClearResetEmissionRelatedInfoClass) is not None
