"""
This module contains tests for the CryptoServiceJobNeeds class
in the AUTOSAR CommonStructure ServiceNeeds module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    CryptoServiceJobNeeds,
    ServiceNeeds,
)

SPEC_NOTE = "This meta-class shall be taken to indicate that the service use case modeled with this kind of Service Needs assumes the usage of the crypto job API."


class TestCryptoServiceJobNeeds:
    def test_initialization(self):
        """Test that the concrete CryptoServiceJobNeeds is a ServiceNeeds wired with parent and short name"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = CryptoServiceJobNeeds(ar_root, "TestCryptoServiceJobNeeds")

        assert isinstance(needs, ServiceNeeds)
        assert needs.getShortName() == "TestCryptoServiceJobNeeds"

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 13.10)"""
        assert CryptoServiceJobNeeds.__doc__.strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert CryptoServiceJobNeeds.__init__.__doc__ is None
