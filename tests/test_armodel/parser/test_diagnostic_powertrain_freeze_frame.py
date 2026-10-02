"""Parser tests for DiagnosticPowertrainFreezeFrame (Table 4.134, p.153).

XSD group DIAGNOSTIC-POWERTRAIN-FREEZE-FRAME (AUTOSAR_00052.xsd l.40923) element
order: PID-REFS (wrapper, 0..1) with unbounded PID-REF items (DEST
DIAGNOSTIC-PARAMETER-IDENTIFIER--SUBTYPES-ENUM).

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_powertrain_freeze_frame.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticPowertrainFreezeFrame

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-POWERTRAIN-FREEZE-FRAME") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticPowertrainFreezeFrame:
    def test_read_sets_all_fields(self, parser):
        freeze_frame = DiagnosticPowertrainFreezeFrame(AUTOSAR.getInstance(), "Frame1")
        element = _snip(
            "<SHORT-NAME>Frame1</SHORT-NAME>"
            "<PID-REFS><PID-REF DEST='DIAGNOSTIC-PARAMETER-IDENTIFIER'>/AUTOSAR/DiagnosticParameterIdentifiers/Pid1</PID-REF>"
            "<PID-REF DEST='DIAGNOSTIC-PARAMETER-IDENTIFIER'>/AUTOSAR/DiagnosticParameterIdentifiers/Pid2</PID-REF></PID-REFS>"
        )
        parser.readDiagnosticPowertrainFreezeFrame(element, freeze_frame)
        assert freeze_frame.getShortName() == "Frame1"
        pid_refs = freeze_frame.getPidRefs()
        assert len(pid_refs) == 2
        assert pid_refs[0].getValue() == "/AUTOSAR/DiagnosticParameterIdentifiers/Pid1"
        assert pid_refs[0].getDest() == "DIAGNOSTIC-PARAMETER-IDENTIFIER"
        assert pid_refs[1].getValue() == "/AUTOSAR/DiagnosticParameterIdentifiers/Pid2"
        assert pid_refs[1].getDest() == "DIAGNOSTIC-PARAMETER-IDENTIFIER"

    def test_read_empty(self, parser):
        freeze_frame = DiagnosticPowertrainFreezeFrame(AUTOSAR.getInstance(), "Frame1")
        element = _snip("<SHORT-NAME>Frame1</SHORT-NAME>")
        parser.readDiagnosticPowertrainFreezeFrame(element, freeze_frame)
        assert freeze_frame.getPidRefs() == []
