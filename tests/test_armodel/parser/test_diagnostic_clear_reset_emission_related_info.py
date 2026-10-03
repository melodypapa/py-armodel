"""Parser tests for DiagnosticClearResetEmissionRelatedInfo (Table 4.137, p.155).

XSD group DIAGNOSTIC-CLEAR-RESET-EMISSION-RELATED-INFO (AUTOSAR_00052.xsd
l.32432) element order: CLEAR-RESET-EMISSION-RELATED-DIAGNOSTIC-INFO-CLASS-REF
(single 0..1).

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_clear_reset_emission_related_info.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticClearResetEmissionRelatedInfo

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-CLEAR-RESET-EMISSION-RELATED-INFO") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticClearResetEmissionRelatedInfo:
    def test_read_sets_all_fields(self, parser):
        mode04 = DiagnosticClearResetEmissionRelatedInfo(AUTOSAR.getInstance(), "Mode04")
        element = _snip(
            "<SHORT-NAME>Mode04</SHORT-NAME>"
            "<CLEAR-RESET-EMISSION-RELATED-DIAGNOSTIC-INFO-CLASS-REF DEST='DIAGNOSTIC-CLEAR-RESET-EMISSION-RELATED-INFO-CLASS'>/AUTOSAR/DiagnosticClearResetEmissionRelatedInfoClasses/Class1</CLEAR-RESET-EMISSION-RELATED-DIAGNOSTIC-INFO-CLASS-REF>"
        )
        parser.readDiagnosticClearResetEmissionRelatedInfo(element, mode04)
        assert mode04.getShortName() == "Mode04"
        assert mode04.getClearResetEmissionRelatedDiagnosticInfoClassRef() is not None
        assert mode04.getClearResetEmissionRelatedDiagnosticInfoClassRef().getValue() == "/AUTOSAR/DiagnosticClearResetEmissionRelatedInfoClasses/Class1"
        assert mode04.getClearResetEmissionRelatedDiagnosticInfoClassRef().getDest() == "DIAGNOSTIC-CLEAR-RESET-EMISSION-RELATED-INFO-CLASS"

    def test_read_empty(self, parser):
        mode04 = DiagnosticClearResetEmissionRelatedInfo(AUTOSAR.getInstance(), "Mode04")
        element = _snip("<SHORT-NAME>Mode04</SHORT-NAME>")
        parser.readDiagnosticClearResetEmissionRelatedInfo(element, mode04)
        assert mode04.getClearResetEmissionRelatedDiagnosticInfoClassRef() is None
