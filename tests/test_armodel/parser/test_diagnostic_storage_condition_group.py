"""
Tests for reading the DIAGNOSTIC-STORAGE-CONDITION-GROUP element —
DiagnosticStorageConditionGroup, Table 4.195 (p.200, R23-11).

DiagnosticStorageConditionGroup (Base most-derived DiagnosticConditionGroup) carries a
single Attribute row: storageCondition (DiagnosticStorageCondition, *, ref). The XSD
serializes it as the STORAGE-CONDITIONS wrapper (AUTOSAR_00052.xsd l.45675) holding
unbounded DIAGNOSTIC-STORAGE-CONDITION-REF-CONDITIONAL items, each with a
DIAGNOSTIC-STORAGE-CONDITION-REF — the RefConditional wrapper class is not modeled, so
the reader flattens the wrapper path into storageConditionRefs (precedent
readBswModuleEntityIssuedTriggerRefs). The abstract base group
DIAGNOSTIC-CONDITION-GROUP (l.33439) is an empty sequence, so the reader is
readDiagnosticStorageConditionGroup = readIdentifiable + readDiagnosticConditionGroup
+ the storageConditionRefs flatten.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_storage_condition_group.py
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticStorageConditionGroup:
    """Tests for readDiagnosticStorageConditionGroup — own element field values (Table 4.195)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticStorageConditionGroup

        group = DiagnosticStorageConditionGroup(AUTOSAR.getInstance(), "StorageConditionGroup1")
        parser.readDiagnosticStorageConditionGroup(_snip(inner, root_tag="DIAGNOSTIC-STORAGE-CONDITION-GROUP"), group)
        return group

    def test_read_sets_storage_condition_refs(self, parser):
        """Test that STORAGE-CONDITIONS conditional refs are read into storageConditionRefs with their values."""
        group = self._read(
            parser,
            "<SHORT-NAME>StorageConditionGroup1</SHORT-NAME>"
            "<STORAGE-CONDITIONS>"
            "<DIAGNOSTIC-STORAGE-CONDITION-REF-CONDITIONAL>"
            '<DIAGNOSTIC-STORAGE-CONDITION-REF DEST="DIAGNOSTIC-STORAGE-CONDITION">/DiagnosticConditions/StorageCondition1</DIAGNOSTIC-STORAGE-CONDITION-REF>'
            "</DIAGNOSTIC-STORAGE-CONDITION-REF-CONDITIONAL>"
            "<DIAGNOSTIC-STORAGE-CONDITION-REF-CONDITIONAL>"
            '<DIAGNOSTIC-STORAGE-CONDITION-REF DEST="DIAGNOSTIC-STORAGE-CONDITION">/DiagnosticConditions/StorageCondition2</DIAGNOSTIC-STORAGE-CONDITION-REF>'
            "</DIAGNOSTIC-STORAGE-CONDITION-REF-CONDITIONAL>"
            "</STORAGE-CONDITIONS>",
        )
        assert group.getShortName() == "StorageConditionGroup1"
        refs = group.getStorageConditionRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/DiagnosticConditions/StorageCondition1"
        assert refs[0].getDest() == "DIAGNOSTIC-STORAGE-CONDITION"
        assert refs[1].getValue() == "/DiagnosticConditions/StorageCondition2"

    def test_read_empty_wrapper_leaves_refs_empty(self, parser):
        """Test that a STORAGE-CONDITIONS wrapper without conditional refs leaves storageConditionRefs empty (empty wrapper case)."""
        group = self._read(
            parser,
            "<SHORT-NAME>StorageConditionGroup1</SHORT-NAME><STORAGE-CONDITIONS></STORAGE-CONDITIONS>",
        )
        assert group.getStorageConditionRefs() == []

    def test_read_without_wrapper_leaves_refs_empty(self, parser):
        """Test that an element without STORAGE-CONDITIONS leaves storageConditionRefs empty."""
        group = self._read(parser, "<SHORT-NAME>StorageConditionGroup1</SHORT-NAME>")
        assert group.getStorageConditionRefs() == []
