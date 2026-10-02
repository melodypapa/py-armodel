"""Parser tests for DiagnosticEventToTroubleCodeUdsMapping (Table 5.19, p.245).

XSD group DIAGNOSTIC-EVENT-TO-TROUBLE-CODE-UDS-MAPPING (AUTOSAR_00052.xsd l.37073) element order:
DIAGNOSTIC-EVENT-REF, TROUBLE-CODE-UDS-REF.
Base DIAGNOSTIC-MAPPING group (provider/requester software-cluster refs) is read
by readDiagnosticMapping.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticEventToTroubleCodeUdsMapping

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-EVENT-TO-TROUBLE-CODE-UDS-MAPPING") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticEventToTroubleCodeUdsMapping:
    def test_read_sets_all_fields(self, parser):
        mapping = DiagnosticEventToTroubleCodeUdsMapping(AUTOSAR.getInstance(), "M1")
        element = _snip(
            "<SHORT-NAME>M1</SHORT-NAME>"
            "<DIAGNOSTIC-EVENT-REF DEST='DEST'>/AUTOSAR/DiagnosticEvent1</DIAGNOSTIC-EVENT-REF><TROUBLE-CODE-UDS-REF DEST='DEST'>/AUTOSAR/TroubleCodeUds1</TROUBLE-CODE-UDS-REF>"
        )
        parser.readDiagnosticEventToTroubleCodeUdsMapping(element, mapping)
        assert mapping.getShortName() == "M1"
        assert mapping.getDiagnosticEventRef() is not None
        assert mapping.getDiagnosticEventRef().getValue() == "/AUTOSAR/DiagnosticEvent1"
        assert mapping.getTroubleCodeUdsRef() is not None
        assert mapping.getTroubleCodeUdsRef().getValue() == "/AUTOSAR/TroubleCodeUds1"

    def test_read_empty(self, parser):
        mapping = DiagnosticEventToTroubleCodeUdsMapping(AUTOSAR.getInstance(), "M1")
        element = _snip("")
        parser.readDiagnosticEventToTroubleCodeUdsMapping(element, mapping)
        assert mapping.getDiagnosticEventRef() is None
        assert mapping.getTroubleCodeUdsRef() is None
