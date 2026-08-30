"""
Tests for writing ARObject XML attributes (S checksum, T timestamp) — Table 6.1.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DateTime,
    String,
)
from armodel.writer.abstract_arxml_writer import AbstractARXMLWriter


class ConcreteARObject(ARObject):
    pass


def _make_writer():
    return AbstractARXMLWriter.__new__(AbstractARXMLWriter)


class TestWriteARObjectAttributes:
    def test_write_checksum_timestamp_uuid(self):
        writer = _make_writer()
        element = ET.Element("SHORT-NAME")

        obj = ConcreteARObject()
        checksum = String()
        checksum.setValue("checksum-1")
        timestamp = DateTime()
        timestamp.setValue("2009-07-23T13:38:00Z")
        obj.setChecksum(checksum)
        obj.setTimestamp(timestamp)
        obj.uuid = "uuid-1"

        writer.writeARObjectAttributes(element, obj)

        assert element.attrib["S"] == "checksum-1"
        assert element.attrib["T"] == "2009-07-23T13:38:00Z"
        assert element.attrib["UUID"] == "uuid-1"

    def test_write_attributes_absent(self):
        writer = _make_writer()
        element = ET.Element("SHORT-NAME")

        writer.writeARObjectAttributes(element, ConcreteARObject())

        assert "S" not in element.attrib
        assert "T" not in element.attrib
        assert "UUID" not in element.attrib

    def test_write_timestamp_only(self):
        writer = _make_writer()
        element = ET.Element("SHORT-NAME")

        obj = ConcreteARObject()
        timestamp = DateTime()
        timestamp.setValue("2009-07-23")
        obj.setTimestamp(timestamp)

        writer.writeARObjectAttributes(element, obj)

        assert element.attrib["T"] == "2009-07-23"
        assert "S" not in element.attrib
