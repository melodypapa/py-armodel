"""Parser tests for EcucDefinitionCollection (Table 2.1, p.25).

XSD group ECUC-DEFINITION-COLLECTION (AUTOSAR_00052.xsd l.51778) element order:
MODULE-REFS (wrapper, MODULE-REF with DEST=ECUC-MODULE-DEF--SUBTYPES-ENUM).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucDefinitionCollection

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "ECUC-DEFINITION-COLLECTION") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadEcucDefinitionCollection:
    def test_read_sets_all_fields(self, parser):
        collection = EcucDefinitionCollection(AUTOSAR.getInstance(), "Collection")
        element = _snip(
            "<SHORT-NAME>Collection</SHORT-NAME>"
            "<MODULE-REFS>"
            "<MODULE-REF DEST='ECUC-MODULE-DEF'>/EcucModuleDefs/ModuleA</MODULE-REF>"
            "<MODULE-REF DEST='ECUC-MODULE-DEF'>/EcucModuleDefs/ModuleB</MODULE-REF>"
            "</MODULE-REFS>"
        )
        parser.readEcucDefinitionCollection(element, collection)
        assert collection.getShortName() == "Collection"
        module_refs = collection.getModuleRefs()
        assert len(module_refs) == 2
        assert module_refs[0].getValue() == "/EcucModuleDefs/ModuleA"
        assert module_refs[0].getDest() == "ECUC-MODULE-DEF"
        assert module_refs[1].getValue() == "/EcucModuleDefs/ModuleB"
        assert module_refs[1].getDest() == "ECUC-MODULE-DEF"

    def test_read_empty(self, parser):
        collection = EcucDefinitionCollection(AUTOSAR.getInstance(), "Collection")
        element = _snip("")
        parser.readEcucDefinitionCollection(element, collection)
        assert collection.getModuleRefs() == []
