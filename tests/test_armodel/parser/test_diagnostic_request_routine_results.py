"""
Tests for reading the DIAGNOSTIC-REQUEST-ROUTINE-RESULTS element — DiagnosticRequestRoutineResults, Table 4.88 (p.125, R23-11).

DiagnosticRequestRoutineResults (Base most-derived DiagnosticRoutineSubfunction)
owns two attributes: the `*` request/response aggregations of
DiagnosticParameter (REQUESTS/RESPONSES wrappers of DIAGNOSTIC-PARAMETER,
AUTOSAR_00052.xsd group DIAGNOSTIC-REQUEST-ROUTINE-RESULTS l.42402). It
inherits the 0..1 accessPermission ref (ACCESS-PERMISSION-REF) from the
abstract DiagnosticRoutineSubfunction (Table 4.84); the reader delegates the
inherited field to the Rule 0001.7 helper readDiagnosticRoutineSubfunction.
Per the XSD complexType sequence (l.42436) the inherited
ACCESS-PERMISSION-REF precedes the own REQUESTS and RESPONSES wrappers.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_request_routine_results.py
"""

from unittest.mock import MagicMock

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticRequestRoutineResults:
    """Tests for readDiagnosticRequestRoutineResults — own element field values (Table 4.88)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DiagnosticRequestRoutineResults

        request_results = DiagnosticRequestRoutineResults(parent=MagicMock(), short_name="RequestResults1")
        element = _snip(inner, root_tag="DIAGNOSTIC-REQUEST-ROUTINE-RESULTS")
        parser.readDiagnosticRequestRoutineResults(element, request_results)
        return request_results

    def test_read_short_name(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name)."""
        request_results = self._read(parser, "<SHORT-NAME>RequestResults1</SHORT-NAME>")
        assert request_results.getShortName() == "RequestResults1"

    def test_read_inherited_access_permission_ref(self, parser):
        """Test that the inherited ACCESS-PERMISSION-REF is read via the base helper."""
        request_results = self._read(parser, '<ACCESS-PERMISSION-REF DEST="DIAGNOSTIC-ACCESS-PERMISSION">/AUTOSAR/DiagnosticAccessPermissions/Level1</ACCESS-PERMISSION-REF>')
        ref = request_results.getAccessPermission()
        assert ref is not None
        assert ref.getValue() == "/AUTOSAR/DiagnosticAccessPermissions/Level1"
        assert ref.getDest() == "DIAGNOSTIC-ACCESS-PERMISSION"

    def test_read_requests_wrapper(self, parser):
        """Test that the REQUESTS wrapper DIAGNOSTIC-PARAMETER items are read."""
        request_results = self._read(
            parser,
            "<REQUESTS><DIAGNOSTIC-PARAMETER><IDENT><SHORT-NAME>ReqParam1</SHORT-NAME></IDENT></DIAGNOSTIC-PARAMETER><DIAGNOSTIC-PARAMETER><IDENT><SHORT-NAME>ReqParam2</SHORT-NAME></IDENT></DIAGNOSTIC-PARAMETER></REQUESTS>",
        )
        requests = request_results.getRequest()
        assert len(requests) == 2
        assert requests[0].getIdent() is not None
        assert requests[0].getIdent().getShortName() == "ReqParam1"
        assert requests[1].getIdent() is not None
        assert requests[1].getIdent().getShortName() == "ReqParam2"

    def test_read_responses_wrapper(self, parser):
        """Test that the RESPONSES wrapper DIAGNOSTIC-PARAMETER items are read."""
        request_results = self._read(parser, "<RESPONSES><DIAGNOSTIC-PARAMETER><IDENT><SHORT-NAME>RespParam1</SHORT-NAME></IDENT></DIAGNOSTIC-PARAMETER></RESPONSES>")
        responses = request_results.getResponse()
        assert len(responses) == 1
        assert responses[0].getIdent() is not None
        assert responses[0].getIdent().getShortName() == "RespParam1"

    def test_read_empty_wrappers_omitted(self, parser):
        """Test that absent REQUESTS/RESPONSES wrappers leave both lists empty."""
        request_results = self._read(parser, "<SHORT-NAME>RequestResults1</SHORT-NAME>")
        assert request_results.getRequest() == []
        assert request_results.getResponse() == []
