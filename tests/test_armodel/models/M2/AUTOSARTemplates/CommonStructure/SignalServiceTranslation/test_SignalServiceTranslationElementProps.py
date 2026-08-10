"""
This module contains tests for the SignalServiceTranslationElementProps class in the
AUTOSAR CommonStructure.SignalServiceTranslation module.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Filter import DataFilter
from armodel.models.M2.AUTOSARTemplates.CommonStructure.SignalServiceTranslation import SignalServiceTranslationElementProps


class TestSignalServiceTranslationElementProps:
    """
    Test class for SignalServiceTranslationElementProps functionality.
    """

    def test_initialization(self):
        obj = SignalServiceTranslationElementProps(None, "Test")
        assert isinstance(obj, SignalServiceTranslationElementProps)
        assert obj.getElement() is None
        assert obj.getFilter() is None
        assert obj.getTransmissionTrigger() is None

    def test_set_element_placeholder(self):
        obj = SignalServiceTranslationElementProps(None, "Test")
        placeholder = object()
        assert obj.setElement(placeholder) is obj
        assert obj.getElement() is placeholder
        assert obj.setElement(None) is obj
        assert obj.getElement() is placeholder

    def test_set_filter(self):
        obj = SignalServiceTranslationElementProps(None, "Test")
        data_filter = DataFilter()
        assert obj.setFilter(data_filter) is obj
        assert obj.getFilter() is data_filter
        assert obj.setFilter(None) is obj
        assert obj.getFilter() is data_filter

    def test_set_transmission_trigger(self):
        obj = SignalServiceTranslationElementProps(None, "Test")
        trigger = True
        assert obj.setTransmissionTrigger(trigger) is obj
        assert obj.getTransmissionTrigger() is trigger
        assert obj.setTransmissionTrigger(None) is obj
        assert obj.getTransmissionTrigger() is trigger
