from typing import List, Optional


class OsApplication:
    """AUTOSAR OS-Application configuration as defined by SWS_Os_00114."""

    def __init__(self) -> None:
        # Short name identifying the OS-Application.
        self.name: str = ""

        # Specifies whether the OS-Application is trusted.
        self.osTrusted: Optional[bool] = None

        # Specifies whether timing violations in a trusted OS-Application are delayed until return to the calling OS-Application.
        self.osTrustedApplicationDelayTimingViolationCall: Optional[bool] = None

        # Specifies whether a trusted OS-Application is executed with memory protection.
        self.osTrustedApplicationWithProtection: Optional[bool] = None

        # Specifies the OsAlarms that belong to the OS-Application.
        self.osAppAlarmRef: List[str] = []

        # References the OsCounters that belong to the OS-Application.
        self.osAppCounterRef: List[str] = []

        # Denotes which EcucPartition is implemented by this OS-Application.
        self.osAppEcucPartitionRef: Optional[str] = None

        # References the OsISRs that belong to the OS-Application.
        self.osAppIsrRef: List[str] = []

        # References the OsScheduleTables that belong to the OS-Application.
        self.osAppScheduleTableRef: List[str] = []

        # References the OsTasks that belong to the OS-Application.
        self.osAppTaskRef: List[OsTask] = []

        # Specifies the memory mapping code location of the OS-Application.
        self.osMemoryMappingCodeLocationRef: Optional[str] = None

        # References the task that shall be executed when the OS-Application is restarted.
        self.osRestartTask: Optional[OsTask] = None

        # Specifies whether the startup hook is enabled for the OS-Application.
        self.osAppStartupHook: Optional[bool] = None

        # Specifies whether the error hook is enabled for the OS-Application.
        self.osAppErrorHook: Optional[bool] = None

        # Specifies whether the shutdown hook is enabled for the OS-Application.
        self.osAppShutdownHook: Optional[bool] = None

        # Contains the names of trusted functions provided by the OS-Application.
        self.osTrustedFunctionName: List[str] = []

        # Specifies the initial state of the OS-Application.
        self.applicationState: str = "APPLICATION_ACCESSIBLE"

    def getName(self) -> str:
        return self.name

    def setName(self, value: str) -> "OsApplication":
        self.name = value
        return self

    def getOsTrusted(self) -> Optional[bool]:
        return self.osTrusted

    def setOsTrusted(self, value: Optional[bool]) -> "OsApplication":
        self.osTrusted = value
        return self

    def getOsTrustedApplicationDelayTimingViolationCall(self) -> Optional[bool]:
        return self.osTrustedApplicationDelayTimingViolationCall

    def setOsTrustedApplicationDelayTimingViolationCall(self, value: Optional[bool]) -> "OsApplication":
        self.osTrustedApplicationDelayTimingViolationCall = value
        return self

    def getOsTrustedApplicationWithProtection(self) -> Optional[bool]:
        return self.osTrustedApplicationWithProtection

    def setOsTrustedApplicationWithProtection(self, value: Optional[bool]) -> "OsApplication":
        self.osTrustedApplicationWithProtection = value
        return self

    def getOsAppAlarmRefs(self) -> List[str]:
        return self.osAppAlarmRef

    def addOsAppAlarmRef(self, value: str) -> "OsApplication":
        self.osAppAlarmRef.append(value)
        return self

    def getOsAppCounterRefs(self) -> List[str]:
        return self.osAppCounterRef

    def addOsAppCounterRef(self, value: str) -> "OsApplication":
        self.osAppCounterRef.append(value)
        return self

    def getOsAppEcucPartitionRef(self) -> Optional[str]:
        return self.osAppEcucPartitionRef

    def setOsAppEcucPartitionRef(self, value: Optional[str]) -> "OsApplication":
        self.osAppEcucPartitionRef = value
        return self

    def getOsAppIsrRefs(self) -> List[str]:
        return self.osAppIsrRef

    def addOsAppIsrRef(self, value: str) -> "OsApplication":
        self.osAppIsrRef.append(value)
        return self

    def getOsAppScheduleTableRefs(self) -> List[str]:
        return self.osAppScheduleTableRef

    def addOsAppScheduleTableRef(self, value: str) -> "OsApplication":
        self.osAppScheduleTableRef.append(value)
        return self

    def getOsAppTaskRefs(self) -> List["OsTask"]:
        return self.osAppTaskRef

    def addOsAppTaskRef(self, value: "OsTask") -> "OsApplication":
        self.osAppTaskRef.append(value)
        return self

    def getOsMemoryMappingCodeLocationRef(self) -> Optional[str]:
        return self.osMemoryMappingCodeLocationRef

    def setOsMemoryMappingCodeLocationRef(self, value: Optional[str]) -> "OsApplication":
        self.osMemoryMappingCodeLocationRef = value
        return self

    def getOsRestartTask(self) -> Optional["OsTask"]:
        return self.osRestartTask

    def setOsRestartTask(self, value: Optional["OsTask"]) -> "OsApplication":
        self.osRestartTask = value
        return self

    def getOsAppStartupHook(self) -> Optional[bool]:
        return self.osAppStartupHook

    def setOsAppStartupHook(self, value: Optional[bool]) -> "OsApplication":
        self.osAppStartupHook = value
        return self

    def getOsAppErrorHook(self) -> Optional[bool]:
        return self.osAppErrorHook

    def setOsAppErrorHook(self, value: Optional[bool]) -> "OsApplication":
        self.osAppErrorHook = value
        return self

    def getOsAppShutdownHook(self) -> Optional[bool]:
        return self.osAppShutdownHook

    def setOsAppShutdownHook(self, value: Optional[bool]) -> "OsApplication":
        self.osAppShutdownHook = value
        return self

    def getOsTrustedFunctionNames(self) -> List[str]:
        return self.osTrustedFunctionName

    def addOsTrustedFunctionName(self, value: str) -> "OsApplication":
        self.osTrustedFunctionName.append(value)
        return self

    def getApplicationState(self) -> str:
        return self.applicationState

    def setApplicationState(self, value: str) -> "OsApplication":
        self.applicationState = value
        return self


