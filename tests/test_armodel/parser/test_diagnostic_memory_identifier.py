"""Parser tests for DiagnosticMemoryIdentifier (Table 4.112, p.140).

XSD group DIAGNOSTIC-MEMORY-IDENTIFIER (AUTOSAR_00052.xsd l.39770) element order:
ACCESS-PERMISSION-REF, ID, MEMORY-HIGH-ADDRESS, MEMORY-HIGH-ADDRESS-LABEL,
MEMORY-LOW-ADDRESS, MEMORY-LOW-ADDRESS-LABEL.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_memory_identifier.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticMemoryIdentifier

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-MEMORY-IDENTIFIER") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticMemoryIdentifier:
    def test_read_sets_all_fields(self, parser):
        identifier = DiagnosticMemoryIdentifier(AUTOSAR.getInstance(), "Segment1")
        element = _snip(
            "<SHORT-NAME>Segment1</SHORT-NAME>"
            "<ACCESS-PERMISSION-REF DEST='DIAGNOSTIC-ACCESS-PERMISSION'>/AUTOSAR/DiagnosticAccessPermissions/Permission1</ACCESS-PERMISSION-REF>"
            "<ID>1</ID>"
            "<MEMORY-HIGH-ADDRESS>4096</MEMORY-HIGH-ADDRESS>"
            "<MEMORY-HIGH-ADDRESS-LABEL>0x1000</MEMORY-HIGH-ADDRESS-LABEL>"
            "<MEMORY-LOW-ADDRESS>0</MEMORY-LOW-ADDRESS>"
            "<MEMORY-LOW-ADDRESS-LABEL>0x0</MEMORY-LOW-ADDRESS-LABEL>"
        )
        parser.readDiagnosticMemoryIdentifier(element, identifier)
        assert identifier.getShortName() == "Segment1"
        assert identifier.getAccessPermissionRef() is not None
        assert identifier.getAccessPermissionRef().getValue() == "/AUTOSAR/DiagnosticAccessPermissions/Permission1"
        assert identifier.getAccessPermissionRef().getDest() == "DIAGNOSTIC-ACCESS-PERMISSION"
        assert identifier.getId() is not None
        assert identifier.getId().getValue() == 1
        assert identifier.getMemoryHighAddress() is not None
        assert identifier.getMemoryHighAddress().getValue() == 4096
        assert identifier.getMemoryHighAddressLabel() is not None
        assert identifier.getMemoryHighAddressLabel().getValue() == "0x1000"
        assert identifier.getMemoryLowAddress() is not None
        assert identifier.getMemoryLowAddress().getValue() == 0
        assert identifier.getMemoryLowAddressLabel() is not None
        assert identifier.getMemoryLowAddressLabel().getValue() == "0x0"

    def test_read_empty(self, parser):
        identifier = DiagnosticMemoryIdentifier(AUTOSAR.getInstance(), "Segment1")
        element = _snip("<SHORT-NAME>Segment1</SHORT-NAME>")
        parser.readDiagnosticMemoryIdentifier(element, identifier)
        assert identifier.getAccessPermissionRef() is None
        assert identifier.getId() is None
        assert identifier.getMemoryHighAddress() is None
        assert identifier.getMemoryHighAddressLabel() is None
        assert identifier.getMemoryLowAddress() is None
        assert identifier.getMemoryLowAddressLabel() is None
