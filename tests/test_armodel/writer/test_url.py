"""Writer tests for the XSD-only Url class."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import MimeTypeString, UriString
from armodel.models.M2.MSR.Documentation.BlockElements import Url
from armodel.writer.arxml_writer import ARXMLWriter


class TestUrlWriter:
    def test_set_url_writes_text_mime_type_and_ar_object_attributes(self):
        url = Url()
        url.setValue(UriString().setValue("https://example.com"))
        url.setMimeType(MimeTypeString().setValue("text/plain"))

        checksum = url.getChecksum()
        assert checksum is None

        element = ET.Element("PARENT")
        ARXMLWriter().setUrl(element, "URL", url)

        written = element.find("URL")
        assert written is not None
        assert written.text == "https://example.com"
        assert written.attrib["MIME-TYPE"] == "text/plain"

    def test_set_url_omits_none(self):
        element = ET.Element("PARENT")

        ARXMLWriter().setUrl(element, "URL", None)

        assert element.find("URL") is None
