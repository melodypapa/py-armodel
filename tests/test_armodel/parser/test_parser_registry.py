"""Test parser registry routing."""
import pytest
from armodel.parser.arxml_parser import ARXMLParser


class TestParserRegistry:
    """Test parser registry routes elements to correct parsers."""

    def test_registry_initialized(self):
        """Test that parser registry is initialized."""
        parser = ARXMLParser()
        assert hasattr(parser, '_parser_registry')
        assert isinstance(parser._parser_registry, dict)

    def test_registry_has_common_elements(self):
        """Test registry contains common structure elements."""
        parser = ARXMLParser()
        # Add some expected mappings
        # This will be populated as we migrate methods
        pass

    def test_get_parser_for_element(self):
        """Test getting parser instance for element tag."""
        parser = ARXMLParser()
        # This method will be implemented in Step 3
        # parser_instance = parser._get_parser_for_tag('APPLICATION-SW-COMPONENT-TYPE')
        # assert parser_instance is parser._component_parser
        pass
