"""
Tests for writing DIAGNOSTIC-SERVICE-SW-MAPPING elements —
DiagnosticServiceSwMapping, Table 5.15 (p.239, R23-11).

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_service_sw_mapping.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticParameterElementAccess, DiagnosticServiceSwMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticServiceSwMapping:
    """Tests for writeDiagnosticServiceSwMapping — own element field values (Table 5.15)."""

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticServiceSwMapping without attributes emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticServiceMappings")
        package.createDiagnosticServiceSwMapping("M1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticServiceSwMapping(parent, package.getElement("M1", DiagnosticServiceSwMapping))

        child = parent.find("DIAGNOSTIC-SERVICE-SW-MAPPING")
        assert child is not None
        assert child.find("SHORT-NAME").text == "M1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_fields_in_xsd_order(self):
        """Test that all attributes are emitted in XSD order with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticServiceMappings")
        mapping = package.createDiagnosticServiceSwMapping("M1")
        mapping.setAccessedDataPrototypeIRef(RefType().setValue("/AUTOSAR/Interfaces/Op1"))
        mapping.setDiagnosticDataElementRef(RefType().setValue("/AUTOSAR/DataElements/Did1"))
        mapping.setDiagnosticParameterRef(RefType().setValue("/AUTOSAR/ParamIdents/Ident1"))
        mapping.setMappedBswServiceDependencyRef(RefType().setValue("/AUTOSAR/BswDeps/Dep1"))
        mapping.setMappedFlatSwcServiceDependencyRef(RefType().setValue("/AUTOSAR/SwcDeps/Dep2"))
        mapping.setMappedSwcServiceDependencyInSystemIRef(RefType().setValue("/AUTOSAR/System/SwcDep3"))
        pea = DiagnosticParameterElementAccess()
        pea.setTargetElementRef(RefType().setValue("/AUTOSAR/ParamElements/Target"))
        mapping.setParameterElementAccess(pea)
        mapping.setServiceInstanceRef(RefType().setValue("/AUTOSAR/Services/Svc1"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticServiceSwMapping(parent, mapping)

        child = parent.find("DIAGNOSTIC-SERVICE-SW-MAPPING")
        assert [c.tag for c in child] == [
            "SHORT-NAME",
            "ACCESSED-DATA-PROTOTYPE-IREF",
            "DIAGNOSTIC-DATA-ELEMENT-REF",
            "DIAGNOSTIC-PARAMETER-REF",
            "MAPPED-BSW-SERVICE-DEPENDENCY-REF",
            "MAPPED-FLAT-SWC-SERVICE-DEPENDENCY-REF",
            "MAPPED-SWC-SERVICE-DEPENDENCY-IN-SYSTEM-IREF",
            "PARAMETER-ELEMENT-ACCESS",
            "SERVICE-INSTANCE-REF",
        ]
        assert child.find("PARAMETER-ELEMENT-ACCESS/TARGET-ELEMENT-REF").text == "/AUTOSAR/ParamElements/Target"
        assert child.find("SERVICE-INSTANCE-REF").text == "/AUTOSAR/Services/Svc1"
