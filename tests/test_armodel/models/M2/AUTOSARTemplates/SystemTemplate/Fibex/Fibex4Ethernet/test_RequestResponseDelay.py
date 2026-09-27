import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import RequestResponseDelay

CLASS_NOTE = """Time to wait before answering the query."""


class TestRequestResponseDelay:
    """Test cases for RequestResponseDelay (Table 6.171, p.515)."""

    def test_initialization_defaults(self):
        obj = RequestResponseDelay()
        assert obj.getMaxValue() is None
        assert obj.getMinValue() is None

    def test_setters_round_trip_and_none_noop(self):
        obj = RequestResponseDelay()
        item = TimeValue()
        assert obj.setMaxValue(item) is obj
        assert obj.getMaxValue() is item
        obj.setMaxValue(None)
        assert obj.getMaxValue() is item
        item = TimeValue()
        assert obj.setMinValue(item) is obj
        assert obj.getMinValue() is item
        obj.setMinValue(None)
        assert obj.getMinValue() is item

    def test_class_docstring_note(self):
        assert inspect.cleandoc(RequestResponseDelay.__doc__).split("\n\n")[0] == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        obj = RequestResponseDelay()
        assert inspect.cleandoc(obj.getMaxValue.__doc__) == "Maximum allowable response delay to entries received by multicast in seconds."
        assert inspect.cleandoc(obj.setMaxValue.__doc__).split("\n")[0] == "Maximum allowable response delay to entries received by multicast in seconds."
        assert inspect.cleandoc(obj.getMinValue.__doc__) == "Minimum allowable response delay to entries received by multicast in seconds."
        assert inspect.cleandoc(obj.setMinValue.__doc__).split("\n")[0] == "Minimum allowable response delay to entries received by multicast in seconds."
