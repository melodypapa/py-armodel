"""
Tests for reading the DIAGNOSTIC-REQUEST-VEHICLE-INFO-CLASS element —
DiagnosticRequestVehicleInfoClass, Table 4.145 (p.160, R23-11).

DiagnosticRequestVehicleInfoClass (Base most-derived DiagnosticServiceClass,
concrete) defines no own attributes — the R23-11 table's attribute row is `-` and
XSD group DIAGNOSTIC-REQUEST-VEHICLE-INFO-CLASS, AUTOSAR_00052.xsd l.42599, is an
empty sequence. Only the IDENTIFIABLE wrapper is read. The dispatch entry is
readARPackageElementsRest → readDiagnosticRequestVehicleInfoClass via the
ARPackage create factory.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_request_vehicle_info_class.py
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticRequestVehicleInfoClass
from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticRequestVehicleInfoClass:
    """Tests for readDiagnosticRequestVehicleInfoClass — own element field values (Table 4.145)."""

    def _read(self, parser, inner):
        request_vehicle_info_class = DiagnosticRequestVehicleInfoClass(AUTOSAR.getInstance(), "Rvi1")
        element = _snip(inner, root_tag="DIAGNOSTIC-REQUEST-VEHICLE-INFO-CLASS")
        parser.readDiagnosticRequestVehicleInfoClass(element, request_vehicle_info_class)
        return request_vehicle_info_class

    def test_read_identifiable_wrapper(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name comes from the dispatch constructor)."""
        request_vehicle_info_class = self._read(parser, "<SHORT-NAME>Rvi1</SHORT-NAME>")
        assert request_vehicle_info_class.getShortName() == "Rvi1"

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving the element valid."""
        request_vehicle_info_class = self._read(parser, "")
        assert request_vehicle_info_class.getShortName() == "Rvi1"

    def test_arpackage_dispatch_reads_element(self, parser):
        """Test that readARPackageElementsRest dispatches DIAGNOSTIC-REQUEST-VEHICLE-INFO-CLASS through the ARPackage create factory."""
        package = AUTOSAR.getInstance().createARPackage("OBDMode09Classes")
        element = _snip("<SHORT-NAME>Rvi1</SHORT-NAME>", root_tag="DIAGNOSTIC-REQUEST-VEHICLE-INFO-CLASS")
        parser.readARPackageElementsRest("DIAGNOSTIC-REQUEST-VEHICLE-INFO-CLASS", element, package)
        assert package.getReferrableElement("Rvi1", DiagnosticRequestVehicleInfoClass) is not None
