"""
Tests for reading the DIAGNOSTIC-STOP-ROUTINE element — DiagnosticStopRoutine, Table 4.87 (p.125, R23-11).

DiagnosticStopRoutine (Base most-derived DiagnosticRoutineSubfunction) owns
two attributes: the `*` request/response aggregations of DiagnosticParameter
(REQUESTS/RESPONSES wrappers of DIAGNOSTIC-PARAMETER, AUTOSAR_00052.xsd group
DIAGNOSTIC-STOP-ROUTINE l.45577). It inherits the 0..1 accessPermission ref
(ACCESS-PERMISSION-REF) from the abstract DiagnosticRoutineSubfunction
(Table 4.84); the reader delegates the inherited field to the Rule 0001.7
helper readDiagnosticRoutineSubfunction. Per the XSD complexType sequence
(l.45611) the inherited ACCESS-PERMISSION-REF precedes the own REQUESTS and
RESPONSES wrappers.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_stop_routine.py
"""

from unittest.mock import MagicMock

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticStopRoutine:
    """Tests for readDiagnosticStopRoutine — own element field values (Table 4.87)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DiagnosticStopRoutine

        stop_routine = DiagnosticStopRoutine(parent=MagicMock(), short_name="StopRoutine1")
        element = _snip(inner, root_tag="DIAGNOSTIC-STOP-ROUTINE")
        parser.readDiagnosticStopRoutine(element, stop_routine)
        return stop_routine

    def test_read_short_name(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name)."""
        stop_routine = self._read(parser, "<SHORT-NAME>StopRoutine1</SHORT-NAME>")
        assert stop_routine.getShortName() == "StopRoutine1"

    def test_read_inherited_access_permission_ref(self, parser):
        """Test that the inherited ACCESS-PERMISSION-REF is read via the base helper."""
        stop_routine = self._read(parser, '<ACCESS-PERMISSION-REF DEST="DIAGNOSTIC-ACCESS-PERMISSION">/AUTOSAR/DiagnosticAccessPermissions/Level1</ACCESS-PERMISSION-REF>')
        ref = stop_routine.getAccessPermission()
        assert ref is not None
        assert ref.getValue() == "/AUTOSAR/DiagnosticAccessPermissions/Level1"
        assert ref.getDest() == "DIAGNOSTIC-ACCESS-PERMISSION"

    def test_read_requests_wrapper(self, parser):
        """Test that the REQUESTS wrapper DIAGNOSTIC-PARAMETER items are read."""
        stop_routine = self._read(
            parser,
            "<REQUESTS><DIAGNOSTIC-PARAMETER><IDENT><SHORT-NAME>ReqParam1</SHORT-NAME></IDENT></DIAGNOSTIC-PARAMETER><DIAGNOSTIC-PARAMETER><IDENT><SHORT-NAME>ReqParam2</SHORT-NAME></IDENT></DIAGNOSTIC-PARAMETER></REQUESTS>",
        )
        requests = stop_routine.getRequest()
        assert len(requests) == 2
        assert requests[0].getIdent() is not None
        assert requests[0].getIdent().getShortName() == "ReqParam1"
        assert requests[1].getIdent() is not None
        assert requests[1].getIdent().getShortName() == "ReqParam2"

    def test_read_responses_wrapper(self, parser):
        """Test that the RESPONSES wrapper DIAGNOSTIC-PARAMETER items are read."""
        stop_routine = self._read(parser, "<RESPONSES><DIAGNOSTIC-PARAMETER><IDENT><SHORT-NAME>RespParam1</SHORT-NAME></IDENT></DIAGNOSTIC-PARAMETER></RESPONSES>")
        responses = stop_routine.getResponse()
        assert len(responses) == 1
        assert responses[0].getIdent() is not None
        assert responses[0].getIdent().getShortName() == "RespParam1"

    def test_read_empty_wrappers_omitted(self, parser):
        """Test that absent REQUESTS/RESPONSES wrappers leave both lists empty."""
        stop_routine = self._read(parser, "<SHORT-NAME>StopRoutine1</SHORT-NAME>")
        assert stop_routine.getRequest() == []
        assert stop_routine.getResponse() == []
