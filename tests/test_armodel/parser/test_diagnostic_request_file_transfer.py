"""Parser tests for DiagnosticRequestFileTransfer (Table 4.125, p.147).

XSD group DIAGNOSTIC-REQUEST-FILE-TRANSFER (AUTOSAR_00052.xsd l.42045) element order:
REQUEST-FILE-TRANSFER-CLASS-REF.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_request_file_transfer.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticRequestFileTransfer

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-REQUEST-FILE-TRANSFER") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticRequestFileTransfer:
    def test_read_sets_all_fields(self, parser):
        request_file_transfer = DiagnosticRequestFileTransfer(AUTOSAR.getInstance(), "RequestFileTransfer1")
        element = _snip(
            "<SHORT-NAME>RequestFileTransfer1</SHORT-NAME>"
            "<REQUEST-FILE-TRANSFER-CLASS-REF DEST='DIAGNOSTIC-REQUEST-FILE-TRANSFER-CLASS'>/AUTOSAR/DiagnosticRequestFileTransferClasses/Class1</REQUEST-FILE-TRANSFER-CLASS-REF>"
        )
        parser.readDiagnosticRequestFileTransfer(element, request_file_transfer)
        assert request_file_transfer.getShortName() == "RequestFileTransfer1"
        assert request_file_transfer.getRequestFileTransferClassRef() is not None
        assert request_file_transfer.getRequestFileTransferClassRef().getValue() == "/AUTOSAR/DiagnosticRequestFileTransferClasses/Class1"
        assert request_file_transfer.getRequestFileTransferClassRef().getDest() == "DIAGNOSTIC-REQUEST-FILE-TRANSFER-CLASS"

    def test_read_empty(self, parser):
        request_file_transfer = DiagnosticRequestFileTransfer(AUTOSAR.getInstance(), "RequestFileTransfer1")
        element = _snip("<SHORT-NAME>RequestFileTransfer1</SHORT-NAME>")
        parser.readDiagnosticRequestFileTransfer(element, request_file_transfer)
        assert request_file_transfer.getRequestFileTransferClassRef() is None
