"""
Tests for writing DIAGNOSTIC-J-1939-EXPANDED-FREEZE-FRAME elements —
DiagnosticJ1939ExpandedFreezeFrame, Table 4.221 (p.221, R23-11).

DiagnosticJ1939ExpandedFreezeFrame (Base most-derived DiagnosticCommonElement)
owns the 0..1 node reference (NODE-REF) and the ordered * spn references
(SPN-REFS/SPN-REF), AUTOSAR_00052.xsd group
DIAGNOSTIC-J-1939-EXPANDED-FREEZE-FRAME l.38896.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_j1939_expanded_freeze_frame.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticJ1939ExpandedFreezeFrame
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticJ1939ExpandedFreezeFrame:
    """Tests for writeDiagnosticJ1939ExpandedFreezeFrame — own element field values (Table 4.221)."""

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticJ1939ExpandedFreezeFrame without references emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticJ1939ExpandedFreezeFrames")
        package.createDiagnosticJ1939ExpandedFreezeFrame("ExpandedFreezeFrame1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticJ1939ExpandedFreezeFrame(parent, package.getElement("ExpandedFreezeFrame1", DiagnosticJ1939ExpandedFreezeFrame))

        child = parent.find("DIAGNOSTIC-J-1939-EXPANDED-FREEZE-FRAME")
        assert child is not None
        assert child.find("SHORT-NAME").text == "ExpandedFreezeFrame1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_refs(self):
        """Test that NODE-REF and the SPN-REFS wrapper are emitted in XSD order with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticJ1939ExpandedFreezeFrames")
        expanded_freeze_frame = package.createDiagnosticJ1939ExpandedFreezeFrame("ExpandedFreezeFrame1")
        expanded_freeze_frame.setNodeRef(RefType().setValue("/AUTOSAR/J1939Nodes/Node1").setDest("DIAGNOSTIC-J-1939-NODE"))
        expanded_freeze_frame.addSpnRef(RefType().setValue("/AUTOSAR/Spns/Spn1").setDest("DIAGNOSTIC-J-1939-SPN"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticJ1939ExpandedFreezeFrame(parent, expanded_freeze_frame)

        child = parent.find("DIAGNOSTIC-J-1939-EXPANDED-FREEZE-FRAME")
        assert [c.tag for c in child] == ["SHORT-NAME", "NODE-REF", "SPN-REFS"]
        node_ref = child.find("NODE-REF")
        assert node_ref.text == "/AUTOSAR/J1939Nodes/Node1"
        assert node_ref.get("DEST") == "DIAGNOSTIC-J-1939-NODE"
        spn_refs = child.find("SPN-REFS")
        assert [ref.text for ref in spn_refs.findall("SPN-REF")] == ["/AUTOSAR/Spns/Spn1"]
