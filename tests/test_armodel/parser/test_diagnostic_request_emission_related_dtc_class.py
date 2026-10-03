"""
Tests for reading the DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-CLASS element —
DiagnosticRequestEmissionRelatedDTCClass, Table 4.136 (p.154, R23-11).

DiagnosticRequestEmissionRelatedDTCClass (Base most-derived
DiagnosticServiceClass, concrete) defines no own attributes — the R23-11 table's
attribute row is `-` and XSD group
DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-CLASS, AUTOSAR_00052.xsd l.41926, is an
empty sequence. Only the IDENTIFIABLE wrapper is read. The dispatch entry is
readARPackageElementsRest → readDiagnosticRequestEmissionRelatedDTCClass via the
ARPackage create factory.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_request_emission_related_dtc_class.py
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticRequestEmissionRelatedDTCClass
from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticRequestEmissionRelatedDTCClass:
    """Tests for readDiagnosticRequestEmissionRelatedDTCClass — own element field values (Table 4.136)."""

    def _read(self, parser, inner):
        request_emission_related_dtc_class = DiagnosticRequestEmissionRelatedDTCClass(AUTOSAR.getInstance(), "Red1")
        element = _snip(inner, root_tag="DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-CLASS")
        parser.readDiagnosticRequestEmissionRelatedDTCClass(element, request_emission_related_dtc_class)
        return request_emission_related_dtc_class

    def test_read_identifiable_wrapper(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name comes from the dispatch constructor)."""
        request_emission_related_dtc_class = self._read(parser, "<SHORT-NAME>Red1</SHORT-NAME>")
        assert request_emission_related_dtc_class.getShortName() == "Red1"

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving the element valid."""
        request_emission_related_dtc_class = self._read(parser, "")
        assert request_emission_related_dtc_class.getShortName() == "Red1"

    def test_arpackage_dispatch_reads_element(self, parser):
        """Test that readARPackageElementsRest dispatches DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-CLASS through the ARPackage create factory."""
        package = AUTOSAR.getInstance().createARPackage("OBDMode0307Classes")
        element = _snip("<SHORT-NAME>Red1</SHORT-NAME>", root_tag="DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-CLASS")
        parser.readARPackageElementsRest("DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-CLASS", element, package)
        assert package.getReferrableElement("Red1", DiagnosticRequestEmissionRelatedDTCClass) is not None
