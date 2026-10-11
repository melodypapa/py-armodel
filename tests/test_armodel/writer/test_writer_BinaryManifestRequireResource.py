"""Writer/reader round-trip tests for BinaryManifestRequireResource (Table 11.20, p.916)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import BinaryManifestRequireResource
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


def _new_require_resource(short_name: str = "RequireRes1") -> BinaryManifestRequireResource:
    require_resource = BinaryManifestRequireResource(AUTOSAR.getInstance(), short_name)
    require_resource.setGlobalResourceId(PositiveInteger().setValue("7"))
    require_resource.createItem("Handle1")
    require_resource.setResourceRef(RefType().setValue("/AUTOSAR/CpSoftwareClusterResources/Res1").setDest("CP-SOFTWARE-CLUSTER-RESOURCE"))
    require_resource.setConnectionIsMandatory(Boolean().setValue("true"))
    return require_resource


def _assert_all_fields(require_resource: BinaryManifestRequireResource):
    assert require_resource.getShortName() == "RequireRes1"
    assert require_resource.getGlobalResourceId().getValue() == 7
    assert [item.getShortName() for item in require_resource.getItems()] == ["Handle1"]
    assert require_resource.getResourceRef().getValue() == "/AUTOSAR/CpSoftwareClusterResources/Res1"
    assert require_resource.getConnectionIsMandatory().getValue() is True


class TestWriteBinaryManifestRequireResource:
    def test_write_all_elements_in_xsd_order(self, writer):
        """
        The helper populates the caller-created element: SHORT-NAME via the Identifiable base
        group, then the inherited BINARY-MANIFEST-RESOURCE group (GLOBAL-RESOURCE-ID, ITEMS
        wrapper, RESOURCE-REF), then the Table 11.20 attribute in the XSD
        BINARY-MANIFEST-REQUIRE-RESOURCE group order (AUTOSAR_00052.xsd l.8852:
        CONNECTION-IS-MANDATORY).
        """
        element = ET.Element("BINARY-MANIFEST-REQUIRE-RESOURCE")
        writer.writeBinaryManifestRequireResource(element, _new_require_resource())

        assert [child.tag for child in element] == [
            "SHORT-NAME",
            "GLOBAL-RESOURCE-ID",
            "ITEMS",
            "RESOURCE-REF",
            "CONNECTION-IS-MANDATORY",
        ]
        assert element.find("GLOBAL-RESOURCE-ID").text == "7"
        assert [item.find("SHORT-NAME").text for item in element.findall("ITEMS/BINARY-MANIFEST-ITEM")] == ["Handle1"]
        assert element.find("RESOURCE-REF").text == "/AUTOSAR/CpSoftwareClusterResources/Res1"
        assert element.find("CONNECTION-IS-MANDATORY").text == "true"

    def test_write_empty_element(self, writer):
        """
        A require resource without members emits only the SHORT-NAME: no ITEMS wrapper and no
        optional attribute element.
        """
        element = ET.Element("BINARY-MANIFEST-REQUIRE-RESOURCE")
        writer.writeBinaryManifestRequireResource(element, BinaryManifestRequireResource(AUTOSAR.getInstance(), "RequireRes2"))

        assert [child.tag for child in element] == ["SHORT-NAME"]


class TestBinaryManifestRequireResourceRoundTrip:
    def test_round_trip_direct(self, writer, parser):
        """
        Write -> serialize -> re-parse through the writeBinaryManifestRequireResource /
        readBinaryManifestRequireResource helper pair keeps every field value, including the
        inherited BINARY-MANIFEST-RESOURCE group and the nested ITEMS aggregation.
        """
        require_resource = _new_require_resource()

        parent = ET.Element("PARENT")
        require_resource_element = ET.SubElement(parent, "BINARY-MANIFEST-REQUIRE-RESOURCE")
        writer.writeBinaryManifestRequireResource(require_resource_element, require_resource)
        xml = ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1)
        root = ET.fromstring(xml)

        reloaded = BinaryManifestRequireResource(AUTOSAR.getInstance(), "RequireRes1")
        parser.readBinaryManifestRequireResource(root[0], reloaded)
        _assert_all_fields(reloaded)

    def test_round_trip_empty_wrapper_list_case(self, writer, parser):
        """
        An empty wrapper case: a require resource without items emits no ITEMS wrapper, and an
        element without members re-parses to unset state and an empty list.
        """
        element = ET.Element("BINARY-MANIFEST-REQUIRE-RESOURCE")
        writer.writeBinaryManifestRequireResource(element, BinaryManifestRequireResource(AUTOSAR.getInstance(), "RequireRes2"))
        assert element.find("ITEMS") is None
        xml = ET.tostring(element).decode("utf-8").replace("<BINARY-MANIFEST-REQUIRE-RESOURCE>", "<BINARY-MANIFEST-REQUIRE-RESOURCE xmlns='%s'>" % NS, 1)
        parsed_element = ET.fromstring(xml)
        reloaded = parser.readBinaryManifestRequireResource(parsed_element, BinaryManifestRequireResource(AUTOSAR.getInstance(), "RequireRes2"))
        assert reloaded.getGlobalResourceId() is None
        assert reloaded.getItems() == []
        assert reloaded.getResourceRef() is None
        assert reloaded.getConnectionIsMandatory() is None
