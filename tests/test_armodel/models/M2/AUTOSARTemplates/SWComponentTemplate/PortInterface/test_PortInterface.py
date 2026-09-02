import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import TextValueSpecification
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import ServiceProviderEnum
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import AtpBlueprintable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable, MultilanguageReferrable, Referrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import AtpPrototype, AutosarDataPrototype, DataPrototype, VariableDataPrototype
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    ApplicationError,
    ArgumentDataPrototype,
    ClientServerInterface,
    ClientServerInterfaceMapping,
    ClientServerOperation,
    DataInterface,
    MetaDataItem,
    MetaDataItemSet,
    ModeInterfaceMapping,
    NvDataInterface,
    ParameterInterface,
    PortInterface,
    PortInterfaceMapping,
    PortInterfaceMappingSet,
    SenderReceiverInterface,
    TriggerInterfaceMapping,
    VariableAndParameterInterfaceMapping,
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


class TestPortInterfaceMappingSet:
    """
    Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.19, p.119 (R23-11)
    portInterfaceMapping is a * aggr of PortInterfaceMapping (concrete subclasses).
    """

    def test_initialization(self):
        obj = PortInterfaceMappingSet(AUTOSAR.getInstance(), "pim_set")

        assert obj.parent == AUTOSAR.getInstance()
        assert obj.short_name == "pim_set"
        assert obj.getPortInterfaceMappings() == []

        # Base chain (Table 4.19): most-derived model base = ARElement
        assert isinstance(obj, ARElement)
        assert isinstance(obj, ARObject)
        assert isinstance(obj, Identifiable)
        assert isinstance(obj, MultilanguageReferrable)
        assert isinstance(obj, Referrable)

    def test_create_mappings(self):
        ar_root = AUTOSAR.getInstance()
        obj = PortInterfaceMappingSet(ar_root, "pim_set")

        cs = obj.createClientServerInterfaceMapping("cs_mapping")
        assert isinstance(cs, ClientServerInterfaceMapping)
        assert cs.parent is obj
        assert cs.short_name == "cs_mapping"

        vp = obj.createVariableAndParameterInterfaceMapping("vp_mapping")
        assert isinstance(vp, VariableAndParameterInterfaceMapping)

        mode = obj.createModeInterfaceMapping("mode_mapping")
        assert isinstance(mode, ModeInterfaceMapping)

        trig = obj.createTriggerInterfaceMapping("trig_mapping")
        assert isinstance(trig, TriggerInterfaceMapping)

        mappings = obj.getPortInterfaceMappings()
        assert len(mappings) == 4
        assert mappings[0] is cs
        assert mappings[1] is vp
        assert mappings[2] is mode
        assert mappings[3] is trig

    def test_create_duplicate_returns_existing(self):
        ar_root = AUTOSAR.getInstance()
        obj = PortInterfaceMappingSet(ar_root, "pim_set")

        first = obj.createClientServerInterfaceMapping("cs_mapping")
        second = obj.createClientServerInterfaceMapping("cs_mapping")
        assert second is first
        assert len(obj.getPortInterfaceMappings()) == 1

    def test_polymorphic_list(self):
        """
        All created mappings are PortInterfaceMapping subtypes (Table 4.20 abstract base).
        """
        ar_root = AUTOSAR.getInstance()
        obj = PortInterfaceMappingSet(ar_root, "pim_set")

        obj.createClientServerInterfaceMapping("cs_mapping")
        obj.createVariableAndParameterInterfaceMapping("vp_mapping")

        for mapping in obj.getPortInterfaceMappings():
            assert isinstance(mapping, PortInterfaceMapping)


class TestMetaDataItem:
    """
    Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.4, p.98 (R23-11)
    length is a 0..1 attr (PositiveInteger); metaDataItemType is a 0..1 aggr (TextValueSpecification).
    """

    def test_initialization(self):
        obj = MetaDataItem()

        assert obj.getLength() is None
        assert obj.getMetaDataItemType() is None

        # Base chain (Table 4.4): most-derived model base = ARObject (no SHORT-NAME)
        assert isinstance(obj, ARObject)
        assert not isinstance(obj, Referrable)

    def test_length_round_trip(self):
        obj = MetaDataItem()

        length = PositiveInteger().setValue(8)
        assert obj.setLength(length) is obj
        assert obj.getLength() is length

    def test_length_none_no_op(self):
        obj = MetaDataItem()
        obj.setLength(PositiveInteger().setValue(8))

        obj.setLength(None)

        assert obj.getLength() is not None
        assert obj.getLength().getValue() == 8

    def test_meta_data_item_type_round_trip(self):
        obj = MetaDataItem()

        value_spec = TextValueSpecification()
        assert obj.setMetaDataItemType(value_spec) is obj
        assert obj.getMetaDataItemType() is value_spec

    def test_meta_data_item_type_none_no_op(self):
        obj = MetaDataItem()
        obj.setMetaDataItemType(TextValueSpecification())

        obj.setMetaDataItemType(None)

        assert obj.getMetaDataItemType() is not None


class TestMetaDataItemSet:
    """
    Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.5, p.99 (R23-11)
    dataElement is a * ref (VariableDataPrototype); metaDataItem is a * ordered aggr of MetaDataItem.
    """

    def test_initialization(self):
        obj = MetaDataItemSet()

        assert obj.getDataElementRefs() == []
        assert obj.getMetaDataItems() == []

        # Base chain (Table 4.5): most-derived model base = ARObject (no SHORT-NAME)
        assert isinstance(obj, ARObject)
        assert not isinstance(obj, Referrable)

    def test_add_data_element_refs(self):
        obj = MetaDataItemSet()

        ref1 = RefType()
        ref1.setValue("/pkg/sr_iface/de1")
        ref2 = RefType()
        ref2.setValue("/pkg/sr_iface/de2")

        assert obj.addDataElementRef(ref1) is obj
        obj.addDataElementRef(ref2)

        refs = obj.getDataElementRefs()
        assert len(refs) == 2
        assert refs[0] is ref1
        assert refs[0].getValue() == "/pkg/sr_iface/de1"
        assert refs[1] is ref2
        assert refs[1].getValue() == "/pkg/sr_iface/de2"

    def test_add_meta_data_items_ordered(self):
        obj = MetaDataItemSet()

        item1 = MetaDataItem()
        item2 = MetaDataItem()

        assert obj.addMetaDataItem(item1) is obj
        obj.addMetaDataItem(item2)

        items = obj.getMetaDataItems()
        assert len(items) == 2
        # Table 4.5 metaDataItem is ordered — insertion order is preserved
        assert items[0] is item1
        assert items[1] is item2
