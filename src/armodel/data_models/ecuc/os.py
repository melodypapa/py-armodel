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


class OsIsr:
    """AUTOSAR OS interrupt service routine configuration as defined by SWS_Os_00128."""

    def __init__(self) -> None:
        # Short name identifying the OS ISR.
        self.name: str = ""

        # Specifies the name of the ISR function.
        self.osIsrName: Optional[str] = None

        # Specifies whether the ISR is CATEGORY_1 or CATEGORY_2.
        self.osIsrCategory: Optional[str] = None

        # Specifies the priority of the ISR.
        self.osIsrPriority: Optional[int] = None

        # Specifies the period in seconds of a cyclically triggered interrupt.
        self.osIsrPeriod: Optional[float] = None

        # References the resource that is assigned to the ISR.
        self.osIsrResourceRef: Optional[str] = None

        # References the hardware interrupt source of the ISR.
        self.osIsrInterruptSource: Optional[str] = None

        # References the OS-Applications that have access to the ISR.
        self.osIsrAccessingApplication: List[str] = []

        # Specifies the memory mapping code location of the ISR.
        self.osMemoryMappingCodeLocationRef: Optional[str] = None

        # Specifies the execution-time budget of the ISR (OsIsrTimingProtection).
        self.osIsrExecutionBudget: Optional[float] = None

        # Specifies the time frame used for ISR arrival protection (OsIsrTimingProtection).
        self.osIsrTimeFrame: Optional[float] = None

        # Specifies the maximum time for which the ISR may lock all interrupts (OsIsrTimingProtection).
        self.osIsrAllInterruptLockBudget: Optional[float] = None

        # Specifies the maximum time for which the ISR may lock OS interrupts (OsIsrTimingProtection).
        self.osIsrOsInterruptLockBudget: Optional[float] = None

        # Specifies the resource-lock budgets configured for the ISR (OsIsrResourceLock).
        self.osIsrResourceLockBudget: List[float] = []

        # References the resources associated with the resource-lock budgets.
        self.osIsrResourceLockResourceRef: List[str] = []

    def getName(self) -> str:
        return self.name

    def setName(self, value: str) -> "OsIsr":
        self.name = value
        return self

    def getOsIsrName(self) -> Optional[str]:
        return self.osIsrName

    def setOsIsrName(self, value: Optional[str]) -> "OsIsr":
        self.osIsrName = value
        return self

    def getOsIsrCategory(self) -> Optional[str]:
        return self.osIsrCategory

    def setOsIsrCategory(self, value: Optional[str]) -> "OsIsr":
        self.osIsrCategory = value
        return self

    def getOsIsrPriority(self) -> Optional[int]:
        return self.osIsrPriority

    def setOsIsrPriority(self, value: Optional[int]) -> "OsIsr":
        self.osIsrPriority = value
        return self

    def getOsIsrPeriod(self) -> Optional[float]:
        return self.osIsrPeriod

    def setOsIsrPeriod(self, value: Optional[float]) -> "OsIsr":
        self.osIsrPeriod = value
        return self

    def getOsIsrResourceRef(self) -> Optional[str]:
        return self.osIsrResourceRef

    def setOsIsrResourceRef(self, value: Optional[str]) -> "OsIsr":
        self.osIsrResourceRef = value
        return self

    def getOsIsrInterruptSource(self) -> Optional[str]:
        return self.osIsrInterruptSource

    def setOsIsrInterruptSource(self, value: Optional[str]) -> "OsIsr":
        self.osIsrInterruptSource = value
        return self

    def getOsIsrAccessingApplications(self) -> List[str]:
        return self.osIsrAccessingApplication

    def addOsIsrAccessingApplication(self, value: str) -> "OsIsr":
        self.osIsrAccessingApplication.append(value)
        return self

    def getOsMemoryMappingCodeLocationRef(self) -> Optional[str]:
        return self.osMemoryMappingCodeLocationRef

    def setOsMemoryMappingCodeLocationRef(self, value: Optional[str]) -> "OsIsr":
        self.osMemoryMappingCodeLocationRef = value
        return self

    def getOsIsrExecutionBudget(self) -> Optional[float]:
        return self.osIsrExecutionBudget

    def setOsIsrExecutionBudget(self, value: Optional[float]) -> "OsIsr":
        self.osIsrExecutionBudget = value
        return self

    def getOsIsrTimeFrame(self) -> Optional[float]:
        return self.osIsrTimeFrame

    def setOsIsrTimeFrame(self, value: Optional[float]) -> "OsIsr":
        self.osIsrTimeFrame = value
        return self

    def getOsIsrAllInterruptLockBudget(self) -> Optional[float]:
        return self.osIsrAllInterruptLockBudget

    def setOsIsrAllInterruptLockBudget(self, value: Optional[float]) -> "OsIsr":
        self.osIsrAllInterruptLockBudget = value
        return self

    def getOsIsrOsInterruptLockBudget(self) -> Optional[float]:
        return self.osIsrOsInterruptLockBudget

    def setOsIsrOsInterruptLockBudget(self, value: Optional[float]) -> "OsIsr":
        self.osIsrOsInterruptLockBudget = value
        return self

    def getOsIsrResourceLockBudgets(self) -> List[float]:
        return self.osIsrResourceLockBudget

    def addOsIsrResourceLockBudget(self, value: float) -> "OsIsr":
        self.osIsrResourceLockBudget.append(value)
        return self

    def getOsIsrResourceLockResourceRefs(self) -> List[str]:
        return self.osIsrResourceLockResourceRef

    def addOsIsrResourceLockResourceRef(self, value: str) -> "OsIsr":
        self.osIsrResourceLockResourceRef.append(value)
        return self


