"""Parser tests for DiagnosticJ1939FreezeFrame (Table 4.220, p.220).

XSD group DIAGNOSTIC-J-1939-FREEZE-FRAME (AUTOSAR_00052.xsd l.38959) element order:
NODE-REF, SPN-REFS/SPN-REF.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticJ1939FreezeFrame

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-J-1939-FREEZE-FRAME") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticJ1939FreezeFrame:
    def test_read_sets_all_fields(self, parser):
        freeze_frame = DiagnosticJ1939FreezeFrame(AUTOSAR.getInstance(), "FreezeFrame")
        element = _snip(
            "<SHORT-NAME>FreezeFrame</SHORT-NAME>"
            "<NODE-REF DEST='DIAGNOSTIC-J-1939-NODE'>/AUTOSAR/J1939Nodes/Node1</NODE-REF>"
            "<SPN-REFS>"
            "<SPN-REF DEST='DIAGNOSTIC-J-1939-SPN'>/AUTOSAR/Spns/Spn1</SPN-REF>"
            "<SPN-REF DEST='DIAGNOSTIC-J-1939-SPN'>/AUTOSAR/Spns/Spn2</SPN-REF>"
            "</SPN-REFS>"
        )
        parser.readDiagnosticJ1939FreezeFrame(element, freeze_frame)
        assert freeze_frame.getShortName() == "FreezeFrame"
        assert freeze_frame.getNodeRef() is not None
        assert freeze_frame.getNodeRef().getValue() == "/AUTOSAR/J1939Nodes/Node1"
        assert freeze_frame.getNodeRef().getDest() == "DIAGNOSTIC-J-1939-NODE"
        refs = freeze_frame.getSpnRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/AUTOSAR/Spns/Spn1"
        assert refs[0].getDest() == "DIAGNOSTIC-J-1939-SPN"
        assert refs[1].getValue() == "/AUTOSAR/Spns/Spn2"

    def test_read_empty(self, parser):
        freeze_frame = DiagnosticJ1939FreezeFrame(AUTOSAR.getInstance(), "FreezeFrame")
        element = _snip("")
        parser.readDiagnosticJ1939FreezeFrame(element, freeze_frame)
        assert freeze_frame.getNodeRef() is None
        assert freeze_frame.getSpnRefs() == []
