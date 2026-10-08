"""
This module contains tests for the AbstractCondition class.
"""

import pytest
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import AbstractCondition


class TestAbstractCondition:

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_abstract_instantiation(self):
        with pytest.raises(TypeError):
            AbstractCondition()

    def test_subclass_instantiability(self):
        class Concrete(AbstractCondition):
            pass

        obj = Concrete()
        assert isinstance(obj, AbstractCondition)