class OsTask:
    """AUTOSAR OS task configuration as defined by SWS_Os_00073."""

    def __init__(self) -> None:
        # Short name identifying the OS task.
        self.name: str = ""

        # Defines the maximum number of queued activation requests for the task.
        self.osTaskActivation: Optional[int] = None

        # Specifies the period in seconds for a cyclically activated task.
        self.osTaskPeriod: Optional[float] = None

        # Specifies the priority of the task.
        self.osTaskPriority: Optional[int] = None

        # Specifies the scheduling policy of the task.
        self.osTaskSchedule: Optional[str] = None

        # Specifies the stack size of the task.
        self.osStacksize: Optional[int] = None

        # Specifies the memory mapping code location of the task.
        self.osMemoryMappingCodeLocationRef: Optional[str] = None

        # References the OS-Applications that have access to the task.
        self.osTaskAccessingApplication: List[OsApplication] = []

        # References the events assigned to the task.
        self.osTaskEventRef: List[str] = []

        # References the resources assigned to the task.
        self.osTaskResourceRef: List[str] = []

        # References the application modes in which the task is started automatically.
        self.osTaskAppModeRef: List[str] = []

        # Specifies the maximum time for which the task may lock all interrupts.
        self.osTaskAllInterruptLockBudget: Optional[float] = None

        # Specifies the execution-time budget of the task.
        self.osTaskExecutionBudget: Optional[float] = None

        # Specifies the maximum time for which the task may lock OS interrupts.
        self.osTaskOsInterruptLockBudget: Optional[float] = None

        # Specifies the time frame used for task arrival protection.
        self.osTaskTimeFrame: Optional[float] = None

        # Specifies the resource-lock budgets configured for the task.
        self.osTaskResourceLockBudget: List[float] = []

        # References the resources associated with the resource-lock budgets.
        self.osTaskResourceLockResourceRef: List[str] = []

    def getName(self) -> str:
        return self.name

    def setName(self, value: str) -> "OsTask":
        self.name = value
        return self

    def getOsTaskActivation(self) -> Optional[int]:
        return self.osTaskActivation

    def setOsTaskActivation(self, value: Optional[int]) -> "OsTask":
        self.osTaskActivation = value
        return self

    def getOsTaskPeriod(self) -> Optional[float]:
        return self.osTaskPeriod

    def setOsTaskPeriod(self, value: Optional[float]) -> "OsTask":
        self.osTaskPeriod = value
        return self

    def getOsTaskPriority(self) -> Optional[int]:
        return self.osTaskPriority

    def setOsTaskPriority(self, value: Optional[int]) -> "OsTask":
        self.osTaskPriority = value
        return self

    def getOsTaskSchedule(self) -> Optional[str]:
        return self.osTaskSchedule

    def setOsTaskSchedule(self, value: Optional[str]) -> "OsTask":
        self.osTaskSchedule = value
        return self

    def getOsStacksize(self) -> Optional[int]:
        return self.osStacksize

    def setOsStacksize(self, value: Optional[int]) -> "OsTask":
        self.osStacksize = value
        return self

    def getOsMemoryMappingCodeLocationRef(self) -> Optional[str]:
        return self.osMemoryMappingCodeLocationRef

    def setOsMemoryMappingCodeLocationRef(self, value: Optional[str]) -> "OsTask":
        self.osMemoryMappingCodeLocationRef = value
        return self

    def getOsTaskAccessingApplications(self) -> List[OsApplication]:
        return self.osTaskAccessingApplication

    def addOsTaskAccessingApplication(self, value: OsApplication) -> "OsTask":
        self.osTaskAccessingApplication.append(value)
        return self

    def getOsTaskEventRefs(self) -> List[str]:
        return self.osTaskEventRef

    def addOsTaskEventRef(self, value: str) -> "OsTask":
        self.osTaskEventRef.append(value)
        return self

    def getOsTaskResourceRefs(self) -> List[str]:
        return self.osTaskResourceRef

    def addOsTaskResourceRef(self, value: str) -> "OsTask":
        self.osTaskResourceRef.append(value)
        return self

    def getOsTaskAppModeRefs(self) -> List[str]:
        return self.osTaskAppModeRef

    def addOsTaskAppModeRef(self, value: str) -> "OsTask":
        self.osTaskAppModeRef.append(value)
        return self

    def getOsTaskAllInterruptLockBudget(self) -> Optional[float]:
        return self.osTaskAllInterruptLockBudget

    def setOsTaskAllInterruptLockBudget(self, value: Optional[float]) -> "OsTask":
        self.osTaskAllInterruptLockBudget = value
        return self

    def getOsTaskExecutionBudget(self) -> Optional[float]:
        return self.osTaskExecutionBudget

    def setOsTaskExecutionBudget(self, value: Optional[float]) -> "OsTask":
        self.osTaskExecutionBudget = value
        return self

    def getOsTaskOsInterruptLockBudget(self) -> Optional[float]:
        return self.osTaskOsInterruptLockBudget

    def setOsTaskOsInterruptLockBudget(self, value: Optional[float]) -> "OsTask":
        self.osTaskOsInterruptLockBudget = value
        return self

    def getOsTaskTimeFrame(self) -> Optional[float]:
        return self.osTaskTimeFrame

    def setOsTaskTimeFrame(self, value: Optional[float]) -> "OsTask":
        self.osTaskTimeFrame = value
        return self

    def getOsTaskResourceLockBudgets(self) -> List[float]:
        return self.osTaskResourceLockBudget

    def addOsTaskResourceLockBudget(self, value: float) -> "OsTask":
        self.osTaskResourceLockBudget.append(value)
        return self

    def getOsTaskResourceLockResourceRefs(self) -> List[str]:
        return self.osTaskResourceLockResourceRef

    def addOsTaskResourceLockResourceRef(self, value: str) -> "OsTask":
        self.osTaskResourceLockResourceRef.append(value)
        return self


