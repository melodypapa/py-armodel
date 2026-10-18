from typing import Any, Dict, List, Optional, Tuple

from armodel.data_models.ecuc import (
    BswmAction,
    BswmActionList,
    BswmActionListItem,
    BswmDataTypeMappingSets,
    BswmElement,
    BswmEventRequestPort,
    BswmGeneral,
    BswmLogicalExpression,
    BswmModeCondition,
    BswmModeRequestPort,
    BswmModule,
    BswmRteModeRequestPort,
    BswmRule,
    BswmSwitchPort,
)
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import Container
from armodel.parser.ecuc_parser import EcucParser

# BswMAvailableActions choice containers and their parameters/references as defined in
# AUTOSAR_CP_SWS_BSWModeManager chapter 10.2; anything else in the ECUC values is vendor-specific and ignored.
BSWM_AVAILABLE_ACTIONS: Dict[str, List[str]] = {
    "BswMClearEventRequest": ["BswMClearEventRequestPortRef"],
    "BswMComMAllowCom": ["BswMComAllowed", "BswMComMAllowChannelRef"],
    "BswMComMModeLimitation": ["BswMComMLimitMode", "BswMComMLimitChannelRef"],
    "BswMComMModeSwitch": ["BswMComMRequestedMode", "BswMComMUserRef"],
    "BswMCoreHaltMode": ["BswMCoreHaltActivationState", "BswMTargetCoreRef"],
    "BswMDeadlineMonitoringControl": ["BswMDisabledDMPduGroupRef", "BswMEnabledDMPduGroupRef"],
    "BswMEcuMDriverInitListBswM": ["BswMEcuMDriverInitListBswMRef"],
    "BswMEcuMGoDownHaltPoll": ["BswMEcuMUserIdRef"],
    "BswMEcuMSelectShutdownTarget": ["BswMEcuMShutdownTarget", "BswMEcuMResetModeRef", "BswMEcuMSleepModeRef"],
    "BswMEcuMStateSwitch": ["BswMEcuMState"],
    "BswMEthIfStartAllPorts": [],
    "BswMEthIfSwitchPortGroupRequestMode": ["BswMEthTrcvMode", "BswMEthIfSwitchPortGroupRef"],
    "BswMFrSMAllSlots": ["BswMFrSMAllSlotsNetworkHandleRef"],
    "BswMJ1939DcmStateSwitch": ["BswMJ1939DcmRequestedState", "BswMJ1939DcmChannelRef", "BswMJ1939DcmNodeRef"],
    "BswMJ1939RmStateSwitch": ["BswMJ1939RmRequestedState", "BswMJ1939RmChannelRef", "BswMJ1939RmNodeRef"],
    "BswMLinScheduleSwitch": ["BswMLinScheduleRef"],
    "BswMNMControl": ["BswMNMAction", "BswMComMNetworkHandleRef"],
    "BswMPduGroupSwitch": ["BswMPduGroupSwitchReinit", "BswMDisabledPduGroupRef", "BswMEnabledPduGroupRef"],
    "BswMPduRouterControl": ["BswMPduRouterAction", "BswMPduRouterDisableInitBuffer", "BswMPduRoutingPathGroupRef"],
    "BswMRteModeRequest": ["BswMRequestedModeRef", "BswMRteModeRequestPortRef"],
    "BswMRteStart": [],
    "BswMRteStop": [],
    "BswMRteSwitch": ["BswMRteSwitchPortRef", "BswMSwitchedMode"],
    "BswMSchMSwitch": ["BswMSchMSwitchedMode", "BswMSchMSwitchPortRef"],
    "BswMSdClientServiceModeRequest": ["BswMSdClientServiceState", "BswMSdClientMethodsRef"],
    "BswMSdConsumedEventGroupModeRequest": ["BswMSdConsumedEventGroupState", "BswMSdConsumedEventGroupRef"],
    "BswMSdServerServiceModeRequest": ["BswMSdServerServiceState", "BswMSdServerMethodsRef"],
    "BswMSdServiceGroupSwitch": ["BswMDisabledSdServiceGroupRef", "BswMEnabledSdServiceGroupRef"],
    "BswMSetFirewallState": ["BswMFirewallStateRef"],
    "BswMSwitchIPduMode": ["BswMSwitchIPduModeValue", "BswMSwitchIPduModeRef"],
    "BswMTimerControl": ["BswMTimerAction", "BswMTimerValue", "BswMTimerRef"],
    "BswMTriggerIPduSend": ["BswMTriggeredIPduRef"],
    "BswMUserCallout": ["BswMUserCalloutFunction"],
}


