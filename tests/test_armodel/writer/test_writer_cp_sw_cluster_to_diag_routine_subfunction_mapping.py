"""
Tests for writing CP-SW-CLUSTER-TO-DIAG-ROUTINE-SUBFUNCTION-MAPPING elements —
CpSwClusterToDiagRoutineSubfunctionMapping, Table 5.48 (p.274, R23-11).

Round-trip counterpart: tests/test_armodel/parser/test_cp_sw_cluster_to_diag_routine_subfunction_mapping.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import CpSwClusterToDiagRoutineSubfunctionMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteCpSwClusterToDiagRoutineSubfunctionMapping:
    """Tests for writeCpSwClusterToDiagRoutineSubfunctionMapping — own element field values (Table 5.48)."""

    def test_write_empty_wrapper(self):
        """Test that a CpSwClusterToDiagRoutineSubfunctionMapping without attributes emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        package.createCpSwClusterToDiagRoutineSubfunctionMapping("M1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeCpSwClusterToDiagRoutineSubfunctionMapping(parent, package.getReferrableElement("M1", CpSwClusterToDiagRoutineSubfunctionMapping))

        child = parent.find("CP-SW-CLUSTER-TO-DIAG-ROUTINE-SUBFUNCTION-MAPPING")
        assert child is not None
        assert child.find("SHORT-NAME").text == "M1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_fields_in_xsd_order(self):
        """Test that all attributes are emitted in XSD order with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        mapping = package.createCpSwClusterToDiagRoutineSubfunctionMapping("M1")
        mapping.setCpSoftwareClusterResourceRef(RefType().setValue("/AUTOSAR/CpSoftwareClusterResource1"))
        mapping.setRoutineSubfunctionRef(RefType().setValue("/AUTOSAR/RoutineSubfunction1"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeCpSwClusterToDiagRoutineSubfunctionMapping(parent, mapping)

        child = parent.find("CP-SW-CLUSTER-TO-DIAG-ROUTINE-SUBFUNCTION-MAPPING")
        assert [c.tag for c in child] == ["SHORT-NAME", "CP-SOFTWARE-CLUSTER-RESOURCE-REF", "ROUTINE-SUBFUNCTION-REF"]
        assert child.find("CP-SOFTWARE-CLUSTER-RESOURCE-REF").text == "/AUTOSAR/CpSoftwareClusterResource1"
        assert child.find("ROUTINE-SUBFUNCTION-REF").text == "/AUTOSAR/RoutineSubfunction1"
