"""Parser tests for DiagnosticTroubleCodeJ1939 (Table 4.223, p.222).

XSD group DIAGNOSTIC-TROUBLE-CODE-J-1939 (AUTOSAR_00052.xsd l.46261) element order:
DTC-PROPS-REF, FMI, KIND, NODE-REF, SPN-REF (J-1939-DTC-VALUE atp.Status="removed", not modeled).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticTroubleCodeJ1939

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-TROUBLE-CODE-J-1939") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticTroubleCodeJ1939:
    def test_read_sets_all_fields(self, parser):
        trouble_code = DiagnosticTroubleCodeJ1939(AUTOSAR.getInstance(), "Dtc")
        element = _snip(
            "<SHORT-NAME>Dtc</SHORT-NAME>"
            "<DTC-PROPS-REF DEST='DIAGNOSTIC-TROUBLE-CODE-PROPS'>/AUTOSAR/DtcProps/Props1</DTC-PROPS-REF>"
            "<FMI>9</FMI>"
            "<KIND>SERVICE-ONLY</KIND>"
            "<NODE-REF DEST='DIAGNOSTIC-J-1939-NODE'>/AUTOSAR/J1939Nodes/Node1</NODE-REF>"
            "<SPN-REF DEST='DIAGNOSTIC-J-1939-SPN'>/AUTOSAR/Spns/Spn1</SPN-REF>"
        )
        parser.readDiagnosticTroubleCodeJ1939(element, trouble_code)
        assert trouble_code.getShortName() == "Dtc"
        assert trouble_code.getDtcPropsRef() is not None
        assert trouble_code.getDtcPropsRef().getValue() == "/AUTOSAR/DtcProps/Props1"
        assert trouble_code.getFmi() is not None
        assert trouble_code.getFmi().getValue() == 9
        assert trouble_code.getKind() is not None
        assert trouble_code.getKind().getValue() == "serviceOnly"
        assert trouble_code.getNodeRef().getValue() == "/AUTOSAR/J1939Nodes/Node1"
        assert trouble_code.getSpnRef().getValue() == "/AUTOSAR/Spns/Spn1"

    def test_read_kind_standard_token(self, parser):
        trouble_code = DiagnosticTroubleCodeJ1939(AUTOSAR.getInstance(), "Dtc")
        element = _snip("<KIND>STANDARD</KIND>")
        parser.readDiagnosticTroubleCodeJ1939(element, trouble_code)
        assert trouble_code.getKind().getValue() == "standard"

    def test_read_empty(self, parser):
        trouble_code = DiagnosticTroubleCodeJ1939(AUTOSAR.getInstance(), "Dtc")
        element = _snip("")
        parser.readDiagnosticTroubleCodeJ1939(element, trouble_code)
        assert trouble_code.getDtcPropsRef() is None
        assert trouble_code.getFmi() is None
        assert trouble_code.getKind() is None
        assert trouble_code.getNodeRef() is None
        assert trouble_code.getSpnRef() is None
