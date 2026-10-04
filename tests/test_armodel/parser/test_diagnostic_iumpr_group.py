"""
Tests for reading the DIAGNOSTIC-IUMPR-GROUP element —
DiagnosticIumprGroup, Table 4.209 (p.210, R23-11).

DiagnosticIumprGroup (Base most-derived ARElement) carries two own Attribute
rows: iumpr (kind ref, multiplicity *) and iumprGroupIdentifier (kind aggr,
multiplicity 0..1). The XSD group DIAGNOSTIC-IUMPR-GROUP
(AUTOSAR_00052.xsd l.38728) fixes the wrapper structure: the optional
IUMPR-GROUP-IDENTIFIERS wrapper holds the DIAGNOSTIC-IUMPR-GROUP-IDENTIFIER
choice element and the optional IUMPR-REFS wrapper holds an unbounded choice
of IUMPR-REF elements (DEST DIAGNOSTIC-IUMPR, atpSplitable). The XSD-only
GROUP-IDENTIFIER element carries atp.Status="removed" and is not modeled
(Rule 0015).

The referenced type DiagnosticIumpr (Table 4.207) is fully synced on this
branch. DiagnosticIumprGroupIdentifier (Table 4.210) is still an empty stub
queued later in Group25 — the reader instantiates the typed field from the
wrapper presence until that row syncs.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_iumpr_group.py
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticIumprGroup:
    """Tests for readDiagnosticIumprGroup — own element field values (Table 4.209)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticIumprGroup

        group = DiagnosticIumprGroup(AUTOSAR.getInstance(), "IumprGroup1")
        parser.readDiagnosticIumprGroup(_snip(inner, root_tag="DIAGNOSTIC-IUMPR-GROUP"), group)
        return group

    def test_read_sets_iumpr_refs(self, parser):
        """Test that the IUMPR-REFS/IUMPR-REF entries are read into iumprRefs in order with their destinations."""
        group = self._read(
            parser,
            "<SHORT-NAME>IumprGroup1</SHORT-NAME>"
            "<IUMPR-REFS>"
            '<IUMPR-REF DEST="DIAGNOSTIC-IUMPR">/AUTOSAR/DiagnosticIumprs/Iumpr1</IUMPR-REF>'
            '<IUMPR-REF DEST="DIAGNOSTIC-IUMPR">/AUTOSAR/DiagnosticIumprs/Iumpr2</IUMPR-REF>'
            "</IUMPR-REFS>",
        )
        assert group.getShortName() == "IumprGroup1"
        refs = group.getIumprRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/AUTOSAR/DiagnosticIumprs/Iumpr1"
        assert refs[0].getDest() == "DIAGNOSTIC-IUMPR"
        assert refs[1].getValue() == "/AUTOSAR/DiagnosticIumprs/Iumpr2"
        assert refs[1].getDest() == "DIAGNOSTIC-IUMPR"

    def test_read_sets_iumpr_group_identifier(self, parser):
        """Test that the IUMPR-GROUP-IDENTIFIERS wrapper instantiates the iumprGroupIdentifier aggregation (typed field over the Table 4.210 stub)."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticIumprGroupIdentifier

        group = self._read(
            parser,
            "<SHORT-NAME>IumprGroup1</SHORT-NAME>" "<IUMPR-GROUP-IDENTIFIERS>" "<DIAGNOSTIC-IUMPR-GROUP-IDENTIFIER></DIAGNOSTIC-IUMPR-GROUP-IDENTIFIER>" "</IUMPR-GROUP-IDENTIFIERS>",
        )
        identifier = group.getIumprGroupIdentifier()
        assert identifier is not None
        assert isinstance(identifier, DiagnosticIumprGroupIdentifier)

    def test_read_empty_identifier_wrapper_leaves_aggregation_none(self, parser):
        """Test that an empty IUMPR-GROUP-IDENTIFIERS wrapper leaves iumprGroupIdentifier None (empty wrapper case)."""
        group = self._read(parser, "<SHORT-NAME>IumprGroup1</SHORT-NAME><IUMPR-GROUP-IDENTIFIERS></IUMPR-GROUP-IDENTIFIERS>")
        assert group.getIumprGroupIdentifier() is None

    def test_read_empty_refs_wrapper_leaves_refs_empty(self, parser):
        """Test that an empty IUMPR-REFS wrapper leaves iumprRefs empty (empty wrapper case)."""
        group = self._read(parser, "<SHORT-NAME>IumprGroup1</SHORT-NAME><IUMPR-REFS></IUMPR-REFS>")
        assert group.getIumprRefs() == []

    def test_read_without_wrappers_leaves_own_fields_defaulted(self, parser):
        """Test that an element without the own wrappers leaves iumprRefs empty and iumprGroupIdentifier None."""
        group = self._read(parser, "<SHORT-NAME>IumprGroup1</SHORT-NAME>")
        assert group.getIumprRefs() == []
        assert group.getIumprGroupIdentifier() is None
