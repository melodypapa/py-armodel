"""
This module contains tests for the DoIpPowerModeStatusNeeds class
in the AUTOSAR CommonStructure ServiceNeeds module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    DoIpPowerModeStatusNeeds,
    DoIpServiceNeeds,
)

SPEC_NOTE = "The DoIpPowerModeStatusNeeds indicates that the software-component owning this ServiceNeeds is providing the PowerModeStatus for the DoIP service 0x4003 according to ISO 13400-2:2012."


class TestDoIpPowerModeStatusNeeds:
    def test_initialization(self):
        """Test that the concrete DoIpPowerModeStatusNeeds is a DoIpServiceNeeds wired with parent and short name"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = DoIpPowerModeStatusNeeds(ar_root, "TestDoIpPowerModeStatusNeeds")

        assert isinstance(needs, DoIpServiceNeeds)
        assert needs.getShortName() == "TestDoIpPowerModeStatusNeeds"

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 13.57)"""
        assert DoIpPowerModeStatusNeeds.__doc__.strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert DoIpPowerModeStatusNeeds.__init__.__doc__ is None
