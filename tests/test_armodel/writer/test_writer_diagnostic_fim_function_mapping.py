"""
Tests for writing DIAGNOSTIC-FIM-FUNCTION-MAPPING elements —
DiagnosticFimFunctionMapping, Table 5.37 (p.265, R23-11).

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_fim_function_mapping.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticFimFunctionMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticFimFunctionMapping:
    """Tests for writeDiagnosticFimFunctionMapping — own element field values (Table 5.37)."""

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticFimFunctionMapping without attributes emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        package.createDiagnosticFimFunctionMapping("M1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticFimFunctionMapping(parent, package.getReferrableElement("M1", DiagnosticFimFunctionMapping))

        child = parent.find("DIAGNOSTIC-FIM-FUNCTION-MAPPING")
        assert child is not None
        assert child.find("SHORT-NAME").text == "M1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_fields_in_xsd_order(self):
        """Test that all attributes are emitted in XSD order with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        mapping = package.createDiagnosticFimFunctionMapping("M1")
        mapping.setMappedBswServiceDependencyRef(RefType().setValue("/AUTOSAR/MappedBswServiceDependency1"))
        mapping.setMappedFlatSwcServiceDependencyRef(RefType().setValue("/AUTOSAR/MappedFlatSwcServiceDependency1"))
        mapping.setMappedFunctionRef(RefType().setValue("/AUTOSAR/MappedFunction1"))
        mapping.setMappedSwcServiceDependencyRef(RefType().setValue("/AUTOSAR/MappedSwcServiceDependency1"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticFimFunctionMapping(parent, mapping)

        child = parent.find("DIAGNOSTIC-FIM-FUNCTION-MAPPING")
        assert [c.tag for c in child] == ["SHORT-NAME", "MAPPED-BSW-SERVICE-DEPENDENCY-REF", "MAPPED-FLAT-SWC-SERVICE-DEPENDENCY-REF", "MAPPED-FUNCTION-REF", "MAPPED-SWC-SERVICE-DEPENDENCY-IREF"]
        assert child.find("MAPPED-BSW-SERVICE-DEPENDENCY-REF").text == "/AUTOSAR/MappedBswServiceDependency1"
        assert child.find("MAPPED-FLAT-SWC-SERVICE-DEPENDENCY-REF").text == "/AUTOSAR/MappedFlatSwcServiceDependency1"
        assert child.find("MAPPED-FUNCTION-REF").text == "/AUTOSAR/MappedFunction1"
        assert child.find("MAPPED-SWC-SERVICE-DEPENDENCY-IREF").text == "/AUTOSAR/MappedSwcServiceDependency1"
