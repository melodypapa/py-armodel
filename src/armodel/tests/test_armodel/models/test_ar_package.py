""" Test AR Package """
import pytest

from ....models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import ApplicationPrimitiveDataType, ApplicationRecordDataType
from ....models.M2.MSR.AsamHdo.BaseTypes import SwBaseType
from ....models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import PackageableElement
from ....models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import CollectableElement
from ....models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable, MultilanguageReferrable, Referrable
from ....models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ....models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import ImplementationDataType
from ....models.M2.AUTOSARTemplates.SWComponentTemplate.Components import ApplicationSwComponentType, AtomicSwComponentType
from ....models.M2.AUTOSARTemplates.SWComponentTemplate.Components import EcuAbstractionSwComponentType, SwComponentType
from ....models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from ....models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import DataTypeMappingSet
from ....models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement
from ....models.M2.MSR.AsamHdo.ComputationMethod import CompuMethod
from ....models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import ClientServerInterface, DataInterface, PortInterface
from ....models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import SenderReceiverInterface
from ....models.M2.AUTOSARTemplates.SWComponentTemplate.Components import ServiceSwComponentType
from ....models.M2.AUTOSARTemplates.SWComponentTemplate.Components import CompositionSwComponentType


class TestAUTOSAR:

    def test_autosar_singleton_exception(self):
        AUTOSAR.getInstance()
        with pytest.raises(Exception) as err:
            AUTOSAR()
        assert (str(err.value) == "The AUTOSAR is singleton!")

    def test_cannot_find_element(self):
        document = AUTOSAR.getInstance()
        # with pytest.raises(Exception) as err:
        #    document.find("/sw_package/not_found")
        # assert(str(err.value) ==
        #       "The sw_package of reference </sw_package/not_found> does not exist.")
        assert (document.find("/sw_package/not_found") is None)

    def test_autosar(self):
        document = AUTOSAR.getInstance()
        document.clear()
        assert (isinstance(document, CollectableElement))
        assert (isinstance(document, AUTOSAR))
        assert (len(document.getARPackages()) == 0)
        assert (document.schema_location is None)
        assert (document.full_name == "")

    def test_create_autosar_package(self):
        document = AUTOSAR.getInstance()
        ar_package = document.createARPackage("sw_package")
        assert ("sw_package" == ar_package.short_name)
        assert (len(document.getARPackages()) == 1)
        assert (document.getARPackages()[0] == ar_package)

        ar_package = document.find("/sw_package")
        assert ("sw_package" == ar_package.short_name)

        assert (isinstance(ar_package, ARObject))
        assert (isinstance(ar_package, Identifiable))
        assert (isinstance(ar_package, Referrable))
        assert (isinstance(ar_package, MultilanguageReferrable))


