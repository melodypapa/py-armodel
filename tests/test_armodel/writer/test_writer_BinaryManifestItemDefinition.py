"""Writer/reader round-trip tests for BinaryManifestItemDefinition (Table 11.23, p.920)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import BinaryManifestItemDefinition
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


def _new_item_definition(short_name: str = "Def1") -> BinaryManifestItemDefinition:
    item_definition = BinaryManifestItemDefinition(AUTOSAR.getInstance(), short_name)

    item_definition.setIsOptional(Boolean().setValue("true"))
    item_definition.setSize(PositiveInteger().setValue("4096"))

    auxiliary_field_definition = item_definition.createAuxiliaryFieldDefinition("FieldDef1")
    auxiliary_field_definition.setSize(PositiveInteger().setValue("8"))

    return item_definition


def _assert_all_fields(item_definition: BinaryManifestItemDefinition):
    assert item_definition.getIsOptional().getValue() is True
    assert item_definition.getSize().getValue() == 4096

    auxiliary_field_definitions = item_definition.getAuxiliaryFieldDefinitions()
    assert [field.getShortName() for field in auxiliary_field_definitions] == ["FieldDef1"]
    assert auxiliary_field_definitions[0].getSize().getValue() == 8
    assert auxiliary_field_definitions[0].getIsOptional() is None


class TestWriteBinaryManifestItemDefinition:
    def test_write_all_elements_in_xsd_order(self, writer):
        """
        The helper populates the caller-created element: SHORT-NAME via the Identifiable base
        group, then the three Table 11.23 rows in the XSD group order (AUTOSAR_00052.xsd
        l.8647): the AUXILIARY-FIELD-DEFINITIONS wrapper (emitted only when non-empty) carrying
        the BINARY-MANIFEST-ITEM-DEFINITION self-aggregation, IS-OPTIONAL and SIZE.
        """
        element = ET.Element("BINARY-MANIFEST-ITEM-DEFINITION")
        writer.writeBinaryManifestItemDefinition(element, _new_item_definition())

        tags = [child.tag for child in element]
        assert tags == [
            "SHORT-NAME",
            "AUXILIARY-FIELD-DEFINITIONS",
            "IS-OPTIONAL",
            "SIZE",
        ]
        assert element.find("SHORT-NAME").text == "Def1"
        assert element.find("AUXILIARY-FIELD-DEFINITIONS/BINARY-MANIFEST-ITEM-DEFINITION/SHORT-NAME").text == "FieldDef1"
        assert element.find("AUXILIARY-FIELD-DEFINITIONS/BINARY-MANIFEST-ITEM-DEFINITION/SIZE").text == "8"
        assert element.find("IS-OPTIONAL").text == "true"
        assert element.find("SIZE").text == "4096"

    def test_write_empty_element(self, writer):
        """
        An item definition without members emits only the SHORT-NAME: no
        AUXILIARY-FIELD-DEFINITIONS wrapper, no IS-OPTIONAL and no SIZE.
        """
        element = ET.Element("BINARY-MANIFEST-ITEM-DEFINITION")
        writer.writeBinaryManifestItemDefinition(element, BinaryManifestItemDefinition(AUTOSAR.getInstance(), "Def2"))

        tags = [child.tag for child in element]
        assert tags == ["SHORT-NAME"]


class TestBinaryManifestItemDefinitionRoundTrip:
    def test_round_trip_direct(self, writer, parser):
        """
        Write -> serialize -> re-parse through the readBinaryManifestItemDefinition /
        writeBinaryManifestItemDefinition helper pair keeps every field value, including the
        nested AUXILIARY-FIELD-DEFINITIONS self-aggregation.
        """
        item_definition = _new_item_definition()

        parent = ET.Element("PARENT")
        item_definition_element = ET.SubElement(parent, "BINARY-MANIFEST-ITEM-DEFINITION")
        writer.writeBinaryManifestItemDefinition(item_definition_element, item_definition)
        xml = ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1)
        root = ET.fromstring(xml)

        reloaded = BinaryManifestItemDefinition(AUTOSAR.getInstance(), "Def1")
        parser.readBinaryManifestItemDefinition(root[0], reloaded)
        assert reloaded.getShortName() == "Def1"
        _assert_all_fields(reloaded)

    def test_round_trip_empty_wrapper_list_case(self, writer, parser):
        """
        An empty wrapper case: an item definition without auxiliary field definitions emits no
        AUXILIARY-FIELD-DEFINITIONS wrapper, and an element without members re-parses to unset
        fields and an empty list.
        """
        element = ET.Element("BINARY-MANIFEST-ITEM-DEFINITION")
        writer.writeBinaryManifestItemDefinition(element, BinaryManifestItemDefinition(AUTOSAR.getInstance(), "Def2"))
        assert element.find("AUXILIARY-FIELD-DEFINITIONS") is None
        xml = ET.tostring(element).decode("utf-8").replace("<BINARY-MANIFEST-ITEM-DEFINITION>", "<BINARY-MANIFEST-ITEM-DEFINITION xmlns='%s'>" % NS, 1)
        parsed_element = ET.fromstring(xml)
        item_definition = parser.readBinaryManifestItemDefinition(parsed_element, BinaryManifestItemDefinition(AUTOSAR.getInstance(), "Def2"))
        assert item_definition.getIsOptional() is None
        assert item_definition.getSize() is None
        assert item_definition.getAuxiliaryFieldDefinitions() == []
