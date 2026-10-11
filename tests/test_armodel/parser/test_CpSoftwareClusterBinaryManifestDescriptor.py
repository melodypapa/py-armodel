"""Reader tests for the CpSoftwareClusterBinaryManifestDescriptor aggregator (Table 11.17, p.913)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import CpSoftwareClusterBinaryManifestDescriptor
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    BinaryManifestMetaDataField,
    BinaryManifestProvideResource,
    BinaryManifestRequireResource,
    BinaryManifestResourceDefinition,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    from armodel.models import AUTOSAR

    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    return ARXMLParser()


class TestReadCpSoftwareClusterBinaryManifestDescriptor:
    def test_read_all_elements(self, parser):
        """
        Every Table 11.17 row is read: the CP-SOFTWARE-CLUSTER-REF reference, the four
        aggregation wrappers (META-DATA-FIELDS, PROVIDE-RESOURCES, REQUIRE-RESOURCES,
        RESOURCE-DEFINITIONS) dispatching to the synced BinaryManifest* helpers and the
        SOFTWARE-CLUSTER-ID attribute.
        """
        element = ET.fromstring(
            "<CP-SOFTWARE-CLUSTER-BINARY-MANIFEST-DESCRIPTOR xmlns='%s' UUID='1a2b3c4d-5e6f-4aaa-bbbc-2e3f4a5b6c7d'>"
            "<SHORT-NAME>manifest1</SHORT-NAME>"
            "<CP-SOFTWARE-CLUSTER-REF DEST='CP-SOFTWARE-CLUSTER'>/Cluster/Cluster1</CP-SOFTWARE-CLUSTER-REF>"
            "<META-DATA-FIELDS>"
            "<BINARY-MANIFEST-META-DATA-FIELD><SHORT-NAME>field1</SHORT-NAME>"
            "<SIZE>16</SIZE><VALUE>CHECKSUM_TABLE_V1</VALUE></BINARY-MANIFEST-META-DATA-FIELD>"
            "</META-DATA-FIELDS>"
            "<PROVIDE-RESOURCES>"
            "<BINARY-MANIFEST-PROVIDE-RESOURCE><SHORT-NAME>provide1</SHORT-NAME>"
            "<GLOBAL-RESOURCE-ID>5</GLOBAL-RESOURCE-ID>"
            "<NUMBER-OF-NOTIFIER-SETS>2</NUMBER-OF-NOTIFIER-SETS>"
            "<SUPPORTS-MULTIPLE-NOTIFIER-SETS>true</SUPPORTS-MULTIPLE-NOTIFIER-SETS>"
            "</BINARY-MANIFEST-PROVIDE-RESOURCE>"
            "</PROVIDE-RESOURCES>"
            "<REQUIRE-RESOURCES>"
            "<BINARY-MANIFEST-REQUIRE-RESOURCE><SHORT-NAME>require1</SHORT-NAME>"
            "<CONNECTION-IS-MANDATORY>true</CONNECTION-IS-MANDATORY>"
            "</BINARY-MANIFEST-REQUIRE-RESOURCE>"
            "</REQUIRE-RESOURCES>"
            "<RESOURCE-DEFINITIONS>"
            "<BINARY-MANIFEST-RESOURCE-DEFINITION><SHORT-NAME>definition1</SHORT-NAME>"
            "</BINARY-MANIFEST-RESOURCE-DEFINITION>"
            "</RESOURCE-DEFINITIONS>"
            "<SOFTWARE-CLUSTER-ID>5</SOFTWARE-CLUSTER-ID>"
            "</CP-SOFTWARE-CLUSTER-BINARY-MANIFEST-DESCRIPTOR>" % NS
        )

        descriptor = parser.readCpSoftwareClusterBinaryManifestDescriptor(element, CpSoftwareClusterBinaryManifestDescriptor(None, "manifest1"))

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

    def test_read_empty_element(self, parser):
        """
        A descriptor without group content leaves all fields unset.
        """
        element = ET.fromstring("<CP-SOFTWARE-CLUSTER-BINARY-MANIFEST-DESCRIPTOR xmlns='%s'><SHORT-NAME>manifest2</SHORT-NAME></CP-SOFTWARE-CLUSTER-BINARY-MANIFEST-DESCRIPTOR>" % NS)

        descriptor = parser.readCpSoftwareClusterBinaryManifestDescriptor(element, CpSoftwareClusterBinaryManifestDescriptor(None, "manifest2"))

        assert descriptor.getCpSoftwareClusterRef() is None
        assert descriptor.getMetaDataFields() == []
        assert descriptor.getProvideResources() == []
        assert descriptor.getRequireResources() == []
        assert descriptor.getResourceDefinitions() == []
        assert descriptor.getSoftwareClusterId() is None
