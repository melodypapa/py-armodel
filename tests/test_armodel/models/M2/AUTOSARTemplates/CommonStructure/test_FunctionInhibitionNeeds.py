"""
This module contains tests for the FunctionInhibitionNeeds class
in the AUTOSAR CommonStructure ServiceNeeds module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    FunctionInhibitionNeeds,
    ServiceNeeds,
)

SPEC_NOTE = "Specifies the abstract needs on the configuration of the Function Inhibition Manager for one Function Identifier (FID). This class currently contains no attributes. Its name can be regarded as a symbol identifying the FID from the viewpoint of the component or module which owns this class."


class TestFunctionInhibitionNeeds:
    def test_initialization(self):
        """Test that the concrete FunctionInhibitionNeeds is a ServiceNeeds wired with parent and short name"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = FunctionInhibitionNeeds(ar_root, "TestFunctionInhibitionNeeds")

        assert isinstance(needs, ServiceNeeds)
        assert needs.getShortName() == "TestFunctionInhibitionNeeds"

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 12.19)"""
        assert FunctionInhibitionNeeds.__doc__.strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert FunctionInhibitionNeeds.__init__.__doc__ is None
