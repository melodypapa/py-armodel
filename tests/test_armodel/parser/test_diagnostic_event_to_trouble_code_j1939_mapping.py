"""Parser tests for DiagnosticEventToTroubleCodeJ1939Mapping (Table 5.43, p.269).

XSD group DIAGNOSTIC-EVENT-TO-TROUBLE-CODE-J-1939-MAPPING element order (AUTOSAR_00052.xsd): DIAGNOSTIC-EVENT-REF, TROUBLE-CODE-J-1939-REF.
Base DIAGNOSTIC-MAPPING group (provider/requester software-cluster refs) is read
by readDiagnosticMapping.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticEventToTroubleCodeJ1939Mapping

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-EVENT-TO-TROUBLE-CODE-J-1939-MAPPING") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticEventToTroubleCodeJ1939Mapping:
    def test_read_sets_all_fields(self, parser):
        mapping = DiagnosticEventToTroubleCodeJ1939Mapping(AUTOSAR.getInstance(), "M1")
        element = _snip(
            "<SHORT-NAME>M1</SHORT-NAME>"
            "<DIAGNOSTIC-EVENT-REF DEST='DEST'>/AUTOSAR/DiagnosticEvent1</DIAGNOSTIC-EVENT-REF><TROUBLE-CODE-J-1939-REF DEST='DEST'>/AUTOSAR/TroubleCodeJ19391</TROUBLE-CODE-J-1939-REF>"
        )
        parser.readDiagnosticEventToTroubleCodeJ1939Mapping(element, mapping)
        assert mapping.getShortName() == "M1"
        assert mapping.getDiagnosticEventRef() is not None
        assert mapping.getDiagnosticEventRef().getValue() == "/AUTOSAR/DiagnosticEvent1"
        assert mapping.getTroubleCodeJ1939Ref() is not None
        assert mapping.getTroubleCodeJ1939Ref().getValue() == "/AUTOSAR/TroubleCodeJ19391"

    def test_read_empty(self, parser):
        mapping = DiagnosticEventToTroubleCodeJ1939Mapping(AUTOSAR.getInstance(), "M1")
        element = _snip("")
        parser.readDiagnosticEventToTroubleCodeJ1939Mapping(element, mapping)
        assert mapping.getDiagnosticEventRef() is None
        assert mapping.getTroubleCodeJ1939Ref() is None
