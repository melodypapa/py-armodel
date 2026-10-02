"""
Tests for reading the DIAGNOSTIC-ROUTINE element — DiagnosticRoutine, Table 4.85 (p.124, R23-11).

DiagnosticRoutine (Base most-derived ARElement, Aggregated by ARPackage.element)
owns five attributes (AUTOSAR_00052.xsd group DIAGNOSTIC-ROUTINE l.42845, XSD
complexType sequence l.42887: ID, REQUEST-RESULT, ROUTINE-INFO, START, STOP):
the 0..1 id PositiveInteger (ID/POSITIVE-INTEGER-VALUE-VARIATION-POINT), the
0..1 requestResult/start/stop aggregations of the DiagnosticRoutineSubfunction
concretes (read via the Rule 0001.7 concrete readers), and the 0..1 routineInfo
PositiveInteger.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_routine.py
"""

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticRoutine:
    """Tests for readDiagnosticRoutine — own element field values (Table 4.85)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticRoutine

        routine = DiagnosticRoutine(parent=None, short_name="Routine1")
        element = _snip(inner, root_tag="DIAGNOSTIC-ROUTINE")
        parser.readDiagnosticRoutine(element, routine)
        return routine

    def test_read_short_name(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name)."""
        routine = self._read(parser, "<SHORT-NAME>Routine1</SHORT-NAME>")
        assert routine.getShortName() == "Routine1"

    def test_read_id_variation_point(self, parser):
        """Test that the ID/POSITIVE-INTEGER-VALUE-VARIATION-POINT is read into id."""
        routine = self._read(parser, "<ID><POSITIVE-INTEGER-VALUE-VARIATION-POINT>5</POSITIVE-INTEGER-VALUE-VARIATION-POINT></ID>")
        assert routine.getId() is not None
        assert routine.getId().getValue() == 5

    def test_read_request_result(self, parser):
        """Test that the REQUEST-RESULT aggregation is read into requestResult."""
        routine = self._read(
            parser,
            "<REQUEST-RESULT><SHORT-NAME>RequestResults1</SHORT-NAME><RESPONSES><DIAGNOSTIC-PARAMETER><IDENT><SHORT-NAME>RespParam1</SHORT-NAME></IDENT></DIAGNOSTIC-PARAMETER></RESPONSES></REQUEST-RESULT>",
        )
        request_result = routine.getRequestResult()
        assert request_result is not None
        assert request_result.getShortName() == "RequestResults1"
        assert [p.getIdent().getShortName() for p in request_result.getResponse()] == ["RespParam1"]

    def test_read_routine_info(self, parser):
        """Test that the ROUTINE-INFO is read into routineInfo."""
        routine = self._read(parser, "<ROUTINE-INFO>7</ROUTINE-INFO>")
        assert routine.getRoutineInfo() is not None
        assert routine.getRoutineInfo().getValue() == 7

    def test_read_start(self, parser):
        """Test that the START aggregation is read into start."""
        routine = self._read(
            parser, "<START><SHORT-NAME>Start1</SHORT-NAME><REQUESTS><DIAGNOSTIC-PARAMETER><IDENT><SHORT-NAME>ReqParam1</SHORT-NAME></IDENT></DIAGNOSTIC-PARAMETER></REQUESTS></START>"
        )
        start = routine.getStart()
        assert start is not None
        assert start.getShortName() == "Start1"
        assert [p.getIdent().getShortName() for p in start.getRequest()] == ["ReqParam1"]

    def test_read_stop(self, parser):
        """Test that the STOP aggregation is read into stop."""
        routine = self._read(
            parser, '<STOP><SHORT-NAME>Stop1</SHORT-NAME><ACCESS-PERMISSION-REF DEST="DIAGNOSTIC-ACCESS-PERMISSION">/AUTOSAR/DiagnosticAccessPermissions/Level1</ACCESS-PERMISSION-REF></STOP>'
        )
        stop = routine.getStop()
        assert stop is not None
        assert stop.getShortName() == "Stop1"
        assert stop.getAccessPermission() is not None
        assert stop.getAccessPermission().getValue() == "/AUTOSAR/DiagnosticAccessPermissions/Level1"

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving all fields unset."""
        routine = self._read(parser, "<SHORT-NAME>Routine1</SHORT-NAME>")
        assert routine.getId() is None
        assert routine.getRequestResult() is None
        assert routine.getRoutineInfo() is None
        assert routine.getStart() is None
        assert routine.getStop() is None
