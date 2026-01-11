"""
This module contains tests for the Components subdirectory in SWComponentTemplate.
"""
import pytest
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import (
    SymbolProps,
    PortPrototype,
    AbstractProvidedPortPrototype,
    AbstractRequiredPortPrototype,
    PPortPrototype,
    RPortPrototype,
    PRPortPrototype,
    PortGroup,
    SwComponentType,
    AtomicSwComponentType,
    EcuAbstractionSwComponentType,
    ApplicationSwComponentType,
    ComplexDeviceDriverSwComponentType,
    NvBlockSwComponentType,
    SensorActuatorSwComponentType,
    ServiceProxySwComponentType,
    ServiceSwComponentType,
    CompositionSwComponentType
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition import (
    AssemblySwConnector,
    DelegationSwConnector,
    SwComponentPrototype
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import SwcInternalBehavior
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import (
    PPortComSpec, RPortComSpec, NonqueuedSenderComSpec, ServerComSpec, 
    QueuedSenderComSpec, ModeSwitchSenderComSpec, ClientComSpec,
    NonqueuedReceiverComSpec, QueuedReceiverComSpec, ModeSwitchReceiverComSpec,
    ParameterRequireComSpec
)
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TRefType, ARBoolean, RefType
)


class Test_M2_AUTOSARTemplates_SWComponentTemplate_Components:
    """Test class for Components module classes."""
    
    def test_SymbolProps(self):
        """Test SymbolProps class."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        symbol_props = SymbolProps(ar_root, "TestSymbol")
        
        assert symbol_props.parent == ar_root
        assert symbol_props.short_name == "TestSymbol"

    def test_PortPrototype(self):
        """Test PortPrototype class."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        port_prototype = PortPrototype(ar_root, "TestPort")
        
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
        
        # Test setters and getters
        port_prototype.addClientServerAnnotation("Annotation1")
        assert "Annotation1" in port_prototype.getClientServerAnnotations()
        
        port_prototype.setDelegatedPortAnnotation("DelegatedAnnotation")
        assert port_prototype.getDelegatedPortAnnotation() == "DelegatedAnnotation"

    def test_AbstractProvidedPortPrototype(self):
        """Test AbstractProvidedPortPrototype class."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        provided_port = AbstractProvidedPortPrototype(ar_root, "TestProvidedPort")
        
        assert provided_port.providedComSpecs == []
        
        # Test adding provided com spec
        com_spec = NonqueuedSenderComSpec()
        com_spec.dataElementRef = RefType()
        com_spec.dataElementRef.dest = "VARIABLE-DATA-PROTOTYPE"
        provided_port.addProvidedComSpec(com_spec)
        assert com_spec in provided_port.getProvidedComSpecs()

    def test_AbstractRequiredPortPrototype(self):
        """Test AbstractRequiredPortPrototype class."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        required_port = AbstractRequiredPortPrototype(ar_root, "TestRequiredPort")
        
        assert required_port.requiredComSpecs == []
        
        # Test adding required com spec
        com_spec = ClientComSpec()
        required_port.addRequiredComSpec(com_spec)
        assert com_spec in required_port.getRequiredComSpecs()

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
        ar_bool = ARBoolean()
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
        assert pr_port.providedRequiredInterface is None
        
        # Test adding com specs
        # Use concrete implementations instead of abstract class
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import QueuedSenderComSpec, ClientComSpec
        provided_spec = QueuedSenderComSpec()
        pr_port.addProvidedComSpec(provided_spec)
        assert provided_spec in pr_port.getProvidedComSpecs()
        
        required_spec = ClientComSpec()
        pr_port.addRequiredComSpec(required_spec)
        assert required_spec in pr_port.getRequiredComSpecs()

    def test_PortGroup(self):
        """Test PortGroup class."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        port_group = PortGroup(ar_root, "TestPortGroup")
        
        assert port_group._inner_group_iref == []
        assert port_group._outer_port_ref == []
        
        # Test adding inner group IRefs
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import InnerPortGroupInCompositionInstanceRef
        iref = InnerPortGroupInCompositionInstanceRef()
        port_group.addInnerGroupIRef(iref)
        assert iref in port_group.getInnerGroupIRefs()
        
        # Test adding outer port refs
        ref = RefType()
        port_group.addOuterPortRef(ref)
        assert ref in port_group.getOuterPortRefs()

    def test_SwComponentType_abstract(self):
        """Test that SwComponentType is abstract."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
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
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
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