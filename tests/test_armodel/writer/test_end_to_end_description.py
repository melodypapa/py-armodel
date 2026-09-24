"""
Tests for writing END-TO-END-PROFILE elements — EndToEndDescription, Table 4.95 (p.206, R23-11).

EndToEndDescription (Base = ARObject) carries ten own attributes whose writer element
order must follow the XSD sequence (AUTOSAR_00052.xsd group END-TO-END-DESCRIPTION,
sequenceOffset): CATEGORY → DATA-IDS → DATA-ID-MODE → DATA-LENGTH → MAX-DELTA-COUNTER-INIT
→ CRC-OFFSET → COUNTER-OFFSET → MAX-NO-NEW-OR-REPEATED-DATA → SYNC-COUNTER-INIT →
DATA-ID-NIBBLE-OFFSET. The DATA-IDS wrapper is emitted only when non-empty. The
set-level round-trip goes through the EndToEndProtection aggregation (writeEndToEndProtection
dispatch → readEndToEndProtection dispatch).

Round-trip counterpart: tests/test_armodel/parser/test_end_to_end_description.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameToken, PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.EndToEndProtection import EndToEndDescription, EndToEndProtectionSet
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    """Create ARXML writer instance."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLWriter()


def _positive_int(value):
    numerical = PositiveInteger()
    numerical.setValue(value)
    return numerical


def _name_token(value):
    token = NameToken()
    token.setValue(value)
    return token


def _filled_description():
    desc = EndToEndDescription()
    desc.setCategory(_name_token("PROFILE1"))
    desc.addDataId(_positive_int("1"))
    desc.addDataId(_positive_int("2"))
    desc.setDataIdMode(_positive_int("1"))
    desc.setDataLength(_positive_int("120"))
    desc.setMaxDeltaCounterInit(_positive_int("2"))
    desc.setCrcOffset(_positive_int("0"))
    desc.setCounterOffset(_positive_int("8"))
    desc.setMaxNoNewOrRepeatedData(_positive_int("3"))
    desc.setSyncCounterInit(_positive_int("3"))
    desc.setDataIdNibbleOffset(_positive_int("4"))
    return desc


XSD_ELEMENT_ORDER = [
    "CATEGORY",
    "DATA-IDS",
    "DATA-ID-MODE",
    "DATA-LENGTH",
    "MAX-DELTA-COUNTER-INIT",
    "CRC-OFFSET",
    "COUNTER-OFFSET",
    "MAX-NO-NEW-OR-REPEATED-DATA",
    "SYNC-COUNTER-INIT",
    "DATA-ID-NIBBLE-OFFSET",
]


class TestSetEndToEndDescription:
    """Tests for setEndToEndDescription — own element field values (Table 4.95)."""

    def test_write_field_values(self, writer):
        """Test that all ten attribute elements are emitted with their values read through the getters."""
        parent = ET.Element("PARENT")

        writer.setEndToEndDescription(parent, "END-TO-END-PROFILE", _filled_description())

        profile = parent.find("END-TO-END-PROFILE")
        assert profile is not None
        assert profile.find("CATEGORY").text == "PROFILE1"
        data_ids = profile.findall("DATA-IDS/DATA-ID")
        assert [data_id.text for data_id in data_ids] == ["1", "2"]
        assert profile.find("DATA-ID-MODE").text == "1"
        assert profile.find("DATA-LENGTH").text == "120"
        assert profile.find("MAX-DELTA-COUNTER-INIT").text == "2"
        assert profile.find("CRC-OFFSET").text == "0"
        assert profile.find("COUNTER-OFFSET").text == "8"
        assert profile.find("MAX-NO-NEW-OR-REPEATED-DATA").text == "3"
        assert profile.find("SYNC-COUNTER-INIT").text == "3"
        assert profile.find("DATA-ID-NIBBLE-OFFSET").text == "4"

    def test_write_xsd_element_order(self, writer):
        """Test that the element order follows the XSD group sequenceOffset order."""
        parent = ET.Element("PARENT")

        writer.setEndToEndDescription(parent, "END-TO-END-PROFILE", _filled_description())

        profile = parent.find("END-TO-END-PROFILE")
        assert [elem.tag for elem in profile] == XSD_ELEMENT_ORDER

    def test_write_unset_description_emits_no_children(self, writer):
        """Test that a description without fields emits the wrapper only, with no DATA-IDS element."""
        parent = ET.Element("PARENT")

        writer.setEndToEndDescription(parent, "END-TO-END-PROFILE", EndToEndDescription())

        profile = parent.find("END-TO-END-PROFILE")
        assert profile is not None
        assert len(profile) == 0
        assert profile.find("DATA-IDS") is None

    def test_write_none_description(self, writer):
        """Test that a None description emits no wrapper element."""
        parent = ET.Element("PARENT")

        writer.setEndToEndDescription(parent, "END-TO-END-PROFILE", None)

        assert len(parent) == 0


