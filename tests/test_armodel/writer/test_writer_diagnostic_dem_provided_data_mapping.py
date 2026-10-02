"""
Tests for writing DIAGNOSTIC-DEM-PROVIDED-DATA-MAPPING elements —
DiagnosticDemProvidedDataMapping, Table 5.28 (p.255, R23-11).

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_dem_provided_data_mapping.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticDemProvidedDataMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameToken, RefType
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticDemProvidedDataMapping:
    """Tests for writeDiagnosticDemProvidedDataMapping — own element field values (Table 5.28)."""

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticDemProvidedDataMapping without attributes emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        package.createDiagnosticDemProvidedDataMapping("M1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticDemProvidedDataMapping(parent, package.getReferrableElement("M1", DiagnosticDemProvidedDataMapping))

        child = parent.find("DIAGNOSTIC-DEM-PROVIDED-DATA-MAPPING")
        assert child is not None
        assert child.find("SHORT-NAME").text == "M1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_fields_in_xsd_order(self):
        """Test that all attributes are emitted in XSD order with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        mapping = package.createDiagnosticDemProvidedDataMapping("M1")
        mapping.setDataElementRef(RefType().setValue("/AUTOSAR/DataElement1"))
        mapping.setDataProvider(NameToken().setValue("provider"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticDemProvidedDataMapping(parent, mapping)

        child = parent.find("DIAGNOSTIC-DEM-PROVIDED-DATA-MAPPING")
        assert [c.tag for c in child] == ["SHORT-NAME", "DATA-ELEMENT-REF", "DATA-PROVIDER"]
        assert child.find("DATA-ELEMENT-REF").text == "/AUTOSAR/DataElement1"
        assert child.find("DATA-PROVIDER").text == "provider"
