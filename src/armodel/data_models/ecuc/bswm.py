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


class BswmRule:
    """A BswMRule container (ECUC_BswM_00806): a logical expression plus the action lists run on True/False."""

    def __init__(self) -> None:
        # Short name identifying the BswMRule.
        self.name: str = ""

        # True for a subordinate rule that is only evaluated from action lists (BswMNestedExecutionOnly).
        self.nestedExecutionOnly: Optional[bool] = None

        # Previous evaluation result assumed after initialization: BSWM_FALSE, BSWM_TRUE or BSWM_UNDEFINED (BswMRuleInitState).
        self.initState: Optional[str] = None

        # Absolute path of the evaluated BswMLogicalExpression (BswMRuleExpressionRef).
        self.expressionRef: Optional[str] = None

        # Absolute path of the BswMActionList run when the rule is True (BswMRuleTrueActionList).
        self.trueActionList: Optional[str] = None

        # Absolute path of the BswMActionList run when the rule is False (BswMRuleFalseActionList).
        self.falseActionList: Optional[str] = None

    def getName(self) -> str:
        return self.name

    def setName(self, value: str) -> "BswmRule":
        self.name = value
        return self

    def getNestedExecutionOnly(self) -> Optional[bool]:
        return self.nestedExecutionOnly

    def setNestedExecutionOnly(self, value: Optional[bool]) -> "BswmRule":
        self.nestedExecutionOnly = value
        return self

    def getInitState(self) -> Optional[str]:
        return self.initState

    def setInitState(self, value: Optional[str]) -> "BswmRule":
        self.initState = value
        return self

    def getExpressionRef(self) -> Optional[str]:
        return self.expressionRef

    def setExpressionRef(self, value: Optional[str]) -> "BswmRule":
        self.expressionRef = value
        return self

    def getTrueActionList(self) -> Optional[str]:
        return self.trueActionList

    def setTrueActionList(self, value: Optional[str]) -> "BswmRule":
        self.trueActionList = value
        return self

    def getFalseActionList(self) -> Optional[str]:
        return self.falseActionList

    def setFalseActionList(self, value: Optional[str]) -> "BswmRule":
        self.falseActionList = value
        return self


class BswmLogicalExpression:
    """A BswMLogicalExpression container (ECUC_BswM_00808)."""

    def __init__(self) -> None:
        # Short name identifying the BswMLogicalExpression.
        self.name: str = ""

        # BSWM_AND, BSWM_NAND, BSWM_NOT, BSWM_OR or BSWM_XOR (BswMLogicalOperator).
        self.operator: Optional[str] = None

        # Absolute paths of the arguments (BswMArgumentRef), in document order.
        self.argumentRefs: List[str] = []

        # Definition short name of each argument (BswMModeCondition or BswMLogicalExpression), None when unresolved.
        self.argumentRefTypes: List[Optional[str]] = []

    def getName(self) -> str:
        return self.name

    def setName(self, value: str) -> "BswmLogicalExpression":
        self.name = value
        return self

    def getOperator(self) -> Optional[str]:
        return self.operator

    def setOperator(self, value: Optional[str]) -> "BswmLogicalExpression":
        self.operator = value
        return self

    def getArgumentRefs(self) -> List[str]:
        return self.argumentRefs

    def getArgumentRefTypes(self) -> List[Optional[str]]:
        return self.argumentRefTypes

    def addArgumentRef(self, path: str, ref_type: Optional[str]) -> "BswmLogicalExpression":
        self.argumentRefs.append(path)
        self.argumentRefTypes.append(ref_type)
        return self


class BswmModeCondition:
    """A BswMModeCondition container (ECUC_BswM_00807) with its BswMConditionValue choice."""

    def __init__(self) -> None:
        # Short name identifying the BswMModeCondition.
        self.name: str = ""

        # BSWM_EQUALS, BSWM_EQUALS_NOT, BSWM_EVENT_IS_CLEARED or BSWM_EVENT_IS_SET (BswMConditionType).
        self.conditionType: Optional[str] = None

        # Absolute path of the referenced request port (BswMConditionMode).
        self.conditionMode: Optional[str] = None

        # BswMModeRequestPort or BswMEventRequestPort, None when unresolved.
        self.conditionModeType: Optional[str] = None

        # Selected BswMConditionValue choice: BswMBswMode, BswMModeDeclaration or BswMCompuScaleModeValue.
        self.conditionValueType: Optional[str] = None

        # SWS-defined values of the selected choice by definition short name.
        self.conditionValues: Dict[str, List[Any]] = {}

    def getName(self) -> str:
        return self.name

    def setName(self, value: str) -> "BswmModeCondition":
        self.name = value
        return self

    def getConditionType(self) -> Optional[str]:
        return self.conditionType

    def setConditionType(self, value: Optional[str]) -> "BswmModeCondition":
        self.conditionType = value
        return self

    def getConditionMode(self) -> Optional[str]:
        return self.conditionMode

    def setConditionMode(self, value: Optional[str]) -> "BswmModeCondition":
        self.conditionMode = value
        return self

    def getConditionModeType(self) -> Optional[str]:
        return self.conditionModeType

    def setConditionModeType(self, value: Optional[str]) -> "BswmModeCondition":
        self.conditionModeType = value
        return self

    def getConditionValueType(self) -> Optional[str]:
        return self.conditionValueType

    def setConditionValueType(self, value: Optional[str]) -> "BswmModeCondition":
        self.conditionValueType = value
        return self

    def getConditionValues(self) -> Dict[str, List[Any]]:
        return self.conditionValues

    def getConditionValue(self, name: str) -> List[Any]:
        return self.conditionValues.get(name, [])

    def addConditionValue(self, name: str, value: Any) -> "BswmModeCondition":
        self.conditionValues.setdefault(name, []).append(value)
        return self


