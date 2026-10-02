"""
Tests for writing the DIAGNOSTIC-REQUEST-ROUTINE-RESULTS element — DiagnosticRequestRoutineResults, Table 4.88 (p.125, R23-11).

DiagnosticRequestRoutineResults (Base most-derived DiagnosticRoutineSubfunction)
owns two attributes: the `*` request/response aggregations of
DiagnosticParameter (REQUESTS/RESPONSES wrappers of DIAGNOSTIC-PARAMETER,
AUTOSAR_00052.xsd group DIAGNOSTIC-REQUEST-ROUTINE-RESULTS l.42402). It
inherits the 0..1 accessPermission ref (ACCESS-PERMISSION-REF) from the
abstract DiagnosticRoutineSubfunction (Table 4.84); the writer delegates the
inherited field to the Rule 0001.7 helper writeDiagnosticRoutineSubfunction.
Per the XSD complexType sequence (l.42436) the inherited
ACCESS-PERMISSION-REF precedes the own REQUESTS and RESPONSES wrappers.
DiagnosticRequestRoutineResults is aggregated by
DiagnosticRoutine.requestResult — it is not an ARPackage element and has no
writeARPackageElement dispatch branch.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_request_routine_results.py
"""

import xml.etree.ElementTree as ET
from unittest.mock import MagicMock

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticParameter
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DiagnosticRequestRoutineResults
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _ref(dest: str, value: str) -> RefType:
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


class TestWriteDiagnosticRequestRoutineResults:
    """Tests for writeDiagnosticRequestRoutineResults — own element field values (Table 4.88)."""

    def _write(self, request_results: DiagnosticRequestRoutineResults) -> ET.Element:
        parent = ET.Element("DIAGNOSTIC-REQUEST-ROUTINE-RESULTS", {"xmlns": "http://autosar.org/schema/r4.0"})
        ARXMLWriter().writeDiagnosticRequestRoutineResults(parent, request_results)
        return parent

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticRequestRoutineResults without attributes emits only the IDENTIFIABLE wrapper content."""
        child = self._write(DiagnosticRequestRoutineResults(parent=MagicMock(), short_name="RequestResults1"))
        assert child.find("SHORT-NAME").text == "RequestResults1"
        assert child.find("REQUESTS") is None
        assert child.find("RESPONSES") is None

    def test_write_inherited_access_permission_ref(self):
        """Test that the inherited ACCESS-PERMISSION-REF is written via the base helper."""
        obj = DiagnosticRequestRoutineResults(parent=MagicMock(), short_name="RequestResults1")
        obj.setAccessPermission(_ref("DIAGNOSTIC-ACCESS-PERMISSION", "/AUTOSAR/DiagnosticAccessPermissions/Level1"))
        child = self._write(obj)
        ref = child.find("ACCESS-PERMISSION-REF")
        assert ref is not None
        assert ref.text == "/AUTOSAR/DiagnosticAccessPermissions/Level1"
        assert ref.get("DEST") == "DIAGNOSTIC-ACCESS-PERMISSION"

    def test_write_requests_wrapper(self):
        """Test that the REQUESTS wrapper DIAGNOSTIC-PARAMETER items are written."""
        obj = DiagnosticRequestRoutineResults(parent=MagicMock(), short_name="RequestResults1")
        request_parameter = DiagnosticParameter()
        request_parameter.createIdent("ReqParam1")
        obj.addRequest(request_parameter)
        child = self._write(obj)
        requests = child.find("REQUESTS")
        assert requests is not None
        parameters = requests.findall("DIAGNOSTIC-PARAMETER")
        assert len(parameters) == 1
        assert parameters[0].find("IDENT/SHORT-NAME").text == "ReqParam1"

    def test_write_responses_wrapper(self):
        """Test that the RESPONSES wrapper DIAGNOSTIC-PARAMETER items are written."""
        obj = DiagnosticRequestRoutineResults(parent=MagicMock(), short_name="RequestResults1")
        response_parameter = DiagnosticParameter()
        response_parameter.createIdent("RespParam1")
        obj.addResponse(response_parameter)
        child = self._write(obj)
        responses = child.find("RESPONSES")
        assert responses is not None
        parameters = responses.findall("DIAGNOSTIC-PARAMETER")
        assert len(parameters) == 1
        assert parameters[0].find("IDENT/SHORT-NAME").text == "RespParam1"

    def test_write_element_order_matches_xsd_sequence(self):
        """Test that the inherited ACCESS-PERMISSION-REF precedes the own REQUESTS and RESPONSES (XSD l.42436)."""
        obj = DiagnosticRequestRoutineResults(parent=MagicMock(), short_name="RequestResults1")
        obj.setAccessPermission(_ref("DIAGNOSTIC-ACCESS-PERMISSION", "/AUTOSAR/DiagnosticAccessPermissions/Level1"))
        request_parameter = DiagnosticParameter()
        request_parameter.createIdent("ReqParam1")
        obj.addRequest(request_parameter)
        response_parameter = DiagnosticParameter()
        response_parameter.createIdent("RespParam1")
        obj.addResponse(response_parameter)
        child = self._write(obj)
        assert [c.tag for c in child if c.tag != "SHORT-NAME"] == ["ACCESS-PERMISSION-REF", "REQUESTS", "RESPONSES"]

    def test_round_trip_preserves_field_values(self):
        """Test the write → serialize → re-parse → read-back cycle preserving the field values."""
        obj = DiagnosticRequestRoutineResults(parent=MagicMock(), short_name="RequestResults1")
        obj.setAccessPermission(_ref("DIAGNOSTIC-ACCESS-PERMISSION", "/AUTOSAR/DiagnosticAccessPermissions/Level1"))
        request_parameter = DiagnosticParameter()
        request_parameter.createIdent("ReqParam1")
        obj.addRequest(request_parameter)
        response_parameter = DiagnosticParameter()
        response_parameter.createIdent("RespParam1")
        obj.addResponse(response_parameter)

        parent = ET.Element("DIAGNOSTIC-REQUEST-ROUTINE-RESULTS", {"xmlns": "http://autosar.org/schema/r4.0"})
        ARXMLWriter().writeDiagnosticRequestRoutineResults(parent, obj)
        xml_text = ET.tostring(parent, encoding="unicode")

        reloaded = DiagnosticRequestRoutineResults(parent=MagicMock(), short_name="RequestResults1")
        ARXMLParser().readDiagnosticRequestRoutineResults(ET.fromstring(xml_text), reloaded)
        assert reloaded.getShortName() == "RequestResults1"
        assert reloaded.getAccessPermission() is not None
        assert reloaded.getAccessPermission().getValue() == "/AUTOSAR/DiagnosticAccessPermissions/Level1"
        assert reloaded.getAccessPermission().getDest() == "DIAGNOSTIC-ACCESS-PERMISSION"
        assert [p.getIdent().getShortName() for p in reloaded.getRequest()] == ["ReqParam1"]
        assert [p.getIdent().getShortName() for p in reloaded.getResponse()] == ["RespParam1"]
