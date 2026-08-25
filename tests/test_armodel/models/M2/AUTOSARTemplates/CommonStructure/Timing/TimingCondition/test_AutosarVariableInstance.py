"""
This module contains tests for the AutosarVariableInstance class in the
AUTOSAR CommonStructure.Timing.TimingCondition module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition import (
    AutosarVariableInstance,
    VariableInComponentInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestAutosarVariableInstance:
    """
    Test class for AutosarVariableInstance functionality.
    """

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_initialization(self):
        parent = self._parent()
        obj = AutosarVariableInstance(parent, "Var1")
        assert isinstance(obj, AutosarVariableInstance)
        assert obj.getShortName() == "Var1"
        assert obj.getVariableInstanceIRef() is None

    def test_set_variable_instance_iref(self):
        parent = self._parent()
        obj = AutosarVariableInstance(parent, "Var1")
        iref = VariableInComponentInstanceRef()
        iref.setTargetDataPrototypeRef(RefType().setValue("/Pkg/DP").setDest("DATA-PROTOTYPE"))
        assert obj.setVariableInstanceIRef(iref) is obj
        assert obj.getVariableInstanceIRef() is iref
        assert isinstance(obj.getVariableInstanceIRef(), VariableInComponentInstanceRef)

    def test_set_variable_instance_iref_none_noop(self):
        parent = self._parent()
        obj = AutosarVariableInstance(parent, "Var1")
        iref = VariableInComponentInstanceRef()
        iref.setTargetDataPrototypeRef(RefType().setValue("/Pkg/DP").setDest("DATA-PROTOTYPE"))
        obj.setVariableInstanceIRef(iref)
        assert obj.setVariableInstanceIRef(None) is obj
        assert obj.getVariableInstanceIRef() is iref
