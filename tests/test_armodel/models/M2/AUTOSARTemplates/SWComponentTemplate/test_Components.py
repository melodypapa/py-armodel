"""
This module contains comprehensive tests for the Components module in SWComponentTemplate.
Tests cover all classes and methods in the __init__.py file to achieve 100% test coverage.
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import (
    AbstractProvidedPortPrototype,
    AbstractRequiredPortPrototype,
    ApplicationSwComponentType,
    AtomicSwComponentType,
    ComplexDeviceDriverSwComponentType,
    EcuAbstractionSwComponentType,
    NvBlockSwComponentType,
    PortGroup,
    PortPrototype,
    PPortPrototype,
    PRPortPrototype,
    RPortPrototype,
    SensorActuatorSwComponentType,
    ServiceProxySwComponentType,
    ServiceSwComponentType,
    SwComponentType,
    SymbolProps,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition import (
    CompositionSwComponentType,
)


class TestSymbolProps:
    """Test class for SymbolProps class."""

    def test_symbol_props_initialization(self):
        """Test SymbolProps initialization."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        symbol_props = SymbolProps(ar_root, "TestSymbolProps")

        assert symbol_props.parent == ar_root
        assert symbol_props.short_name == "TestSymbolProps"


class TestPortPrototype:
    """Test class for PortPrototype class."""

    def test_abstract_class_cannot_be_instantiated(self):
        """Test that PortPrototype abstract class cannot be instantiated directly."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        with pytest.raises(TypeError, match="PortPrototype is an abstract class"):
            PortPrototype(ar_root, "TestPortPrototype")

    def test_concrete_subclass_initialization(self):
        """Test that a concrete subclass of PortPrototype can be instantiated."""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import (
            PRPortPrototype,
        )

        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        port_proto = PRPortPrototype(ar_root, "TestPortPrototype")

        assert port_proto.parent == ar_root
        assert port_proto.short_name == "TestPortPrototype"
        assert port_proto.clientServerAnnotations == []
        assert port_proto.delegatedPortAnnotation is None
        assert port_proto.ioHwAbstractionServerAnnotations == []
        assert port_proto.modePortAnnotations == []
        assert port_proto.nvDataPortAnnotations == []
        assert port_proto.parameterPortAnnotations == []
        assert port_proto.senderReceiverAnnotations == []
        assert port_proto.triggerPortAnnotations == []

        # Test clientServerAnnotations methods
        cs_annotation = "test_cs_annotation"
        port_proto.addClientServerAnnotation(cs_annotation)
        assert cs_annotation in port_proto.getClientServerAnnotations()

        # Test delegatedPortAnnotation methods
        del_port_annotation = "test_del_port_annotation"
        port_proto.setDelegatedPortAnnotation(del_port_annotation)
        assert port_proto.getDelegatedPortAnnotation() == del_port_annotation

        # Test ioHwAbstractionServerAnnotations methods
        io_hw_annotation = "test_io_hw_annotation"
        port_proto.addIoHwAbstractionServerAnnotation(io_hw_annotation)
        assert io_hw_annotation in port_proto.getIoHwAbstractionServerAnnotations()

        # Test modePortAnnotations methods
        mode_annotation = "test_mode_annotation"
        port_proto.addModePortAnnotation(mode_annotation)
        assert mode_annotation in port_proto.getModePortAnnotations()

        # Test nvDataPortAnnotations methods
        nv_annotation = "test_nv_annotation"
        port_proto.addNvDataPortAnnotation(nv_annotation)
        assert nv_annotation in port_proto.getNvDataPortAnnotations()

        # Test parameterPortAnnotations methods
        param_annotation = "test_param_annotation"
        port_proto.addParameterPortAnnotation(param_annotation)
        assert param_annotation in port_proto.getParameterPortAnnotations()

        # Test senderReceiverAnnotations methods
        sr_annotation = "test_sr_annotation"
        port_proto.addSenderReceiverAnnotation(sr_annotation)
        assert sr_annotation in port_proto.getSenderReceiverAnnotations()

        # Test triggerPortAnnotations methods
        trigger_annotation = "test_trigger_annotation"
        port_proto.addTriggerPortAnnotation(trigger_annotation)
        assert trigger_annotation in port_proto.getTriggerPortAnnotations()


class TestAbstractProvidedPortPrototype:
    """Test class for AbstractProvidedPortPrototype class."""

    def test_abstract_class_cannot_be_instantiated(self):
        """Test that AbstractProvidedPortPrototype abstract class cannot be instantiated directly."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        with pytest.raises(TypeError, match="AbstractProvidedPortPrototype is an abstract class"):
            AbstractProvidedPortPrototype(ar_root, "TestAbstractProvidedPortPrototype")

    def test_concrete_subclass_initialization(self):
        """Test that a concrete subclass of AbstractProvidedPortPrototype can be instantiated."""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import (
            PPortPrototype,
        )

        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        provided_port = PPortPrototype(ar_root, "TestAbstractProvidedPortPrototype")

        assert provided_port.parent == ar_root
        assert provided_port.short_name == "TestAbstractProvidedPortPrototype"
        assert provided_port.clientServerAnnotations == []
        assert provided_port.delegatedPortAnnotation is None
        assert provided_port.ioHwAbstractionServerAnnotations == []
        assert provided_port.modePortAnnotations == []
        assert provided_port.nvDataPortAnnotations == []
        assert provided_port.parameterPortAnnotations == []
        assert provided_port.senderReceiverAnnotations == []
        assert provided_port.triggerPortAnnotations == []
        assert provided_port.providedComSpecs == []

        # Test providedComSpecs methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
            RefType,
        )
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import (
            NonqueuedSenderComSpec,
        )
        com_spec = NonqueuedSenderComSpec()
        # Set required fields to pass validation
        data_ref = RefType()
        data_ref.setDest("VARIABLE-DATA-PROTOTYPE")
        com_spec.setDataElementRef(data_ref)
        # Add to provided specs (this internally calls validation)
        provided_port.addProvidedComSpec(com_spec)
        assert com_spec in provided_port.getProvidedComSpecs()


