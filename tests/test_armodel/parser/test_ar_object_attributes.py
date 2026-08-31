"""
Tests for reading ARObject XML attributes (S checksum, T timestamp) — Table 6.1.
The uuid attribute (Table 4.4) is owned by Identifiable and is read inside
readIdentifiable (together with the UUID-manager registration — see the
ordering trap in docs/plan/sync-todo/Group1.md "uuid move work order"), so the
uuid cases below exercise readIdentifiable on a concrete Identifiable subclass.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.parser.arxml_parser import ARXMLParser


class ConcreteARObject(ARObject):
    pass


class ConcreteIdentifiable(Identifiable):
    def __init__(self):
        AUTOSAR.getInstance().new()
        parent = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        super().__init__(parent, "TestIdentifiable")


class TestReadARObjectAttributes:
    def test_read_checksum_timestamp(self):
        parser = ARXMLParser(options={"warning": True})
        element = ET.Element("SHORT-NAME", {"S": "checksum-1", "T": "2009-07-23T13:38:00Z", "UUID": "uuid-1"})

        obj = ConcreteARObject()
        parser.readARObject(element, obj)

        assert obj.getChecksum() is not None
        assert obj.getChecksum().getValue() == "checksum-1"
        assert obj.getTimestamp() is not None
        assert obj.getTimestamp().getValue() == "2009-07-23T13:38:00Z"

    def test_read_uuid_on_identifiable(self):
        parser = ARXMLParser(options={"warning": True})
        element = ET.Element("SHORT-NAME", {"UUID": "uuid-1"})

        obj = ConcreteIdentifiable()
        parser.readIdentifiable(element, obj)

        assert obj.getUuid() == "uuid-1"

    def test_read_attributes_absent(self):
        parser = ARXMLParser(options={"warning": True})
        element = ET.Element("SHORT-NAME")

        obj = ConcreteARObject()
        parser.readARObject(element, obj)

        assert obj.getChecksum() is None
        assert obj.getTimestamp() is None

    def test_read_uuid_absent_on_identifiable(self):
        parser = ARXMLParser(options={"warning": True})
        element = ET.Element("SHORT-NAME")

        obj = ConcreteIdentifiable()
        parser.readIdentifiable(element, obj)

        assert obj.getUuid() is None

    def test_read_checksum_only(self):
        parser = ARXMLParser(options={"warning": True})
        element = ET.Element("SHORT-NAME", {"S": "only-checksum"})

        obj = ConcreteARObject()
        parser.readARObject(element, obj)

        assert obj.getChecksum().getValue() == "only-checksum"
        assert obj.getTimestamp() is None