class BswmModeRequestPort:
    """A BswMModeRequestPort container (ECUC_BswM_00805) with its BswMModeRequestSource choice and BswMModeInitValue."""

    def __init__(self) -> None:
        # Short name identifying the BswMModeRequestPort.
        self.name: str = ""

        # BSWM_DEFERRED or BSWM_IMMEDIATE (BswMRequestProcessing).
        self.requestProcessing: Optional[str] = None

        # Selected BswMModeRequestSource choice, e.g. BswMComMIndication.
        self.sourceType: Optional[str] = None

        # SWS-defined parameters/references of the selected source by definition short name.
        self.sourceParameters: Dict[str, List[Any]] = {}

        # Initial mode as symbolic name (BswMModeInitValue/BswMBswModeInitValue).
        self.bswModeInitValue: Optional[str] = None

        # Initial mode as CompuConst text (BswMModeInitValue/BswMCompuScaleModeValue/BswMCompuConstText).
        self.initCompuConstText: Optional[str] = None

        # CompuMethod of the initial mode (BswMModeInitValue/BswMCompuScaleModeValue/BswMCompuMethodRef).
        self.initCompuMethodRef: Optional[str] = None

    def getName(self) -> str:
        return self.name

    def setName(self, value: str) -> "BswmModeRequestPort":
        self.name = value
        return self

    def getRequestProcessing(self) -> Optional[str]:
        return self.requestProcessing

    def setRequestProcessing(self, value: Optional[str]) -> "BswmModeRequestPort":
        self.requestProcessing = value
        return self

    def getSourceType(self) -> Optional[str]:
        return self.sourceType

    def setSourceType(self, value: Optional[str]) -> "BswmModeRequestPort":
        self.sourceType = value
        return self

    def getSourceParameters(self) -> Dict[str, List[Any]]:
        return self.sourceParameters

    def getSourceParameter(self, name: str) -> List[Any]:
        return self.sourceParameters.get(name, [])

    def addSourceParameter(self, name: str, value: Any) -> "BswmModeRequestPort":
        self.sourceParameters.setdefault(name, []).append(value)
        return self

    def getBswModeInitValue(self) -> Optional[str]:
        return self.bswModeInitValue

    def setBswModeInitValue(self, value: Optional[str]) -> "BswmModeRequestPort":
        self.bswModeInitValue = value
        return self

    def getInitCompuConstText(self) -> Optional[str]:
        return self.initCompuConstText

    def setInitCompuConstText(self, value: Optional[str]) -> "BswmModeRequestPort":
        self.initCompuConstText = value
        return self

    def getInitCompuMethodRef(self) -> Optional[str]:
        return self.initCompuMethodRef

    def setInitCompuMethodRef(self, value: Optional[str]) -> "BswmModeRequestPort":
        self.initCompuMethodRef = value
        return self


class BswmEventRequestPort:
    """A BswMEventRequestPort container (ECUC_BswM_01052) with its BswMEventRequestSource choice."""

    def __init__(self) -> None:
        # Short name identifying the BswMEventRequestPort.
        self.name: str = ""

        # BSWM_DEFERRED or BSWM_IMMEDIATE (BswMEventRequestProcessing).
        self.requestProcessing: Optional[str] = None

        # Selected BswMEventRequestSource choice, e.g. BswMComMInitiateReset.
        self.sourceType: Optional[str] = None

        # SWS-defined parameters/references of the selected source by definition short name.
        self.sourceParameters: Dict[str, List[Any]] = {}

    def getName(self) -> str:
        return self.name

    def setName(self, value: str) -> "BswmEventRequestPort":
        self.name = value
        return self

    def getRequestProcessing(self) -> Optional[str]:
        return self.requestProcessing

    def setRequestProcessing(self, value: Optional[str]) -> "BswmEventRequestPort":
        self.requestProcessing = value
        return self

    def getSourceType(self) -> Optional[str]:
        return self.sourceType

    def setSourceType(self, value: Optional[str]) -> "BswmEventRequestPort":
        self.sourceType = value
        return self

    def getSourceParameters(self) -> Dict[str, List[Any]]:
        return self.sourceParameters

    def getSourceParameter(self, name: str) -> List[Any]:
        return self.sourceParameters.get(name, [])

    def addSourceParameter(self, name: str, value: Any) -> "BswmEventRequestPort":
        self.sourceParameters.setdefault(name, []).append(value)
        return self


