"""Reader tests for BinaryManifestRequireResource (Table 11.20, p.916)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import BinaryManifestRequireResource
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


class TestReadBinaryManifestRequireResource:
    def test_read_full_element(self, parser):
        """
        The Table 11.20 attribute is read in the XSD BINARY-MANIFEST-REQUIRE-RESOURCE group
        order (AUTOSAR_00052.xsd l.8852: CONNECTION-IS-MANDATORY) after the inherited
        readBinaryManifestResource helper reads the Identifiable level and the
        BINARY-MANIFEST-RESOURCE group (GLOBAL-RESOURCE-ID, ITEMS, RESOURCE-REF).
        """
        element = ET.fromstring(
            "<BINARY-MANIFEST-REQUIRE-RESOURCE xmlns='%s'>"
            "<SHORT-NAME>RequireRes1</SHORT-NAME>"
            "<GLOBAL-RESOURCE-ID>7</GLOBAL-RESOURCE-ID>"
            "<ITEMS>"
            "<BINARY-MANIFEST-ITEM><SHORT-NAME>Handle1</SHORT-NAME><IS-UNUSED>true</IS-UNUSED></BINARY-MANIFEST-ITEM>"
            "</ITEMS>"
            "<CONNECTION-IS-MANDATORY>true</CONNECTION-IS-MANDATORY>"
            "</BINARY-MANIFEST-REQUIRE-RESOURCE>" % NS
        )

        require_resource = BinaryManifestRequireResource(AUTOSAR.getInstance(), "RequireRes1")
        parser.readBinaryManifestRequireResource(element, require_resource)

        assert require_resource.getShortName() == "RequireRes1"
        assert require_resource.getGlobalResourceId().getValue() == 7
        items = require_resource.getItems()
        assert [item.getShortName() for item in items] == ["Handle1"]
        assert items[0].getIsUnused().getValue() is True
        assert require_resource.getConnectionIsMandatory().getValue() is True

    def test_read_empty_element(self, parser):
        """
        An element without attribute content leaves the inherited item list empty and the
        optional attribute unset.
        """
        element = ET.fromstring("<BINARY-MANIFEST-REQUIRE-RESOURCE xmlns='%s'><SHORT-NAME>RequireRes2</SHORT-NAME></BINARY-MANIFEST-REQUIRE-RESOURCE>" % NS)

        require_resource = BinaryManifestRequireResource(AUTOSAR.getInstance(), "RequireRes2")
        parser.readBinaryManifestRequireResource(element, require_resource)

        assert require_resource.getShortName() == "RequireRes2"
        assert require_resource.getGlobalResourceId() is None
        assert require_resource.getItems() == []
        assert require_resource.getConnectionIsMandatory() is None
