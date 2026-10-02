"""Parser tests for DiagnosticReadMemoryByAddress (Table 4.115, p.142).

XSD group DIAGNOSTIC-READ-MEMORY-BY-ADDRESS (AUTOSAR_00052.xsd l.41433) element order:
MEMORY-RANGE-REFS (inherited from DIAGNOSTIC-MEMORY-ADDRESSABLE-RANGE-ACCESS),
READ-CLASS-REF.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_read_memory_by_address.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticReadMemoryByAddress

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-READ-MEMORY-BY-ADDRESS") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticReadMemoryByAddress:
    def test_read_sets_all_fields(self, parser):
        read_memory = DiagnosticReadMemoryByAddress(AUTOSAR.getInstance(), "ReadMem1")
        element = _snip(
            "<SHORT-NAME>ReadMem1</SHORT-NAME>"
            "<MEMORY-RANGE-REFS>"
            "<MEMORY-RANGE-REF DEST='DIAGNOSTIC-MEMORY-IDENTIFIER'>/AUTOSAR/DiagnosticMemoryIdentifiers/Segment1</MEMORY-RANGE-REF>"
            "<MEMORY-RANGE-REF DEST='DIAGNOSTIC-MEMORY-IDENTIFIER'>/AUTOSAR/DiagnosticMemoryIdentifiers/Segment2</MEMORY-RANGE-REF>"
            "</MEMORY-RANGE-REFS>"
            "<READ-CLASS-REF DEST='DIAGNOSTIC-READ-MEMORY-BY-ADDRESS-CLASS'>/AUTOSAR/DiagnosticReadMemoryByAddressClasses/Class1</READ-CLASS-REF>"
        )
        parser.readDiagnosticReadMemoryByAddress(element, read_memory)
        assert read_memory.getShortName() == "ReadMem1"
        assert len(read_memory.getMemoryRanges()) == 2
        assert read_memory.getMemoryRanges()[0].getValue() == "/AUTOSAR/DiagnosticMemoryIdentifiers/Segment1"
        assert read_memory.getMemoryRanges()[0].getDest() == "DIAGNOSTIC-MEMORY-IDENTIFIER"
        assert read_memory.getMemoryRanges()[1].getValue() == "/AUTOSAR/DiagnosticMemoryIdentifiers/Segment2"
        assert read_memory.getReadClassRef() is not None
        assert read_memory.getReadClassRef().getValue() == "/AUTOSAR/DiagnosticReadMemoryByAddressClasses/Class1"
        assert read_memory.getReadClassRef().getDest() == "DIAGNOSTIC-READ-MEMORY-BY-ADDRESS-CLASS"

    def test_read_empty(self, parser):
        read_memory = DiagnosticReadMemoryByAddress(AUTOSAR.getInstance(), "ReadMem1")
        element = _snip("<SHORT-NAME>ReadMem1</SHORT-NAME>")
        parser.readDiagnosticReadMemoryByAddress(element, read_memory)
        assert read_memory.getMemoryRanges() == []
        assert read_memory.getReadClassRef() is None
