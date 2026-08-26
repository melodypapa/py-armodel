"""
This module contains tests for the EOCExecutableEntityRefAbstract class in the
AUTOSAR CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint module.
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint import (
    EOCExecutableEntityRef,
    EOCExecutableEntityRefAbstract,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestEOCExecutableEntityRefAbstract:
    """
    Test class for EOCExecutableEntityRefAbstract functionality.
    """

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_abstract_class_cannot_be_instantiated(self):
        parent = self._parent()
        with pytest.raises(TypeError, match="EOCExecutableEntityRefAbstract is an abstract class"):
            EOCExecutableEntityRefAbstract(parent, "EOCAbstract")

    def test_initialization_defaults_via_concrete_subclass(self):
        parent = self._parent()
        obj = EOCExecutableEntityRef(parent, "Entity1")
        assert isinstance(obj, EOCExecutableEntityRefAbstract)
        assert obj.getShortName() == "Entity1"
        assert obj.getDirectSuccessorRefs() == []

    def test_base_properties(self):
        parent = self._parent()
        obj = EOCExecutableEntityRef(parent, "Entity1")

        assert obj.addDirectSuccessorRef(RefType().setValue("/AUTOSAR/Group1").setDest("EOC-EXECUTABLE-ENTITY-REF-GROUP")) is obj
        assert obj.addDirectSuccessorRef(RefType().setValue("/AUTOSAR/Entity2").setDest("EOC-EXECUTABLE-ENTITY-REF")) is obj

        refs = obj.getDirectSuccessorRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/AUTOSAR/Group1"
        assert refs[0].getDest() == "EOC-EXECUTABLE-ENTITY-REF-GROUP"
        assert refs[1].getValue() == "/AUTOSAR/Entity2"

        obj.addDirectSuccessorRef(None)
        assert len(obj.getDirectSuccessorRefs()) == 2
