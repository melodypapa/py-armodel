"""
This module contains tests for the SignalServiceTranslationControlEnum class in the
AUTOSAR CommonStructure.SignalServiceTranslation module.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.SignalServiceTranslation import SignalServiceTranslationControlEnum


class TestSignalServiceTranslationControlEnum:
    """
    Test class for SignalServiceTranslationControlEnum functionality.
    """

    def test_literals_and_values(self):
        assert SignalServiceTranslationControlEnum.ALL_PARTIAL_NETWORKS_ACTIVE == "allPartialNetworksActive"
        assert SignalServiceTranslationControlEnum.ANY_PARTIAL_NETWORK_ACTIVE == "anyPartialNetworkActive"
        assert SignalServiceTranslationControlEnum.PARTIAL_NETWORK == "partialNetwork"
        assert SignalServiceTranslationControlEnum.SERVICE_DISCOVERY == "serviceDiscovery"
        assert SignalServiceTranslationControlEnum.TRANSLATION_START == "translationStart"

    def test_initialization(self):
        enum_obj = SignalServiceTranslationControlEnum()
        assert isinstance(enum_obj, SignalServiceTranslationControlEnum)
