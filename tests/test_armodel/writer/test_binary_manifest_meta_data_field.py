"""
Writer tests for BINARY-MANIFEST-META-DATA-FIELD elements — BinaryManifestMetaDataField,
Table 11.28 (p.923, R23-11).

writeBinaryManifestMetaDataField emits <BINARY-MANIFEST-META-DATA-FIELD> with the
IDENTIFIABLE level (SHORT-NAME, UUID — writeIdentifiable) and the group members
SIZE, VALUE in XSD sequenceOffset order (AUTOSAR_00052.xsd l.8794).

Round-trip counterpart: tests/test_armodel/parser/test_binary_manifest_meta_data_field.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import BinaryManifestMetaDataField
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, VerbatimString
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _new_field() -> BinaryManifestMetaDataField:
    field = BinaryManifestMetaDataField(AUTOSAR.getInstance(), "Field1")
    field.setSize(PositiveInteger().setValue("4096"))
    field.setValue(VerbatimString().setValue("CHECKSUM_TABLE_V1"))
    return field


class TestWriteBinaryManifestMetaDataField:
    def test_write_emits_element_short_name_and_members(self):
        """Test that the writer emits the element with SHORT-NAME and both members in XSD order."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeBinaryManifestMetaDataField(parent, _new_field())
        node = parent.find("BINARY-MANIFEST-META-DATA-FIELD")
        assert node is not None
        children = [child.tag for child in node]
        assert children[0] == "SHORT-NAME"
        assert node.find("SHORT-NAME").text == "Field1"
        assert children.index("SIZE") < children.index("VALUE")
        assert node.find("SIZE").text == "4096"
        assert node.find("VALUE").text == "CHECKSUM_TABLE_V1"

    def test_write_partial_omits_absent_elements(self):
        field = BinaryManifestMetaDataField(AUTOSAR.getInstance(), "Field1")
        field.setValue(VerbatimString().setValue("CHECKSUM_TABLE_V1"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeBinaryManifestMetaDataField(parent, field)
        node = parent.find("BINARY-MANIFEST-META-DATA-FIELD")

        assert node.find("SIZE") is None
        assert node.find("VALUE").text == "CHECKSUM_TABLE_V1"

    def test_write_empty_emits_identifiable_level_only(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeBinaryManifestMetaDataField(parent, BinaryManifestMetaDataField(AUTOSAR.getInstance(), "Empty"))
        node = parent.find("BINARY-MANIFEST-META-DATA-FIELD")

        assert node.find("SHORT-NAME").text == "Empty"
        assert node.find("SIZE") is None
        assert node.find("VALUE") is None

    def test_round_trip_preserves_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeBinaryManifestMetaDataField(parent, _new_field())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reloaded = BinaryManifestMetaDataField(AUTOSAR.getInstance(), "Field1")
        ARXMLParser().readBinaryManifestMetaDataField(root.find("{%s}BINARY-MANIFEST-META-DATA-FIELD" % NS), reloaded)
        assert reloaded.getShortName() == "Field1"
        assert reloaded.getSize().getValue() == 4096
        assert reloaded.getValue().getValue() == "CHECKSUM_TABLE_V1"
