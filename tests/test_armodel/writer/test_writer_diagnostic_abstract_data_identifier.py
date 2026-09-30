"""
Tests for writing the DIAGNOSTIC-ABSTRACT-DATA-IDENTIFIER XML group — DiagnosticAbstractDataIdentifier, Table 4.4 (p.34, R23-11).

DiagnosticAbstractDataIdentifier is an abstract base: its XML group
DIAGNOSTIC-ABSTRACT-DATA-IDENTIFIER (AUTOSAR_00052.xsd l.31403) carries the single
optional ID element whose XSD type is POSITIVE-INTEGER-VALUE-VARIATION-POINT
(attribute-value variation of the atpVariation-stereotyped id attribute). The
reusable writeDiagnosticAbstractDataIdentifier helper is exercised through the
concrete subclass DiagnosticDataIdentifier.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_abstract_data_identifier.py
"""

import xml.etree.ElementTree as ET
from unittest.mock import MagicMock

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticDataIdentifier
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _positive_integer(value: str) -> PositiveInteger:
    id_value = PositiveInteger()
    id_value.setValue(value)
    return id_value


class TestWriteDiagnosticAbstractDataIdentifier:
    """Tests for writeDiagnosticAbstractDataIdentifier — own element field values (Table 4.4)."""

    def test_write_id_in_xsd_order(self):
        """Test that the ID element is emitted with its POSITIVE-INTEGER-VALUE-VARIATION-POINT wrapper after the IDENTIFIABLE group."""
        did = DiagnosticDataIdentifier(parent=MagicMock(), short_name="Di")
        did.setId(_positive_integer("4"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticAbstractDataIdentifier(parent, did)

        assert [child.tag for child in parent] == ["SHORT-NAME", "ID"]
        id_element = parent.find("ID")
        avp_element = id_element.find("POSITIVE-INTEGER-VALUE-VARIATION-POINT")
        assert avp_element is not None
        assert avp_element.text == "4"

    def test_write_unset_id_omits_tag(self):
        """Test that an unset id emits no ID element."""
        did = DiagnosticDataIdentifier(parent=MagicMock(), short_name="Di")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticAbstractDataIdentifier(parent, did)

        assert [child.tag for child in parent] == ["SHORT-NAME"]
        assert parent.find("ID") is None

    def test_round_trip(self):
        """Test the write → serialize → re-parse → read-back cycle with field values."""
        did = DiagnosticDataIdentifier(parent=MagicMock(), short_name="Di")
        did.setId(_positive_integer("4"))

        parent = ET.Element("DIAGNOSTIC-DATA-IDENTIFIER", {"xmlns": "http://autosar.org/schema/r4.0"})
        ARXMLWriter().writeDiagnosticAbstractDataIdentifier(parent, did)
        xml_text = ET.tostring(parent, encoding="unicode")

        reloaded = DiagnosticDataIdentifier(parent=MagicMock(), short_name="Di")
        ARXMLParser().readDiagnosticAbstractDataIdentifier(ET.fromstring(xml_text), reloaded)
        assert reloaded.getShortName() == "Di"
        assert reloaded.getId() is not None
        assert reloaded.getId().getValue() == 4
