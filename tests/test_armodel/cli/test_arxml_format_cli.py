import pytest
import tempfile
import os

from armodel.writer.arxml_writer import ARXMLWriter
from armodel.parser.arxml_parser import ARXMLParser
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR


class TestArxmlFormatCli:
    """Test the arxml-format CLI functionality for --unescape-entities parameter"""

    def test_unescape_entities_flag_default_disabled(self):
        """Test that without --unescape-entities option, entities in attributes remain escaped"""
        # The XML parser unescapes during parsing, but minidom re-escapes quotes in attributes
        # Test verifies that the patch_xml doesn't unescape them when flag is False
        writer = ARXMLWriter(options={'unescape_entities': False})
        xml_input = '<ELEMENT ATTR="test&quot;value"/>'
        result = writer.patch_xml(xml_input)
        # Without flag, quote entities in attributes should remain escaped
        assert '&quot;' in result

    def test_unescape_entities_in_attributes(self):
        """Test that unescape_entities unescapes quotes in attribute values"""
        # Minodm keeps quotes escaped in attributes, patch_xml should unescape them when flag is True
        writer = ARXMLWriter(options={'unescape_entities': True})
        xml_input = '<ELEMENT ATTR="test&quot;value&quot;"/>'
        result = writer.patch_xml(xml_input)
        # With flag, quote entities in attributes should be unescaped
        assert 'ATTR="test"value"' in result
        assert '&quot;' not in result

    def test_unescape_entities_flag_enabled(self):
        """Test that with unescape_entities option, entities are unescaped"""
        writer = ARXMLWriter(options={'unescape_entities': True})
        xml_input = '<ELEMENT ATTR="test&quot;value&apos;123&apos;end"/>'
        result = writer.patch_xml(xml_input)
        # With flag, both quote types should be unescaped
        assert 'ATTR="test"value\'123\'end"' in result
        assert '&quot;' not in result
        assert '&apos;' not in result

    def test_unescape_entities_both_types(self):
        """Test that both quote entity types are unescaped correctly"""
        writer = ARXMLWriter(options={'unescape_entities': True})
        xml_input = '<ELEMENT NAME="Test&quot;Both&apos;Quotes&quot;"/>'
        result = writer.patch_xml(xml_input)
        # Both quote types should be unescaped
        assert 'NAME="Test"Both\'Quotes"' in result
        assert '&quot;' not in result
        assert '&apos;' not in result

    def test_unescape_entities_with_warning_mode(self):
        """Test that unescape_entities works with warning mode"""
        writer = ARXMLWriter(options={'unescape_entities': True, 'warning': True})
        xml_input = '<ELEMENT ATTR="test&quot;value"/>'
        result = writer.patch_xml(xml_input)
        # Should unescape even with warning mode enabled
        assert 'ATTR="test"value"' in result
        assert '&quot;' not in result
