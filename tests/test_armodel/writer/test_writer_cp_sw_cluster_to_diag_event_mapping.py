"""
Tests for writing CP-SW-CLUSTER-TO-DIAG-EVENT-MAPPING elements —
CpSwClusterToDiagEventMapping, Table 5.46 (p.272, R23-11).

Round-trip counterpart: tests/test_armodel/parser/test_cp_sw_cluster_to_diag_event_mapping.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import CpSwClusterToDiagEventMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteCpSwClusterToDiagEventMapping:
    """Tests for writeCpSwClusterToDiagEventMapping — own element field values (Table 5.46)."""

    def test_write_empty_wrapper(self):
        """Test that a CpSwClusterToDiagEventMapping without attributes emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        package.createCpSwClusterToDiagEventMapping("M1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeCpSwClusterToDiagEventMapping(parent, package.getReferrableElement("M1", CpSwClusterToDiagEventMapping))

        child = parent.find("CP-SW-CLUSTER-TO-DIAG-EVENT-MAPPING")
        assert child is not None
        assert child.find("SHORT-NAME").text == "M1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_fields_in_xsd_order(self):
        """Test that all attributes are emitted in XSD order with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        mapping = package.createCpSwClusterToDiagEventMapping("M1")
        mapping.setCpSoftwareClusterResourceRef(RefType().setValue("/AUTOSAR/CpSoftwareClusterResource1"))
        mapping.setDiagnosticEventRef(RefType().setValue("/AUTOSAR/DiagnosticEvent1"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeCpSwClusterToDiagEventMapping(parent, mapping)

        child = parent.find("CP-SW-CLUSTER-TO-DIAG-EVENT-MAPPING")
        assert [c.tag for c in child] == ["SHORT-NAME", "CP-SOFTWARE-CLUSTER-RESOURCE-REF", "DIAGNOSTIC-EVENT-REF"]
        assert child.find("CP-SOFTWARE-CLUSTER-RESOURCE-REF").text == "/AUTOSAR/CpSoftwareClusterResource1"
        assert child.find("DIAGNOSTIC-EVENT-REF").text == "/AUTOSAR/DiagnosticEvent1"
