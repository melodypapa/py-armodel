"""
Test suite for main SystemTemplate classes in AUTOSAR System Template.

This module contains comprehensive unit tests for core SystemTemplate classes
including SwcToEcuMapping, ComManagementMapping, SystemMapping, RootSwCompositionPrototype,
J1939SharedAddressCluster, and System. Each test validates the functionality,
inheritance, and setter/getter methods of the respective classes.
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.SystemTemplate import (
    SwcToEcuMapping,
    ComManagementMapping,
    SystemMapping,
    RootSwCompositionPrototype,
    J1939SharedAddressCluster,
    System
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable, ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import ComponentInSystemInstanceRef


class MockParent(ARObject):
    """
    Mock parent class for testing purposes.
    
    This class extends ARObject to provide a concrete implementation
    that can be used as a parent for testing classes that require
    an ARObject instance during initialization.
    """
    def __init__(self):
        super().__init__()


class Test_SystemTemplate:
    """
    Test class for main SystemTemplate module functionality.
    
    This class contains test methods for validating the behavior of
    core SystemTemplate classes, including their initialization,
    inheritance relationships, and property accessors.
    """
    
    def test_SwcToEcuMapping(self):
        """
        Test SwcToEcuMapping class functionality.
        
        This test validates that SwcToEcuMapping can be instantiated,
        properly inherits from Identifiable, and that its setter/getter methods
        work correctly for ECU mapping properties.
        """
        parent = MockParent()
        mapping = SwcToEcuMapping(parent, "test_swcec_mapping")

        assert isinstance(mapping, Identifiable)
        
        # Test default values
        assert mapping.getComponentIRefs() == []
        assert mapping.getControlledHwElementRef() is None
        assert mapping.getEcuInstanceRef() is None
        assert mapping.getProcessingUnitRef() is None
        
        # Test setter/getter methods
        mock_hw_element_ref = "hw_element_ref"
        mapping.setControlledHwElementRef(mock_hw_element_ref)
        assert mapping.getControlledHwElementRef() == mock_hw_element_ref
        
        mock_ecu_instance_ref = "ecu_instance_ref"
        mapping.setEcuInstanceRef(mock_ecu_instance_ref)
        assert mapping.getEcuInstanceRef() == mock_ecu_instance_ref
        
        mock_processing_unit_ref = "processing_unit_ref"
        mapping.setProcessingUnitRef(mock_processing_unit_ref)
        assert mapping.getProcessingUnitRef() == mock_processing_unit_ref
        
        # Test adding component IRefs
        mock_comp_ref = ComponentInSystemInstanceRef()
        mapping.addComponentIRef(mock_comp_ref)
        assert mapping.getComponentIRefs() == [mock_comp_ref]

    def test_ComManagementMapping(self):
        """
        Test ComManagementMapping class functionality.
        
        This test verifies that ComManagementMapping is properly instantiated,
        inherits from Identifiable, and that all its reference collections
        can be accessed and modified correctly.
        """
        parent = MockParent()
        mapping = ComManagementMapping(parent, "test_com_management_mapping")

        assert isinstance(mapping, Identifiable)
        
        # Test default values
        assert mapping.getComManagementGroupRefs() == []
        assert mapping.getComManagementPortGroupRefs() == []
        assert mapping.getPhysicalChannelRef() is None
        
        # Test setter/getter methods
        mock_channel_ref = "channel_ref"
        mapping.setPhysicalChannelRef(mock_channel_ref)
        assert mapping.getPhysicalChannelRef() == mock_channel_ref
        
        # Test adding management group refs
        mock_group_ref = "group_ref"
        mapping.addComManagementGroupRef(mock_group_ref)
        assert mapping.getComManagementGroupRefs() == [mock_group_ref]
        
        # Test adding management port group refs
        mock_port_group_ref = "port_group_ref"
        mapping.addComManagementPortGroupRef(mock_port_group_ref)
        assert mapping.getComManagementPortGroupRefs() == [mock_port_group_ref]

    def test_SystemMapping(self):
        """
        Test SystemMapping class functionality.
        
        This test ensures that SystemMapping can be instantiated with a parent,
        inherits from Identifiable, and that all its various mapping collections
        are properly initialized as empty lists.
        """
        parent = MockParent()
        mapping = SystemMapping(parent, "test_system_mapping")

        assert isinstance(mapping, Identifiable)
        
        # Test default values
        assert mapping.getApplicationPartitionToEcuPartitionMappings() == []
        assert mapping.getAppOsTaskProxyToEcuTaskProxyMappings() == []
        assert mapping.getComManagementMappings() == []
        assert mapping.getCryptoServiceMappings() == []
        assert mapping.getDataMappings() == []
        assert mapping.getDdsISignalToTopicMapping() == []
        assert mapping.getEcuResourceMappings() == []
        assert mapping.getJ1939ControllerApplicationToJ1939NmNodeMappings() == []
        assert mapping.getMappingConstraints() == []
        assert mapping.getPncMappings() == []
        assert mapping.getPortElementToComResourceMappings() == []
        assert mapping.getResourceEstimations() == []
        assert mapping.getResourceToApplicationPartitionMappings() == []
        assert mapping.getRteEventSeparations() == []
        assert mapping.getRteEventToOsTaskProxyMappings() == []
        assert mapping.getSignalPathConstraints() == []
        assert mapping.getSoftwareClusterToApplicationPartitionMappings() == []
        assert mapping.getSoftwareClusterToResourceMappings() == []
        assert mapping.getSwClusterMappings() == []
        assert mapping.getSwcToApplicationPartitionMappings() == []
        assert mapping.getSwImplMappings() == []
        assert mapping.getSwMappings() == []

    def test_RootSwCompositionPrototype(self):
        """
        Test RootSwCompositionPrototype class functionality.
        
        This test validates that RootSwCompositionPrototype can be instantiated,
        inherits from Identifiable, and that its reference properties can be
        set and retrieved correctly.
        """
        parent = MockParent()
        prototype = RootSwCompositionPrototype(parent, "test_root_sw_comp_proto")

        assert isinstance(prototype, Identifiable)
        
        # Test default values
        assert prototype.getCalibrationParameterValueSetRef() is None
        assert prototype.getFlatMapRef() is None
        assert prototype.getSoftwareCompositionTRef() is None
        
        # Test setter/getter methods
        prototype.setCalibrationParameterValueSetRef("cal_param_ref")
        assert prototype.getCalibrationParameterValueSetRef() == "cal_param_ref"
        
        prototype.setFlatMapRef("flat_map_ref")
        assert prototype.getFlatMapRef() == "flat_map_ref"
        
        prototype.setSoftwareCompositionTRef("comp_t_ref")
        assert prototype.getSoftwareCompositionTRef() == "comp_t_ref"

    def test_J1939SharedAddressCluster(self):
        """
        Test J1939SharedAddressCluster class functionality.
        
        This test verifies that J1939SharedAddressCluster can be instantiated,
        inherits from Identifiable, and that its cluster reference collection
        can be modified correctly.
        """
        parent = MockParent()
        cluster = J1939SharedAddressCluster(parent, "test_j1939_shared_addr_cluster")

        assert isinstance(cluster, Identifiable)
        
        # Test default values
        assert cluster.getParticipatingJ1939ClusterRefs() == []
        
        # Test adding cluster refs
        mock_cluster_ref = "cluster_ref"
        cluster.addParticipatingJ1939ClusterRef(mock_cluster_ref)
        assert cluster.getParticipatingJ1939ClusterRefs() == [mock_cluster_ref]

    def test_System(self):
        """
        Test System class functionality.
        
        This test ensures that System can be instantiated with a parent,
        inherits from ARElement, and that all its properties and collections
        are properly initialized and accessible.
        """
        parent = MockParent()
        system = System(parent, "test_system")

        assert isinstance(system, ARElement)
        
        # Test default values
        assert system.getClientIdDefinitionSetRefs() == []
        assert system.getContainerIPduHeaderByteOrder() is None
        assert system.getEcuExtractVersion() is None
        assert system.getFibexElementRefs() == []
        assert system.getInterpolationRoutineMappingSetRefs() == []
        assert system.getJ1939SharedAddressClusters() == []
        assert system.getMappings() == []
        assert system.getPncVectorLength() is None
        assert system.getPncVectorOffset() is None
        assert system.getRootSoftwareComposition() is None
        assert system.getSwClusterRefs() == []
        assert system.getSystemDocumentation() == []
        assert system.getSystemVersion() is None
        
        # Test adding client ID definition refs
        mock_client_id_ref = "client_id_ref"
        system.addClientIdDefinitionSetRefs(mock_client_id_ref)
        assert system.getClientIdDefinitionSetRefs() == [mock_client_id_ref]
        
        # Test adding fibex element refs
        mock_fibex_ref = "fibex_ref"
        system.addFibexElementRef(mock_fibex_ref)
        assert system.getFibexElementRefs() == [mock_fibex_ref]
        
        # Test adding interpolation routine refs
        mock_interp_ref = "interp_ref"
        system.addInterpolationRoutineMappingSetRefs(mock_interp_ref)
        assert system.getInterpolationRoutineMappingSetRefs() == [mock_interp_ref]