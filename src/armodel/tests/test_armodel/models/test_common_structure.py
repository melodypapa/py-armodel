import pytest

from .... import AUTOSAR
from ....models.common_structure import AbstractImplementationDataTypeElement, ConstantReference, ImplementationDataTypeElement, ValueSpecification, ConstantSpecification, ExecutableEntity
from ....models.datatype import AbstractImplementationDataType
from ....models.general_structure import ARElement, ARObject, CollectableElement, Identifiable
from ....models.general_structure import MultilanguageReferrable, PackageableElement, Referrable

class Test_M2_AUTOSARTemplates_CommonStructure_Constants:
    
    def test_ValueSpecification(self):
        with pytest.raises(NotImplementedError) as err:
            ValueSpecification()
        assert(str(err.value) == "ValueSpecification is an abstract class.")

    def test_ConstantSpecification(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        spec = ConstantSpecification(ar_root, "constant")
        
        assert(isinstance(spec, ARElement))
        assert(isinstance(spec, ARObject))
        assert(isinstance(spec, CollectableElement))
        assert(isinstance(spec, Identifiable))
        assert(isinstance(spec, MultilanguageReferrable))
        assert(isinstance(spec, PackageableElement))
        assert(isinstance(spec, Referrable))
        assert(isinstance(spec, ConstantSpecification)) 

    def test_ConstantReference(self):
        ref = ConstantReference()

        assert(ref.constant_ref == None)

        assert(isinstance(ref, ARObject))
        assert(isinstance(ref, ValueSpecification))
        assert(isinstance(ref, ConstantReference))

class Test_M2_AUTOSARTemplates_CommonStructure_InternalBehavior:
    def test_ExecutableEntity(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        with pytest.raises(NotImplementedError) as err:
            ExecutableEntity(ar_root, "ExecutableEntity")
        assert(str(err.value) == "ExecutableEntity is an abstract class.")

class Test_M2_AUTOSARTemplates_CommonStructure_ImplementationDataTypes:
    def test_ImplementationDataTypeElement(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        data_type = ImplementationDataTypeElement(ar_root, "implementation_data_type")

        assert(data_type.short_name == "implementation_data_type")
        assert(data_type.arraySize == None)
        assert(data_type.isOptional == None)

        assert(isinstance(data_type, ARObject))
        assert(isinstance(data_type, AbstractImplementationDataTypeElement))
        # assert(isinstance(data_type, AtpClassifier))
        # assert(isinstance(data_type, AtpFeature))
        # assert(isinstance(data_type, AtpStructureElement))
        assert(isinstance(data_type, Identifiable))
        assert(isinstance(data_type, MultilanguageReferrable))
        assert(isinstance(data_type, Referrable))
        assert(isinstance(data_type, ImplementationDataTypeElement))

        sub_type = data_type.createImplementationDataTypeElement("sub_type")
        assert(sub_type.short_name == "sub_type")
        assert(isinstance(sub_type, ImplementationDataTypeElement))

        assert(len(data_type.getImplementationDataTypeElements()) == 1)
        sub_type2 = data_type.getImplementationDataTypeElements()[0]
        assert(sub_type == sub_type2) 
