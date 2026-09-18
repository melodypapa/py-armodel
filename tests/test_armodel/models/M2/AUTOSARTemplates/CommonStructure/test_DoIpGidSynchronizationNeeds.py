"""
This module contains tests for the DoIpGidSynchronizationNeeds class
in the AUTOSAR CommonStructure ServiceNeeds module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    DoIpGidSynchronizationNeeds,
    DoIpServiceNeeds,
)

SPEC_NOTE = "The DoIpGidSynchronizationNeeds indicates that the software-component owning this ServiceNeeds is triggered by the DoIP entity to start a synchronization of the GID (Group Identification) on the DoIP service 0x0001, 0x0002, 0x0003 or before announcement via service 0x0004 according to ISO 13400-2:2012 if necessary. Note that this need is only relevant for DoIP synchronization masters."


class TestDoIpGidSynchronizationNeeds:
    def test_initialization(self):
        """Test that the concrete DoIpGidSynchronizationNeeds is a DoIpServiceNeeds wired with parent and short name"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = DoIpGidSynchronizationNeeds(ar_root, "TestDoIpGidSynchronizationNeeds")

        assert isinstance(needs, DoIpServiceNeeds)
        assert needs.getShortName() == "TestDoIpGidSynchronizationNeeds"

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 13.56)"""
        assert DoIpGidSynchronizationNeeds.__doc__.strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert DoIpGidSynchronizationNeeds.__init__.__doc__ is None
