"""
Tests for writing CP-SW-CLUSTER-RESOURCE-TO-DIAG-DATA-ELEM-MAPPING elements —
CpSwClusterResourceToDiagDataElemMapping, Table 5.47 (p.273, R23-11).

Round-trip counterpart: tests/test_armodel/parser/test_cp_sw_cluster_resource_to_diag_data_elem_mapping.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import CpSwClusterResourceToDiagDataElemMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteCpSwClusterResourceToDiagDataElemMapping:
    """Tests for writeCpSwClusterResourceToDiagDataElemMapping — own element field values (Table 5.47)."""

    def test_write_empty_wrapper(self):
        """Test that a CpSwClusterResourceToDiagDataElemMapping without attributes emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        package.createCpSwClusterResourceToDiagDataElemMapping("M1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeCpSwClusterResourceToDiagDataElemMapping(parent, package.getElement("M1", CpSwClusterResourceToDiagDataElemMapping))

        child = parent.find("CP-SW-CLUSTER-RESOURCE-TO-DIAG-DATA-ELEM-MAPPING")
        assert child is not None
        assert child.find("SHORT-NAME").text == "M1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_fields_in_xsd_order(self):
        """Test that all attributes are emitted in XSD order with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        mapping = package.createCpSwClusterResourceToDiagDataElemMapping("M1")
        mapping.setCpSoftwareClusterResourceRef(RefType().setValue("/AUTOSAR/CpSoftwareClusterResource1"))
        mapping.setDiagnosticDataElementRef(RefType().setValue("/AUTOSAR/DiagnosticDataElement1"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeCpSwClusterResourceToDiagDataElemMapping(parent, mapping)

        child = parent.find("CP-SW-CLUSTER-RESOURCE-TO-DIAG-DATA-ELEM-MAPPING")
        assert [c.tag for c in child] == ["SHORT-NAME", "CP-SOFTWARE-CLUSTER-RESOURCE-REF", "DIAGNOSTIC-DATA-ELEMENT-REF"]
        assert child.find("CP-SOFTWARE-CLUSTER-RESOURCE-REF").text == "/AUTOSAR/CpSoftwareClusterResource1"
        assert child.find("DIAGNOSTIC-DATA-ELEMENT-REF").text == "/AUTOSAR/DiagnosticDataElement1"