class TestAbstractRequiredPortPrototype:
    """Test class for AbstractRequiredPortPrototype class."""

    def test_abstract_class_cannot_be_instantiated(self):
        """Test that AbstractRequiredPortPrototype abstract class cannot be instantiated directly."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        with pytest.raises(TypeError, match="AbstractRequiredPortPrototype is an abstract class"):
            AbstractRequiredPortPrototype(ar_root, "TestAbstractRequiredPortPrototype")

    def test_concrete_subclass_initialization(self):
        """Test that a concrete subclass of AbstractRequiredPortPrototype can be instantiated."""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import (
            RPortPrototype,
        )

        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        required_port = RPortPrototype(ar_root, "TestAbstractRequiredPortPrototype")

        assert required_port.parent == ar_root
        assert required_port.short_name == "TestAbstractRequiredPortPrototype"
        assert required_port.clientServerAnnotations == []
        assert required_port.delegatedPortAnnotation is None
        assert required_port.ioHwAbstractionServerAnnotations == []
        assert required_port.modePortAnnotations == []
        assert required_port.nvDataPortAnnotations == []
        assert required_port.parameterPortAnnotations == []
        assert required_port.senderReceiverAnnotations == []
        assert required_port.triggerPortAnnotations == []
        assert required_port.requiredComSpecs == []

        # Test requiredComSpecs methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
            RefType,
        )
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import (
            ClientComSpec,
        )
        com_spec = ClientComSpec()
        # Set required fields for validation
        operation_ref = RefType()
        operation_ref.setDest("CLIENT-SERVER-OPERATION")
        com_spec.setOperationRef(operation_ref)
        # Add to required specs
        required_port.addRequiredComSpec(com_spec)
        assert com_spec in required_port.getRequiredComSpecs()


class TestPPortPrototype:
    """Test class for PPortPrototype class."""

    def test_p_port_prototype_initialization(self):
        """Test PPortPrototype initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        p_port = PPortPrototype(ar_root, "TestPPortPrototype")

        assert p_port.parent == ar_root
        assert p_port.short_name == "TestPPortPrototype"
        assert p_port.clientServerAnnotations == []
        assert p_port.delegatedPortAnnotation is None
        assert p_port.ioHwAbstractionServerAnnotations == []
        assert p_port.modePortAnnotations == []
        assert p_port.nvDataPortAnnotations == []
        assert p_port.parameterPortAnnotations == []
        assert p_port.senderReceiverAnnotations == []
        assert p_port.triggerPortAnnotations == []
        assert p_port.providedComSpecs == []
        assert p_port.providedInterfaceTRef is None

        # Test providedInterfaceTRef methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
            TRefType,
        )
        t_ref = TRefType()
        t_ref.setValue("/Interface/Ref")
        p_port.setProvidedInterfaceTRef(t_ref)
        assert p_port.getProvidedInterfaceTRef() == t_ref


