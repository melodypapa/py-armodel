"""
Tests for writing DIAGNOSTIC-J-1939-FREEZE-FRAME elements —
DiagnosticJ1939FreezeFrame, Table 4.220 (p.220, R23-11).

DiagnosticJ1939FreezeFrame (Base most-derived DiagnosticCommonElement) owns the
0..1 node reference (NODE-REF) and the ordered * spn references
(SPN-REFS/SPN-REF), AUTOSAR_00052.xsd group DIAGNOSTIC-J-1939-FREEZE-FRAME
l.38959.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_j1939_freeze_frame.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticJ1939FreezeFrame
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticJ1939FreezeFrame:
    """Tests for writeDiagnosticJ1939FreezeFrame — own element field values (Table 4.220)."""

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticJ1939FreezeFrame without references emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticJ1939FreezeFrames")
        package.createDiagnosticJ1939FreezeFrame("FreezeFrame1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticJ1939FreezeFrame(parent, package.getReferrableElement("FreezeFrame1", DiagnosticJ1939FreezeFrame))

        child = parent.find("DIAGNOSTIC-J-1939-FREEZE-FRAME")
        assert child is not None
        assert child.find("SHORT-NAME").text == "FreezeFrame1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_refs(self):
        """Test that NODE-REF and the SPN-REFS wrapper are emitted in XSD order with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticJ1939FreezeFrames")
        freeze_frame = package.createDiagnosticJ1939FreezeFrame("FreezeFrame1")
        freeze_frame.setNodeRef(RefType().setValue("/AUTOSAR/J1939Nodes/Node1").setDest("DIAGNOSTIC-J-1939-NODE"))
        freeze_frame.addSpnRef(RefType().setValue("/AUTOSAR/Spns/Spn1").setDest("DIAGNOSTIC-J-1939-SPN"))
        freeze_frame.addSpnRef(RefType().setValue("/AUTOSAR/Spns/Spn2").setDest("DIAGNOSTIC-J-1939-SPN"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticJ1939FreezeFrame(parent, freeze_frame)

        child = parent.find("DIAGNOSTIC-J-1939-FREEZE-FRAME")
        assert [c.tag for c in child] == ["SHORT-NAME", "NODE-REF", "SPN-REFS"]
        node_ref = child.find("NODE-REF")
        assert node_ref.text == "/AUTOSAR/J1939Nodes/Node1"
        assert node_ref.get("DEST") == "DIAGNOSTIC-J-1939-NODE"
        spn_refs = child.find("SPN-REFS")
        assert [ref.text for ref in spn_refs.findall("SPN-REF")] == ["/AUTOSAR/Spns/Spn1", "/AUTOSAR/Spns/Spn2"]