class OsScheduleTableExpiryPoint:
    """AUTOSAR OS schedule table expiry point configuration as defined by SWS_Os_00235."""

    def __init__(self) -> None:
        # Specifies the offset of the expiry point (counter ticks).
        self.osScheduleTableExpiryPointOffset: Optional[int] = None

        # Specifies the maximum number of ticks that can be subtracted from the expiry point offset.
        self.osScheduleTableMaxShorten: Optional[int] = None

        # Specifies the maximum number of ticks that can be added to the expiry point offset.
        self.osScheduleTableMaxLengthen: Optional[int] = None

        # References the task that is activated at the expiry point (OsScheduleTableTaskActivation).
        self.osScheduleTableActivateTaskRef: Optional[str] = None

        # References the task that receives the event at the expiry point (OsScheduleTableEventSetting).
        self.osScheduleTableSetEventTaskRef: Optional[str] = None

        # References the event that is set at the expiry point (OsScheduleTableEventSetting).
        self.osScheduleTableSetEventRef: Optional[str] = None

    def getOsScheduleTableExpiryPointOffset(self) -> Optional[int]:
        return self.osScheduleTableExpiryPointOffset

    def setOsScheduleTableExpiryPointOffset(self, value: Optional[int]) -> "OsScheduleTableExpiryPoint":
        self.osScheduleTableExpiryPointOffset = value
        return self

    def getOsScheduleTableMaxShorten(self) -> Optional[int]:
        return self.osScheduleTableMaxShorten

    def setOsScheduleTableMaxShorten(self, value: Optional[int]) -> "OsScheduleTableExpiryPoint":
        self.osScheduleTableMaxShorten = value
        return self

    def getOsScheduleTableMaxLengthen(self) -> Optional[int]:
        return self.osScheduleTableMaxLengthen

    def setOsScheduleTableMaxLengthen(self, value: Optional[int]) -> "OsScheduleTableExpiryPoint":
        self.osScheduleTableMaxLengthen = value
        return self

    def getOsScheduleTableActivateTaskRef(self) -> Optional[str]:
        return self.osScheduleTableActivateTaskRef

    def setOsScheduleTableActivateTaskRef(self, value: Optional[str]) -> "OsScheduleTableExpiryPoint":
        self.osScheduleTableActivateTaskRef = value
        return self

    def getOsScheduleTableSetEventTaskRef(self) -> Optional[str]:
        return self.osScheduleTableSetEventTaskRef

    def setOsScheduleTableSetEventTaskRef(self, value: Optional[str]) -> "OsScheduleTableExpiryPoint":
        self.osScheduleTableSetEventTaskRef = value
        return self

    def getOsScheduleTableSetEventRef(self) -> Optional[str]:
        return self.osScheduleTableSetEventRef

    def setOsScheduleTableSetEventRef(self, value: Optional[str]) -> "OsScheduleTableExpiryPoint":
        self.osScheduleTableSetEventRef = value
        return self


