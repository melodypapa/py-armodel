"""Parser tests for DiagnosticRequestControlOfOnBoardDevice (Table 4.141, p.157).

XSD group DIAGNOSTIC-REQUEST-CONTROL-OF-ON-BOARD-DEVICE (AUTOSAR_00052.xsd
l.41602) element order: REQUEST-CONTROL-OF-ON-BOARD-DEVICE-CLASS-REF, TEST-ID-REF.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_request_control_of_on_board_device.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticRequestControlOfOnBoardDevice

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-REQUEST-CONTROL-OF-ON-BOARD-DEVICE") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticRequestControlOfOnBoardDevice:
    def test_read_sets_all_fields(self, parser):
        mode08 = DiagnosticRequestControlOfOnBoardDevice(AUTOSAR.getInstance(), "Mode08")
        element = _snip(
            "<SHORT-NAME>Mode08</SHORT-NAME>"
            "<REQUEST-CONTROL-OF-ON-BOARD-DEVICE-CLASS-REF DEST='DIAGNOSTIC-REQUEST-CONTROL-OF-ON-BOARD-DEVICE-CLASS'>/AUTOSAR/DiagnosticRequestControlOfOnBoardDeviceClasses/Class1</REQUEST-CONTROL-OF-ON-BOARD-DEVICE-CLASS-REF>"
            "<TEST-ID-REF DEST='DIAGNOSTIC-TEST-ROUTINE-IDENTIFIER'>/AUTOSAR/DiagnosticTestRoutineIdentifiers/Tid1</TEST-ID-REF>"
        )
        parser.readDiagnosticRequestControlOfOnBoardDevice(element, mode08)
        assert mode08.getShortName() == "Mode08"
        assert mode08.getRequestControlOfOnBoardDeviceClassRef() is not None
        assert mode08.getRequestControlOfOnBoardDeviceClassRef().getValue() == "/AUTOSAR/DiagnosticRequestControlOfOnBoardDeviceClasses/Class1"
        assert mode08.getRequestControlOfOnBoardDeviceClassRef().getDest() == "DIAGNOSTIC-REQUEST-CONTROL-OF-ON-BOARD-DEVICE-CLASS"
        assert mode08.getTestIdRef() is not None
        assert mode08.getTestIdRef().getValue() == "/AUTOSAR/DiagnosticTestRoutineIdentifiers/Tid1"
        assert mode08.getTestIdRef().getDest() == "DIAGNOSTIC-TEST-ROUTINE-IDENTIFIER"

    def test_read_empty(self, parser):
        mode08 = DiagnosticRequestControlOfOnBoardDevice(AUTOSAR.getInstance(), "Mode08")
        element = _snip("<SHORT-NAME>Mode08</SHORT-NAME>")
        parser.readDiagnosticRequestControlOfOnBoardDevice(element, mode08)
        assert mode08.getRequestControlOfOnBoardDeviceClassRef() is None
        assert mode08.getTestIdRef() is None
