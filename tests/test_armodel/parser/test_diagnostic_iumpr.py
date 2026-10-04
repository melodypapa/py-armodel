"""
Tests for reading the DIAGNOSTIC-IUMPR element —
DiagnosticIumpr, Table 4.207 (p.210, R23-11).

DiagnosticIumpr (Base most-derived ARElement) carries two own
Attribute rows in displayed order (event, ratioKind). The XSD group
DIAGNOSTIC-IUMPR (AUTOSAR_00052.xsd l.38622) fixes the element order
EVENT-REF; RATIO-KIND.

ratioKind — DiagnosticIumprKindEnum (Table 4.208) is a stub queued
later in Group25; the RATIO-KIND literal is read as a raw literal and
cast to the enum type until its own sync (DiagnosticEvent EVENT-KIND
interim precedent).

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_iumpr.py
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
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
        """Test that RATIO-KIND is read into ratioKind as the raw literal."""
        iumpr = self._read(parser, "<SHORT-NAME>Iumpr1</SHORT-NAME><RATIO-KIND>OBSERVER-BASED</RATIO-KIND>")
        assert iumpr.getRatioKind() is not None
        assert iumpr.getRatioKind().getValue() == "OBSERVER-BASED"

    def test_read_empty_leaves_fields_unset(self, parser):
        """Test that an element without own children leaves every field unset (empty wrapper case)."""
        iumpr = self._read(parser, "<SHORT-NAME>Iumpr1</SHORT-NAME>")
        assert iumpr.getEventRef() is None
        assert iumpr.getRatioKind() is None
