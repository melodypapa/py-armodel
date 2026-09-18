"""
This module contains tests for the SyncTimeBaseMgrUserNeeds class
in the AUTOSAR CommonStructure ServiceNeeds module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    ServiceNeeds,
    SyncTimeBaseMgrUserNeeds,
)

SPEC_NOTE = "Specifies the needs on the configuration of the Synchronized Time-base Manager for one time-base. This class currently contains no attributes. An instance of this class is used to find out which ports of a software-component belong to this time-base in order to group the request and response ports of the same time-base. The actual time-base value is stored in the PortDefinedArgumentValue of the respective port specification."


class TestSyncTimeBaseMgrUserNeeds:
    def test_initialization(self):
        """Test that the concrete SyncTimeBaseMgrUserNeeds is a ServiceNeeds wired with parent and short name"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = SyncTimeBaseMgrUserNeeds(ar_root, "TestSyncTimeBaseMgrUserNeeds")

        assert isinstance(needs, ServiceNeeds)
        assert needs.getShortName() == "TestSyncTimeBaseMgrUserNeeds"

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 12.17)"""
        assert SyncTimeBaseMgrUserNeeds.__doc__.strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert SyncTimeBaseMgrUserNeeds.__init__.__doc__ is None
