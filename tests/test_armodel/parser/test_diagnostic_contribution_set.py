"""
Tests for reading the DIAGNOSTIC-CONTRIBUTION-SET element — DiagnosticContributionSet, Table 4.14 (p.57, R23-11).

DiagnosticContributionSet (Base = ARElement) carries COMMON-PROPERTIES
(DiagnosticCommonProps, 0..1 aggr) and the two wrapper reference lists
ELEMENTS (DIAGNOSTIC-COMMON-ELEMENT-REF-CONDITIONAL items) and SERVICE-TABLES
(DIAGNOSTIC-SERVICE-TABLE-REF-CONDITIONAL items) — XSD group
DIAGNOSTIC-CONTRIBUTION-SET, AUTOSAR_00052.xsd l.33717. The removed
ecuInstance attribute (atp.Status="removed", ECU-INSTANCE-REFS) is not modeled.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_contribution_set.py
"""

from unittest.mock import MagicMock

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticContributionSet:
    """Tests for readDiagnosticContributionSet — own element field values (Table 4.14)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticContributionSet

        contribution_set = DiagnosticContributionSet(parent=MagicMock(), short_name="Dcs")
        element = _snip(inner, root_tag="DIAGNOSTIC-CONTRIBUTION-SET")
        parser.readDiagnosticContributionSet(element, contribution_set)
        return contribution_set

    def test_with_common_properties(self, parser):
        """Test that a COMMON-PROPERTIES element yields a DiagnosticCommonProps instance."""
        contribution_set = self._read(parser, "<SHORT-NAME>Dcs</SHORT-NAME><COMMON-PROPERTIES/>")
        assert contribution_set.getShortName() == "Dcs"
        assert contribution_set.getCommonProperties() is not None

    def test_without_common_properties(self, parser):
        """Test that an absent COMMON-PROPERTIES element leaves commonProperties None."""
        contribution_set = self._read(parser, "<SHORT-NAME>Dcs</SHORT-NAME>")
        assert contribution_set.getCommonProperties() is None

    def test_with_element_refs(self, parser):
        """Test that ELEMENTS items are read through the REF-CONDITIONAL wrapper with DEST and value."""
        inner = (
            "<SHORT-NAME>Dcs</SHORT-NAME>"
            "<ELEMENTS>"
            "<DIAGNOSTIC-COMMON-ELEMENT-REF-CONDITIONAL>"
            '<DIAGNOSTIC-COMMON-ELEMENT-REF DEST="DIAGNOSTIC-COMMON-ELEMENT">/AUTOSAR/DiagnosticCommonElements/Did</DIAGNOSTIC-COMMON-ELEMENT-REF>'
            "</DIAGNOSTIC-COMMON-ELEMENT-REF-CONDITIONAL>"
            "<DIAGNOSTIC-COMMON-ELEMENT-REF-CONDITIONAL>"
            '<DIAGNOSTIC-COMMON-ELEMENT-REF DEST="DIAGNOSTIC-COMMON-ELEMENT">/AUTOSAR/DiagnosticCommonElements/Rid</DIAGNOSTIC-COMMON-ELEMENT-REF>'
            "</DIAGNOSTIC-COMMON-ELEMENT-REF-CONDITIONAL>"
            "</ELEMENTS>"
        )
        contribution_set = self._read(parser, inner)
        refs = contribution_set.getElementRefs()
        assert len(refs) == 2
        assert refs[0].getDest() == "DIAGNOSTIC-COMMON-ELEMENT"
        assert refs[0].getValue() == "/AUTOSAR/DiagnosticCommonElements/Did"
        assert refs[1].getValue() == "/AUTOSAR/DiagnosticCommonElements/Rid"

    def test_with_empty_elements_wrapper(self, parser):
        """Test that an empty ELEMENTS wrapper yields an empty elementRefs list."""
        contribution_set = self._read(parser, "<SHORT-NAME>Dcs</SHORT-NAME><ELEMENTS/>")
        assert contribution_set.getElementRefs() == []

    def test_with_service_table_refs(self, parser):
        """Test that SERVICE-TABLES items are read through the REF-CONDITIONAL wrapper with DEST and value."""
        inner = (
            "<SHORT-NAME>Dcs</SHORT-NAME>"
            "<SERVICE-TABLES>"
            "<DIAGNOSTIC-SERVICE-TABLE-REF-CONDITIONAL>"
            '<DIAGNOSTIC-SERVICE-TABLE-REF DEST="DIAGNOSTIC-SERVICE-TABLE">/AUTOSAR/DiagnosticServiceTables/Table</DIAGNOSTIC-SERVICE-TABLE-REF>'
            "</DIAGNOSTIC-SERVICE-TABLE-REF-CONDITIONAL>"
            "</SERVICE-TABLES>"
        )
        contribution_set = self._read(parser, inner)
        refs = contribution_set.getServiceTableRefs()
        assert len(refs) == 1
        assert refs[0].getDest() == "DIAGNOSTIC-SERVICE-TABLE"
        assert refs[0].getValue() == "/AUTOSAR/DiagnosticServiceTables/Table"

    def test_without_service_tables(self, parser):
        """Test that an absent SERVICE-TABLES wrapper leaves serviceTableRefs empty."""
        contribution_set = self._read(parser, "<SHORT-NAME>Dcs</SHORT-NAME>")
        assert contribution_set.getServiceTableRefs() == []
