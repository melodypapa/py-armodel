from armodel.models.M2.AUTOSARTemplates.SystemTemplate import (
    SwcToEcuMapping,
    ComManagementMapping,
    SystemMapping,
    RootSwCompositionPrototype,
    J1939SharedAddressCluster,
    System
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class TestSystemTemplate:
    """
    Test class for SystemTemplate __init__ module functionality.
    This class contains test methods for validating the behavior of
    system template classes, including their initialization,
    inheritance relationships, and property accessors.
    """

    def test_swc_to_ecu_mapping(self):
        """
        Test SwcToEcuMapping class functionality with method chaining and None handling.
        """
        parent = MockParent()
        mapping = SwcToEcuMapping(parent, "test_swc_to_ecu_mapping")

        # Test constructor
        assert mapping is not None

        # Test default values
        assert mapping.getComponentIRefs() == []
        assert mapping.getControlledHwElementRef() is None
        assert mapping.getEcuInstanceRef() is None
        assert mapping.getProcessingUnitRef() is None

        # Test setter/getter methods with method chaining
        mapping.setControlledHwElementRef("hw_element_ref")
        assert mapping.getControlledHwElementRef() == "hw_element_ref"
        assert mapping == mapping.setControlledHwElementRef("hw_element_ref")

        mapping.setEcuInstanceRef("ecu_ref")
        assert mapping.getEcuInstanceRef() == "ecu_ref"
        assert mapping == mapping.setEcuInstanceRef("ecu_ref")

        mapping.setProcessingUnitRef("processing_unit_ref")
        assert mapping.getProcessingUnitRef() == "processing_unit_ref"
        assert mapping == mapping.setProcessingUnitRef("processing_unit_ref")

        # Test addComponentIRef
        mapping.addComponentIRef("component_i_ref")
        assert "component_i_ref" in mapping.getComponentIRefs()
        assert mapping == mapping.addComponentIRef("component_i_ref2")

    def test_com_management_mapping(self):
        """
        Test ComManagementMapping class functionality with method chaining and None handling.
        """
        parent = MockParent()
        mapping = ComManagementMapping(parent, "test_com_management_mapping")

        # Test constructor
        assert mapping is not None

        # Test default values
        assert mapping.getComManagementGroupRefs() == []
        assert mapping.getComManagementPortGroupRefs() == []
        assert mapping.getPhysicalChannelRef() is None

        # Test setter/getter methods with method chaining - with None values
        assert mapping == mapping.setPhysicalChannelRef(None)
        assert mapping.getPhysicalChannelRef() is None

        # Test setter/getter methods with method chaining - with actual values
        mapping.setPhysicalChannelRef("channel_ref")
        assert mapping.getPhysicalChannelRef() == "channel_ref"
        assert mapping == mapping.setPhysicalChannelRef("channel_ref")

        # Test addComManagementGroupRef
        mapping.addComManagementGroupRef("group_ref")
        assert "group_ref" in mapping.getComManagementGroupRefs()
        assert mapping == mapping.addComManagementGroupRef("group_ref2")

        # Test addComManagementPortGroupRef
        mapping.addComManagementPortGroupRef("port_group_ref")
        assert "port_group_ref" in mapping.getComManagementPortGroupRefs()
        assert mapping == mapping.addComManagementPortGroupRef("port_group_ref2")

    def test_system_mapping(self):
        """
        Test SystemMapping class functionality.
        """
        parent = MockParent()
        mapping = SystemMapping(parent, "test_system_mapping")

        # Test constructor
        assert mapping is not None

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
        assert mapping.getSystemSignalGroupToComResourceMappings() == []
        assert mapping.getSystemSignalToComResourceMappings() == []

        # Test add methods
        mapping.addApplicationPartitionToEcuPartitionMapping("app_partition_mapping")
        assert "app_partition_mapping" in mapping.getApplicationPartitionToEcuPartitionMappings()
        assert mapping == mapping.addApplicationPartitionToEcuPartitionMapping("app_partition_mapping2")

        mapping.addAppOsTaskProxyToEcuTaskProxyMapping("app_task_mapping")
        assert "app_task_mapping" in mapping.getAppOsTaskProxyToEcuTaskProxyMappings()
        assert mapping == mapping.addAppOsTaskProxyToEcuTaskProxyMapping("app_task_mapping2")

        mapping.addComManagementMapping("com_management_mapping")
        assert "com_management_mapping" in mapping.getComManagementMappings()
        assert mapping == mapping.addComManagementMapping("com_management_mapping2")

        mapping.addCryptoServiceMapping("crypto_service_mapping")
        assert "crypto_service_mapping" in mapping.getCryptoServiceMappings()
        assert mapping == mapping.addCryptoServiceMapping("crypto_service_mapping2")

        mapping.addDataMapping("data_mapping")
        assert "data_mapping" in mapping.getDataMappings()
        assert mapping == mapping.addDataMapping("data_mapping2")

        mapping.addDdsISignalToTopicMapping("dds_mapping")
        assert "dds_mapping" in mapping.getDdsISignalToTopicMapping()
        assert mapping == mapping.addDdsISignalToTopicMapping("dds_mapping2")

        mapping.addJ1939ControllerApplicationToJ1939NmNodeMapping("j1939_mapping")
        assert "j1939_mapping" in mapping.getJ1939ControllerApplicationToJ1939NmNodeMappings()
        assert mapping == mapping.addJ1939ControllerApplicationToJ1939NmNodeMapping("j1939_mapping2")

        mapping.addMappingConstraint("constraint")
        assert "constraint" in mapping.getMappingConstraints()
        assert mapping == mapping.addMappingConstraint("constraint2")

        mapping.addPncMapping("pnc_mapping")
        assert "pnc_mapping" in mapping.getPncMappings()
        assert mapping == mapping.addPncMapping("pnc_mapping2")

        mapping.addPortElementToComResourceMapping("port_mapping")
        assert "port_mapping" in mapping.getPortElementToComResourceMappings()
        assert mapping == mapping.addPortElementToComResourceMapping("port_mapping2")

        mapping.addResourceEstimation("resource_estimation")
        assert "resource_estimation" in mapping.getResourceEstimations()
        assert mapping == mapping.addResourceEstimation("resource_estimation2")

        mapping.addResourceToApplicationPartitionMapping("resource_app_mapping")
        assert "resource_app_mapping" in mapping.getResourceToApplicationPartitionMappings()
        assert mapping == mapping.addResourceToApplicationPartitionMapping("resource_app_mapping2")

        mapping.addRteEventSeparation("rte_event_separation")
        assert "rte_event_separation" in mapping.getRteEventSeparations()
        assert mapping == mapping.addRteEventSeparation("rte_event_separation2")

        mapping.addRteEventToOsTaskProxyMapping("rte_os_mapping")
        assert "rte_os_mapping" in mapping.getRteEventToOsTaskProxyMappings()
        assert mapping == mapping.addRteEventToOsTaskProxyMapping("rte_os_mapping2")

        mapping.addSignalPathConstraint("signal_constraint")
        assert "signal_constraint" in mapping.getSignalPathConstraints()
        assert mapping == mapping.addSignalPathConstraint("signal_constraint2")

        mapping.addSoftwareClusterToApplicationPartitionMapping("sw_cluster_app_mapping")
        assert "sw_cluster_app_mapping" in mapping.getSoftwareClusterToApplicationPartitionMappings()
        assert mapping == mapping.addSoftwareClusterToApplicationPartitionMapping("sw_cluster_app_mapping2")

        mapping.addSoftwareClusterToResourceMapping("sw_cluster_resource_mapping")
        assert "sw_cluster_resource_mapping" in mapping.getSoftwareClusterToResourceMappings()
        assert mapping == mapping.addSoftwareClusterToResourceMapping("sw_cluster_resource_mapping2")

        mapping.addSwClusterMapping("sw_cluster_mapping")
        assert "sw_cluster_mapping" in mapping.getSwClusterMappings()
        assert mapping == mapping.addSwClusterMapping("sw_cluster_mapping2")

        mapping.addSwcToApplicationPartitionMappings("swc_app_mapping")
        assert "swc_app_mapping" in mapping.getSwcToApplicationPartitionMappings()
        assert mapping == mapping.addSwcToApplicationPartitionMappings("swc_app_mapping2")

        mapping.addSystemSignalGroupToComResourceMapping("signal_group_mapping")
        assert "signal_group_mapping" in mapping.getSystemSignalGroupToComResourceMappings()
        assert mapping == mapping.addSystemSignalGroupToComResourceMapping("signal_group_mapping2")

        mapping.addSystemSignalToComResourceMapping("signal_mapping")
        assert "signal_mapping" in mapping.getSystemSignalToComResourceMappings()
        assert mapping == mapping.addSystemSignalToComResourceMapping("signal_mapping2")

        # Test create methods
        ecu_mapping = mapping.createECUMapping("ecu_mapping_name")
        assert ecu_mapping is not None
        assert ecu_mapping in mapping.getEcuResourceMappings()

        impl_mapping = mapping.createSwcToImplMapping("impl_mapping_name")
        assert impl_mapping is not None
        assert impl_mapping in mapping.getSwImplMappings()

        swc_mapping = mapping.createSwcToEcuMapping("swc_mapping_name")
        assert swc_mapping is not None
        assert swc_mapping in mapping.getSwMappings()

        # Test getSwcToEcuMappings to cover line 291
        swc_to_ecu_mappings = mapping.getSwcToEcuMappings()
        assert swc_mapping in swc_to_ecu_mappings
        assert isinstance(swc_to_ecu_mappings, list)

    def test_root_sw_composition_prototype(self):
        """
        Test RootSwCompositionPrototype class functionality with method chaining.
        """
        parent = MockParent()
        prototype = RootSwCompositionPrototype(parent, "test_root_sw_composition_prototype")

        # Test constructor
        assert prototype is not None

        # Test default values
        assert prototype.getCalibrationParameterValueSetRef() is None
        assert prototype.getFlatMapRef() is None
        assert prototype.getSoftwareCompositionTRef() is None

        # Test setter/getter methods with method chaining
        prototype.setCalibrationParameterValueSetRef("calibration_ref")
        assert prototype.getCalibrationParameterValueSetRef() == "calibration_ref"
        assert prototype == prototype.setCalibrationParameterValueSetRef("calibration_ref")

        prototype.setFlatMapRef("flat_map_ref")
        assert prototype.getFlatMapRef() == "flat_map_ref"
        assert prototype == prototype.setFlatMapRef("flat_map_ref")

        prototype.setSoftwareCompositionTRef("sw_composition_ref")
        assert prototype.getSoftwareCompositionTRef() == "sw_composition_ref"
        assert prototype == prototype.setSoftwareCompositionTRef("sw_composition_ref")

    def test_j1939_shared_address_cluster(self):
        """
        Test J1939SharedAddressCluster class functionality with method chaining and None handling.
        """
        parent = MockParent()
        cluster = J1939SharedAddressCluster(parent, "test_j1939_shared_address_cluster")

        # Test constructor
        assert cluster is not None

        # Test default values
        assert cluster.getParticipatingJ1939ClusterRefs() == []

        # Test setter/getter methods with method chaining - with None values
        assert cluster == cluster.addParticipatingJ1939ClusterRef(None)
        assert len(cluster.getParticipatingJ1939ClusterRefs()) == 0

        # Test addParticipatingJ1939ClusterRef with actual values
        cluster.addParticipatingJ1939ClusterRef("j1939_cluster_ref")
        assert "j1939_cluster_ref" in cluster.getParticipatingJ1939ClusterRefs()
        assert cluster == cluster.addParticipatingJ1939ClusterRef("j1939_cluster_ref2")

    def test_system(self):
        """
        Test System class functionality with method chaining and None handling.
        """
        parent = MockParent()
        system = System(parent, "test_system")

        # Test constructor
        assert system is not None

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

        # Test setter/getter methods with method chaining
        system.setContainerIPduHeaderByteOrder("big_endian")
        assert system.getContainerIPduHeaderByteOrder() == "big_endian"
        assert system == system.setContainerIPduHeaderByteOrder("big_endian")

        system.setEcuExtractVersion("1.0.0")
        assert system.getEcuExtractVersion() == "1.0.0"
        assert system == system.setEcuExtractVersion("1.0.0")

        system.setPncVectorLength(8)
        assert system.getPncVectorLength() == 8
        assert system == system.setPncVectorLength(8)

        system.setPncVectorOffset(4)
        assert system.getPncVectorOffset() == 4
        assert system == system.setPncVectorOffset(4)

        system.setSystemVersion("2.0.0")
        assert system.getSystemVersion() == "2.0.0"
        assert system == system.setSystemVersion("2.0.0")

        system.setSystemDocumentation(["doc1", "doc2"])
        assert system.getSystemDocumentation() == ["doc1", "doc2"]
        assert system == system.setSystemDocumentation(["doc1", "doc2"])

        # Test add methods
        system.addClientIdDefinitionSetRefs("client_def_ref")
        assert "client_def_ref" in system.getClientIdDefinitionSetRefs()
        assert system == system.addClientIdDefinitionSetRefs("client_def_ref2")

        system.addFibexElementRef("fibex_ref")
        assert "fibex_ref" in system.getFibexElementRefs()
        assert system == system.addFibexElementRef("fibex_ref2")

        system.addInterpolationRoutineMappingSetRefs("interp_mapping_ref")
        assert "interp_mapping_ref" in system.getInterpolationRoutineMappingSetRefs()
        assert system == system.addInterpolationRoutineMappingSetRefs("interp_mapping_ref2")

        system.addSwClusterRef("sw_cluster_ref")
        assert "sw_cluster_ref" in system.getSwClusterRefs()
        assert system == system.addSwClusterRef("sw_cluster_ref2")

        # Test create methods
        mapping = system.createSystemMapping("mapping_name")
        assert mapping is not None
        assert mapping in system.getMappings()

        # Test getSystemMappings to cover line 441
        system_mappings = system.getSystemMappings()
        assert mapping in system_mappings
        assert isinstance(system_mappings, list)

        prototype = system.createRootSoftwareComposition("prototype_name")
        assert prototype is not None
        assert system.getRootSoftwareComposition() == prototype

        # Test setJ1939SharedAddressClusters
        cluster = J1939SharedAddressCluster(parent, "cluster_name")
        system.setJ1939SharedAddressClusters(cluster)
        assert cluster in system.getJ1939SharedAddressClusters()
        assert system == system.setJ1939SharedAddressClusters(cluster)