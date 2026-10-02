"""
Tests for writing the DIAGNOSTIC-DATA-BY-IDENTIFIER XML group — DiagnosticDataByIdentifier, Table 4.73 (p.113, R23-11).

DiagnosticDataByIdentifier is an abstract base: its XML group
DIAGNOSTIC-DATA-BY-IDENTIFIER (AUTOSAR_00052.xsd l.34064) carries the single
optional DATA-IDENTIFIER-REF element (DEST
DIAGNOSTIC-ABSTRACT-DATA-IDENTIFIER--SUBTYPES-ENUM). The reusable
writeDiagnosticDataByIdentifier helper is exercised through the concrete
subclass DiagnosticReadDataByIdentifier.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_data_by_identifier.py
"""

import xml.etree.ElementTree as ET
from unittest.mock import MagicMock

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticReadDataByIdentifier
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


class TestWriteDiagnosticDataByIdentifier:
    """Tests for writeDiagnosticDataByIdentifier — own element field values (Table 4.73)."""

    def test_write_data_identifier_ref(self):
        """Test that the DATA-IDENTIFIER-REF is emitted with its DEST attribute."""
        obj = DiagnosticReadDataByIdentifier(parent=MagicMock(), short_name="ReadDataByIdentifier")
        obj.setDataIdentifier(_ref("DIAGNOSTIC-DATA-IDENTIFIER", "/AUTOSAR/DiagnosticDataIdentifiers/VIN_DID"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticDataByIdentifier(parent, obj)

        ref = parent.find("DATA-IDENTIFIER-REF")
        assert ref is not None
        assert ref.text == "/AUTOSAR/DiagnosticDataIdentifiers/VIN_DID"
        assert ref.get("DEST") == "DIAGNOSTIC-DATA-IDENTIFIER"

    def test_write_unset_ref_omits_tag(self):
        """Test that an unset dataIdentifier emits no DATA-IDENTIFIER-REF element."""
        obj = DiagnosticReadDataByIdentifier(parent=MagicMock(), short_name="ReadDataByIdentifier")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticDataByIdentifier(parent, obj)

        assert len(list(parent)) == 0
        assert parent.find("DATA-IDENTIFIER-REF") is None

    def test_round_trip_preserves_field_value(self):
        """Test the write → serialize → re-parse → read-back cycle preserving the field value."""
        obj = DiagnosticReadDataByIdentifier(parent=MagicMock(), short_name="ReadDataByIdentifier")
        obj.setDataIdentifier(_ref("DIAGNOSTIC-DATA-IDENTIFIER", "/AUTOSAR/DiagnosticDataIdentifiers/VIN_DID"))

        parent = ET.Element("DIAGNOSTIC-READ-DATA-BY-IDENTIFIER", {"xmlns": "http://autosar.org/schema/r4.0"})
        ARXMLWriter().writeDiagnosticDataByIdentifier(parent, obj)
        xml_text = ET.tostring(parent, encoding="unicode")

        reloaded = DiagnosticReadDataByIdentifier(parent=MagicMock(), short_name="ReadDataByIdentifier")
        ARXMLParser().readDiagnosticDataByIdentifier(ET.fromstring(xml_text), reloaded)
        assert reloaded.getDataIdentifier() is not None
        assert reloaded.getDataIdentifier().getValue() == "/AUTOSAR/DiagnosticDataIdentifiers/VIN_DID"
        assert reloaded.getDataIdentifier().getDest() == "DIAGNOSTIC-DATA-IDENTIFIER"