class BswmSwitchPort:
    """A BswMSwitchPort container (ECUC_BswM_00950): an output mode-switch port generated by the BswM."""

    def __init__(self) -> None:
        # Short name identifying the BswMSwitchPort.
        self.name: str = ""

        # Foreign reference to the MODE-SWITCH-INTERFACE (BswMModeSwitchInterfaceRef).
        self.modeSwitchInterfaceRef: Optional[str] = None

        # Foreign reference to the MODE-DECLARATION-GROUP (BswMSchMModeDeclarationGroupRef).
        self.schMModeDeclarationGroupRef: Optional[str] = None

    def getName(self) -> str:
        return self.name

    def setName(self, value: str) -> "BswmSwitchPort":
        self.name = value
        return self

    def getModeSwitchInterfaceRef(self) -> Optional[str]:
        return self.modeSwitchInterfaceRef

    def setModeSwitchInterfaceRef(self, value: Optional[str]) -> "BswmSwitchPort":
        self.modeSwitchInterfaceRef = value
        return self

    def getSchMModeDeclarationGroupRef(self) -> Optional[str]:
        return self.schMModeDeclarationGroupRef

    def setSchMModeDeclarationGroupRef(self, value: Optional[str]) -> "BswmSwitchPort":
        self.schMModeDeclarationGroupRef = value
        return self


class BswmGeneral:
    """The BswMGeneral container (ECUC_BswM_00800) with its BswMUserIncludeFiles."""

    def __init__(self) -> None:
        # SWS-defined BswMGeneral parameters by definition short name.
        self.parameters: Dict[str, Any] = {}

        # Header files included by the BswM (BswMUserIncludeFiles/BswMUserIncludeFile).
        self.userIncludeFiles: List[str] = []

    def getParameters(self) -> Dict[str, Any]:
        return self.parameters

    def setParameter(self, name: str, value: Any) -> "BswmGeneral":
        self.parameters[name] = value
        return self

    def getUserIncludeFiles(self) -> List[str]:
        return self.userIncludeFiles

    def addUserIncludeFile(self, value: str) -> "BswmGeneral":
        self.userIncludeFiles.append(value)
        return self


class BswmModule:
    """The BswM ECUC module configuration values."""

    def __init__(self) -> None:
        # Short name of the ECUC module configuration values.
        self.name: str = ""

        self.actions: List[BswmAction] = []
        self.actionLists: List[BswmActionList] = []
        self.rules: List[BswmRule] = []
        self.logicalExpressions: List[BswmLogicalExpression] = []
        self.modeConditions: List[BswmModeCondition] = []
        self.modeRequestPorts: List[BswmModeRequestPort] = []
        self.eventRequestPorts: List[BswmEventRequestPort] = []
        self.switchPorts: List[BswmSwitchPort] = []
        self.general: Optional[BswmGeneral] = None

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

    def getRules(self) -> List[BswmRule]:
        return self.rules

    def addRule(self, value: BswmRule) -> "BswmModule":
        self.rules.append(value)
        return self

    def getLogicalExpressions(self) -> List[BswmLogicalExpression]:
        return self.logicalExpressions

    def addLogicalExpression(self, value: BswmLogicalExpression) -> "BswmModule":
        self.logicalExpressions.append(value)
        return self

    def getModeConditions(self) -> List[BswmModeCondition]:
        return self.modeConditions

    def addModeCondition(self, value: BswmModeCondition) -> "BswmModule":
        self.modeConditions.append(value)
        return self

    def getModeRequestPorts(self) -> List[BswmModeRequestPort]:
        return self.modeRequestPorts

    def addModeRequestPort(self, value: BswmModeRequestPort) -> "BswmModule":
        self.modeRequestPorts.append(value)
        return self

    def getEventRequestPorts(self) -> List[BswmEventRequestPort]:
        return self.eventRequestPorts

    def addEventRequestPort(self, value: BswmEventRequestPort) -> "BswmModule":
        self.eventRequestPorts.append(value)
        return self

    def getSwitchPorts(self) -> List[BswmSwitchPort]:
        return self.switchPorts

    def addSwitchPort(self, value: BswmSwitchPort) -> "BswmModule":
        self.switchPorts.append(value)
        return self

    def getGeneral(self) -> Optional[BswmGeneral]:
        return self.general

    def setGeneral(self, value: Optional[BswmGeneral]) -> "BswmModule":
        self.general = value
        return self

    @classmethod
    def from_ecuc(cls, document, warning: bool = False) -> "BswmModule":
        from armodel.parser import BswmEcucParser

        return BswmEcucParser().parseEcuc(document, warning=warning)

    @classmethod
    def from_file(cls, path, warning: bool = False) -> "BswmModule":
        from armodel.parser import BswmEcucParser

        return BswmEcucParser().load(path, warning=warning)
