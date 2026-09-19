from typing import List, Optional


class OsApplication:
    def __init__(self) -> None:
        self.name: str = ""
        self.OsTrusted: Optional[bool] = None
        self.OsTrustedApplicationDelayTimingViolationCall: Optional[bool] = None
        self.OsTrustedApplicationWithProtection: Optional[bool] = None
        self.OsAppAlarmRef: List[str] = []
        self.OsAppCounterRef: List[str] = []
        self.OsAppEcucPartitionRef: Optional[str] = None
        self.OsAppIsrRef: List[str] = []
        self.OsAppScheduleTableRef: List[str] = []
        self.OsAppTaskRef: List[OsTask] = []
        self.OsMemoryMappingCodeLocationRef: Optional[str] = None
        self.OsRestartTask: Optional[OsTask] = None
        self.OsAppStartupHook: Optional[bool] = None
        self.OsAppErrorHook: Optional[bool] = None
        self.OsAppShutdownHook: Optional[bool] = None
        self.OsTrustedFunctionName: List[str] = []
        self.ApplicationState: str = "APPLICATION_ACCESSIBLE"

    def getName(self) -> str:
        return self.name

    def setName(self, value: str) -> "OsApplication":
        self.name = value
        return self

    def getOsTrusted(self) -> Optional[bool]:
        return self.OsTrusted

    def setOsTrusted(self, value: Optional[bool]) -> "OsApplication":
        self.OsTrusted = value
        return self

    def getOsTrustedApplicationDelayTimingViolationCall(self) -> Optional[bool]:
        return self.OsTrustedApplicationDelayTimingViolationCall

    def setOsTrustedApplicationDelayTimingViolationCall(self, value: Optional[bool]) -> "OsApplication":
        self.OsTrustedApplicationDelayTimingViolationCall = value
        return self

    def getOsTrustedApplicationWithProtection(self) -> Optional[bool]:
        return self.OsTrustedApplicationWithProtection

    def setOsTrustedApplicationWithProtection(self, value: Optional[bool]) -> "OsApplication":
        self.OsTrustedApplicationWithProtection = value
        return self

    def getOsAppAlarmRefs(self) -> List[str]:
        return self.OsAppAlarmRef

    def addOsAppAlarmRef(self, value: str) -> "OsApplication":
        self.OsAppAlarmRef.append(value)
        return self

    def getOsAppCounterRefs(self) -> List[str]:
        return self.OsAppCounterRef

    def addOsAppCounterRef(self, value: str) -> "OsApplication":
        self.OsAppCounterRef.append(value)
        return self

    def getOsAppEcucPartitionRef(self) -> Optional[str]:
        return self.OsAppEcucPartitionRef

    def setOsAppEcucPartitionRef(self, value: Optional[str]) -> "OsApplication":
        self.OsAppEcucPartitionRef = value
        return self

    def getOsAppIsrRefs(self) -> List[str]:
        return self.OsAppIsrRef

    def addOsAppIsrRef(self, value: str) -> "OsApplication":
        self.OsAppIsrRef.append(value)
        return self

    def getOsAppScheduleTableRefs(self) -> List[str]:
        return self.OsAppScheduleTableRef

    def addOsAppScheduleTableRef(self, value: str) -> "OsApplication":
        self.OsAppScheduleTableRef.append(value)
        return self

    def getOsAppTaskRefs(self) -> List["OsTask"]:
        return self.OsAppTaskRef

    def addOsAppTaskRef(self, value: "OsTask") -> "OsApplication":
        self.OsAppTaskRef.append(value)
        return self

    def getOsMemoryMappingCodeLocationRef(self) -> Optional[str]:
        return self.OsMemoryMappingCodeLocationRef

    def setOsMemoryMappingCodeLocationRef(self, value: Optional[str]) -> "OsApplication":
        self.OsMemoryMappingCodeLocationRef = value
        return self

    def getOsRestartTask(self) -> Optional["OsTask"]:
        return self.OsRestartTask

    def setOsRestartTask(self, value: Optional["OsTask"]) -> "OsApplication":
        self.OsRestartTask = value
        return self

    def getOsAppStartupHook(self) -> Optional[bool]:
        return self.OsAppStartupHook

    def setOsAppStartupHook(self, value: Optional[bool]) -> "OsApplication":
        self.OsAppStartupHook = value
        return self

    def getOsAppErrorHook(self) -> Optional[bool]:
        return self.OsAppErrorHook

    def setOsAppErrorHook(self, value: Optional[bool]) -> "OsApplication":
        self.OsAppErrorHook = value
        return self

    def getOsAppShutdownHook(self) -> Optional[bool]:
        return self.OsAppShutdownHook

    def setOsAppShutdownHook(self, value: Optional[bool]) -> "OsApplication":
        self.OsAppShutdownHook = value
        return self

    def getOsTrustedFunctionNames(self) -> List[str]:
        return self.OsTrustedFunctionName

    def addOsTrustedFunctionName(self, value: str) -> "OsApplication":
        self.OsTrustedFunctionName.append(value)
        return self

    def getApplicationState(self) -> str:
        return self.ApplicationState

    def setApplicationState(self, value: str) -> "OsApplication":
        self.ApplicationState = value
        return self