class TestARPackage:

    def test_create_autosar_package(self):
        document = AUTOSAR.getInstance()
        ar_package_level1 = document.createARPackage("package_level1")
        assert (ar_package_level1.short_name == "package_level1")
        assert (ar_package_level1.full_name == "/package_level1")
        assert (len(ar_package_level1.getARPackages()) == 0)

        ar_find_package = document.find("/package_level1")
        assert (ar_find_package == ar_package_level1)
        assert (ar_find_package.short_name == 'package_level1')

        ar_package_level2 = ar_package_level1.createARPackage("package_level2")
        assert (ar_package_level2.short_name == 'package_level2')
        assert (ar_package_level2.full_name == "/package_level1/package_level2")
        assert (len(ar_package_level1.getARPackages()) == 1)
        assert (ar_package_level1.getARPackages()[0] == ar_package_level2)

        ar_find_package = document.find("/package_level1/package_level2")
        assert (ar_find_package == ar_package_level2)
        assert (ar_find_package.short_name == "package_level2")

    def test_createEcuAbstractionSwComponentType(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        sw_component_type = ar_root.createEcuAbstractionSwComponentType("ecu_abstract_sw_component")
        assert (sw_component_type.short_name == "ecu_abstract_sw_component")
        assert (isinstance(sw_component_type, EcuAbstractionSwComponentType))

        find_component_type = document.find("/AUTOSAR/ecu_abstract_sw_component")
        assert (find_component_type == sw_component_type)
        assert (find_component_type.short_name == "ecu_abstract_sw_component")

    def test_createApplicationSwComponentType(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        sw_component_type = ar_root.createApplicationSwComponentType(
            "application_sw_component")
        assert (sw_component_type.short_name == "application_sw_component")

        assert (isinstance(sw_component_type, ARElement))
        assert (isinstance(sw_component_type, AtomicSwComponentType))
        assert (isinstance(sw_component_type, CollectableElement))
        assert (isinstance(sw_component_type, Identifiable))
        assert (isinstance(sw_component_type, MultilanguageReferrable))
        assert (isinstance(sw_component_type, PackageableElement))
        assert (isinstance(sw_component_type, Referrable))
        assert (isinstance(sw_component_type, SwComponentType))
        assert (isinstance(sw_component_type, ApplicationSwComponentType))

        find_component_type = document.find(
            "/AUTOSAR/application_sw_component")
        assert (find_component_type == sw_component_type)
        assert (find_component_type.short_name == "application_sw_component")

    def test_createServiceSwComponentType(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        sw_component_type = ar_root.createServiceSwComponentType(
            "service_sw_component")
        assert (sw_component_type.short_name == "service_sw_component")

        assert (isinstance(sw_component_type, ARElement))
        assert (isinstance(sw_component_type, AtomicSwComponentType))
        assert (isinstance(sw_component_type, CollectableElement))
        assert (isinstance(sw_component_type, Identifiable))
        assert (isinstance(sw_component_type, MultilanguageReferrable))
        assert (isinstance(sw_component_type, PackageableElement))
        assert (isinstance(sw_component_type, Referrable))
        assert (isinstance(sw_component_type, SwComponentType))
        assert (isinstance(sw_component_type, ServiceSwComponentType))

        find_component_type = document.find("/AUTOSAR/service_sw_component")
        assert (find_component_type == sw_component_type)
        assert (find_component_type.short_name == "service_sw_component")

    def test_createCompositionSwComponentType(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        sw_component_type = ar_root.createCompositionSwComponentType(
            "composition_sw_component")
        assert (sw_component_type.short_name == "composition_sw_component")

        assert (isinstance(sw_component_type, ARElement))
        assert (isinstance(sw_component_type, CollectableElement))
        assert (isinstance(sw_component_type, Identifiable))
        assert (isinstance(sw_component_type, MultilanguageReferrable))
        assert (isinstance(sw_component_type, PackageableElement))
        assert (isinstance(sw_component_type, Referrable))
        assert (isinstance(sw_component_type, SwComponentType))
        assert (isinstance(sw_component_type, CompositionSwComponentType))

        find_component_type = document.find(
            "/AUTOSAR/composition_sw_component")
        assert (find_component_type == sw_component_type)
        assert (find_component_type.short_name == "composition_sw_component")

    def test_createSenderReceiverInterface(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        instance_if = ar_root.createSenderReceiverInterface(
            "sender_receiver_interface")
        assert (instance_if.short_name == "sender_receiver_interface")

        assert (isinstance(instance_if, ARElement))
        assert (isinstance(instance_if, CollectableElement))
        assert (isinstance(instance_if, DataInterface))
        assert (isinstance(instance_if, Identifiable))
        assert (isinstance(instance_if, MultilanguageReferrable))
        assert (isinstance(instance_if, PackageableElement))
        assert (isinstance(instance_if, PortInterface))
        assert (isinstance(instance_if, Referrable))
        assert (isinstance(instance_if, SenderReceiverInterface))

        find_component = document.find("/AUTOSAR/sender_receiver_interface")
        assert (find_component == instance_if)
        assert (find_component.short_name == "sender_receiver_interface")

        assert (len(ar_root.getSenderReceiverInterfaces()) == 1)
        assert (ar_root.getSenderReceiverInterfaces()[0] == instance_if)
        assert (ar_root.getSenderReceiverInterfaces()[
                0].short_name == "sender_receiver_interface")

    def test_createClientServerInterface(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        instance_if = ar_root.createClientServerInterface(
            "client_server_interface")
        assert (instance_if.short_name == "client_server_interface")
        assert (isinstance(instance_if, ClientServerInterface))

        find_component = document.find("/AUTOSAR/client_server_interface")
        assert (find_component == instance_if)
        assert (find_component.short_name == "client_server_interface")

        assert (len(ar_root.getClientServerInterfaces()) == 1)
        assert (ar_root.getClientServerInterfaces()[0] == instance_if)
        assert (ar_root.getClientServerInterfaces()[
                0].short_name == "client_server_interface")

    def test_createApplicationPrimitiveDataType(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        data_type = ar_root.createApplicationPrimitiveDataType(
            "application_primitive_data_type")
        assert (data_type.short_name == "application_primitive_data_type")
        assert (isinstance(data_type, ApplicationPrimitiveDataType))

        find_component = document.find(
            "/AUTOSAR/application_primitive_data_type")
        assert (find_component == data_type)
        assert (find_component.short_name == "application_primitive_data_type")

        assert (len(ar_root.getApplicationPrimitiveDataTypes()) == 1)
        assert (ar_root.getApplicationPrimitiveDataTypes()[0] == data_type)
        assert (ar_root.getApplicationPrimitiveDataTypes()[
                0].short_name == "application_primitive_data_type")

    def test_createApplicationRecordDataType(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        data_type = ar_root.createApplicationRecordDataType(
            "application_record_data_type")
        assert (data_type.short_name == "application_record_data_type")
        assert (isinstance(data_type, ApplicationRecordDataType))

        find_component = document.find("/AUTOSAR/application_record_data_type")
        assert (find_component == data_type)
        assert (find_component.short_name == "application_record_data_type")

    def test_createImplementationDataType(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        data_type = ar_root.createImplementationDataType(
            "implementation_data_type")
        assert (data_type.short_name == "implementation_data_type")
        assert (isinstance(data_type, ImplementationDataType))

        find_component = document.find("/AUTOSAR/implementation_data_type")
        assert (find_component == data_type)
        assert (find_component.short_name == "implementation_data_type")

        assert (len(ar_root.getImplementationDataTypes()) == 1)
        assert (ar_root.getImplementationDataTypes()[0] == data_type)
        assert (ar_root.getImplementationDataTypes()[
                0].short_name == "implementation_data_type")

    def test_createSwBaseType(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        data_type = ar_root.createSwBaseType("sw_base_type")
        assert (data_type.short_name == "sw_base_type")
        assert (isinstance(data_type, SwBaseType))

        find_component = document.find("/AUTOSAR/sw_base_type")
        assert (find_component == data_type)
        assert (find_component.short_name == "sw_base_type")

        assert (len(ar_root.getSwBaseTypes()) == 1)
        assert (ar_root.getSwBaseTypes()[0] == data_type)
        assert (ar_root.getSwBaseTypes()[0].short_name == "sw_base_type")

    def test_createDataTypeMappingSet(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        mapping_set = ar_root.createDataTypeMappingSet("data_type_mapping_set")
        assert (mapping_set.short_name == "data_type_mapping_set")
        assert (isinstance(mapping_set, DataTypeMappingSet))

        find_component = document.find("/AUTOSAR/data_type_mapping_set")
        assert (find_component == mapping_set)
        assert (find_component.short_name == "data_type_mapping_set")

        assert (len(ar_root.getDataTypeMappingSets()) == 1)
        assert (ar_root.getDataTypeMappingSets()[0] == mapping_set)
        assert (ar_root.getDataTypeMappingSets()[
                0].short_name == "data_type_mapping_set")

    def test_createCompuMethod(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        compu_method = ar_root.createCompuMethod("compu_method")
        assert (compu_method.short_name == "compu_method")
        assert (isinstance(compu_method, CompuMethod))

        find_component = document.find("/AUTOSAR/compu_method")
        assert (find_component == compu_method)
        assert (find_component.short_name == "compu_method")

        assert (len(ar_root.getCompuMethods()) == 1)
        assert (ar_root.getCompuMethods()[0] == compu_method)
        assert (ar_root.getCompuMethods()[0].short_name == "compu_method")

    def test_getSwComponentTypes(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")

        assert (len(ar_root.getSwComponentTypes()) == 4)
        assert (len(ar_root.getAtomicSwComponentTypes()) == 3)
        assert (len(ar_root.getCompositionSwComponentTypes()) == 1)
