"""
Tests for reading the DIAGNOSTIC-INDICATOR element —
DiagnosticIndicator, Table 4.199 (p.203, R23-11).

DiagnosticIndicator (Base most-derived ARElement) carries one own
Attribute row in displayed order. The XSD group DIAGNOSTIC-INDICATOR
(AUTOSAR_00052.xsd l.38096) fixes the element order TYPE; the preceding
HEALING-CYCLE-COUNTER-THRESHOLD carries atp.Status="removed" and is not
modeled (Rule 0015).

type — markdown Type DiagnosticIndicatorTypeEnum wins over the XSD element
type DIAGNOSTIC-INDICATOR-TYPE-ENUM-VALUE-VARIATION-POINT (atpMixedString —
value carried as element text, Rule 0015); the literal is read from the
TYPE element text and cast to the enum (DiagnosticAging THRESHOLD flattened
precedent).

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_indicator.py
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from tests.test_armodel.parser._helpers import _snip
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import DiagnosticIndicatorTypeEnum


class TestReadDiagnosticIndicator:
    """Tests for readDiagnosticIndicator — own element field values (Table 4.199)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticIndicator

        indicator = DiagnosticIndicator(AUTOSAR.getInstance(), "Indicator1")
        parser.readDiagnosticIndicator(_snip(inner, root_tag="DIAGNOSTIC-INDICATOR"), indicator)
        return indicator

    def test_read_sets_type(self, parser):
        """Test that TYPE is read into type as the indicator type literal."""
        indicator = self._read(parser, "<SHORT-NAME>Indicator1</SHORT-NAME><TYPE>MALFUNCTION</TYPE>")
        assert indicator.getShortName() == "Indicator1"
        assert indicator.getType() is not None
        assert indicator.getType().getValue() == DiagnosticIndicatorTypeEnum.MALFUNCTION

    def test_read_empty_leaves_fields_unset(self, parser):
        """Test that an element without own children leaves every field unset (empty wrapper case)."""
        indicator = self._read(parser, "<SHORT-NAME>Indicator1</SHORT-NAME>")
        assert indicator.getType() is None
