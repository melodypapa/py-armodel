"""Tests for the Xdoc inline text element."""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, String, UriString
from armodel.models.M2.MSR.Documentation.BlockElements import Url
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import Xdoc
from armodel.models.M2.MSR.Documentation.TextModel.SingleLanguageData import SingleLanguageLongName


class TestXdoc:
    def test_xdoc_initialization(self):
        xdoc = Xdoc(None, "XDOC")

        assert xdoc.getDate() is None
        assert xdoc.getNumber() is None
        assert xdoc.getPosition() is None
        assert xdoc.getPublisher() is None
        assert xdoc.getState() is None
        assert xdoc.getUrl() is None
        assert xdoc.getLongName1() is None

    def test_xdoc_get_set_attributes(self):
        xdoc = Xdoc(None, "XDOC")
        date = DateTime().setValue("2026-09-12")
        number = String().setValue("DOC-1")
        position = String().setValue("section 1")
        publisher = String().setValue("Publisher")
        state = String().setValue("final")
        url = Url().setValue(UriString().setValue("https://example.com/doc"))

        assert xdoc.setDate(date) is xdoc
        assert xdoc.setNumber(number) is xdoc
        assert xdoc.setPosition(position) is xdoc
        assert xdoc.setPublisher(publisher) is xdoc
        assert xdoc.setState(state) is xdoc
        assert xdoc.setUrl(url) is xdoc
        assert xdoc.getDate() is date
        assert xdoc.getNumber() is number
        assert xdoc.getPosition() is position
        assert xdoc.getPublisher() is publisher
        assert xdoc.getState() is state
        assert xdoc.getUrl() is url

        assert xdoc.setDate(None) is xdoc
        assert xdoc.setNumber(None) is xdoc
        assert xdoc.setPosition(None) is xdoc
        assert xdoc.setPublisher(None) is xdoc
        assert xdoc.setState(None) is xdoc
        assert xdoc.setUrl(None) is xdoc
        assert xdoc.getDate() is date
        assert xdoc.getNumber() is number
        assert xdoc.getPosition() is position
        assert xdoc.getPublisher() is publisher
        assert xdoc.getState() is state
        assert xdoc.getUrl() is url

    def test_xdoc_inherited_long_name(self):
        xdoc = Xdoc(None, "XDOC")
        long_name = SingleLanguageLongName().setValue(String().setValue("Document"))

        assert xdoc.setLongName1(long_name) is xdoc
        assert xdoc.getLongName1() is long_name
