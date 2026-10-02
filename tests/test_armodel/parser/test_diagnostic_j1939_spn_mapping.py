"""Parser tests for DiagnosticJ1939SpnMapping (Table 5.40, p.267).

XSD group DIAGNOSTIC-J-1939-SPN-MAPPING element order (AUTOSAR_00052.xsd): SENDING-NODE-REFS, SPN-REF, SYSTEM-SIGNAL-REF.
Base DIAGNOSTIC-MAPPING group (provider/requester software-cluster refs) is read
by readDiagnosticMapping.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticJ1939SpnMapping

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-J-1939-SPN-MAPPING") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticJ1939SpnMapping:
    def test_read_sets_all_fields(self, parser):
        mapping = DiagnosticJ1939SpnMapping(AUTOSAR.getInstance(), "M1")
        element = _snip(
            "<SHORT-NAME>M1</SHORT-NAME>"
            "<SENDING-NODE-REFS><SENDING-NODE-REF DEST='DEST'>/AUTOSAR/SendingNode1</SENDING-NODE-REF></SENDING-NODE-REFS><SPN-REF DEST='DEST'>/AUTOSAR/Spn1</SPN-REF><SYSTEM-SIGNAL-REF DEST='DEST'>/AUTOSAR/SystemSignal1</SYSTEM-SIGNAL-REF>"
        )
        parser.readDiagnosticJ1939SpnMapping(element, mapping)
        assert mapping.getShortName() == "M1"
        assert len(mapping.getSendingNodeRefs()) == 1
        assert mapping.getSendingNodeRefs()[0].getValue() == "/AUTOSAR/SendingNode1"
        assert mapping.getSpnRef() is not None
        assert mapping.getSpnRef().getValue() == "/AUTOSAR/Spn1"
        assert mapping.getSystemSignalRef() is not None
        assert mapping.getSystemSignalRef().getValue() == "/AUTOSAR/SystemSignal1"

    def test_read_empty(self, parser):
        mapping = DiagnosticJ1939SpnMapping(AUTOSAR.getInstance(), "M1")
        element = _snip("")
        parser.readDiagnosticJ1939SpnMapping(element, mapping)
        assert mapping.getSendingNodeRefs() == []
        assert mapping.getSpnRef() is None
        assert mapping.getSystemSignalRef() is None
