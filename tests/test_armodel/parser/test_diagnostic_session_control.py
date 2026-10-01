"""
Tests for reading the DIAGNOSTIC-SESSION-CONTROL element —
DiagnosticSessionControl, Table 4.47 (p.93, R23-11).

DiagnosticSessionControl (Base most-derived ARElement, DiagnosticServiceInstance
in the chain) carries two 0..1 ref attributes — DIAGNOSTIC-SESSION-REF
(DIAGNOSTIC-SESSION--SUBTYPES-ENUM) and SESSION-CONTROL-CLASS-REF
(DIAGNOSTIC-SESSION-CONTROL-CLASS--SUBTYPES-ENUM) — XSD group
DIAGNOSTIC-SESSION-CONTROL, AUTOSAR_00052.xsd l.44381. The base groups
DIAGNOSTIC-COMMON-ELEMENT and DIAGNOSTIC-SERVICE-INSTANCE serialize nothing for
ARElement-derived service instances (the <<atpDerived>> serviceClass association
is skipped by the XSD group; the sibling DiagnosticProtocol precedent models the
chain through ARElement only).

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_session_control.py
"""

from unittest.mock import MagicMock

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticSessionControl:
    """Tests for readDiagnosticSessionControl — own element field values (Table 4.47)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticSessionControl

        session_control = DiagnosticSessionControl(parent=MagicMock(), short_name="SessionCtrl")
        element = _snip(inner, root_tag="DIAGNOSTIC-SESSION-CONTROL")
        parser.readDiagnosticSessionControl(element, session_control)
        return session_control

    def test_with_refs(self, parser):
        """Test that DIAGNOSTIC-SESSION-REF and SESSION-CONTROL-CLASS-REF are read with field values."""
        inner = (
            "<SHORT-NAME>SessionCtrl</SHORT-NAME>"
            '<DIAGNOSTIC-SESSION-REF DEST="DIAGNOSTIC-SESSION">/AUTOSAR/DiagnosticSessions/DefaultSession</DIAGNOSTIC-SESSION-REF>'
            '<SESSION-CONTROL-CLASS-REF DEST="DIAGNOSTIC-SESSION-CONTROL-CLASS">/AUTOSAR/DiagnosticSessionControls/SessionControlClass</SESSION-CONTROL-CLASS-REF>'
        )
        session_control = self._read(parser, inner)
        assert session_control.getShortName() == "SessionCtrl"
        diagnostic_session_ref = session_control.getDiagnosticSessionRef()
        assert diagnostic_session_ref is not None
        assert diagnostic_session_ref.getValue() == "/AUTOSAR/DiagnosticSessions/DefaultSession"
        assert diagnostic_session_ref.getDest() == "DIAGNOSTIC-SESSION"
        session_control_class_ref = session_control.getSessionControlClassRef()
        assert session_control_class_ref is not None
        assert session_control_class_ref.getValue() == "/AUTOSAR/DiagnosticSessionControls/SessionControlClass"
        assert session_control_class_ref.getDest() == "DIAGNOSTIC-SESSION-CONTROL-CLASS"

    def test_without_refs(self, parser):
        """Test that absent DIAGNOSTIC-SESSION-REF / SESSION-CONTROL-CLASS-REF leave the fields None."""
        session_control = self._read(parser, "<SHORT-NAME>SessionCtrl</SHORT-NAME>")
        assert session_control.getDiagnosticSessionRef() is None
        assert session_control.getSessionControlClassRef() is None
