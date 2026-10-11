"""Writer/reader round-trip tests for CpSoftwareClusterBinaryManifestDescriptor (Table 11.17, p.913)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import CpSoftwareClusterBinaryManifestDescriptor
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    BinaryManifestMetaDataField,
    BinaryManifestProvideResource,
    BinaryManifestRequireResource,
    BinaryManifestResourceDefinition,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    RefType,
    String,
    VerbatimString,
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


def _new_descriptor():
    descriptor = CpSoftwareClusterBinaryManifestDescriptor(None, "manifest1")
    descriptor.setUuid(String().setValue("1a2b3c4d-5e6f-4aaa-bbbc-2e3f4a5b6c7d"))
    descriptor.setCpSoftwareClusterRef(RefType().setValue("/Cluster/Cluster1").setDest("CP-SOFTWARE-CLUSTER"))
    field = descriptor.createMetaDataField("field1")
    field.setSize(PositiveInteger().setValue(16))
    field.setValue(VerbatimString().setValue("CHECKSUM_TABLE_V1"))
    provide_resource = descriptor.createProvideResource("provide1")
    provide_resource.setGlobalResourceId(PositiveInteger().setValue(5))
    provide_resource.setNumberOfNotifierSets(PositiveInteger().setValue(2))
    provide_resource.setSupportsMultipleNotifierSets(Boolean().setValue(True))
    require_resource = descriptor.createRequireResource("require1")
    require_resource.setConnectionIsMandatory(Boolean().setValue(True))
    descriptor.createResourceDefinition("definition1")
    descriptor.setSoftwareClusterId(PositiveInteger().setValue(5))
    return descriptor


class TestWriteCpSoftwareClusterBinaryManifestDescriptor:
    def test_write_all_elements_in_xsd_order(self, writer):
        """
        The helper writes the SHORT-NAME first, then the six Table 11.17 members in the
        XSD group element order (CP-SOFTWARE-CLUSTER-REF, META-DATA-FIELDS,
        PROVIDE-RESOURCES, REQUIRE-RESOURCES, RESOURCE-DEFINITIONS, SOFTWARE-CLUSTER-ID);
        the aggregation wrappers are emitted only when non-empty.
        """
        parent = ET.Element("AR-PACKAGE")
        writer.writeCpSoftwareClusterBinaryManifestDescriptor(parent, _new_descriptor())

        element = parent[0]
        assert element.tag == "CP-SOFTWARE-CLUSTER-BINARY-MANIFEST-DESCRIPTOR"
        assert element.attrib["UUID"] == "1a2b3c4d-5e6f-4aaa-bbbc-2e3f4a5b6c7d"
        assert [child.tag for child in element][0] == "SHORT-NAME"
        assert element.find("SHORT-NAME").text == "manifest1"

        ref = element.find("CP-SOFTWARE-CLUSTER-REF")
        assert ref.text == "/Cluster/Cluster1"
        assert ref.attrib["DEST"] == "CP-SOFTWARE-CLUSTER"

        meta_data_fields = element.find("META-DATA-FIELDS")
        assert [child.tag for child in meta_data_fields] == ["BINARY-MANIFEST-META-DATA-FIELD"]
        assert meta_data_fields[0].find("SHORT-NAME").text == "field1"
        assert meta_data_fields[0].find("SIZE").text == "16"
        assert meta_data_fields[0].find("VALUE").text == "CHECKSUM_TABLE_V1"

        provide_resources = element.find("PROVIDE-RESOURCES")
        assert [child.tag for child in provide_resources] == ["BINARY-MANIFEST-PROVIDE-RESOURCE"]
        assert provide_resources[0].find("SHORT-NAME").text == "provide1"
        assert provide_resources[0].find("GLOBAL-RESOURCE-ID").text == "5"
        assert provide_resources[0].find("NUMBER-OF-NOTIFIER-SETS").text == "2"
        assert provide_resources[0].find("SUPPORTS-MULTIPLE-NOTIFIER-SETS").text == "true"

        require_resources = element.find("REQUIRE-RESOURCES")
        assert [child.tag for child in require_resources] == ["BINARY-MANIFEST-REQUIRE-RESOURCE"]
        assert require_resources[0].find("SHORT-NAME").text == "require1"
        assert require_resources[0].find("CONNECTION-IS-MANDATORY").text == "true"

        resource_definitions = element.find("RESOURCE-DEFINITIONS")
        assert [child.tag for child in resource_definitions] == ["BINARY-MANIFEST-RESOURCE-DEFINITION"]
        assert resource_definitions[0].find("SHORT-NAME").text == "definition1"

        assert element.find("SOFTWARE-CLUSTER-ID").text == "5"

        tags = [child.tag for child in element]
        assert (
            tags.index("SHORT-NAME")
            < tags.index("CP-SOFTWARE-CLUSTER-REF")
            < tags.index("META-DATA-FIELDS")
            < tags.index("PROVIDE-RESOURCES")
            < tags.index("REQUIRE-RESOURCES")
            < tags.index("RESOURCE-DEFINITIONS")
            < tags.index("SOFTWARE-CLUSTER-ID")
        )

    def test_write_empty_element(self, writer):
        """
        A descriptor without members emits no aggregation wrappers.
        """
        parent = ET.Element("AR-PACKAGE")
        writer.writeCpSoftwareClusterBinaryManifestDescriptor(parent, CpSoftwareClusterBinaryManifestDescriptor(None, "manifest2"))

        element = parent[0]
        assert element.find("CP-SOFTWARE-CLUSTER-REF") is None
        assert element.find("META-DATA-FIELDS") is None
        assert element.find("PROVIDE-RESOURCES") is None
        assert element.find("REQUIRE-RESOURCES") is None
        assert element.find("RESOURCE-DEFINITIONS") is None
        assert element.find("SOFTWARE-CLUSTER-ID") is None


class TestCpSoftwareClusterBinaryManifestDescriptorRoundTrip:
    def test_round_trip_preserves_field_values(self, writer, parser):
        """
        Write -> serialize -> parse keeps every field value including the aggregated
        BinaryManifest* children inside their wrappers.
        """
        parent = ET.Element("AR-PACKAGE")
        writer.writeCpSoftwareClusterBinaryManifestDescriptor(parent, _new_descriptor())
        xml = ET.tostring(parent[0], encoding="unicode")

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        descriptor = parser.readCpSoftwareClusterBinaryManifestDescriptor(parsed_element, CpSoftwareClusterBinaryManifestDescriptor(None, "manifest1"))

        assert descriptor.getShortName() == "manifest1"
        assert descriptor.getUuid().getValue() == "1a2b3c4d-5e6f-4aaa-bbbc-2e3f4a5b6c7d"

        ref = descriptor.getCpSoftwareClusterRef()
        assert ref.getValue() == "/Cluster/Cluster1"
        assert ref.getDest() == "CP-SOFTWARE-CLUSTER"

        meta_data_fields = descriptor.getMetaDataFields()
        assert len(meta_data_fields) == 1
        assert isinstance(meta_data_fields[0], BinaryManifestMetaDataField)
        assert meta_data_fields[0].getShortName() == "field1"
        assert meta_data_fields[0].getSize().getValue() == 16
        assert meta_data_fields[0].getValue().getValue() == "CHECKSUM_TABLE_V1"

        provide_resources = descriptor.getProvideResources()
        assert len(provide_resources) == 1
        assert isinstance(provide_resources[0], BinaryManifestProvideResource)
        assert provide_resources[0].getShortName() == "provide1"
        assert provide_resources[0].getGlobalResourceId().getValue() == 5
        assert provide_resources[0].getNumberOfNotifierSets().getValue() == 2
        assert provide_resources[0].getSupportsMultipleNotifierSets().getValue() is True

        require_resources = descriptor.getRequireResources()
        assert len(require_resources) == 1
        assert isinstance(require_resources[0], BinaryManifestRequireResource)
        assert require_resources[0].getShortName() == "require1"
        assert require_resources[0].getConnectionIsMandatory().getValue() is True

        resource_definitions = descriptor.getResourceDefinitions()
        assert len(resource_definitions) == 1
        assert isinstance(resource_definitions[0], BinaryManifestResourceDefinition)
        assert resource_definitions[0].getShortName() == "definition1"

        assert descriptor.getSoftwareClusterId().getValue() == 5