class TestRPortPrototype:
    """Test class for RPortPrototype class."""

    def test_r_port_prototype_initialization(self):
        """Test RPortPrototype initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        r_port = RPortPrototype(ar_root, "TestRPortPrototype")

        assert r_port.parent == ar_root
        assert r_port.short_name == "TestRPortPrototype"
        assert r_port.clientServerAnnotations == []
        assert r_port.delegatedPortAnnotation is None
        assert r_port.ioHwAbstractionServerAnnotations == []
        assert r_port.modePortAnnotations == []
        assert r_port.nvDataPortAnnotations == []
        assert r_port.parameterPortAnnotations == []
        assert r_port.senderReceiverAnnotations == []
        assert r_port.triggerPortAnnotations == []
        assert r_port.requiredComSpecs == []
        assert r_port.mayBeUnconnected is None
        assert r_port.requiredInterfaceTRef is None

        # Test mayBeUnconnected methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
            ARBoolean,
        )
        may_be_unconnected = ARBoolean()
        may_be_unconnected.setValue(True)
        r_port.setMayBeUnconnected(may_be_unconnected)
        assert r_port.getMayBeUnconnected() == may_be_unconnected

        # Test requiredInterfaceTRef methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
            TRefType,
        )
        t_ref = TRefType()
        t_ref.setValue("/Interface/Ref")
        r_port.setRequiredInterfaceTRef(t_ref)
        assert r_port.getRequiredInterfaceTRef() == t_ref


class TestPRPortPrototype:
    """Test class for PRPortPrototype class."""

    def test_pr_port_prototype_initialization(self):
        """Test PRPortPrototype initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        pr_port = PRPortPrototype(ar_root, "TestPRPortPrototype")

        assert pr_port.parent == ar_root
        assert pr_port.short_name == "TestPRPortPrototype"
        assert pr_port.providedComSpecs == []
        assert pr_port.requiredComSpecs == []
        assert pr_port.providedRequiredInterface is None

        # Test providedComSpecs methods
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import (
            NonqueuedSenderComSpec,
        )
        provided_spec = NonqueuedSenderComSpec()
        pr_port.addProvidedComSpec(provided_spec)
        assert provided_spec in pr_port.getProvidedComSpecs()

        # Test requiredComSpecs methods
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import (
            ClientComSpec,
        )
        required_spec = ClientComSpec()
        pr_port.addRequiredComSpec(required_spec)
        assert required_spec in pr_port.getRequiredComSpecs()

        # Test providedRequiredInterface methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
            TRefType,
        )
        interface_ref = TRefType()
        interface_ref.setValue("/Interface/Ref")
        pr_port.setProvidedRequiredInterface(interface_ref)
        assert pr_port.getProvidedRequiredInterface() == interface_ref


class TestPortGroup:
    """Test class for PortGroup class."""

    def test_port_group_initialization(self):
        """Test PortGroup initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        port_group = PortGroup(ar_root, "TestPortGroup")

        assert port_group.parent == ar_root
        assert port_group.short_name == "TestPortGroup"
        assert port_group._inner_group_iref == []
        assert port_group._outer_port_ref == []

        # Test inner group IRef methods
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import (
            InnerPortGroupInCompositionInstanceRef,
        )
        iref = InnerPortGroupInCompositionInstanceRef()
        port_group.addInnerGroupIRef(iref)
        assert iref in port_group.getInnerGroupIRefs()

        # Test outer port ref methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
            RefType,
        )
        ref = RefType()
        ref.setValue("/Outer/Port/Ref")
        port_group.addOuterPortRef(ref)
        assert ref in port_group.getOuterPortRefs()


class TestSwComponentType:
    """Test class for SwComponentType abstract class."""

    def test_abstract_class_cannot_be_instantiated(self):
        """Test that SwComponentType abstract class cannot be instantiated directly."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        with pytest.raises(TypeError, match="SwComponentType is an abstract class"):
            SwComponentType(ar_root, "TestSwComponentType")

    def test_concrete_subclass_initialization(self):
        """Test that a concrete subclass of SwComponentType can be instantiated."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        comp_type = ApplicationSwComponentType(ar_root, "TestSwComponentType")

        assert comp_type.parent == ar_root
        assert comp_type.short_name == "TestSwComponentType"
        assert comp_type.ports == []
        assert comp_type.portGroups == []


class TestAtomicSwComponentType:
    """Test class for AtomicSwComponentType class."""

    def test_atomic_sw_component_type_initialization(self):
        """Test AtomicSwComponentType initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        # AtomicSwComponentType is marked as abstract with ABCMeta, but has no abstract methods
        # so it can actually be instantiated
        atomic_comp_type = AtomicSwComponentType(ar_root, "TestAtomicSwComponentType")

        assert atomic_comp_type.parent == ar_root
        assert atomic_comp_type.short_name == "TestAtomicSwComponentType"
        assert atomic_comp_type.ports == []
        assert atomic_comp_type.portGroups == []
        assert atomic_comp_type.internalBehavior is None
        assert atomic_comp_type.symbolProps is None


