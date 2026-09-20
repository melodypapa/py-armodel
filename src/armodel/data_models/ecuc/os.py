from typing import List, Optional


class OsApplication:
    """AUTOSAR OS-Application configuration as defined by SWS_Os_00114."""

    def __init__(self) -> None:
        self.name: str = ""
        self.osTrusted: Optional[bool] = None
        self.osTrustedApplicationDelayTimingViolationCall: Optional[bool] = None
        self.osTrustedApplicationWithProtection: Optional[bool] = None
        self.osAppAlarmRef: List[str] = []
        self.osAppCounterRef: List[str] = []
        self.osAppEcucPartitionRef: Optional[str] = None
        self.osAppIsrRef: List[str] = []
        self.osAppScheduleTableRef: List[str] = []
        self.osAppTaskRef: List[OsTask] = []
        self.osMemoryMappingCodeLocationRef: Optional[str] = None
        self.osRestartTask: Optional[OsTask] = None
        self.osAppStartupHook: Optional[bool] = None
        self.osAppErrorHook: Optional[bool] = None
        self.osAppShutdownHook: Optional[bool] = None
        self.osTrustedFunctionName: List[str] = []
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
        self.name: str = ""
        self.osTaskActivation: Optional[int] = None
        self.osTaskPeriod: Optional[float] = None
        self.osTaskPriority: Optional[int] = None
        self.osTaskSchedule: Optional[str] = None
        self.osStacksize: Optional[int] = None
        self.osMemoryMappingCodeLocationRef: Optional[str] = None
        self.osTaskAccessingApplication: List[OsApplication] = []
        self.osTaskEventRef: List[str] = []
        self.osTaskResourceRef: List[str] = []
        self.osTaskAppModeRef: List[str] = []
        self.osTaskAllInterruptLockBudget: Optional[float] = None
        self.osTaskExecutionBudget: Optional[float] = None
        self.osTaskOsInterruptLockBudget: Optional[float] = None
        self.osTaskTimeFrame: Optional[float] = None
        self.osTaskResourceLockBudget: List[float] = []
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


class OsOs:
    """Semantic OS configuration containing applications and tasks."""

    def __init__(self) -> None:
        self.name: str = ""
        self.osApplication: List[OsApplication] = []
        self.osTask: List[OsTask] = []

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

    @classmethod
    def from_ecuc(cls, document, warning: bool = False) -> "OsOs":
        from armodel.parser import OsEcucParser

        return OsEcucParser().parseEcuc(document, warning=warning)

    @classmethod
    def from_file(cls, path, warning: bool = False) -> "OsOs":
        from armodel.parser import OsEcucParser

        return OsEcucParser().load(path, warning=warning)
