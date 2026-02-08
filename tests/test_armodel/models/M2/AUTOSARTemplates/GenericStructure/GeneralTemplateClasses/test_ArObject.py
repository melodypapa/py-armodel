"""
This module contains comprehensive tests for the ArObject.py file
in the AUTOSAR GenericStructure module.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class TestARObject:
    """
    Test class for ARObject functionality.
    """

    def test_abstract_initialization(self):
        """
        Test that ARObject cannot be instantiated directly (abstract class).
        """
        try:
            obj = ARObject()
            assert False, "ARObject should not be instantiable"
        except TypeError as e:
            # The error message should indicate it's abstract
            assert "abstract class" in str(e) or "ARObject is an abstract class" in str(e)

    def test_concrete_implementation_initialization(self):
        """
        Test that a concrete implementation of ARObject can be instantiated and initializes properties correctly.
        """
        class ConcreteARObject(ARObject):
            def __init__(self):
                super().__init__()  # This should work since type(self) is not ARObject

        obj = ConcreteARObject()

        # Properties should be initialized to None (or appropriate defaults)
        assert obj.parent is None
        assert obj.checksum is None
        assert obj.timestamp is None
        assert obj.uuid is None

    def test_get_tag_name(self):
        """
        Test getTagName method functionality.
        """
        class ConcreteARObject(ARObject):
            def __init__(self):
                super().__init__()

        obj = ConcreteARObject()

        # Test with a tag that has a namespace
        tag_with_ns = "{http://www.example.com/ns}elementName"
        nsmap = {"xmlns": "http://www.example.com/ns"}

        result = obj.getTagName(tag_with_ns, nsmap)
        assert result == "elementName"

        # Test with different namespace
        tag_with_ns2 = "{http://another.com/schema}testTag"
        nsmap2 = {"xmlns": "http://another.com/schema"}

        result2 = obj.getTagName(tag_with_ns2, nsmap2)
        assert result2 == "testTag"

        # Test with tag that doesn't match namespace (should still work with replace)
        tag_with_ns3 = "{http://different.com/ns}otherTag"
        nsmap3 = {"xmlns": "http://different.com/ns"}

        result3 = obj.getTagName(tag_with_ns3, nsmap3)
        assert result3 == "otherTag"

        # Test with tag that has no namespace prefix (edge case)
        tag_no_ns = "simpleTag"
        result4 = obj.getTagName(tag_no_ns, nsmap)
        assert result4 == "simpleTag"
