"""
Tests for writing DIAGNOSTIC-MASTER-TO-SLAVE-EVENT-MAPPING elements —
DiagnosticMasterToSlaveEventMapping, Table 5.29 (p.256, R23-11).

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_master_to_slave_event_mapping.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticMasterToSlaveEventMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticMasterToSlaveEventMapping:
    """Tests for writeDiagnosticMasterToSlaveEventMapping — own element field values (Table 5.29)."""

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticMasterToSlaveEventMapping without attributes emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        package.createDiagnosticMasterToSlaveEventMapping("M1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticMasterToSlaveEventMapping(parent, package.getReferrableElement("M1", DiagnosticMasterToSlaveEventMapping))

        child = parent.find("DIAGNOSTIC-MASTER-TO-SLAVE-EVENT-MAPPING")
        assert child is not None
        assert child.find("SHORT-NAME").text == "M1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_fields_in_xsd_order(self):
        """Test that all attributes are emitted in XSD order with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        mapping = package.createDiagnosticMasterToSlaveEventMapping("M1")
        mapping.setMasterEventRef(RefType().setValue("/AUTOSAR/MasterEvent1"))
        mapping.setSlaveEventRef(RefType().setValue("/AUTOSAR/SlaveEvent1"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticMasterToSlaveEventMapping(parent, mapping)

        child = parent.find("DIAGNOSTIC-MASTER-TO-SLAVE-EVENT-MAPPING")
        assert [c.tag for c in child] == ["SHORT-NAME", "MASTER-EVENT-REF", "SLAVE-EVENT-REF"]
        assert child.find("MASTER-EVENT-REF").text == "/AUTOSAR/MasterEvent1"
        assert child.find("SLAVE-EVENT-REF").text == "/AUTOSAR/SlaveEvent1"
