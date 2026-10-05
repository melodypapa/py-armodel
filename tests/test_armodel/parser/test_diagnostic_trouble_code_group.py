"""
Tests for reading the DIAGNOSTIC-TROUBLE-CODE-GROUP element —
DiagnosticTroubleCodeGroup, Table 4.162 (p.177, R23-11).

DiagnosticTroubleCodeGroup (Base most-derived ARElement) carries two Attribute rows:
dtc (DiagnosticTroubleCode, *, ref) and groupNumber (PositiveInteger, 0..1, attr).
The XSD serializes dtc as the DTCS wrapper (AUTOSAR_00052.xsd l.46211) holding
unbounded DIAGNOSTIC-TROUBLE-CODE-REF-CONDITIONAL items, each with a
DIAGNOSTIC-TROUBLE-CODE-REF — the RefConditional wrapper class is not modeled, so
the reader flattens the wrapper path into dtcRefs (twin precedent
readDiagnosticStorageConditionGroup). groupNumber is XSD-typed
POSITIVE-INTEGER-VALUE-VARIATION-POINT (l.46230) and is read through the nested
POSITIVE-INTEGER-VALUE-VARIATION-POINT child (precedent
DiagnosticEvent.confirmationThreshold). The reader is
readDiagnosticTroubleCodeGroup = readIdentifiable + the dtcRefs flatten + the
groupNumber nested value.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_trouble_code_group.py
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticTroubleCodeGroup:
    """Tests for readDiagnosticTroubleCodeGroup — own element field values (Table 4.162)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticTroubleCodeGroup

        group = DiagnosticTroubleCodeGroup(AUTOSAR.getInstance(), "TroubleCodeGroup1")
        parser.readDiagnosticTroubleCodeGroup(_snip(inner, root_tag="DIAGNOSTIC-TROUBLE-CODE-GROUP"), group)
        return group

    def test_read_sets_dtc_refs(self, parser):
        """Test that DTCS conditional refs are read into dtcRefs with their values."""
        group = self._read(
            parser,
            "<SHORT-NAME>TroubleCodeGroup1</SHORT-NAME>"
            "<DTCS>"
            "<DIAGNOSTIC-TROUBLE-CODE-REF-CONDITIONAL>"
            '<DIAGNOSTIC-TROUBLE-CODE-REF DEST="DIAGNOSTIC-TROUBLE-CODE">/DiagnosticTroubleCodes/TroubleCode1</DIAGNOSTIC-TROUBLE-CODE-REF>'
            "</DIAGNOSTIC-TROUBLE-CODE-REF-CONDITIONAL>"
            "<DIAGNOSTIC-TROUBLE-CODE-REF-CONDITIONAL>"
            '<DIAGNOSTIC-TROUBLE-CODE-REF DEST="DIAGNOSTIC-TROUBLE-CODE">/DiagnosticTroubleCodes/TroubleCode2</DIAGNOSTIC-TROUBLE-CODE-REF>'
            "</DIAGNOSTIC-TROUBLE-CODE-REF-CONDITIONAL>"
            "</DTCS>",
        )
        assert group.getShortName() == "TroubleCodeGroup1"
        refs = group.getDtcRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/DiagnosticTroubleCodes/TroubleCode1"
        assert refs[0].getDest() == "DIAGNOSTIC-TROUBLE-CODE"
        assert refs[1].getValue() == "/DiagnosticTroubleCodes/TroubleCode2"

    def test_read_sets_group_number(self, parser):
        """Test that the nested POSITIVE-INTEGER-VALUE-VARIATION-POINT under GROUP-NUMBER is read into groupNumber."""
        group = self._read(
            parser,
            "<SHORT-NAME>TroubleCodeGroup1</SHORT-NAME>" "<GROUP-NUMBER><POSITIVE-INTEGER-VALUE-VARIATION-POINT>3</POSITIVE-INTEGER-VALUE-VARIATION-POINT></GROUP-NUMBER>",
        )
        group_number = group.getGroupNumber()
        assert group_number is not None
        assert group_number.value == 3

    def test_read_empty_wrapper_leaves_refs_empty(self, parser):
        """Test that a DTCS wrapper without conditional refs leaves dtcRefs empty (empty wrapper case)."""
        group = self._read(
            parser,
            "<SHORT-NAME>TroubleCodeGroup1</SHORT-NAME><DTCS></DTCS>",
        )
        assert group.getDtcRefs() == []

    def test_read_without_wrapper_leaves_fields_default(self, parser):
        """Test that an element without DTCS/GROUP-NUMBER leaves dtcRefs empty and groupNumber None."""
        group = self._read(parser, "<SHORT-NAME>TroubleCodeGroup1</SHORT-NAME>")
        assert group.getDtcRefs() == []
        assert group.getGroupNumber() is None
