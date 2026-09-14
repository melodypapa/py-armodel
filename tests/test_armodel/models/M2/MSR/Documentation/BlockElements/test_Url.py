"""Tests for the XSD-only Url model class."""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import MimeTypeString, UriString
from armodel.models.M2.MSR.Documentation.BlockElements import Url


class TestUrl:
    def test_url_initialization(self):
        url = Url()

        assert url.value is None
        assert url.mimeType is None

    def test_url_value_get_set_and_none_noop(self):
        url = Url()
        value = UriString().setValue("https://example.com/resource")

        assert url.getValue() is None
        assert url.setValue(value) is url
        assert url.getValue() is value
        assert url.setValue(None) is url
        assert url.getValue() is value

    def test_url_mime_type_get_set_and_none_noop(self):
        url = Url()
        mime_type = MimeTypeString().setValue("application/xml")

        assert url.getMimeType() is None
        assert url.setMimeType(mime_type) is url
        assert url.getMimeType() is mime_type
        assert url.setMimeType(None) is url
        assert url.getMimeType() is mime_type
