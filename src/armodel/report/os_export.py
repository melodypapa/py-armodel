import os
from typing import Any, Dict, List, Union

from openpyxl.styles import Alignment

from armodel.data_models.ecuc import OsAlarm, OsApplication, OsIsr, OsOs, OsScheduleTable, OsScheduleTableExpiryPoint, OsTask
from armodel.report.excel_report import ExcelReporter


def _format_list_item(item: Any) -> str:
    if isinstance(item, dict):
        return ",".join("%s=%s" % (key, item[key]) for key in item)
    return str(item)


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

    def _headers_for(self, sheet_name: str, rows: List[Dict[str, Any]]) -> List[str]:
        if rows:
            return list(rows[0].keys())
        empty_row = {
            "OsApplication": self.mapper.application_to_dict(OsApplication()),
            "OsTask": self.mapper.task_to_dict(OsTask()),
            "OsAlarm": self.mapper.alarm_to_dict(OsAlarm()),
            "OsIsr": self.mapper.isr_to_dict(OsIsr()),
            "OsScheduleTable": self.mapper.schedule_table_to_dict(OsScheduleTable()),
        }[sheet_name]
        return list(empty_row.keys())

    def export(self, os_os: OsOs, output_path: Union[str, os.PathLike]) -> None:
        data = self.mapper.to_dict(os_os)
        for index, (sheet_name, rows) in enumerate(data.items()):
            sheet = self.wb.active if index == 0 else self.wb.create_sheet(sheet_name)
            if index == 0:
                sheet.title = sheet_name
            headers = self._headers_for(sheet_name, rows)
            self.write_title_row(sheet, headers)
            for row_index, row in enumerate(rows):
                for column_index, header in enumerate(headers):
                    value = row[header]
                    format = None
                    if isinstance(value, list):
                        value = "\n".join(_format_list_item(item) for item in value)
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
