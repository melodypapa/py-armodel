"""
Tests for writing ECUC-DEFINITION-COLLECTION content —
EcucDefinitionCollection, Table 2.1 (p.25, R23-11).

XSD group ECUC-DEFINITION-COLLECTION (AUTOSAR_00052.xsd l.51778) element order:
MODULE-REFS (wrapper, MODULE-REF with DEST=ECUC-MODULE-DEF--SUBTYPES-ENUM).

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

    def _make(self):
        return EcucDefinitionCollection(AUTOSAR.getInstance().createARPackage("Pkg_W"), "Collection")

    def _write(self, collection) -> ET.Element:
        parent = ET.Element("ELEMENTS")
        ARXMLWriter().writeEcucDefinitionCollection(parent, collection)
        return parent.find("ECUC-DEFINITION-COLLECTION")

    def test_write_empty(self):
        """Test that an EcucDefinitionCollection without module refs emits only the IDENTIFIABLE content."""
        child_element = self._write(self._make())

        assert child_element.find("SHORT-NAME").text == "Collection"
        assert child_element.find("MODULE-REFS") is None

    def test_write_module_refs_in_xsd_order(self):
        """Test that module refs are wrapped in MODULE-REFS with DEST attributes."""
        collection = self._make()
        collection.addModuleRef(RefType().setValue("/EcucModuleDefs/ModuleA").setDest("ECUC-MODULE-DEF"))
        collection.addModuleRef(RefType().setValue("/EcucModuleDefs/ModuleB").setDest("ECUC-MODULE-DEF"))

        child_element = self._write(collection)

        module_refs = child_element.find("MODULE-REFS")
        assert module_refs is not None
        refs = module_refs.findall("MODULE-REF")
        assert len(refs) == 2
        assert [ref.text for ref in refs] == ["/EcucModuleDefs/ModuleA", "/EcucModuleDefs/ModuleB"]
        assert all(ref.attrib["DEST"] == "ECUC-MODULE-DEF" for ref in refs)