BSWM_MODE_REQUEST_SOURCES: Dict[str, List[str]] = {
    "BswMBswModeNotification": ["BswMBswModeDeclarationGroupPrototypeRef"],
    "BswMCanSMIndication": ["BswMCanSMChannelRef"],
    "BswMComMIndication": ["BswMComMChannelRef"],
    "BswMComMPncRequest": ["BswMComMPncRef"],
    "BswMDcmComModeRequest": ["BswMDcmComMChannelRef"],
    "BswMEcuMIndication": [],
    "BswMEcuMRUNRequestIndication": ["BswMEcuMRUNRequestProtocolPort"],
    "BswMEcuMWakeupSource": ["BswMEcuMWakeupSrcRef"],
    "BswMEthIfPortGroupLinkStateChg": ["BswMEthIfSwitchPortGroupRef"],
    "BswMEthSMIndication": ["BswMEthSMChannelRef"],
    "BswMFrSMIndication": ["BswMFrSMChannelRef"],
    "BswMGenericRequest": ["BswMModeRequesterId"],
    "BswMJ1939DcmBroadcastStatus": ["BswMJ1939DcmChannelRef"],
    "BswMJ1939NmIndication": ["BswMJ1939NmChannelRef", "BswMJ1939NmNodeRef"],
    "BswMLinSMIndication": ["BswMLinSMChannelRef"],
    "BswMLinScheduleIndication": ["BswMLinScheduleRef", "BswMLinSMChannelRef"],
    "BswMLinTpModeRequest": ["BswMLinTpChannelRef"],
    "BswMNmStateChangeNotification": ["BswMNmChannelRef"],
    "BswMNvMJobModeIndication": ["BswMNvmService"],
    "BswMNvMRequest": ["BswMNvMBlockRef"],
    "BswMSdClientServiceCurrentState": ["BswMSdClientMethodsRef"],
    "BswMSdConsumedEventGroupCurrentState": ["BswMSdConsumedEventGroupRef"],
    "BswMSdEventHandlerCurrentState": ["BswMSdEventHandlerRef"],
    "BswMSoAdSoConModeChg": ["BswMSoAdSocketIdRef"],
    "BswMSwcModeNotification": ["BswMSwcModeNotificationModeDeclarationGroupPrototypeRef"],
    "BswMSwcModeRequest": ["BswMSwcModeRequestVariableDataPrototypeRef"],
    "BswMTimer": [],
}

BSWM_EVENT_REQUEST_SOURCES: Dict[str, List[str]] = {
    "BswMComMInitiateReset": [],
    "BswMDcmApplicationUpdatedIndication": [],
    "BswMModeSwitchErrorEvent": ["BswMRteSwitchPortRef"],
    "BswMNmCarWakeUpIndication": ["BswMNmChannelRef"],
    "BswMPartitionRestarted": [],
    "BswMSwitchAckNotification": ["BswMSwitchPortRef"],
}

BSWM_CONDITION_VALUES: Dict[str, List[str]] = {
    "BswMBswMode": ["BswMBswRequestedMode"],
    "BswMCompuScaleModeValue": ["BswMCompuConstText", "BswMCompuMethodRef"],
    "BswMModeDeclaration": ["BswMModeValueRef"],
}

BSWM_GENERAL_PARAMETERS: List[str] = [
    "BswMCanSMEnabled",
    "BswMComMEnabled",
    "BswMDcmEnabled",
    "BswMDevErrorDetect",
    "BswMEcuMEnabled",
    "BswMEthIfEnabled",
    "BswMEthSMEnabled",
    "BswMFrSMEnabled",
    "BswMGenericRequestEnabled",
    "BswMJ1939DcmEnabled",
    "BswMJ1939NmEnabled",
    "BswMLinSMEnabled",
    "BswMLinTPEnabled",
    "BswMMainFunctionPeriod",
    "BswMNmEnabled",
    "BswMNvMEnabled",
    "BswMSdControlEnabled",
    "BswMSdEnabled",
    "BswMVersionInfoApi",
]


BSWM_RTE_MODE_REQUEST_PORT_REFERENCES: List[str] = ["BswMRteModeRequestPortInterfaceRef", "BswMRteModeRequestVariableDataPrototypeSRRef"]


class BswmEcucConversionError(Exception):
    pass


