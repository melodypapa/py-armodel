"""
Tests for writing DIAGNOSTIC-READ-DATA-BY-PERIODIC-ID elements —
DiagnosticReadDataByPeriodicID, Table 4.97 (p.130, R23-11).

DiagnosticReadDataByPeriodicID (concrete ARElement, Aggregated by
ARPackage.element) defines one 0..1 attribute: readDataClass
(READ-DATA-CLASS-REF) — AUTOSAR_00052.xsd group
DIAGNOSTIC-READ-DATA-BY-PERIODIC-ID l.41230 / complexType l.41268.
The writer emits the children in XSD sequence order. The dispatch entry is
writeARPackageElement → writeDiagnosticReadDataByPeriodicID.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_read_data_by_periodic_id.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticReadDataByPeriodicID
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


class TestWriteDiagnosticReadDataByPeriodicID:
    """Tests for writeDiagnosticReadDataByPeriodicID — own element field values (Table 4.97)."""

    def _write(self, obj: DiagnosticReadDataByPeriodicID) -> ET.Element:
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticReadDataByPeriodicID(parent, obj)
        return parent.find("DIAGNOSTIC-READ-DATA-BY-PERIODIC-ID")

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticReadDataByPeriodicID without attributes emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticReadDataByPeriodicIds")
        package.createDiagnosticReadDataByPeriodicID("Rdbpid1")

        child = self._write(package.getElement("Rdbpid1", DiagnosticReadDataByPeriodicID))
        assert child is not None
        assert child.find("SHORT-NAME").text == "Rdbpid1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_read_data_class_ref(self):
        """Test that the READ-DATA-CLASS-REF is emitted with its DEST attribute."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticReadDataByPeriodicIds")
        obj = package.createDiagnosticReadDataByPeriodicID("Rdbpid1")
        obj.setReadDataClass(_ref("DIAGNOSTIC-READ-DATA-BY-PERIODIC-ID-CLASS", "/AUTOSAR/DiagnosticReadDataByPeriodicIds/Class1"))

        child = self._write(obj)
        assert child is not None
        ref = child.find("READ-DATA-CLASS-REF")
        assert ref is not None
        assert ref.text == "/AUTOSAR/DiagnosticReadDataByPeriodicIds/Class1"
        assert ref.get("DEST") == "DIAGNOSTIC-READ-DATA-BY-PERIODIC-ID-CLASS"

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticReadDataByPeriodicID to a DIAGNOSTIC-READ-DATA-BY-PERIODIC-ID element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticReadDataByPeriodicIds")
        package.createDiagnosticReadDataByPeriodicID("Rdbpid1")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, package.getElement("Rdbpid1", DiagnosticReadDataByPeriodicID))

        child = parent.find("DIAGNOSTIC-READ-DATA-BY-PERIODIC-ID")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Rdbpid1"

    def test_round_trip_preserves_field_values(self):
        """Test the full create → save → reload → assert cycle preserving the field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticReadDataByPeriodicIds")
        obj = package.createDiagnosticReadDataByPeriodicID("Rdbpid1")
        obj.setReadDataClass(_ref("DIAGNOSTIC-READ-DATA-BY-PERIODIC-ID-CLASS", "/AUTOSAR/DiagnosticReadDataByPeriodicIds/Class1"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            obj_2 = package_2.getElement("Rdbpid1", DiagnosticReadDataByPeriodicID)
            assert obj_2 is not None
            assert obj_2.getShortName() == "Rdbpid1"
            read_data_class = obj_2.getReadDataClass()
            assert read_data_class is not None
            assert read_data_class.getValue() == "/AUTOSAR/DiagnosticReadDataByPeriodicIds/Class1"
            assert read_data_class.getDest() == "DIAGNOSTIC-READ-DATA-BY-PERIODIC-ID-CLASS"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
