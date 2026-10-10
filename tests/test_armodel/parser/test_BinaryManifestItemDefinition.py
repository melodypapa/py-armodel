"""Reader tests for BinaryManifestItemDefinition (Table 11.23, p.920)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import BinaryManifestItemDefinition
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


class TestReadBinaryManifestItemDefinition:
    def test_read_elements_in_xsd_group_order(self, parser):
        """
        The Table 11.23 attributes are read in the XSD BINARY-MANIFEST-ITEM-DEFINITION group
        order (AUTOSAR_00052.xsd l.8647: AUXILIARY-FIELD-DEFINITIONS, IS-OPTIONAL, SIZE) after
        the inherited readIdentifiable helper reads SHORT-NAME; the AUXILIARY-FIELD-DEFINITIONS
        wrapper carries the unbounded BINARY-MANIFEST-ITEM-DEFINITION self-aggregation.
        """
        element = ET.fromstring(
            "<BINARY-MANIFEST-ITEM-DEFINITION xmlns='%s'>"
            "<SHORT-NAME>Def1</SHORT-NAME>"
            "<AUXILIARY-FIELD-DEFINITIONS>"
            "<BINARY-MANIFEST-ITEM-DEFINITION><SHORT-NAME>FieldDef1</SHORT-NAME><SIZE>8</SIZE></BINARY-MANIFEST-ITEM-DEFINITION>"
            "</AUXILIARY-FIELD-DEFINITIONS>"
            "<IS-OPTIONAL>true</IS-OPTIONAL>"
            "<SIZE>4096</SIZE>"
            "</BINARY-MANIFEST-ITEM-DEFINITION>" % NS
        )

        item_definition = BinaryManifestItemDefinition(AUTOSAR.getInstance(), "Def1")
        parser.readBinaryManifestItemDefinition(element, item_definition)

        assert item_definition.getShortName() == "Def1"
        assert item_definition.getIsOptional().getValue() is True
        assert item_definition.getSize().getValue() == 4096
        auxiliary_field_definitions = item_definition.getAuxiliaryFieldDefinitions()
        assert [field.getShortName() for field in auxiliary_field_definitions] == ["FieldDef1"]
        assert auxiliary_field_definitions[0].getSize().getValue() == 8
        assert auxiliary_field_definitions[0].getIsOptional() is None

    def test_read_empty_element(self, parser):
        """
        An element without attribute content leaves the fields unset and the auxiliary
        field definition list empty.
        """
        element = ET.fromstring("<BINARY-MANIFEST-ITEM-DEFINITION xmlns='%s'><SHORT-NAME>Def2</SHORT-NAME></BINARY-MANIFEST-ITEM-DEFINITION>" % NS)

        item_definition = BinaryManifestItemDefinition(AUTOSAR.getInstance(), "Def2")
        parser.readBinaryManifestItemDefinition(element, item_definition)

        assert item_definition.getIsOptional() is None
        assert item_definition.getSize() is None
        assert item_definition.getAuxiliaryFieldDefinitions() == []
