import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String, UriString
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    HttpTp,
    RequestMethodEnum,
    TcpTp,
)

CLASS_NOTE = "Http over TCP as transport protocol."


class TestHttpTp:
    """Test cases for HttpTp (Table 6.132, p.461)."""

    def _obj(self):
        return HttpTp()

    def test_initialization_defaults(self):
        obj = self._obj()
        assert obj.getContentType() is None
        assert obj.getProtocolVersion() is None
        assert obj.getRequestMethod() is None
        assert obj.getTcpTpConfig() is None
        assert obj.getUri() is None

    def test_get_set_content_type(self):
        obj = self._obj()
        value = String().setValue("application/json")
        assert obj.setContentType(value) is obj
        assert obj.getContentType() is value
        assert obj.getContentType().getValue() == "application/json"
        obj.setContentType(None)
        assert obj.getContentType() is value

    def test_get_set_protocol_version(self):
        obj = self._obj()
        value = String().setValue("1.1")
        assert obj.setProtocolVersion(value) is obj
        assert obj.getProtocolVersion() is value
        assert obj.getProtocolVersion().getValue() == "1.1"
        obj.setProtocolVersion(None)
        assert obj.getProtocolVersion() is value

    def test_get_set_request_method(self):
        obj = self._obj()
        value = RequestMethodEnum().setValue(RequestMethodEnum.GET)
        assert obj.setRequestMethod(value) is obj
        assert obj.getRequestMethod() is value
        assert obj.getRequestMethod().getValue() == RequestMethodEnum.GET
        obj.setRequestMethod(None)
        assert obj.getRequestMethod() is value

    def test_get_set_tcp_tp_config(self):
        obj = self._obj()
        value = TcpTp()
        assert obj.setTcpTpConfig(value) is obj
        assert obj.getTcpTpConfig() is value
        obj.setTcpTpConfig(None)
        assert obj.getTcpTpConfig() is value

    def test_get_set_uri(self):
        obj = self._obj()
        value = UriString().setValue("http://example.com/service")
        assert obj.setUri(value) is obj
        assert obj.getUri() is value
        assert obj.getUri().getValue() == "http://example.com/service"
        obj.setUri(None)
        assert obj.getUri() is value

    def test_class_docstring_note(self):
        assert inspect.cleandoc(HttpTp.__doc__) == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        obj = self._obj()
        assert inspect.cleandoc(obj.getContentType.__doc__) == "Descriptor for the transported content."
        assert inspect.cleandoc(obj.setContentType.__doc__).split("\n")[0] == "Descriptor for the transported content."
        assert inspect.cleandoc(obj.getProtocolVersion.__doc__) == "HTTP Protocol version (e.g. 1.1)"
        assert inspect.cleandoc(obj.setProtocolVersion.__doc__).split("\n")[0] == "HTTP Protocol version (e.g. 1.1)"
        assert inspect.cleandoc(obj.getRequestMethod.__doc__) == "HTTP request method to be used."
        assert inspect.cleandoc(obj.setRequestMethod.__doc__).split("\n")[0] == "HTTP request method to be used."
        assert inspect.cleandoc(obj.getTcpTpConfig.__doc__) == "TcpTp Configuration."
        assert inspect.cleandoc(obj.setTcpTpConfig.__doc__).split("\n")[0] == "TcpTp Configuration."
        assert inspect.cleandoc(obj.getUri.__doc__) == "URI to be called."
        assert inspect.cleandoc(obj.setUri.__doc__).split("\n")[0] == "URI to be called."
