"""Writer/reader round-trip tests for BinaryManifestItem (Table 11.22, p.919)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    BinaryManifestItemNumericalValue,
    BinaryManifestItemPointerValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    BinaryManifestItem,
    BinaryManifestResource,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Address,
    Boolean,
    Numerical,
    SymbolString,
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


class ConcreteBinaryManifestResource(BinaryManifestResource):
    pass


def _new_item(short_name: str = "Handle1") -> BinaryManifestItem:
    item = BinaryManifestItem(AUTOSAR.getInstance(), short_name)

    item.setAddress(Address().setValue("0x1000"))
    item.setSymbol(SymbolString().setValue("HANDLE_1"))
    item.setIsUnused(Boolean().setValue("true"))

    value = BinaryManifestItemNumericalValue()
    value.setValue(Numerical().setValue("4096"))
    item.setValue(value)

    default_value = BinaryManifestItemPointerValue()
    default_value.setAddress(Address().setValue("0x2000"))
    item.setDefaultValue(default_value)

    auxiliary_field = item.createAuxiliaryField("Field1")
    auxiliary_field.setIsUnused(Boolean().setValue("false"))

    return item


def _assert_all_fields(item: BinaryManifestItem):
    assert item.getAddress().getValue() == "0x1000"
    assert item.getSymbol().getValue() == "HANDLE_1"
    assert item.getIsUnused().getValue() is True

    assert isinstance(item.getValue(), BinaryManifestItemNumericalValue)
    assert item.getValue().getValue().getValue() == 4096

    assert isinstance(item.getDefaultValue(), BinaryManifestItemPointerValue)
    assert item.getDefaultValue().getAddress().getValue() == "0x2000"

    auxiliary_fields = item.getAuxiliaryFields()
    assert [field.getShortName() for field in auxiliary_fields] == ["Field1"]
    assert auxiliary_fields[0].getIsUnused().getValue() is False


class TestWriteBinaryManifestItem:
    def test_write_all_elements_in_xsd_order(self, writer):
        """
        The helper populates the caller-created element: SHORT-NAME / ADDRESS / SYMBOL via
        the BinaryManifestAddressableObject base group, then the four Table 11.22 rows in
        the XSD group order (AUTOSAR_00052.xsd l.8574), with the VALUE / DEFAULT-VALUE
        wrappers each carrying the BINARY-MANIFEST-ITEM-NUMERICAL-VALUE or
        BINARY-MANIFEST-ITEM-POINTER-VALUE choice child and the AUXILIARY-FIELDS wrapper
        emitted only when non-empty.
        """
        element = ET.Element("BINARY-MANIFEST-ITEM")
        writer.writeBinaryManifestItem(element, _new_item())

        tags = [child.tag for child in element]
        assert tags == [
            "SHORT-NAME",
            "ADDRESS",
            "SYMBOL",
            "IS-UNUSED",
            "VALUE",
            "DEFAULT-VALUE",
            "AUXILIARY-FIELDS",
        ]
        assert element.find("SHORT-NAME").text == "Handle1"
        assert element.find("ADDRESS").text == "0x1000"
        assert element.find("SYMBOL").text == "HANDLE_1"
        assert element.find("IS-UNUSED").text == "true"
        numerical_element = element.find("VALUE/BINARY-MANIFEST-ITEM-NUMERICAL-VALUE")
        assert numerical_element is not None
        assert numerical_element.find("VALUE").text == "4096"
        pointer_element = element.find("DEFAULT-VALUE/BINARY-MANIFEST-ITEM-POINTER-VALUE")
        assert pointer_element is not None
        assert pointer_element.find("ADDRESS").text == "0x2000"
        assert element.find("AUXILIARY-FIELDS/BINARY-MANIFEST-ITEM/SHORT-NAME").text == "Field1"

    def test_write_empty_element(self, writer):
        """
        An item without members emits only the SHORT-NAME: no IS-UNUSED, no VALUE /
        DEFAULT-VALUE wrappers and no AUXILIARY-FIELDS wrapper.
        """
        element = ET.Element("BINARY-MANIFEST-ITEM")
        writer.writeBinaryManifestItem(element, BinaryManifestItem(AUTOSAR.getInstance(), "Handle2"))

        tags = [child.tag for child in element]
        assert tags == ["SHORT-NAME"]


class TestBinaryManifestItemRoundTrip:
    def test_round_trip_via_binary_manifest_resource(self, writer, parser):
        """
        Write -> serialize -> re-parse through the BinaryManifestResource ITEMS dispatch
        keeps every field value.
        """
        resource = ConcreteBinaryManifestResource(AUTOSAR.getInstance(), "Resource1")
        resource.createItem("Handle1")
        stored = resource.getItems()[0]
        populated = _new_item("Handle1")
        stored.setAddress(populated.getAddress())
        stored.setSymbol(populated.getSymbol())
        stored.setIsUnused(populated.getIsUnused())
        stored.setValue(populated.getValue())
        stored.setDefaultValue(populated.getDefaultValue())
        auxiliary_field = stored.createAuxiliaryField("Field1")
        auxiliary_field.setIsUnused(Boolean().setValue("false"))

        parent = ET.Element("PARENT")
        resource_element = ET.SubElement(parent, "BINARY-MANIFEST-PROVIDE-RESOURCE")
        writer.writeBinaryManifestResource(resource_element, resource)
        xml = ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1)
        root = ET.fromstring(xml)

        reloaded = ConcreteBinaryManifestResource(AUTOSAR.getInstance(), "Resource1")
        parser.readBinaryManifestResource(root[0], reloaded)

        items = reloaded.getItems()
        assert len(items) == 1
        assert items[0].getShortName() == "Handle1"
        _assert_all_fields(items[0])

    def test_round_trip_via_nested_auxiliary_field(self, writer, parser):
        """
        The self-aggregation AUXILIARY-FIELDS round-trips through the same
        readBinaryManifestItem / writeBinaryManifestItem helpers recursively.
        """
        item = _new_item("Handle1")

        parent = ET.Element("PARENT")
        item_element = ET.SubElement(parent, "BINARY-MANIFEST-ITEM")
        writer.writeBinaryManifestItem(item_element, item)
        xml = ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1)
        root = ET.fromstring(xml)

        reloaded = BinaryManifestItem(AUTOSAR.getInstance(), "Handle1")
        parser.readBinaryManifestItem(root[0], reloaded)
        _assert_all_fields(reloaded)

    def test_round_trip_empty_wrapper_list_case(self, writer, parser):
        """
        An empty wrapper case: a resource without items emits no ITEMS wrapper, and an
        item without members re-parses to unset fields.
        """
        resource = ConcreteBinaryManifestResource(AUTOSAR.getInstance(), "Resource1")
        parent = ET.Element("PARENT")
        resource_element = ET.SubElement(parent, "BINARY-MANIFEST-PROVIDE-RESOURCE")
        writer.writeBinaryManifestResource(resource_element, resource)
        xml = ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1)
        root = ET.fromstring(xml)

        reloaded = ConcreteBinaryManifestResource(AUTOSAR.getInstance(), "Resource1")
        parser.readBinaryManifestResource(root[0], reloaded)
        assert reloaded.getItems() == []

        element = ET.Element("BINARY-MANIFEST-ITEM")
        writer.writeBinaryManifestItem(element, BinaryManifestItem(AUTOSAR.getInstance(), "Handle2"))
        xml = ET.tostring(element).decode("utf-8").replace("<BINARY-MANIFEST-ITEM>", "<BINARY-MANIFEST-ITEM xmlns='%s'>" % NS, 1)
        parsed_element = ET.fromstring(xml)
        item = parser.readBinaryManifestItem(parsed_element, BinaryManifestItem(AUTOSAR.getInstance(), "Handle2"))
        assert item.getIsUnused() is None
        assert item.getValue() is None
        assert item.getDefaultValue() is None
        assert item.getAuxiliaryFields() == []
