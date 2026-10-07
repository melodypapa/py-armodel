import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import RequestMethodEnum

CLASS_NOTE = "Available request methods for HTTPs."
XSD_FACETS = ["CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "POST", "PUT", "TRACE"]


class TestRequestMethodEnum:
    """Test cases for RequestMethodEnum (XSD-only enum; AUTOSAR_00052.xsd REQUEST-METHOD-ENUM--SIMPLE)."""

    def test_member_presence_and_values(self):
        assert RequestMethodEnum.CONNECT == "CONNECT"
        assert RequestMethodEnum.DELETE == "DELETE"
        assert RequestMethodEnum.GET == "GET"
        assert RequestMethodEnum.HEAD == "HEAD"
        assert RequestMethodEnum.OPTIONS == "OPTIONS"
        assert RequestMethodEnum.POST == "POST"
        assert RequestMethodEnum.PUT == "PUT"
        assert RequestMethodEnum.TRACE == "TRACE"
        assert list(RequestMethodEnum().getEnumValues()) == XSD_FACETS

    def test_instantiability(self):
        enum = RequestMethodEnum()
        assert enum == enum.setValue(RequestMethodEnum.POST)
        assert enum.getValue() == RequestMethodEnum.POST

    def test_class_docstring_note(self):
        assert inspect.cleandoc(RequestMethodEnum.__doc__) == CLASS_NOTE
