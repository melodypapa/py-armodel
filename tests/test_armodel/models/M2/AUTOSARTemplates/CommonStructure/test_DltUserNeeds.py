"""
This module contains tests for the DltUserNeeds class
in the AUTOSAR CommonStructure ServiceNeeds module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    DltUserNeeds,
    ServiceNeeds,
)

SPEC_NOTE = (
    "This meta-class specifies the needs on the configuration of the Diagnostic Log and Trace module for one SessionId. "
    "This class currently contains no attributes. "
    "An instance of this class is used to find out which PortPrototypes of an AtomicSwComponentType belong to this SessionId "
    "in order to group the request and response PortPrototypes of the same SessionId. "
    "The actual SessionId value is stored in the PortDefinedArgumentValue of the respective PortPrototype specification."
)


class TestDltUserNeeds:
    def test_initialization(self):
        """Test that the concrete DltUserNeeds is an Identifiable wired with parent and short name"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        dlt_user = DltUserNeeds(ar_root, "TestDltUserNeeds")

        assert isinstance(dlt_user, ServiceNeeds)
        assert dlt_user.getShortName() == "TestDltUserNeeds"

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 12.16)"""
        assert DltUserNeeds.__doc__.strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert DltUserNeeds.__init__.__doc__ is None
