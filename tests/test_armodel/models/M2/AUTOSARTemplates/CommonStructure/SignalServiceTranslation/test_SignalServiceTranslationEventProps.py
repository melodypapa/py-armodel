"""
This module contains tests for the SignalServiceTranslationEventProps class in the
AUTOSAR CommonStructure.SignalServiceTranslation module.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.SignalServiceTranslation.SignalServiceTranslationEventProps import (
    SignalServiceTranslationEventProps,
)


class TestSignalServiceTranslationEventProps:
    """
    Test class for SignalServiceTranslationEventProps functionality.
    """

    def test_initialization(self):
        obj = SignalServiceTranslationEventProps()
        assert isinstance(obj, SignalServiceTranslationEventProps)
