from typing import Any, Dict, List, Optional


class BswmAction:
    """A BswMAction container (ECUC_BswM_00810) with the action selected in its BswMAvailableActions choice."""

    def __init__(self) -> None:
        # Short name identifying the BswMAction.
        self.name: str = ""

        # Definition short name of the selected BswMAvailableActions choice, e.g. BswMUserCallout.
        self.actionType: Optional[str] = None

        # SWS-defined parameter and reference values of the selected choice by definition short name.
        self.parameters: Dict[str, List[Any]] = {}

    def getName(self) -> str:
        return self.name

    def setName(self, value: str) -> "BswmAction":
        self.name = value
        return self

    def getActionType(self) -> Optional[str]:
        return self.actionType

    def setActionType(self, value: Optional[str]) -> "BswmAction":
        self.actionType = value
        return self

    def getParameters(self) -> Dict[str, List[Any]]:
        return self.parameters

    def getParameter(self, name: str) -> List[Any]:
        return self.parameters.get(name, [])

    def addParameter(self, name: str, value: Any) -> "BswmAction":
        self.parameters.setdefault(name, []).append(value)
        return self


class BswmActionListItem:
    """A BswMActionListItem container (ECUC_BswM_00830) of a BswMActionList."""

    def __init__(self) -> None:
        # Short name identifying the BswMActionListItem.
        self.name: str = ""

        # Execution order of the item inside its action list (BswMActionListItemIndex).
        self.index: Optional[int] = None

        # Whether the action list is aborted when this item fails (BswMAbortOnFail).
        self.abortOnFail: Optional[bool] = None

        # Absolute path of the referenced BswMAction, BswMActionList or BswMRule (BswMActionListItemRef).
        self.actionRef: Optional[str] = None

        # Definition short name of the referenced container, or None when the reference is unresolved.
        self.actionRefType: Optional[str] = None

        # Runtime error id reported to the DET when this item fails (BswMReportFailRuntimeErrorId, 128..255).
        self.reportFailRuntimeErrorId: Optional[int] = None

    def getName(self) -> str:
        return self.name

    def setName(self, value: str) -> "BswmActionListItem":
        self.name = value
        return self

    def getIndex(self) -> Optional[int]:
        return self.index

    def setIndex(self, value: Optional[int]) -> "BswmActionListItem":
        self.index = value
        return self

    def getAbortOnFail(self) -> Optional[bool]:
        return self.abortOnFail

    def setAbortOnFail(self, value: Optional[bool]) -> "BswmActionListItem":
        self.abortOnFail = value
        return self

    def getActionRef(self) -> Optional[str]:
        return self.actionRef

    def setActionRef(self, value: Optional[str]) -> "BswmActionListItem":
        self.actionRef = value
        return self

    def getActionRefType(self) -> Optional[str]:
        return self.actionRefType

    def setActionRefType(self, value: Optional[str]) -> "BswmActionListItem":
        self.actionRefType = value
        return self

    def getReportFailRuntimeErrorId(self) -> Optional[int]:
        return self.reportFailRuntimeErrorId

    def setReportFailRuntimeErrorId(self, value: Optional[int]) -> "BswmActionListItem":
        self.reportFailRuntimeErrorId = value
        return self


class BswmActionList:
    """A BswMActionList container (ECUC_BswM_00811)."""

    def __init__(self) -> None:
        # Short name identifying the BswMActionList.
        self.name: str = ""

        # BSWM_CONDITION or BSWM_TRIGGER (BswMActionListExecution).
        self.execution: Optional[str] = None

        # Priority of the action list, 0..255 (BswMActionListPriority).
        self.priority: Optional[int] = None

        # The BswMActionListItems in document order.
        self.items: List[BswmActionListItem] = []

    def getName(self) -> str:
        return self.name

    def setName(self, value: str) -> "BswmActionList":
        self.name = value
        return self

    def getExecution(self) -> Optional[str]:
        return self.execution

    def setExecution(self, value: Optional[str]) -> "BswmActionList":
        self.execution = value
        return self

    def getPriority(self) -> Optional[int]:
        return self.priority

    def setPriority(self, value: Optional[int]) -> "BswmActionList":
        self.priority = value
        return self

    def getItems(self) -> List[BswmActionListItem]:
        return self.items

    def addItem(self, value: BswmActionListItem) -> "BswmActionList":
        self.items.append(value)
        return self


class BswmModule:
    """The BswM ECUC module configuration values."""

    def __init__(self) -> None:
        # Short name of the ECUC module configuration values.
        self.name: str = ""

        self.actions: List[BswmAction] = []
        self.actionLists: List[BswmActionList] = []

    def getName(self) -> str:
        return self.name

    def setName(self, value: str) -> "BswmModule":
        self.name = value
        return self

    def getActions(self) -> List[BswmAction]:
        return self.actions

    def addAction(self, value: BswmAction) -> "BswmModule":
        self.actions.append(value)
        return self

    def getActionLists(self) -> List[BswmActionList]:
        return self.actionLists

    def addActionList(self, value: BswmActionList) -> "BswmModule":
        self.actionLists.append(value)
        return self

    @classmethod
    def from_ecuc(cls, document, warning: bool = False) -> "BswmModule":
        from armodel.parser import BswmEcucParser

        return BswmEcucParser().parseEcuc(document, warning=warning)

    @classmethod
    def from_file(cls, path, warning: bool = False) -> "BswmModule":
        from armodel.parser import BswmEcucParser

        return BswmEcucParser().load(path, warning=warning)
