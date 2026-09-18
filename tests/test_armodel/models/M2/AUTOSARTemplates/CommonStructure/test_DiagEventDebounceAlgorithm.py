"""
This module contains tests for the DiagEventDebounceAlgorithm class
in the AUTOSAR CommonStructure ServiceNeeds module.
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    DiagEventDebounceAlgorithm,
    DiagEventDebounceCounterBased,
)

SPEC_NOTE = (
    "This class represents the ability to specify the pre-debounce algorithm which is "
    "selected and/or required by the particular monitor. This class inherits from "
    "Identifiable in order to allow further documentation of the expected or implemented "
    "debouncing and to use the category for the identification of the expected / "
    "implemented debouncing."
)


class TestDiagEventDebounceAlgorithm:
    def test_abstract_initialization(self):
        """Test that DiagEventDebounceAlgorithm cannot be instantiated directly"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        with pytest.raises(TypeError):
            DiagEventDebounceAlgorithm(ar_root, "TestDiagEventDebounceAlgorithm")

    def test_concrete_subclass_initialization(self):
        """Test that a concrete DiagEventDebounceAlgorithm subclass is an Identifiable wired with parent and short name"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        debounce = DiagEventDebounceCounterBased(ar_root, "TestDiagEventDebounceAlgorithm")

        assert isinstance(debounce, DiagEventDebounceAlgorithm)
        assert debounce.getShortName() == "TestDiagEventDebounceAlgorithm"

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 12.32)"""
        assert DiagEventDebounceAlgorithm.__doc__.strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert DiagEventDebounceAlgorithm.__init__.__doc__ is None
