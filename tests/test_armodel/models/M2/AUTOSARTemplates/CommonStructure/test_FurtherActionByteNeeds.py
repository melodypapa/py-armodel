"""
This module contains tests for the FurtherActionByteNeeds class
in the AUTOSAR CommonStructure ServiceNeeds module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    DoIpServiceNeeds,
    FurtherActionByteNeeds,
)

SPEC_NOTE = 'The FurtherActionByteNeeds indicates that the software-component is able to provide the "further action byte" to the DoIp Service Component.'


class TestFurtherActionByteNeeds:
    def test_initialization(self):
        """Test that the concrete FurtherActionByteNeeds is a DoIpServiceNeeds wired with parent and short name"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = FurtherActionByteNeeds(ar_root, "TestFurtherActionByteNeeds")

        assert isinstance(needs, DoIpServiceNeeds)
        assert needs.getShortName() == "TestFurtherActionByteNeeds"

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 13.62)"""
        assert FurtherActionByteNeeds.__doc__.strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert FurtherActionByteNeeds.__init__.__doc__ is None
