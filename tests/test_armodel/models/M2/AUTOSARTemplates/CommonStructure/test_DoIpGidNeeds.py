"""
This module contains tests for the DoIpGidNeeds class
in the AUTOSAR CommonStructure ServiceNeeds module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    DoIpGidNeeds,
    DoIpServiceNeeds,
)

SPEC_NOTE = "The DoIpGidNeeds indicates that the software-component owning this ServiceNeeds is providing the GID number either after a GID Synchronisation or by other means like e.g. flashed EEPROM parameter. This need can be used independent from DoIpGidSynchronizationNeeds and is necessary if the GID can not be provided out of the DoIP configuration options."


class TestDoIpGidNeeds:
    def test_initialization(self):
        """Test that the concrete DoIpGidNeeds is a DoIpServiceNeeds wired with parent and short name"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = DoIpGidNeeds(ar_root, "TestDoIpGidNeeds")

        assert isinstance(needs, DoIpServiceNeeds)
        assert needs.getShortName() == "TestDoIpGidNeeds"

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 13.55)"""
        assert DoIpGidNeeds.__doc__.strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert DoIpGidNeeds.__init__.__doc__ is None
