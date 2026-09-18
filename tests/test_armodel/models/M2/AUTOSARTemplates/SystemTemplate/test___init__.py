from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import AtpBlueprintable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpPrototype
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ByteOrderEnum, PositiveInteger, RefType, RevisionLabelString
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import ComManagementMapping, J1939SharedAddressCluster, RootSwCompositionPrototype, SwcToEcuMapping, System, SystemMapping


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
        Test RootSwCompositionPrototype class functionality with method chaining and None handling.
        """
        parent = MockParent()
        prototype = RootSwCompositionPrototype(parent, "test_root_sw_composition_prototype")

        # Test inherited from AtpPrototype
        assert isinstance(prototype, AtpPrototype)

        # Heritage drift (AtpPrototype re-parented AtpBlueprintable -> AtpFeature):
        # RootSwCompositionPrototype's spec Base closure excludes AtpBlueprintable,
        # so losing it transitively through AtpPrototype is spec-correct.
        assert type(prototype).__bases__[0] is AtpPrototype
        assert AtpBlueprintable not in type(prototype).__mro__
        assert issubclass(RootSwCompositionPrototype, Identifiable)
        assert issubclass(RootSwCompositionPrototype, ARObject)

        # Test default values
        assert prototype.getCalibrationParameterValueSetRefs() == []
        assert prototype.getFlatMapRef() is None
        assert prototype.getSoftwareCompositionTRef() is None

        # Test add/get calibrationParameterValueSetRefs
        prototype.addCalibrationParameterValueSetRef("/t/f/CalibrationParameterValueSet")
        prototype.addCalibrationParameterValueSetRef("/t/f/CalibrationParameterValueSet2")
        assert prototype.getCalibrationParameterValueSetRefs() == [
            "/t/f/CalibrationParameterValueSet",
            "/t/f/CalibrationParameterValueSet2",
        ]
        prototype.addCalibrationParameterValueSetRef(None)
        assert len(prototype.getCalibrationParameterValueSetRefs()) == 2

        # Test setter/getter methods with method chaining
        prototype.setFlatMapRef("/t/f/FlatMap")
        assert prototype.getFlatMapRef() == "/t/f/FlatMap"
        assert prototype == prototype.setFlatMapRef("/t/f/FlatMap")
        prototype.setFlatMapRef(None)
        assert prototype.getFlatMapRef() == "/t/f/FlatMap"

        prototype.setSoftwareCompositionTRef("/t/f/CompositionSwComponentType")
        assert prototype.getSoftwareCompositionTRef() == "/t/f/CompositionSwComponentType"
        assert prototype == prototype.setSoftwareCompositionTRef("/t/f/CompositionSwComponentType")
        prototype.setSoftwareCompositionTRef(None)
        assert prototype.getSoftwareCompositionTRef() == "/t/f/CompositionSwComponentType"

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

    def test_system_initialization(self):
        """
        Test System class default values after initialization.
        """
        parent = MockParent()
        system = System(parent, "test_system")

        assert system is not None

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
        assert system.getSystemDocumentations() == []
        assert system.getSystemVersion() is None

    def test_system_get_set_attributes(self):
        """
        Test System scalar attribute getter/setter pairs with method chaining and None no-op.
        """
        parent = MockParent()
        system = System(parent, "test_system")

        byte_order = ByteOrderEnum().setValue(ByteOrderEnum.MOST_SIGNIFICANT_BYTE_FIRST)
        assert system == system.setContainerIPduHeaderByteOrder(byte_order)
        assert system.getContainerIPduHeaderByteOrder() is byte_order
        system.setContainerIPduHeaderByteOrder(None)
        assert system.getContainerIPduHeaderByteOrder() is byte_order

        ecu_extract_version = RevisionLabelString().setValue("1.0.0")
        assert system == system.setEcuExtractVersion(ecu_extract_version)
        assert system.getEcuExtractVersion() is ecu_extract_version
        system.setEcuExtractVersion(None)
        assert system.getEcuExtractVersion() is ecu_extract_version

        pnc_vector_length = PositiveInteger().setValue("8")
        assert system == system.setPncVectorLength(pnc_vector_length)
        assert system.getPncVectorLength().getValue() == 8
        system.setPncVectorLength(None)
        assert system.getPncVectorLength().getValue() == 8

        pnc_vector_offset = PositiveInteger().setValue("4")
        assert system == system.setPncVectorOffset(pnc_vector_offset)
        assert system.getPncVectorOffset().getValue() == 4
        system.setPncVectorOffset(None)
        assert system.getPncVectorOffset().getValue() == 4

        system_version = RevisionLabelString().setValue("2.0.0")
        assert system == system.setSystemVersion(system_version)
        assert system.getSystemVersion() is system_version
        system.setSystemVersion(None)
        assert system.getSystemVersion() is system_version

    def test_system_add_refs(self):
        """
        Test System reference list adders with appending, chaining and None no-op.
        """
        parent = MockParent()
        system = System(parent, "test_system")

        client_id_definition_set_ref = RefType().setValue("/Systems/ClientIdDefinitionSet")
        assert system == system.addClientIdDefinitionSetRef(client_id_definition_set_ref)
        assert system.getClientIdDefinitionSetRefs() == [client_id_definition_set_ref]
        assert system == system.addClientIdDefinitionSetRef(None)
        assert len(system.getClientIdDefinitionSetRefs()) == 1

        fibex_element_ref = RefType().setValue("/CanSystem/CLUSTERS/CanNetwork")
        assert system == system.addFibexElementRef(fibex_element_ref)
        assert system.getFibexElementRefs() == [fibex_element_ref]
        assert system == system.addFibexElementRef(None)
        assert len(system.getFibexElementRefs()) == 1

        interpolation_routine_mapping_set_ref = RefType().setValue("/Systems/InterpolationRoutineMappingSet")
        assert system == system.addInterpolationRoutineMappingSetRef(interpolation_routine_mapping_set_ref)
        assert system.getInterpolationRoutineMappingSetRefs() == [interpolation_routine_mapping_set_ref]
        assert system == system.addInterpolationRoutineMappingSetRef(None)
        assert len(system.getInterpolationRoutineMappingSetRefs()) == 1

        sw_cluster_ref = RefType().setValue("/Systems/CpSoftwareCluster")
        assert system == system.addSwClusterRef(sw_cluster_ref)
        assert system.getSwClusterRefs() == [sw_cluster_ref]
        assert system == system.addSwClusterRef(None)
        assert len(system.getSwClusterRefs()) == 1

    def test_system_create_aggregates(self):
        """
        Test System aggregate factories: appending, duplicate returns existing, dedicated list fields.
        """
        parent = MockParent()
        system = System(parent, "test_system")

        mapping = system.createSystemMapping("mapping_name")
        assert mapping is not None
        assert system.getMappings() == [mapping]
        assert system.createSystemMapping("mapping_name") is mapping

        prototype = system.createRootSoftwareComposition("prototype_name")
        assert prototype is not None
        assert system.getRootSoftwareComposition() is prototype
        assert system.createRootSoftwareComposition("prototype_name") is prototype

        cluster = system.createJ1939SharedAddressCluster("cluster_name")
        assert cluster is not None
        assert system.getJ1939SharedAddressClusters() == [cluster]
        assert system.createJ1939SharedAddressCluster("cluster_name") is cluster

        chapter = system.createSystemDocumentation("chapter_name")
        assert chapter is not None
        assert system.getSystemDocumentations() == [chapter]
        assert system.createSystemDocumentation("chapter_name") is chapter
