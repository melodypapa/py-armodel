"""
Tests for writing DIAGNOSTIC-TROUBLE-CODE-J-1939 elements —
DiagnosticTroubleCodeJ1939, Table 4.223 (p.222, R23-11).

DiagnosticTroubleCodeJ1939 (Base most-derived DiagnosticTroubleCode) owns the
0..1 dtcProps reference (DTC-PROPS-REF), fmi (FMI, POSITIVE-INTEGER), kind
(KIND, DIAGNOSTIC-TROUBLE-CODE-J-1939-DTC-KIND-ENUM), node reference
(NODE-REF) and spn reference (SPN-REF), AUTOSAR_00052.xsd group
DIAGNOSTIC-TROUBLE-CODE-J-1939 l.46261 (J-1939-DTC-VALUE atp.Status="removed",
not modeled).

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_trouble_code_j1939.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticTroubleCodeJ1939
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DiagnosticTroubleCodeJ1939DtcKindEnum, PositiveInteger, RefType
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticTroubleCodeJ1939:
    """Tests for writeDiagnosticTroubleCodeJ1939 — own element field values (Table 4.223)."""

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticTroubleCodeJ1939 without attributes emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticTroubleCodes")
        package.createDiagnosticTroubleCodeJ1939("Dtc1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticTroubleCodeJ1939(parent, package.getReferrableElement("Dtc1", DiagnosticTroubleCodeJ1939))

        child = parent.find("DIAGNOSTIC-TROUBLE-CODE-J-1939")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Dtc1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_all_fields_in_xsd_order(self):
        """Test that all attributes are emitted in XSD order with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticTroubleCodes")
        trouble_code = package.createDiagnosticTroubleCodeJ1939("Dtc1")
        trouble_code.setDtcPropsRef(RefType().setValue("/AUTOSAR/DtcProps/Props1").setDest("DIAGNOSTIC-TROUBLE-CODE-PROPS"))
        fmi = PositiveInteger()
        fmi.setValue("9")
        trouble_code.setFmi(fmi)
        kind = DiagnosticTroubleCodeJ1939DtcKindEnum()
        kind.setValue(DiagnosticTroubleCodeJ1939DtcKindEnum.SERVICE_ONLY)
        trouble_code.setKind(kind)
        trouble_code.setNodeRef(RefType().setValue("/AUTOSAR/J1939Nodes/Node1").setDest("DIAGNOSTIC-J-1939-NODE"))
        trouble_code.setSpnRef(RefType().setValue("/AUTOSAR/Spns/Spn1").setDest("DIAGNOSTIC-J-1939-SPN"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticTroubleCodeJ1939(parent, trouble_code)

        child = parent.find("DIAGNOSTIC-TROUBLE-CODE-J-1939")
        assert [c.tag for c in child] == ["SHORT-NAME", "DTC-PROPS-REF", "FMI", "KIND", "NODE-REF", "SPN-REF"]
        assert child.find("DTC-PROPS-REF").text == "/AUTOSAR/DtcProps/Props1"
        assert child.find("FMI").text == "9"
        assert child.find("KIND").text == "SERVICE-ONLY"
        assert child.find("NODE-REF").text == "/AUTOSAR/J1939Nodes/Node1"
        assert child.find("SPN-REF").text == "/AUTOSAR/Spns/Spn1"