class OsAlarm:
    """AUTOSAR OS alarm configuration as defined by SWS_Os_00114."""

    def __init__(self) -> None:
        # Short name identifying the OS alarm.
        self.name: str = ""

        # References the counter that drives the alarm.
        self.osAlarmCounterRef: Optional[str] = None

        # References the OS-Applications that have access to the alarm.
        self.osAlarmAccessingApplication: List[str] = []

        # References the task that is activated when the alarm expires (OsAlarmActivateTask action).
        self.osAlarmActivateTaskRef: Optional[str] = None

        # References the task that receives the event when the alarm expires (OsAlarmSetEvent action).
        self.osAlarmSetEventTaskRef: Optional[str] = None

        # References the event that is set when the alarm expires (OsAlarmSetEvent action).
        self.osAlarmSetEventRef: Optional[str] = None

        # References the counter that is incremented when the alarm expires (OsAlarmIncrementCounter action).
        self.osAlarmIncrementCounterRef: Optional[str] = None

        # Specifies the callback function that is called when the alarm expires (OsAlarmCallback action).
        self.osAlarmCallbackName: Optional[str] = None

        # Specifies the alarm time of the autostart alarm (ticks).
        self.osAlarmAlarmTime: Optional[int] = None

        # Specifies whether the autostart alarm is ABSOLUTE or RELATIVE.
        self.osAlarmAutostartType: Optional[str] = None

        # Specifies the cycle time of a periodic autostart alarm (ticks).
        self.osAlarmCycleTime: Optional[int] = None

        # References the application mode in which the alarm is started automatically.
        self.osAlarmAppModeRef: Optional[str] = None

    def getName(self) -> str:
        return self.name

    def setName(self, value: str) -> "OsAlarm":
        self.name = value
        return self

    def getOsAlarmCounterRef(self) -> Optional[str]:
        return self.osAlarmCounterRef

    def setOsAlarmCounterRef(self, value: Optional[str]) -> "OsAlarm":
        self.osAlarmCounterRef = value
        return self

    def getOsAlarmAccessingApplications(self) -> List[str]:
        return self.osAlarmAccessingApplication

    def addOsAlarmAccessingApplication(self, value: str) -> "OsAlarm":
        self.osAlarmAccessingApplication.append(value)
        return self

    def getOsAlarmActivateTaskRef(self) -> Optional[str]:
        return self.osAlarmActivateTaskRef

    def setOsAlarmActivateTaskRef(self, value: Optional[str]) -> "OsAlarm":
        self.osAlarmActivateTaskRef = value
        return self

    def getOsAlarmSetEventTaskRef(self) -> Optional[str]:
        return self.osAlarmSetEventTaskRef

    def setOsAlarmSetEventTaskRef(self, value: Optional[str]) -> "OsAlarm":
        self.osAlarmSetEventTaskRef = value
        return self

    def getOsAlarmSetEventRef(self) -> Optional[str]:
        return self.osAlarmSetEventRef

    def setOsAlarmSetEventRef(self, value: Optional[str]) -> "OsAlarm":
        self.osAlarmSetEventRef = value
        return self

    def getOsAlarmIncrementCounterRef(self) -> Optional[str]:
        return self.osAlarmIncrementCounterRef

    def setOsAlarmIncrementCounterRef(self, value: Optional[str]) -> "OsAlarm":
        self.osAlarmIncrementCounterRef = value
        return self

    def getOsAlarmCallbackName(self) -> Optional[str]:
        return self.osAlarmCallbackName

    def setOsAlarmCallbackName(self, value: Optional[str]) -> "OsAlarm":
        self.osAlarmCallbackName = value
        return self

    def getOsAlarmAlarmTime(self) -> Optional[int]:
        return self.osAlarmAlarmTime

    def setOsAlarmAlarmTime(self, value: Optional[int]) -> "OsAlarm":
        self.osAlarmAlarmTime = value
        return self

    def getOsAlarmAutostartType(self) -> Optional[str]:
        return self.osAlarmAutostartType

    def setOsAlarmAutostartType(self, value: Optional[str]) -> "OsAlarm":
        self.osAlarmAutostartType = value
        return self

    def getOsAlarmCycleTime(self) -> Optional[int]:
        return self.osAlarmCycleTime

    def setOsAlarmCycleTime(self, value: Optional[int]) -> "OsAlarm":
        self.osAlarmCycleTime = value
        return self

    def getOsAlarmAppModeRef(self) -> Optional[str]:
        return self.osAlarmAppModeRef

    def setOsAlarmAppModeRef(self, value: Optional[str]) -> "OsAlarm":
        self.osAlarmAppModeRef = value
        return self


