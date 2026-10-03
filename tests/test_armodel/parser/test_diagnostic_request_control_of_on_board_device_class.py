"""
Tests for reading the DIAGNOSTIC-REQUEST-CONTROL-OF-ON-BOARD-DEVICE-CLASS
element — DiagnosticRequestControlOfOnBoardDeviceClass, Table 4.142 (p.158,
R23-11).

DiagnosticRequestControlOfOnBoardDeviceClass (Base most-derived
DiagnosticServiceClass, concrete) defines no own attributes — the R23-11 table's
attribute row is `-` and XSD group
DIAGNOSTIC-REQUEST-CONTROL-OF-ON-BOARD-DEVICE-CLASS, AUTOSAR_00052.xsd l.41662,
is an empty sequence. Only the IDENTIFIABLE wrapper is read. The dispatch entry
is readARPackageElementsRest → readDiagnosticRequestControlOfOnBoardDeviceClass
via the ARPackage create factory.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_request_control_of_on_board_device_class.py
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticRequestControlOfOnBoardDeviceClass
from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticRequestControlOfOnBoardDeviceClass:
    """Tests for readDiagnosticRequestControlOfOnBoardDeviceClass — own element field values (Table 4.142)."""

    def _read(self, parser, inner):
        request_control_of_on_board_device_class = DiagnosticRequestControlOfOnBoardDeviceClass(AUTOSAR.getInstance(), "Coob1")
        element = _snip(inner, root_tag="DIAGNOSTIC-REQUEST-CONTROL-OF-ON-BOARD-DEVICE-CLASS")
        parser.readDiagnosticRequestControlOfOnBoardDeviceClass(element, request_control_of_on_board_device_class)
        return request_control_of_on_board_device_class

    def test_read_identifiable_wrapper(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name comes from the dispatch constructor)."""
        request_control_of_on_board_device_class = self._read(parser, "<SHORT-NAME>Coob1</SHORT-NAME>")
        assert request_control_of_on_board_device_class.getShortName() == "Coob1"

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving the element valid."""
        request_control_of_on_board_device_class = self._read(parser, "")
        assert request_control_of_on_board_device_class.getShortName() == "Coob1"

    def test_arpackage_dispatch_reads_element(self, parser):
        """Test that readARPackageElementsRest dispatches DIAGNOSTIC-REQUEST-CONTROL-OF-ON-BOARD-DEVICE-CLASS through the ARPackage create factory."""
        package = AUTOSAR.getInstance().createARPackage("OBDMode08Classes")
        element = _snip("<SHORT-NAME>Coob1</SHORT-NAME>", root_tag="DIAGNOSTIC-REQUEST-CONTROL-OF-ON-BOARD-DEVICE-CLASS")
        parser.readARPackageElementsRest("DIAGNOSTIC-REQUEST-CONTROL-OF-ON-BOARD-DEVICE-CLASS", element, package)
        assert package.getReferrableElement("Coob1", DiagnosticRequestControlOfOnBoardDeviceClass) is not None
