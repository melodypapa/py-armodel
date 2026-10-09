"""
This module contains tests for the AbstractSecurityEventFilter abstract base class.
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import AbstractSecurityEventFilter


class TestAbstractSecurityEventFilter:
    """
    Test class for AbstractSecurityEventFilter functionality.
    """

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_abstract_instantiation(self):
        with pytest.raises(TypeError):
            AbstractSecurityEventFilter(self._parent(), "Filter")

    def test_subclass_instantiability(self):
        class ConcreteFilter(AbstractSecurityEventFilter):
            pass

        obj = ConcreteFilter(self._parent(), "Filter")
        assert isinstance(obj, AbstractSecurityEventFilter)
        assert obj.getShortName() == "Filter"
