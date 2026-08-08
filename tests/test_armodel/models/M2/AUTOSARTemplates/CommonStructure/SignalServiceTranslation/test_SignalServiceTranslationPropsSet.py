"""
This module contains tests for the SignalServiceTranslationPropsSet class in the
AUTOSAR CommonStructure.SignalServiceTranslation module.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.SignalServiceTranslation.SignalServiceTranslationPropsSet import (
    SignalServiceTranslationPropsSet,
)


class TestSignalServiceTranslationPropsSet:
    """
    Test class for SignalServiceTranslationPropsSet functionality.
    """

    def test_initialization(self):
        obj = SignalServiceTranslationPropsSet()
        assert isinstance(obj, SignalServiceTranslationPropsSet)