class TestEcuAbstractionSwComponentType:
    """Test class for EcuAbstractionSwComponentType class."""

    def test_ecu_abstraction_sw_component_type_initialization(self):
        """Test EcuAbstractionSwComponentType initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        comp_type = EcuAbstractionSwComponentType(ar_root, "TestEcuAbstractionSwComponentType")

        assert comp_type.parent == ar_root
        assert comp_type.short_name == "TestEcuAbstractionSwComponentType"
        assert comp_type.ports == []
        assert comp_type.portGroups == []
        assert comp_type.internalBehavior is None
        assert comp_type.symbolProps is None
        assert comp_type.hardwareElementRefs == []

        # Test hardwareElementRefs methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
            RefType,
        )
        ref = RefType()
        ref.setValue("/Hardware/Element")
        comp_type.addHardwareElementRefs(ref)
        assert ref in comp_type.getHardwareElementRefs()


class TestApplicationSwComponentType:
    """Test class for ApplicationSwComponentType class."""

    def test_application_sw_component_type_initialization(self):
        """Test ApplicationSwComponentType initialization."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        comp_type = ApplicationSwComponentType(ar_root, "TestApplicationSwComponentType")

        assert comp_type.parent == ar_root
        assert comp_type.short_name == "TestApplicationSwComponentType"
        assert comp_type.ports == []
        assert comp_type.portGroups == []
        assert comp_type.internalBehavior is None
        assert comp_type.symbolProps is None


class TestComplexDeviceDriverSwComponentType:
    """Test class for ComplexDeviceDriverSwComponentType class."""

    def test_complex_device_driver_sw_component_type_initialization(self):
        """Test ComplexDeviceDriverSwComponentType initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        comp_type = ComplexDeviceDriverSwComponentType(ar_root, "TestComplexDeviceDriverSwComponentType")

        assert comp_type.parent == ar_root
        assert comp_type.short_name == "TestComplexDeviceDriverSwComponentType"
        assert comp_type.ports == []
        assert comp_type.portGroups == []
        assert comp_type.internalBehavior is None
        assert comp_type.symbolProps is None
        assert comp_type.hardwareElementRefs == []

        # Test hardwareElementRefs methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
            RefType,
        )
        ref = RefType()
        ref.setValue("/Hardware/Element")
        comp_type.addHardwareElementRefs(ref)
        assert ref in comp_type.getHardwareElementRefs()


class TestNvBlockSwComponentType:
    """Test class for NvBlockSwComponentType class."""

    def test_nv_block_sw_component_type_initialization(self):
        """Test NvBlockSwComponentType initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        comp_type = NvBlockSwComponentType(ar_root, "TestNvBlockSwComponentType")

        assert comp_type.parent == ar_root
        assert comp_type.short_name == "TestNvBlockSwComponentType"
        assert comp_type.ports == []
        assert comp_type.portGroups == []
        assert comp_type.internalBehavior is None
        assert comp_type.symbolProps is None
        assert comp_type.bulkNvDataDescriptors == []
        assert comp_type.nvBlockDescriptors == []

        # Test bulkNvDataDescriptors methods
        bulk_desc = "test_bulk_desc"
        comp_type.addBulkNvDataDescriptor(bulk_desc)
        assert bulk_desc in comp_type.getBulkNvDataDescriptors()

        # Test nvBlockDescriptors methods
        block_desc = "test_block_desc"
        comp_type.setNvBlockDescriptor(block_desc)
        # Note: setNvBlockDescriptor adds to the list, so we check the length
        assert len(comp_type.nvBlockDescriptors) == 1


