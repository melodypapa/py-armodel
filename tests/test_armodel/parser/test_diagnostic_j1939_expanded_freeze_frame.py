"""Parser tests for DiagnosticJ1939ExpandedFreezeFrame (Table 4.221, p.221).

XSD group DIAGNOSTIC-J-1939-EXPANDED-FREEZE-FRAME (AUTOSAR_00052.xsd l.38896)
element order: NODE-REF, SPN-REFS/SPN-REF.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticJ1939ExpandedFreezeFrame

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-J-1939-EXPANDED-FREEZE-FRAME") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticJ1939ExpandedFreezeFrame:
    def test_read_sets_all_fields(self, parser):
        expanded_freeze_frame = DiagnosticJ1939ExpandedFreezeFrame(AUTOSAR.getInstance(), "ExpandedFreezeFrame")
        element = _snip(
            "<SHORT-NAME>ExpandedFreezeFrame</SHORT-NAME>"
            "<NODE-REF DEST='DIAGNOSTIC-J-1939-NODE'>/AUTOSAR/J1939Nodes/Node1</NODE-REF>"
            "<SPN-REFS>"
            "<SPN-REF DEST='DIAGNOSTIC-J-1939-SPN'>/AUTOSAR/Spns/Spn1</SPN-REF>"
            "</SPN-REFS>"
        )
        parser.readDiagnosticJ1939ExpandedFreezeFrame(element, expanded_freeze_frame)
        assert expanded_freeze_frame.getShortName() == "ExpandedFreezeFrame"
        assert expanded_freeze_frame.getNodeRef() is not None
        assert expanded_freeze_frame.getNodeRef().getValue() == "/AUTOSAR/J1939Nodes/Node1"
        refs = expanded_freeze_frame.getSpnRefs()
        assert len(refs) == 1
        assert refs[0].getValue() == "/AUTOSAR/Spns/Spn1"
        assert refs[0].getDest() == "DIAGNOSTIC-J-1939-SPN"

    def test_read_empty(self, parser):
        expanded_freeze_frame = DiagnosticJ1939ExpandedFreezeFrame(AUTOSAR.getInstance(), "ExpandedFreezeFrame")
        element = _snip("")
        parser.readDiagnosticJ1939ExpandedFreezeFrame(element, expanded_freeze_frame)
        assert expanded_freeze_frame.getNodeRef() is None
        assert expanded_freeze_frame.getSpnRefs() == []
