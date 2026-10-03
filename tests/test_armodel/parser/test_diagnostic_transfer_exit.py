"""Parser tests for DiagnosticTransferExit (Table 4.117, p.143).

XSD group DIAGNOSTIC-TRANSFER-EXIT (AUTOSAR_00052.xsd l.46110) element order:
TRANSFER-EXIT-CLASS-REF.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_transfer_exit.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticTransferExit

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-TRANSFER-EXIT") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticTransferExit:
    def test_read_sets_all_fields(self, parser):
        transfer_exit = DiagnosticTransferExit(AUTOSAR.getInstance(), "TransferExit1")
        element = _snip(
            "<SHORT-NAME>TransferExit1</SHORT-NAME>" "<TRANSFER-EXIT-CLASS-REF DEST='DIAGNOSTIC-TRANSFER-EXIT-CLASS'>/AUTOSAR/DiagnosticTransferExitClasses/Class1</TRANSFER-EXIT-CLASS-REF>"
        )
        parser.readDiagnosticTransferExit(element, transfer_exit)
        assert transfer_exit.getShortName() == "TransferExit1"
        assert transfer_exit.getTransferExitClassRef() is not None
        assert transfer_exit.getTransferExitClassRef().getValue() == "/AUTOSAR/DiagnosticTransferExitClasses/Class1"
        assert transfer_exit.getTransferExitClassRef().getDest() == "DIAGNOSTIC-TRANSFER-EXIT-CLASS"

    def test_read_empty(self, parser):
        transfer_exit = DiagnosticTransferExit(AUTOSAR.getInstance(), "TransferExit1")
        element = _snip("<SHORT-NAME>TransferExit1</SHORT-NAME>")
        parser.readDiagnosticTransferExit(element, transfer_exit)
        assert transfer_exit.getTransferExitClassRef() is None
