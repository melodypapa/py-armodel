"""
Tests for reading the DIAGNOSTIC-FUNCTION-IDENTIFIER element —
DiagnosticFunctionIdentifier, Table 4.214 (p.215, R23-11).

DiagnosticFunctionIdentifier (Base most-derived ARElement) carries NO own
Attribute rows — an identity-only FID marker class aggregated by
ARPackage.element. The XSD group DIAGNOSTIC-FUNCTION-IDENTIFIER
(AUTOSAR_00052.xsd l.37879) is an empty xsd:sequence, so the reader replays
only the inherited Identifiable content (SHORT-NAME, DESC, ...) via
readIdentifiable.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_function_identifier.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticFunctionIdentifier

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-FUNCTION-IDENTIFIER") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticFunctionIdentifier:
    """Tests for readDiagnosticFunctionIdentifier — inherited Identifiable field values (Table 4.214)."""

    def test_read_sets_short_name(self, parser):
        """Test that SHORT-NAME is replayed into the inherited short name."""
        identifier = DiagnosticFunctionIdentifier(AUTOSAR.getInstance(), "FID1")
        element = _snip("<SHORT-NAME>FID1</SHORT-NAME>")
        parser.readDiagnosticFunctionIdentifier(element, identifier)
        assert identifier.getShortName() == "FID1"

    def test_read_sets_desc(self, parser):
        """Test that DESC is read into the inherited desc MultiLanguageOverviewParagraph."""
        identifier = DiagnosticFunctionIdentifier(AUTOSAR.getInstance(), "FID1")
        element = _snip("<SHORT-NAME>FID1</SHORT-NAME><DESC><L-2>FID description</L-2></DESC>")
        parser.readDiagnosticFunctionIdentifier(element, identifier)
        assert identifier.getDesc() is not None
        assert identifier.getDesc().getL2s()[0].getValue() == "FID description"

    def test_read_empty_leaves_fields_unset(self, parser):
        """Test that an element without own children leaves the inherited content unset (empty wrapper case)."""
        identifier = DiagnosticFunctionIdentifier(AUTOSAR.getInstance(), "FID1")
        element = _snip("<SHORT-NAME>FID1</SHORT-NAME>")
        parser.readDiagnosticFunctionIdentifier(element, identifier)
        assert identifier.getDesc() is None
        assert identifier.getCategory() is None
