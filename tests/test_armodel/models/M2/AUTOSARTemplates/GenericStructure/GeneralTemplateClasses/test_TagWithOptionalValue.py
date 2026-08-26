"""
This module contains tests for the TagWithOptionalValue class in the
AUTOSAR GenericStructure module (AUTOSAR_CP_TPS_SystemTemplate, Table 6.159).
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, String
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.TagWithOptionalValue import (
    TagWithOptionalValue,
)


class TestTagWithOptionalValue:
    """
    Test class for TagWithOptionalValue functionality.
    """

    def test_initialization(self):
        obj = TagWithOptionalValue()
        assert obj.getKey() is None
        assert obj.getSequenceOffset() is None
        assert obj.getValue() is None

    def test_get_set_key(self):
        obj = TagWithOptionalValue()

        assert obj.setKey(None) is obj
        assert obj.getKey() is None

        key = String().setValue("passreq")
        assert obj.setKey(key) is obj
        assert obj.getKey() is key

        obj.setKey(None)
        assert obj.getKey() is key

    def test_get_set_sequence_offset(self):
        obj = TagWithOptionalValue()

        assert obj.setSequenceOffset(None) is obj
        assert obj.getSequenceOffset() is None

        offset = Integer().setValue("4")
        assert obj.setSequenceOffset(offset) is obj
        assert obj.getSequenceOffset() is offset

        obj.setSequenceOffset(None)
        assert obj.getSequenceOffset() is offset

    def test_get_set_value(self):
        obj = TagWithOptionalValue()

        assert obj.setValue(None) is obj
        assert obj.getValue() is None

        value = String().setValue("JPEG,MPEG2")
        assert obj.setValue(value) is obj
        assert obj.getValue() is value

        obj.setValue(None)
        assert obj.getValue() is value
