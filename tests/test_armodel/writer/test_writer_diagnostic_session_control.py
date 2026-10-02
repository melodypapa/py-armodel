"""
Tests for writing DIAGNOSTIC-SESSION-CONTROL elements —
DiagnosticSessionControl, Table 4.47 (p.93, R23-11).

DiagnosticSessionControl (Base most-derived ARElement, DiagnosticServiceInstance
in the chain) carries two 0..1 ref attributes — DIAGNOSTIC-SESSION-REF
(DIAGNOSTIC-SESSION--SUBTYPES-ENUM) and SESSION-CONTROL-CLASS-REF
(DIAGNOSTIC-SESSION-CONTROL-CLASS--SUBTYPES-ENUM) — XSD group
DIAGNOSTIC-SESSION-CONTROL, AUTOSAR_00052.xsd l.44381. The writer reads
the model via the get* getters; the dispatch entry is writeARPackageElement →
writeDiagnosticSessionControl.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_session_control.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticSessionControl
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


class TestWriteDiagnosticSessionControl:
    """Tests for writeDiagnosticSessionControl — own element field values (Table 4.47)."""

    def test_write_refs(self):
        """Test that DIAGNOSTIC-SESSION-REF and SESSION-CONTROL-CLASS-REF are emitted with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("SessionControls")
        session_control = package.createDiagnosticSessionControl("SessionCtrl")
        session_control.setDiagnosticSessionRef(_ref("DIAGNOSTIC-SESSION", "/AUTOSAR/DiagnosticSessions/DefaultSession"))
        session_control.setSessionControlClassRef(_ref("DIAGNOSTIC-SESSION-CONTROL-CLASS", "/AUTOSAR/DiagnosticSessionControls/SessionControlClass"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticSessionControl(parent, session_control)

        child = parent.find("DIAGNOSTIC-SESSION-CONTROL")
        assert child is not None
        assert child.find("SHORT-NAME").text == "SessionCtrl"
        diagnostic_session_ref = child.find("DIAGNOSTIC-SESSION-REF")
        assert diagnostic_session_ref is not None
        assert diagnostic_session_ref.text == "/AUTOSAR/DiagnosticSessions/DefaultSession"
        assert diagnostic_session_ref.get("DEST") == "DIAGNOSTIC-SESSION"
        session_control_class_ref = child.find("SESSION-CONTROL-CLASS-REF")
        assert session_control_class_ref is not None
        assert session_control_class_ref.text == "/AUTOSAR/DiagnosticSessionControls/SessionControlClass"
        assert session_control_class_ref.get("DEST") == "DIAGNOSTIC-SESSION-CONTROL-CLASS"
        tags = [c.tag for c in child if c.tag != "SHORT-NAME"]
        assert tags == ["DIAGNOSTIC-SESSION-REF", "SESSION-CONTROL-CLASS-REF"]

    def test_write_unset_fields_omit_tags(self):
        """Test that unset refs emit no elements beyond SHORT-NAME."""
        package = AUTOSAR.getInstance().createARPackage("SessionControls")
        package.createDiagnosticSessionControl("SessionCtrl")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticSessionControl(parent, package.getReferrableElement("SessionCtrl", DiagnosticSessionControl))

        child = parent.find("DIAGNOSTIC-SESSION-CONTROL")
        assert child is not None
        assert [c.tag for c in child] == ["SHORT-NAME"]
        assert child.find("DIAGNOSTIC-SESSION-REF") is None
        assert child.find("SESSION-CONTROL-CLASS-REF") is None

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticSessionControl to a DIAGNOSTIC-SESSION-CONTROL element."""
        package = AUTOSAR.getInstance().createARPackage("SessionControls")
        session_control = package.createDiagnosticSessionControl("SessionCtrl")
        session_control.setDiagnosticSessionRef(_ref("DIAGNOSTIC-SESSION", "/AUTOSAR/DiagnosticSessions/DefaultSession"))

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, session_control)

        child = parent.find("DIAGNOSTIC-SESSION-CONTROL")
        assert child is not None
        assert child.find("SHORT-NAME").text == "SessionCtrl"
        assert child.find("DIAGNOSTIC-SESSION-REF").text == "/AUTOSAR/DiagnosticSessions/DefaultSession"

    def test_round_trip(self):
        """Test the full set → save → reload → assert cycle over an ARPackage with field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("SessionControls")
        session_control = package.createDiagnosticSessionControl("SessionCtrl")
        session_control.setDiagnosticSessionRef(_ref("DIAGNOSTIC-SESSION", "/AUTOSAR/DiagnosticSessions/DefaultSession"))
        session_control.setSessionControlClassRef(_ref("DIAGNOSTIC-SESSION-CONTROL-CLASS", "/AUTOSAR/DiagnosticSessionControls/SessionControlClass"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            session_control_2 = package_2.getReferrableElement("SessionCtrl", DiagnosticSessionControl)
            assert session_control_2 is not None
            assert session_control_2.getDiagnosticSessionRef() is not None
            assert session_control_2.getDiagnosticSessionRef().getValue() == "/AUTOSAR/DiagnosticSessions/DefaultSession"
            assert session_control_2.getDiagnosticSessionRef().getDest() == "DIAGNOSTIC-SESSION"
            assert session_control_2.getSessionControlClassRef() is not None
            assert session_control_2.getSessionControlClassRef().getValue() == "/AUTOSAR/DiagnosticSessionControls/SessionControlClass"
            assert session_control_2.getSessionControlClassRef().getDest() == "DIAGNOSTIC-SESSION-CONTROL-CLASS"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_empty(self):
        """Test that a DiagnosticSessionControl without field values round-trips with all fields empty."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("SessionControls")
        package.createDiagnosticSessionControl("SessionCtrl")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            session_control_2 = package_2.getReferrableElement("SessionCtrl", DiagnosticSessionControl)
            assert session_control_2 is not None
            assert session_control_2.getDiagnosticSessionRef() is None
            assert session_control_2.getSessionControlClassRef() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