class BswmEcucParser(EcucParser):
    conversion_error = BswmEcucConversionError

    def __init__(self):
        super().__init__()
        self.config_paths: Dict[str, str] = {}

    def load(self, path: str, document: Optional[AUTOSAR] = None, warning: bool = False) -> BswmModule:
        return super().load(path, document=document, warning=warning)

    def parseEcuc(self, document: AUTOSAR, warning: bool = False) -> BswmModule:
        index = self.get_all_containers(document, module_name="BswM")
        module = BswmModule()
        module.setName(self.get_module_short_name(document, "BswM") or "BswM")
        self.config_paths = {self.get_path(config): config.getShortName() for config in self.get_containers_by_definition(index, "BswMConfig")}

        for container in self.get_containers_by_definition(index, "BswMAction"):
            module.addAction(self.get_collect_action(container))
        for container in self.get_containers_by_definition(index, "BswMActionList"):
            module.addActionList(self.get_collect_action_list(container, index, warning))
        for container in self.get_containers_by_definition(index, "BswMRule"):
            module.addRule(self.get_collect_rule(container, index, warning))
        for container in self.get_containers_by_definition(index, "BswMLogicalExpression"):
            module.addLogicalExpression(self.get_collect_logical_expression(container, index, warning))
        for container in self.get_containers_by_definition(index, "BswMModeCondition"):
            module.addModeCondition(self.get_collect_mode_condition(container, index, warning))
        for container in self.get_containers_by_definition(index, "BswMModeRequestPort"):
            module.addModeRequestPort(self.get_collect_mode_request_port(container))
        for container in self.get_containers_by_definition(index, "BswMEventRequestPort"):
            module.addEventRequestPort(self.get_collect_event_request_port(container))
        for container in self.get_containers_by_definition(index, "BswMSwitchPort"):
            module.addSwitchPort(self.get_collect_switch_port(container))
        for container in self.get_containers_by_definition(index, "BswMGeneral"):
            module.setGeneral(self.get_collect_general(container))
        for container in self.get_containers_by_definition(index, "BswMRteModeRequestPort"):
            module.addRteModeRequestPort(self.get_collect_rte_mode_request_port(container))
        for container in self.get_containers_by_definition(index, "BswMDataTypeMappingSets"):
            module.addDataTypeMappingSets(self.get_collect_data_type_mapping_sets(container))
        return module

    def get_collect_choice(self, container: Container, choice_name: str, table: Dict[str, List[str]]) -> Tuple[Optional[str], Dict[str, List[Any]]]:
        """Read the choice container ``choice_name`` below ``container``: the selected SWS choice and its SWS-defined values."""
        choice_type: Optional[str] = None
        values: Dict[str, List[Any]] = {}
        for choice_container in self.get_sub_containers_by_name(container).get(choice_name, []):
            for choice in choice_container.getSubContainers():
                name = self.get_definition_name(choice.getDefinitionRef())
                if name not in table:
                    self.logger.debug("Ignore non-standard %s choice %s" % (choice_name, name))
                    continue
                choice_type = name
                allowed = table[name]
                for parameter in self.get_parameter_values(choice):
                    parameter_name = self.get_definition_name(parameter.getDefinitionRef())
                    if parameter_name in allowed:
                        values.setdefault(parameter_name, []).append(self.get_typed_value(parameter))
                    else:
                        self.logger.debug("Ignore non-standard %s parameter %s" % (name, parameter_name))
                for reference_name, path in self.iter_references(choice):
                    if reference_name in allowed:
                        values.setdefault(reference_name, []).append(path)
                    else:
                        self.logger.debug("Ignore non-standard %s reference %s" % (name, reference_name))
        return choice_type, values

    def get_collect_action(self, container: Container) -> BswmAction:
        action = BswmAction()
        action.setName(container.getShortName())
        self.locate(action, container)
        self.logger.debug("Parsing BswMAction: %s", action.getName())
        action_type, values = self.get_collect_choice(container, "BswMAvailableActions", BSWM_AVAILABLE_ACTIONS)
        action.setActionType(action_type)
        for name, items in values.items():
            for value in items:
                action.addParameter(name, value)
        return action

    def get_collect_action_list(self, container: Container, index: Dict[str, Container], warning: bool) -> BswmActionList:
        action_list = BswmActionList()
        action_list.setName(container.getShortName())
        self.locate(action_list, container)
        self.logger.debug("Parsing BswMActionList: %s", action_list.getName())
        for name, raw in self.iter_parameters(container):
            if name == "BswMActionListExecution":
                action_list.setExecution(self.get_str(name, raw))
            elif name == "BswMActionListPriority":
                action_list.setPriority(self.get_int(name, raw))
            else:
                self.logger.debug("Ignore non-standard BswMActionList parameter %s" % name)

        for item_container in self.get_sub_containers_by_name(container).get("BswMActionListItem", []):
            item = BswmActionListItem()
            item.setName(item_container.getShortName())
            for name, raw in self.iter_parameters(item_container):
                if name == "BswMActionListItemIndex":
                    item.setIndex(self.get_int(name, raw))
                elif name == "BswMAbortOnFail":
                    item.setAbortOnFail(self.get_bool(name, raw))
                elif name == "BswMReportFailRuntimeErrorId":
                    item.setReportFailRuntimeErrorId(self.get_int(name, raw))
                else:
                    self.logger.debug("Ignore non-standard BswMActionListItem parameter %s" % name)
            for name, path in self.iter_references(item_container):
                if name == "BswMActionListItemRef":
                    item.setActionRef(path)
                    item.setActionRefType(self.get_lookup_type(name, path, index, warning))
                else:
                    self.logger.debug("Ignore non-standard BswMActionListItem reference %s" % name)
            action_list.addItem(item)
        return action_list

    def get_collect_rule(self, container: Container, index: Dict[str, Container], warning: bool) -> BswmRule:
        rule = BswmRule()
        rule.setName(container.getShortName())
        self.locate(rule, container)
        for name, raw in self.iter_parameters(container):
            if name == "BswMNestedExecutionOnly":
                rule.setNestedExecutionOnly(self.get_bool(name, raw))
            elif name == "BswMRuleInitState":
                rule.setInitState(self.get_str(name, raw))
            else:
                self.logger.debug("Ignore non-standard BswMRule parameter %s" % name)
        for name, path in self.iter_references(container):
            if name == "BswMRuleExpressionRef":
                rule.setExpressionRef(path)
            elif name == "BswMRuleTrueActionList":
                rule.setTrueActionList(path)
            elif name == "BswMRuleFalseActionList":
                rule.setFalseActionList(path)
            else:
                self.logger.debug("Ignore non-standard BswMRule reference %s" % name)
                continue
            self.get_lookup_type(name, path, index, warning)
        return rule

    def get_collect_logical_expression(self, container: Container, index: Dict[str, Container], warning: bool) -> BswmLogicalExpression:
        expression = BswmLogicalExpression()
        expression.setName(container.getShortName())
        self.locate(expression, container)
        for name, raw in self.iter_parameters(container):
            if name == "BswMLogicalOperator":
                expression.setOperator(self.get_str(name, raw))
            else:
                self.logger.debug("Ignore non-standard BswMLogicalExpression parameter %s" % name)
        for name, path in self.iter_references(container):
            if name == "BswMArgumentRef":
                expression.addArgumentRef(path, self.get_lookup_type(name, path, index, warning))
            else:
                self.logger.debug("Ignore non-standard BswMLogicalExpression reference %s" % name)
        return expression

    def get_collect_mode_condition(self, container: Container, index: Dict[str, Container], warning: bool) -> BswmModeCondition:
        condition = BswmModeCondition()
        condition.setName(container.getShortName())
        self.locate(condition, container)
        for name, raw in self.iter_parameters(container):
            if name == "BswMConditionType":
                condition.setConditionType(self.get_str(name, raw))
            else:
                self.logger.debug("Ignore non-standard BswMModeCondition parameter %s" % name)
        for name, path in self.iter_references(container):
            if name == "BswMConditionMode":
                condition.setConditionMode(path)
                condition.setConditionModeType(self.get_lookup_type(name, path, index, warning))
            else:
                self.logger.debug("Ignore non-standard BswMModeCondition reference %s" % name)
        value_type, values = self.get_collect_choice(container, "BswMConditionValue", BSWM_CONDITION_VALUES)
        condition.setConditionValueType(value_type)
        for name, items in values.items():
            for value in items:
                condition.addConditionValue(name, value)
        return condition

    def get_collect_mode_request_port(self, container: Container) -> BswmModeRequestPort:
        port = BswmModeRequestPort()
        port.setName(container.getShortName())
        self.locate(port, container)
        for name, raw in self.iter_parameters(container):
            if name == "BswMRequestProcessing":
                port.setRequestProcessing(self.get_str(name, raw))
            else:
                self.logger.debug("Ignore non-standard BswMModeRequestPort parameter %s" % name)
        source_type, values = self.get_collect_choice(container, "BswMModeRequestSource", BSWM_MODE_REQUEST_SOURCES)
        port.setSourceType(source_type)
        for name, items in values.items():
            for value in items:
                port.addSourceParameter(name, value)
        for init_value in self.get_sub_containers_by_name(container).get("BswMModeInitValue", []):
            for name, raw in self.iter_parameters(init_value):
                if name == "BswMBswModeInitValue":
                    port.setBswModeInitValue(self.get_str(name, raw))
            for compu in self.get_sub_containers_by_name(init_value).get("BswMCompuScaleModeValue", []):
                for name, raw in self.iter_parameters(compu):
                    if name == "BswMCompuConstText":
                        port.setInitCompuConstText(self.get_str(name, raw))
                for name, path in self.iter_references(compu):
                    if name == "BswMCompuMethodRef":
                        port.setInitCompuMethodRef(path)
        return port

    def get_collect_event_request_port(self, container: Container) -> BswmEventRequestPort:
        port = BswmEventRequestPort()
        port.setName(container.getShortName())
        self.locate(port, container)
        for name, raw in self.iter_parameters(container):
            if name == "BswMEventRequestProcessing":
                port.setRequestProcessing(self.get_str(name, raw))
            else:
                self.logger.debug("Ignore non-standard BswMEventRequestPort parameter %s" % name)
        source_type, values = self.get_collect_choice(container, "BswMEventRequestSource", BSWM_EVENT_REQUEST_SOURCES)
        port.setSourceType(source_type)
        for name, items in values.items():
            for value in items:
                port.addSourceParameter(name, value)
        return port

    def get_collect_switch_port(self, container: Container) -> BswmSwitchPort:
        port = BswmSwitchPort()
        port.setName(container.getShortName())
        self.locate(port, container)
        for name, path in self.iter_references(container):
            if name == "BswMModeSwitchInterfaceRef":
                port.setModeSwitchInterfaceRef(path)
            elif name == "BswMSchMModeDeclarationGroupRef":
                port.setSchMModeDeclarationGroupRef(path)
            else:
                self.logger.debug("Ignore non-standard BswMSwitchPort reference %s" % name)
        return port

    def get_collect_general(self, container: Container) -> BswmGeneral:
        general = BswmGeneral()
        for parameter in self.get_parameter_values(container):
            name = self.get_definition_name(parameter.getDefinitionRef())
            if name in BSWM_GENERAL_PARAMETERS:
                general.setParameter(name, self.get_typed_value(parameter))
            else:
                self.logger.debug("Ignore non-standard BswMGeneral parameter %s" % name)
        for include_files in self.get_sub_containers_by_name(container).get("BswMUserIncludeFiles", []):
            for name, raw in self.iter_parameters(include_files):
                value = self.get_str(name, raw) if name == "BswMUserIncludeFile" else None
                if value:
                    general.addUserIncludeFile(value)
        return general

    def locate(self, element: BswmElement, container: Container) -> None:
        """Record the absolute path of a container and the BswMConfig partition it belongs to."""
        path = self.get_path(container)
        element.setPath(path).setPartition(self.get_partition(path))

    def get_partition(self, path: str) -> Optional[str]:
        for config_path, config_name in self.config_paths.items():
            if path.startswith(config_path + "/"):
                return config_name
        return None

    def get_collect_rte_mode_request_port(self, container: Container) -> BswmRteModeRequestPort:
        port = BswmRteModeRequestPort()
        port.setName(container.getShortName())
        self.locate(port, container)
        for name, path in self.iter_references(container):
            if name == "BswMRteModeRequestPortInterfaceRef":
                port.setInterfaceRef(path)
            elif name == "BswMRteModeRequestVariableDataPrototypeSRRef":
                port.setVariableDataPrototypeRef(path)
            else:
                self.logger.debug("Ignore non-standard BswMRteModeRequestPort reference %s" % name)
        return port

    def get_collect_data_type_mapping_sets(self, container: Container) -> BswmDataTypeMappingSets:
        mapping_sets = BswmDataTypeMappingSets()
        self.locate(mapping_sets, container)
        for name, path in self.iter_references(container):
            if name == "BswMDataTypeMappingSetRef":
                mapping_sets.addRef(path)
            else:
                self.logger.debug("Ignore non-standard BswMDataTypeMappingSets reference %s" % name)
        return mapping_sets

    def get_lookup_type(self, name: str, path: str, index: Dict[str, Container], warning: bool) -> Optional[str]:
        """Return the definition short name of the referenced container, applying strict or warning handling."""
        target = index.get(path)
        if target is not None:
            return self.get_definition_name(target.getDefinitionRef())
        message = "Unresolved standard reference %s -> %s" % (name, path)
        if warning:
            self.logger.warning(message)
            return None
        raise BswmEcucConversionError(message)
