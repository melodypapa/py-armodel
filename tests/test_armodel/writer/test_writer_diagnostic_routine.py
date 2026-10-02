"""
Tests for writing the DIAGNOSTIC-ROUTINE element — DiagnosticRoutine, Table 4.85 (p.124, R23-11).

DiagnosticRoutine (Base most-derived ARElement, Aggregated by ARPackage.element)
owns five attributes (AUTOSAR_00052.xsd group DIAGNOSTIC-ROUTINE l.42845, XSD
complexType sequence l.42887: ID, REQUEST-RESULT, ROUTINE-INFO, START, STOP):
the 0..1 id PositiveInteger (ID/POSITIVE-INTEGER-VALUE-VARIATION-POINT), the
0..1 requestResult/start/stop aggregations of the DiagnosticRoutineSubfunction
concretes (written via the Rule 0001.7 concrete writers), and the 0..1
routineInfo PositiveInteger. The dispatch entry is writeARPackageElement →
writeDiagnosticRoutine.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_routine.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticParameter
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticRoutine
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticRoutine:
    """Tests for writeDiagnosticRoutine — own element field values (Table 4.85)."""

    def _write(self, routine: DiagnosticRoutine) -> ET.Element:
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticRoutine(parent, routine)
        return parent.find("DIAGNOSTIC-ROUTINE")

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticRoutine without attributes emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticRoutines")
        package.createDiagnosticRoutine("Routine1")

        child = self._write(package.getElement("Routine1", DiagnosticRoutine))
        assert child is not None
        assert child.find("SHORT-NAME").text == "Routine1"
        assert child.find("ID") is None
        assert child.find("REQUEST-RESULT") is None
        assert child.find("ROUTINE-INFO") is None
        assert child.find("START") is None
        assert child.find("STOP") is None

    def test_write_id_variation_point(self):
        """Test that the ID/POSITIVE-INTEGER-VALUE-VARIATION-POINT is written from id."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticRoutines")
        routine = package.createDiagnosticRoutine("Routine1")
        id_value = PositiveInteger()
        id_value.setValue("5")
        routine.setId(id_value)

        child = self._write(routine)
        id_element = child.find("ID")
        assert id_element is not None
        avp_element = id_element.find("POSITIVE-INTEGER-VALUE-VARIATION-POINT")
        assert avp_element is not None
        assert avp_element.text == "5"

    def test_write_request_result(self):
        """Test that the REQUEST-RESULT aggregation is written from requestResult."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticRoutines")
        routine = package.createDiagnosticRoutine("Routine1")
        request_result = routine.createRequestResult("RequestResults1")
        response_parameter = DiagnosticParameter()
        response_parameter.createIdent("RespParam1")
        request_result.addResponse(response_parameter)

        child = self._write(routine)
        request_result_element = child.find("REQUEST-RESULT")
        assert request_result_element is not None
        assert request_result_element.find("SHORT-NAME").text == "RequestResults1"
        assert request_result_element.find("RESPONSES/DIAGNOSTIC-PARAMETER/IDENT/SHORT-NAME").text == "RespParam1"

    def test_write_routine_info(self):
        """Test that the ROUTINE-INFO is written from routineInfo."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticRoutines")
        routine = package.createDiagnosticRoutine("Routine1")
        routine_info = PositiveInteger()
        routine_info.setValue("7")
        routine.setRoutineInfo(routine_info)

        child = self._write(routine)
        routine_info_element = child.find("ROUTINE-INFO")
        assert routine_info_element is not None
        assert routine_info_element.text == "7"

    def test_write_start_and_stop(self):
        """Test that the START and STOP aggregations are written from start and stop."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticRoutines")
        routine = package.createDiagnosticRoutine("Routine1")
        start = routine.createStart("Start1")
        request_parameter = DiagnosticParameter()
        request_parameter.createIdent("ReqParam1")
        start.addRequest(request_parameter)
        routine.createStop("Stop1")

        child = self._write(routine)
        start_element = child.find("START")
        assert start_element is not None
        assert start_element.find("SHORT-NAME").text == "Start1"
        assert start_element.find("REQUESTS/DIAGNOSTIC-PARAMETER/IDENT/SHORT-NAME").text == "ReqParam1"
        stop_element = child.find("STOP")
        assert stop_element is not None
        assert stop_element.find("SHORT-NAME").text == "Stop1"

    def test_write_element_order_matches_xsd_sequence(self):
        """Test that ID, REQUEST-RESULT, ROUTINE-INFO, START, STOP order matches the XSD sequence (l.42887)."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticRoutines")
        routine = package.createDiagnosticRoutine("Routine1")
        id_value = PositiveInteger()
        id_value.setValue("5")
        routine.setId(id_value)
        routine.createRequestResult("RequestResults1")
        routine_info = PositiveInteger()
        routine_info.setValue("7")
        routine.setRoutineInfo(routine_info)
        routine.createStart("Start1")
        routine.createStop("Stop1")

        child = self._write(routine)
        assert [c.tag for c in child if c.tag != "SHORT-NAME"] == ["ID", "REQUEST-RESULT", "ROUTINE-INFO", "START", "STOP"]

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticRoutine to a DIAGNOSTIC-ROUTINE element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticRoutines")
        package.createDiagnosticRoutine("Routine1")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, package.getElement("Routine1", DiagnosticRoutine))

        child = parent.find("DIAGNOSTIC-ROUTINE")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Routine1"

    def test_round_trip_preserves_field_values(self):
        """Test the full create → save → reload → assert cycle preserving the field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticRoutines")
        routine = package.createDiagnosticRoutine("Routine1")
        id_value = PositiveInteger()
        id_value.setValue("5")
        routine.setId(id_value)
        request_result = routine.createRequestResult("RequestResults1")
        response_parameter = DiagnosticParameter()
        response_parameter.createIdent("RespParam1")
        request_result.addResponse(response_parameter)
        routine_info = PositiveInteger()
        routine_info.setValue("7")
        routine.setRoutineInfo(routine_info)
        start = routine.createStart("Start1")
        request_parameter = DiagnosticParameter()
        request_parameter.createIdent("ReqParam1")
        start.addRequest(request_parameter)
        routine.createStop("Stop1")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            routine_2 = package_2.getElement("Routine1", DiagnosticRoutine)
            assert routine_2 is not None
            assert routine_2.getShortName() == "Routine1"
            assert routine_2.getId() is not None
            assert routine_2.getId().getValue() == 5
            request_result_2 = routine_2.getRequestResult()
            assert request_result_2 is not None
            assert request_result_2.getShortName() == "RequestResults1"
            assert [p.getIdent().getShortName() for p in request_result_2.getResponse()] == ["RespParam1"]
            assert routine_2.getRoutineInfo() is not None
            assert routine_2.getRoutineInfo().getValue() == 7
            start_2 = routine_2.getStart()
            assert start_2 is not None
            assert start_2.getShortName() == "Start1"
            assert [p.getIdent().getShortName() for p in start_2.getRequest()] == ["ReqParam1"]
            stop_2 = routine_2.getStop()
            assert stop_2 is not None
            assert stop_2.getShortName() == "Stop1"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
