"""
Tests for writing DIAGNOSTIC-CONTRIBUTION-SET elements — DiagnosticContributionSet, Table 4.14 (p.57, R23-11).

DiagnosticContributionSet (Base = ARElement) carries COMMON-PROPERTIES
(DiagnosticCommonProps, 0..1 aggr) and the two wrapper reference lists
ELEMENTS (DIAGNOSTIC-COMMON-ELEMENT-REF-CONDITIONAL items) and SERVICE-TABLES
(DIAGNOSTIC-SERVICE-TABLE-REF-CONDITIONAL items) — XSD group
DIAGNOSTIC-CONTRIBUTION-SET, AUTOSAR_00052.xsd l.33717. The writer reads the
model via the getCommonProperties/getElementRefs/getServiceTableRefs getters;
the dispatch entry is writeARPackageElement → writeDiagnosticContributionSet.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_contribution_set.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticCommonProps
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticContributionSet
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


class TestWriteDiagnosticContributionSet:
    """Tests for writeDiagnosticContributionSet — own element field values (Table 4.14)."""

    def test_write_field_values_in_xsd_order(self):
        """Test that COMMON-PROPERTIES, ELEMENTS and SERVICE-TABLES are emitted with field values in XSD order."""
        contribution_set = DiagnosticContributionSet(parent=AUTOSAR.getInstance(), short_name="Dcs")
        contribution_set.setCommonProperties(DiagnosticCommonProps())
        contribution_set.addElementRef(_ref("DIAGNOSTIC-COMMON-ELEMENT", "/AUTOSAR/DiagnosticCommonElements/Did"))
        contribution_set.addElementRef(_ref("DIAGNOSTIC-COMMON-ELEMENT", "/AUTOSAR/DiagnosticCommonElements/Rid"))
        contribution_set.addServiceTableRef(_ref("DIAGNOSTIC-SERVICE-TABLE", "/AUTOSAR/DiagnosticServiceTables/Table"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticContributionSet(parent, contribution_set)

        child = parent.find("DIAGNOSTIC-CONTRIBUTION-SET")
        assert child is not None
        assert child.find("COMMON-PROPERTIES") is not None
        elements = child.find("ELEMENTS")
        assert elements is not None
        conditionals = elements.findall("DIAGNOSTIC-COMMON-ELEMENT-REF-CONDITIONAL")
        assert len(conditionals) == 2
        first_ref = conditionals[0].find("DIAGNOSTIC-COMMON-ELEMENT-REF")
        assert first_ref.attrib["DEST"] == "DIAGNOSTIC-COMMON-ELEMENT"
        assert first_ref.text == "/AUTOSAR/DiagnosticCommonElements/Did"
        service_tables = child.find("SERVICE-TABLES")
        assert service_tables is not None
        service_ref = service_tables.find("DIAGNOSTIC-SERVICE-TABLE-REF-CONDITIONAL/DIAGNOSTIC-SERVICE-TABLE-REF")
        assert service_ref.attrib["DEST"] == "DIAGNOSTIC-SERVICE-TABLE"
        assert service_ref.text == "/AUTOSAR/DiagnosticServiceTables/Table"
        tags = [c.tag for c in child if c.tag != "SHORT-NAME"]
        assert tags == ["COMMON-PROPERTIES", "ELEMENTS", "SERVICE-TABLES"]

    def test_write_unset_fields_omits_tags(self):
        """Test that unset fields and empty ref lists emit no wrapper elements."""
        contribution_set = DiagnosticContributionSet(parent=AUTOSAR.getInstance(), short_name="Dcs")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticContributionSet(parent, contribution_set)

        child = parent.find("DIAGNOSTIC-CONTRIBUTION-SET")
        assert child is not None
        assert [c.tag for c in child] == ["SHORT-NAME"]
        assert child.find("COMMON-PROPERTIES") is None
        assert child.find("ELEMENTS") is None
        assert child.find("SERVICE-TABLES") is None

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticContributionSet to a DIAGNOSTIC-CONTRIBUTION-SET element."""
        package = AUTOSAR.getInstance().createARPackage("ContributionSets")
        contribution_set = package.createDiagnosticContributionSet("Dcs")
        contribution_set.addElementRef(_ref("DIAGNOSTIC-COMMON-ELEMENT", "/AUTOSAR/DiagnosticCommonElements/Did"))

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, contribution_set)

        child = parent.find("DIAGNOSTIC-CONTRIBUTION-SET")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Dcs"
        assert child.find("ELEMENTS/DIAGNOSTIC-COMMON-ELEMENT-REF-CONDITIONAL/DIAGNOSTIC-COMMON-ELEMENT-REF").text == "/AUTOSAR/DiagnosticCommonElements/Did"

    def test_round_trip(self):
        """Test the full set → save → reload → assert cycle over an ARPackage with field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("ContributionSets")
        contribution_set = package.createDiagnosticContributionSet("Dcs")
        contribution_set.setCommonProperties(DiagnosticCommonProps())
        contribution_set.addElementRef(_ref("DIAGNOSTIC-COMMON-ELEMENT", "/AUTOSAR/DiagnosticCommonElements/Did"))
        contribution_set.addElementRef(_ref("DIAGNOSTIC-COMMON-ELEMENT", "/AUTOSAR/DiagnosticCommonElements/Rid"))
        contribution_set.addServiceTableRef(_ref("DIAGNOSTIC-SERVICE-TABLE", "/AUTOSAR/DiagnosticServiceTables/Table"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            contribution_set_2 = package_2.getReferrableElement("Dcs", DiagnosticContributionSet)
            assert contribution_set_2 is not None
            assert contribution_set_2.getCommonProperties() is not None
            refs = contribution_set_2.getElementRefs()
            assert len(refs) == 2
            assert refs[0].getDest() == "DIAGNOSTIC-COMMON-ELEMENT"
            assert refs[0].getValue() == "/AUTOSAR/DiagnosticCommonElements/Did"
            assert refs[1].getValue() == "/AUTOSAR/DiagnosticCommonElements/Rid"
            table_refs = contribution_set_2.getServiceTableRefs()
            assert len(table_refs) == 1
            assert table_refs[0].getDest() == "DIAGNOSTIC-SERVICE-TABLE"
            assert table_refs[0].getValue() == "/AUTOSAR/DiagnosticServiceTables/Table"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_empty(self):
        """Test that a DiagnosticContributionSet without field values round-trips with all fields empty."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("ContributionSets")
        package.createDiagnosticContributionSet("Dcs")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            contribution_set_2 = package_2.getReferrableElement("Dcs", DiagnosticContributionSet)
            assert contribution_set_2 is not None
            assert contribution_set_2.getCommonProperties() is None
            assert contribution_set_2.getElementRefs() == []
            assert contribution_set_2.getServiceTableRefs() == []
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
