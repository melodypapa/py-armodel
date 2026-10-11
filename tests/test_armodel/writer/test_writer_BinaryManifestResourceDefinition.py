"""Writer/reader round-trip tests for BinaryManifestResourceDefinition (Table 11.21, p.917)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import BinaryManifestResourceDefinition
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    autosar = AUTOSAR.getInstance()
    autosar.new()
    autosar.setARRelease("R23-11")
    yield
    autosar.new()


@pytest.fixture
def writer():
    return ARXMLWriter()


@pytest.fixture
def parser():
    return ARXMLParser()


def _new_resource_definition(short_name: str = "ResDef1") -> BinaryManifestResourceDefinition:
    resource_definition = BinaryManifestResourceDefinition(AUTOSAR.getInstance(), short_name)

    item_definition1 = resource_definition.createItemDefinition("ItemDef1")
    item_definition1.setIsOptional(Boolean().setValue("true"))
    item_definition1.setSize(PositiveInteger().setValue("8"))

    item_definition2 = resource_definition.createItemDefinition("ItemDef2")
    item_definition2.setSize(PositiveInteger().setValue("4096"))

    return resource_definition


def _assert_all_fields(resource_definition: BinaryManifestResourceDefinition):
    item_definitions = resource_definition.getItemDefinitions()
    assert [item.getShortName() for item in item_definitions] == ["ItemDef1", "ItemDef2"]
    assert item_definitions[0].getIsOptional().getValue() is True
    assert item_definitions[0].getSize().getValue() == 8
    assert item_definitions[1].getIsOptional() is None
    assert item_definitions[1].getSize().getValue() == 4096


class TestWriteBinaryManifestResourceDefinition:
    def test_write_all_elements_in_xsd_order(self, writer):
        """
        The helper populates the caller-created element: SHORT-NAME via the Identifiable base
        group, then the ITEM-DEFINITIONS wrapper (emitted only when non-empty) carrying the
        unbounded BINARY-MANIFEST-ITEM-DEFINITION aggregation in the XSD group order
        (AUTOSAR_00052.xsd l.8947), dispatched through writeBinaryManifestItemDefinition.
        """
        element = ET.Element("BINARY-MANIFEST-RESOURCE-DEFINITION")
        writer.writeBinaryManifestResourceDefinition(element, _new_resource_definition())

        tags = [child.tag for child in element]
        assert tags == ["SHORT-NAME", "ITEM-DEFINITIONS"]
        assert element.find("SHORT-NAME").text == "ResDef1"
        item_definitions = element.findall("ITEM-DEFINITIONS/BINARY-MANIFEST-ITEM-DEFINITION")
        assert [item.find("SHORT-NAME").text for item in item_definitions] == ["ItemDef1", "ItemDef2"]
        assert element.find("ITEM-DEFINITIONS/BINARY-MANIFEST-ITEM-DEFINITION/IS-OPTIONAL").text == "true"
        assert element.find("ITEM-DEFINITIONS/BINARY-MANIFEST-ITEM-DEFINITION/SIZE").text == "8"
        assert item_definitions[1].find("IS-OPTIONAL") is None
        assert item_definitions[1].find("SIZE").text == "4096"

    def test_write_empty_element(self, writer):
        """
        A resource definition without members emits only the SHORT-NAME: no ITEM-DEFINITIONS
        wrapper.
        """
        element = ET.Element("BINARY-MANIFEST-RESOURCE-DEFINITION")
        writer.writeBinaryManifestResourceDefinition(element, BinaryManifestResourceDefinition(AUTOSAR.getInstance(), "ResDef2"))

        tags = [child.tag for child in element]
        assert tags == ["SHORT-NAME"]


class TestBinaryManifestResourceDefinitionRoundTrip:
    def test_round_trip_direct(self, writer, parser):
        """
        Write -> serialize -> re-parse through the writeBinaryManifestResourceDefinition /
        readBinaryManifestResourceDefinition helper pair keeps every field value, including the
        nested ITEM-DEFINITIONS aggregation.
        """
        resource_definition = _new_resource_definition()

        parent = ET.Element("PARENT")
        resource_definition_element = ET.SubElement(parent, "BINARY-MANIFEST-RESOURCE-DEFINITION")
        writer.writeBinaryManifestResourceDefinition(resource_definition_element, resource_definition)
        xml = ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1)
        root = ET.fromstring(xml)

        reloaded = BinaryManifestResourceDefinition(AUTOSAR.getInstance(), "ResDef1")
        parser.readBinaryManifestResourceDefinition(root[0], reloaded)
        assert reloaded.getShortName() == "ResDef1"
        _assert_all_fields(reloaded)

    def test_round_trip_empty_wrapper_list_case(self, writer, parser):
        """
        An empty wrapper case: a resource definition without item definitions emits no
        ITEM-DEFINITIONS wrapper, and an element without members re-parses to unset state and
        an empty list.
        """
        element = ET.Element("BINARY-MANIFEST-RESOURCE-DEFINITION")
        writer.writeBinaryManifestResourceDefinition(element, BinaryManifestResourceDefinition(AUTOSAR.getInstance(), "ResDef2"))
        assert element.find("ITEM-DEFINITIONS") is None
        xml = ET.tostring(element).decode("utf-8").replace("<BINARY-MANIFEST-RESOURCE-DEFINITION>", "<BINARY-MANIFEST-RESOURCE-DEFINITION xmlns='%s'>" % NS, 1)
        parsed_element = ET.fromstring(xml)
        resource_definition = parser.readBinaryManifestResourceDefinition(parsed_element, BinaryManifestResourceDefinition(AUTOSAR.getInstance(), "ResDef2"))
        assert resource_definition.getItemDefinitions() == []
