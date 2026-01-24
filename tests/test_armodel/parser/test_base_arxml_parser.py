"""Test BaseARXMLParser utility methods."""
import pytest
import xml.etree.ElementTree as ET
from armodel.parser.base_arxml_parser import BaseARXMLParser


class TestBaseARXMLParser:
    """Test BaseARXMLParser utility methods."""

    def test_read_collection_basic(self):
        """Test read_collection with handler map."""
        xml = """
        <PARENT xmlns="http://autosar.org/schema/r4.0">
            <ITEMS>
                <A><SHORT-NAME>Item1</SHORT-NAME></A>
                <B><SHORT-NAME>Item2</SHORT-NAME></B>
                <A><SHORT-NAME>Item3</SHORT-NAME></A>
            </ITEMS>
        </PARENT>
        """
        element = ET.fromstring(xml)
        parser = BaseARXMLParser()

        results = []
        handler_map = {
            'A': lambda e: results.append(('A', parser.getShortName(e))),
            'B': lambda e: results.append(('B', parser.getShortName(e))),
        }

        parser.read_collection(element, "ITEMS/*", handler_map)

        assert results == [('A', 'Item1'), ('B', 'Item2'), ('A', 'Item3')]

    def test_read_collection_unsupported_tag(self):
        """Test read_collection with unsupported tag raises error."""
        xml = """
        <PARENT xmlns="http://autosar.org/schema/r4.0">
            <ITEMS>
                <UNSUPPORTED><SHORT-NAME>Item1</SHORT-NAME></UNSUPPORTED>
            </ITEMS>
        </PARENT>
        """
        element = ET.fromstring(xml)
        parser = BaseARXMLParser(options={"warning": False})

        handler_map = {}

        with pytest.raises(NotImplementedError, match="Unsupported element"):
            parser.read_collection(element, "ITEMS/*", handler_map)

    def test_read_collection_with_warning_mode(self):
        """Test read_collection with warning mode logs error."""
        xml = """
        <PARENT xmlns="http://autosar.org/schema/r4.0">
            <ITEMS>
                <UNSUPPORTED><SHORT-NAME>Item1</SHORT-NAME></UNSUPPORTED>
            </ITEMS>
        </PARENT>
        """
        element = ET.fromstring(xml)
        parser = BaseARXMLParser(options={"warning": True})

        handler_map = {}

        # Should not raise, just log
        parser.read_collection(element, "ITEMS/*", handler_map)

    def test_read_optional_with_value(self):
        """Test read_optional when element exists."""
        xml = """
        <PARENT xmlns="http://autosar.org/schema/r4.0">
            <OPTIONAL-FIELD>Value123</OPTIONAL-FIELD>
        </PARENT>
        """
        element = ET.fromstring(xml)
        parser = BaseARXMLParser()

        reader = lambda e: e.text
        result = parser.read_optional(element, "OPTIONAL-FIELD", reader)

        assert result == "Value123"

    def test_read_optional_without_value(self):
        """Test read_optional when element doesn't exist."""
        xml = """
        <PARENT xmlns="http://autosar.org/schema/r4.0">
            <OTHER-FIELD>Value123</OTHER-FIELD>
        </PARENT>
        """
        element = ET.fromstring(xml)
        parser = BaseARXMLParser()

        reader = lambda e: e.text
        result = parser.read_optional(element, "OPTIONAL-FIELD", reader)

        assert result is None

    def test_inherits_from_abstract_parser(self):
        """Test BaseARXMLParser inherits from AbstractARXMLParser."""
        from armodel.parser.abstract_arxml_parser import AbstractARXMLParser

        parser = BaseARXMLParser()
        assert isinstance(parser, AbstractARXMLParser)
