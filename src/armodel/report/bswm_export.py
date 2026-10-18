from typing import Any, Dict, List, Optional

from armodel.data_models.ecuc import BswmAction, BswmActionList, BswmActionListItem, BswmModule
from armodel.report.ecuc_export import EcucConfigExporter, EcucConfigModelMapper, EcucConfigXlsxExporter, EcucConfigYamlExporter, Sections

ACTION_HEADERS = ["name", "BswMActionType"]
ACTION_LIST_HEADERS = [
    "name",
    "BswMActionListExecution",
    "BswMActionListPriority",
    "BswMActionListItem",
    "BswMActionListItemIndex",
    "BswMAbortOnFail",
    "BswMReportFailRuntimeErrorId",
    "BswMActionListItemRef",
    "BswMActionListItemRefType",
]


def short_name(path: Optional[str]) -> Optional[str]:
    if path is None:
        return None
    return path.rstrip("/").rsplit("/", 1)[-1]


class BswmConfigModelMapper(EcucConfigModelMapper[BswmModule]):
    def action_to_dict(self, action: BswmAction) -> Dict[str, Any]:
        row: Dict[str, Any] = {"name": action.getName(), "BswMActionType": action.getActionType()}
        for name, values in action.getParameters().items():
            row[name] = values[0] if len(values) == 1 else list(values)
        return row

    def item_to_dict(self, action_list: BswmActionList, item: Optional[BswmActionListItem]) -> Dict[str, Any]:
        row: Dict[str, Any] = {"name": action_list.getName(), "BswMActionListExecution": action_list.getExecution(), "BswMActionListPriority": action_list.getPriority()}
        row["BswMActionListItem"] = item.getName() if item is not None else None
        row["BswMActionListItemIndex"] = item.getIndex() if item is not None else None
        row["BswMAbortOnFail"] = item.getAbortOnFail() if item is not None else None
        row["BswMReportFailRuntimeErrorId"] = item.getReportFailRuntimeErrorId() if item is not None else None
        row["BswMActionListItemRef"] = short_name(item.getActionRef()) if item is not None else None
        row["BswMActionListItemRefType"] = item.getActionRefType() if item is not None else None
        return row

    def action_list_to_rows(self, action_list: BswmActionList) -> List[Dict[str, Any]]:
        items = sorted(action_list.getItems(), key=lambda item: (item.getIndex() is None, item.getIndex() or 0))
        if not items:
            return [self.item_to_dict(action_list, None)]
        return [self.item_to_dict(action_list, item) for item in items]

    def to_dict(self, model: BswmModule) -> Sections:
        action_list_rows: List[Dict[str, Any]] = []
        for action_list in model.getActionLists():
            action_list_rows.extend(self.action_list_to_rows(action_list))
        return {
            "BswMAction": [self.action_to_dict(action) for action in model.getActions()],
            "BswMActionList": action_list_rows,
        }

    def headers(self, section: str) -> List[str]:
        return {"BswMAction": ACTION_HEADERS, "BswMActionList": ACTION_LIST_HEADERS}.get(section, [])


class BswmConfigYamlExporter(EcucConfigYamlExporter[BswmModule]):
    def __init__(self, mapper: Optional[BswmConfigModelMapper] = None):
        super().__init__(mapper or BswmConfigModelMapper())


class BswmConfigXlsxExporter(EcucConfigXlsxExporter[BswmModule]):
    def __init__(self, mapper: Optional[BswmConfigModelMapper] = None):
        super().__init__(mapper or BswmConfigModelMapper())


class BswmConfigExporter(EcucConfigExporter[BswmModule]):
    def __init__(self, mapper: Optional[BswmConfigModelMapper] = None):
        super().__init__(mapper or BswmConfigModelMapper(), "BswM")
