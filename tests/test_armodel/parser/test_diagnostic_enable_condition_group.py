"""
Tests for reading the DIAGNOSTIC-ENABLE-CONDITION-GROUP element —
DiagnosticEnableConditionGroup, Table 4.194 (p.200, R23-11).

DiagnosticEnableConditionGroup (Base most-derived DiagnosticConditionGroup) carries a
single Attribute row: enableCondition (DiagnosticEnableCondition, *, ref). The XSD
serializes it as the ENABLE-CONDITIONS wrapper (AUTOSAR_00052.xsd l.35542) holding
unbounded DIAGNOSTIC-ENABLE-CONDITION-REF-CONDITIONAL items, each with a
DIAGNOSTIC-ENABLE-CONDITION-REF — the RefConditional wrapper class is not modeled, so
the reader flattens the wrapper path into enableConditionRefs (precedent
readBswModuleEntityIssuedTriggerRefs). The abstract base group
DIAGNOSTIC-CONDITION-GROUP (l.33439) is an empty sequence, so the reader is
readDiagnosticEnableConditionGroup = readIdentifiable + readDiagnosticConditionGroup
+ the enableConditionRefs flatten.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_enable_condition_group.py
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticEnableConditionGroup:
    """Tests for readDiagnosticEnableConditionGroup — own element field values (Table 4.194)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticEnableConditionGroup

        group = DiagnosticEnableConditionGroup(AUTOSAR.getInstance(), "EnableConditionGroup1")
        parser.readDiagnosticEnableConditionGroup(_snip(inner, root_tag="DIAGNOSTIC-ENABLE-CONDITION-GROUP"), group)
        return group

    def test_read_sets_enable_condition_refs(self, parser):
        """Test that ENABLE-CONDITIONS conditional refs are read into enableConditionRefs with their values."""
        group = self._read(
            parser,
            "<SHORT-NAME>EnableConditionGroup1</SHORT-NAME>"
            "<ENABLE-CONDITIONS>"
            "<DIAGNOSTIC-ENABLE-CONDITION-REF-CONDITIONAL>"
            '<DIAGNOSTIC-ENABLE-CONDITION-REF DEST="DIAGNOSTIC-ENABLE-CONDITION">/DiagnosticConditions/EnableCondition1</DIAGNOSTIC-ENABLE-CONDITION-REF>'
            "</DIAGNOSTIC-ENABLE-CONDITION-REF-CONDITIONAL>"
            "<DIAGNOSTIC-ENABLE-CONDITION-REF-CONDITIONAL>"
            '<DIAGNOSTIC-ENABLE-CONDITION-REF DEST="DIAGNOSTIC-ENABLE-CONDITION">/DiagnosticConditions/EnableCondition2</DIAGNOSTIC-ENABLE-CONDITION-REF>'
            "</DIAGNOSTIC-ENABLE-CONDITION-REF-CONDITIONAL>"
            "</ENABLE-CONDITIONS>",
        )
        assert group.getShortName() == "EnableConditionGroup1"
        refs = group.getEnableConditionRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/DiagnosticConditions/EnableCondition1"
        assert refs[0].getDest() == "DIAGNOSTIC-ENABLE-CONDITION"
        assert refs[1].getValue() == "/DiagnosticConditions/EnableCondition2"

    def test_read_empty_wrapper_leaves_refs_empty(self, parser):
        """Test that an ENABLE-CONDITIONS wrapper without conditional refs leaves enableConditionRefs empty (empty wrapper case)."""
        group = self._read(
            parser,
            "<SHORT-NAME>EnableConditionGroup1</SHORT-NAME><ENABLE-CONDITIONS></ENABLE-CONDITIONS>",
        )
        assert group.getEnableConditionRefs() == []

    def test_read_without_wrapper_leaves_refs_empty(self, parser):
        """Test that an element without ENABLE-CONDITIONS leaves enableConditionRefs empty."""
        group = self._read(parser, "<SHORT-NAME>EnableConditionGroup1</SHORT-NAME>")
        assert group.getEnableConditionRefs() == []
