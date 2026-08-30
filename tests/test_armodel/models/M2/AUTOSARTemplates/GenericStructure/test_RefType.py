"""Test ARRef"""

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, TRefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import (
    OperationInAtomicSwcInstanceRef,
    POperationInAtomicSwcInstanceRef,
    ROperationInAtomicSwcInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import (
    PPortInCompositionInstanceRef,
    RPortInCompositionInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import ArVariableInImplementationDataInstanceRef, AutosarVariableRef


class TestARRef:
    def test_RefType(self):
        ref_type = RefType()
        assert ref_type.getBase() is None
        assert ref_type.getValue() is None
        assert ref_type.getDest() is None

    def test_TRefType(self):
        ref_type = TRefType()
        assert ref_type.getBase() is None
        assert ref_type.getValue() is None
        assert ref_type.getDest() is None

    def test_AutosarVariableRef(self):
        ref_type = AutosarVariableRef()
        assert ref_type is not None
        assert ref_type.autosarVariableIRef is None
        assert ref_type.autosarVariableInImplDatatype is None
        assert ref_type.localVariableRef is None

    def test_AtpInstanceRef(self):
        with pytest.raises(TypeError) as err:
            _ref_type = AtpInstanceRef()
        assert str(err.value) == "AtpInstanceRef is an abstract class."

    def test_ProvidedPortPrototypeInstanceRef(self):
        ref_type = PPortInCompositionInstanceRef()
        assert ref_type is not None
        assert ref_type.getContextComponentRef() is None
        assert ref_type.getTargetPPortRef() is None

    def test_RequiredPortPrototypeInstanceRef(self):
        ref_type = RPortInCompositionInstanceRef()
        assert ref_type is not None
        assert ref_type.getContextComponentRef() is None
        assert ref_type.getTargetRPortRef() is None

    def test_ArVariableInImplementationDataInstanceRef(self):
        ref_type = ArVariableInImplementationDataInstanceRef()
        assert ref_type is not None
        assert ref_type.getPortPrototypeRef() is None
        assert ref_type.getTargetDataPrototypeRef() is None

    def test_OperationInAtomicSwcInstanceRef(self):
        with pytest.raises(TypeError) as err:
            _ = OperationInAtomicSwcInstanceRef()
        assert str(err.value) == "OperationInAtomicSwcInstanceRef is an abstract class."

    def test_POperationInAtomicSwcInstanceRef(self):
        ref_type = POperationInAtomicSwcInstanceRef()
        assert isinstance(ref_type, ARObject)
        assert isinstance(ref_type, AtpInstanceRef)
        assert isinstance(ref_type, OperationInAtomicSwcInstanceRef)
        assert isinstance(ref_type, POperationInAtomicSwcInstanceRef)
        assert ref_type is not None
        assert ref_type.getContextPPortRef() is None
        assert ref_type.getTargetProvidedOperationRef() is None

    def test_ROperationInAtomicSwcInstanceRef(self):
        ref_type = ROperationInAtomicSwcInstanceRef()
        assert isinstance(ref_type, ARObject)
        assert isinstance(ref_type, AtpInstanceRef)
        assert isinstance(ref_type, OperationInAtomicSwcInstanceRef)
        assert isinstance(ref_type, ROperationInAtomicSwcInstanceRef)
        assert ref_type is not None
        assert ref_type.getContextRPortRef() is None
        assert ref_type.getTargetRequiredOperationRef() is None
