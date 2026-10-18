from typing import Any, Dict, List, Optional, Tuple

from armodel.data_models.ecuc import (
    BswmAction,
    BswmActionList,
    BswmActionListItem,
    BswmElement,
    BswmEventRequestPort,
    BswmLogicalExpression,
    BswmModeCondition,
    BswmModeRequestPort,
    BswmModule,
    BswmRteModeRequestPort,
    BswmRule,
    BswmSwitchPort,
)
from armodel.report.bswm_checks import BswmConfigChecker
from armodel.report.ecuc_export import EcucConfigExporter, EcucConfigModelMapper, EcucConfigXlsxExporter, EcucConfigYamlExporter, Sections

ACTION_HEADERS = ["name", "BswMConfig", "BswMActionType", "UsedByActionLists"]
ACTION_LIST_HEADERS = [
    "name",
    "BswMConfig",
    "BswMActionListExecution",
    "BswMActionListPriority",
    "BswMActionListItem",
    "BswMActionListItemIndex",
    "BswMAbortOnFail",
    "BswMReportFailRuntimeErrorId",
    "BswMActionListItemRef",
    "BswMActionListItemRefType",
    "UsedByRules",
    "UsedByActionLists",
]
RULE_HEADERS = ["name", "BswMConfig", "BswMRuleInitState", "BswMNestedExecutionOnly", "BswMRuleExpressionRef", "BswMRuleTrueActionList", "BswMRuleFalseActionList", "UsedByActionLists"]
EXPRESSION_HEADERS = ["name", "BswMConfig", "BswMLogicalOperator", "BswMArgumentRef", "BswMArgumentRefType", "UsedByRules", "UsedByExpressions"]
CONDITION_HEADERS = ["name", "BswMConfig", "BswMConditionType", "BswMConditionMode", "BswMConditionModeType", "BswMConditionValueType", "BswMConditionValue", "BswMCompuMethodRef", "UsedByExpressions"]
MODE_PORT_HEADERS = [
    "name",
    "BswMConfig",
    "BswMRequestProcessing",
    "BswMModeRequestSourceType",
    "BswMBswModeInitValue",
    "BswMModeInitValue.BswMCompuConstText",
    "BswMModeInitValue.BswMCompuMethodRef",
    "UsedByConditions",
]
EVENT_PORT_HEADERS = ["name", "BswMConfig", "BswMEventRequestProcessing", "BswMEventRequestSourceType", "UsedByConditions", "UsedByActions"]
SWITCH_PORT_HEADERS = ["name", "BswMConfig", "BswMModeSwitchInterfaceRef", "BswMSchMModeDeclarationGroupRef", "UsedByActions"]
RTE_MODE_PORT_HEADERS = ["name", "BswMConfig", "BswMRteModeRequestPortInterfaceRef", "BswMRteModeRequestVariableDataPrototypeSRRef", "UsedByActions"]
DATA_TYPE_MAPPING_HEADERS = ["BswMConfig", "BswMDataTypeMappingSetRef"]
CHECK_HEADERS = ["Rule", "Element", "Message"]
ACTION_REFERENCE_PARAMETERS = ["BswMRteSwitchPortRef", "BswMSchMSwitchPortRef", "BswMRteModeRequestPortRef", "BswMClearEventRequestPortRef"]

Usage = Dict[str, List[Tuple[str, str]]]


def short_name(path: Optional[str]) -> Optional[str]:
    if path is None:
        return None
    return path.rstrip("/").rsplit("/", 1)[-1]


def flatten(values: Dict[str, List[Any]]) -> Dict[str, Any]:
    return {name: items[0] if len(items) == 1 else list(items) for name, items in values.items()}


def location(element: BswmElement) -> Dict[str, Optional[str]]:
    return {"BswMConfig": element.getPartition()}


