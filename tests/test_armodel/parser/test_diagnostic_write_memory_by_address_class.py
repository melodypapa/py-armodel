"""
Tests for reading the DIAGNOSTIC-WRITE-MEMORY-BY-ADDRESS-CLASS element —
DiagnosticWriteMemoryByAddressClass, Table 4.114 (p.141, R23-11).

DiagnosticWriteMemoryByAddressClass (Base most-derived DiagnosticServiceClass,
concrete) defines no own attributes — the R23-11 table's attribute row is `-`
and XSD group DIAGNOSTIC-WRITE-MEMORY-BY-ADDRESS-CLASS, AUTOSAR_00052.xsd
l.47307, is an empty sequence. Only the IDENTIFIABLE wrapper is read. The
dispatch entry is readARPackageElementsRest → readDiagnosticWriteMemoryByAddressClass
via the ARPackage create factory.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_write_memory_by_address_class.py
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticWriteMemoryByAddressClass
from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticWriteMemoryByAddressClass:
    """Tests for readDiagnosticWriteMemoryByAddressClass — own element field values (Table 4.114)."""

    def _read(self, parser, inner):
        write_memory_by_address_class = DiagnosticWriteMemoryByAddressClass(AUTOSAR.getInstance(), "Wmba1")
        element = _snip(inner, root_tag="DIAGNOSTIC-WRITE-MEMORY-BY-ADDRESS-CLASS")
        parser.readDiagnosticWriteMemoryByAddressClass(element, write_memory_by_address_class)
        return write_memory_by_address_class

    def test_read_identifiable_wrapper(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name comes from the dispatch constructor)."""
        write_memory_by_address_class = self._read(parser, "<SHORT-NAME>Wmba1</SHORT-NAME>")
        assert write_memory_by_address_class.getShortName() == "Wmba1"

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving the element valid."""
        write_memory_by_address_class = self._read(parser, "")
        assert write_memory_by_address_class.getShortName() == "Wmba1"

    def test_arpackage_dispatch_reads_element(self, parser):
        """Test that readARPackageElementsRest dispatches DIAGNOSTIC-WRITE-MEMORY-BY-ADDRESS-CLASS through the ARPackage create factory."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticWriteMemoryByAddressClasses")
        element = _snip("<SHORT-NAME>Wmba1</SHORT-NAME>", root_tag="DIAGNOSTIC-WRITE-MEMORY-BY-ADDRESS-CLASS")
        parser.readARPackageElementsRest("DIAGNOSTIC-WRITE-MEMORY-BY-ADDRESS-CLASS", element, package)
        assert package.getReferrableElement("Wmba1", DiagnosticWriteMemoryByAddressClass) is not None
