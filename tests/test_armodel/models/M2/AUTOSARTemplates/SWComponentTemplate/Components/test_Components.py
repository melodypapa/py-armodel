"""
This module contains tests for the Components subdirectory in SWComponentTemplate.
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation import ImplementationProps
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Referrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, CIdentifier, RefType, TRefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes import (
    ClientServerAnnotation,
    DelegatedPortAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import (
    ClientComSpec,
    ModeSwitchReceiverComSpec,
    ModeSwitchSenderComSpec,
    NonqueuedReceiverComSpec,
    NonqueuedSenderComSpec,
    ParameterRequireComSpec,
    PPortComSpec,
    QueuedReceiverComSpec,
    QueuedSenderComSpec,
    RPortComSpec,
    ServerComSpec,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import (
    ApplicationSwComponentType,
    AtomicSwComponentType,
    ComplexDeviceDriverSwComponentType,
    EcuAbstractionSwComponentType,
    NvBlockSwComponentType,
    PortGroup,
    PPortPrototype,
    PRPortPrototype,
    RPortPrototype,
    SensorActuatorSwComponentType,
    ServiceProxySwComponentType,
    ServiceSwComponentType,
    SwComponentType,
    SymbolProps,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import InnerPortGroupInCompositionInstanceRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition import CompositionSwComponentType


class Test_M2_AUTOSARTemplates_SWComponentTemplate_Components:
    """Test class for Components module classes."""

    def test_PortPrototype(self):
        """Test PortPrototype class."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        port_prototype = PRPortPrototype(ar_root, "TestPort")

        assert port_prototype.parent == ar_root
        assert port_prototype.short_name == "TestPort"
        assert port_prototype.clientServerAnnotations == []
        assert port_prototype.delegatedPortAnnotation is None
        assert port_prototype.ioHwAbstractionServerAnnotations == []
        assert port_prototype.modePortAnnotations == []
        assert port_prototype.nvDataPortAnnotations == []
        assert port_prototype.parameterPortAnnotations == []
        assert port_prototype.senderReceiverAnnotations == []
        assert port_prototype.triggerPortAnnotations == []

        # Test setters and getters with real annotation objects
        cs_annotation = ClientServerAnnotation()
        port_prototype.addClientServerAnnotation(cs_annotation)
        assert cs_annotation in port_prototype.getClientServerAnnotations()

        delegated_annotation = DelegatedPortAnnotation()
        port_prototype.setDelegatedPortAnnotation(delegated_annotation)
        assert port_prototype.getDelegatedPortAnnotation() == delegated_annotation

        # None no-ops
        port_prototype.addClientServerAnnotation(None)
        assert len(port_prototype.getClientServerAnnotations()) == 1
        port_prototype.setDelegatedPortAnnotation(None)
        assert port_prototype.getDelegatedPortAnnotation() == delegated_annotation

    def test_AbstractProvidedPortPrototype(self):
        """Test AbstractProvidedPortPrototype class."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        provided_port = PPortPrototype(ar_root, "TestProvidedPort")

        assert provided_port.providedComSpecs == []

        # Test adding provided com spec
        com_spec = NonqueuedSenderComSpec()
        com_spec.dataElementRef = RefType()
        com_spec.dataElementRef.dest = "VARIABLE-DATA-PROTOTYPE"
        provided_port.addProvidedComSpec(com_spec)
        assert com_spec in provided_port.getProvidedComSpecs()

        # Test QueuedSenderComSpec to cover line 109
        queued_spec = QueuedSenderComSpec()
        queued_spec.dataElementRef = RefType()
        queued_spec.dataElementRef.dest = "VARIABLE-DATA-PROTOTYPE"
        provided_port.addProvidedComSpec(queued_spec)
        assert queued_spec in provided_port.getProvidedComSpecs()

        # Test ModeSwitchSenderComSpec to cover line 111
        mode_switch_spec = ModeSwitchSenderComSpec()
        mode_switch_spec.dataElementRef = RefType()
        mode_switch_spec.dataElementRef.dest = "VARIABLE-DATA-PROTOTYPE"
        provided_port.addProvidedComSpec(mode_switch_spec)
        assert mode_switch_spec in provided_port.getProvidedComSpecs()

        # Test ServerComSpec (line 107)
        server_spec = ServerComSpec()
        provided_port.addProvidedComSpec(server_spec)
        assert server_spec in provided_port.getProvidedComSpecs()

    def test_AbstractRequiredPortPrototype(self):
        """Test AbstractRequiredPortPrototype class."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        required_port = RPortPrototype(ar_root, "TestRequiredPort")

        assert required_port.requiredComSpecs == []

        # Test adding required com spec
        com_spec = ClientComSpec()
        required_port.addRequiredComSpec(com_spec)
        assert com_spec in required_port.getRequiredComSpecs()

        # Test QueuedReceiverComSpec to cover line 142
        queued_receiver_spec = QueuedReceiverComSpec()
        required_port.addRequiredComSpec(queued_receiver_spec)
        assert queued_receiver_spec in required_port.getRequiredComSpecs()

        # Test ModeSwitchReceiverComSpec to cover line 144
        mode_switch_receiver_spec = ModeSwitchReceiverComSpec()
        required_port.addRequiredComSpec(mode_switch_receiver_spec)
        assert mode_switch_receiver_spec in required_port.getRequiredComSpecs()

        # Test ParameterRequireComSpec (line 145-148)
        param_spec = ParameterRequireComSpec()
        param_ref = RefType()
        param_ref.setValue("/Test/Parameter")
        param_ref.dest = "PARAMETER-DATA-PROTOTYPE"
        param_spec.setParameterRef(param_ref)
        required_port.addRequiredComSpec(param_spec)
        assert param_spec in required_port.getRequiredComSpecs()

        # Test NonqueuedReceiverComSpec (line 137-140)
        receiver_spec = NonqueuedReceiverComSpec()
        receiver_ref = RefType()
        receiver_ref.setValue("/Test/Variable")
        receiver_ref.dest = "VARIABLE-DATA-PROTOTYPE"
        receiver_spec.setDataElementRef(receiver_ref)
        required_port.addRequiredComSpec(receiver_spec)
        assert receiver_spec in required_port.getRequiredComSpecs()

    def test_PPortPrototype(self):
        """Test PPortPrototype class."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        p_port = PPortPrototype(ar_root, "TestPPort")

        assert p_port.providedInterfaceTRef is None

        # Test setter and getter
        tref = TRefType()
        p_port.setProvidedInterfaceTRef(tref)
        assert p_port.getProvidedInterfaceTRef() == tref

    def test_RPortPrototype(self):
        """Test RPortPrototype class."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        r_port = RPortPrototype(ar_root, "TestRPort")

        assert r_port.mayBeUnconnected is None
        assert r_port.requiredInterfaceTRef is None

        # Test setters and getters
        ar_bool = Boolean()
        ar_bool.setValue(True)
        r_port.setMayBeUnconnected(ar_bool)
        assert r_port.getMayBeUnconnected().getValue() is True

        tref = TRefType()
        r_port.setRequiredInterfaceTRef(tref)
        assert r_port.getRequiredInterfaceTRef() == tref

    def test_PRPortPrototype(self):
        """Test PRPortPrototype class."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        pr_port = PRPortPrototype(ar_root, "TestPRPort")

        assert isinstance(pr_port.providedComSpecs, list)
        assert isinstance(pr_port.requiredComSpecs, list)
        assert pr_port.providedRequiredInterfaceTRef is None

        # Test adding com specs
        # Use concrete implementations instead of abstract class
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import ClientComSpec, QueuedSenderComSpec

        provided_spec = QueuedSenderComSpec()
        pr_port.addProvidedComSpec(provided_spec)
        assert provided_spec in pr_port.getProvidedComSpecs()

        required_spec = ClientComSpec()
        pr_port.addRequiredComSpec(required_spec)
        assert required_spec in pr_port.getRequiredComSpecs()

        # Test getProvidedRequiredInterfaceTRef
        assert pr_port.getProvidedRequiredInterfaceTRef() is None

        # Test setProvidedRequiredInterfaceTRef
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import TRefType

        tref = TRefType()
        tref.setValue("test_interface")
        pr_port.setProvidedRequiredInterfaceTRef(tref)
        assert pr_port.getProvidedRequiredInterfaceTRef() == tref
        assert pr_port.getProvidedRequiredInterfaceTRef().getValue() == "test_interface"
        assert pr_port == pr_port.setProvidedRequiredInterfaceTRef(tref)

    def test_PortGroup(self):
        """Test PortGroup class against spec Table 4.94."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        port_group = PortGroup(ar_root, "TestPortGroup")

        # Defaults
        assert port_group.innerGroupIRefs == []
        assert port_group.outerPortRefs == []

        # Inheritance chain
        assert isinstance(port_group, Referrable)
        assert isinstance(port_group, AtpStructureElement)
        assert isinstance(port_group, ARObject)

        # Class docstring is the spec Note verbatim
        assert port_group.__doc__ is not None
        assert port_group.__doc__.strip() == (
            "Group of ports which share a common functionality , e.g. need specific network resources. "
            "This information shall be available on the VFB level in order to delegate it properly via compositions. "
            "When propagated into the ECU extract, this information is used as input for the configuration of Services "
            "like the Communication Manager. A PortGroup is defined locally in a component (which can be a composition) "
            'and refers to the "outer" ports belonging to the group as well as to the "inner" groups which propagate '
            "this group into the components which are part of a composition. A PortGroup within an atomic SWC cannot "
            "be linked to inner groups."
        )

        # innerGroup
        iref = InnerPortGroupInCompositionInstanceRef()
        returned = port_group.addInnerGroupIRef(iref)
        assert returned is port_group
        assert iref in port_group.getInnerGroupIRefs()
        assert "Links a PortGroup in a composition to another PortGroup" in port_group.getInnerGroupIRefs.__doc__

        # outerPort
        ref = RefType()
        returned = port_group.addOuterPortRef(ref)
        assert returned is port_group
        assert ref in port_group.getOuterPortRefs()
        assert "Outer PortPrototype of this AtomicSwComponentType" in port_group.getOuterPortRefs.__doc__

    def test_SwComponentType_abstract(self):
        """Test that SwComponentType is abstract."""

        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")

        # Create a concrete subclass to test the abstract class
        class TestSwComponentType(SwComponentType):
            def __init__(self, parent: ARObject, short_name: str):
                super().__init__(parent, short_name)

        test_component = TestSwComponentType(ar_root, "TestSwComponent")
        assert test_component is not None
        assert test_component.short_name == "TestSwComponent"
        assert isinstance(test_component, SwComponentType)

    def test_AtomicSwComponentType_abstract(self):
        """Test that AtomicSwComponentType is abstract."""

        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")

        # Create a concrete subclass to test the abstract class
        class TestAtomicSwComponentType(AtomicSwComponentType):
            def __init__(self, parent: ARObject, short_name: str):
                super().__init__(parent, short_name)

        test_component = TestAtomicSwComponentType(ar_root, "TestAtomicSwComponent")
        assert test_component is not None
        assert test_component.short_name == "TestAtomicSwComponent"
        assert isinstance(test_component, AtomicSwComponentType)
        assert isinstance(test_component, SwComponentType)

    def test_ApplicationSwComponentType(self):
        """Test ApplicationSwComponentType class."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        app_sw_component = ApplicationSwComponentType(ar_root, "TestAppSwComponent")

        assert app_sw_component.internalBehavior is None
        assert app_sw_component.symbolProps is None

    def test_EcuAbstractionSwComponentType(self):
        """Test EcuAbstractionSwComponentType class."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        ecu_sw_component = EcuAbstractionSwComponentType(ar_root, "TestEcuAbstractionSwComponent")

        assert ecu_sw_component.hardwareElementRefs == []

    def test_ComplexDeviceDriverSwComponentType(self):
        """Test ComplexDeviceDriverSwComponentType class."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        driver_sw_component = ComplexDeviceDriverSwComponentType(ar_root, "TestComplexDeviceDriverSwComponent")

        assert driver_sw_component.hardwareElementRefs == []

    def test_NvBlockSwComponentType(self):
        """Test NvBlockSwComponentType class."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        nv_sw_component = NvBlockSwComponentType(ar_root, "TestNvBlockSwComponent")

        assert nv_sw_component.bulkNvDataDescriptors == []
        assert nv_sw_component.nvBlockDescriptors == []

    def test_SensorActuatorSwComponentType(self):
        """Test SensorActuatorSwComponentType class."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        sensor_sw_component = SensorActuatorSwComponentType(ar_root, "TestSensorActuatorSwComponent")

        # Just check instantiation
        assert sensor_sw_component is not None

    def test_ServiceProxySwComponentType(self):
        """Test ServiceProxySwComponentType class."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        service_proxy_sw_component = ServiceProxySwComponentType(ar_root, "TestServiceProxySwComponent")

        # Just check instantiation
        assert service_proxy_sw_component is not None

    def test_ServiceSwComponentType(self):
        """Test ServiceSwComponentType class."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        service_sw_component = ServiceSwComponentType(ar_root, "TestServiceSwComponent")

        # Just check instantiation
        assert service_sw_component is not None

    def test_CompositionSwComponentType(self):
        """Test CompositionSwComponentType class."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        composition_sw_component = CompositionSwComponentType(ar_root, "TestCompositionSwComponent")

        assert composition_sw_component.components == []
        assert composition_sw_component.constantValueMappingRefs == []
        assert composition_sw_component.dataTypeMappingRefs == []
        assert composition_sw_component.instantiationRTEEventProps == []

        # Test creating and getting components
        component = composition_sw_component.createSwComponentPrototype("Component1")
        assert component is not None
        assert len(composition_sw_component.getComponents()) == 1

        # Test connector methods
        assembly_connector = composition_sw_component.createAssemblySwConnector("TestAssembly")
        delegation_connector = composition_sw_component.createDelegationSwConnector("TestDelegation")

        # Test removeAllAssemblySwConnector
        assert assembly_connector in composition_sw_component.elements
        composition_sw_component.removeAllAssemblySwConnector()
        assert assembly_connector not in composition_sw_component.elements

        # Recreate and test removeAllDelegationSwConnector
        assembly_connector = composition_sw_component.createAssemblySwConnector("TestAssembly2")
        assert delegation_connector in composition_sw_component.elements
        composition_sw_component.removeAllDelegationSwConnector()
        assert delegation_connector not in composition_sw_component.elements

    def test_Validate_PPortComSpec_Errors(self):
        """Test validation error paths for PPortComSpec."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        provided_port = PPortPrototype(ar_root, "TestProvidedPort")

        # Test NonqueuedSenderComSpec without dataElementRef
        com_spec_no_ref = NonqueuedSenderComSpec()
        com_spec_no_ref.dataElementRef = None
        with pytest.raises(ValueError) as exc_info:
            provided_port._validateProvidedComSpec(com_spec_no_ref)
        assert "operation of NonqueuedSenderComSpec is invalid" in str(exc_info.value)

        # Test NonqueuedSenderComSpec with invalid dest
        com_spec_invalid_dest = NonqueuedSenderComSpec()
        ref = RefType()
        ref.setValue("/Test/Variable")
        ref.dest = "INVALID-DEST"
        com_spec_invalid_dest.dataElementRef = ref
        with pytest.raises(ValueError) as exc_info:
            provided_port._validateProvidedComSpec(com_spec_invalid_dest)
        assert "Invalid operation dest of NonqueuedSenderComSpec" in str(exc_info.value)

        # Test unsupported com spec type
        class UnsupportedComSpec(PPortComSpec):
            def __init__(self):
                super().__init__()

        unsupported_spec = UnsupportedComSpec()
        with pytest.raises(ValueError) as exc_info:
            provided_port._validateProvidedComSpec(unsupported_spec)
        assert "Unsupported com spec" in str(exc_info.value)

    def test_Validate_RPortComSpec_Errors(self):
        """Test validation error paths for RPortComSpec."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        required_port = RPortPrototype(ar_root, "TestRequiredPort")

        # Test ClientComSpec with invalid dest
        client_spec = ClientComSpec()
        client_ref = RefType()
        client_ref.setValue("/Test/Operation")
        client_ref.dest = "INVALID-DEST"
        client_spec.operationRef = client_ref
        with pytest.raises(ValueError) as exc_info:
            required_port._validateRequiredComSpec(client_spec)
        assert "Invalid operation dest of ClientComSpec." in str(exc_info.value)

        # Test NonqueuedReceiverComSpec with invalid dest
        receiver_spec = NonqueuedReceiverComSpec()
        receiver_ref = RefType()
        receiver_ref.setValue("/Test/Variable")
        receiver_ref.dest = "INVALID-DEST"
        receiver_spec.dataElementRef = receiver_ref
        with pytest.raises(ValueError) as exc_info:
            required_port._validateRequiredComSpec(receiver_spec)
        assert "Invalid date element dest of NonqueuedReceiverComSpec." in str(exc_info.value)

        # Test ParameterRequireComSpec with invalid dest
        param_spec = ParameterRequireComSpec()
        param_ref = RefType()
        param_ref.setValue("/Test/Parameter")
        param_ref.dest = "INVALID-DEST"
        param_spec.parameterRef = param_ref
        with pytest.raises(ValueError) as exc_info:
            required_port._validateRequiredComSpec(param_spec)
        assert "Invalid parameter dest of ParameterRequireComSpec." in str(exc_info.value)

        # Test unsupported RPortComSpec type
        class UnsupportedRPortComSpec(RPortComSpec):
            def __init__(self):
                super().__init__()

        unsupported_spec = UnsupportedRPortComSpec()
        with pytest.raises(ValueError) as exc_info:
            required_port._validateRequiredComSpec(unsupported_spec)
        assert "Unsupported RPortComSpec" in str(exc_info.value)

    def test_getNonqueuedSenderComSpecs(self):
        """Test getting nonqueued sender com specs filter."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        provided_port = PPortPrototype(ar_root, "TestProvidedPort")

        com_spec = NonqueuedSenderComSpec()
        ref = RefType()
        ref.setValue("/Test/Variable")
        ref.dest = "VARIABLE-DATA-PROTOTYPE"
        com_spec.dataElementRef = ref
        provided_port.addProvidedComSpec(com_spec)

        server_spec = ServerComSpec()
        provided_port.addProvidedComSpec(server_spec)

        nonqueued_specs = list(provided_port.getNonqueuedSenderComSpecs())
        assert com_spec in nonqueued_specs
        assert server_spec not in nonqueued_specs

    def test_getClientComSpecs(self):
        """Test getting client com specs filter."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        required_port = RPortPrototype(ar_root, "TestRequiredPort")

        client_spec = ClientComSpec()
        required_port.addRequiredComSpec(client_spec)

        receiver_spec = NonqueuedReceiverComSpec()
        required_port.addRequiredComSpec(receiver_spec)

        client_specs = list(required_port.getClientComSpecs())
        assert client_spec in client_specs
        assert receiver_spec not in client_specs

    def test_getNonqueuedReceiverComSpecs(self):
        """Test getting nonqueued receiver com specs filter."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        required_port = RPortPrototype(ar_root, "TestRequiredPort")

        client_spec = ClientComSpec()
        required_port.addRequiredComSpec(client_spec)

        receiver_spec = NonqueuedReceiverComSpec()
        required_port.addRequiredComSpec(receiver_spec)

        receiver_specs = list(required_port.getNonqueuedReceiverComSpecs())
        assert receiver_spec in receiver_specs
        assert client_spec not in receiver_specs

    def test_AtomicSwComponentType_full(self):
        """Test AtomicSwComponentType full functionality."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        swc = AtomicSwComponentType(ar_root, "TestAtomicSwc")

        # Test internal behavior creation returns the existing element on re-create
        behavior = swc.createSwcInternalBehavior("TestBehavior")
        assert swc.getInternalBehavior() == behavior
        assert swc.createSwcInternalBehavior("TestBehavior") == behavior
        assert behavior.short_name == "TestBehavior"
        assert behavior in swc.elements

        # Test symbol props creation returns the existing element on re-create
        symbol_props = swc.createSymbolProps("TestSymbolProps")
        assert swc.getSymbolProps() == symbol_props
        assert swc.createSymbolProps("TestSymbolProps") == symbol_props
        assert symbol_props.short_name == "TestSymbolProps"
        assert symbol_props in swc.elements

    def test_AtomicSwComponentType_base_properties(self):
        """Test AtomicSwComponentType abstract base accessors through a concrete subclass."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        swc = ApplicationSwComponentType(ar_root, "TestAtomicSwc")

        assert swc.getInternalBehavior() is None
        assert swc.getSymbolProps() is None

        behavior = swc.createSwcInternalBehavior("TestBehavior")
        assert swc.getInternalBehavior() == behavior

        symbol_props = swc.createSymbolProps("TestSymbolProps")
        assert swc.getSymbolProps() == symbol_props

    def test_AtomicSwComponentType_round_trip(self):
        """Test AtomicSwComponentType symbolProps and internalBehavior round trip."""
        import os
        import tempfile

        from armodel.parser.arxml_parser import ARXMLParser
        from armodel.writer.arxml_writer import ARXMLWriter

        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        swc = ar_root.createApplicationSwComponentType("TestAtomicSwc")

        swc.createSwcInternalBehavior("TestBehavior")
        symbol_props = swc.createSymbolProps("TestSymbolProps")
        symbol_props.setSymbol(CIdentifier().setValue("TestSymbol"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            swc_2 = document_2.getARPackages()[0].getAtomicSwComponentTypes()[0]

            assert swc_2.getInternalBehavior().getShortName() == "TestBehavior"
            assert swc_2.getSymbolProps().getShortName() == "TestSymbolProps"
            assert swc_2.getSymbolProps().getSymbol().getValue() == "TestSymbol"
        finally:
            os.remove(file_path)

    def test_EcuAbstractionSwComponentType_methods(self):
        """Test EcuAbstractionSwComponentType methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        swc = EcuAbstractionSwComponentType(ar_root, "TestEcu")

        ref = RefType()
        ref.setValue("/Test/HwElement")
        swc.addHardwareElementRef(ref)
        assert ref in swc.getHardwareElementRefs()

        # Test addHardwareElementRef with None
        swc.addHardwareElementRef(None)
        assert len(swc.getHardwareElementRefs()) == 1

    def test_ComplexDeviceDriverSwComponentType_methods(self):
        """Test ComplexDeviceDriverSwComponentType methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        swc = ComplexDeviceDriverSwComponentType(ar_root, "TestCdd")

        ref = RefType()
        ref.setValue("/Test/HwElement")
        swc.addHardwareElementRef(ref)
        assert ref in swc.getHardwareElementRefs()

        # Test addHardwareElementRef with None
        swc.addHardwareElementRef(None)
        assert len(swc.getHardwareElementRefs()) == 1

    def test_NvBlockSwComponentType_methods(self):
        """Test NvBlockSwComponentType methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        swc = NvBlockSwComponentType(ar_root, "TestNvBlock")

        # Test createBulkNvDataDescriptor
        descriptor = swc.createBulkNvDataDescriptor("BulkDesc")
        assert descriptor in swc.getBulkNvDataDescriptors()
        assert swc.createBulkNvDataDescriptor("BulkDesc") is descriptor

        # Test createNvBlockDescriptor
        nv_descriptor = swc.createNvBlockDescriptor("BlockDesc")
        assert nv_descriptor in swc.getNvBlockDescriptors()
        assert swc.createNvBlockDescriptor("BlockDesc") is nv_descriptor

    def test_PortPrototype_all_annotation_methods(self):
        """Test all annotation methods for PortPrototype."""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes import (
            IoHwAbstractionServerAnnotation,
            ModePortAnnotation,
            NvDataPortAnnotation,
            ParameterPortAnnotation,
            SenderReceiverAnnotation,
            TriggerPortAnnotation,
        )

        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        port = PRPortPrototype(ar_root, "TestPort")

        # Test all add annotation methods with real annotation objects
        io_hw = IoHwAbstractionServerAnnotation()
        port.addIoHwAbstractionServerAnnotation(io_hw)
        mode = ModePortAnnotation()
        port.addModePortAnnotation(mode)
        nv_data = NvDataPortAnnotation()
        port.addNvDataPortAnnotation(nv_data)
        param = ParameterPortAnnotation()
        port.addParameterPortAnnotation(param)
        sender_recv = SenderReceiverAnnotation()
        port.addSenderReceiverAnnotation(sender_recv)
        trigger = TriggerPortAnnotation()
        port.addTriggerPortAnnotation(trigger)

        assert io_hw in port.getIoHwAbstractionServerAnnotations()
        assert mode in port.getModePortAnnotations()
        assert nv_data in port.getNvDataPortAnnotations()
        assert param in port.getParameterPortAnnotations()
        assert sender_recv in port.getSenderReceiverAnnotations()
        assert trigger in port.getTriggerPortAnnotations()

        # None no-ops for the add annotation methods
        port.addIoHwAbstractionServerAnnotation(None)
        assert len(port.getIoHwAbstractionServerAnnotations()) == 1

    def test_SwComponentType_port_creation(self):
        """Test SwComponentType port creation methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")

        class TestSwcType(SwComponentType):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        swc = TestSwcType(ar_root, "TestSwc")

        # Test all port creation methods
        p_port = swc.createPPortPrototype("PPort")
        assert p_port.short_name == "PPort"
        assert p_port in swc.getPPortPrototypes()

        r_port = swc.createRPortPrototype("RPort")
        assert r_port.short_name == "RPort"
        assert r_port in swc.getRPortPrototypes()

        pr_port = swc.createPRPortPrototype("PRPort")
        assert pr_port.short_name == "PRPort"
        assert pr_port in swc.getPRPortPrototypes()

        # Test getPortPrototypes
        all_ports = swc.getPortPrototypes()
        assert len(all_ports) == 3
        assert p_port in all_ports
        assert r_port in all_ports
        assert pr_port in all_ports

        # Test getPorts to cover line 260
        ports = swc.getPorts()
        assert len(ports) == 3
        assert p_port in ports
        assert r_port in ports
        assert pr_port in ports

    def test_SwComponentType_port_group_methods(self):
        """Test SwComponentType port group methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")

        class TestSwcType(SwComponentType):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        swc = TestSwcType(ar_root, "TestSwc")

        # Test port group creation
        port_group = swc.createPortGroup("TestGroup")
        assert port_group.short_name == "TestGroup"
        assert port_group in swc.getPortGroups()

        # Test port group methods

        iref = InnerPortGroupInCompositionInstanceRef()
        port_group.addInnerGroupIRef(iref)
        assert iref in port_group.getInnerGroupIRefs()

        outer_ref = RefType()
        outer_ref.setValue("/Test/Port")
        port_group.addOuterPortRef(outer_ref)
        assert outer_ref in port_group.getOuterPortRefs()

    def test_CompositionSwComponentType_connector_methods(self):
        """Test CompositionSwComponentType connector methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        swc = CompositionSwComponentType(ar_root, "TestComposition")

        # Test getSwConnectors
        connector1 = swc.createAssemblySwConnector("Assembly1")
        connector2 = swc.createDelegationSwConnector("Delegation1")

        connectors = swc.getSwConnectors()
        assert connector1 in connectors
        assert connector2 in connectors

        # Test addDataTypeMappingRef
        mapping_ref = RefType()
        mapping_ref.setValue("/Test/Mapping")
        swc.addDataTypeMappingRef(mapping_ref)
        assert mapping_ref in swc.getDataTypeMappingRefs()


class TestSymbolProps:
    """
    Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.21, p.288 (R23-11)
    """

    # Table 5.21 Note, verbatim
    NOTE = (
        "This meta-class represents the ability to attach with the symbol attribute a "
        "symbolic name that is conform to C language requirements to another meta-class, "
        "e.g. AtomicSwComponentType, that is a potential subject to a name clash on the "
        "level of RTE source code."
    )

    def _make(self) -> SymbolProps:
        document = AUTOSAR.getInstance()
        document.new()
        ar_root = document.createARPackage("AUTOSAR")
        return SymbolProps(ar_root, "TestSymbol")

    def test_initialization(self):
        """
        Test that SymbolProps is a concrete ImplementationProps subclass with an
        inherited (None) symbol and no own fields.
        """
        symbol_props = self._make()

        assert symbol_props.parent is not None
        assert symbol_props.short_name == "TestSymbol"
        assert isinstance(symbol_props, ImplementationProps)
        assert symbol_props.getSymbol() is None

    def test_inherited_symbol_round_trip(self):
        """
        Test that the symbol attribute (inherited from ImplementationProps, Table 5.20)
        round-trips and that None is a no-op.
        """
        symbol_props = self._make()

        symbol = CIdentifier()
        symbol.setValue("TestSymbol_C")
        assert symbol_props.setSymbol(symbol) is symbol_props
        assert symbol_props.getSymbol() is symbol

        symbol_props.setSymbol(None)
        assert symbol_props.getSymbol() is symbol

    def test_class_docstring_verbatim(self):
        """
        Test that the class docstring is the Table 5.21 Note copied verbatim.
        """
        assert (SymbolProps.__doc__ or "").strip() == self.NOTE