class OsOs:
    """Semantic OS configuration containing applications and tasks."""

    def __init__(self) -> None:
        # Short name identifying the OS configuration.
        self.name: str = ""

        # Contains the semantic OS-Application objects extracted from ECUC.
        self.osApplication: List[OsApplication] = []

        # Contains the semantic OS task objects extracted from ECUC.
        self.osTask: List[OsTask] = []

        # Contains the semantic OS alarm objects extracted from ECUC.
        self.osAlarm: List[OsAlarm] = []

    def getName(self) -> str:
        return self.name

    def setName(self, value: str) -> "OsOs":
        self.name = value
        return self

    def getOsApplications(self) -> List[OsApplication]:
        return self.osApplication

    def addOsApplication(self, value: OsApplication) -> "OsOs":
        self.osApplication.append(value)
        return self

    def getOsTasks(self) -> List[OsTask]:
        return self.osTask

    def addOsTask(self, value: OsTask) -> "OsOs":
        self.osTask.append(value)
        return self

    def getOsAlarms(self) -> List[OsAlarm]:
        return self.osAlarm

    def addOsAlarm(self, value: OsAlarm) -> "OsOs":
        self.osAlarm.append(value)
        return self

    @classmethod
    def from_ecuc(cls, document, warning: bool = False) -> "OsOs":
        from armodel.parser import OsEcucParser

        return OsEcucParser().parseEcuc(document, warning=warning)

    @classmethod
    def from_file(cls, path, warning: bool = False) -> "OsOs":
        from armodel.parser import OsEcucParser

        return OsEcucParser().load(path, warning=warning)
