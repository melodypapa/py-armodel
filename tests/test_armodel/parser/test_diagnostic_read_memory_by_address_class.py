"""
Tests for reading the DIAGNOSTIC-READ-MEMORY-BY-ADDRESS-CLASS element —
DiagnosticReadMemoryByAddressClass, Table 4.116 (p.142, R23-11).

DiagnosticReadMemoryByAddressClass (Base most-derived DiagnosticServiceClass,
concrete) defines no own attributes — the R23-11 table's attribute row is `-`
and XSD group DIAGNOSTIC-READ-MEMORY-BY-ADDRESS-CLASS, AUTOSAR_00052.xsd
l.41482, is an empty sequence. Only the IDENTIFIABLE wrapper is read. The
dispatch entry is readARPackageElementsRest → readDiagnosticReadMemoryByAddressClass
via the ARPackage create factory.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_read_memory_by_address_class.py
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticReadMemoryByAddressClass
from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticReadMemoryByAddressClass:
    """Tests for readDiagnosticReadMemoryByAddressClass — own element field values (Table 4.116)."""

    def _read(self, parser, inner):
        read_memory_by_address_class = DiagnosticReadMemoryByAddressClass(AUTOSAR.getInstance(), "Rmba1")
        element = _snip(inner, root_tag="DIAGNOSTIC-READ-MEMORY-BY-ADDRESS-CLASS")
        parser.readDiagnosticReadMemoryByAddressClass(element, read_memory_by_address_class)
        return read_memory_by_address_class

    def test_read_identifiable_wrapper(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name comes from the dispatch constructor)."""
        read_memory_by_address_class = self._read(parser, "<SHORT-NAME>Rmba1</SHORT-NAME>")
        assert read_memory_by_address_class.getShortName() == "Rmba1"

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving the element valid."""
        read_memory_by_address_class = self._read(parser, "")
        assert read_memory_by_address_class.getShortName() == "Rmba1"

    def test_arpackage_dispatch_reads_element(self, parser):
        """Test that readARPackageElementsRest dispatches DIAGNOSTIC-READ-MEMORY-BY-ADDRESS-CLASS through the ARPackage create factory."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticReadMemoryByAddressClasses")
        element = _snip("<SHORT-NAME>Rmba1</SHORT-NAME>", root_tag="DIAGNOSTIC-READ-MEMORY-BY-ADDRESS-CLASS")
        parser.readARPackageElementsRest("DIAGNOSTIC-READ-MEMORY-BY-ADDRESS-CLASS", element, package)
        assert package.getReferrableElement("Rmba1", DiagnosticReadMemoryByAddressClass) is not None
