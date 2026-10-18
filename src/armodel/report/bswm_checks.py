from typing import Any, Callable, Dict, List, Optional

from armodel.data_models.ecuc import BswmActionList, BswmModule

MAX_NESTING_LEVELS = 7
GROUP_SWITCH_CONSTRAINTS = {
    "BswMDeadlineMonitoringControl": ("SWS_BswM_CONSTR_00003", "BswMEnabledDMPduGroupRef", "BswMDisabledDMPduGroupRef"),
    "BswMPduGroupSwitch": ("SWS_BswM_CONSTR_00004", "BswMEnabledPduGroupRef", "BswMDisabledPduGroupRef"),
    "BswMSdServiceGroupSwitch": ("SWS_BswM_CONSTR_00005", "BswMEnabledSdServiceGroupRef", "BswMDisabledSdServiceGroupRef"),
}


def short_name(path: Optional[str]) -> Optional[str]:
    if path is None:
        return None
    return path.rstrip("/").rsplit("/", 1)[-1]


class BswmCyclicNesting(Exception):
    def __init__(self, path: List[str]) -> None:
        super().__init__(" -> ".join(path))
        self.path = path


class BswmConfigChecker:
    """Checks a BswmModule against the configuration constraints of SWS BSW Mode Manager chapters 7 and 10."""

    def check(self, model: BswmModule) -> List[Dict[str, Any]]:
        rows: List[Dict[str, Any]] = []

        def report(rule: str, element: str, message: str) -> None:
            rows.append({"Rule": rule, "Element": element, "Message": message})

        for expression in model.getLogicalExpressions():
            count = len(expression.getArgumentRefs())
            if expression.getOperator() == "BSWM_NAND" and count != 2:
                report("SWS_BswM_00242", expression.getName(), "BSWM_NAND needs exactly 2 arguments, found %d" % count)
            if expression.getOperator() == "BSWM_NOT" and count != 1:
                report("SWS_BswM_00243", expression.getName(), "BSWM_NOT needs exactly 1 argument, found %d" % count)

        for condition in model.getModeConditions():
            condition_type = condition.getConditionType()
            mode_type = condition.getConditionModeType()
            if condition_type in ("BSWM_EQUALS", "BSWM_EQUALS_NOT") and mode_type == "BswMEventRequestPort":
                report("SWS_BswM_00256", condition.getName(), "%s cannot be used with the BswMEventRequestPort %s" % (condition_type, short_name(condition.getConditionMode())))
            if condition_type in ("BSWM_EVENT_IS_SET", "BSWM_EVENT_IS_CLEARED") and mode_type == "BswMModeRequestPort":
                report("SWS_BswM_00256", condition.getName(), "%s cannot be used with the BswMModeRequestPort %s" % (condition_type, short_name(condition.getConditionMode())))

        for port in model.getModeRequestPorts():
            if port.getBswModeInitValue() is not None and port.getInitCompuConstText() is not None:
                report("SWS_BswM_00203", port.getName(), "BswMModeInitValue sets both BswMBswModeInitValue and BswMCompuScaleModeValue")

        for action_list in model.getActionLists():
            seen: Dict[int, str] = {}
            for item in action_list.getItems():
                index = item.getIndex()
                if index is not None:
                    if index in seen:
                        report("SWS_BswM_CONSTR_00001", action_list.getName(), "items %s and %s share BswMActionListItemIndex %d" % (seen[index], item.getName(), index))
                    else:
                        seen[index] = item.getName()
            for item in action_list.getItems():
                error_id = item.getReportFailRuntimeErrorId()
                if error_id is not None and not 128 <= error_id <= 255:
                    report("SWS_BswM_00240", item.getName(), "BswMReportFailRuntimeErrorId %d is outside 128..255" % error_id)

        for action in model.getActions():
            constraint = GROUP_SWITCH_CONSTRAINTS.get(action.getActionType() or "")
            if constraint is None:
                continue
            rule, enabled_name, disabled_name = constraint
            for group in sorted(set(action.getParameter(enabled_name)) & set(action.getParameter(disabled_name))):
                report(rule, action.getName(), "%s is both enabled and disabled" % short_name(group))

        self.check_nesting(model, report)
        return rows

    def check_nesting(self, model: BswmModule, report: Callable[[str, str, str], None]) -> None:
        lists = {action_list.getName(): action_list for action_list in model.getActionLists()}
        rules = {rule.getName(): rule for rule in model.getRules()}
        depths: Dict[str, int] = {}

        def children(action_list: BswmActionList) -> List[str]:
            result: List[str] = []
            for item in action_list.getItems():
                target = short_name(item.getActionRef())
                if target is None:
                    continue
                if item.getActionRefType() == "BswMActionList" and target in lists:
                    result.append(target)
                elif item.getActionRefType() == "BswMRule" and target in rules:
                    rule = rules[target]
                    for path in (rule.getTrueActionList(), rule.getFalseActionList()):
                        name = short_name(path)
                        if name is not None and name in lists:
                            result.append(name)
            return result

        def depth(name: str, stack: List[str]) -> int:
            if name in stack:
                raise BswmCyclicNesting(stack + [name])
            if name not in depths:
                depths[name] = 1 + max([depth(child, stack + [name]) for child in children(lists[name])] or [0])
            return depths[name]

        for name in lists:
            try:
                levels = depth(name, [])
            except BswmCyclicNesting as cycle:
                report("SWS_BswM_00037", name, "cyclic action list nesting: %s" % " -> ".join(cycle.path))
                continue
            if levels > MAX_NESTING_LEVELS:
                report("SWS_BswM_00037", name, "action list nesting has %d levels, at most %d are allowed" % (levels, MAX_NESTING_LEVELS))
