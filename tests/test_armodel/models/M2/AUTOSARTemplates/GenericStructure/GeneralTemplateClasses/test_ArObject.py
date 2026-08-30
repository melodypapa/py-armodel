"""
Tests for the ARObject class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 6.1).
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DateTime,
    String,
)


class ConcreteARObject(ARObject):
    pass


class TestARObject:
    def test_abstract_initialization(self):
        """
        ARObject is abstract and cannot be instantiated directly.
        """
        with pytest.raises(TypeError):
            ARObject()

    def test_initialization(self):
        """
        A concrete ARObject initializes all members to None.
        """
        obj = ConcreteARObject()

        assert obj.getChecksum() is None
        assert obj.getTimestamp() is None
        assert obj.parent is None
        assert obj.uuid is None

    def test_get_set_checksum(self):
        """
        Round-trips the checksum member; None is a no-op.
        """
        obj = ConcreteARObject()

        value = String()
        value.setValue("abc123")
        obj.setChecksum(value)
        assert obj.getChecksum() is value

        obj.setChecksum(None)
        assert obj.getChecksum() is value

    def test_get_set_timestamp(self):
        """
        Round-trips the timestamp member; None is a no-op.
        """
        obj = ConcreteARObject()

        value = DateTime()
        value.setValue("2009-07-23T13:38:00Z")
        obj.setTimestamp(value)
        assert obj.getTimestamp() is value

        obj.setTimestamp(None)
        assert obj.getTimestamp() is value

    def test_get_tag_name(self):
        """
        getTagName strips the namespace prefix from a tag name.
        """
        obj = ConcreteARObject()

        nsmap = {"xmlns": "http://www.example.com/ns"}
        assert obj.getTagName("{http://www.example.com/ns}elementName", nsmap) == "elementName"
        assert obj.getTagName("simpleTag", nsmap) == "simpleTag"
