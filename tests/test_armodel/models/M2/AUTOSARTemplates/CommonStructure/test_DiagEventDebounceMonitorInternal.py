"""
This module contains tests for the DiagEventDebounceMonitorInternal class
in the AUTOSAR CommonStructure ServiceNeeds module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    DiagEventDebounceAlgorithm,
    DiagEventDebounceMonitorInternal,
)

SPEC_NOTE = (
    "This meta-class represents the ability to indicate that no Dem pre-debounce "
    "algorithm shall be used for this diagnostic monitor. The SWC might implement an "
    "internal debouncing algorithm and report qualified (debounced) results to the Dem/DM."
)


class TestDiagEventDebounceMonitorInternal:
    def test_initialization(self):
        """Test that the concrete DiagEventDebounceMonitorInternal is an Identifiable wired with parent and short name"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        debounce = DiagEventDebounceMonitorInternal(ar_root, "TestDiagEventDebounceMonitorInternal")

        assert isinstance(debounce, DiagEventDebounceAlgorithm)
        assert debounce.getShortName() == "TestDiagEventDebounceMonitorInternal"

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 12.35)"""
        assert DiagEventDebounceMonitorInternal.__doc__.strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert DiagEventDebounceMonitorInternal.__init__.__doc__ is None
