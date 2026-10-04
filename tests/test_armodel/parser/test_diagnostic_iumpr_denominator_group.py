"""
Tests for reading the DIAGNOSTIC-IUMPR-DENOMINATOR-GROUP element —
DiagnosticIumprDenominatorGroup, Table 4.211 (p.211, R23-11).

DiagnosticIumprDenominatorGroup (Base most-derived ARElement) carries one own
Attribute row: iumpr (kind ref, multiplicity *). The XSD group
DIAGNOSTIC-IUMPR-DENOMINATOR-GROUP (AUTOSAR_00052.xsd l.38677) fixes the
wrapper structure: the optional IUMPR-REFS wrapper holds an unbounded choice
of IUMPR-REF elements (DEST DIAGNOSTIC-IUMPR, atpSplitable).

The referenced type DiagnosticIumpr (Table 4.207) is fully synced on this
branch.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_iumpr_denominator_group.py
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticIumprDenominatorGroup:
    """Tests for readDiagnosticIumprDenominatorGroup — own element field values (Table 4.211)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticIumprDenominatorGroup

        group = DiagnosticIumprDenominatorGroup(AUTOSAR.getInstance(), "DenominatorGroup1")
        parser.readDiagnosticIumprDenominatorGroup(_snip(inner, root_tag="DIAGNOSTIC-IUMPR-DENOMINATOR-GROUP"), group)
        return group

    def test_read_sets_iumpr_refs(self, parser):
        """Test that the IUMPR-REFS/IUMPR-REF entries are read into iumprRefs in order with their destinations."""
        group = self._read(
            parser,
            "<SHORT-NAME>DenominatorGroup1</SHORT-NAME>"
            "<IUMPR-REFS>"
            '<IUMPR-REF DEST="DIAGNOSTIC-IUMPR">/AUTOSAR/DiagnosticIumprs/Iumpr1</IUMPR-REF>'
            '<IUMPR-REF DEST="DIAGNOSTIC-IUMPR">/AUTOSAR/DiagnosticIumprs/Iumpr2</IUMPR-REF>'
            "</IUMPR-REFS>",
        )
        assert group.getShortName() == "DenominatorGroup1"
        refs = group.getIumprRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/AUTOSAR/DiagnosticIumprs/Iumpr1"
        assert refs[0].getDest() == "DIAGNOSTIC-IUMPR"
        assert refs[1].getValue() == "/AUTOSAR/DiagnosticIumprs/Iumpr2"
        assert refs[1].getDest() == "DIAGNOSTIC-IUMPR"

    def test_read_empty_wrapper_leaves_refs_empty(self, parser):
        """Test that an empty IUMPR-REFS wrapper leaves iumprRefs empty (empty wrapper case)."""
        group = self._read(parser, "<SHORT-NAME>DenominatorGroup1</SHORT-NAME><IUMPR-REFS></IUMPR-REFS>")
        assert group.getIumprRefs() == []

    def test_read_without_wrapper_leaves_refs_empty(self, parser):
        """Test that an element without the IUMPR-REFS wrapper leaves iumprRefs empty."""
        group = self._read(parser, "<SHORT-NAME>DenominatorGroup1</SHORT-NAME>")
        assert group.getIumprRefs() == []
