import os
from typing import Any, Dict, List, Union

from openpyxl.styles import Alignment

from armodel.data_models.ecuc import OsApplication, OsOs, OsTask
from armodel.report.excel_report import ExcelReporter


class OsConfigModelMapper:
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

    def to_dict(self, os_os: OsOs) -> Dict[str, List[Dict[str, Any]]]:
        return {
            "OsApplication": [self.application_to_dict(application) for application in os_os.getOsApplications()],
            "OsTask": [self.task_to_dict(task) for task in os_os.getOsTasks()],
        }


class OsConfigYamlExporter:
    def __init__(self, mapper: OsConfigModelMapper = None):
        self.mapper = mapper or OsConfigModelMapper()

    def export(self, os_os: OsOs, output_path: Union[str, os.PathLike]) -> None:
        try:
            import yaml
        except ImportError as e:
            raise ImportError("pyyaml is required for YAML export: pip install pyyaml") from e

        data = self.mapper.to_dict(os_os)
        filtered_data = {section: [{key: value for key, value in row.items() if value is not None and value != []} for row in rows] for section, rows in data.items()}
        with open(output_path, "w", encoding="utf-8") as file:
            yaml.safe_dump(filtered_data, file, sort_keys=False)


class OsConfigXlsxExporter(ExcelReporter):
    def __init__(self, mapper: OsConfigModelMapper = None):
        super().__init__()
        self.mapper = mapper or OsConfigModelMapper()

    def export(self, os_os: OsOs, output_path: Union[str, os.PathLike]) -> None:
        data = self.mapper.to_dict(os_os)
        for index, (sheet_name, rows) in enumerate(data.items()):
            sheet = self.wb.active if index == 0 else self.wb.create_sheet(sheet_name)
            if index == 0:
                sheet.title = sheet_name
            headers = (
                list(rows[0].keys()) if rows else list(self.mapper.application_to_dict(OsApplication()).keys()) if sheet_name == "OsApplication" else list(self.mapper.task_to_dict(OsTask()).keys())
            )
            self.write_title_row(sheet, headers)
            for row_index, row in enumerate(rows):
                for column_index, header in enumerate(headers):
                    value = row[header]
                    format = None
                    if isinstance(value, list):
                        value = "\n".join(str(item) for item in value)
                        format = {"alignment": Alignment(wrap_text=True)}
                    self.write_cell(sheet, row_index + 2, column_index + 1, value, format)
            self.auto_width(sheet)
        self.save(output_path)


class OsConfigExporter:
    def __init__(self, mapper: OsConfigModelMapper = None):
        mapper = mapper or OsConfigModelMapper()
        self._exporters = {"yaml": OsConfigYamlExporter(mapper), "xlsx": OsConfigXlsxExporter(mapper)}

    def export(self, os_os: OsOs, output_path: Union[str, os.PathLike]) -> None:
        extension = os.path.splitext(os.fspath(output_path))[1].lower().lstrip(".")
        if extension == "yml":
            extension = "yaml"
        try:
            exporter = self._exporters[extension]
        except KeyError as e:
            raise ValueError("Unsupported OS configuration export format: %s" % extension) from e
        exporter.export(os_os, output_path)