class OsScheduleTable:
    """AUTOSAR OS schedule table configuration as defined by SWS_Os_00232."""

    def __init__(self) -> None:
        # Short name identifying the OS schedule table.
        self.name: str = ""

        # References the counter that drives the schedule table.
        self.osScheduleTableCounterRef: Optional[str] = None

        # Specifies the duration of the schedule table (counter ticks).
        self.osScheduleTableDuration: Optional[int] = None

        # Specifies whether the schedule table is repeated after completion.
        self.osScheduleTableRepeating: Optional[bool] = None

        # References the OS-Applications that have access to the schedule table.
        self.osScheduleTableAccessingApplication: List[str] = []

        # Contains the expiry points of the schedule table in configuration order.
        self.osScheduleTableExpiryPoint: List[OsScheduleTableExpiryPoint] = []

        # Specifies whether the autostart schedule table is ABSOLUTE or RELATIVE.
        self.osScheduleTableAutostartType: Optional[str] = None

        # Specifies the absolute tick value or relative offset when the schedule table starts.
        self.osScheduleTableStartValue: Optional[int] = None

        # References the application mode in which the schedule table is started automatically.
        self.osScheduleTableAppModeRef: Optional[str] = None

        # Specifies the synchronization strategy (NONE, IMPLICIT, or EXPLICIT).
        self.osScheduleTableSyncStrategy: Optional[str] = None

        # Specifies the maximum adjustment for explicit synchronization (counter ticks).
        self.osScheduleTableExplicitPrecision: Optional[int] = None

    def getName(self) -> str:
        return self.name

    def setName(self, value: str) -> "OsScheduleTable":
        self.name = value
        return self

    def getOsScheduleTableCounterRef(self) -> Optional[str]:
        return self.osScheduleTableCounterRef

    def setOsScheduleTableCounterRef(self, value: Optional[str]) -> "OsScheduleTable":
        self.osScheduleTableCounterRef = value
        return self

    def getOsScheduleTableDuration(self) -> Optional[int]:
        return self.osScheduleTableDuration

    def setOsScheduleTableDuration(self, value: Optional[int]) -> "OsScheduleTable":
        self.osScheduleTableDuration = value
        return self

    def getOsScheduleTableRepeating(self) -> Optional[bool]:
        return self.osScheduleTableRepeating

    def setOsScheduleTableRepeating(self, value: Optional[bool]) -> "OsScheduleTable":
        self.osScheduleTableRepeating = value
        return self

    def getOsScheduleTableAccessingApplications(self) -> List[str]:
        return self.osScheduleTableAccessingApplication

    def addOsScheduleTableAccessingApplication(self, value: str) -> "OsScheduleTable":
        self.osScheduleTableAccessingApplication.append(value)
        return self

    def getOsScheduleTableExpiryPoints(self) -> List[OsScheduleTableExpiryPoint]:
        return self.osScheduleTableExpiryPoint

    def addOsScheduleTableExpiryPoint(self, value: OsScheduleTableExpiryPoint) -> "OsScheduleTable":
        self.osScheduleTableExpiryPoint.append(value)
        return self

    def getOsScheduleTableAutostartType(self) -> Optional[str]:
        return self.osScheduleTableAutostartType

    def setOsScheduleTableAutostartType(self, value: Optional[str]) -> "OsScheduleTable":
        self.osScheduleTableAutostartType = value
        return self

    def getOsScheduleTableStartValue(self) -> Optional[int]:
        return self.osScheduleTableStartValue

    def setOsScheduleTableStartValue(self, value: Optional[int]) -> "OsScheduleTable":
        self.osScheduleTableStartValue = value
        return self

    def getOsScheduleTableAppModeRef(self) -> Optional[str]:
        return self.osScheduleTableAppModeRef

    def setOsScheduleTableAppModeRef(self, value: Optional[str]) -> "OsScheduleTable":
        self.osScheduleTableAppModeRef = value
        return self

    def getOsScheduleTableSyncStrategy(self) -> Optional[str]:
        return self.osScheduleTableSyncStrategy

    def setOsScheduleTableSyncStrategy(self, value: Optional[str]) -> "OsScheduleTable":
        self.osScheduleTableSyncStrategy = value
        return self

    def getOsScheduleTableExplicitPrecision(self) -> Optional[int]:
        return self.osScheduleTableExplicitPrecision

    def setOsScheduleTableExplicitPrecision(self, value: Optional[int]) -> "OsScheduleTable":
        self.osScheduleTableExplicitPrecision = value
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

        # Contains the semantic OS ISR objects extracted from ECUC.
        self.osIsr: List[OsIsr] = []

        # Contains the semantic OS schedule table objects extracted from ECUC.
        self.osScheduleTable: List[OsScheduleTable] = []

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

    def getOsIsrs(self) -> List[OsIsr]:
        return self.osIsr

    def addOsIsr(self, value: OsIsr) -> "OsOs":
        self.osIsr.append(value)
        return self

    def getOsScheduleTables(self) -> List[OsScheduleTable]:
        return self.osScheduleTable

    def addOsScheduleTable(self, value: OsScheduleTable) -> "OsOs":
        self.osScheduleTable.append(value)
        return self

    @classmethod
    def from_ecuc(cls, document, warning: bool = False) -> "OsOs":
        from armodel.parser import OsEcucParser

        return OsEcucParser().parseEcuc(document, warning=warning)

    @classmethod
    def from_file(cls, path, warning: bool = False) -> "OsOs":
        from armodel.parser import OsEcucParser

        return OsEcucParser().load(path, warning=warning)
