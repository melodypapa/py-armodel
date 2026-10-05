"""
Tests for reading the DIAGNOSTIC-STORAGE-CONDITION element —
DiagnosticStorageCondition, Table 4.186 (p.194, R23-11).

DiagnosticStorageCondition (Base most-derived DiagnosticCondition) carries no own
Attribute rows — its XSD group DIAGNOSTIC-STORAGE-CONDITION (AUTOSAR_00052.xsd
l.45629) is an empty sequence and the INIT-VALUE child comes from the base group
DIAGNOSTIC-CONDITION (l.33411), so the reader is readDiagnosticStorageCondition =
readIdentifiable + readDiagnosticCondition.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_storage_condition.py
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticStorageCondition:
    """Tests for readDiagnosticStorageCondition — own element field values (Table 4.186)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticStorageCondition

        storage_condition = DiagnosticStorageCondition(AUTOSAR.getInstance(), "StorageCondition1")
        parser.readDiagnosticStorageCondition(_snip(inner, root_tag="DIAGNOSTIC-STORAGE-CONDITION"), storage_condition)
        return storage_condition

    def test_read_sets_init_value_true(self, parser):
        """Test that the inherited INIT-VALUE true is read into initValue."""
        storage_condition = self._read(parser, "<SHORT-NAME>StorageCondition1</SHORT-NAME><INIT-VALUE>true</INIT-VALUE>")
        assert storage_condition.getShortName() == "StorageCondition1"
        assert storage_condition.getInitValue() is not None
        assert storage_condition.getInitValue().value is True

    def test_read_sets_init_value_false(self, parser):
        """Test that the inherited INIT-VALUE false is read into initValue."""
        storage_condition = self._read(parser, "<INIT-VALUE>false</INIT-VALUE>")
        assert storage_condition.getInitValue() is not None
        assert storage_condition.getInitValue().value is False

    def test_read_empty_leaves_init_value_none(self, parser):
        """Test that an element without INIT-VALUE leaves the inherited initValue None (empty wrapper case)."""
        storage_condition = self._read(parser, "<SHORT-NAME>StorageCondition1</SHORT-NAME>")
        assert storage_condition.getInitValue() is None
