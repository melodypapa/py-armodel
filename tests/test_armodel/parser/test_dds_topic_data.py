"""
Tests for reading DDS-TOPIC-DATA elements — DdsTopicData, Table 6.180 (p.529, R23-11).

The class is a nested non-top-level element (aggregated by DdsCpQosProfile.topicData as the
<TOPIC-DATA> element), so the reusable helper readDdsTopicData is exercised directly on a
standalone XML subtree (XSD complexType DDS-TOPIC-DATA, AUTOSAR_00052.xsd l.30691:
AR-OBJECT group + attributeGroup — S/T round-trip; group member TOPIC-DATA typed AR:STRING).
Note the nested same-name shape: the object element <TOPIC-DATA> carries the string member
<TOPIC-DATA> inside.

Round-trip counterpart: tests/test_armodel/writer/test_writer_dds_topic_data.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DdsTopicData

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<TOPIC-DATA xmlns='{NS}'>{inner}</TOPIC-DATA>")


class TestReadDdsTopicData:
    """Tests for readDdsTopicData — own group field values (Table 6.180)."""

    def _read(self, parser, inner):
        topic_data = DdsTopicData()
        parser.readDdsTopicData(_snip(inner), topic_data)
        return topic_data

    def test_read_sets_topic_data(self, parser):
        """Test that the nested TOPIC-DATA string member is read with its value."""
        topic_data = self._read(parser, "<TOPIC-DATA>raw topic payload</TOPIC-DATA>")
        assert topic_data.getTopicData() is not None
        assert topic_data.getTopicData().getValue() == "raw topic payload"

    def test_read_empty(self, parser):
        """Test that an absent member leaves the field None."""
        topic_data = self._read(parser, "")
        assert topic_data.getTopicData() is None

    def test_read_ar_object_attributes(self, parser):
        """Test that the AR-OBJECT attributeGroup (S/T) is read via the base helper."""
        element = ET.fromstring("<TOPIC-DATA xmlns='%s' S='5' T='2025-04-04T00:00:00Z'><TOPIC-DATA>payload</TOPIC-DATA></TOPIC-DATA>" % NS)
        topic_data = DdsTopicData()
        parser.readDdsTopicData(element, topic_data)
        assert topic_data.getChecksum() is not None
        assert topic_data.getChecksum().getValue() == "5"
        assert topic_data.getTimestamp() is not None
        assert topic_data.getTimestamp().getValue() == "2025-04-04T00:00:00Z"
        assert topic_data.getTopicData().getValue() == "payload"
