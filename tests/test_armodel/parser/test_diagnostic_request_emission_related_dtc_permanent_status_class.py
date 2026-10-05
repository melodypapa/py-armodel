"""
Tests for reading the DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-PERMANENT-STATUS-CLASS element —
DiagnosticRequestEmissionRelatedDTCPermanentStatusClass, Table 4.148 (p.162, R23-11).

DiagnosticRequestEmissionRelatedDTCPermanentStatusClass (Base most-derived
DiagnosticServiceClass, concrete) defines no own attributes — the R23-11 table's
attribute row is `-` and XSD group
DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-PERMANENT-STATUS-CLASS, AUTOSAR_00052.xsd
l.42009, is an empty sequence. Only the IDENTIFIABLE wrapper is read. The dispatch
entry is readARPackageElementsRest → readDiagnosticRequestEmissionRelatedDTCPermanentStatusClass
via the ARPackage create factory.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_request_emission_related_dtc_permanent_status_class.py
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticRequestEmissionRelatedDTCPermanentStatusClass
from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticRequestEmissionRelatedDTCPermanentStatusClass:
    """Tests for readDiagnosticRequestEmissionRelatedDTCPermanentStatusClass — own element field values (Table 4.148)."""

    def _read(self, parser, inner):
        request_emission_related_dtc_permanent_status_class = DiagnosticRequestEmissionRelatedDTCPermanentStatusClass(AUTOSAR.getInstance(), "Redps1")
        element = _snip(inner, root_tag="DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-PERMANENT-STATUS-CLASS")
        parser.readDiagnosticRequestEmissionRelatedDTCPermanentStatusClass(element, request_emission_related_dtc_permanent_status_class)
        return request_emission_related_dtc_permanent_status_class

    def test_read_identifiable_wrapper(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name comes from the dispatch constructor)."""
        request_emission_related_dtc_permanent_status_class = self._read(parser, "<SHORT-NAME>Redps1</SHORT-NAME>")
        assert request_emission_related_dtc_permanent_status_class.getShortName() == "Redps1"

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving the element valid."""
        request_emission_related_dtc_permanent_status_class = self._read(parser, "")
        assert request_emission_related_dtc_permanent_status_class.getShortName() == "Redps1"

    def test_arpackage_dispatch_reads_element(self, parser):
        """Test that readARPackageElementsRest dispatches DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-PERMANENT-STATUS-CLASS through the ARPackage create factory."""
        package = AUTOSAR.getInstance().createARPackage("OBDMode0AClasses")
        element = _snip("<SHORT-NAME>Redps1</SHORT-NAME>", root_tag="DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-PERMANENT-STATUS-CLASS")
        parser.readARPackageElementsRest("DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-PERMANENT-STATUS-CLASS", element, package)
        assert package.getReferrableElement("Redps1", DiagnosticRequestEmissionRelatedDTCPermanentStatusClass) is not None
