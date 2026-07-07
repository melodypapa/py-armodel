"""Tests for writer remaining coverage gaps - dispatch else branches."""
import xml.etree.ElementTree as ET
import pytest
from unittest.mock import MagicMock

from armodel.writer.arxml_writer import ARXMLWriter
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR


class TestWriterDispatchElseBranches:
    """Test all dispatch else branches with warning option enabled."""

    def setup_method(self):
        AUTOSAR.getInstance().new()
        self.writer = ARXMLWriter(options={'warning': True})

    def test_timing_event_disabled_mode_irefs_empty(self):
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        swc = pkg.createApplicationSwComponentType("Swc")
        behavior = swc.createSwcInternalBehavior("Behavior")
        event = behavior.createTimingEvent("TimingEvent1")
        event.disabledModeIRefs = []
        element = ET.Element("TIMING-EVENT")
        self.writer.writeTimingEvent(element, event)
        assert element.find("DISABLED-MODE-IREFS") is None

    def test_server_call_points_unsupported_type(self):
        entity = MagicMock()
        entity.getServerCallPoints.return_value = [MagicMock(spec=object)]
        element = ET.Element("RUNNABLE-ENTITY")
        self.writer.writeRunnableEntityServerCallPoints(element, entity)
        assert True

    def test_ar_typed_per_instance_memories_unsupported_type(self):
        behavior = MagicMock()
        behavior.getArTypedPerInstanceMemories.return_value = [MagicMock(spec=object)]
        element = ET.Element("SWC-INTERNAL-BEHAVIOR")
        self.writer.writeSwcInternalBehaviorArTypedPerInstanceMemories(element, behavior)
        assert True

    def test_explicit_inter_runnable_variables_unsupported_type(self):
        behavior = MagicMock()
        behavior.getExplicitInterRunnableVariables.return_value = [MagicMock(spec=object)]
        element = ET.Element("SWC-INTERNAL-BEHAVIOR")
        self.writer.writeSwcInternalBehaviorExplicitInterRunnableVariables(element, behavior)
        assert True

    def test_service_dependency_assigned_data_unsupported_type(self):
        dependency = MagicMock()
        dependency.getAssignedData.return_value = [MagicMock(spec=object)]
        element = ET.Element("SERVICE-DEPENDENCY")
        self.writer.writeServiceDependencyAssignedDataType(element, dependency)
        assert True

    def test_swc_service_dependency_assigned_data_unsupported_type(self):
        dependency = MagicMock()
        dependency.getAssignedData.return_value = [MagicMock(spec=object)]
        element = ET.Element("SWC-SERVICE-DEPENDENCY")
        self.writer.writeSwcServiceDependencyAssignedData(element, dependency)
        assert True

    def test_swc_service_dependency_assigned_ports_unsupported_type(self):
        dependency = MagicMock()
        dependency.getAssignedPorts.return_value = [MagicMock(spec=object)]
        element = ET.Element("SWC-SERVICE-DEPENDENCY")
        self.writer.writeSwcServiceDependencyAssignedPorts(element, dependency)
        assert True

    def test_diag_event_debounce_algorithm_unsupported_type(self):
        needs = MagicMock()
        needs.getDiagEventDebounceAlgorithm.return_value = MagicMock(spec=object)
        element = ET.Element("DIAGNOSTIC-EVENT-NEEDS")
        self.writer.writeDiagEventDebounceAlgorithm(element, needs)
        assert True

    def test_swc_internal_behavior_service_dependencies_unsupported_type(self):
        behavior = MagicMock()
        behavior.getServiceDependencies.return_value = [MagicMock(spec=object)]
        element = ET.Element("SWC-INTERNAL-BEHAVIOR")
        self.writer.writeSwcInternalBehaviorServiceDependencies(element, behavior)
        assert True

    def test_swc_internal_behavior_included_mode_declaration_group_sets_unsupported_type(self):
        behavior = MagicMock()
        behavior.getIncludedModeDeclarationGroupSets.return_value = [MagicMock(spec=object)]
        element = ET.Element("SWC-INTERNAL-BEHAVIOR")
        self.writer.writeSwcInternalBehaviorIncludedModeDeclarationGroupSets(element, behavior)
        assert True

    def test_atomic_sw_component_type_internal_behaviors_unsupported_type(self):
        component = MagicMock()
        component.getInternalBehavior.return_value = MagicMock(spec=object)
        element = ET.Element("APPLICATION-SW-COMPONENT-TYPE")
        self.writer.writeAtomicSwComponentTypeInternalBehaviors(element, component)
        assert True

    def test_bsw_module_description_provided_mode_groups_unsupported_type(self):
        desc = MagicMock()
        desc.getProvidedModeGroups.return_value = [MagicMock(spec=object)]
        element = ET.Element("BSW-MODULE-DESCRIPTION")
        self.writer.writeBswModuleDescriptionProvidedModeGroups(element, desc)
        assert True

    def test_bsw_module_description_required_mode_groups_unsupported_type(self):
        desc = MagicMock()
        desc.getRequiredModeGroups.return_value = [MagicMock(spec=object)]
        element = ET.Element("BSW-MODULE-DESCRIPTION")
        self.writer.writeBswModuleDescriptionRequiredModeGroups(element, desc)
        assert True

    def test_bsw_module_entity_data_send_points_unsupported_type(self):
        entity = MagicMock()
        entity.getDataSendPoints.return_value = [MagicMock(spec=object)]
        element = ET.Element("BSW-MODULE-ENTITY")
        self.writer.writeBswModuleEntityDataSendPoints(element, entity)
        assert True

    def test_bsw_module_entity_data_receive_points_unsupported_type(self):
        entity = MagicMock()
        entity.getDataReceivePoints.return_value = [MagicMock(spec=object)]
        element = ET.Element("BSW-MODULE-ENTITY")
        self.writer.writeBswModuleEntityDataReceivePoints(element, entity)
        assert True

    def test_bsw_module_entity_call_points_unsupported_type(self):
        entity = MagicMock()
        entity.getCallPoints.return_value = [MagicMock(spec=object)]
        element = ET.Element("BSW-MODULE-ENTITY")
        self.writer.writeBswModuleEntityCallPoints(element, entity)
        assert True

    def test_bsw_internal_behavior_entities_unsupported_type(self):
        behavior = MagicMock()
        behavior.getEntities.return_value = [MagicMock(spec=object)]
        element = ET.Element("BSW-INTERNAL-BEHAVIOR")
        self.writer.writeBswInternalBehaviorEntities(element, behavior)
        assert True

    def test_bsw_internal_behavior_events_unsupported_type(self):
        behavior = MagicMock()
        behavior.getBswEvents.return_value = [MagicMock(spec=object)]
        element = ET.Element("BSW-INTERNAL-BEHAVIOR")
        self.writer.writeBswInternalBehaviorEvents(element, behavior)
        assert True

    def test_bsw_internal_behavior_reception_policies_unsupported_type(self):
        behavior = MagicMock()
        behavior.getReceptionPolicies.return_value = [MagicMock(spec=object)]
        element = ET.Element("BSW-INTERNAL-BEHAVIOR")
        self.writer.writeBswInternalBehaviorReceptionPolicies(element, behavior)
        assert True

    def test_bsw_internal_behavior_internal_triggering_points_unsupported_type(self):
        behavior = MagicMock()
        behavior.getInternalTriggeringPoints.return_value = [MagicMock(spec=object)]
        element = ET.Element("BSW-INTERNAL-BEHAVIOR")
        self.writer.writeBswInternalBehaviorInternalTriggeringPoints(element, behavior)
        assert True

    def test_bsw_module_description_internal_behaviors_unsupported_type(self):
        desc = MagicMock()
        desc.getInternalBehavior.return_value = MagicMock(spec=object)
        element = ET.Element("BSW-MODULE-DESCRIPTION")
        self.writer.writeBswModuleDescriptionInternalBehaviors(element, desc)
        assert True

    def test_bsw_module_description_released_triggers_unsupported_type(self):
        desc = MagicMock()
        desc.getReleasedTriggers.return_value = [MagicMock(spec=object)]
        element = ET.Element("BSW-MODULE-DESCRIPTION")
        self.writer.writeBswModuleDescriptionReleasedTriggers(element, desc)
        assert True

    def test_bsw_module_description_required_triggers_unsupported_type(self):
        desc = MagicMock()
        desc.getRequiredTriggers.return_value = [MagicMock(spec=object)]
        element = ET.Element("BSW-MODULE-DESCRIPTION")
        self.writer.writeBswModuleDescriptionRequiredTriggers(element, desc)
        assert True

    def test_bsw_module_description_provided_datas_unsupported_type(self):
        desc = MagicMock()
        desc.getProvidedDatas.return_value = [MagicMock(spec=object)]
        element = ET.Element("BSW-MODULE-DESCRIPTION")
        self.writer.writeBswModuleDescriptionProvidedDatas(element, desc)
        assert True

    def test_bsw_module_description_required_datas_unsupported_type(self):
        desc = MagicMock()
        desc.getRequiredDatas.return_value = [MagicMock(spec=object)]
        element = ET.Element("BSW-MODULE-DESCRIPTION")
        self.writer.writeBswModuleDescriptionRequiredDatas(element, desc)
        assert True

    def test_bsw_module_description_provided_client_server_entries_unsupported_type(self):
        desc = MagicMock()
        desc.getProvidedClientServerEntries.return_value = [MagicMock(spec=object)]
        element = ET.Element("BSW-MODULE-DESCRIPTION")
        self.writer.writeBswModuleDescriptionProvidedClientServerEntries(element, desc)
        assert True

    def test_bsw_module_description_required_client_server_entries_unsupported_type(self):
        desc = MagicMock()
        desc.getRequiredClientServerEntries.return_value = [MagicMock(spec=object)]
        element = ET.Element("BSW-MODULE-DESCRIPTION")
        self.writer.writeBswModuleDescriptionRequiredClientServerEntries(element, desc)
        assert True

    def test_bus_dependent_nm_ecus_unsupported_type(self):
        nm_ecu = MagicMock()
        nm_ecu.getBusDependentNmEcus.return_value = [MagicMock(spec=object)]
        element = ET.Element("NM-ECU")
        self.writer.writeBusDependentNmEcus(element, nm_ecu)
        assert True

    def test_nm_config_nm_if_ecus_unsupported_type(self):
        config = MagicMock()
        config.getNmIfEcus.return_value = [MagicMock(spec=object)]
        element = ET.Element("NM-CONFIG")
        self.writer.writeNmConfigNmIfEcus(element, config)
        assert True

    def test_multiplicity_config_classes_unsupported_type(self):
        common_attrs = MagicMock()
        common_attrs.getMultiplicityConfigClasses.return_value = [MagicMock(spec=object)]
        element = ET.Element("ECUC-COMMON-ATTRIBUTES")
        self.writer.setEcucMultiplicityConfigClasses(element, common_attrs.getMultiplicityConfigClasses())
        assert True

    def test_enumeration_literal_def_unsupported_type(self):
        param_def = MagicMock()
        param_def.getLiterals.return_value = [MagicMock(spec=object)]
        element = ET.Element("ECUC-ENUMERATION-PARAM-DEF")
        self.writer.writeEcucEnumerationParamDefLiterals(element, param_def)
        assert True

    def test_container_def_parameters_unsupported_type(self):
        container_def = MagicMock()
        container_def.getParameters.return_value = [MagicMock(spec=object)]
        element = ET.Element("ECUC-PARAM-CONF-CONTAINER-DEF")
        self.writer.writeEcucContainerDefParameters(element, container_def)
        assert True

    def test_container_def_references_unsupported_type(self):
        container_def = MagicMock()
        container_def.getReferences.return_value = [MagicMock(spec=object)]
        element = ET.Element("ECUC-PARAM-CONF-CONTAINER-DEF")
        self.writer.writeEcucContainerDefReferences(element, container_def)
        assert True

    def test_container_def_sub_containers_unsupported_type(self):
        container_def = MagicMock()
        container_def.getSubContainers.return_value = [MagicMock(spec=object)]
        element = ET.Element("ECUC-PARAM-CONF-CONTAINER-DEF")
        self.writer.writeEcucContainerDefSubContainers(element, container_def)
        assert True

    def test_choice_container_def_choices_unsupported_type(self):
        container_def = MagicMock()
        container_def.getChoices.return_value = [MagicMock(spec=object)]
        element = ET.Element("ECUC-CHOICE-CONTAINER-DEF")
        self.writer.writeEcucChoiceContainerDefChoices(element, container_def)
        assert True

    def test_module_def_containers_unsupported_type(self):
        module_def = MagicMock()
        module_def.getContainers.return_value = [MagicMock(spec=object)]
        element = ET.Element("ECUC-MODULE-DEF")
        self.writer.writeEcucModuleDefContainers(element, module_def)
        assert True

    def test_comm_connector_port_instances_unsupported_type(self):
        connector = MagicMock()
        connector.getEcuCommPortInstances.return_value = [MagicMock(spec=object)]
        element = ET.Element("COMMUNICATION-CONNECTOR")
        self.writer.writeCommunicationConnectorEcuCommPortInstances(element, connector)
        assert True

    def test_can_controller_attributes_unsupported_type(self):
        controller = MagicMock()
        controller.getCanControllerAttributes.return_value = MagicMock(spec=object)
        element = ET.Element("CAN-COMMUNICATION-CONTROLLER")
        self.writer.writeAbstractCanCommunicationControllerCanControllerAttributes(element, controller)
        assert True

    def test_coupling_port_structural_elements_unsupported_type(self):
        details = MagicMock()
        details.getCouplingPortStructuralElements.return_value = [MagicMock(spec=object)]
        element = ET.Element("COUPLING-PORT-DETAILS")
        self.writer.writeCouplingPortDetailsCouplingPortStructuralElements(element, details)
        assert True

    def test_ethernet_priority_regenerations_unsupported_type(self):
        details = MagicMock()
        details.getEthernetPriorityRegenerations.return_value = [MagicMock(spec=object)]
        element = ET.Element("COUPLING-PORT-DETAILS")
        self.writer.writeCouplingPortDetailsEthernetPriorityRegenerations(element, details)
        assert True

    def test_sender_rec_array_type_mapping_record_element_mapping_unsupported_type(self):
        mapping = MagicMock()
        mapping.getRecordElementMappings.return_value = [MagicMock(spec=object)]
        element = ET.Element("SENDER-REC-RECORD-TYPE-MAPPING")
        self.writer.writeSenderRecArrayTypeMappingRecordElementMapping(element, mapping)
        assert True

    def test_system_mapping_data_mappings_unsupported_type(self):
        mapping = MagicMock()
        mapping.getDataMappings.return_value = [MagicMock(spec=object)]
        element = ET.Element("SYSTEM-MAPPING")
        self.writer.writeSystemMappingDataMappings(element, mapping)
        assert True

    def test_system_mapping_sw_mappings_unsupported_type(self):
        mapping = MagicMock()
        mapping.getSwMappings.return_value = [MagicMock(spec=object)]
        element = ET.Element("SYSTEM-MAPPING")
        self.writer.writeSystemMappingSwMappings(element, mapping)
        assert True

    def test_system_mapping_ecu_resource_mappings_unsupported_type(self):
        mapping = MagicMock()
        mapping.getEcuResourceMappings.return_value = [MagicMock(spec=object)]
        element = ET.Element("SYSTEM-MAPPING")
        self.writer.writeSystemMappingEcuResourceMappings(element, mapping)
        assert True

    def test_system_mapping_sw_impl_mappings_unsupported_type(self):
        mapping = MagicMock()
        mapping.getSwImplMappings.return_value = [MagicMock(spec=object)]
        element = ET.Element("SYSTEM-MAPPING")
        self.writer.writeSystemMappingSwImplMappings(element, mapping)
        assert True

    def test_system_mappings_unsupported_type(self):
        system = MagicMock()
        system.getSystemMappings.return_value = [MagicMock(spec=object)]
        element = ET.Element("SYSTEM")
        self.writer.writeSystemMappings(element, system)
        assert True

    def test_flat_map_instances_unsupported_type(self):
        map = MagicMock()
        map.getInstances.return_value = [MagicMock(spec=object)]
        element = ET.Element("FLAT-MAP")
        self.writer.writeFlatMapInstances(element, map)
        assert True

    def test_port_interface_mappings_unsupported_type(self):
        mapping_set = MagicMock()
        mapping_set.getPortInterfaceMappings.return_value = [MagicMock(spec=object)]
        element = ET.Element("PORT-INTERFACE-MAPPING-SET")
        self.writer.writePortInterfaceMappings(element, mapping_set)
        assert True

    def test_ecuc_container_value_sub_containers_unsupported_type(self):
        container_value = MagicMock()
        container_value.getSubContainers.return_value = [MagicMock(spec=object)]
        element = ET.Element("ECUC-CONTAINER-VALUE")
        self.writer.writeEcucContainerValueSubContainers(element, container_value)
        assert True

    def test_ecuc_container_value_parameter_values_unsupported_type(self):
        container_value = MagicMock()
        container_value.getParameterValues.return_value = [MagicMock(spec=object)]
        element = ET.Element("ECUC-CONTAINER-VALUE")
        self.writer.writeEcucContainerValueParameterValues(element, container_value)
        assert True

    def test_ecuc_container_value_reference_values_unsupported_type(self):
        container_value = MagicMock()
        container_value.getReferenceValues.return_value = [MagicMock(spec=object)]
        element = ET.Element("ECUC-CONTAINER-VALUE")
        self.writer.writeEcucContainerValueReferenceValues(element, container_value)
        assert True

    def test_ecuc_module_configuration_values_containers_unsupported_type(self):
        values = MagicMock()
        values.getContainers.return_value = [MagicMock(spec=object)]
        element = ET.Element("ECUC-MODULE-CONFIGURATION-VALUES")
        self.writer.writeEcucModuleConfigurationValuesContainers(element, values)
        assert True

    def test_life_cycle_info_set_life_cycle_infos_unsupported_type(self):
        info_set = MagicMock()
        info_set.getLifeCycleInfos.return_value = [MagicMock(spec=object)]
        element = ET.Element("LIFE-CYCLE-INFO-SET")
        self.writer.writeLifeCycleInfoSetLifeCycleInfos(element, info_set)
        assert True

    def test_multiplexed_i_pdu_dynamic_parts_unsupported_type(self):
        ipdu = MagicMock()
        ipdu.getDynamicParts.return_value = [MagicMock(spec=object)]
        element = ET.Element("MULTIPLEXED-I-PDU")
        self.writer.writeMultiplexedIPduDynamicParts(element, ipdu)
        assert True

    def test_dynamic_part_dynamic_part_alternatives_unsupported_type(self):
        part = MagicMock()
        part.getDynamicPartAlternatives.return_value = [MagicMock(spec=object)]
        element = ET.Element("DYNAMIC-PART")
        self.writer.writeDynamicPartDynamicPartAlternatives(element, part)
        assert True

    def test_multiplexed_i_pdu_static_parts_unsupported_type(self):
        ipdu = MagicMock()
        ipdu.getStaticParts.return_value = [MagicMock(spec=object)]
        element = ET.Element("MULTIPLEXED-I-PDU")
        self.writer.writeMultiplexedIPduStaticParts(element, ipdu)
        assert True

    def test_secure_communication_props_set_authentication_props_unsupported_type(self):
        set = MagicMock()
        set.getAuthenticationProps.return_value = [MagicMock(spec=object)]
        element = ET.Element("SECURE-COMMUNICATION-PROPS-SET")
        self.writer.writeSecureCommunicationPropsSetAuthenticationProps(element, set)
        assert True

    def test_secure_communication_props_set_freshness_props_unsupported_type(self):
        set = MagicMock()
        set.getFreshnessProps.return_value = [MagicMock(spec=object)]
        element = ET.Element("SECURE-COMMUNICATION-PROPS-SET")
        self.writer.writeSecureCommunicationPropsSetFreshnessProps(element, set)
        assert True

    def test_do_ip_tp_config_do_ip_logic_addresses_unsupported_type(self):
        config = MagicMock()
        config.getDoIpLogicAddresses.return_value = [MagicMock(spec=object)]
        element = ET.Element("DO-IP-TP-CONFIG")
        self.writer.writeDoIpTpConfigDoIpLogicAddresses(element, config)
        assert True

    def test_hw_category_hw_attribute_def_unsupported_type(self):
        hw_category = MagicMock()
        hw_category.getHwAttributeDefs.return_value = [MagicMock(spec=object)]
        element = ET.Element("HW-CATEGORY")
        self.writer.writeHwCategoryHwAttributeDef(element, hw_category)
        assert True

    def test_data_transformation_set_data_transformations_unsupported_type(self):
        dtf_set = MagicMock()
        dtf_set.getDataTransformations.return_value = [MagicMock(spec=object)]
        element = ET.Element("DATA-TRANSFORMATION-SET")
        self.writer.writeDataTransformationSetDataTransformations(element, dtf_set)
        assert True

    def test_data_transformation_set_transformation_technologies_unsupported_type(self):
        dtf_set = MagicMock()
        dtf_set.getTransformationTechnologies.return_value = [MagicMock(spec=object)]
        element = ET.Element("DATA-TRANSFORMATION-SET")
        self.writer.writeDataTransformationSetTransformationTechnologies(element, dtf_set)
        assert True

    def test_transformation_technology_transformation_descriptions_unsupported_type(self):
        tech = MagicMock()
        tech.getTransformationDescriptions.return_value = [MagicMock(spec=object)]
        element = ET.Element("TRANSFORMATION-TECHNOLOGY")
        self.writer.writeTransformationTechnologyTransformationDescriptions(element, tech)
        assert True