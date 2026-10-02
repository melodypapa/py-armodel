"""
Tests for writing DIAGNOSTIC-SERVICE-DATA-MAPPING elements —
DiagnosticServiceDataMapping, Table 5.4 (p.228, R23-11).

DiagnosticServiceDataMapping (Base most-derived DiagnosticSwMapping) owns the
0..1 diagnosticDataElement reference, diagnosticParameter reference,
mappedDataElement instance reference and the 0..1 parameterElementAccess
aggregation, AUTOSAR_00052.xsd group DIAGNOSTIC-SERVICE-DATA-MAPPING l.43661.
DiagnosticParameterElementAccess, Table 5.5 (p.229), own group
DIAGNOSTIC-PARAMETER-ELEMENT-ACCESS l.40680.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_service_data_mapping.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticParameterElementAccess, DiagnosticServiceDataMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticServiceDataMapping:
    """Tests for writeDiagnosticServiceDataMapping — own element field values (Table 5.4)."""

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticServiceDataMapping without attributes emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticServiceMappings")
        package.createDiagnosticServiceDataMapping("Mapping1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticServiceDataMapping(parent, package.getReferrableElement("Mapping1", DiagnosticServiceDataMapping))

        child = parent.find("DIAGNOSTIC-SERVICE-DATA-MAPPING")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Mapping1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_all_fields_in_xsd_order(self):
        """Test that base and own attributes are emitted in XSD order with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticServiceMappings")
        mapping = package.createDiagnosticServiceDataMapping("Mapping1")
        mapping.setProviderSoftwareClusterRef(RefType().setValue("/AUTOSAR/Clusters/C1").setDest("CP-SOFTWARE-CLUSTER"))
        mapping.setDiagnosticDataElementRef(RefType().setValue("/AUTOSAR/DataElements/Did1").setDest("DIAGNOSTIC-DATA-ELEMENT"))
        mapping.setMappedDataElementIRef(RefType().setValue("/AUTOSAR/System/DataProtos/Proto1"))
        pea = DiagnosticParameterElementAccess()
        pea.addContextElementRef(RefType().setValue("/AUTOSAR/ParamElements/Ctx1").setDest("DIAGNOSTIC-PARAMETER-ELEMENT"))
        pea.setTargetElementRef(RefType().setValue("/AUTOSAR/ParamElements/Target").setDest("DIAGNOSTIC-PARAMETER-ELEMENT"))
        mapping.setParameterElementAccess(pea)
        mapping.setDiagnosticParameterRef(RefType().setValue("/AUTOSAR/ParamIdents/Ident1").setDest("DIAGNOSTIC-PARAMETER-IDENT"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticServiceDataMapping(parent, mapping)

        child = parent.find("DIAGNOSTIC-SERVICE-DATA-MAPPING")
        assert [c.tag for c in child] == [
            "SHORT-NAME",
            "PROVIDER-SOFTWARE-CLUSTER-REF",
            "DIAGNOSTIC-DATA-ELEMENT-REF",
            "MAPPED-DATA-ELEMENT-IREF",
            "PARAMETER-ELEMENT-ACCESS",
            "DIAGNOSTIC-PARAMETER-REF",
        ]
        pea_element = child.find("PARAMETER-ELEMENT-ACCESS")
        assert [c.tag for c in pea_element] == ["CONTEXT-ELEMENT-REFS", "TARGET-ELEMENT-REF"]
        assert pea_element.find("TARGET-ELEMENT-REF").text == "/AUTOSAR/ParamElements/Target"
