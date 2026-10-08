"""
This module contains tests for the AbstractMultiplicityRestriction class.
"""

import pytest
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import AbstractMultiplicityRestriction


class TestAbstractMultiplicityRestriction:

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_abstract_instantiation(self):
        with pytest.raises(TypeError):
            AbstractMultiplicityRestriction()

    def test_subclass_instantiability(self):
        class Concrete(AbstractMultiplicityRestriction):
            pass

        obj = Concrete()
        assert isinstance(obj, AbstractMultiplicityRestriction)
