"""
This module contains tests for the CryptoKeyManagementNeeds class
in the AUTOSAR CommonStructure ServiceNeeds module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    CryptoKeyManagementNeeds,
    ServiceNeeds,
)

SPEC_NOTE = "This meta-class can be used to indicate a service use case for key management."


class TestCryptoKeyManagementNeeds:
    def test_initialization(self):
        """Test that the concrete CryptoKeyManagementNeeds is a ServiceNeeds wired with parent and short name"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = CryptoKeyManagementNeeds(ar_root, "TestCryptoKeyManagementNeeds")

        assert isinstance(needs, ServiceNeeds)
        assert needs.getShortName() == "TestCryptoKeyManagementNeeds"

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 13.11)"""
        assert CryptoKeyManagementNeeds.__doc__.strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert CryptoKeyManagementNeeds.__init__.__doc__ is None