class BswmConfigModelMapper(EcucConfigModelMapper[BswmModule]):
    def build_usage(self, model: BswmModule) -> Usage:
        """Index who references what, keyed by the absolute path of the referenced element."""
        usage: Usage = {}

        def add(target: Optional[str], user_type: str, user_name: str) -> None:
            if target is None:
                return
            users = usage.setdefault(target, [])
            if (user_type, user_name) not in users:
                users.append((user_type, user_name))

        for rule in model.getRules():
            add(rule.getExpressionRef(), "BswMRule", rule.getName())
            add(rule.getTrueActionList(), "BswMRule", rule.getName())
            add(rule.getFalseActionList(), "BswMRule", rule.getName())
        for expression in model.getLogicalExpressions():
            for path in expression.getArgumentRefs():
                add(path, "BswMLogicalExpression", expression.getName())
        for condition in model.getModeConditions():
            add(condition.getConditionMode(), "BswMModeCondition", condition.getName())
        for action_list in model.getActionLists():
            for item in action_list.getItems():
                add(item.getActionRef(), "BswMActionList", action_list.getName())
        for action in model.getActions():
            for parameter in ACTION_REFERENCE_PARAMETERS:
                for path in action.getParameter(parameter):
                    add(path, "BswMAction", action.getName())
        return usage

    def used_by(self, usage: Usage, path: Optional[str], user_type: str) -> List[str]:
        if path is None:
            return []
        return [name for kind, name in usage.get(path, []) if kind == user_type]

    def action_to_dict(self, action: BswmAction, usage: Usage) -> Dict[str, Any]:
        row: Dict[str, Any] = {"name": action.getName(), **location(action), "BswMActionType": action.getActionType(), "UsedByActionLists": self.used_by(usage, action.getPath(), "BswMActionList")}
        row.update(flatten(action.getParameters()))
        return row

    def item_to_dict(self, action_list: BswmActionList, item: Optional[BswmActionListItem], usage: Usage) -> Dict[str, Any]:
        row: Dict[str, Any] = {"name": action_list.getName(), **location(action_list), "BswMActionListExecution": action_list.getExecution(), "BswMActionListPriority": action_list.getPriority()}
        row["BswMActionListItem"] = item.getName() if item is not None else None
        row["BswMActionListItemIndex"] = item.getIndex() if item is not None else None
        row["BswMAbortOnFail"] = item.getAbortOnFail() if item is not None else None
        row["BswMReportFailRuntimeErrorId"] = item.getReportFailRuntimeErrorId() if item is not None else None
        row["BswMActionListItemRef"] = short_name(item.getActionRef()) if item is not None else None
        row["BswMActionListItemRefType"] = item.getActionRefType() if item is not None else None
        row["UsedByRules"] = self.used_by(usage, action_list.getPath(), "BswMRule")
        row["UsedByActionLists"] = self.used_by(usage, action_list.getPath(), "BswMActionList")
        return row

    def action_list_to_rows(self, action_list: BswmActionList, usage: Usage) -> List[Dict[str, Any]]:
        items = sorted(action_list.getItems(), key=lambda item: (item.getIndex() is None, item.getIndex() or 0))
        if not items:
            return [self.item_to_dict(action_list, None, usage)]
        return [self.item_to_dict(action_list, item, usage) for item in items]

    def rule_to_dict(self, rule: BswmRule, usage: Usage) -> Dict[str, Any]:
        return {
            "name": rule.getName(),
            **location(rule),
            "BswMRuleInitState": rule.getInitState(),
            "BswMNestedExecutionOnly": rule.getNestedExecutionOnly(),
            "BswMRuleExpressionRef": short_name(rule.getExpressionRef()),
            "BswMRuleTrueActionList": short_name(rule.getTrueActionList()),
            "BswMRuleFalseActionList": short_name(rule.getFalseActionList()),
            "UsedByActionLists": self.used_by(usage, rule.getPath(), "BswMActionList"),
        }

    def expression_to_dict(self, expression: BswmLogicalExpression, usage: Usage) -> Dict[str, Any]:
        return {
            "name": expression.getName(),
            **location(expression),
            "BswMLogicalOperator": expression.getOperator(),
            "BswMArgumentRef": [short_name(path) for path in expression.getArgumentRefs()],
            "BswMArgumentRefType": list(expression.getArgumentRefTypes()),
            "UsedByRules": self.used_by(usage, expression.getPath(), "BswMRule"),
            "UsedByExpressions": self.used_by(usage, expression.getPath(), "BswMLogicalExpression"),
        }

    def condition_to_dict(self, condition: BswmModeCondition, usage: Usage) -> Dict[str, Any]:
        value: Optional[Any] = None
        for parameter_name in ("BswMBswRequestedMode", "BswMModeValueRef", "BswMCompuConstText"):
            values = condition.getConditionValue(parameter_name)
            if values:
                value = short_name(values[0]) if parameter_name == "BswMModeValueRef" else values[0]
                break
        compu_method = condition.getConditionValue("BswMCompuMethodRef")
        return {
            "name": condition.getName(),
            **location(condition),
            "BswMConditionType": condition.getConditionType(),
            "BswMConditionMode": short_name(condition.getConditionMode()),
            "BswMConditionModeType": condition.getConditionModeType(),
            "BswMConditionValueType": condition.getConditionValueType(),
            "BswMConditionValue": value,
            "BswMCompuMethodRef": short_name(compu_method[0]) if compu_method else None,
            "UsedByExpressions": self.used_by(usage, condition.getPath(), "BswMLogicalExpression"),
        }

    def mode_port_to_dict(self, port: BswmModeRequestPort, usage: Usage) -> Dict[str, Any]:
        row: Dict[str, Any] = {
            "name": port.getName(),
            **location(port),
            "BswMRequestProcessing": port.getRequestProcessing(),
            "BswMModeRequestSourceType": port.getSourceType(),
            "BswMBswModeInitValue": port.getBswModeInitValue(),
            "BswMModeInitValue.BswMCompuConstText": port.getInitCompuConstText(),
            "BswMModeInitValue.BswMCompuMethodRef": short_name(port.getInitCompuMethodRef()),
            "UsedByConditions": self.used_by(usage, port.getPath(), "BswMModeCondition"),
        }
        row.update(flatten(port.getSourceParameters()))
        return row

    def event_port_to_dict(self, port: BswmEventRequestPort, usage: Usage) -> Dict[str, Any]:
        row: Dict[str, Any] = {
            "name": port.getName(),
            **location(port),
            "BswMEventRequestProcessing": port.getRequestProcessing(),
            "BswMEventRequestSourceType": port.getSourceType(),
            "UsedByConditions": self.used_by(usage, port.getPath(), "BswMModeCondition"),
            "UsedByActions": self.used_by(usage, port.getPath(), "BswMAction"),
        }
        row.update(flatten(port.getSourceParameters()))
        return row

    def switch_port_to_dict(self, port: BswmSwitchPort, usage: Usage) -> Dict[str, Any]:
        return {
            "name": port.getName(),
            **location(port),
            "BswMModeSwitchInterfaceRef": port.getModeSwitchInterfaceRef(),
            "BswMSchMModeDeclarationGroupRef": port.getSchMModeDeclarationGroupRef(),
            "UsedByActions": self.used_by(usage, port.getPath(), "BswMAction"),
        }

    def rte_mode_port_to_dict(self, port: BswmRteModeRequestPort, usage: Usage) -> Dict[str, Any]:
        return {
            "name": port.getName(),
            **location(port),
            "BswMRteModeRequestPortInterfaceRef": short_name(port.getInterfaceRef()),
            "BswMRteModeRequestVariableDataPrototypeSRRef": short_name(port.getVariableDataPrototypeRef()),
            "UsedByActions": self.used_by(usage, port.getPath(), "BswMAction"),
        }

    def data_type_mapping_to_rows(self, model: BswmModule) -> List[Dict[str, Any]]:
        rows: List[Dict[str, Any]] = []
        for mapping_sets in model.getDataTypeMappingSets():
            if not mapping_sets.getRefs():
                rows.append({**location(mapping_sets), "BswMDataTypeMappingSetRef": None})
            for path in mapping_sets.getRefs():
                rows.append({**location(mapping_sets), "BswMDataTypeMappingSetRef": short_name(path)})
        return rows

    def general_to_rows(self, model: BswmModule) -> List[Dict[str, Any]]:
        general = model.getGeneral()
        if general is None:
            return []
        row: Dict[str, Any] = dict(general.getParameters())
        row["BswMUserIncludeFile"] = list(general.getUserIncludeFiles())
        return [row]

    def checks_to_rows(self, model: BswmModule) -> List[Dict[str, Any]]:
        return BswmConfigChecker().check(model)

    def to_dict(self, model: BswmModule) -> Sections:
        usage = self.build_usage(model)
        action_list_rows: List[Dict[str, Any]] = []
        for action_list in model.getActionLists():
            action_list_rows.extend(self.action_list_to_rows(action_list, usage))
        return {
            "BswMAction": [self.action_to_dict(action, usage) for action in model.getActions()],
            "BswMActionList": action_list_rows,
            "BswMRule": [self.rule_to_dict(rule, usage) for rule in model.getRules()],
            "BswMLogicalExpression": [self.expression_to_dict(expression, usage) for expression in model.getLogicalExpressions()],
            "BswMModeCondition": [self.condition_to_dict(condition, usage) for condition in model.getModeConditions()],
            "BswMModeRequestPort": [self.mode_port_to_dict(port, usage) for port in model.getModeRequestPorts()],
            "BswMEventRequestPort": [self.event_port_to_dict(port, usage) for port in model.getEventRequestPorts()],
            "BswMSwitchPort": [self.switch_port_to_dict(port, usage) for port in model.getSwitchPorts()],
            "BswMRteModeRequestPort": [self.rte_mode_port_to_dict(port, usage) for port in model.getRteModeRequestPorts()],
            "BswMDataTypeMappingSets": self.data_type_mapping_to_rows(model),
            "BswMGeneral": self.general_to_rows(model),
            "BswMChecks": self.checks_to_rows(model),
        }

    def headers(self, section: str) -> List[str]:
        return {
            "BswMAction": ACTION_HEADERS,
            "BswMActionList": ACTION_LIST_HEADERS,
            "BswMRule": RULE_HEADERS,
            "BswMLogicalExpression": EXPRESSION_HEADERS,
            "BswMModeCondition": CONDITION_HEADERS,
            "BswMModeRequestPort": MODE_PORT_HEADERS,
            "BswMEventRequestPort": EVENT_PORT_HEADERS,
            "BswMSwitchPort": SWITCH_PORT_HEADERS,
            "BswMRteModeRequestPort": RTE_MODE_PORT_HEADERS,
            "BswMDataTypeMappingSets": DATA_TYPE_MAPPING_HEADERS,
            "BswMChecks": CHECK_HEADERS,
        }.get(section, [])


class BswmConfigYamlExporter(EcucConfigYamlExporter[BswmModule]):
    def __init__(self, mapper: Optional[BswmConfigModelMapper] = None):
        super().__init__(mapper or BswmConfigModelMapper())


class BswmConfigXlsxExporter(EcucConfigXlsxExporter[BswmModule]):
    def __init__(self, mapper: Optional[BswmConfigModelMapper] = None):
        super().__init__(mapper or BswmConfigModelMapper())


class BswmConfigExporter(EcucConfigExporter[BswmModule]):
    def __init__(self, mapper: Optional[BswmConfigModelMapper] = None):
        super().__init__(mapper or BswmConfigModelMapper(), "BswM")
