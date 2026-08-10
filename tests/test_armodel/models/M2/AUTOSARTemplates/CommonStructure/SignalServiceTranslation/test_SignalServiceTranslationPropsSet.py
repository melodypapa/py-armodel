"""
This module contains tests for the SignalServiceTranslationPropsSet class in the
AUTOSAR CommonStructure.SignalServiceTranslation module.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.SignalServiceTranslation import (
    SignalServiceTranslationProps,
    SignalServiceTranslationPropsSet,
)


class TestSignalServiceTranslationPropsSet:
    """
    Test class for SignalServiceTranslationPropsSet functionality.
    """

    def test_initialization(self):
        obj = SignalServiceTranslationPropsSet(None, "Test")
        assert isinstance(obj, SignalServiceTranslationPropsSet)
        assert obj.getSignalServiceTranslationProps() == []

    def test_create_signal_service_translation_props(self):
        obj = SignalServiceTranslationPropsSet(None, "Test")
        child = obj.createSignalServiceTranslationProps("Props1")
        assert isinstance(child, SignalServiceTranslationProps)
        assert child.getParent() is obj
        assert obj.getSignalServiceTranslationProps() == [child]