class TestEndToEndDescriptionRoundTrip:
    """Round-trip through the EndToEndProtection aggregation (write → read → assert)."""

    def test_round_trip_field_values(self, writer):
        """Test that all ten field values survive the write/read cycle through the protection dispatch."""
        protection_set = EndToEndProtectionSet(AUTOSAR.getInstance(), "Set")
        protection = protection_set.createEndToEndProtection("e2e")
        protection.setEndToEndProfile(_filled_description())

        parent = ET.Element("PARENT")
        writer.writeEndToEndProtection(parent, protection)
        protection_element = parent.find("END-TO-END-PROTECTION")

        xml_text = ET.tostring(protection_element, encoding="unicode")
        reloaded_element = ET.fromstring(xml_text.replace("END-TO-END-PROTECTION", "END-TO-END-PROTECTION xmlns='http://autosar.org/schema/r4.0'", 1))

        reloaded_set = EndToEndProtectionSet(AUTOSAR.getInstance(), "Set")
        ARXMLParser().readEndToEndProtection(reloaded_element, reloaded_set)
        reloaded = reloaded_set.getEndToEndProtections()[0].getEndToEndProfile()
        assert reloaded is not None
        assert reloaded.getCategory().getValue() == "PROFILE1"
        assert [data_id.getValue() for data_id in reloaded.getDataIds()] == [1, 2]
        assert reloaded.getDataIdMode().getValue() == 1
        assert reloaded.getDataLength().getValue() == 120
        assert reloaded.getMaxDeltaCounterInit().getValue() == 2
        assert reloaded.getCrcOffset().getValue() == 0
        assert reloaded.getCounterOffset().getValue() == 8
        assert reloaded.getMaxNoNewOrRepeatedData().getValue() == 3
        assert reloaded.getSyncCounterInit().getValue() == 3
        assert reloaded.getDataIdNibbleOffset().getValue() == 4

    def test_round_trip_ar_object_attributes(self, writer):
        """Test that the ARObject base attributes (S checksum, T timestamp) survive the write/read cycle."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, String

        desc = EndToEndDescription()
        checksum = String()
        checksum.setValue("abc123")
        desc.setChecksum(checksum)
        timestamp = DateTime()
        timestamp.setValue("2024-01-01T12:00:00+00:00")
        desc.setTimestamp(timestamp)

        parent = ET.Element("PARENT")
        writer.setEndToEndDescription(parent, "END-TO-END-PROFILE", desc)
        profile = parent.find("END-TO-END-PROFILE")
        assert profile.attrib.get("S") is not None
        assert profile.attrib.get("T") is not None

        xml_text = ET.tostring(profile, encoding="unicode")
        reloaded_element = ET.fromstring(xml_text.replace("END-TO-END-PROFILE", "END-TO-END-PROFILE xmlns='http://autosar.org/schema/r4.0'", 1))
        reloaded = EndToEndDescription()
        ARXMLParser().readARObject(reloaded_element, reloaded)
        assert reloaded.getChecksum() is not None
        assert reloaded.getChecksum().getValue() == "abc123"
        assert reloaded.getTimestamp() is not None
