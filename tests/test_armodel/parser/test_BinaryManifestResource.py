"""Reader tests for BinaryManifestResource (Table 11.19, p.916)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import BinaryManifestResource
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    return ARXMLParser()


class ConcreteBinaryManifestResource(BinaryManifestResource):
    pass


class TestReadBinaryManifestResource:
    def test_read_elements_in_xsd_group_order(self, parser):
        """
        The Table 11.19 attributes are read from the concrete subclass element in the XSD
        BINARY-MANIFEST-RESOURCE group order (GLOBAL-RESOURCE-ID, ITEMS, RESOURCE-REF) and the
        inherited Identifiable helper reads SHORT-NAME / UUID.
        """
        element = ET.fromstring(
            "<BINARY-MANIFEST-PROVIDE-RESOURCE xmlns='%s'>"
            "<SHORT-NAME>Resource1</SHORT-NAME>"
            "<UUID>11111111-1111-1111-1111-111111111111</UUID>"
            "<GLOBAL-RESOURCE-ID>4</GLOBAL-RESOURCE-ID>"
            "<ITEMS>"
            "<BINARY-MANIFEST-ITEM><SHORT-NAME>Handle1</SHORT-NAME></BINARY-MANIFEST-ITEM>"
            "<BINARY-MANIFEST-ITEM><SHORT-NAME>Handle2</SHORT-NAME></BINARY-MANIFEST-ITEM>"
            "</ITEMS>"
            "<RESOURCE-REF DEST='CP-SOFTWARE-CLUSTER-RESOURCE'>/AUTOSAR/CpSoftwareClusterResources/Res1</RESOURCE-REF>"
            "</BINARY-MANIFEST-PROVIDE-RESOURCE>" % NS
        )

        resource = ConcreteBinaryManifestResource(AUTOSAR.getInstance(), "Resource1")
        parser.readBinaryManifestResource(element, resource)

        assert resource.getShortName() == "Resource1"
        assert resource.getGlobalResourceId().getValue() == 4
        assert [item.getShortName() for item in resource.getItems()] == ["Handle1", "Handle2"]
        assert resource.getResourceRef().getValue() == "/AUTOSAR/CpSoftwareClusterResources/Res1"
        assert resource.getResourceRef().getDest() == "CP-SOFTWARE-CLUSTER-RESOURCE"

    def test_read_empty_element(self, parser):
        """
        An element without attribute content leaves the fields unset and the item list empty.
        """
        element = ET.fromstring("<BINARY-MANIFEST-PROVIDE-RESOURCE xmlns='%s'><SHORT-NAME>Resource1</SHORT-NAME></BINARY-MANIFEST-PROVIDE-RESOURCE>" % NS)

        resource = ConcreteBinaryManifestResource(AUTOSAR.getInstance(), "Resource1")
        parser.readBinaryManifestResource(element, resource)

        assert resource.getGlobalResourceId() is None
        assert resource.getItems() == []
        assert resource.getResourceRef() is None
