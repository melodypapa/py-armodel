
from ....parser.arxml_parser import ARXMLParser


class TestARXMLParser:
    def test_convert_find_key(self):
        parser = ARXMLParser()
        assert (parser.convert_find_key("ELEMENTS") == "xmlns:ELEMENTS")
        assert (parser.convert_find_key("ELEMENTS/*") == "xmlns:ELEMENTS/*")
        assert (parser.convert_find_key("./ELEMENTS") == "./xmlns:ELEMENTS")
        assert (parser.convert_find_key("./ELEMENTS/*") == "./xmlns:ELEMENTS/*")
        assert (parser.convert_find_key("A/B") == "xmlns:A/xmlns:B")
        assert (parser.convert_find_key("A/B/*") == "xmlns:A/xmlns:B/*")
        assert (parser.convert_find_key("./A/B") == "./xmlns:A/xmlns:B")
        assert (parser.convert_find_key("./A/B/*") == "./xmlns:A/xmlns:B/*")