class TestSensorActuatorSwComponentType:
    """Test class for SensorActuatorSwComponentType class."""

    def test_sensor_actuator_sw_component_type_initialization(self):
        """Test SensorActuatorSwComponentType initialization."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        comp_type = SensorActuatorSwComponentType(ar_root, "TestSensorActuatorSwComponentType")

        assert comp_type.parent == ar_root
        assert comp_type.short_name == "TestSensorActuatorSwComponentType"
        assert comp_type.ports == []
        assert comp_type.portGroups == []
        assert comp_type.internalBehavior is None
        assert comp_type.symbolProps is None


class TestServiceProxySwComponentType:
    """Test class for ServiceProxySwComponentType class."""

    def test_service_proxy_sw_component_type_initialization(self):
        """Test ServiceProxySwComponentType initialization."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        comp_type = ServiceProxySwComponentType(ar_root, "TestServiceProxySwComponentType")

        assert comp_type.parent == ar_root
        assert comp_type.short_name == "TestServiceProxySwComponentType"
        assert comp_type.ports == []
        assert comp_type.portGroups == []
        assert comp_type.internalBehavior is None
        assert comp_type.symbolProps is None


class TestServiceSwComponentType:
    """Test class for ServiceSwComponentType class."""

    def test_service_sw_component_type_initialization(self):
        """Test ServiceSwComponentType initialization."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        comp_type = ServiceSwComponentType(ar_root, "TestServiceSwComponentType")

        assert comp_type.parent == ar_root
        assert comp_type.short_name == "TestServiceSwComponentType"
        assert comp_type.ports == []
        assert comp_type.portGroups == []
        assert comp_type.internalBehavior is None
        assert comp_type.symbolProps is None


class TestCompositionSwComponentType:
    """Test class for CompositionSwComponentType class."""

    def test_composition_sw_component_type_initialization(self):
        """Test CompositionSwComponentType initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        comp_type = CompositionSwComponentType(ar_root, "TestCompositionSwComponentType")

        assert comp_type.parent == ar_root
        assert comp_type.short_name == "TestCompositionSwComponentType"
        assert comp_type.ports == []
        assert comp_type.portGroups == []
        assert comp_type.components == []
        assert comp_type.constantValueMappingRefs == []
        assert comp_type.dataTypeMappingRefs == []
        assert comp_type.instantiationRTEEventProps == []
        assert comp_type.components == []
        assert comp_type.constantValueMappingRefs == []
        assert comp_type.dataTypeMappingRefs == []
        assert comp_type.instantiationRTEEventProps == []

        # Test component methods
        comp_proto = comp_type.createSwComponentPrototype("TestComponent")
        assert comp_proto is not None
        assert comp_proto.short_name == "TestComponent"
        assert comp_proto in comp_type.getComponents()

        # Test data type mapping methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
            RefType,
        )
        data_type_ref = RefType()
        data_type_ref.setValue("/Data/Type/Ref")
        comp_type.addDataTypeMapping(data_type_ref)
        assert data_type_ref in comp_type.getDataTypeMappings()

        # Test connector methods
        assembly_connector = comp_type.createAssemblySwConnector("TestAssemblyConnector")
        assert assembly_connector is not None
        assert assembly_connector.short_name == "TestAssemblyConnector"
        assert assembly_connector in comp_type.getAssemblySwConnectors()

        delegation_connector = comp_type.createDelegationSwConnector("TestDelegationConnector")
        assert delegation_connector is not None
        assert delegation_connector.short_name == "TestDelegationConnector"
        assert delegation_connector in comp_type.getDelegationSwConnectors()

        # Test port creation methods
        p_port = comp_type.createPPortPrototype("TestPPort")
        assert p_port is not None
        assert p_port.short_name == "TestPPort"
        assert p_port in comp_type.getPPortPrototypes()

        r_port = comp_type.createRPortPrototype("TestRPort")
        assert r_port is not None
        assert r_port.short_name == "TestRPort"
        assert r_port in comp_type.getRPortPrototypes()

        pr_port = comp_type.createPRPortPrototype("TestPRPort")
        assert pr_port is not None
        assert pr_port.short_name == "TestPRPort"
        assert pr_port in comp_type.getPRPortPrototypes()

        port_group = comp_type.createPortGroup("TestPortGroup")
        assert port_group is not None
        assert port_group.short_name == "TestPortGroup"
        assert port_group in comp_type.getPortGroups()
