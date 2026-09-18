"""
This module contains tests for the J1939RmIncomingRequestServiceNeeds class
in the AUTOSAR CommonStructure ServiceNeeds module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    J1939RmIncomingRequestServiceNeeds,
    ServiceNeeds,
)

SPEC_NOTE = '"This meta-class shall be used to specify needs with respect to the configuration of the J1939Rm, in particular for the case where an ApplicationSwComponentType needs to accept a request from another J1939 node.'


class TestJ1939RmIncomingRequestServiceNeeds:
    def test_initialization(self):
        """Test that the concrete J1939RmIncomingRequestServiceNeeds is a ServiceNeeds wired with parent and short name"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = J1939RmIncomingRequestServiceNeeds(ar_root, "TestJ1939RmIncomingRequestServiceNeeds")

        assert isinstance(needs, ServiceNeeds)
        assert needs.getShortName() == "TestJ1939RmIncomingRequestServiceNeeds"

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 13.71)"""
        assert J1939RmIncomingRequestServiceNeeds.__doc__.strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert J1939RmIncomingRequestServiceNeeds.__init__.__doc__ is None
