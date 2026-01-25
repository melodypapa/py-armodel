"""Test PortInterfaceParser methods."""
from armodel.parser.parsers.port_interface_parser import PortInterfaceParser
from armodel.parser.parsers.common_structure_parser import (
    CommonStructureParser,
)


class TestPortInterfaceParser:
    """Test PortInterfaceParser."""

    def test_port_interface_parser_initialization(self):
        """Test that PortInterfaceParser can be initialized."""
        parser = PortInterfaceParser()
        assert parser is not None
        assert hasattr(parser, 'readSenderReceiverInterface')
        assert hasattr(parser, 'readClientServerInterface')
        assert hasattr(parser, 'readModeSwitchInterface')
        assert hasattr(parser, 'readParameterInterface')
        assert hasattr(parser, 'readTriggerInterface')

    def test_port_interface_parser_with_parent_parser(self):
        """Test that PortInterfaceParser can accept parent parser."""
        common_parser = CommonStructureParser()
        parser = PortInterfaceParser(parent_parser=common_parser)
        assert parser._parent_parser == common_parser

    def test_read_sender_receiver_interface_method_exists(self):
        """Test that readSenderReceiverInterface method exists and is callable."""
        parser = PortInterfaceParser()
        assert callable(parser.readSenderReceiverInterface)
        assert hasattr(parser.readSenderReceiverInterface, '__self__')

    def test_all_port_interface_methods_exist(self):
        """Test that all PortInterface methods exist."""
        parser = PortInterfaceParser()

        # Port Interface Types
        port_interface_methods = [
            'readSenderReceiverInterface',
            'readClientServerInterface',
            'readParameterInterface',
            'readDataInterface',
            'readTriggerInterface',
            'readModeSwitchInterface',
            'readPortInterface',
        ]

        # Port Prototypes
        port_prototype_methods = [
            'readPPortPrototype',
            'readRPortPrototype',
            'readPRPortPrototype',
            'readAbstractProvidedPortPrototype',
            'readAbstractRequiredPortPrototype',
            'readSwComponentTypePorts',
            'readPortPrototypeBlueprint',
            'readFramePort',
            'readIPduPort',
            'readISignalPort',
            'readCommConnectorPort',
            'readCouplingPort',
        ]

        # Communication Specs
        communication_spec_methods = [
            'readPPortComSpec',
            'readRPortComSpec',
            'readProvidedComSpec',
            'readRequiredComSpec',
            'readSenderComSpec',
        ]

        # ClientServer Operations
        client_server_methods = [
            'readClientServerOperation',
            'readClientServerOperationArguments',
            'readClientServerInterfaceOperations',
            'readPossibleErrors',
            'readPossibleErrorRefs',
        ]

        # SenderReceiver Data Elements
        sender_receiver_methods = [
            'readSenderReceiverInterfaceDataElements',
            'readSenderReceiverInterfaceInvalidationPolicies',
            'readInvalidationPolicys',
        ]

        # Mode Switch Related
        mode_switch_methods = [
            'readModeDeclarationGroup',
            'readModeDeclarationGroupModeDeclaration',
            'readModeSwitchInterfaceModeGroup',
            'readModeDeclarationMapping',
            'readModeDeclarationMappingFirstModeRefs',
            'readModeDeclarationMappingSet',
            'readModeDeclarationMappingSetModeDeclarationMappings',
            'readModeInterfaceMapping',
            'readModeInterfaceMappingModeMapping',
            'readSwcModeSwitchEvent',
            'readBswModeSwitchEvent',
            'readModeSwitchedAckEvent',
            'readModeSwitchPoint',
            'readModeSwitchPointModeGroupIRef',
            'readRunnableEntityModeSwitchPoints',
        ]

        # Port Groups
        port_group_methods = [
            'readPortGroup',
            'readPortGroupInnerGroupIRefs',
            'readPortGroupOuterPortRefs',
            'readSwComponentTypePortGroups',
        ]

        # Connector Methods
        connector_methods = [
            'readPPortInCompositionInstanceRef',
            'readRPortInCompositionInstanceRef',
            'readDelegationSwConnectorInnerPortIRef',
            'readCommunicationConnectorEcuCommPortInstances',
            'readCouplingPortScheduler',
            'readCouplingPortFifo',
            'readCouplingPortSchedulerCouplingPortStructuralElement',
            'readCouplingPortDetailsCouplingPortStructuralElements',
            'readCouplingPortDetailsEthernetPriorityRegenerations',
            'readCouplingPortVlanMemberships',
            'readEthernetCommunicationControllerCouplingPorts',
        ]

        # Interface Mappings
        interface_mapping_methods = [
            'readPortInterfaceMappingSet',
            'readPortInterfaceMappings',
            'readClientServerInterfaceMapping',
            'readClientServerInterfaceMappingOperationMappings',
            'readClientServerOperationMapping',
            'readVariableAndParameterInterfaceMapping',
            'readModeInterfaceMapping',
            'readSenderReceiverToSignalMapping',
            'readSenderReceiverToSignalGroupMapping',
            'readSenderReceiverToSignalGroupMappingTypeMapping',
            'readSenderRecRecordTypeMapping',
            'readSenderRecArrayTypeMappingRecordElementMapping',
            'readSenderRecRecordElementMapping',
            'readSenderRecCompositeTypeMapping',
        ]

        # Frame Triggering
        frame_triggering_methods = [
            'readFrameTriggering',
            'readCanFrameTriggering',
            'readLinFrameTriggering',
            'readFlexrayFrameTriggering',
            'readFlexrayFrameTriggeringAbsolutelyScheduledTimings',
            'readISignalTriggering',
            'readPduTriggering',
            'readPhysicalChannelFrameTriggerings',
            'readPhysicalChannelISignalTriggerings',
            'readPhysicalChannelPduTriggerings',
        ]

        # Mode Declaration/Group
        mode_declaration_methods = [
            'readModeDeclarationGroupPrototype',
            'readIncludedModeDeclarationGroupSet',
            'readSwcInternalBehaviorIncludedModeDeclarationGroupSets',
            'readBswModuleDescriptionProvidedModeGroups',
            'readBswModuleDescriptionRequiredModeGroups',
            'readBswModuleEntityManagedModeGroups',
        ]

        # Parameter Interfaces
        parameter_interface_methods = [
            'readParameterInterfaceParameters',
            'readParameterDataPrototype',
            'readSwcInternalBehaviorPerInstanceParameters',
        ]

        # Additional Port-related methods
        additional_methods = [
            'readPortDefinedArgumentValue',
            'readRunnableEntityModeAccessPoints',
            'readModeAccessPoint',
        ]

        # Combine all methods
        all_methods = (
            port_interface_methods +
            port_prototype_methods +
            communication_spec_methods +
            client_server_methods +
            sender_receiver_methods +
            mode_switch_methods +
            port_group_methods +
            connector_methods +
            interface_mapping_methods +
            frame_triggering_methods +
            mode_declaration_methods +
            parameter_interface_methods +
            additional_methods
        )

        for method_name in all_methods:
            assert hasattr(parser, method_name), \
                f"Missing method: {method_name}"
            assert callable(getattr(parser, method_name)), \
                f"Method {method_name} is not callable"
