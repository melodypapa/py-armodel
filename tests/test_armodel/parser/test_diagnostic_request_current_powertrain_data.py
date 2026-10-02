"""Parser tests for DiagnosticRequestCurrentPowertrainData (Table 4.130, p.151).

XSD group DIAGNOSTIC-REQUEST-CURRENT-POWERTRAIN-DATA (AUTOSAR_00052.xsd l.41698)
element order: PID-REF, REQUEST-CURRENT-POWERTRAIN-DIAGNOSTIC-DATA-CLASS-REF.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_request_current_powertrain_data.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticRequestCurrentPowertrainData

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-REQUEST-CURRENT-POWERTRAIN-DATA") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticRequestCurrentPowertrainData:
    def test_read_sets_all_fields(self, parser):
        mode01 = DiagnosticRequestCurrentPowertrainData(AUTOSAR.getInstance(), "Mode01")
        element = _snip(
            "<SHORT-NAME>Mode01</SHORT-NAME>"
            "<PID-REF DEST='DIAGNOSTIC-PARAMETER-IDENTIFIER'>/AUTOSAR/DiagnosticParameterIdentifiers/Pid1</PID-REF>"
            "<REQUEST-CURRENT-POWERTRAIN-DIAGNOSTIC-DATA-CLASS-REF DEST='DIAGNOSTIC-REQUEST-CURRENT-POWERTRAIN-DATA-CLASS'>/AUTOSAR/DiagnosticRequestCurrentPowertrainDataClasses/Class1</REQUEST-CURRENT-POWERTRAIN-DIAGNOSTIC-DATA-CLASS-REF>"
        )
        parser.readDiagnosticRequestCurrentPowertrainData(element, mode01)
        assert mode01.getShortName() == "Mode01"
        assert mode01.getPidRef() is not None
        assert mode01.getPidRef().getValue() == "/AUTOSAR/DiagnosticParameterIdentifiers/Pid1"
        assert mode01.getPidRef().getDest() == "DIAGNOSTIC-PARAMETER-IDENTIFIER"
        assert mode01.getRequestCurrentPowertrainDiagnosticDataClassRef() is not None
        assert mode01.getRequestCurrentPowertrainDiagnosticDataClassRef().getValue() == "/AUTOSAR/DiagnosticRequestCurrentPowertrainDataClasses/Class1"
        assert mode01.getRequestCurrentPowertrainDiagnosticDataClassRef().getDest() == "DIAGNOSTIC-REQUEST-CURRENT-POWERTRAIN-DATA-CLASS"

    def test_read_empty(self, parser):
        mode01 = DiagnosticRequestCurrentPowertrainData(AUTOSAR.getInstance(), "Mode01")
        element = _snip("<SHORT-NAME>Mode01</SHORT-NAME>")
        parser.readDiagnosticRequestCurrentPowertrainData(element, mode01)
        assert mode01.getPidRef() is None
        assert mode01.getRequestCurrentPowertrainDiagnosticDataClassRef() is None
