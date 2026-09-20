import os
from typing import Any, Dict, List, Union

from armodel.data_models.ecuc import OsApplication, OsOs, OsTask
from armodel.report.excel_report import ExcelReporter


def _applicationToDict(application: OsApplication) -> Dict[str, Any]:
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


def _taskToDict(task: OsTask) -> Dict[str, Any]:
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


def osOsToDict(os_os: OsOs) -> Dict[str, List[Dict[str, Any]]]:
    return {
        "OsApplication": [_applicationToDict(application) for application in os_os.getOsApplications()],
        "OsTask": [_taskToDict(task) for task in os_os.getOsTasks()],
    }


def _cellValue(value: Any) -> Any:
    if isinstance(value, list):
        return ", ".join(str(item) for item in value)
    return value


def write_yaml(os_os: OsOs, output_path: Union[str, os.PathLike]) -> None:
    try:
        import yaml
    except ImportError as e:
        raise ImportError("pyyaml is required for YAML export: pip install pyyaml") from e

    with open(output_path, "w", encoding="utf-8") as file:
        yaml.safe_dump(osOsToDict(os_os), file, sort_keys=False)


class _OsXlsxReport(ExcelReporter):
    def __init__(self, os_os: OsOs):
        super().__init__()
        self._os_os = os_os

    def export(self, output_path: Union[str, os.PathLike]) -> None:
        data = osOsToDict(self._os_os)
        first = True
        for sheet_name, rows in data.items():
            if first:
                sheet = self.wb.active
                sheet.title = sheet_name
                first = False
            else:
                sheet = self.wb.create_sheet(sheet_name)
            if rows:
                headers = list(rows[0].keys())
            elif sheet_name == "OsApplication":
                headers = list(_applicationToDict(OsApplication()).keys())
            else:
                headers = list(_taskToDict(OsTask()).keys())
            self.write_title_row(sheet, headers)
            for row_index, row in enumerate(rows):
                for column_index, header in enumerate(headers):
                    self.write_cell(sheet, row_index + 2, column_index + 1, _cellValue(row[header]))
            self.auto_width(sheet)
        self.save(output_path)


def write_xlsx(os_os: OsOs, output_path: Union[str, os.PathLike]) -> None:
    _OsXlsxReport(os_os).export(output_path)
