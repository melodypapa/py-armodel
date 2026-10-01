"""
Tests for reading the DIAGNOSTIC-ENV-SWC-MODE-ELEMENT element —
DiagnosticEnvSwcModeElement, Table 4.45 (p.89, R23-11).

DiagnosticEnvSwcModeElement (Base most-derived DiagnosticEnvModeElement, a
Referrable) carries its own 0..1 MODE-IREF of type P-MODE-IN-SYSTEM-INSTANCE-REF
— XSD group DIAGNOSTIC-ENV-SWC-MODE-ELEMENT, AUTOSAR_00052.xsd l.36081. The
MODE-IREF read is deferred until the PModeInSystemInstanceRef model class exists
(Rule 0001.10); the Referrable identity (SHORT-NAME, AR-OBJECT attributes) is
read now. It is a concrete alternative of the DiagnosticEnvironmentalCondition
MODE-ELEMENTS choice: the aggregator dispatches DIAGNOSTIC-ENV-SWC-MODE-ELEMENT
to readDiagnosticEnvSwcModeElement.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_env_swc_mode_element.py
"""

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticEnvSwcModeElement:
    """Tests for readDiagnosticEnvSwcModeElement — own element field values (Table 4.45)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
        from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.EnvironmentalCondition import DiagnosticEnvSwcModeElement

        mode_element = DiagnosticEnvSwcModeElement(AUTOSAR.getInstance(), "SwcMode1")
        element = _snip(inner, root_tag="DIAGNOSTIC-ENV-SWC-MODE-ELEMENT")
        parser.readDiagnosticEnvSwcModeElement(element, mode_element)
        return mode_element

    def test_short_name_identity_read(self, parser):
        """Test that the Referrable identity (SHORT-NAME) is read from the element."""
        inner = "<SHORT-NAME>SwcMode1</SHORT-NAME>"
        mode_element = self._read(parser, inner)
        assert mode_element.getShortName() == "SwcMode1"

    def test_mode_iref_deferred(self, parser):
        """Test that the MODE-IREF element is not read yet (PModeInSystemInstanceRef not implemented)."""
        inner = (
            "<SHORT-NAME>SwcMode1</SHORT-NAME>"
            "<MODE-IREF>"
            '<CONTEXT-COMPOSITION-REF DEST="ROOT-SW-COMPOSITION-PROTOTYPE">/AUTOSAR/System/RootSwComposition</CONTEXT-COMPOSITION-REF>'
            '<TARGET-MODE-REF DEST="MODE-DECLARATION">/AUTOSAR/ModeDcls/MDG1/Normal</TARGET-MODE-REF>'
            "</MODE-IREF>"
        )
        mode_element = self._read(parser, inner)
        assert mode_element.getModeIRef() is None

    def test_mode_elements_dispatch_reads_swc_mode_element(self, parser):
        """Test that the MODE-ELEMENTS choice dispatches DIAGNOSTIC-ENV-SWC-MODE-ELEMENT to a DiagnosticEnvSwcModeElement."""
        from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.EnvironmentalCondition import DiagnosticEnvironmentalCondition

        inner = "<SHORT-NAME>Env1</SHORT-NAME>" "<MODE-ELEMENTS>" "<DIAGNOSTIC-ENV-SWC-MODE-ELEMENT>" "<SHORT-NAME>SwcMode1</SHORT-NAME>" "</DIAGNOSTIC-ENV-SWC-MODE-ELEMENT>" "</MODE-ELEMENTS>"
        condition = DiagnosticEnvironmentalCondition(None, "Env1")
        element = _snip(inner, root_tag="DIAGNOSTIC-ENVIRONMENTAL-CONDITION")
        parser.readDiagnosticEnvironmentalCondition(element, condition)
        mode_elements = condition.getModeElements()
        assert len(mode_elements) == 1
        mode_element = mode_elements[0]
        assert type(mode_element).__name__ == "DiagnosticEnvSwcModeElement"
        assert mode_element.getShortName() == "SwcMode1"
