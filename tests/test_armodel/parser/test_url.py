"""Reader tests for the XSD-only Url class."""

import xml.etree.ElementTree as ET

from armodel.parser.arxml_parser import ARXMLParser


class TestUrlParser:
    def test_get_url_reads_text_mime_type_and_ar_object_attributes(self):
        parser = ARXMLParser()
        element = ET.fromstring('<PARENT xmlns="http://autosar.org/schema/r4.0"><URL S="checksum" T="timestamp" MIME-TYPE="text/plain">https://example.com</URL></PARENT>')

        url = parser.getUrl(element, "URL")

        assert url.getValue().getValue() == "https://example.com"
        assert url.getMimeType().getValue() == "text/plain"
        assert url.getChecksum().getValue() == "checksum"
        assert url.getTimestamp().getValue() == "timestamp"

    def test_get_url_returns_empty_object_when_optional_content_is_absent(self):
        url = ARXMLParser().getUrl(ET.fromstring('<PARENT xmlns="http://autosar.org/schema/r4.0"/>'), "URL")

        assert url is None
