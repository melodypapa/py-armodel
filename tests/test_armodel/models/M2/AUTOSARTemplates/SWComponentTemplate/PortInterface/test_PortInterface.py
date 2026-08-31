import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import ServiceProviderEnum
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import AtpBlueprintable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable, MultilanguageReferrable, Referrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import AtpPrototype, AutosarDataPrototype, DataPrototype, VariableDataPrototype
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    ApplicationError,
    ArgumentDataPrototype,
    ClientServerInterface,
    ClientServerInterfaceMapping,
    ClientServerOperation,
    DataInterface,
    NvDataInterface,
    ParameterInterface,
    PortInterface,
    PortInterfaceMapping,
    SenderReceiverInterface,
)


class Test_M2_AUTOSARTemplates_SWComponentTemplate_PortInterface:

    def test_PortInterfaceMapping_abstract(self):
        """
        PortInterfaceMapping is abstract (Table 4.20) — direct instantiation fails.

        Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.20, p.119 (R23-11)
        """
        with pytest.raises(TypeError) as err:
            PortInterfaceMapping(AUTOSAR.getInstance(), "PortInterfaceMapping")
        assert str(err.value) == "PortInterfaceMapping is an abstract class."

    def test_PortInterfaceMapping_concrete_subclass_inheritance(self):
        """
        Concrete subclasses derive from PortInterfaceMapping (Base chain:
        ARObject, AtpBlueprint, AtpBlueprintable, Identifiable, MultilanguageReferrable,
        Referrable — Python base = AtpBlueprintable role branch).

        Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.20, p.119 (R23-11)
        """
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        mapping = ClientServerInterfaceMapping(ar_root, "cs_mapping")

        assert isinstance(mapping, ARObject)
        assert isinstance(mapping, AtpBlueprintable)
        assert isinstance(mapping, Identifiable)
        assert isinstance(mapping, MultilanguageReferrable)
        assert isinstance(mapping, Referrable)
        assert isinstance(mapping, PortInterfaceMapping)

        assert mapping.parent == ar_root
        assert mapping.short_name == "cs_mapping"

    def test_PortInterface(self):
        with pytest.raises(TypeError) as err:
            PortInterface(AUTOSAR.getInstance(), "PortInterface")
        assert str(err.value) == "PortInterface is an abstract class."

    def test_DataInterface(self):
        with pytest.raises(TypeError) as err:
            DataInterface(AUTOSAR.getInstance(), "DataInterface")
        assert str(err.value) == "DataInterface is an abstract class."

    def test_NvDataInterface(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        data_if = NvDataInterface(ar_root, "NvDataInterface")

        assert isinstance(data_if, ARObject)
        assert isinstance(data_if, AtpType)
        assert isinstance(data_if, DataInterface)
        assert isinstance(data_if, Identifiable)
        assert isinstance(data_if, MultilanguageReferrable)
        assert isinstance(data_if, PortInterface)
        assert isinstance(data_if, Referrable)
        assert isinstance(data_if, NvDataInterface)

        assert data_if.parent == ar_root
        assert data_if.short_name == "NvDataInterface"

    def test_ParameterInterface(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        data_if = ParameterInterface(ar_root, "ParameterInterface")

        assert isinstance(data_if, ARObject)
        assert isinstance(data_if, AtpType)
        assert isinstance(data_if, DataInterface)
        assert isinstance(data_if, Identifiable)
        assert isinstance(data_if, MultilanguageReferrable)
        assert isinstance(data_if, PortInterface)
        assert isinstance(data_if, Referrable)
        assert isinstance(data_if, ParameterInterface)

        assert data_if.parent == ar_root
        assert data_if.short_name == "ParameterInterface"

    def test_SenderReceiverInterface(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        sr_if = SenderReceiverInterface(ar_root, "sr_if")

        assert isinstance(sr_if, ARObject)
        assert isinstance(sr_if, AtpType)
        assert isinstance(sr_if, DataInterface)
        assert isinstance(sr_if, Identifiable)
        assert isinstance(sr_if, MultilanguageReferrable)
        assert isinstance(sr_if, PortInterface)
        assert isinstance(sr_if, Referrable)
        assert isinstance(sr_if, SenderReceiverInterface)

        assert sr_if.getShortName() == "sr_if"
        assert sr_if.parent == ar_root
        assert len(sr_if.getDataElements()) == 0

        element = sr_if.createDataElement("element")
        assert isinstance(element, VariableDataPrototype)
        assert element.getShortName() == "element"
        assert len(sr_if.getDataElements()) == 1

        element2 = sr_if.getDataElement("element")
        assert element == element2

    def test_ArgumentDataPrototype(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        prototype = ArgumentDataPrototype(ar_root, "ArgumentDataPrototype")

        assert isinstance(prototype, ARObject)
        assert isinstance(prototype, AtpBlueprintable)
        assert isinstance(prototype, AtpPrototype)
        assert isinstance(prototype, AutosarDataPrototype)
        assert isinstance(prototype, DataPrototype)
        assert isinstance(prototype, Identifiable)
        assert isinstance(prototype, MultilanguageReferrable)
        assert isinstance(prototype, Referrable)
        assert isinstance(prototype, ArgumentDataPrototype)

        assert prototype.getParent() == ar_root
        assert prototype.getShortName() == "ArgumentDataPrototype"
        assert prototype.getDirection() is None
        assert prototype.getServerArgumentImplPolicy() is None

    def test_ApplicationError(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        app_error = ApplicationError(ar_root, "ApplicationError")

        assert isinstance(app_error, ARObject)
        assert isinstance(app_error, Identifiable)
        assert isinstance(app_error, MultilanguageReferrable)
        assert isinstance(app_error, Referrable)
        assert isinstance(app_error, ApplicationError)

        assert app_error.parent == ar_root
        assert app_error.short_name == "ApplicationError"

    def test_ClientServerOperation(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        operation = ClientServerOperation(ar_root, "client_server_operation")
        assert isinstance(operation, ARObject)
        # assert (isinstance(operation, AtpClassifier))
        assert isinstance(operation, AtpBlueprintable)
        assert isinstance(operation, Identifiable)
        assert isinstance(operation, MultilanguageReferrable)
        assert isinstance(operation, Referrable)
        assert isinstance(operation, ClientServerOperation)
        assert operation.short_name == "client_server_operation"

        assert operation.getDiagArgIntegrity() is None

        prototype = operation.createArgumentDataPrototype("argument_data_prototype1")
        assert prototype.short_name == "argument_data_prototype1"

        assert len(operation.getArguments()) == 1
        assert operation.getArguments()[0] == prototype

        # creating an existing argument returns the existing instance
        prototype2 = operation.createArgumentDataPrototype("argument_data_prototype1")
        assert prototype2 == prototype
        assert len(operation.getArguments()) == 1

        refType = RefType()
        refType.dest = "APPLICATION-ERROR"
        refType.value = "/AUTOSAR_NvM/PortInterfaces/NvMService/E_NOT_OK"
        operation.addPossibleErrorRef(refType)

        assert len(operation.getPossibleErrorRefs()) == 1
        assert operation.getPossibleErrorRefs()[0] == refType

    def test_ClientServerOperation_diagArgIntegrity(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        operation = ClientServerOperation(ar_root, "client_server_operation")

        bool_true = Boolean()
        bool_true.value = True
        assert operation.setDiagArgIntegrity(bool_true) == operation
        assert operation.getDiagArgIntegrity() == bool_true

        # None is a no-op: existing value is preserved
        operation.setDiagArgIntegrity(None)
        assert operation.getDiagArgIntegrity() == bool_true

        bool_false = Boolean()
        bool_false.value = False
        operation.setDiagArgIntegrity(bool_false)
        assert operation.getDiagArgIntegrity() == bool_false

    def test_ClientServerInterface(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        cs_if = ClientServerInterface(ar_root, "client_server_interface")
        assert isinstance(cs_if, ARObject)
        assert isinstance(cs_if, AtpType)
        assert isinstance(cs_if, Identifiable)
        assert isinstance(cs_if, MultilanguageReferrable)
        assert isinstance(cs_if, PortInterface)
        assert isinstance(cs_if, Referrable)
        assert cs_if.getOperations() == []
        assert cs_if.getPossibleErrors() == []

        element = cs_if.createOperation("operation")
        assert isinstance(element, ClientServerOperation)
        assert element.short_name == "operation"
        assert len(cs_if.getOperations()) == 1

        element2 = cs_if.getOperations()[0]
        assert element == element2

        element = cs_if.createApplicationError("error")
        assert isinstance(element, ApplicationError)
        assert element.short_name == "error"
        assert len(cs_if.getPossibleErrors()) == 1

        element2 = cs_if.getPossibleErrors()[0]
        assert element == element2

    def test_PortInterface_isService(self):
        """PortInterface.isService: default None, setter chains, value round-trips, None no-op."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        pi = NvDataInterface(ar_root, "NvDataInterface")

        assert pi.getIsService() is None

        is_service = Boolean()
        is_service.setValue("true")
        assert pi.setIsService(is_service) is pi
        assert pi.getIsService() is is_service
        assert pi.getIsService().getValue() is True

        # None is a no-op: existing value is preserved
        pi.setIsService(None)
        assert pi.getIsService() is is_service

        is_service_false = Boolean()
        is_service_false.setValue("false")
        pi.setIsService(is_service_false)
        assert pi.getIsService() is is_service_false

    def test_PortInterface_serviceKind(self):
        """PortInterface.serviceKind: default None, setter chains, value round-trips, None no-op."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        pi = NvDataInterface(ar_root, "NvDataInterface")

        assert pi.getServiceKind() is None

        service_kind = ServiceProviderEnum().setValue(ServiceProviderEnum.COM_MANAGER)
        assert pi.setServiceKind(service_kind) is pi
        assert pi.getServiceKind() is service_kind
        assert pi.getServiceKind().getValue() == "comManager"

        # None is a no-op: existing value is preserved
        pi.setServiceKind(None)
        assert pi.getServiceKind() is service_kind

        service_kind2 = ServiceProviderEnum().setValue(ServiceProviderEnum.DEFAULT_ERROR_TRACER)
        pi.setServiceKind(service_kind2)
        assert pi.getServiceKind() is service_kind2
