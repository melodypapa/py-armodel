"""
This module contains tests for the AutosarOperationArgumentInstance class in the
AUTOSAR CommonStructure.Timing.TimingCondition module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition import (
    AutosarOperationArgumentInstance,
    OperationArgumentInComponentInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestAutosarOperationArgumentInstance:
    """
    Test class for AutosarOperationArgumentInstance functionality.
    """

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_initialization(self):
        parent = self._parent()
        obj = AutosarOperationArgumentInstance(parent, "Arg1")
        assert isinstance(obj, AutosarOperationArgumentInstance)
        assert obj.getShortName() == "Arg1"
        assert obj.getOperationArgumentInstanceIRef() is None

    def test_set_operation_argument_instance_iref(self):
        parent = self._parent()
        obj = AutosarOperationArgumentInstance(parent, "Arg1")
        iref = OperationArgumentInComponentInstanceRef()
        iref.setTargetDataPrototypeRef(RefType().setValue("/Pkg/DP").setDest("DATA-PROTOTYPE"))
        assert obj.setOperationArgumentInstanceIRef(iref) is obj
        assert obj.getOperationArgumentInstanceIRef() is iref
        assert isinstance(obj.getOperationArgumentInstanceIRef(), OperationArgumentInComponentInstanceRef)

    def test_set_operation_argument_instance_iref_none_noop(self):
        parent = self._parent()
        obj = AutosarOperationArgumentInstance(parent, "Arg1")
        iref = OperationArgumentInComponentInstanceRef()
        iref.setTargetDataPrototypeRef(RefType().setValue("/Pkg/DP").setDest("DATA-PROTOTYPE"))
        obj.setOperationArgumentInstanceIRef(iref)
        assert obj.setOperationArgumentInstanceIRef(None) is obj
        assert obj.getOperationArgumentInstanceIRef() is iref
