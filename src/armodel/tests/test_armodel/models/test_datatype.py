import pytest

from ....models.M2.MSR.AsamHdo.BaseTypes import BaseType, BaseTypeDirectDefinition
from ....models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import ApplicationArrayDataType, ApplicationCompositeDataType
from ....models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import ApplicationDataType, ApplicationPrimitiveDataType
from ....models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import ApplicationRecordDataType, AutosarDataType, DataTypeMap
from ....models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpType
from ....models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import PackageableElement
from ....models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import CollectableElement
from ....models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable, MultilanguageReferrable, Referrable
from ....models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ....models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import AbstractImplementationDataType, ImplementationDataType
from ....models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import ImplementationDataTypeElement
from ....models.M2.AUTOSARTemplates.SWComponentTemplate.Components import SymbolProps
from ....models.M2.AUTOSARTemplates.CommonStructure.Implementation import ImplementationProps
from ....models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import ApplicationRecordElement
from ....models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import DataTypeMappingSet
from ....models.M2.MSR.AsamHdo.BaseTypes import SwBaseType
from ....models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement
from .... import AUTOSAR


class Test_M2_AUTOSARTemplates_CommonStructure_Implementation:
    def test_ImplementationProps(self):
        with pytest.raises(NotImplementedError) as err:
            document = AUTOSAR.getInstance()
            ar_root = document.createARPackage("AUTOSAR")
            ImplementationProps(ar_root, "ImplementationProps")
        assert (str(err.value) == "ImplementationProps is an abstract class.")

    def test_SymbolProps(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        prototype = SymbolProps(ar_root, "SymbolProps")

        assert (isinstance(prototype, ARObject))
        assert (isinstance(prototype, ImplementationProps))
        assert (isinstance(prototype, Referrable))
        assert (isinstance(prototype, SymbolProps))

        assert (prototype.parent == ar_root)
        assert (prototype.short_name == "SymbolProps")
        assert (prototype.symbol is None)


class Test_M2_MSR_AsamHdo_BaseTypes:
    def test_BaseType(self):
        with pytest.raises(NotImplementedError) as err:
            document = AUTOSAR.getInstance()
            ar_root = document.createARPackage("AUTOSAR")
            BaseType(ar_root, "BaseType")
        assert (str(err.value) == "BaseType is an abstract class.")

    def test_SwBaseType(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        base_type = SwBaseType(ar_root, "SwBaseType")

        assert (isinstance(base_type, ARElement))
        assert (isinstance(base_type, ARObject))
        assert (isinstance(base_type, CollectableElement))
        assert (isinstance(base_type, Identifiable))
        assert (isinstance(base_type, MultilanguageReferrable))
        assert (isinstance(base_type, PackageableElement))
        assert (isinstance(base_type, Referrable))
        assert (isinstance(base_type, SwBaseType))

        assert (base_type.parent == ar_root)
        assert (base_type.short_name == "SwBaseType")
        assert (isinstance(base_type.baseTypeDefinition, BaseTypeDirectDefinition))


class Test_M2_AUTOSARTemplates_SWComponentTemplate_Datatype_Datatypes:
    def test_AtpType(self):
        with pytest.raises(TypeError) as err:
            document = AUTOSAR.getInstance()
            ar_root = document.createARPackage("AUTOSAR")
            AtpType(ar_root, "AtpType")
        assert (str(err.value) == "AtpType is an abstract class.")

    def test_AutosarDataType(self):
        with pytest.raises(TypeError) as err:
            document = AUTOSAR.getInstance()
            ar_root = document.createARPackage("AUTOSAR")
            AutosarDataType(ar_root, "AutosarDataType")
        assert (str(err.value) == "AutosarDataType is an abstract class.")

    def test_ApplicationDataType(self):
        with pytest.raises(TypeError) as err:
            document = AUTOSAR.getInstance()
            ar_root = document.createARPackage("AUTOSAR")
            ApplicationDataType(ar_root, "ApplicationDataType")
        assert (str(err.value) == "ApplicationDataType is an abstract class.")

    def test_ApplicationPrimitiveDataType(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        data_type = ApplicationPrimitiveDataType(ar_root, "ApplicationPrimitiveDataType")

        assert (isinstance(data_type, ARElement))
        assert (isinstance(data_type, ARObject))
        # assert (isinstance(data_type, AtpBlueprint))
        # assert (isinstance(data_type, AtpBlueprintable))
        # assert (isinstance(data_type, AtpClassifier))
        assert (isinstance(data_type, AtpType))
        assert (isinstance(data_type, AutosarDataType))
        assert (isinstance(data_type, CollectableElement))
        assert (isinstance(data_type, Identifiable))
        assert (isinstance(data_type, MultilanguageReferrable))
        assert (isinstance(data_type, PackageableElement))
        assert (isinstance(data_type, Referrable))
        assert (isinstance(data_type, ApplicationPrimitiveDataType))

        assert (data_type.parent == ar_root)
        assert (data_type.short_name == "ApplicationPrimitiveDataType")
        assert (data_type.swDataDefProps is None)

    def test_ApplicationCompositeDataType(self):
        with pytest.raises(TypeError) as err:
            document = AUTOSAR.getInstance()
            ar_root = document.createARPackage("AUTOSAR")
            ApplicationCompositeDataType(ar_root, "ApplicationCompositeDataType")
        assert (str(err.value) == "ApplicationCompositeDataType is an abstract class.")

    def test_ApplicationArrayDataType(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        data_type = ApplicationArrayDataType(ar_root, "ApplicationArrayDataType")

        assert (isinstance(data_type, ARElement))
        assert (isinstance(data_type, ARObject))
        assert (isinstance(data_type, ApplicationDataType))
        # assert (isinstance(data_type, AtpBlueprint))
        # assert (isinstance(data_type, AtpBlueprintable))
        # assert (isinstance(data_type, AtpClassifier))
        assert (isinstance(data_type, AtpType))
        assert (isinstance(data_type, AutosarDataType))
        assert (isinstance(data_type, CollectableElement))
        assert (isinstance(data_type, Identifiable))
        assert (isinstance(data_type, MultilanguageReferrable))
        assert (isinstance(data_type, PackageableElement))
        assert (isinstance(data_type, Referrable))
        assert (isinstance(data_type, ApplicationArrayDataType))

        assert (data_type.parent == ar_root)
        assert (data_type.short_name == "ApplicationArrayDataType")
        assert (data_type.dynamicArraySizeProfile is None)
        assert (data_type.element is None)

    def test_ApplicationRecordDataType(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        data_type = ApplicationRecordDataType(ar_root, "ApplicationRecordDataType")

        assert (isinstance(data_type, ARElement))
        assert (isinstance(data_type, ARObject))
        assert (isinstance(data_type, ApplicationDataType))
        # assert (isinstance(data_type, AtpBlueprint))
        # assert (isinstance(data_type, AtpBlueprintable))
        # assert (isinstance(data_type, AtpClassifier))
        assert (isinstance(data_type, AtpType))
        assert (isinstance(data_type, AutosarDataType))
        assert (isinstance(data_type, CollectableElement))
        assert (isinstance(data_type, Identifiable))
        assert (isinstance(data_type, MultilanguageReferrable))
        assert (isinstance(data_type, PackageableElement))
        assert (isinstance(data_type, Referrable))
        assert (isinstance(data_type, ApplicationRecordDataType))

        assert (data_type.parent == ar_root)
        assert (data_type.short_name == "ApplicationRecordDataType")

        element = data_type.createApplicationRecordElement("element")
        assert (isinstance(element, ApplicationRecordElement))
        assert (element.short_name == "element")

    def test_DataTypeMap(self):
        data_type_map = DataTypeMap()

        assert (isinstance(data_type_map, ARObject))
        assert (isinstance(data_type_map, DataTypeMap))

        assert (data_type_map.applicationDataTypeRef is None)
        assert (data_type_map.implementationDataTypeRef is None)

    def test_DataTypeMappingSet(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        data_type_mapping_set = DataTypeMappingSet(ar_root, "DataTypeMappingSet")

        assert (isinstance(data_type_mapping_set, ARElement))
        assert (isinstance(data_type_mapping_set, ARObject))
        # assert (isinstance(data_type_mapping_set, AtpBlueprint))
        # assert (isinstance(data_type_mapping_set, AtpBlueprintable))
        assert (isinstance(data_type_mapping_set, CollectableElement))
        assert (isinstance(data_type_mapping_set, Identifiable))
        assert (isinstance(data_type_mapping_set, MultilanguageReferrable))
        assert (isinstance(data_type_mapping_set, PackageableElement))
        assert (isinstance(data_type_mapping_set, Referrable))
        assert (isinstance(data_type_mapping_set, DataTypeMappingSet))

        assert (data_type_mapping_set.parent == ar_root)
        assert (data_type_mapping_set.short_name == "DataTypeMappingSet")
        assert (len(data_type_mapping_set.dataTypeMaps) == 0)

        data_type_map = DataTypeMap()
        data_type_mapping_set.addDataTypeMap(data_type_map)
        assert (len(data_type_mapping_set.getDataTypeMaps()) == 1)
        assert (data_type_mapping_set.getDataTypeMaps()[0] == data_type_map)


class Test_M2_AUTOSARTemplates_CommonStructure_ImplementationDataTypes:
    def test_AbstractImplementationDataType(self):
        with pytest.raises(NotImplementedError) as err:
            document = AUTOSAR.getInstance()
            ar_root = document.createARPackage("AUTOSAR")
            AbstractImplementationDataType(ar_root, "AbstractImplementationDataType")
        assert (str(err.value) == "AbstractImplementationDataType is an abstract class.")

    def test_ImplementationDataType(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        data_type = ar_root.createImplementationDataType("ImplementationDataType")

        assert (isinstance(data_type, ARElement))
        assert (isinstance(data_type, ARObject))
        assert (isinstance(data_type, AbstractImplementationDataType,))
        # assert (isinstance(data_type, AtpBlueprint))
        # assert (isinstance(data_type, AtpBlueprintable))
        # assert (isinstance(data_type, AtpClassifier))
        assert (isinstance(data_type, AtpType))
        assert (isinstance(data_type, AutosarDataType))
        assert (isinstance(data_type, CollectableElement))
        assert (isinstance(data_type, Identifiable))
        assert (isinstance(data_type, MultilanguageReferrable))
        assert (isinstance(data_type, PackageableElement))
        assert (isinstance(data_type, Referrable))
        assert (isinstance(data_type, ImplementationDataType))

        assert (data_type.parent == ar_root)
        assert (data_type.short_name == "ImplementationDataType")
        assert (data_type.subElements == [])
        assert (data_type.symbolProps is None)
        assert (data_type.getTypeEmitter() is None)

        element = data_type.createImplementationDataTypeElement("ImplementationDataTypeElement")
        assert (isinstance(element, ImplementationDataTypeElement))
        assert (element.short_name == "ImplementationDataTypeElement")

        assert (len(data_type.getSubElements()) == 1)
        assert (data_type.getSubElements()[0] == element)
