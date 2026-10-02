"""
Tests for writing the DIAGNOSTIC-ROUTINE-SUBFUNCTION XML group — DiagnosticRoutineSubfunction, Table 4.84 (p.121, R23-11).

DiagnosticRoutineSubfunction is an abstract base: its XML group
DIAGNOSTIC-ROUTINE-SUBFUNCTION (AUTOSAR_00052.xsd l.43145) carries the single
optional ACCESS-PERMISSION-REF element (DEST
DIAGNOSTIC-ACCESS-PERMISSION--SUBTYPES-ENUM). The reusable
writeDiagnosticRoutineSubfunction helper is exercised through the concrete
subclass DiagnosticStartRoutine.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_routine_subfunction.py
"""

import xml.etree.ElementTree as ET
from unittest.mock import MagicMock

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DiagnosticStartRoutine
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _ref(dest: str, value: str) -> RefType:
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


class TestWriteDiagnosticRoutineSubfunction:
    """Tests for writeDiagnosticRoutineSubfunction — own element field values (Table 4.84)."""

    def test_write_access_permission_ref(self):
        """Test that the ACCESS-PERMISSION-REF is emitted with its DEST attribute."""
        obj = DiagnosticStartRoutine(parent=MagicMock(), short_name="StartRoutine1")
        obj.setAccessPermission(_ref("DIAGNOSTIC-ACCESS-PERMISSION", "/AUTOSAR/DiagnosticAccessPermissions/Level1"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticRoutineSubfunction(parent, obj)

        ref = parent.find("ACCESS-PERMISSION-REF")
        assert ref is not None
        assert ref.text == "/AUTOSAR/DiagnosticAccessPermissions/Level1"
        assert ref.get("DEST") == "DIAGNOSTIC-ACCESS-PERMISSION"

    def test_write_unset_ref_omits_tag(self):
        """Test that an unset accessPermission emits no ACCESS-PERMISSION-REF element."""
        obj = DiagnosticStartRoutine(parent=MagicMock(), short_name="StartRoutine1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticRoutineSubfunction(parent, obj)

        assert len(list(parent)) == 0
        assert parent.find("ACCESS-PERMISSION-REF") is None

    def test_round_trip_preserves_field_value(self):
        """Test the write → serialize → re-parse → read-back cycle preserving the field value."""
        obj = DiagnosticStartRoutine(parent=MagicMock(), short_name="StartRoutine1")
        obj.setAccessPermission(_ref("DIAGNOSTIC-ACCESS-PERMISSION", "/AUTOSAR/DiagnosticAccessPermissions/Level1"))

        parent = ET.Element("DIAGNOSTIC-START-ROUTINE", {"xmlns": "http://autosar.org/schema/r4.0"})
        ARXMLWriter().writeDiagnosticRoutineSubfunction(parent, obj)
        xml_text = ET.tostring(parent, encoding="unicode")

        reloaded = DiagnosticStartRoutine(parent=MagicMock(), short_name="StartRoutine1")
        ARXMLParser().readDiagnosticRoutineSubfunction(ET.fromstring(xml_text), reloaded)
        assert reloaded.getAccessPermission() is not None
        assert reloaded.getAccessPermission().getValue() == "/AUTOSAR/DiagnosticAccessPermissions/Level1"
        assert reloaded.getAccessPermission().getDest() == "DIAGNOSTIC-ACCESS-PERMISSION"
