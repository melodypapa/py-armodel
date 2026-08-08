"""
This module contains tests for the SignalServiceTranslationControlEnum class in the
AUTOSAR CommonStructure.SignalServiceTranslation module.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.SignalServiceTranslation.SignalServiceTranslationControlEnum import (
    SignalServiceTranslationControlEnum,
)


class TestSignalServiceTranslationControlEnum:
    """
    Test class for SignalServiceTranslationControlEnum functionality.
    """

    def test_members(self):
        assert SignalServiceTranslationControlEnum.ENUM_AUTOMATIC.value == "automatic"
        assert SignalServiceTranslationControlEnum.ENUM_MANUAL.value == "manual"
