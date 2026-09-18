"""
This module contains tests for the DoIpActivationLineNeeds class
in the AUTOSAR CommonStructure ServiceNeeds module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    DoIpActivationLineNeeds,
    DoIpServiceNeeds,
)

SPEC_NOTE = "A DoIP entity needs to be informed when an external tester is attached or activated. The DoIpActivation ServiceNeeds specifies the trigger for such an event. Examples would be a Pdu via a regular communication bus, a PWM signal, or an I/O. For details please refer to the ISO 13400."


class TestDoIpActivationLineNeeds:
    def test_initialization(self):
        """Test that the concrete DoIpActivationLineNeeds is a DoIpServiceNeeds wired with parent and short name"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = DoIpActivationLineNeeds(ar_root, "TestDoIpActivationLineNeeds")

        assert isinstance(needs, DoIpServiceNeeds)
        assert needs.getShortName() == "TestDoIpActivationLineNeeds"

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 13.60)"""
        assert DoIpActivationLineNeeds.__doc__.strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert DoIpActivationLineNeeds.__init__.__doc__ is None
