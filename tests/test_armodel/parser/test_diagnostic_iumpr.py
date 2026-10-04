"""
Tests for reading the DIAGNOSTIC-IUMPR element —
DiagnosticIumpr, Table 4.207 (p.210, R23-11).

DiagnosticIumpr (Base most-derived ARElement) carries two own
Attribute rows in displayed order (event, ratioKind). The XSD group
DIAGNOSTIC-IUMPR (AUTOSAR_00052.xsd l.38622) fixes the element order
EVENT-REF; RATIO-KIND.

ratioKind round-trips as the typed DiagnosticIumprKindEnum (Table 4.208)
literal — the RATIO-KIND XSD token maps to the enum value.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_iumpr.py
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DiagnosticIumprKindEnum
from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticIumpr:
    """Tests for readDiagnosticIumpr — own element field values (Table 4.207)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticIumpr

        iumpr = DiagnosticIumpr(AUTOSAR.getInstance(), "Iumpr1")
        parser.readDiagnosticIumpr(_snip(inner, root_tag="DIAGNOSTIC-IUMPR"), iumpr)
        return iumpr

    def test_read_sets_event_ref(self, parser):
        """Test that EVENT-REF is read into eventRef with its destination."""
        iumpr = self._read(parser, '<SHORT-NAME>Iumpr1</SHORT-NAME><EVENT-REF DEST="DIAGNOSTIC-EVENT">/AUTOSAR/DiagnosticEvent</EVENT-REF><RATIO-KIND>OBSERVER-BASED</RATIO-KIND>')
        assert iumpr.getShortName() == "Iumpr1"
        assert iumpr.getEventRef() is not None
        assert iumpr.getEventRef().getValue() == "/AUTOSAR/DiagnosticEvent"
        assert iumpr.getEventRef().getDest() == "DIAGNOSTIC-EVENT"

    def test_read_sets_ratio_kind(self, parser):
        """Test that the RATIO-KIND token is read as the typed enum literal."""
        iumpr = self._read(parser, "<SHORT-NAME>Iumpr1</SHORT-NAME><RATIO-KIND>OBSERVER-BASED</RATIO-KIND>")
        assert iumpr.getRatioKind() is not None
        assert isinstance(iumpr.getRatioKind(), DiagnosticIumprKindEnum)
        assert iumpr.getRatioKind().getValue() == "observerBased"

    def test_read_empty_leaves_fields_unset(self, parser):
        """Test that an element without own children leaves every field unset (empty wrapper case)."""
        iumpr = self._read(parser, "<SHORT-NAME>Iumpr1</SHORT-NAME>")
        assert iumpr.getEventRef() is None
        assert iumpr.getRatioKind() is None