class OsTask:
    def __init__(self) -> None:
        self.name: str = ""
        self.OsTaskActivation: Optional[int] = None
        self.OsTaskPeriod: Optional[float] = None
        self.OsTaskPriority: Optional[int] = None
        self.OsTaskSchedule: Optional[str] = None
        self.OsStacksize: Optional[int] = None
        self.OsMemoryMappingCodeLocationRef: Optional[str] = None
        self.OsTaskAccessingApplication: List[OsApplication] = []
        self.OsTaskEventRef: List[str] = []
        self.OsTaskResourceRef: List[str] = []
        self.OsTaskAppModeRef: List[str] = []
        self.OsTaskAllInterruptLockBudget: Optional[float] = None
        self.OsTaskExecutionBudget: Optional[float] = None
        self.OsTaskOsInterruptLockBudget: Optional[float] = None
        self.OsTaskTimeFrame: Optional[float] = None
        self.OsTaskResourceLockBudget: List[float] = []
        self.OsTaskResourceLockResourceRef: List[str] = []

    def getName(self) -> str:
        return self.name

    def setName(self, value: str) -> "OsTask":
        self.name = value
        return self

    def getOsTaskActivation(self) -> Optional[int]:
        return self.OsTaskActivation

    def setOsTaskActivation(self, value: Optional[int]) -> "OsTask":
        self.OsTaskActivation = value
        return self

    def getOsTaskPeriod(self) -> Optional[float]:
        return self.OsTaskPeriod

    def setOsTaskPeriod(self, value: Optional[float]) -> "OsTask":
        self.OsTaskPeriod = value
        return self

    def getOsTaskPriority(self) -> Optional[int]:
        return self.OsTaskPriority

    def setOsTaskPriority(self, value: Optional[int]) -> "OsTask":
        self.OsTaskPriority = value
        return self

    def getOsTaskSchedule(self) -> Optional[str]:
        return self.OsTaskSchedule

    def setOsTaskSchedule(self, value: Optional[str]) -> "OsTask":
        self.OsTaskSchedule = value
        return self

    def getOsStacksize(self) -> Optional[int]:
        return self.OsStacksize

    def setOsStacksize(self, value: Optional[int]) -> "OsTask":
        self.OsStacksize = value
        return self

    def getOsMemoryMappingCodeLocationRef(self) -> Optional[str]:
        return self.OsMemoryMappingCodeLocationRef

    def setOsMemoryMappingCodeLocationRef(self, value: Optional[str]) -> "OsTask":
        self.OsMemoryMappingCodeLocationRef = value
        return self

    def getOsTaskAccessingApplications(self) -> List[OsApplication]:
        return self.OsTaskAccessingApplication

    def addOsTaskAccessingApplication(self, value: OsApplication) -> "OsTask":
        self.OsTaskAccessingApplication.append(value)
        return self

    def getOsTaskEventRefs(self) -> List[str]:
        return self.OsTaskEventRef

    def addOsTaskEventRef(self, value: str) -> "OsTask":
        self.OsTaskEventRef.append(value)
        return self

    def getOsTaskResourceRefs(self) -> List[str]:
        return self.OsTaskResourceRef

    def addOsTaskResourceRef(self, value: str) -> "OsTask":
        self.OsTaskResourceRef.append(value)
        return self

    def getOsTaskAppModeRefs(self) -> List[str]:
        return self.OsTaskAppModeRef

    def addOsTaskAppModeRef(self, value: str) -> "OsTask":
        self.OsTaskAppModeRef.append(value)
        return self

    def getOsTaskAllInterruptLockBudget(self) -> Optional[float]:
        return self.OsTaskAllInterruptLockBudget

    def setOsTaskAllInterruptLockBudget(self, value: Optional[float]) -> "OsTask":
        self.OsTaskAllInterruptLockBudget = value
        return self

    def getOsTaskExecutionBudget(self) -> Optional[float]:
        return self.OsTaskExecutionBudget

    def setOsTaskExecutionBudget(self, value: Optional[float]) -> "OsTask":
        self.OsTaskExecutionBudget = value
        return self

    def getOsTaskOsInterruptLockBudget(self) -> Optional[float]:
        return self.OsTaskOsInterruptLockBudget

    def setOsTaskOsInterruptLockBudget(self, value: Optional[float]) -> "OsTask":
        self.OsTaskOsInterruptLockBudget = value
        return self

    def getOsTaskTimeFrame(self) -> Optional[float]:
        return self.OsTaskTimeFrame

    def setOsTaskTimeFrame(self, value: Optional[float]) -> "OsTask":
        self.OsTaskTimeFrame = value
        return self

    def getOsTaskResourceLockBudgets(self) -> List[float]:
        return self.OsTaskResourceLockBudget

    def addOsTaskResourceLockBudget(self, value: float) -> "OsTask":
        self.OsTaskResourceLockBudget.append(value)
        return self

    def getOsTaskResourceLockResourceRefs(self) -> List[str]:
        return self.OsTaskResourceLockResourceRef

    def addOsTaskResourceLockResourceRef(self, value: str) -> "OsTask":
        self.OsTaskResourceLockResourceRef.append(value)
        return self


class OsOs:
    def __init__(self) -> None:
        self.name: str = ""
        self.OsApplication: List[OsApplication] = []
        self.OsTask: List[OsTask] = []

    def getName(self) -> str:
        return self.name

    def setName(self, value: str) -> "OsOs":
        self.name = value
        return self

    def getOsApplications(self) -> List[OsApplication]:
        return self.OsApplication

    def addOsApplication(self, value: OsApplication) -> "OsOs":
        self.OsApplication.append(value)
        return self

    def getOsTasks(self) -> List[OsTask]:
        return self.OsTask

    def addOsTask(self, value: OsTask) -> "OsOs":
        self.OsTask.append(value)
        return self
