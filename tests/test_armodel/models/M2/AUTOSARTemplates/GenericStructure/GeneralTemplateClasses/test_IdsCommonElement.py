"""
This module contains tests for the IdsCommonElement and IdsMapping abstract base classes.
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import IdsCommonElement, IdsMapping


class TestIdsCommonElement:
    """
    Test class for the IDS base classes.
    """

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_abstract_instantiation(self):
        with pytest.raises(TypeError):
            IdsCommonElement(self._parent(), "IdsElement")

    def test_subclass_instantiability(self):
        class ConcreteIdsElement(IdsCommonElement):
            pass

        obj = ConcreteIdsElement(self._parent(), "IdsElement")
        assert isinstance(obj, IdsCommonElement)
        assert obj.getShortName() == "IdsElement"

    def test_ids_mapping_abstract_instantiation(self):
        with pytest.raises(TypeError):
            IdsMapping(self._parent(), "Mapping")

    def test_ids_mapping_subclass_instantiability(self):
        class ConcreteIdsMapping(IdsMapping):
            pass

        obj = ConcreteIdsMapping(self._parent(), "Mapping")
        assert isinstance(obj, IdsMapping)
        assert isinstance(obj, IdsCommonElement)
        assert obj.getShortName() == "Mapping"
