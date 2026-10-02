"""Parser tests for DiagnosticDataTransfer (Table 4.119, p.143).

XSD group DIAGNOSTIC-DATA-TRANSFER (AUTOSAR_00052.xsd l.34573 region) element order:
DATA-TRANSFER-CLASS-REF.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_data_transfer.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticDataTransfer

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-DATA-TRANSFER") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticDataTransfer:
    def test_read_sets_all_fields(self, parser):
        data_transfer = DiagnosticDataTransfer(AUTOSAR.getInstance(), "DataTransfer1")
        element = _snip(
            "<SHORT-NAME>DataTransfer1</SHORT-NAME>"
            "<DATA-TRANSFER-CLASS-REF DEST='DIAGNOSTIC-DATA-TRANSFER-CLASS'>/AUTOSAR/DiagnosticDataTransferClasses/Class1</DATA-TRANSFER-CLASS-REF>"
        )
        parser.readDiagnosticDataTransfer(element, data_transfer)
        assert data_transfer.getShortName() == "DataTransfer1"
        assert data_transfer.getDataTransferClassRef() is not None
        assert data_transfer.getDataTransferClassRef().getValue() == "/AUTOSAR/DiagnosticDataTransferClasses/Class1"
        assert data_transfer.getDataTransferClassRef().getDest() == "DIAGNOSTIC-DATA-TRANSFER-CLASS"

    def test_read_empty(self, parser):
        data_transfer = DiagnosticDataTransfer(AUTOSAR.getInstance(), "DataTransfer1")
        element = _snip("<SHORT-NAME>DataTransfer1</SHORT-NAME>")
        parser.readDiagnosticDataTransfer(element, data_transfer)
        assert data_transfer.getDataTransferClassRef() is None
