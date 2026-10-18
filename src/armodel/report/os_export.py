from typing import Any, Dict, List, Optional

from armodel.data_models.ecuc import OsAlarm, OsApplication, OsIsr, OsOs, OsScheduleTable, OsScheduleTableExpiryPoint, OsTask
from armodel.report.ecuc_export import EcucConfigExporter, EcucConfigModelMapper, EcucConfigXlsxExporter, EcucConfigYamlExporter


class OsConfigModelMapper(EcucConfigModelMapper[OsOs]):
    def application_to_dict(self, application: OsApplication) -> Dict[str, Any]:
        restart_task = application.getOsRestartTask()
        return {
            "name": application.getName(),
            "OsTrusted": application.getOsTrusted(),
            "OsTrustedApplicationDelayTimingViolationCall": application.getOsTrustedApplicationDelayTimingViolationCall(),
            "OsTrustedApplicationWithProtection": application.getOsTrustedApplicationWithProtection(),
            "OsAppAlarmRef": list(application.getOsAppAlarmRefs()),
            "OsAppCounterRef": list(application.getOsAppCounterRefs()),
            "OsAppEcucPartitionRef": application.getOsAppEcucPartitionRef(),
            "OsAppIsrRef": list(application.getOsAppIsrRefs()),
            "OsAppScheduleTableRef": list(application.getOsAppScheduleTableRefs()),
            "OsAppTaskRef": [task.getName() for task in application.getOsAppTaskRefs()],
            "OsMemoryMappingCodeLocationRef": application.getOsMemoryMappingCodeLocationRef(),
            "OsRestartTask": restart_task.getName() if restart_task is not None else None,
            "OsAppStartupHook": application.getOsAppStartupHook(),
            "OsAppErrorHook": application.getOsAppErrorHook(),
            "OsAppShutdownHook": application.getOsAppShutdownHook(),
            "OsTrustedFunctionName": list(application.getOsTrustedFunctionNames()),
            "ApplicationState": application.getApplicationState(),
        }

    def task_to_dict(self, task: OsTask) -> Dict[str, Any]:
        return {
            "name": task.getName(),
            "OsTaskActivation": task.getOsTaskActivation(),
            "OsTaskPeriod": task.getOsTaskPeriod(),
            "OsTaskPriority": task.getOsTaskPriority(),
            "OsTaskSchedule": task.getOsTaskSchedule(),
            "OsStacksize": task.getOsStacksize(),
            "OsMemoryMappingCodeLocationRef": task.getOsMemoryMappingCodeLocationRef(),
            "OsTaskAccessingApplication": [application.getName() for application in task.getOsTaskAccessingApplications()],
            "OsTaskEventRef": list(task.getOsTaskEventRefs()),
            "OsTaskResourceRef": list(task.getOsTaskResourceRefs()),
            "OsTaskAppModeRef": list(task.getOsTaskAppModeRefs()),
            "OsTaskAllInterruptLockBudget": task.getOsTaskAllInterruptLockBudget(),
            "OsTaskExecutionBudget": task.getOsTaskExecutionBudget(),
            "OsTaskOsInterruptLockBudget": task.getOsTaskOsInterruptLockBudget(),
            "OsTaskTimeFrame": task.getOsTaskTimeFrame(),
            "OsTaskResourceLockBudget": list(task.getOsTaskResourceLockBudgets()),
            "OsTaskResourceLockResourceRef": list(task.getOsTaskResourceLockResourceRefs()),
        }

    def alarm_to_dict(self, alarm: OsAlarm) -> Dict[str, Any]:
        return {
            "name": alarm.getName(),
            "OsAlarmCounterRef": alarm.getOsAlarmCounterRef(),
            "OsAlarmAccessingApplication": list(alarm.getOsAlarmAccessingApplications()),
            "OsAlarmActivateTaskRef": alarm.getOsAlarmActivateTaskRef(),
            "OsAlarmSetEventTaskRef": alarm.getOsAlarmSetEventTaskRef(),
            "OsAlarmSetEventRef": alarm.getOsAlarmSetEventRef(),
            "OsAlarmIncrementCounterRef": alarm.getOsAlarmIncrementCounterRef(),
            "OsAlarmCallbackName": alarm.getOsAlarmCallbackName(),
            "OsAlarmAlarmTime": alarm.getOsAlarmAlarmTime(),
            "OsAlarmAutostartType": alarm.getOsAlarmAutostartType(),
            "OsAlarmCycleTime": alarm.getOsAlarmCycleTime(),
            "OsAlarmAppModeRef": alarm.getOsAlarmAppModeRef(),
        }

    def isr_to_dict(self, isr: OsIsr) -> Dict[str, Any]:
        return {
            "name": isr.getName(),
            "OsIsrName": isr.getOsIsrName(),
            "OsIsrCategory": isr.getOsIsrCategory(),
            "OsIsrPriority": isr.getOsIsrPriority(),
            "OsIsrPeriod": isr.getOsIsrPeriod(),
            "OsIsrResourceRef": isr.getOsIsrResourceRef(),
            "OsIsrInterruptSource": isr.getOsIsrInterruptSource(),
            "OsIsrAccessingApplication": list(isr.getOsIsrAccessingApplications()),
            "OsMemoryMappingCodeLocationRef": isr.getOsMemoryMappingCodeLocationRef(),
            "OsIsrExecutionBudget": isr.getOsIsrExecutionBudget(),
            "OsIsrTimeFrame": isr.getOsIsrTimeFrame(),
            "OsIsrAllInterruptLockBudget": isr.getOsIsrAllInterruptLockBudget(),
            "OsIsrOsInterruptLockBudget": isr.getOsIsrOsInterruptLockBudget(),
            "OsIsrResourceLockBudget": list(isr.getOsIsrResourceLockBudgets()),
            "OsIsrResourceLockResourceRef": list(isr.getOsIsrResourceLockResourceRefs()),
        }

    def expiry_point_to_dict(self, expiry_point: OsScheduleTableExpiryPoint) -> Dict[str, Any]:
        return {
            key: value
            for key, value in {
                "OsScheduleTblExpPointOffset": expiry_point.getOsScheduleTableExpiryPointOffset(),
                "OsScheduleTableMaxShorten": expiry_point.getOsScheduleTableMaxShorten(),
                "OsScheduleTableMaxLengthen": expiry_point.getOsScheduleTableMaxLengthen(),
                "OsScheduleTableActivateTaskRef": expiry_point.getOsScheduleTableActivateTaskRef(),
                "OsScheduleTableSetEventTaskRef": expiry_point.getOsScheduleTableSetEventTaskRef(),
                "OsScheduleTableSetEventRef": expiry_point.getOsScheduleTableSetEventRef(),
            }.items()
            if value is not None
        }

    def schedule_table_to_dict(self, schedule_table: OsScheduleTable) -> Dict[str, Any]:
        return {
            "name": schedule_table.getName(),
            "OsScheduleTableCounterRef": schedule_table.getOsScheduleTableCounterRef(),
            "OsScheduleTableDuration": schedule_table.getOsScheduleTableDuration(),
            "OsScheduleTableRepeating": schedule_table.getOsScheduleTableRepeating(),
            "OsScheduleTableAccessingApplication": list(schedule_table.getOsScheduleTableAccessingApplications()),
            "OsScheduleTableAutostartType": schedule_table.getOsScheduleTableAutostartType(),
            "OsScheduleTableStartValue": schedule_table.getOsScheduleTableStartValue(),
            "OsScheduleTableAppModeRef": schedule_table.getOsScheduleTableAppModeRef(),
            "OsScheduleTableSyncStrategy": schedule_table.getOsScheduleTableSyncStrategy(),
            "OsScheduleTableExplicitPrecision": schedule_table.getOsScheduleTableExplicitPrecision(),
            "OsScheduleTableExpiryPoint": [self.expiry_point_to_dict(point) for point in schedule_table.getOsScheduleTableExpiryPoints()],
        }

    def to_dict(self, os_os: OsOs) -> Dict[str, List[Dict[str, Any]]]:
        return {
            "OsApplication": [self.application_to_dict(application) for application in os_os.getOsApplications()],
            "OsTask": [self.task_to_dict(task) for task in os_os.getOsTasks()],
            "OsAlarm": [self.alarm_to_dict(alarm) for alarm in os_os.getOsAlarms()],
            "OsIsr": [self.isr_to_dict(isr) for isr in os_os.getOsIsrs()],
            "OsScheduleTable": [self.schedule_table_to_dict(schedule_table) for schedule_table in os_os.getOsScheduleTables()],
        }

    def headers(self, section: str) -> List[str]:
        empty_rows = {
            "OsApplication": self.application_to_dict(OsApplication()),
            "OsTask": self.task_to_dict(OsTask()),
            "OsAlarm": self.alarm_to_dict(OsAlarm()),
            "OsIsr": self.isr_to_dict(OsIsr()),
            "OsScheduleTable": self.schedule_table_to_dict(OsScheduleTable()),
        }
        return list(empty_rows[section].keys()) if section in empty_rows else []


class OsConfigYamlExporter(EcucConfigYamlExporter[OsOs]):
    def __init__(self, mapper: Optional[OsConfigModelMapper] = None):
        super().__init__(mapper or OsConfigModelMapper())


class OsConfigXlsxExporter(EcucConfigXlsxExporter[OsOs]):
    def __init__(self, mapper: Optional[OsConfigModelMapper] = None):
        super().__init__(mapper or OsConfigModelMapper())


class OsConfigExporter(EcucConfigExporter[OsOs]):
    def __init__(self, mapper: Optional[OsConfigModelMapper] = None):
        super().__init__(mapper or OsConfigModelMapper(), "OS")
