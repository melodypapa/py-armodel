"""
Tests for reading the DIAGNOSTIC-ENABLE-CONDITION element —
DiagnosticEnableCondition, Table 4.185 (p.194, R23-11).

DiagnosticEnableCondition (Base most-derived DiagnosticCondition) carries no own
Attribute rows — its XSD group DIAGNOSTIC-ENABLE-CONDITION (AUTOSAR_00052.xsd
l.35506) is an empty sequence and the INIT-VALUE child comes from the base group
DIAGNOSTIC-CONDITION (l.33411), so the reader is readDiagnosticEnableCondition =
readIdentifiable + readDiagnosticCondition.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_enable_condition.py
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticEnableCondition:
    """Tests for readDiagnosticEnableCondition — own element field values (Table 4.185)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticEnableCondition

        enable_condition = DiagnosticEnableCondition(AUTOSAR.getInstance(), "EnableCondition1")
        parser.readDiagnosticEnableCondition(_snip(inner, root_tag="DIAGNOSTIC-ENABLE-CONDITION"), enable_condition)
        return enable_condition

    def test_read_sets_init_value_true(self, parser):
        """Test that the inherited INIT-VALUE true is read into initValue."""
        enable_condition = self._read(parser, "<SHORT-NAME>EnableCondition1</SHORT-NAME><INIT-VALUE>true</INIT-VALUE>")
        assert enable_condition.getShortName() == "EnableCondition1"
        assert enable_condition.getInitValue() is not None
        assert enable_condition.getInitValue().value is True

    def test_read_sets_init_value_false(self, parser):
        """Test that the inherited INIT-VALUE false is read into initValue."""
        enable_condition = self._read(parser, "<INIT-VALUE>false</INIT-VALUE>")
        assert enable_condition.getInitValue() is not None
        assert enable_condition.getInitValue().value is False

    def test_read_empty_leaves_init_value_none(self, parser):
        """Test that an element without INIT-VALUE leaves the inherited initValue None (empty wrapper case)."""
        enable_condition = self._read(parser, "<SHORT-NAME>EnableCondition1</SHORT-NAME>")
        assert enable_condition.getInitValue() is None
