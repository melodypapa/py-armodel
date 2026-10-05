"""Parser tests for DiagnosticTroubleCodeUdsToTroubleCodeObdMapping (Table 4.180, p.188).

XSD group DIAGNOSTIC-TROUBLE-CODE-UDS-TO-TROUBLE-CODE-OBD-MAPPING element order (AUTOSAR_00052.xsd): TROUBLE-CODE-OBD-REF, TROUBLE-CODE-UDS-REF.
Base DIAGNOSTIC-MAPPING group (provider/requester software-cluster refs) is read
by readDiagnosticMapping.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticTroubleCodeUdsToTroubleCodeObdMapping

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-TROUBLE-CODE-UDS-TO-TROUBLE-CODE-OBD-MAPPING") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticTroubleCodeUdsToTroubleCodeObdMapping:
    def test_read_sets_all_fields(self, parser):
        mapping = DiagnosticTroubleCodeUdsToTroubleCodeObdMapping(AUTOSAR.getInstance(), "M1")
        element = _snip(
            "<SHORT-NAME>M1</SHORT-NAME>"
            "<TROUBLE-CODE-OBD-REF DEST='DIAGNOSTIC-TROUBLE-CODE-OBD'>/AUTOSAR/TroubleCodeObd1</TROUBLE-CODE-OBD-REF>"
            "<TROUBLE-CODE-UDS-REF DEST='DIAGNOSTIC-TROUBLE-CODE-UDS'>/AUTOSAR/TroubleCodeUds1</TROUBLE-CODE-UDS-REF>"
        )
        parser.readDiagnosticTroubleCodeUdsToTroubleCodeObdMapping(element, mapping)
        assert mapping.getShortName() == "M1"
        assert mapping.getTroubleCodeObdRef() is not None
        assert mapping.getTroubleCodeObdRef().getValue() == "/AUTOSAR/TroubleCodeObd1"
        assert mapping.getTroubleCodeUdsRef() is not None
        assert mapping.getTroubleCodeUdsRef().getValue() == "/AUTOSAR/TroubleCodeUds1"

    def test_read_empty(self, parser):
        mapping = DiagnosticTroubleCodeUdsToTroubleCodeObdMapping(AUTOSAR.getInstance(), "M1")
        element = _snip("")
        parser.readDiagnosticTroubleCodeUdsToTroubleCodeObdMapping(element, mapping)
        assert mapping.getTroubleCodeObdRef() is None
        assert mapping.getTroubleCodeUdsRef() is None
