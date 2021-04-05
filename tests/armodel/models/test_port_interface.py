import pytest

from armodel.models.ar_package import AUTOSAR
from armodel.models.data_prototype import AtpPrototype, AutosarDataPrototype, DataPrototype, VariableDataPrototype
from armodel.models.datatype import AtpType
from armodel.models.general_structure import ARElement, ARObject, AtpFeature, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
from armodel.models.port_interface import ApplicationError, ArgumentDataPrototype, DataInterface, NvDataInterface, ParameterInterface, PortInterface, SenderReceiverInterface


class Test_M2_AUTOSARTemplates_SWComponentTemplate_PortInterface:

    def test_PortInterface(self):
        with pytest.raises(NotImplementedError) as err:
            PortInterface(AUTOSAR.getInstance(), "PortInterface")
        assert(str(err.value) == "PortInterface is an abstract class.")

    def test_DataInterface(self):
        with pytest.raises(NotImplementedError) as err:
            DataInterface(AUTOSAR.getInstance(), "DataInterface")
        assert(str(err.value) == "DataInterface is an abstract class.")

    def test_NvDataInterface(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        data_if = NvDataInterface(ar_root, "NvDataInterface")

        assert(isinstance(data_if, ARElement))
        assert(isinstance(data_if, ARObject))
        # assert(isinstance(sr, AtpBlueprint))
        # assert(isinstance(sr, AtpBlueprintable))
        # assert(isinstance(sr, AtpClassifier))
        assert(isinstance(data_if, AtpType))
        assert(isinstance(data_if, CollectableElement))
        assert(isinstance(data_if, DataInterface))
        assert(isinstance(data_if, Identifiable))
        assert(isinstance(data_if, MultilanguageReferrable))
        assert(isinstance(data_if, PackageableElement)) 
        assert(isinstance(data_if, PortInterface)) 
        assert(isinstance(data_if, Referrable))
        assert(isinstance(data_if, NvDataInterface))

        assert(data_if.parent == ar_root)
        assert(data_if.short_name == "NvDataInterface")

    def test_ParameterInterface(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        data_if = ParameterInterface(ar_root, "ParameterInterface")

        assert(isinstance(data_if, ARElement))
        assert(isinstance(data_if, ARObject))
        # assert(isinstance(sr, AtpBlueprint))
        # assert(isinstance(sr, AtpBlueprintable))
        # assert(isinstance(sr, AtpClassifier))
        assert(isinstance(data_if, AtpType))
        assert(isinstance(data_if, CollectableElement))
        assert(isinstance(data_if, DataInterface))
        assert(isinstance(data_if, Identifiable))
        assert(isinstance(data_if, MultilanguageReferrable))
        assert(isinstance(data_if, PackageableElement)) 
        assert(isinstance(data_if, PortInterface)) 
        assert(isinstance(data_if, Referrable))
        assert(isinstance(data_if, ParameterInterface))

        assert(data_if.parent == ar_root)
        assert(data_if.short_name == "ParameterInterface")

    def test_SenderReceiverInterface(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        sr_if = SenderReceiverInterface(ar_root, "sr_if")

        assert(isinstance(sr_if, ARElement))
        assert(isinstance(sr_if, ARObject))
        # assert(isinstance(sr, AtpBlueprint))
        # assert(isinstance(sr, AtpBlueprintable))
        # assert(isinstance(sr, AtpClassifier))
        assert(isinstance(sr_if, AtpType))
        assert(isinstance(sr_if, CollectableElement))
        assert(isinstance(sr_if, DataInterface))
        assert(isinstance(sr_if, Identifiable))
        assert(isinstance(sr_if, MultilanguageReferrable))
        assert(isinstance(sr_if, PackageableElement)) 
        assert(isinstance(sr_if, PortInterface)) 
        assert(isinstance(sr_if, Referrable))
        assert(isinstance(sr_if, SenderReceiverInterface))

        assert(sr_if.short_name == "sr_if")
        assert(sr_if.parent == ar_root)
        assert(len(sr_if.getDataElements()) == 0)

        element = sr_if.createDataElement("element")
        assert(isinstance(element, VariableDataPrototype))
        assert(element.short_name == "element")
        assert(len(sr_if.getDataElements()) == 1)

        element2 = sr_if.getDataElement("element")
        assert(element == element2)

        with pytest.raises(IndexError) as err:
            sr_if.getDataElement("non_exist_element")
        assert(str(err.value) == "data element <non_exist_element> can not be found.")

    def test_ArgumentDataPrototype(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        prototype = ArgumentDataPrototype(ar_root, "ArgumentDataPrototype")

        assert(isinstance(prototype, ARObject))
        assert(isinstance(prototype, AtpFeature))
        assert(isinstance(prototype, AtpPrototype))
        assert(isinstance(prototype, AutosarDataPrototype))
        assert(isinstance(prototype, DataPrototype))
        assert(isinstance(prototype, Identifiable))
        assert(isinstance(prototype, MultilanguageReferrable))
        assert(isinstance(prototype, Referrable))
        assert(isinstance(prototype, ArgumentDataPrototype))

        assert(prototype.parent == ar_root)
        assert(prototype.short_name == "ArgumentDataPrototype")
        assert(prototype.direction == "")
        assert(prototype.server_argument_impl_policy == "")

    def test_ApplicationError(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        app_error = ApplicationError(ar_root, "ApplicationError")

        assert(isinstance(app_error, ARObject))
        assert(isinstance(app_error, Identifiable))
        assert(isinstance(app_error, MultilanguageReferrable))
        assert(isinstance(app_error, Referrable))
        assert(isinstance(app_error, ApplicationError))

        assert(app_error.parent == ar_root)
        assert(app_error.short_name == "ApplicationError")

