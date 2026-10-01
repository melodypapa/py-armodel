"""
Tests for reading the DIAGNOSTIC-ENV-BSW-MODE-ELEMENT element —
DiagnosticEnvBswModeElement, Table 4.46 (p.90, R23-11).

DiagnosticEnvBswModeElement (Base most-derived DiagnosticEnvModeElement, a
Referrable) carries its own 0..1 MODE-IREF of type MODE-IN-BSW-MODULE-DESCRIPTION-INSTANCE-REF
— XSD group DIAGNOSTIC-ENV-BSW-MODE-ELEMENT, AUTOSAR_00052.xsd l.35762. The
MODE-IREF read is deferred until the ModeInBswModuleDescriptionInstanceRef model
class exists (Rule 0001.10); the Referrable identity (SHORT-NAME, AR-OBJECT
attributes) is read now. It is a concrete alternative of the
DiagnosticEnvironmentalCondition MODE-ELEMENTS choice: the aggregator dispatches
DIAGNOSTIC-ENV-BSW-MODE-ELEMENT to readDiagnosticEnvBswModeElement.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_env_bsw_mode_element.py
"""

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticEnvBswModeElement:
    """Tests for readDiagnosticEnvBswModeElement — own element field values (Table 4.46)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
        from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.EnvironmentalCondition import DiagnosticEnvBswModeElement

        mode_element = DiagnosticEnvBswModeElement(AUTOSAR.getInstance(), "BswMode1")
        element = _snip(inner, root_tag="DIAGNOSTIC-ENV-BSW-MODE-ELEMENT")
        parser.readDiagnosticEnvBswModeElement(element, mode_element)
        return mode_element

    def test_short_name_identity_read(self, parser):
        """Test that the Referrable identity (SHORT-NAME) is read from the element."""
        inner = "<SHORT-NAME>BswMode1</SHORT-NAME>"
        mode_element = self._read(parser, inner)
        assert mode_element.getShortName() == "BswMode1"

    def test_mode_iref_deferred(self, parser):
        """Test that the MODE-IREF element is not read yet (ModeInBswModuleDescriptionInstanceRef not implemented)."""
        inner = (
            "<SHORT-NAME>BswMode1</SHORT-NAME>"
            "<MODE-IREF>"
            '<CONTEXT-REF DEST="BSW-MODE-DECLARATION-GROUP-PROTOTYPE">/AUTOSAR/BswM/MDGP</CONTEXT-REF>'
            '<TARGET-MODE-REF DEST="MODE-DECLARATION">/AUTOSAR/BswM/MDGP/Normal</TARGET-MODE-REF>'
            "</MODE-IREF>"
        )
        mode_element = self._read(parser, inner)
        assert mode_element.getModeIRef() is None

    def test_mode_elements_dispatch_reads_bsw_mode_element(self, parser):
        """Test that the MODE-ELEMENTS choice dispatches DIAGNOSTIC-ENV-BSW-MODE-ELEMENT to a DiagnosticEnvBswModeElement."""
        from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.EnvironmentalCondition import DiagnosticEnvironmentalCondition

        inner = "<SHORT-NAME>Env1</SHORT-NAME>" "<MODE-ELEMENTS>" "<DIAGNOSTIC-ENV-BSW-MODE-ELEMENT>" "<SHORT-NAME>BswMode1</SHORT-NAME>" "</DIAGNOSTIC-ENV-BSW-MODE-ELEMENT>" "</MODE-ELEMENTS>"
        condition = DiagnosticEnvironmentalCondition(None, "Env1")
        element = _snip(inner, root_tag="DIAGNOSTIC-ENVIRONMENTAL-CONDITION")
        parser.readDiagnosticEnvironmentalCondition(element, condition)
        mode_elements = condition.getModeElements()
        assert len(mode_elements) == 1
        mode_element = mode_elements[0]
        assert type(mode_element).__name__ == "DiagnosticEnvBswModeElement"
        assert mode_element.getShortName() == "BswMode1"
