"""
This module contains tests for the SignalServiceTranslationProps class in the
AUTOSAR CommonStructure.SignalServiceTranslation module.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.SignalServiceTranslation.SignalServiceTranslationProps import (
    SignalServiceTranslationProps,
)


class TestSignalServiceTranslationProps:
    """
    Test class for SignalServiceTranslationProps functionality.
    """

    def test_initialization(self):
        obj = SignalServiceTranslationProps()
        assert isinstance(obj, SignalServiceTranslationProps)
