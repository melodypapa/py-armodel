"""
Tests for reading the DIAGNOSTIC-ENV-MODE-CONDITION element —
DiagnosticEnvModeCondition, Table 4.43 (p.89, R23-11).

DiagnosticEnvModeCondition (Base most-derived DiagnosticEnvCompareCondition —
the queue row's `ARObject` was a placeholder, the Table 4.43 Base cell names
`ARObject , DiagnosticEnvCompareCondition , DiagnosticEnvConditionFormulaPart`)
carries the inherited COMPARE-TYPE plus its own 0..1 MODE-ELEMENT-REF
(DEST DIAGNOSTIC-ENV-MODE-ELEMENT--SUBTYPES-ENUM) — XSD group
DIAGNOSTIC-ENV-MODE-CONDITION, AUTOSAR_00052.xsd l.36015. It is a concrete
DiagnosticEnvConditionFormulaPart: the formula PARTS loop dispatches
DIAGNOSTIC-ENV-MODE-CONDITION to readDiagnosticEnvModeCondition.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_env_mode_condition.py
"""

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticEnvModeCondition:
    """Tests for readDiagnosticEnvModeCondition — own element field values (Table 4.43)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.EnvironmentalCondition import DiagnosticEnvModeCondition

        condition = DiagnosticEnvModeCondition()
        element = _snip(inner, root_tag="DIAGNOSTIC-ENV-MODE-CONDITION")
        parser.readDiagnosticEnvModeCondition(element, condition)
        return condition

    def test_with_all_fields(self, parser):
        """Test that COMPARE-TYPE (inherited) and MODE-ELEMENT-REF are read with field values."""
        inner = "<COMPARE-TYPE>IS-EQUAL</COMPARE-TYPE>" '<MODE-ELEMENT-REF DEST="DIAGNOSTIC-ENV-BSW-MODE-ELEMENT">/AUTOSAR/DiagEnvConditions/Env1/ModeElements/BswMode1</MODE-ELEMENT-REF>'
        condition = self._read(parser, inner)
        assert condition.getCompareType() is not None
        assert condition.getCompareType().getValue() == "IS-EQUAL"
        mode_element_ref = condition.getModeElementRef()
        assert mode_element_ref is not None
        assert mode_element_ref.getDest() == "DIAGNOSTIC-ENV-BSW-MODE-ELEMENT"
        assert mode_element_ref.getValue() == "/AUTOSAR/DiagEnvConditions/Env1/ModeElements/BswMode1"

    def test_without_fields(self, parser):
        """Test that absent fields leave the model empty."""
        condition = self._read(parser, "")
        assert condition.getCompareType() is None
        assert condition.getModeElementRef() is None

    def test_formula_parts_dispatch_reads_mode_condition(self, parser):
        """Test that the formula PARTS loop dispatches DIAGNOSTIC-ENV-MODE-CONDITION to a DiagnosticEnvModeCondition part."""
        from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.EnvironmentalCondition import DiagnosticEnvConditionFormula

        inner = (
            "<NRC-VALUE>49</NRC-VALUE>"
            "<OP>LOGICAL-AND</OP>"
            "<PARTS>"
            "<DIAGNOSTIC-ENV-MODE-CONDITION>"
            "<COMPARE-TYPE>IS-NOT-EQUAL</COMPARE-TYPE>"
            '<MODE-ELEMENT-REF DEST="DIAGNOSTIC-ENV-SWC-MODE-ELEMENT">/AUTOSAR/DiagEnvConditions/Env1/ModeElements/SwcMode1</MODE-ELEMENT-REF>'
            "</DIAGNOSTIC-ENV-MODE-CONDITION>"
            "</PARTS>"
        )
        formula = DiagnosticEnvConditionFormula()
        element = _snip(inner, root_tag="DIAGNOSTIC-ENV-CONDITION-FORMULA")
        parser.readDiagnosticEnvConditionFormula(element, formula)
        parts = formula.getParts()
        assert len(parts) == 1
        part = parts[0]
        assert type(part).__name__ == "DiagnosticEnvModeCondition"
        assert part.getCompareType().getValue() == "IS-NOT-EQUAL"
        assert part.getModeElementRef().getValue() == "/AUTOSAR/DiagEnvConditions/Env1/ModeElements/SwcMode1"
