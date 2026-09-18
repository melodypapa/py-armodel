"""
This module contains tests for the HardwareTestNeeds class
in the AUTOSAR CommonStructure ServiceNeeds module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    HardwareTestNeeds,
    ServiceNeeds,
)

SPEC_NOTE = "This meta-class represents the ability to indicate that a software-component is interested in the results of the hardware test and will establish a PortPrototype to query the hardware test manager."


class TestHardwareTestNeeds:
    def test_initialization(self):
        """Test that the concrete HardwareTestNeeds is a ServiceNeeds wired with parent and short name"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = HardwareTestNeeds(ar_root, "TestHardwareTestNeeds")

        assert isinstance(needs, ServiceNeeds)
        assert needs.getShortName() == "TestHardwareTestNeeds"

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 12.40)"""
        assert HardwareTestNeeds.__doc__.strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert HardwareTestNeeds.__init__.__doc__ is None
