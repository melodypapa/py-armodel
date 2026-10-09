"""Writer/reader round-trip tests for BinaryManifestResource (Table 11.19, p.916)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import BinaryManifestResource
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    return ARXMLWriter()


@pytest.fixture
def parser():
    return ARXMLParser()


class ConcreteBinaryManifestResource(BinaryManifestResource):
    pass


def _new_resource() -> BinaryManifestResource:
    resource = ConcreteBinaryManifestResource(AUTOSAR.getInstance(), "Resource1")
    resource.setGlobalResourceId(PositiveInteger().setValue("4"))
    resource.createItem("Handle1")
    resource.setResourceRef(RefType().setValue("/AUTOSAR/CpSoftwareClusterResources/Res1").setDest("CP-SOFTWARE-CLUSTER-RESOURCE"))
    return resource


class TestWriteBinaryManifestResource:
    def test_write_elements_in_xsd_group_order(self, writer):
        """
        The helper writes the Identifiable level (SHORT-NAME, UUID) and the Table 11.19
        attributes in the XSD BINARY-MANIFEST-RESOURCE group order (GLOBAL-RESOURCE-ID, ITEMS
        wrapper, RESOURCE-REF).
        """
        element = ET.Element("BINARY-MANIFEST-PROVIDE-RESOURCE")
        writer.writeBinaryManifestResource(element, _new_resource())

        assert [child.tag for child in element] == ["SHORT-NAME", "GLOBAL-RESOURCE-ID", "ITEMS", "RESOURCE-REF"]
        assert element.find("GLOBAL-RESOURCE-ID").text == "4"
        assert [item.find("SHORT-NAME").text for item in element.findall("ITEMS/BINARY-MANIFEST-ITEM")] == ["Handle1"]
        assert element.find("RESOURCE-REF").text == "/AUTOSAR/CpSoftwareClusterResources/Res1"
        assert element.find("RESOURCE-REF").attrib["DEST"] == "CP-SOFTWARE-CLUSTER-RESOURCE"

    def test_write_empty_wrapper_list(self, writer):
        """
        With no items, no ITEMS wrapper is emitted (empty-wrapper-list case).
        """
        element = ET.Element("BINARY-MANIFEST-PROVIDE-RESOURCE")
        resource = ConcreteBinaryManifestResource(AUTOSAR.getInstance(), "Resource1")
        resource.setResourceRef(RefType().setValue("/AUTOSAR/CpSoftwareClusterResources/Res1").setDest("CP-SOFTWARE-CLUSTER-RESOURCE"))
        writer.writeBinaryManifestResource(element, resource)

        assert element.find("ITEMS") is None
        assert len(element.findall("RESOURCE-REF")) == 1


class TestBinaryManifestResourceRoundTrip:
    def test_round_trip_preserves_field_values(self, writer, parser):
        """
        Write -> serialize -> parse keeps the Identifiable level and every Table 11.19 value.
        """
        element = ET.Element("BINARY-MANIFEST-PROVIDE-RESOURCE")
        writer.writeBinaryManifestResource(element, _new_resource())
        xml = ET.tostring(element, encoding="unicode")

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        resource = ConcreteBinaryManifestResource(AUTOSAR.getInstance(), "Resource1")
        parser.readBinaryManifestResource(parsed_element, resource)

        assert resource.getShortName() == "Resource1"
        assert resource.getGlobalResourceId().getValue() == 4
        assert [item.getShortName() for item in resource.getItems()] == ["Handle1"]
        assert resource.getResourceRef().getValue() == "/AUTOSAR/CpSoftwareClusterResources/Res1"

    def test_round_trip_empty_wrapper_list(self, writer, parser):
        """
        A resource without items round-trips with an empty item list and no ITEMS wrapper.
        """
        element = ET.Element("BINARY-MANIFEST-PROVIDE-RESOURCE")
        resource = ConcreteBinaryManifestResource(AUTOSAR.getInstance(), "Resource1")
        writer.writeBinaryManifestResource(element, resource)
        xml = ET.tostring(element, encoding="unicode")

        assert "ITEMS" not in xml

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        parsed_resource = ConcreteBinaryManifestResource(AUTOSAR.getInstance(), "Resource1")
        parser.readBinaryManifestResource(parsed_element, parsed_resource)

        assert parsed_resource.getItems() == []
        assert parsed_resource.getGlobalResourceId() is None
        assert parsed_resource.getResourceRef() is None
