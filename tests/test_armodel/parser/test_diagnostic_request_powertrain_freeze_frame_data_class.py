"""
Tests for reading the DIAGNOSTIC-REQUEST-POWERTRAIN-FREEZE-FRAME-DATA-CLASS element —
DiagnosticRequestPowertrainFreezeFrameDataClass, Table 4.133 (p.152, R23-11).

DiagnosticRequestPowertrainFreezeFrameDataClass (Base most-derived
DiagnosticServiceClass, concrete) defines no own attributes — the R23-11 table's
attribute row is `-` and XSD group
DIAGNOSTIC-REQUEST-POWERTRAIN-FREEZE-FRAME-DATA-CLASS, AUTOSAR_00052.xsd l.42366,
is an empty sequence. Only the IDENTIFIABLE wrapper is read. The dispatch entry is
readARPackageElementsRest → readDiagnosticRequestPowertrainFreezeFrameDataClass
via the ARPackage create factory.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_request_powertrain_freeze_frame_data_class.py
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticRequestPowertrainFreezeFrameDataClass
from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticRequestPowertrainFreezeFrameDataClass:
    """Tests for readDiagnosticRequestPowertrainFreezeFrameDataClass — own element field values (Table 4.133)."""

    def _read(self, parser, inner):
        request_powertrain_freeze_frame_data_class = DiagnosticRequestPowertrainFreezeFrameDataClass(AUTOSAR.getInstance(), "Rpf1")
        element = _snip(inner, root_tag="DIAGNOSTIC-REQUEST-POWERTRAIN-FREEZE-FRAME-DATA-CLASS")
        parser.readDiagnosticRequestPowertrainFreezeFrameDataClass(element, request_powertrain_freeze_frame_data_class)
        return request_powertrain_freeze_frame_data_class

    def test_read_identifiable_wrapper(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name comes from the dispatch constructor)."""
        request_powertrain_freeze_frame_data_class = self._read(parser, "<SHORT-NAME>Rpf1</SHORT-NAME>")
        assert request_powertrain_freeze_frame_data_class.getShortName() == "Rpf1"

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving the element valid."""
        request_powertrain_freeze_frame_data_class = self._read(parser, "")
        assert request_powertrain_freeze_frame_data_class.getShortName() == "Rpf1"

    def test_arpackage_dispatch_reads_element(self, parser):
        """Test that readARPackageElementsRest dispatches DIAGNOSTIC-REQUEST-POWERTRAIN-FREEZE-FRAME-DATA-CLASS through the ARPackage create factory."""
        package = AUTOSAR.getInstance().createARPackage("OBDMode02Classes")
        element = _snip("<SHORT-NAME>Rpf1</SHORT-NAME>", root_tag="DIAGNOSTIC-REQUEST-POWERTRAIN-FREEZE-FRAME-DATA-CLASS")
        parser.readARPackageElementsRest("DIAGNOSTIC-REQUEST-POWERTRAIN-FREEZE-FRAME-DATA-CLASS", element, package)
        assert package.getReferrableElement("Rpf1", DiagnosticRequestPowertrainFreezeFrameDataClass) is not None
