"""
Tests for writing ECUC-DEFINITION-COLLECTION elements —
EcucDefinitionCollection, Table 2.1 (p.25, R23-11).

EcucDefinitionCollection (Base most-derived AtpBlueprintable) owns the 0..*
module multi-reference (MODULE-REFS/MODULE-REF), AUTOSAR_00052.xsd group
ECUC-DEFINITION-COLLECTION.

Round-trip counterpart: tests/test_armodel/parser/test_ecuc_definition_collection.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucDefinitionCollection
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteEcucDefinitionCollection:
    """Tests for writeEcucDefinitionCollection — own element field values (Table 2.1)."""

    def test_write_empty_wrapper(self):
        """Test that an EcucDefinitionCollection without refs emits only the ARElement wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("EcucDefinitionCollections")
        package.createEcucDefinitionCollection("Collection1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeEcucDefinitionCollection(parent, package.getReferrableElement("Collection1", EcucDefinitionCollection))

        child = parent.find("ECUC-DEFINITION-COLLECTION")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Collection1"
        assert child.find("MODULE-REFS") is None

    def test_write_module_refs(self):
        """Test that the module multi-reference is emitted under MODULE-REFS with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("EcucDefinitionCollections")
        collection = package.createEcucDefinitionCollection("Collection1")
        ref = RefType()
        ref.setDest("ECUC-MODULE-DEF")
        ref.setValue("/AUTOSAR/EcucModuleDefs/Module1")
        collection.addModuleRef(ref)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeEcucDefinitionCollection(parent, collection)

        child = parent.find("ECUC-DEFINITION-COLLECTION")
        refs_tag = child.find("MODULE-REFS")
        assert refs_tag is not None
        refs = refs_tag.findall("MODULE-REF")
        assert len(refs) == 1
        assert refs[0].text == "/AUTOSAR/EcucModuleDefs/Module1"
        assert refs[0].attrib["DEST"] == "ECUC-MODULE-DEF"
