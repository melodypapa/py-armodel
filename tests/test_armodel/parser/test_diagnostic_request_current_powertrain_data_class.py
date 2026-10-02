"""
Tests for reading the DIAGNOSTIC-REQUEST-CURRENT-POWERTRAIN-DATA-CLASS element —
DiagnosticRequestCurrentPowertrainDataClass, Table 4.131 (p.151, R23-11).

DiagnosticRequestCurrentPowertrainDataClass (Base most-derived
DiagnosticServiceClass, concrete) defines no own attributes — the R23-11 table's
attribute row is `-` and XSD group
DIAGNOSTIC-REQUEST-CURRENT-POWERTRAIN-DATA-CLASS, AUTOSAR_00052.xsd l.41758, is an
empty sequence. Only the IDENTIFIABLE wrapper is read. The dispatch entry is
readARPackageElementsRest → readDiagnosticRequestCurrentPowertrainDataClass via
the ARPackage create factory.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_request_current_powertrain_data_class.py
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticRequestCurrentPowertrainDataClass
from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticRequestCurrentPowertrainDataClass:
    """Tests for readDiagnosticRequestCurrentPowertrainDataClass — own element field values (Table 4.131)."""

    def _read(self, parser, inner):
        request_current_powertrain_data_class = DiagnosticRequestCurrentPowertrainDataClass(AUTOSAR.getInstance(), "Rcp1")
        element = _snip(inner, root_tag="DIAGNOSTIC-REQUEST-CURRENT-POWERTRAIN-DATA-CLASS")
        parser.readDiagnosticRequestCurrentPowertrainDataClass(element, request_current_powertrain_data_class)
        return request_current_powertrain_data_class

    def test_read_identifiable_wrapper(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name comes from the dispatch constructor)."""
        request_current_powertrain_data_class = self._read(parser, "<SHORT-NAME>Rcp1</SHORT-NAME>")
        assert request_current_powertrain_data_class.getShortName() == "Rcp1"

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving the element valid."""
        request_current_powertrain_data_class = self._read(parser, "")
        assert request_current_powertrain_data_class.getShortName() == "Rcp1"

    def test_arpackage_dispatch_reads_element(self, parser):
        """Test that readARPackageElementsRest dispatches DIAGNOSTIC-REQUEST-CURRENT-POWERTRAIN-DATA-CLASS through the ARPackage create factory."""
        package = AUTOSAR.getInstance().createARPackage("OBDMode01Classes")
        element = _snip("<SHORT-NAME>Rcp1</SHORT-NAME>", root_tag="DIAGNOSTIC-REQUEST-CURRENT-POWERTRAIN-DATA-CLASS")
        parser.readARPackageElementsRest("DIAGNOSTIC-REQUEST-CURRENT-POWERTRAIN-DATA-CLASS", element, package)
        assert package.getReferrableElement("Rcp1", DiagnosticRequestCurrentPowertrainDataClass) is not None
