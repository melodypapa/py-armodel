""" Test ARRef """

import pytest

from ....models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpInstanceRef
from ....models.M2.AUTOSARTemplates.sw_component_template.composition.instance_refs import OperationInAtomicSwcInstanceRef, POperationInAtomicSwcInstanceRef, PPortInCompositionInstanceRef, ROperationInAtomicSwcInstanceRef, RPortInCompositionInstanceRef
from ....models.M2.AUTOSARTemplates.sw_component_template.swc_internal_behavior.instance_refs_usage import ArVariableInImplementationDataInstanceRef, AutosarVariableRef
from ....models.ar_ref import RefType, TRefType
from ....models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class TestARRef:
    def test_RefType(self):
        ref_type = RefType()
        assert(ref_type.value == "")
        assert(ref_type.dest == "")

    def test_TRefType(self):
        ref_type = TRefType()
        assert(ref_type.value == "")
        assert(ref_type.dest == "")

    def test_AutosarVariableRef(self):
        ref_type = AutosarVariableRef()
        assert(ref_type != None)
        assert(ref_type.autosarVariableIRef == None)
        assert(ref_type.autosarVariableInImplDatatype == None)
        assert(ref_type.localVariableRef == None)

    def test_AtpInstanceRef(self):
        with pytest.raises(NotImplementedError) as err:
            ref_type = AtpInstanceRef()
        assert(str(err.value) == "AtpInstanceRef is an abstract class.")

    def test_ProvidedPortPrototypeInstanceRef(self):
        ref_type = PPortInCompositionInstanceRef()
        assert(ref_type != None)
        assert(ref_type.getContextComponentRef() == None)
        assert(ref_type.getTargetPPortRef() == None)

    def test_RequiredPortPrototypeInstanceRef(self):
        ref_type = RPortInCompositionInstanceRef()
        assert(ref_type != None)
        assert(ref_type.getContextComponentRef() == None)
        assert(ref_type.getTargetRPortRef() == None)

    def test_ArVariableInImplementationDataInstanceRef(self):
        ref_type = ArVariableInImplementationDataInstanceRef()
        assert(ref_type != None)
        assert(ref_type.getPortPrototypeRef() == None)
        assert(ref_type.getTargetDataPrototypeRef() == None)

    def test_OperationInAtomicSwcInstanceRef(self):
        with pytest.raises(NotImplementedError) as err:
            _ = OperationInAtomicSwcInstanceRef()
        assert(str(err.value) == "OperationInAtomicSwcInstanceRef is an abstract class.")

    def test_POperationInAtomicSwcInstanceRef(self):
        ref_type = POperationInAtomicSwcInstanceRef()
        assert(isinstance(ref_type, ARObject))
        assert(isinstance(ref_type, AtpInstanceRef))
        assert(isinstance(ref_type, OperationInAtomicSwcInstanceRef))
        assert(isinstance(ref_type, POperationInAtomicSwcInstanceRef))
        assert(ref_type != None)
        assert(ref_type.getContextPPortRef() == None)
        assert(ref_type.getTargetProvidedOperationRef() == None)

    def test_ROperationInAtomicSwcInstanceRef(self):
        ref_type = ROperationInAtomicSwcInstanceRef()
        assert(isinstance(ref_type, ARObject))
        assert(isinstance(ref_type, AtpInstanceRef))
        assert(isinstance(ref_type, OperationInAtomicSwcInstanceRef))
        assert(isinstance(ref_type, ROperationInAtomicSwcInstanceRef))
        assert(ref_type != None)
        assert(ref_type.getContextRPortRef() == None)
        assert(ref_type.getTargetRequiredOperationRef() == None)
