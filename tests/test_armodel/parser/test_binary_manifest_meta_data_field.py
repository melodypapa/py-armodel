"""
Reader tests for BinaryManifestMetaDataField (CP_TPS_SystemTemplate Table 11.28, p.923, R23-11).

The class is a nested non-top-level Identifiable (aggregated by the still-unsynced
CpSoftwareClusterBinaryManifestDescriptor.metaDataField), so the reusable helper
readBinaryManifestMetaDataField is exercised directly on a standalone XML subtree
(XSD complexType BINARY-MANIFEST-META-DATA-FIELD, AUTOSAR_00052.xsd l.8794:
AR-OBJECT + REFERRABLE + MULTILANGUAGE-REFERRABLE + IDENTIFIABLE groups and
attributeGroups — read via readIdentifiable; group members SIZE, VALUE).

Round-trip counterpart: tests/test_armodel/writer/test_binary_manifest_meta_data_field.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import BinaryManifestMetaDataField
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, VerbatimString

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring("<BINARY-MANIFEST-META-DATA-FIELD xmlns='%s'>%s</BINARY-MANIFEST-META-DATA-FIELD>" % (NS, inner))


class TestReadBinaryManifestMetaDataField:
    """Tests for readBinaryManifestMetaDataField — own group field values (Table 11.28)."""

    def _read(self, parser, inner):
        field = BinaryManifestMetaDataField(AUTOSAR.getInstance(), "Field1")
        parser.readBinaryManifestMetaDataField(_snip(inner), field)
        return field

    def test_read_sets_all_fields(self, parser):
        field = self._read(parser, "<SIZE>4096</SIZE><VALUE>CHECKSUM_TABLE_V1</VALUE>")

        assert isinstance(field.getSize(), PositiveInteger)
        assert field.getSize().getValue() == 4096
        assert isinstance(field.getValue(), VerbatimString)
        assert field.getValue().getValue() == "CHECKSUM_TABLE_V1"

    def test_read_partial_attributes(self, parser):
        field = self._read(parser, "<VALUE>CHECKSUM_TABLE_V1</VALUE>")

        assert field.getSize() is None
        assert field.getValue().getValue() == "CHECKSUM_TABLE_V1"

    def test_read_empty_element(self, parser):
        field = self._read(parser, "")

        assert field.getSize() is None
        assert field.getValue() is None

    def test_read_identifiable_level(self, parser):
        """Test that the IDENTIFIABLE attributeGroup (UUID attribute) is read via the base helper (SHORT-NAME is consumed by the aggregator that constructs the object)."""
        element = ET.fromstring("<BINARY-MANIFEST-META-DATA-FIELD xmlns='%s' UUID='1234-5678'/>" % NS)
        field = BinaryManifestMetaDataField(AUTOSAR.getInstance(), "Field1")
        parser.readBinaryManifestMetaDataField(element, field)

        assert field.getUuid() is not None
        assert field.getUuid().getValue() == "1234-5678"
