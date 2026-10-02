"""
Tests for writing DIAGNOSTIC-CUSTOM-SERVICE-INSTANCE elements —
DiagnosticCustomServiceInstance, Table 4.27 (p.70, R23-11).

DiagnosticCustomServiceInstance (Base chain reaches DiagnosticServiceInstance)
carries the inherited ACCESS-PERMISSION-REF (SERVICE-CLASS-REF is atpDerived,
skipped in the XSD group) and its own 0..1 CUSTOM-SERVICE-CLASS-REF — XSD group
DIAGNOSTIC-CUSTOM-SERVICE-INSTANCE, AUTOSAR_00052.xsd l.34019. The writer reads
the model via the get* getters; the dispatch entry is writeARPackageElement →
writeDiagnosticCustomServiceInstance.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_custom_service_instance.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticCustomServiceInstance
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


class TestWriteDiagnosticCustomServiceInstance:
    """Tests for writeDiagnosticCustomServiceInstance — own element field values (Table 4.27)."""

    def test_write_field_values_in_xsd_order(self):
        """Test that ACCESS-PERMISSION-REF (inherited) and CUSTOM-SERVICE-CLASS-REF are emitted with field values in XSD order."""
        package = AUTOSAR.getInstance().createARPackage("CustomInstances")
        instance = package.createDiagnosticCustomServiceInstance("Csi")
        instance.setAccessPermissionRef(_ref("DIAGNOSTIC-ACCESS-PERMISSION", "/AUTOSAR/Dcm/AccessPermission"))
        instance.setCustomServiceClassRef(_ref("DIAGNOSTIC-CUSTOM-SERVICE-CLASS", "/AUTOSAR/DiagnosticCustomInstances/CustomServiceClass"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticCustomServiceInstance(parent, instance)

        child = parent.find("DIAGNOSTIC-CUSTOM-SERVICE-INSTANCE")
        assert child is not None
        access_ref = child.find("ACCESS-PERMISSION-REF")
        assert access_ref.attrib["DEST"] == "DIAGNOSTIC-ACCESS-PERMISSION"
        assert access_ref.text == "/AUTOSAR/Dcm/AccessPermission"
        class_ref = child.find("CUSTOM-SERVICE-CLASS-REF")
        assert class_ref.attrib["DEST"] == "DIAGNOSTIC-CUSTOM-SERVICE-CLASS"
        assert class_ref.text == "/AUTOSAR/DiagnosticCustomInstances/CustomServiceClass"
        tags = [c.tag for c in child if c.tag != "SHORT-NAME"]
        assert tags == ["ACCESS-PERMISSION-REF", "CUSTOM-SERVICE-CLASS-REF"]

    def test_write_unset_fields_omits_tags(self):
        """Test that unset fields emit no elements beyond SHORT-NAME."""
        package = AUTOSAR.getInstance().createARPackage("CustomInstances")
        instance = package.createDiagnosticCustomServiceInstance("Csi")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticCustomServiceInstance(parent, instance)

        child = parent.find("DIAGNOSTIC-CUSTOM-SERVICE-INSTANCE")
        assert child is not None
        assert [c.tag for c in child] == ["SHORT-NAME"]
        assert child.find("ACCESS-PERMISSION-REF") is None
        assert child.find("SERVICE-CLASS-REF") is None
        assert child.find("CUSTOM-SERVICE-CLASS-REF") is None

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticCustomServiceInstance to a DIAGNOSTIC-CUSTOM-SERVICE-INSTANCE element."""
        package = AUTOSAR.getInstance().createARPackage("CustomInstances")
        instance = package.createDiagnosticCustomServiceInstance("Csi")
        instance.setCustomServiceClassRef(_ref("DIAGNOSTIC-CUSTOM-SERVICE-CLASS", "/AUTOSAR/DiagnosticCustomInstances/CustomServiceClass"))

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, instance)

        child = parent.find("DIAGNOSTIC-CUSTOM-SERVICE-INSTANCE")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Csi"
        assert child.find("CUSTOM-SERVICE-CLASS-REF").text == "/AUTOSAR/DiagnosticCustomInstances/CustomServiceClass"

    def test_round_trip(self):
        """Test the full set → save → reload → assert cycle over an ARPackage with field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("CustomInstances")
        instance = package.createDiagnosticCustomServiceInstance("Csi")
        instance.setAccessPermissionRef(_ref("DIAGNOSTIC-ACCESS-PERMISSION", "/AUTOSAR/Dcm/AccessPermission"))
        instance.setCustomServiceClassRef(_ref("DIAGNOSTIC-CUSTOM-SERVICE-CLASS", "/AUTOSAR/DiagnosticCustomInstances/CustomServiceClass"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            instance_2 = package_2.getReferrableElement("Csi", DiagnosticCustomServiceInstance)
            assert instance_2 is not None
            assert instance_2.getAccessPermissionRef() is not None
            assert instance_2.getAccessPermissionRef().getDest() == "DIAGNOSTIC-ACCESS-PERMISSION"
            assert instance_2.getAccessPermissionRef().getValue() == "/AUTOSAR/Dcm/AccessPermission"
            assert instance_2.getCustomServiceClassRef() is not None
            assert instance_2.getCustomServiceClassRef().getDest() == "DIAGNOSTIC-CUSTOM-SERVICE-CLASS"
            assert instance_2.getCustomServiceClassRef().getValue() == "/AUTOSAR/DiagnosticCustomInstances/CustomServiceClass"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_empty(self):
        """Test that a DiagnosticCustomServiceInstance without field values round-trips with all fields empty."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("CustomInstances")
        package.createDiagnosticCustomServiceInstance("Csi")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            instance_2 = package_2.getReferrableElement("Csi", DiagnosticCustomServiceInstance)
            assert instance_2 is not None
            assert instance_2.getAccessPermissionRef() is None
            assert instance_2.getCustomServiceClassRef() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
