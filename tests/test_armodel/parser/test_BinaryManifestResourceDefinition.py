"""Reader tests for BinaryManifestResourceDefinition (Table 11.21, p.917)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import BinaryManifestResourceDefinition
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    autosar = AUTOSAR.getInstance()
    autosar.new()
    autosar.setARRelease("R23-11")
    yield
    autosar.new()


@pytest.fixture
def parser():
    return ARXMLParser()


class TestReadBinaryManifestResourceDefinition:
    def test_read_item_definitions_wrapper(self, parser):
        """
        The Table 11.21 attribute (itemDefinition, mult *, ordered) is read in the XSD
        BINARY-MANIFEST-RESOURCE-DEFINITION group order (AUTOSAR_00052.xsd l.8947) after
        the inherited readIdentifiable helper reads SHORT-NAME: the ITEM-DEFINITIONS
        wrapper carries the unbounded BINARY-MANIFEST-ITEM-DEFINITION aggregation, whose
        items are dispatched through the synced readBinaryManifestItemDefinition helper.
        """
        element = ET.fromstring(
            "<BINARY-MANIFEST-RESOURCE-DEFINITION xmlns='%s'>"
            "<SHORT-NAME>ResDef1</SHORT-NAME>"
            "<ITEM-DEFINITIONS>"
            "<BINARY-MANIFEST-ITEM-DEFINITION><SHORT-NAME>ItemDef1</SHORT-NAME><IS-OPTIONAL>true</IS-OPTIONAL><SIZE>8</SIZE></BINARY-MANIFEST-ITEM-DEFINITION>"
            "<BINARY-MANIFEST-ITEM-DEFINITION><SHORT-NAME>ItemDef2</SHORT-NAME><SIZE>4096</SIZE></BINARY-MANIFEST-ITEM-DEFINITION>"
            "</ITEM-DEFINITIONS>"
            "</BINARY-MANIFEST-RESOURCE-DEFINITION>" % NS
        )

        resource_definition = BinaryManifestResourceDefinition(AUTOSAR.getInstance(), "ResDef1")
        parser.readBinaryManifestResourceDefinition(element, resource_definition)

        assert resource_definition.getShortName() == "ResDef1"
        item_definitions = resource_definition.getItemDefinitions()
        assert [item.getShortName() for item in item_definitions] == ["ItemDef1", "ItemDef2"]
        assert item_definitions[0].getIsOptional().getValue() is True
        assert item_definitions[0].getSize().getValue() == 8
        assert item_definitions[1].getIsOptional() is None
        assert item_definitions[1].getSize().getValue() == 4096

    def test_read_empty_element(self, parser):
        """
        An element without attribute content leaves the item definition list empty.
        """
        element = ET.fromstring("<BINARY-MANIFEST-RESOURCE-DEFINITION xmlns='%s'><SHORT-NAME>ResDef2</SHORT-NAME></BINARY-MANIFEST-RESOURCE-DEFINITION>" % NS)

        resource_definition = BinaryManifestResourceDefinition(AUTOSAR.getInstance(), "ResDef2")
        parser.readBinaryManifestResourceDefinition(element, resource_definition)

        assert resource_definition.getItemDefinitions() == []
