"""
This module contains tests for the EcuStateMgrUserNeeds class
in the AUTOSAR CommonStructure ServiceNeeds module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    EcuStateMgrUserNeeds,
    ServiceNeeds,
)

SPEC_NOTE = (
    'Specifies the abstract needs on the configuration of the ECU State Manager for one "user". '
    "This class currently contains no attributes. Its name can be regarded as a symbol "
    "identifying the user from the viewpoint of the component or module which owns this class."
)


class TestEcuStateMgrUserNeeds:
    def test_initialization(self):
        """Test that the concrete EcuStateMgrUserNeeds is an Identifiable wired with parent and short name"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        ecu_state = EcuStateMgrUserNeeds(ar_root, "TestEcuStateMgrUserNeeds")

        assert isinstance(ecu_state, ServiceNeeds)
        assert ecu_state.getShortName() == "TestEcuStateMgrUserNeeds"

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 12.14)"""
        assert EcuStateMgrUserNeeds.__doc__.strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert EcuStateMgrUserNeeds.__init__.__doc__ is None
