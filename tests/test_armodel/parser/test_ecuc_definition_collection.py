"""Parser tests for EcucDefinitionCollection (Table 2.1, p.25).

XSD group ECUC-DEFINITION-COLLECTION (AUTOSAR_00052.xsd) element order:
MODULE-REFS.
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
            '<MODULE-REF DEST="ECUC-MODULE-DEF">/AUTOSAR/EcucModuleDefs/Module1</MODULE-REF>'
            '<MODULE-REF DEST="ECUC-MODULE-DEF">/AUTOSAR/EcucModuleDefs/Module2</MODULE-REF>'
            "</MODULE-REFS>"
        )
        parser.readEcucDefinitionCollection(element, collection)
        assert collection.getShortName() == "Collection"
        refs = collection.getModuleRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/AUTOSAR/EcucModuleDefs/Module1"
        assert refs[0].getDest() == "ECUC-MODULE-DEF"
        assert refs[1].getValue() == "/AUTOSAR/EcucModuleDefs/Module2"

    def test_read_empty(self, parser):
        collection = EcucDefinitionCollection(AUTOSAR.getInstance(), "Collection")
        element = _snip("")
        parser.readEcucDefinitionCollection(element, collection)
        assert collection.getModuleRefs() == []
