"""
Tests for reading the DIAGNOSTIC-ENV-DATA-ELEMENT-CONDITION element —
DiagnosticEnvDataElementCondition, Table 4.42 (p.85, R23-11).

DiagnosticEnvDataElementCondition (Base most-derived DiagnosticEnvCompareCondition)
carries the inherited COMPARE-TYPE plus its own 0..1 COMPARE-VALUE (choice of 12
ValueSpecification alternatives) and 0..1 SW-DATA-DEF-PROPS (atpSplitable
variants/conditional wrapper) — XSD group DIAGNOSTIC-ENV-DATA-ELEMENT-CONDITION,
AUTOSAR_00052.xsd l.35934. The 0..1 DATA-PROTOTYPE-IREF is deferred until the
DataPrototypeInSystemInstanceRef model class exists (Rule 0001.10). It is a
concrete DiagnosticEnvConditionFormulaPart: the formula PARTS loop dispatches
DIAGNOSTIC-ENV-DATA-ELEMENT-CONDITION to readDiagnosticEnvDataElementCondition.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_env_data_element_condition.py
"""

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticEnvDataElementCondition:
    """Tests for readDiagnosticEnvDataElementCondition — own element field values (Table 4.42)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.EnvironmentalCondition import DiagnosticEnvDataElementCondition

        condition = DiagnosticEnvDataElementCondition()
        element = _snip(inner, root_tag="DIAGNOSTIC-ENV-DATA-ELEMENT-CONDITION")
        parser.readDiagnosticEnvDataElementCondition(element, condition)
        return condition

    def test_with_all_fields(self, parser):
        """Test that COMPARE-TYPE (inherited), COMPARE-VALUE and SW-DATA-DEF-PROPS are read with field values."""
        inner = (
            "<COMPARE-TYPE>IS-EQUAL</COMPARE-TYPE>"
            "<COMPARE-VALUE><TEXT-VALUE-SPECIFICATION><SHORT-LABEL>Limit</SHORT-LABEL><VALUE>42</VALUE></TEXT-VALUE-SPECIFICATION></COMPARE-VALUE>"
            "<SW-DATA-DEF-PROPS>"
            "<SW-DATA-DEF-PROPS-VARIANTS><SW-DATA-DEF-PROPS-CONDITIONAL>"
            '<BASE-TYPE-REF DEST="SW-BASE-TYPE">/DataTypes/BaseTypes/uint8</BASE-TYPE-REF>'
            '<DATA-CONSTR-REF DEST="DATA-CONSTR">/DataTypes/Constrs/DC1</DATA-CONSTR-REF>'
            "</SW-DATA-DEF-PROPS-CONDITIONAL></SW-DATA-DEF-PROPS-VARIANTS>"
            "</SW-DATA-DEF-PROPS>"
        )
        condition = self._read(parser, inner)
        assert condition.getCompareType() is not None
        assert condition.getCompareType().getValue() == "IS-EQUAL"
        compare_value = condition.getCompareValue()
        assert compare_value is not None
        assert compare_value.getValue().getValue() == "42"
        sw_data_def_props = condition.getSwDataDefProps()
        assert sw_data_def_props is not None
        assert sw_data_def_props.getBaseTypeRef().getDest() == "SW-BASE-TYPE"
        assert sw_data_def_props.getBaseTypeRef().getValue() == "/DataTypes/BaseTypes/uint8"
        assert sw_data_def_props.getDataConstrRef().getValue() == "/DataTypes/Constrs/DC1"

    def test_without_fields(self, parser):
        """Test that absent fields leave the model empty."""
        condition = self._read(parser, "")
        assert condition.getCompareType() is None
        assert condition.getCompareValue() is None
        assert condition.getSwDataDefProps() is None

    def test_formula_parts_dispatch_reads_data_element_condition(self, parser):
        """Test that the formula PARTS loop dispatches DIAGNOSTIC-ENV-DATA-ELEMENT-CONDITION to a DiagnosticEnvDataElementCondition part."""
        from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.EnvironmentalCondition import DiagnosticEnvConditionFormula

        inner = (
            "<NRC-VALUE>49</NRC-VALUE>"
            "<OP>LOGICAL-OR</OP>"
            "<PARTS>"
            "<DIAGNOSTIC-ENV-DATA-ELEMENT-CONDITION>"
            "<COMPARE-TYPE>IS-NOT-EQUAL</COMPARE-TYPE>"
            "<COMPARE-VALUE><NUMERICAL-VALUE-SPECIFICATION><VALUE>7</VALUE></NUMERICAL-VALUE-SPECIFICATION></COMPARE-VALUE>"
            "<SW-DATA-DEF-PROPS>"
            "<SW-DATA-DEF-PROPS-VARIANTS><SW-DATA-DEF-PROPS-CONDITIONAL>"
            '<BASE-TYPE-REF DEST="SW-BASE-TYPE">/DataTypes/BaseTypes/uint8</BASE-TYPE-REF>'
            "</SW-DATA-DEF-PROPS-CONDITIONAL></SW-DATA-DEF-PROPS-VARIANTS>"
            "</SW-DATA-DEF-PROPS>"
            "</DIAGNOSTIC-ENV-DATA-ELEMENT-CONDITION>"
            "</PARTS>"
        )
        formula = DiagnosticEnvConditionFormula()
        element = _snip(inner, root_tag="DIAGNOSTIC-ENV-CONDITION-FORMULA")
        parser.readDiagnosticEnvConditionFormula(element, formula)
        parts = formula.getParts()
        assert len(parts) == 1
        part = parts[0]
        assert type(part).__name__ == "DiagnosticEnvDataElementCondition"
        assert part.getCompareType().getValue() == "IS-NOT-EQUAL"
        assert part.getCompareValue().getValue().getValue() == 7
        assert part.getSwDataDefProps().getBaseTypeRef().getValue() == "/DataTypes/BaseTypes/uint8"
