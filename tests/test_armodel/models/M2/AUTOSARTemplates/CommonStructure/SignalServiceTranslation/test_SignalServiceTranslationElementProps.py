"""
This module contains tests for the SignalServiceTranslationElementProps class in the
AUTOSAR CommonStructure.SignalServiceTranslation module.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.SignalServiceTranslation.SignalServiceTranslationElementProps import (
    SignalServiceTranslationElementProps,
)


class TestSignalServiceTranslationElementProps:
    """
    Test class for SignalServiceTranslationElementProps functionality.
    """

    def test_initialization(self):
        obj = SignalServiceTranslationElementProps()
        assert isinstance(obj, SignalServiceTranslationElementProps)
