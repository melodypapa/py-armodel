"""Parser tests for DiagnosticRequestPowertrainFreezeFrameData (Table 4.132, p.152).

XSD group DIAGNOSTIC-REQUEST-POWERTRAIN-FREEZE-FRAME-DATA (AUTOSAR_00052.xsd
l.42306) element order: FREEZE-FRAME-REF, REQUEST-POWERTRAIN-FREEZE-FRAME-DATA-REF.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_request_powertrain_freeze_frame_data.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticRequestPowertrainFreezeFrameData

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-REQUEST-POWERTRAIN-FREEZE-FRAME-DATA") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticRequestPowertrainFreezeFrameData:
    def test_read_sets_all_fields(self, parser):
        mode02 = DiagnosticRequestPowertrainFreezeFrameData(AUTOSAR.getInstance(), "Mode02")
        element = _snip(
            "<SHORT-NAME>Mode02</SHORT-NAME>"
            "<FREEZE-FRAME-REF DEST='DIAGNOSTIC-POWERTRAIN-FREEZE-FRAME'>/AUTOSAR/DiagnosticPowertrainFreezeFrames/Frame1</FREEZE-FRAME-REF>"
            "<REQUEST-POWERTRAIN-FREEZE-FRAME-DATA-REF DEST='DIAGNOSTIC-REQUEST-POWERTRAIN-FREEZE-FRAME-DATA-CLASS'>/AUTOSAR/DiagnosticRequestPowertrainFreezeFrameDataClasses/Class1</REQUEST-POWERTRAIN-FREEZE-FRAME-DATA-REF>"
        )
        parser.readDiagnosticRequestPowertrainFreezeFrameData(element, mode02)
        assert mode02.getShortName() == "Mode02"
        assert mode02.getFreezeFrameRef() is not None
        assert mode02.getFreezeFrameRef().getValue() == "/AUTOSAR/DiagnosticPowertrainFreezeFrames/Frame1"
        assert mode02.getFreezeFrameRef().getDest() == "DIAGNOSTIC-POWERTRAIN-FREEZE-FRAME"
        assert mode02.getRequestPowertrainFreezeFrameDataRef() is not None
        assert mode02.getRequestPowertrainFreezeFrameDataRef().getValue() == "/AUTOSAR/DiagnosticRequestPowertrainFreezeFrameDataClasses/Class1"
        assert mode02.getRequestPowertrainFreezeFrameDataRef().getDest() == "DIAGNOSTIC-REQUEST-POWERTRAIN-FREEZE-FRAME-DATA-CLASS"

    def test_read_empty(self, parser):
        mode02 = DiagnosticRequestPowertrainFreezeFrameData(AUTOSAR.getInstance(), "Mode02")
        element = _snip("<SHORT-NAME>Mode02</SHORT-NAME>")
        parser.readDiagnosticRequestPowertrainFreezeFrameData(element, mode02)
        assert mode02.getFreezeFrameRef() is None
        assert mode02.getRequestPowertrainFreezeFrameDataRef() is None
