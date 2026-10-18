from typing import Dict, List, Optional

from armodel.data_models.ecuc import BswmAction, BswmActionList, BswmActionListItem, BswmModule
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


class BswmEcucConversionError(Exception):
    pass


class BswmEcucParser(EcucParser):
    conversion_error = BswmEcucConversionError

    def __init__(self):
        super().__init__()

    def load(self, path: str, document: Optional[AUTOSAR] = None, warning: bool = False) -> BswmModule:
        return super().load(path, document=document, warning=warning)

    def parseEcuc(self, document: AUTOSAR, warning: bool = False) -> BswmModule:
        index = self.get_all_containers(document, module_name="BswM")
        module = BswmModule()
        module.setName(self.get_module_short_name(document, "BswM") or "BswM")

        for container in self.get_containers_by_definition(index, "BswMAction"):
            module.addAction(self.get_collect_action(container))
        for container in self.get_containers_by_definition(index, "BswMActionList"):
            module.addActionList(self.get_collect_action_list(container, index, warning))
        return module

    def get_collect_action(self, container: Container) -> BswmAction:
        action = BswmAction()
        action.setName(container.getShortName())
        self.logger.debug("Parsing BswMAction: %s", action.getName())
        for available_actions in self.get_sub_containers_by_name(container).get("BswMAvailableActions", []):
            for choice in available_actions.getSubContainers():
                choice_name = self.get_definition_name(choice.getDefinitionRef())
                if choice_name not in BSWM_AVAILABLE_ACTIONS:
                    self.logger.debug("Ignore non-standard BswMAvailableActions choice %s" % choice_name)
                    continue
                allowed = BSWM_AVAILABLE_ACTIONS[choice_name]
                action.setActionType(choice_name)
                for parameter in self.get_parameter_values(choice):
                    name = self.get_definition_name(parameter.getDefinitionRef())
                    if name in allowed:
                        action.addParameter(name, self.get_typed_value(parameter))
                    else:
                        self.logger.debug("Ignore non-standard %s parameter %s" % (choice_name, name))
                for name, path in self.iter_references(choice):
                    if name in allowed:
                        action.addParameter(name, path)
                    else:
                        self.logger.debug("Ignore non-standard %s reference %s" % (choice_name, name))
        return action

    def get_collect_action_list(self, container: Container, index: Dict[str, Container], warning: bool) -> BswmActionList:
        action_list = BswmActionList()
        action_list.setName(container.getShortName())
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
