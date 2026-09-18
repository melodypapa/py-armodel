"""
This module contains tests for the J1939DcmDm19Support class
in the AUTOSAR CommonStructure ServiceNeeds module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    J1939DcmDm19Support,
    ServiceNeeds,
)

SPEC_NOTE = "The software-component provides information about calibration verification numbers for inclusion in DM19"


class TestJ1939DcmDm19Support:
    def test_initialization(self):
        """Test that the concrete J1939DcmDm19Support is a ServiceNeeds wired with parent and short name"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = J1939DcmDm19Support(ar_root, "TestJ1939DcmDm19Support")

        assert isinstance(needs, ServiceNeeds)
        assert needs.getShortName() == "TestJ1939DcmDm19Support"

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 13.72)"""
        assert J1939DcmDm19Support.__doc__.strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert J1939DcmDm19Support.__init__.__doc__ is None
