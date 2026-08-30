"""
Tests for reading ARObject XML attributes (S checksum, T timestamp) — Table 6.1.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.parser.arxml_parser import ARXMLParser


class ConcreteARObject(ARObject):
    pass


class TestReadARObjectAttributes:
    def test_read_checksum_timestamp_uuid(self):
        parser = ARXMLParser(options={"warning": True})
        element = ET.Element("SHORT-NAME", {"S": "checksum-1", "T": "2009-07-23T13:38:00Z", "UUID": "uuid-1"})

        obj = ConcreteARObject()
        parser.readARObjectAttributes(element, obj)

        assert obj.getChecksum() is not None
        assert obj.getChecksum().getValue() == "checksum-1"
        assert obj.getTimestamp() is not None
        assert obj.getTimestamp().getValue() == "2009-07-23T13:38:00Z"
        assert obj.uuid == "uuid-1"

    def test_read_attributes_absent(self):
        parser = ARXMLParser(options={"warning": True})
        element = ET.Element("SHORT-NAME")

        obj = ConcreteARObject()
        parser.readARObjectAttributes(element, obj)

        assert obj.getChecksum() is None
        assert obj.getTimestamp() is None
        assert obj.uuid is None

    def test_read_checksum_only(self):
        parser = ARXMLParser(options={"warning": True})
        element = ET.Element("SHORT-NAME", {"S": "only-checksum"})

        obj = ConcreteARObject()
        parser.readARObjectAttributes(element, obj)

        assert obj.getChecksum().getValue() == "only-checksum"
        assert obj.getTimestamp() is None
