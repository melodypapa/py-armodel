"""
This module contains tests for the VendorSpecificServiceNeeds class
in the AUTOSAR CommonStructure ServiceNeeds module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    ServiceNeeds,
    VendorSpecificServiceNeeds,
)

SPEC_NOTE = "This represents the ability to define vendor-specific service needs."


class TestVendorSpecificServiceNeeds:
    def test_initialization(self):
        """Test that the concrete VendorSpecificServiceNeeds is a ServiceNeeds wired with parent and short name"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = VendorSpecificServiceNeeds(ar_root, "TestVendorSpecificServiceNeeds")

        assert isinstance(needs, ServiceNeeds)
        assert needs.getShortName() == "TestVendorSpecificServiceNeeds"

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 7.53)"""
        assert VendorSpecificServiceNeeds.__doc__.strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert VendorSpecificServiceNeeds.__init__.__doc__ is None
