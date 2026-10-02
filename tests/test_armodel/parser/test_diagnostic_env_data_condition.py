"""
Tests for reading the DIAGNOSTIC-ENV-DATA-CONDITION element —
DiagnosticEnvDataCondition, Table 4.41 (p.84, R23-11).

DiagnosticEnvDataCondition (Base most-derived DiagnosticEnvCompareCondition)
carries the inherited COMPARE-TYPE plus its own 0..1 COMPARE-VALUE (choice of 12
ValueSpecification alternatives) and 0..1 DATA-ELEMENT-REF — XSD group
DIAGNOSTIC-ENV-DATA-CONDITION, AUTOSAR_00052.xsd l.35873. It is a concrete
DiagnosticEnvConditionFormulaPart: the formula PARTS loop dispatches
DIAGNOSTIC-ENV-DATA-CONDITION to readDiagnosticEnvDataCondition.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_env_data_condition.py
"""

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticEnvDataCondition:
    """Tests for readDiagnosticEnvDataCondition — own element field values (Table 4.41)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.EnvironmentalCondition import DiagnosticEnvDataCondition

        condition = DiagnosticEnvDataCondition()
        element = _snip(inner, root_tag="DIAGNOSTIC-ENV-DATA-CONDITION")
        parser.readDiagnosticEnvDataCondition(element, condition)
        return condition

    def test_with_all_fields(self, parser):
        """Test that COMPARE-TYPE (inherited), COMPARE-VALUE and DATA-ELEMENT-REF are read with field values."""
        inner = (
            "<COMPARE-TYPE>IS-LESS-OR-EQUAL</COMPARE-TYPE>"
            "<COMPARE-VALUE><TEXT-VALUE-SPECIFICATION><SHORT-LABEL>Limit</SHORT-LABEL><VALUE>42</VALUE></TEXT-VALUE-SPECIFICATION></COMPARE-VALUE>"
            '<DATA-ELEMENT-REF DEST="DIAGNOSTIC-DATA-ELEMENT">/AUTOSAR/DiagDataElements/Dde1</DATA-ELEMENT-REF>'
        )
        condition = self._read(parser, inner)
        assert condition.getCompareType() is not None
        assert condition.getCompareType().getValue() == "isLessOrEqual"
        compare_value = condition.getCompareValue()
        assert compare_value is not None
        assert compare_value.getValue().getValue() == "42"
        data_element_ref = condition.getDataElementRef()
        assert data_element_ref is not None
        assert data_element_ref.getDest() == "DIAGNOSTIC-DATA-ELEMENT"
        assert data_element_ref.getValue() == "/AUTOSAR/DiagDataElements/Dde1"

    def test_without_fields(self, parser):
        """Test that absent fields leave the model empty."""
        condition = self._read(parser, "")
        assert condition.getCompareType() is None
        assert condition.getCompareValue() is None
        assert condition.getDataElementRef() is None

    def test_formula_parts_dispatch_reads_data_condition(self, parser):
        """Test that the formula PARTS loop dispatches DIAGNOSTIC-ENV-DATA-CONDITION to a DiagnosticEnvDataCondition part."""
        from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.EnvironmentalCondition import DiagnosticEnvConditionFormula

        inner = (
            "<NRC-VALUE>49</NRC-VALUE>"
            "<OP>LOGICAL-AND</OP>"
            "<PARTS>"
            "<DIAGNOSTIC-ENV-DATA-CONDITION>"
            "<COMPARE-TYPE>IS-EQUAL</COMPARE-TYPE>"
            '<DATA-ELEMENT-REF DEST="DIAGNOSTIC-DATA-ELEMENT">/AUTOSAR/DiagDataElements/Dde2</DATA-ELEMENT-REF>'
            "</DIAGNOSTIC-ENV-DATA-CONDITION>"
            "</PARTS>"
        )
        formula = DiagnosticEnvConditionFormula()
        element = _snip(inner, root_tag="DIAGNOSTIC-ENV-CONDITION-FORMULA")
        parser.readDiagnosticEnvConditionFormula(element, formula)
        parts = formula.getParts()
        assert len(parts) == 1
        part = parts[0]
        assert type(part).__name__ == "DiagnosticEnvDataCondition"
        assert part.getCompareType().getValue() == "isEqual"
        assert part.getDataElementRef().getValue() == "/AUTOSAR/DiagDataElements/Dde2"
