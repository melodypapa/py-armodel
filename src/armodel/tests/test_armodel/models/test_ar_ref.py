""" Test ARRef """

import pytest

from ....models.ar_ref import ArVariableInImplementationDataInstanceRef, AutosarVariableRef, ProvidedPortPrototypeInstanceRef, RequiredPortPrototypeInstanceRef
from ....models.ar_ref import OperationInAtomicSwcInstanceRef, POperationInAtomicSwcInstanceRef, ROperationInAtomicSwcInstanceRef, RefType, TRefType, AtpInstanceRef
from ....models.general_structure import ARObject


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
        assert(ref_type.autosar_variable_iref == None)
        assert(ref_type.autosar_variable_in_impl_datatype == None)
        assert(ref_type.local_variable_ref == None)

    def test_AtpInstanceRef(self):
        with pytest.raises(NotImplementedError) as err:
            ref_type = AtpInstanceRef()
        assert(str(err.value) == "AtpInstanceRef is an abstract class.")

    def test_ProvidedPortPrototypeInstanceRef(self):
        ref_type = ProvidedPortPrototypeInstanceRef()
        assert(ref_type != None)
        assert(ref_type.context_component_ref == None)
        assert(ref_type.target_p_port_ref == None)

    def test_RequiredPortPrototypeInstanceRef(self):
        ref_type = RequiredPortPrototypeInstanceRef()
        assert(ref_type != None)
        assert(ref_type.context_component_ref == None)
        assert(ref_type.target_r_port_ref == None)

    def test_ArVariableInImplementationDataInstanceRef(self):
        ref_type = ArVariableInImplementationDataInstanceRef()
        assert(ref_type != None)
        assert(ref_type.port_prototype_ref == None)
        assert(ref_type.target_data_prototype_ref == None)

    def test_OperationInAtomicSwcInstanceRef(self):
        with pytest.raises(NotImplementedError) as err:
            ref_type = OperationInAtomicSwcInstanceRef()
        assert(str(err.value) == "OperationInAtomicSwcInstanceRef is an abstract class.")

    def test_POperationInAtomicSwcInstanceRef(self):
        ref_type = POperationInAtomicSwcInstanceRef()
        assert(isinstance(ref_type, ARObject))
        assert(isinstance(ref_type, AtpInstanceRef))
        assert(isinstance(ref_type, OperationInAtomicSwcInstanceRef))
        assert(isinstance(ref_type, POperationInAtomicSwcInstanceRef))
        assert(ref_type != None)
        assert(ref_type.context_p_port_ref == None)
        assert(ref_type.target_provided_operation_ref == None)

    def test_ROperationInAtomicSwcInstanceRef(self):
        ref_type = ROperationInAtomicSwcInstanceRef()
        assert(isinstance(ref_type, ARObject))
        assert(isinstance(ref_type, AtpInstanceRef))
        assert(isinstance(ref_type, OperationInAtomicSwcInstanceRef))
        assert(isinstance(ref_type, ROperationInAtomicSwcInstanceRef))
        assert(ref_type != None)
        assert(ref_type.context_r_port_ref == None)
        assert(ref_type.target_required_operation_ref == None)
