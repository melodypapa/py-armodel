"""Reader tests for BinaryManifestProvideResource (Table 11.18, p.914)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import BinaryManifestProvideResource
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


class TestReadBinaryManifestProvideResource:
    def test_read_full_element(self, parser):
        """
        The Table 11.18 attributes are read in the XSD BINARY-MANIFEST-PROVIDE-RESOURCE group
        order (AUTOSAR_00052.xsd l.8812: NUMBER-OF-NOTIFIER-SETS, SUPPORTS-MULTIPLE-NOTIFIER-SETS)
        after the inherited readBinaryManifestResource helper reads the Identifiable level and the
        BINARY-MANIFEST-RESOURCE group (GLOBAL-RESOURCE-ID, ITEMS, RESOURCE-REF).
        """
        element = ET.fromstring(
            "<BINARY-MANIFEST-PROVIDE-RESOURCE xmlns='%s'>"
            "<SHORT-NAME>ProvideRes1</SHORT-NAME>"
            "<GLOBAL-RESOURCE-ID>7</GLOBAL-RESOURCE-ID>"
            "<ITEMS>"
            "<BINARY-MANIFEST-ITEM><SHORT-NAME>Handle1</SHORT-NAME><IS-UNUSED>true</IS-UNUSED></BINARY-MANIFEST-ITEM>"
            "</ITEMS>"
            "<NUMBER-OF-NOTIFIER-SETS>4</NUMBER-OF-NOTIFIER-SETS>"
            "<SUPPORTS-MULTIPLE-NOTIFIER-SETS>true</SUPPORTS-MULTIPLE-NOTIFIER-SETS>"
            "</BINARY-MANIFEST-PROVIDE-RESOURCE>" % NS
        )

        provide_resource = BinaryManifestProvideResource(AUTOSAR.getInstance(), "ProvideRes1")
        parser.readBinaryManifestProvideResource(element, provide_resource)

        assert provide_resource.getShortName() == "ProvideRes1"
        assert provide_resource.getGlobalResourceId().getValue() == 7
        items = provide_resource.getItems()
        assert [item.getShortName() for item in items] == ["Handle1"]
        assert items[0].getIsUnused().getValue() is True
        assert provide_resource.getNumberOfNotifierSets().getValue() == 4
        assert provide_resource.getSupportsMultipleNotifierSets().getValue() is True

    def test_read_empty_element(self, parser):
        """
        An element without attribute content leaves the inherited item list empty and the
        optional attributes unset.
        """
        element = ET.fromstring("<BINARY-MANIFEST-PROVIDE-RESOURCE xmlns='%s'><SHORT-NAME>ProvideRes2</SHORT-NAME></BINARY-MANIFEST-PROVIDE-RESOURCE>" % NS)

        provide_resource = BinaryManifestProvideResource(AUTOSAR.getInstance(), "ProvideRes2")
        parser.readBinaryManifestProvideResource(element, provide_resource)

        assert provide_resource.getShortName() == "ProvideRes2"
        assert provide_resource.getGlobalResourceId() is None
        assert provide_resource.getItems() == []
        assert provide_resource.getNumberOfNotifierSets() is None
        assert provide_resource.getSupportsMultipleNotifierSets() is None
