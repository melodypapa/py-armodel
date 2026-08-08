"""
This module contains tests for the CryptoKeySlotContent class in the
AUTOSAR AdaptivePlatform.PlatformModuleDeployment.CryptoDeployment module.
"""

from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.CryptoDeployment.CryptoKeySlotContent import (
    CryptoKeySlotContent,
)
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR


class TestCryptoKeySlotContent:
    """
    Test class for CryptoKeySlotContent functionality.
    """

    def test_initialization(self):
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        obj = CryptoKeySlotContent(ar_root, "TestCryptoKeySlotContent")
        assert obj.getShortName() == "TestCryptoKeySlotContent"
        assert obj.getParent() == ar_root
