"""
Tests for writing CP-SW-CLUSTER-RESOURCE-TO-DIAG-FUNCTION-ID-MAPPING elements —
CpSwClusterResourceToDiagFunctionIdMapping, Table 5.49 (p.275, R23-11).

Round-trip counterpart: tests/test_armodel/parser/test_cp_sw_cluster_resource_to_diag_function_id_mapping.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import CpSwClusterResourceToDiagFunctionIdMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteCpSwClusterResourceToDiagFunctionIdMapping:
    """Tests for writeCpSwClusterResourceToDiagFunctionIdMapping — own element field values (Table 5.49)."""

    def test_write_empty_wrapper(self):
        """Test that a CpSwClusterResourceToDiagFunctionIdMapping without attributes emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        package.createCpSwClusterResourceToDiagFunctionIdMapping("M1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeCpSwClusterResourceToDiagFunctionIdMapping(parent, package.getElement("M1", CpSwClusterResourceToDiagFunctionIdMapping))

        child = parent.find("CP-SW-CLUSTER-RESOURCE-TO-DIAG-FUNCTION-ID-MAPPING")
        assert child is not None
        assert child.find("SHORT-NAME").text == "M1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_fields_in_xsd_order(self):
        """Test that all attributes are emitted in XSD order with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        mapping = package.createCpSwClusterResourceToDiagFunctionIdMapping("M1")
        mapping.setCpSoftwareClusterResourceRef(RefType().setValue("/AUTOSAR/CpSoftwareClusterResource1"))
        mapping.setFunctionIdentifierRef(RefType().setValue("/AUTOSAR/FunctionIdentifier1"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeCpSwClusterResourceToDiagFunctionIdMapping(parent, mapping)

        child = parent.find("CP-SW-CLUSTER-RESOURCE-TO-DIAG-FUNCTION-ID-MAPPING")
        assert [c.tag for c in child] == ["SHORT-NAME", "CP-SOFTWARE-CLUSTER-RESOURCE-REF", "FUNCTION-IDENTIFIER-REF"]
        assert child.find("CP-SOFTWARE-CLUSTER-RESOURCE-REF").text == "/AUTOSAR/CpSoftwareClusterResource1"
        assert child.find("FUNCTION-IDENTIFIER-REF").text == "/AUTOSAR/FunctionIdentifier1"
