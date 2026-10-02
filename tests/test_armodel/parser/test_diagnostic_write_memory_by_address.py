"""Parser tests for DiagnosticWriteMemoryByAddress (Table 4.113, p.141).

XSD group DIAGNOSTIC-WRITE-MEMORY-BY-ADDRESS (AUTOSAR_00052.xsd l.47258) element order:
MEMORY-RANGE-REFS (inherited from DIAGNOSTIC-MEMORY-ADDRESSABLE-RANGE-ACCESS, l.39420),
WRITE-CLASS-REF.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_write_memory_by_address.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticWriteMemoryByAddress

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-WRITE-MEMORY-BY-ADDRESS") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticWriteMemoryByAddress:
    def test_read_sets_all_fields(self, parser):
        write_memory = DiagnosticWriteMemoryByAddress(AUTOSAR.getInstance(), "WriteMem1")
        element = _snip(
            "<SHORT-NAME>WriteMem1</SHORT-NAME>"
            "<MEMORY-RANGE-REFS>"
            "<MEMORY-RANGE-REF DEST='DIAGNOSTIC-MEMORY-IDENTIFIER'>/AUTOSAR/DiagnosticMemoryIdentifiers/Segment1</MEMORY-RANGE-REF>"
            "<MEMORY-RANGE-REF DEST='DIAGNOSTIC-MEMORY-IDENTIFIER'>/AUTOSAR/DiagnosticMemoryIdentifiers/Segment2</MEMORY-RANGE-REF>"
            "</MEMORY-RANGE-REFS>"
            "<WRITE-CLASS-REF DEST='DIAGNOSTIC-WRITE-MEMORY-BY-ADDRESS-CLASS'>/AUTOSAR/DiagnosticWriteMemoryByAddressClasses/Class1</WRITE-CLASS-REF>"
        )
        parser.readDiagnosticWriteMemoryByAddress(element, write_memory)
        assert write_memory.getShortName() == "WriteMem1"
        assert len(write_memory.getMemoryRanges()) == 2
        assert write_memory.getMemoryRanges()[0].getValue() == "/AUTOSAR/DiagnosticMemoryIdentifiers/Segment1"
        assert write_memory.getMemoryRanges()[0].getDest() == "DIAGNOSTIC-MEMORY-IDENTIFIER"
        assert write_memory.getMemoryRanges()[1].getValue() == "/AUTOSAR/DiagnosticMemoryIdentifiers/Segment2"
        assert write_memory.getWriteClassRef() is not None
        assert write_memory.getWriteClassRef().getValue() == "/AUTOSAR/DiagnosticWriteMemoryByAddressClasses/Class1"
        assert write_memory.getWriteClassRef().getDest() == "DIAGNOSTIC-WRITE-MEMORY-BY-ADDRESS-CLASS"

    def test_read_empty(self, parser):
        write_memory = DiagnosticWriteMemoryByAddress(AUTOSAR.getInstance(), "WriteMem1")
        element = _snip("<SHORT-NAME>WriteMem1</SHORT-NAME>")
        parser.readDiagnosticWriteMemoryByAddress(element, write_memory)
        assert write_memory.getMemoryRanges() == []
        assert write_memory.getWriteClassRef() is None
