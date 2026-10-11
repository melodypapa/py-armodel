"""Writer/reader round-trip tests for BinaryManifestProvideResource (Table 11.18, p.914)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import BinaryManifestProvideResource
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    RefType,
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


def _new_provide_resource(short_name: str = "ProvideRes1") -> BinaryManifestProvideResource:
    provide_resource = BinaryManifestProvideResource(AUTOSAR.getInstance(), short_name)
    provide_resource.setGlobalResourceId(PositiveInteger().setValue("7"))
    provide_resource.createItem("Handle1")
    provide_resource.setResourceRef(RefType().setValue("/AUTOSAR/CpSoftwareClusterResources/Res1").setDest("CP-SOFTWARE-CLUSTER-RESOURCE"))
    provide_resource.setNumberOfNotifierSets(PositiveInteger().setValue("4"))
    provide_resource.setSupportsMultipleNotifierSets(Boolean().setValue("true"))
    return provide_resource


def _assert_all_fields(provide_resource: BinaryManifestProvideResource):
    assert provide_resource.getShortName() == "ProvideRes1"
    assert provide_resource.getGlobalResourceId().getValue() == 7
    assert [item.getShortName() for item in provide_resource.getItems()] == ["Handle1"]
    assert provide_resource.getResourceRef().getValue() == "/AUTOSAR/CpSoftwareClusterResources/Res1"
    assert provide_resource.getNumberOfNotifierSets().getValue() == 4
    assert provide_resource.getSupportsMultipleNotifierSets().getValue() is True


class TestWriteBinaryManifestProvideResource:
    def test_write_all_elements_in_xsd_order(self, writer):
        """
        The helper populates the caller-created element: SHORT-NAME via the Identifiable base
        group, then the inherited BINARY-MANIFEST-RESOURCE group (GLOBAL-RESOURCE-ID, ITEMS
        wrapper, RESOURCE-REF), then the Table 11.18 attributes in the XSD
        BINARY-MANIFEST-PROVIDE-RESOURCE group order (AUTOSAR_00052.xsd l.8812:
        NUMBER-OF-NOTIFIER-SETS, SUPPORTS-MULTIPLE-NOTIFIER-SETS).
        """
        element = ET.Element("BINARY-MANIFEST-PROVIDE-RESOURCE")
        writer.writeBinaryManifestProvideResource(element, _new_provide_resource())

        assert [child.tag for child in element] == [
            "SHORT-NAME",
            "GLOBAL-RESOURCE-ID",
            "ITEMS",
            "RESOURCE-REF",
            "NUMBER-OF-NOTIFIER-SETS",
            "SUPPORTS-MULTIPLE-NOTIFIER-SETS",
        ]
        assert element.find("GLOBAL-RESOURCE-ID").text == "7"
        assert [item.find("SHORT-NAME").text for item in element.findall("ITEMS/BINARY-MANIFEST-ITEM")] == ["Handle1"]
        assert element.find("RESOURCE-REF").text == "/AUTOSAR/CpSoftwareClusterResources/Res1"
        assert element.find("NUMBER-OF-NOTIFIER-SETS").text == "4"
        assert element.find("SUPPORTS-MULTIPLE-NOTIFIER-SETS").text == "true"

    def test_write_empty_element(self, writer):
        """
        A provide resource without members emits only the SHORT-NAME: no ITEMS wrapper and no
        optional attribute elements.
        """
        element = ET.Element("BINARY-MANIFEST-PROVIDE-RESOURCE")
        writer.writeBinaryManifestProvideResource(element, BinaryManifestProvideResource(AUTOSAR.getInstance(), "ProvideRes2"))

        assert [child.tag for child in element] == ["SHORT-NAME"]


class TestBinaryManifestProvideResourceRoundTrip:
    def test_round_trip_direct(self, writer, parser):
        """
        Write -> serialize -> re-parse through the writeBinaryManifestProvideResource /
        readBinaryManifestProvideResource helper pair keeps every field value, including the
        inherited BINARY-MANIFEST-RESOURCE group and the nested ITEMS aggregation.
        """
        provide_resource = _new_provide_resource()

        parent = ET.Element("PARENT")
        provide_resource_element = ET.SubElement(parent, "BINARY-MANIFEST-PROVIDE-RESOURCE")
        writer.writeBinaryManifestProvideResource(provide_resource_element, provide_resource)
        xml = ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1)
        root = ET.fromstring(xml)

        reloaded = BinaryManifestProvideResource(AUTOSAR.getInstance(), "ProvideRes1")
        parser.readBinaryManifestProvideResource(root[0], reloaded)
        _assert_all_fields(reloaded)

    def test_round_trip_empty_wrapper_list_case(self, writer, parser):
        """
        An empty wrapper case: a provide resource without items emits no ITEMS wrapper, and an
        element without members re-parses to unset state and an empty list.
        """
        element = ET.Element("BINARY-MANIFEST-PROVIDE-RESOURCE")
        writer.writeBinaryManifestProvideResource(element, BinaryManifestProvideResource(AUTOSAR.getInstance(), "ProvideRes2"))
        assert element.find("ITEMS") is None
        xml = ET.tostring(element).decode("utf-8").replace("<BINARY-MANIFEST-PROVIDE-RESOURCE>", "<BINARY-MANIFEST-PROVIDE-RESOURCE xmlns='%s'>" % NS, 1)
        parsed_element = ET.fromstring(xml)
        reloaded = parser.readBinaryManifestProvideResource(parsed_element, BinaryManifestProvideResource(AUTOSAR.getInstance(), "ProvideRes2"))
        assert reloaded.getGlobalResourceId() is None
        assert reloaded.getItems() == []
        assert reloaded.getResourceRef() is None
        assert reloaded.getNumberOfNotifierSets() is None
        assert reloaded.getSupportsMultipleNotifierSets() is None
