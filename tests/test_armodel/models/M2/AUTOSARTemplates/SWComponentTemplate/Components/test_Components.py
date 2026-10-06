"""
This module contains tests for the Components subdirectory in SWComponentTemplate.
"""

import logging
from abc import ABC
from typing import List

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
    NvProvideComSpec,
    NvRequireComSpec,
    ParameterProvideComSpec,
    ParameterRequireComSpec,
    PPortComSpec,
    QueuedReceiverComSpec,
    QueuedSenderComSpec,
    ReceiverComSpec,
    RPortComSpec,
    SenderComSpec,
    ServerComSpec,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import (
    AbstractProvidedPortPrototype,
    AbstractRequiredPortPrototype,
    ApplicationSwComponentType,
    AtomicSwComponentType,
    ComplexDeviceDriverSwComponentType,
    EcuAbstractionSwComponentType,
    NvBlockSwComponentType,
    ParameterSwComponentType,
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

COMSPEC_DEST_CASES = (
    ("PPort", NonqueuedSenderComSpec, "setDataElementRef", "VARIABLE-DATA-PROTOTYPE"),
    ("PPort", QueuedSenderComSpec, "setDataElementRef", "VARIABLE-DATA-PROTOTYPE"),
    ("PPort", ServerComSpec, "setOperationRef", "CLIENT-SERVER-OPERATION"),
    ("PPort", ModeSwitchSenderComSpec, "setModeGroupRef", "MODE-DECLARATION-GROUP-PROTOTYPE"),
    ("PPort", NvProvideComSpec, "setVariableRef", "VARIABLE-DATA-PROTOTYPE"),
    ("PPort", ParameterProvideComSpec, "setParameterRef", "PARAMETER-DATA-PROTOTYPE"),
    ("RPort", ClientComSpec, "setOperationRef", "CLIENT-SERVER-OPERATION"),
    ("RPort", NonqueuedReceiverComSpec, "setDataElementRef", "VARIABLE-DATA-PROTOTYPE"),
    ("RPort", QueuedReceiverComSpec, "setDataElementRef", "VARIABLE-DATA-PROTOTYPE"),
    ("RPort", ModeSwitchReceiverComSpec, "setModeGroupRef", "MODE-DECLARATION-GROUP-PROTOTYPE"),
    ("RPort", NvRequireComSpec, "setVariableRef", "VARIABLE-DATA-PROTOTYPE"),
    ("RPort", ParameterRequireComSpec, "setParameterRef", "PARAMETER-DATA-PROTOTYPE"),
)


def _create_comspec_port(port_side):
    document = AUTOSAR.getInstance()
    document.clear()
    ar_root = document.createARPackage("AUTOSAR")
    if port_side == "PPort":
        port = PPortPrototype(ar_root, "Provided")
        return port, port.addProvidedComSpec, port.getProvidedComSpecs
    port = RPortPrototype(ar_root, "Required")
    return port, port.addRequiredComSpec, port.getRequiredComSpecs


def _concrete_descendants(base_class):
    descendants = set()
    for child_class in base_class.__subclasses__():
        descendants.update(_concrete_descendants(child_class))
        if child_class not in (SenderComSpec, ReceiverComSpec) and child_class.__module__ == base_class.__module__:
            descendants.add(child_class)
    return descendants


class Test_M2_AUTOSARTemplates_SWComponentTemplate_Components:
    """Test class for Components module classes."""

    def test_comspec_dest_matrix_covers_all_concrete_children(self):
        provided_types = {com_spec_type for side, com_spec_type, _, _ in COMSPEC_DEST_CASES if side == "PPort"}
        required_types = {com_spec_type for side, com_spec_type, _, _ in COMSPEC_DEST_CASES if side == "RPort"}
        assert provided_types == _concrete_descendants(PPortComSpec)
        assert required_types == _concrete_descendants(RPortComSpec)

    @pytest.mark.parametrize(
        ("port_side", "com_spec_type", "setter_name", "expected_dest"),
        COMSPEC_DEST_CASES,
        ids=["%s-%s" % (case[0], case[1].__name__) for case in COMSPEC_DEST_CASES],
    )
    def test_comspec_with_matching_dest_is_appended(self, port_side, com_spec_type, setter_name, expected_dest):
        _, add_com_spec, get_com_specs = _create_comspec_port(port_side)
        com_spec = com_spec_type()
        reference = RefType().setValue("/Test/Target")
        reference.dest = expected_dest
        getattr(com_spec, setter_name)(reference)

        add_com_spec(com_spec)

        assert get_com_specs() == [com_spec]

    @pytest.mark.parametrize(
        ("port_side", "com_spec_type", "setter_name", "expected_dest"),
        COMSPEC_DEST_CASES,
        ids=["%s-%s" % (case[0], case[1].__name__) for case in COMSPEC_DEST_CASES],
    )
    def test_comspec_with_mismatching_dest_warns_and_is_skipped(self, caplog, port_side, com_spec_type, setter_name, expected_dest):
        _, add_com_spec, get_com_specs = _create_comspec_port(port_side)
        com_spec = com_spec_type()
        reference = RefType().setValue("/Test/Target")
        reference.dest = "INVALID-DEST"
        getattr(com_spec, setter_name)(reference)

        with caplog.at_level(logging.WARNING):
            add_com_spec(com_spec)

        assert com_spec not in get_com_specs()
        assert "Invalid DEST" in caplog.text
        assert com_spec_type.__name__ in caplog.text
        assert expected_dest in caplog.text
        assert "INVALID-DEST" in caplog.text

    @pytest.mark.parametrize(
        ("port_side", "com_spec_type", "setter_name", "expected_dest"),
        COMSPEC_DEST_CASES,
        ids=["%s-%s" % (case[0], case[1].__name__) for case in COMSPEC_DEST_CASES],
    )
    def test_comspec_without_reference_is_appended_without_warning(self, caplog, port_side, com_spec_type, setter_name, expected_dest):
        _, add_com_spec, get_com_specs = _create_comspec_port(port_side)
        com_spec = com_spec_type()

        with caplog.at_level(logging.WARNING):
            add_com_spec(com_spec)

        assert get_com_specs() == [com_spec]
        assert caplog.records == []

    @pytest.mark.parametrize(
        ("port_side", "com_spec_base"),
        (("PPort", PPortComSpec), ("RPort", RPortComSpec)),
    )
    def test_unsupported_comspec_warns_and_is_skipped(self, caplog, port_side, com_spec_base):
        _, add_com_spec, get_com_specs = _create_comspec_port(port_side)
        unsupported_type = type("Unsupported%sComSpec" % port_side, (com_spec_base,), {})
        com_spec = unsupported_type()

        with caplog.at_level(logging.WARNING):
            add_com_spec(com_spec)

        assert get_com_specs() == []
        assert "Unsupported" in caplog.text
        assert unsupported_type.__name__ in caplog.text

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
        mode_group_ref = RefType().setValue("/Test/ModeGroup")
        mode_group_ref.dest = "MODE-DECLARATION-GROUP-PROTOTYPE"
        mode_switch_spec.setModeGroupRef(mode_group_ref)
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

        assert ecu_sw_component is not None
        assert isinstance(ecu_sw_component, AtomicSwComponentType)
        assert ecu_sw_component.hardwareElementRefs == []

    def test_EcuAbstractionSwComponentType_add_get_hardwareElementRefs(self):
        """Test addHardwareElementRef/getHardwareElementRefs round-trip and None no-op."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        ecu_sw_component = EcuAbstractionSwComponentType(ar_root, "TestEcuAbstractionSwComponent")

        ref = RefType().setValue("/HwTypes/HwElement")
        ref.dest = "HW-DESCRIPTION-ENTITY"

        assert ecu_sw_component.addHardwareElementRef(ref) is ecu_sw_component
        assert ecu_sw_component.getHardwareElementRefs() == [ref]
        assert ecu_sw_component.hardwareElementRefs == [ref]

        ecu_sw_component.addHardwareElementRef(None)
        assert ecu_sw_component.getHardwareElementRefs() == [ref]

    def test_ComplexDeviceDriverSwComponentType(self):
        """Test ComplexDeviceDriverSwComponentType class."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        driver_sw_component = ComplexDeviceDriverSwComponentType(ar_root, "TestComplexDeviceDriverSwComponent")

        assert driver_sw_component is not None
        assert isinstance(driver_sw_component, AtomicSwComponentType)
        assert driver_sw_component.hardwareElementRefs == []

    def test_ComplexDeviceDriverSwComponentType_add_get_hardwareElementRefs(self):
        """Test addHardwareElementRef/getHardwareElementRefs round-trip and None no-op."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        driver_sw_component = ComplexDeviceDriverSwComponentType(ar_root, "TestComplexDeviceDriverSwComponent")

        ref = RefType().setValue("/HwTypes/HwElement")
        ref.dest = "HW-DESCRIPTION-ENTITY"

        assert driver_sw_component.addHardwareElementRef(ref) is driver_sw_component
        assert driver_sw_component.getHardwareElementRefs() == [ref]
        assert driver_sw_component.hardwareElementRefs == [ref]

        driver_sw_component.addHardwareElementRef(None)
        assert driver_sw_component.getHardwareElementRefs() == [ref]

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

        assert sensor_sw_component is not None
        assert isinstance(sensor_sw_component, AtomicSwComponentType)
        assert sensor_sw_component.sensorActuatorRef is None

    def test_SensorActuatorSwComponentType_get_set_sensorActuatorRef(self):
        """Test getSensorActuatorRef/setSensorActuatorRef round-trip and None no-op."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        sensor_sw_component = SensorActuatorSwComponentType(ar_root, "TestSensorActuatorSwComponent")

        ref = RefType().setValue("/HwTypes/Sensor")
        ref.dest = "HW-DESCRIPTION-ENTITY"

        assert sensor_sw_component.setSensorActuatorRef(ref) is sensor_sw_component
        assert sensor_sw_component.getSensorActuatorRef() is ref
        assert sensor_sw_component.sensorActuatorRef is ref

        sensor_sw_component.setSensorActuatorRef(None)
        assert sensor_sw_component.getSensorActuatorRef() is ref

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

        assert service_sw_component is not None
        assert isinstance(service_sw_component, AtomicSwComponentType)

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
        assert assembly_connector in composition_sw_component.referrableElements
        composition_sw_component.removeAllAssemblySwConnector()
        assert assembly_connector not in composition_sw_component.referrableElements

        # Recreate and test removeAllDelegationSwConnector
        assembly_connector = composition_sw_component.createAssemblySwConnector("TestAssembly2")
        assert delegation_connector in composition_sw_component.referrableElements
        composition_sw_component.removeAllDelegationSwConnector()
        assert delegation_connector not in composition_sw_component.referrableElements

    def test_comspec_refs_are_optional_but_dest_is_checked_when_present(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        provided_port = PPortPrototype(ar_root, "Provided")
        required_port = RPortPrototype(ar_root, "Required")

        sender_without_ref = NonqueuedSenderComSpec()
        provided_port.addProvidedComSpec(sender_without_ref)
        assert provided_port.getProvidedComSpecs() == [sender_without_ref]

        sender_ref = RefType().setValue("/Test/Variable")
        sender_ref.dest = "VARIABLE-DATA-PROTOTYPE"
        sender_with_ref = NonqueuedSenderComSpec().setDataElementRef(sender_ref)
        provided_port.addProvidedComSpec(sender_with_ref)
        assert provided_port.getProvidedComSpecs() == [sender_without_ref, sender_with_ref]

        client_without_ref = ClientComSpec()
        receiver_without_ref = NonqueuedReceiverComSpec()
        parameter_without_ref = ParameterRequireComSpec()
        for com_spec in (client_without_ref, receiver_without_ref, parameter_without_ref):
            required_port.addRequiredComSpec(com_spec)

        client_ref = RefType().setValue("/Test/Operation")
        client_ref.dest = "CLIENT-SERVER-OPERATION"
        client_with_ref = ClientComSpec().setOperationRef(client_ref)
        receiver_ref = RefType().setValue("/Test/Variable")
        receiver_ref.dest = "VARIABLE-DATA-PROTOTYPE"
        receiver_with_ref = NonqueuedReceiverComSpec().setDataElementRef(receiver_ref)
        parameter_ref = RefType().setValue("/Test/Parameter")
        parameter_ref.dest = "PARAMETER-DATA-PROTOTYPE"
        parameter_with_ref = ParameterRequireComSpec().setParameterRef(parameter_ref)
        for com_spec in (client_with_ref, receiver_with_ref, parameter_with_ref):
            required_port.addRequiredComSpec(com_spec)

        assert required_port.getRequiredComSpecs() == [client_without_ref, receiver_without_ref, parameter_without_ref, client_with_ref, receiver_with_ref, parameter_with_ref]

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

        class ConcreteAtomicFullSwComponentType(AtomicSwComponentType):
            pass

        swc = ConcreteAtomicFullSwComponentType(ar_root, "TestAtomicSwc")

        # Test internal behavior creation returns the existing element on re-create
        behavior = swc.createSwcInternalBehavior("TestBehavior")
        assert swc.getInternalBehavior() == behavior
        assert swc.createSwcInternalBehavior("TestBehavior") == behavior
        assert behavior.short_name == "TestBehavior"
        assert behavior in swc.referrableElements

        # Test symbol props creation returns the existing element on re-create
        symbol_props = swc.createSymbolProps("TestSymbolProps")
        assert swc.getSymbolProps() == symbol_props
        assert swc.createSymbolProps("TestSymbolProps") == symbol_props
        assert symbol_props.short_name == "TestSymbolProps"
        assert symbol_props in swc.referrableElements

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
            SenderAnnotation,
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
        sender_recv = SenderAnnotation()
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


class TestAbstractProvidedPortPrototypeSpecContract:
    """Spec-contract tests for AbstractProvidedPortPrototype (SWC TPS Table 3.4, p.68)."""

    CLASS_NOTE = "This abstract class provides the ability to become a provided PortPrototype."
    COM_SPEC_NOTE = "Provided communication attributes per interface element (data element or operation). Stereotypes: atpSplitable Tags: atp.Splitkey=providedComSpec"

    def _make(self, name="pp"):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")

        class _Concrete(AbstractProvidedPortPrototype):
            pass

        return _Concrete(ar_root, name)

    def test_abstract_guard(self):
        with pytest.raises(TypeError):
            AbstractProvidedPortPrototype(None, "abstract")

    def test_abstract_class_declared_abc(self):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import PortPrototype

        assert AbstractProvidedPortPrototype.__bases__ == (PortPrototype, ABC)

    def test_class_note_verbatim(self):
        import inspect

        assert inspect.cleandoc(AbstractProvidedPortPrototype.__doc__) == self.CLASS_NOTE

    def test_base_shape(self):
        """Most-derived base PortPrototype per the Table 3.4 Base row."""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import PortPrototype

        assert issubclass(AbstractProvidedPortPrototype, PortPrototype)

    def test_add_get_provided_com_specs(self):
        """Test providedComSpecs list round-trip, chaining and None no-op (Table 3.4 providedComSpec, `*` aggr)."""
        port = self._make()
        assert port.getProvidedComSpecs() == []
        com_spec = QueuedSenderComSpec()
        assert port.addProvidedComSpec(com_spec) is port
        assert port.getProvidedComSpecs() == [com_spec]
        port.addProvidedComSpec(None)
        assert port.getProvidedComSpecs() == [com_spec]

    def test_validate_provided_comspec_returns_false_for_invalid_dest(self, caplog):
        port = self._make()
        com_spec = NonqueuedSenderComSpec()
        reference = RefType().setValue("/Test/Variable")
        reference.dest = "INVALID-DEST"
        com_spec.setDataElementRef(reference)

        with caplog.at_level(logging.WARNING):
            assert port._validateProvidedComSpec(com_spec) is False

        assert "Invalid DEST" in caplog.text
        assert "NonqueuedSenderComSpec" in caplog.text

    def test_accessor_annotations(self):
        """addProvidedComSpec carries Optional[PPortComSpec] and chains; getProvidedComSpecs returns List[PPortComSpec] (Table 3.4 mults)."""
        from typing import Optional, get_type_hints

        add_hints = get_type_hints(AbstractProvidedPortPrototype.addProvidedComSpec)
        assert add_hints["com_spec"] == Optional[PPortComSpec]
        assert add_hints["return"] == AbstractProvidedPortPrototype
        get_hints = get_type_hints(AbstractProvidedPortPrototype.getProvidedComSpecs)
        assert get_hints["return"] == List[PPortComSpec]

    def test_member_order(self):
        """Exactly the one Table 3.4 attribute row after the base attrs."""
        assert list(vars(self._make()).keys())[-1:] == ["providedComSpecs"]


class TestAbstractRequiredPortPrototypeSpecContract:
    """Spec-contract tests for AbstractRequiredPortPrototype (SWC TPS Table 3.3, p.67)."""

    CLASS_NOTE = "This abstract class provides the ability to become a required PortPrototype."
    COM_SPEC_NOTE = "Required communication attributes, one for each interface element. Stereotypes: atpSplitable Tags: atp.Splitkey=requiredComSpec"

    def _make(self, name="rp"):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")

        class _Concrete(AbstractRequiredPortPrototype):
            pass

        return _Concrete(ar_root, name)

    def test_abstract_guard(self):
        with pytest.raises(TypeError):
            AbstractRequiredPortPrototype(None, "abstract")

    def test_abstract_class_declared_abc(self):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import PortPrototype

        assert AbstractRequiredPortPrototype.__bases__ == (PortPrototype, ABC)

    def test_class_note_verbatim(self):
        import inspect

        assert inspect.cleandoc(AbstractRequiredPortPrototype.__doc__) == self.CLASS_NOTE

    def test_base_shape(self):
        """Most-derived base PortPrototype per the Table 3.3 Base row."""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import PortPrototype

        assert issubclass(AbstractRequiredPortPrototype, PortPrototype)

    def test_attribute_note_comment_verbatim(self):
        import inspect

        init_source = inspect.getsource(AbstractRequiredPortPrototype.__init__)
        assert "# Required communication attributes, one for each interface element." in init_source
        assert "# Required communication attributes, one for each interface element. Stereotypes:" not in init_source

    def test_add_get_required_com_specs(self):
        """Test requiredComSpecs list round-trip, chaining and None no-op (Table 3.3 requiredComSpec, `*` aggr)."""
        port = self._make()
        assert port.getRequiredComSpecs() == []
        com_spec = ClientComSpec()
        assert port.addRequiredComSpec(com_spec) is port
        assert port.getRequiredComSpecs() == [com_spec]
        port.addRequiredComSpec(None)
        assert port.getRequiredComSpecs() == [com_spec]

    def test_validate_required_comspec_returns_false_for_invalid_dest(self, caplog):
        port = self._make()
        com_spec = NonqueuedReceiverComSpec()
        reference = RefType().setValue("/Test/Variable")
        reference.dest = "INVALID-DEST"
        com_spec.setDataElementRef(reference)

        with caplog.at_level(logging.WARNING):
            assert port._validateRequiredComSpec(com_spec) is False

        assert "Invalid DEST" in caplog.text
        assert "NonqueuedReceiverComSpec" in caplog.text

    def test_accessor_annotations(self):
        """addRequiredComSpec carries Optional[RPortComSpec] and chains; getRequiredComSpecs returns List[RPortComSpec] (Table 3.3 mults)."""
        from typing import Optional, get_type_hints

        add_hints = get_type_hints(AbstractRequiredPortPrototype.addRequiredComSpec)
        assert add_hints["com_spec"] == Optional[RPortComSpec]
        assert add_hints["return"] == AbstractRequiredPortPrototype
        get_hints = get_type_hints(AbstractRequiredPortPrototype.getRequiredComSpecs)
        assert get_hints["return"] == List[RPortComSpec]

    def test_member_order(self):
        """Exactly the one Table 3.3 attribute row after the base attrs."""
        assert list(vars(self._make()).keys())[-1:] == ["requiredComSpecs"]


SW_COMPONENT_TYPE_CLASS_NOTE = "Base class for AUTOSAR software components."

SW_COMPONENT_TYPE_MEMBER_NOTES = {
    "consistencyNeeds": "This represents the collection of ConsistencyNeeds owned by the enclosing SwComponentType.",
    "port": "The PortPrototypes through which this SwComponentType can communicate. The aggregation of PortPrototype is subject to variability with the purpose to support the conditional existence of PortPrototypes.",
    "portGroup": "A port group being part of this component.",
    "swcMappingConstraint": "Reference to constraints that are valid for this SwComponentType.",
    "swComponentDocumentation": "This adds a documentation to the SwComponentType.",
    "unitGroup": "This allows for the specification of which UnitGroups are relevant in the context of referencing SwComponentType.",
}

SW_COMPONENT_TYPE_MEMBERS = [
    "consistencyNeeds",
    "ports",
    "portGroups",
    "swcMappingConstraintsRefs",
    "swComponentDocumentation",
    "unitGroupRefs",
]


class ConcreteSwComponentType(SwComponentType):
    pass


class Test_SwComponentType_Spec:
    """Spec pins for SwComponentType (CP_TPS_SoftwareComponentTemplate Table 3.1, p.65)."""

    def _make(self):
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        return ConcreteSwComponentType(ar_root, "Swc")

    def test_inheritance(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement

        assert issubclass(SwComponentType, ARElement)
        assert issubclass(SwComponentType, ARObject)

    def test_abstract_guard(self):
        ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        with pytest.raises(TypeError, match="SwComponentType is an abstract class"):
            SwComponentType(ar_root, "swc")

    def test_class_docstring_note(self):
        import inspect

        assert inspect.cleandoc(SwComponentType.__doc__) == SW_COMPONENT_TYPE_CLASS_NOTE

    def test_init_docless(self):
        assert SwComponentType.__init__.__doc__ is None

    def test_initialization_defaults(self):
        swc = self._make()
        assert swc.getConsistencyNeeds() == []
        assert swc.getPorts() == []
        assert swc.getPortGroups() == []
        assert swc.getSwcMappingConstraintsRefs() == []
        assert swc.getSwComponentDocumentation() is None
        assert swc.getUnitGroupRefs() == []

    def test_member_order(self):
        swc = self._make()
        members = [k for k in vars(swc) if k in set(SW_COMPONENT_TYPE_MEMBERS)]
        assert members == SW_COMPONENT_TYPE_MEMBERS

    def test_docstrings_verbatim(self):
        getter_notes = {
            SwComponentType.getConsistencyNeeds: SW_COMPONENT_TYPE_MEMBER_NOTES["consistencyNeeds"],
            SwComponentType.getPorts: SW_COMPONENT_TYPE_MEMBER_NOTES["port"],
            SwComponentType.getPortGroups: SW_COMPONENT_TYPE_MEMBER_NOTES["portGroup"],
            SwComponentType.getSwcMappingConstraintsRefs: SW_COMPONENT_TYPE_MEMBER_NOTES["swcMappingConstraint"],
            SwComponentType.getSwComponentDocumentation: SW_COMPONENT_TYPE_MEMBER_NOTES["swComponentDocumentation"],
            SwComponentType.getUnitGroupRefs: SW_COMPONENT_TYPE_MEMBER_NOTES["unitGroup"],
        }
        for getter, note in getter_notes.items():
            assert getter.__doc__ is not None, getter.__name__
            assert getter.__doc__.strip().split("\n")[0] == note, getter.__name__
        setter_notes = {
            SwComponentType.createConsistencyNeeds: SW_COMPONENT_TYPE_MEMBER_NOTES["consistencyNeeds"],
            SwComponentType.createPPortPrototype: SW_COMPONENT_TYPE_MEMBER_NOTES["port"],
            SwComponentType.createRPortPrototype: SW_COMPONENT_TYPE_MEMBER_NOTES["port"],
            SwComponentType.createPRPortPrototype: SW_COMPONENT_TYPE_MEMBER_NOTES["port"],
            SwComponentType.createPortGroup: SW_COMPONENT_TYPE_MEMBER_NOTES["portGroup"],
            SwComponentType.addSwcMappingConstraintRef: SW_COMPONENT_TYPE_MEMBER_NOTES["swcMappingConstraint"],
            SwComponentType.setSwComponentDocumentation: SW_COMPONENT_TYPE_MEMBER_NOTES["swComponentDocumentation"],
            SwComponentType.addUnitGroupRef: SW_COMPONENT_TYPE_MEMBER_NOTES["unitGroup"],
        }
        for setter, note in setter_notes.items():
            assert setter.__doc__ is not None, setter.__name__
            assert note in setter.__doc__, setter.__name__
        for setter, member in [
            (SwComponentType.addSwcMappingConstraintRef, "swcMappingConstraintsRefs"),
            (SwComponentType.setSwComponentDocumentation, "swComponentDocumentation"),
            (SwComponentType.addUnitGroupRef, "unitGroupRefs"),
        ]:
            assert (
                "A None value is a no-op and does not overwrite an existing %s." % member in setter.__doc__ or "A None value is a no-op and does not append anything." in setter.__doc__
            ), setter.__name__

    def test_get_set_sw_component_documentation(self):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SoftwareComponentDocumentation import SwComponentDocumentation

        swc = self._make()
        doc = SwComponentDocumentation()
        assert swc == swc.setSwComponentDocumentation(doc)
        assert swc.getSwComponentDocumentation() is doc
        assert swc == swc.setSwComponentDocumentation(None)
        assert swc.getSwComponentDocumentation() is doc

    def test_add_get_swc_mapping_constraint_refs(self):
        swc = self._make()
        ref = RefType().setValue("/Constraints/Mapping1")
        assert swc == swc.addSwcMappingConstraintRef(ref)
        assert swc.getSwcMappingConstraintsRefs() == [ref]
        swc.addSwcMappingConstraintRef(None)
        assert swc.getSwcMappingConstraintsRefs() == [ref]

    def test_add_get_unit_group_refs(self):
        swc = self._make()
        ref = RefType().setValue("/Units/Group1")
        assert swc == swc.addUnitGroupRef(ref)
        assert swc.getUnitGroupRefs() == [ref]
        swc.addUnitGroupRef(None)
        assert swc.getUnitGroupRefs() == [ref]

    def test_create_consistency_needs_duplicate_returns_existing(self):
        swc = self._make()
        needs = swc.createConsistencyNeeds("Needs")
        assert needs.short_name == "Needs"
        assert swc.createConsistencyNeeds("Needs") is needs
        assert swc.getConsistencyNeeds() == [needs]

    def test_create_port_group_duplicate_returns_existing(self):
        swc = self._make()
        group = swc.createPortGroup("Group")
        assert group.short_name == "Group"
        assert swc.createPortGroup("Group") is group

    def test_type_hints(self):
        import typing

        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SoftwareComponentDocumentation import SwComponentDocumentation as SwComponentDocumentation

        hints = typing.get_type_hints(SwComponentType.setSwComponentDocumentation)
        assert hints["value"] == typing.Optional[SwComponentDocumentation]
        assert hints["return"] is SwComponentType
        hints = typing.get_type_hints(SwComponentType.addSwcMappingConstraintRef)
        assert hints["value"] == typing.Optional[RefType]
        assert hints["return"] is SwComponentType
        hints = typing.get_type_hints(SwComponentType.addUnitGroupRef)
        assert hints["value"] == typing.Optional[RefType]
        hints = typing.get_type_hints(SwComponentType.getSwComponentDocumentation)
        assert hints["return"] == typing.Optional[SwComponentDocumentation]
        hints = typing.get_type_hints(SwComponentType.getPorts)
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import PortPrototype as PortPrototype

        assert hints["return"] == typing.List[PortPrototype]


PARAMETER_SW_COMPONENT_TYPE_CLASS_NOTE = (
    "The ParameterSwComponentType defines parameters and characteristic values accessible via provided Ports. The provided values are the same for all connected SwComponentPrototypes"
)

PARAMETER_SW_COMPONENT_TYPE_MEMBER_NOTES = {
    "constantMapping": "Reference to the ConstantSpecificationMapping to be applied for the particular ParameterSwComponentType",
    "dataTypeMapping": "Reference to the DataTypeMapping to be applied for the particular ParameterSwComponentType",
    "instantiationDataDefProps": "The purpose of this is that within the context of a given SwComponentType some data def properties of individual instantiations can be modified. The aggregation of InstantiationDataDefProps is subject to variability with the purpose to support the conditional existence of PortPrototypes",
}

PARAMETER_SW_COMPONENT_TYPE_MEMBERS = [
    "constantMappingRefs",
    "dataTypeMappingRefs",
    "instantiationDataDefProps",
]


class Test_ParameterSwComponentType_Spec:
    """Spec pins for ParameterSwComponentType (CP_TPS_SoftwareComponentTemplate Table 2.1, p.41)."""

    def _make(self):
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        return ParameterSwComponentType(ar_root, "ParamSwc")

    def _make_component(self):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstantiationDataDefProps import InstantiationDataDefProps

        return InstantiationDataDefProps()

    def test_inheritance(self):
        assert issubclass(ParameterSwComponentType, SwComponentType)
        assert issubclass(ParameterSwComponentType, ARObject)

    def test_concrete(self):
        assert self._make() is not None

    def test_class_docstring_note(self):
        import inspect

        assert inspect.cleandoc(ParameterSwComponentType.__doc__) == PARAMETER_SW_COMPONENT_TYPE_CLASS_NOTE

    def test_init_docless(self):
        assert ParameterSwComponentType.__init__.__doc__ is None

    def test_initialization_defaults(self):
        swc = self._make()
        assert swc.getConstantMappingRefs() == []
        assert swc.getDataTypeMappingRefs() == []
        assert swc.getInstantiationDataDefProps() == []

    def test_member_order(self):
        swc = self._make()
        members = [k for k in vars(swc) if k in set(PARAMETER_SW_COMPONENT_TYPE_MEMBERS)]
        assert members == PARAMETER_SW_COMPONENT_TYPE_MEMBERS

    def test_add_get_constant_mapping_refs(self):
        swc = self._make()
        ref = RefType().setValue("/Pkg/ConstantMapping1")
        assert swc == swc.addConstantMappingRef(ref)
        assert swc.getConstantMappingRefs() == [ref]
        swc.addConstantMappingRef(None)
        assert swc.getConstantMappingRefs() == [ref]

    def test_add_get_data_type_mapping_refs(self):
        swc = self._make()
        ref = RefType().setValue("/Pkg/DataTypeMapping1")
        assert swc == swc.addDataTypeMappingRef(ref)
        assert swc.getDataTypeMappingRefs() == [ref]
        swc.addDataTypeMappingRef(None)
        assert swc.getDataTypeMappingRefs() == [ref]

    def test_add_get_instantiation_data_def_props(self):
        swc = self._make()
        props = self._make_component()
        assert swc == swc.addInstantiationDataDefProps(props)
        assert swc.getInstantiationDataDefProps() == [props]
        swc.addInstantiationDataDefProps(None)
        assert swc.getInstantiationDataDefProps() == [props]

    def test_docstrings_verbatim(self):
        getter_notes = {
            ParameterSwComponentType.getConstantMappingRefs: PARAMETER_SW_COMPONENT_TYPE_MEMBER_NOTES["constantMapping"],
            ParameterSwComponentType.getDataTypeMappingRefs: PARAMETER_SW_COMPONENT_TYPE_MEMBER_NOTES["dataTypeMapping"],
            ParameterSwComponentType.getInstantiationDataDefProps: PARAMETER_SW_COMPONENT_TYPE_MEMBER_NOTES["instantiationDataDefProps"],
        }
        for getter, note in getter_notes.items():
            assert getter.__doc__ is not None, getter.__name__
            assert getter.__doc__.strip().split("\n")[0] == note, getter.__name__
        setter_notes = {
            ParameterSwComponentType.addConstantMappingRef: PARAMETER_SW_COMPONENT_TYPE_MEMBER_NOTES["constantMapping"],
            ParameterSwComponentType.addDataTypeMappingRef: PARAMETER_SW_COMPONENT_TYPE_MEMBER_NOTES["dataTypeMapping"],
            ParameterSwComponentType.addInstantiationDataDefProps: PARAMETER_SW_COMPONENT_TYPE_MEMBER_NOTES["instantiationDataDefProps"],
        }
        for setter, note in setter_notes.items():
            assert setter.__doc__ is not None, setter.__name__
            assert note in setter.__doc__, setter.__name__
        for setter, member in [
            (ParameterSwComponentType.addConstantMappingRef, "constantMappingRefs"),
            (ParameterSwComponentType.addDataTypeMappingRef, "dataTypeMappingRefs"),
            (ParameterSwComponentType.addInstantiationDataDefProps, "instantiationDataDefProps"),
        ]:
            assert "A None value is a no-op and does not append anything." in setter.__doc__, setter.__name__

    def test_type_hints(self):
        import typing

        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstantiationDataDefProps import InstantiationDataDefProps

        hints = typing.get_type_hints(ParameterSwComponentType.addConstantMappingRef)
        assert hints["value"] == typing.Optional[RefType]
        assert hints["return"] is ParameterSwComponentType
        hints = typing.get_type_hints(ParameterSwComponentType.getDataTypeMappingRefs)
        assert hints["return"] == typing.List[RefType]
        hints = typing.get_type_hints(ParameterSwComponentType.addInstantiationDataDefProps)
        assert hints["value"] == typing.Optional[InstantiationDataDefProps]
        hints = typing.get_type_hints(ParameterSwComponentType.getInstantiationDataDefProps)
        assert hints["return"] == typing.List[InstantiationDataDefProps]

    def test_inherited_base_accessors(self):
        swc = self._make()
        swc.createPPortPrototype("P1")
        assert [p.short_name for p in swc.getPorts()] == ["P1"]


ATOMIC_SW_COMPONENT_TYPE_CLASS_NOTE = "An atomic software component is atomic in the sense that it cannot be further decomposed and distributed across multiple ECUs."

ATOMIC_SW_COMPONENT_TYPE_MEMBER_NOTES = {
    "internalBehavior": "The SwcInternalBehaviors owned by an AtomicSwComponentType can be located in a different physical file. Therefore the aggregation is <<atpSplitable>>.",
    "symbolProps": "This represents the SymbolProps for the AtomicSwComponentType.",
}

ATOMIC_SW_COMPONENT_TYPE_MEMBERS = [
    "internalBehavior",
    "symbolProps",
]


class Test_AtomicSwComponentType_Spec:
    """Spec pins for AtomicSwComponentType (CP_TPS_SoftwareComponentTemplate Table 3.8, p.70)."""

    def _make(self):
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")

        class ConcreteAtomicSwComponentType(AtomicSwComponentType):
            pass

        return ConcreteAtomicSwComponentType(ar_root, "AtomicSwc")

    def test_inheritance(self):
        assert issubclass(AtomicSwComponentType, SwComponentType)
        assert issubclass(AtomicSwComponentType, ARObject)

    def test_abstract_guard(self):
        ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        with pytest.raises(TypeError, match="AtomicSwComponentType is an abstract class"):
            AtomicSwComponentType(ar_root, "atomic")

    def test_class_docstring_note(self):
        import inspect

        assert inspect.cleandoc(AtomicSwComponentType.__doc__) == ATOMIC_SW_COMPONENT_TYPE_CLASS_NOTE

    def test_init_docless(self):
        assert AtomicSwComponentType.__init__.__doc__ is None

    def test_initialization_defaults(self):
        swc = self._make()
        assert swc.getInternalBehavior() is None
        assert swc.getSymbolProps() is None

    def test_member_order(self):
        swc = self._make()
        members = [k for k in vars(swc) if k in set(ATOMIC_SW_COMPONENT_TYPE_MEMBERS)]
        assert members == ATOMIC_SW_COMPONENT_TYPE_MEMBERS

    def test_create_swc_internal_behavior_duplicate_returns_existing(self):
        swc = self._make()
        behavior = swc.createSwcInternalBehavior("Behavior")
        assert behavior.short_name == "Behavior"
        assert swc.createSwcInternalBehavior("Behavior") is behavior
        assert swc.getInternalBehavior() is behavior

    def test_create_symbol_props_duplicate_returns_existing(self):
        swc = self._make()
        props = swc.createSymbolProps("Sym")
        assert props.short_name == "Sym"
        assert swc.createSymbolProps("Sym") is props
        assert swc.getSymbolProps() is props

    def test_docstrings_verbatim(self):
        assert AtomicSwComponentType.getInternalBehavior.__doc__.strip().split("\n")[0] == ATOMIC_SW_COMPONENT_TYPE_MEMBER_NOTES["internalBehavior"]
        assert AtomicSwComponentType.createSwcInternalBehavior.__doc__ is not None
        assert ATOMIC_SW_COMPONENT_TYPE_MEMBER_NOTES["internalBehavior"] in AtomicSwComponentType.createSwcInternalBehavior.__doc__
        assert AtomicSwComponentType.getSymbolProps.__doc__.strip().split("\n")[0] == ATOMIC_SW_COMPONENT_TYPE_MEMBER_NOTES["symbolProps"]
        assert ATOMIC_SW_COMPONENT_TYPE_MEMBER_NOTES["symbolProps"] in AtomicSwComponentType.createSymbolProps.__doc__

    def test_type_hints(self):
        import typing

        hints = typing.get_type_hints(AtomicSwComponentType.getSymbolProps)
        assert hints["return"] == typing.Optional[SymbolProps]
        hints = typing.get_type_hints(AtomicSwComponentType.createSymbolProps)
        assert hints["return"] is SymbolProps


APPLICATION_SW_COMPONENT_TYPE_CLASS_NOTE = "The ApplicationSwComponentType is used to represent the application software."


class Test_ApplicationSwComponentType_Spec:
    """Spec pins for ApplicationSwComponentType (CP_TPS_SoftwareComponentTemplate Table 3.9, p.71)."""

    def _make(self):
        document = AUTOSAR.getInstance()
        document.clear()
        return document.createARPackage("AUTOSAR").createApplicationSwComponentType("App")

    def test_inheritance(self):
        assert issubclass(ApplicationSwComponentType, AtomicSwComponentType)
        assert issubclass(ApplicationSwComponentType, SwComponentType)

    def test_concrete(self):
        assert self._make() is not None

    def test_class_docstring_note(self):
        import inspect

        assert inspect.cleandoc(ApplicationSwComponentType.__doc__) == APPLICATION_SW_COMPONENT_TYPE_CLASS_NOTE

    def test_init_docless(self):
        assert ApplicationSwComponentType.__init__.__doc__ is None

    def test_no_own_spec_attributes(self):
        swc = self._make()

        class ConcreteAtomicProbeSwComponentType(AtomicSwComponentType):
            pass

        probe = ConcreteAtomicProbeSwComponentType(swc.parent, "Probe")
        assert set(vars(swc)) == set(vars(probe))

    def test_inherited_accessors_via_concrete_class(self):
        swc = self._make()
        swc.createPPortPrototype("P1")
        assert [p.short_name for p in swc.getPorts()] == ["P1"]
        behavior = swc.createSwcInternalBehavior("B")
        assert swc.getInternalBehavior() is behavior
        assert swc.createSymbolProps("S") is swc.getSymbolProps()


SERVICE_SW_COMPONENT_TYPE_CLASS_NOTE = (
    "ServiceSwComponentType is used for configuring services for a given ECU."
    " Instances of this class are only to be created in ECU Configuration phase for the specific purpose of the service configuration."
    " Tags: atp.recommendedPackage=SwComponentTypes"
)


class Test_ServiceSwComponentType_Spec:
    """Spec pins for ServiceSwComponentType (CP_TPS_SoftwareComponentTemplate Table 11.2, p.659)."""

    def _make(self):
        document = AUTOSAR.getInstance()
        document.clear()
        return document.createARPackage("AUTOSAR").createServiceSwComponentType("Svc")

    def test_inheritance(self):
        assert issubclass(ServiceSwComponentType, AtomicSwComponentType)
        assert issubclass(ServiceSwComponentType, SwComponentType)

    def test_concrete(self):
        assert self._make() is not None

    def test_class_docstring_note(self):
        import inspect

        assert inspect.cleandoc(ServiceSwComponentType.__doc__) == SERVICE_SW_COMPONENT_TYPE_CLASS_NOTE

    def test_init_docless(self):
        assert ServiceSwComponentType.__init__.__doc__ is None

    def test_no_own_spec_attributes(self):
        swc = self._make()

        class ConcreteAtomicProbeSwComponentType(AtomicSwComponentType):
            pass

        probe = ConcreteAtomicProbeSwComponentType(swc.parent, "Probe")
        assert set(vars(swc)) == set(vars(probe))

    def test_inherited_accessors_via_concrete_class(self):
        swc = self._make()
        swc.createRPortPrototype("R1")
        assert [p.short_name for p in swc.getPorts()] == ["R1"]
        behavior = swc.createSwcInternalBehavior("B")
        assert swc.getInternalBehavior() is behavior
        assert swc.createSymbolProps("S") is swc.getSymbolProps()
