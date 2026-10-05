"""
Tests for writing DIAGNOSTIC-TROUBLE-CODE elements —
DiagnosticTroubleCode, Table 4.161 (p.176, R23-11).

DiagnosticTroubleCode is abstract and carries no Attribute rows — its XSD group
DIAGNOSTIC-TROUBLE-CODE (AUTOSAR_00052.xsd l.46194) is an empty sequence, so the
writer is writeDiagnosticTroubleCode = DIAGNOSTIC-TROUBLE-CODE subelement +
writeIdentifiable. The dispatch entry is writeARPackageElementRest →
writeDiagnosticTroubleCode (the concrete writeDiagnosticTroubleCodeJ1939 branch
precedes the abstract-base branch so J-1939 elements keep their own tag).
The dispatch entry is also writeDiagnosticElement → writeDiagnosticTroubleCode
after the J-1939 branch.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_trouble_code.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticTroubleCode
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset the AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticTroubleCode:
    """Tests for writeDiagnosticTroubleCode — own element field values (Table 4.161)."""

    def test_write_short_name(self):
        """Test that a DiagnosticTroubleCode is emitted as a DIAGNOSTIC-TROUBLE-CODE element with its short name."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticTroubleCodes")
        package.createDiagnosticTroubleCode("TroubleCode1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticTroubleCode(parent, package.getReferrableElement("TroubleCode1", DiagnosticTroubleCode))

        child = parent.find("DIAGNOSTIC-TROUBLE-CODE")
        assert child is not None
        assert child.find("SHORT-NAME").text == "TroubleCode1"

    def test_write_unset_fields_emit_identifiable_only(self):
        """Test that a DiagnosticTroubleCode without optional children emits no extra elements (empty wrapper case)."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticTroubleCodes")
        package.createDiagnosticTroubleCode("TroubleCode1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticTroubleCode(parent, package.getReferrableElement("TroubleCode1", DiagnosticTroubleCode))

        child = parent.find("DIAGNOSTIC-TROUBLE-CODE")
        assert child is not None
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticTroubleCode to a DIAGNOSTIC-TROUBLE-CODE element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticTroubleCodes")
        trouble_code = package.createDiagnosticTroubleCode("TroubleCode1")
        trouble_code.setCategory("TROUBLE_CODE")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, trouble_code)

        child = parent.find("DIAGNOSTIC-TROUBLE-CODE")
        assert child is not None
        assert child.find("SHORT-NAME").text == "TroubleCode1"
        assert child.find("CATEGORY").text == "TROUBLE_CODE"

    def test_j1939_dispatch_not_shadowed_by_base(self):
        """Test that a DiagnosticTroubleCodeJ1939 still dispatches to its own DIAGNOSTIC-TROUBLE-CODE-J-1939 element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticTroubleCodes")
        trouble_code = package.createDiagnosticTroubleCodeJ1939("Dtc1")
        fmi = PositiveInteger()
        fmi.setValue("13")
        trouble_code.setFmi(fmi)

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, trouble_code)

        assert parent.find("DIAGNOSTIC-TROUBLE-CODE-J-1939") is not None
        child = parent.find("DIAGNOSTIC-TROUBLE-CODE-J-1939")
        assert child.find("SHORT-NAME").text == "Dtc1"
        assert child.find("FMI").text == "13"

    def test_round_trip_preserves_short_name(self):
        """Test the full create → save → reload → assert cycle over an ARPackage with a DiagnosticTroubleCode."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticTroubleCodes")
        trouble_code = package.createDiagnosticTroubleCode("TroubleCode1")
        trouble_code.setCategory("TROUBLE_CODE")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter(options={"validate": False}).save(
                file_path, document
            )  # known writer defect: writer writes DIAGNOSTIC-TROUBLE-CODE as an AR-PACKAGE element where R23-11 does not allow it (docs/plan/xsd-validation-known-writer-defects.md)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser(options={"validate": False}).load(
                file_path, document_2
            )  # known writer defect: writer writes DIAGNOSTIC-TROUBLE-CODE as an AR-PACKAGE element where R23-11 does not allow it (docs/plan/xsd-validation-known-writer-defects.md)
            package_2 = document_2.getARPackages()[0]
            trouble_code_2 = package_2.getReferrableElement("TroubleCode1", DiagnosticTroubleCode)
            assert trouble_code_2 is not None
            assert isinstance(trouble_code_2, DiagnosticTroubleCode)
            assert trouble_code_2.getShortName() == "TroubleCode1"
            assert trouble_code_2.getCategory() is not None
            assert trouble_code_2.getCategory().getValue() == "TROUBLE_CODE"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_empty(self):
        """Test that a DiagnosticTroubleCode without optional children round-trips with category None."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticTroubleCodes")
        package.createDiagnosticTroubleCode("TroubleCode1")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter(options={"validate": False}).save(
                file_path, document
            )  # known writer defect: writer writes DIAGNOSTIC-TROUBLE-CODE as an AR-PACKAGE element where R23-11 does not allow it (docs/plan/xsd-validation-known-writer-defects.md)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser(options={"validate": False}).load(
                file_path, document_2
            )  # known writer defect: writer writes DIAGNOSTIC-TROUBLE-CODE as an AR-PACKAGE element where R23-11 does not allow it (docs/plan/xsd-validation-known-writer-defects.md)
            package_2 = document_2.getARPackages()[0]
            trouble_code_2 = package_2.getReferrableElement("TroubleCode1", DiagnosticTroubleCode)
            assert trouble_code_2 is not None
            assert trouble_code_2.getShortName() == "TroubleCode1"
            assert trouble_code_2.getCategory() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
