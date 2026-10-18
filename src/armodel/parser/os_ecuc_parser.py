import logging
from typing import Dict, List, Optional, TypeVar

from armodel.data_models.ecuc import OsAlarm, OsApplication, OsIsr, OsOs, OsScheduleTable, OsScheduleTableExpiryPoint, OsTask
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import Container
from armodel.parser.ecuc_parser import EcucParser

ValueType = TypeVar("ValueType")

logger = logging.getLogger("armodel.parser.os_ecuc_parser")


class OsEcucConversionError(Exception):
    pass


class OsEcucParser(EcucParser):
    conversion_error = OsEcucConversionError

    def __init__(self):
        super().__init__()

    def load(self, path: str, document: Optional[AUTOSAR] = None, warning: bool = False) -> OsOs:
        return super().load(path, document=document, warning=warning)

    def parseEcuc(self, document: AUTOSAR, warning: bool = False) -> OsOs:
        modules = self.get_modules(document)
        index: Dict[str, Container] = self.get_module_containers(document, module_name="Os")
        os_name = None
        for module in modules:
            if self.get_definition_name(module.getDefinitionRef()) != "Os":
                continue
            if os_name is None:
                os_name = module.getShortName()

        os_os = OsOs()
        os_os.setName(os_name if os_name is not None else "Os")

        tasks: Dict[str, OsTask] = {}
        applications: Dict[str, OsApplication] = {}
        for path in index:
            container = index[path]
            if self.get_definition_name(container.getDefinitionRef()) == "OsTask":
                task = OsTask()
                task.setName(container.getShortName())
                self.logger.info("Parsing OsTask: %s", task.getName())
                self.get_collect_task(task, container, index, warning)
                tasks[path] = task
                os_os.addOsTask(task)
        for path in index:
            container = index[path]
            if self.get_definition_name(container.getDefinitionRef()) == "OsApplication":
                application = OsApplication()
                application.setName(container.getShortName())
                self.logger.info("Parsing OsApplication: %s", application.getName())
                self.get_collect_application(application, container, index, warning)
                applications[path] = application
                os_os.addOsApplication(application)

        for path in tasks:
            self.get_resolve_task_objects(tasks[path], index[path], applications, index, warning)
        for path in applications:
            self.get_resolve_application_objects(applications[path], index[path], tasks, index, warning)

        alarms: Dict[str, OsAlarm] = {}
        for path in index:
            container = index[path]
            if self.get_definition_name(container.getDefinitionRef()) == "OsAlarm":
                alarm = OsAlarm()
                alarm.setName(container.getShortName())
                self.logger.info("Parsing OsAlarm: %s", alarm.getName())
                self.get_collect_alarm(alarm, container, index, warning)
                alarms[path] = alarm
                os_os.addOsAlarm(alarm)

        isrs: Dict[str, OsIsr] = {}
        for path in index:
            container = index[path]
            if self.get_definition_name(container.getDefinitionRef()) == "OsIsr":
                isr = OsIsr()
                isr.setName(container.getShortName())
                self.logger.info("Parsing OsIsr: %s", isr.getName())
                self.get_collect_isr(isr, container, index, warning)
                isrs[path] = isr
                os_os.addOsIsr(isr)

        schedule_tables: Dict[str, OsScheduleTable] = {}
        for path in index:
            container = index[path]
            if self.get_definition_name(container.getDefinitionRef()) == "OsScheduleTable":
                schedule_table = OsScheduleTable()
                schedule_table.setName(container.getShortName())
                self.logger.info("Parsing OsScheduleTable: %s", schedule_table.getName())
                self.get_collect_schedule_table(schedule_table, container, index, warning)
                schedule_tables[path] = schedule_table
                os_os.addOsScheduleTable(schedule_table)
        return os_os

    def get_collect_alarm(self, alarm: OsAlarm, container: Container, index: Dict[str, Container], warning: bool) -> None:
        for name, raw in self.iter_parameters(container):
            if name == "OsAlarmCallbackName":
                alarm.setOsAlarmCallbackName(self.get_str(name, raw))
            else:
                self.logger.debug("Ignore non-standard OsAlarm parameter %s" % name)

        for name, path in self.iter_references(container):
            if name == "OsAlarmCounterRef":
                alarm.setOsAlarmCounterRef(self.check_reference_path(name, path, index))
            elif name == "OsAlarmAccessingApplication":
                alarm.addOsAlarmAccessingApplication(self.check_reference_path(name, path, index))
            else:
                self.logger.debug("Ignore non-standard OsAlarm reference %s" % name)

        sub_containers = self.get_sub_containers_by_name(container)
        for autostart in sub_containers.get("OsAlarmAutostart", []):
            for name, raw in self.iter_parameters(autostart):
                if name == "OsAlarmAlarmTime":
                    alarm.setOsAlarmAlarmTime(self.get_int(name, raw))
                elif name == "OsAlarmAutostartType":
                    alarm.setOsAlarmAutostartType(self.get_str(name, raw))
                elif name == "OsAlarmCycleTime":
                    alarm.setOsAlarmCycleTime(self.get_int(name, raw))
                else:
                    self.logger.debug("Ignore non-standard OsAlarmAutostart parameter %s" % name)
            for name, path in self.iter_references(autostart):
                if name == "OsAlarmAppModeRef":
                    alarm.setOsAlarmAppModeRef(self.check_reference_path(name, path, index))
                else:
                    self.logger.debug("Ignore non-standard OsAlarmAutostart reference %s" % name)

        action_containers = []
        for choice in ("OsAlarmActivateTask", "OsAlarmCallback", "OsAlarmIncrementCounter", "OsAlarmSetEvent"):
            action_containers.extend(sub_containers.get(choice, []))
        for action in action_containers:
            for name, path in self.iter_references(action):
                if name == "OsAlarmActivateTaskRef":
                    alarm.setOsAlarmActivateTaskRef(self.check_reference_path(name, path, index))
                elif name == "OsAlarmSetEventTaskRef":
                    alarm.setOsAlarmSetEventTaskRef(self.check_reference_path(name, path, index))
                elif name == "OsAlarmSetEventRef":
                    alarm.setOsAlarmSetEventRef(self.check_reference_path(name, path, index))
                elif name == "OsAlarmIncrementCounterRef":
                    alarm.setOsAlarmIncrementCounterRef(self.check_reference_path(name, path, index))
                else:
                    self.logger.debug("Ignore non-standard OsAlarmAction reference %s" % name)
            for name, raw in self.iter_parameters(action):
                if name == "OsAlarmCallbackName":
                    alarm.setOsAlarmCallbackName(self.get_str(name, raw))
                else:
                    self.logger.debug("Ignore non-standard OsAlarmAction parameter %s" % name)

    def get_collect_isr(self, isr: OsIsr, container: Container, index: Dict[str, Container], warning: bool) -> None:
        for name, raw in self.iter_parameters(container):
            if name == "OsIsrCategory":
                isr.setOsIsrCategory(self.get_str(name, raw))
            elif name == "OsIsrPeriod":
                isr.setOsIsrPeriod(self.get_float(name, raw))
            elif name == "OsIsrPriority":
                isr.setOsIsrPriority(self.get_int(name, raw))
            elif name == "OsIsrName":
                isr.setOsIsrName(self.get_str(name, raw))
            else:
                self.logger.debug("Ignore non-standard OsIsr parameter %s" % name)

        for name, path in self.iter_references(container):
            if name == "OsIsrResourceRef":
                isr.setOsIsrResourceRef(self.check_reference_path(name, path, index))
            elif name == "OsIsrInterruptSource":
                isr.setOsIsrInterruptSource(self.check_reference_path(name, path, index))
            elif name == "OsIsrAccessingApplication":
                isr.addOsIsrAccessingApplication(self.check_reference_path(name, path, index))
            elif name == "OsMemoryMappingCodeLocationRef":
                isr.setOsMemoryMappingCodeLocationRef(self.check_reference_path(name, path, index))
            else:
                self.logger.debug("Ignore non-standard OsIsr reference %s" % name)

        sub_containers = self.get_sub_containers_by_name(container)
        for timing_protection in sub_containers.get("OsIsrTimingProtection", []):
            for name, raw in self.iter_parameters(timing_protection):
                if name == "OsIsrExecutionBudget":
                    isr.setOsIsrExecutionBudget(self.get_float(name, raw))
                elif name == "OsIsrTimeFrame":
                    isr.setOsIsrTimeFrame(self.get_float(name, raw))
                elif name == "OsIsrAllInterruptLockBudget":
                    isr.setOsIsrAllInterruptLockBudget(self.get_float(name, raw))
                elif name == "OsIsrOsInterruptLockBudget":
                    isr.setOsIsrOsInterruptLockBudget(self.get_float(name, raw))
                else:
                    self.logger.debug("Ignore non-standard OsIsrTimingProtection parameter %s" % name)
            for resource_lock in self.get_sub_containers_by_name(timing_protection).get("OsIsrResourceLock", []):
                for name, raw in self.iter_parameters(resource_lock):
                    if name == "OsIsrResourceLockBudget":
                        budget = self.get_float(name, raw)
                        if budget is not None:
                            isr.addOsIsrResourceLockBudget(budget)
                    else:
                        self.logger.debug("Ignore non-standard OsIsrResourceLock parameter %s" % name)
                for name, path in self.iter_references(resource_lock):
                    if name == "OsIsrResourceLockResourceRef":
                        isr.addOsIsrResourceLockResourceRef(self.check_reference_path(name, path, index))
                    else:
                        self.logger.debug("Ignore non-standard OsIsrResourceLock reference %s" % name)

    def get_collect_schedule_table(self, schedule_table: OsScheduleTable, container: Container, index: Dict[str, Container], warning: bool) -> None:
        for name, raw in self.iter_parameters(container):
            if name == "OsScheduleTableDuration":
                schedule_table.setOsScheduleTableDuration(self.get_int(name, raw))
            elif name == "OsScheduleTableRepeating":
                schedule_table.setOsScheduleTableRepeating(self.get_bool(name, raw))
            else:
                self.logger.debug("Ignore non-standard OsScheduleTable parameter %s" % name)

        for name, path in self.iter_references(container):
            if name == "OsScheduleTableCounterRef":
                schedule_table.setOsScheduleTableCounterRef(self.check_reference_path(name, path, index))
            elif name == "OsScheduleTableAccessingApplication":
                schedule_table.addOsScheduleTableAccessingApplication(self.check_reference_path(name, path, index))
            else:
                self.logger.debug("Ignore non-standard OsScheduleTable reference %s" % name)

        sub_containers = self.get_sub_containers_by_name(container)
        for autostart in sub_containers.get("OsScheduleTableAutostart", []):
            for name, raw in self.iter_parameters(autostart):
                if name == "OsScheduleTableAutostartType":
                    schedule_table.setOsScheduleTableAutostartType(self.get_str(name, raw))
                elif name == "OsScheduleTableStartValue":
                    schedule_table.setOsScheduleTableStartValue(self.get_int(name, raw))
                else:
                    self.logger.debug("Ignore non-standard OsScheduleTableAutostart parameter %s" % name)
            for name, path in self.iter_references(autostart):
                if name == "OsScheduleTableAppModeRef":
                    schedule_table.setOsScheduleTableAppModeRef(self.check_reference_path(name, path, index))
                else:
                    self.logger.debug("Ignore non-standard OsScheduleTableAutostart reference %s" % name)

        for sync in sub_containers.get("OsScheduleTableSync", []):
            for name, raw in self.iter_parameters(sync):
                if name == "OsScheduleTblSyncStrategy":
                    schedule_table.setOsScheduleTableSyncStrategy(self.get_str(name, raw))
                elif name == "OsScheduleTblExplicitPrecision":
                    schedule_table.setOsScheduleTableExplicitPrecision(self.get_int(name, raw))
                else:
                    self.logger.debug("Ignore non-standard OsScheduleTableSync parameter %s" % name)

        for expiry_container in sub_containers.get("OsScheduleTableExpiryPoint", []):
            expiry_point = OsScheduleTableExpiryPoint()
            for name, raw in self.iter_parameters(expiry_container):
                if name == "OsScheduleTblExpPointOffset":
                    expiry_point.setOsScheduleTableExpiryPointOffset(self.get_int(name, raw))
                elif name == "OsScheduleTableMaxShorten":
                    expiry_point.setOsScheduleTableMaxShorten(self.get_int(name, raw))
                elif name == "OsScheduleTableMaxLengthen":
                    expiry_point.setOsScheduleTableMaxLengthen(self.get_int(name, raw))
                else:
                    self.logger.debug("Ignore non-standard OsScheduleTableExpiryPoint parameter %s" % name)
            expiry_sub_containers = self.get_sub_containers_by_name(expiry_container)
            for task_activation in expiry_sub_containers.get("OsScheduleTableTaskActivation", []):
                for name, path in self.iter_references(task_activation):
                    if name == "OsScheduleTableActivateTaskRef":
                        expiry_point.setOsScheduleTableActivateTaskRef(self.check_reference_path(name, path, index))
                    else:
                        self.logger.debug("Ignore non-standard OsScheduleTableTaskActivation reference %s" % name)
            for event_setting in expiry_sub_containers.get("OsScheduleTableEventSetting", []):
                for name, path in self.iter_references(event_setting):
                    if name == "OsScheduleTableSetEventTaskRef":
                        expiry_point.setOsScheduleTableSetEventTaskRef(self.check_reference_path(name, path, index))
                    elif name == "OsScheduleTableSetEventRef":
                        expiry_point.setOsScheduleTableSetEventRef(self.check_reference_path(name, path, index))
                    else:
                        self.logger.debug("Ignore non-standard OsScheduleTableEventSetting reference %s" % name)
            schedule_table.addOsScheduleTableExpiryPoint(expiry_point)

    def get_unique(self, target: List[ValueType], value: ValueType) -> None:
        """Append ``value`` to ``target`` only when it is not already present."""
        if value not in target:
            target.append(value)

    def get_lookup_task(self, name: str, path: str, tasks: Dict[str, OsTask], index: Dict[str, Container], warning: bool) -> Optional[OsTask]:
        """Resolve an OS task reference and apply strict or warning handling."""
        if path in tasks:
            return tasks[path]
        info = index.get(path)
        if info is not None:
            message = "Reference %s must target an OsTask container, but %s is a %s" % (name, path, self.get_definition_name(info.getDefinitionRef()))
        else:
            message = "Unresolved standard reference %s -> %s" % (name, path)
        if warning:
            self.logger.warning(message)
        else:
            raise OsEcucConversionError(message)
        return None

    def get_lookup_application(self, name: str, path: str, applications: Dict[str, OsApplication], index: Dict[str, Container], warning: bool) -> Optional[OsApplication]:
        """Resolve an OS-Application reference and apply strict or warning handling."""
        if path in applications:
            return applications[path]
        info = index.get(path)
        if info is not None:
            message = "Reference %s must target an OsApplication container, but %s is a %s" % (name, path, self.get_definition_name(info.getDefinitionRef()))
        else:
            message = "Unresolved standard reference %s -> %s" % (name, path)
        if warning:
            self.logger.warning(message)
        else:
            raise OsEcucConversionError(message)
        return None

    def get_collect_task(self, task: OsTask, container: Container, index: Dict[str, Container], warning: bool) -> None:
        for name, raw in self.iter_parameters(container):
            if name == "OsTaskActivation":
                task.setOsTaskActivation(self.get_int(name, raw))
            elif name == "OsTaskPeriod":
                task.setOsTaskPeriod(self.get_float(name, raw))
            elif name == "OsTaskPriority":
                task.setOsTaskPriority(self.get_int(name, raw))
            elif name == "OsTaskSchedule":
                task.setOsTaskSchedule(self.get_str(name, raw))
            elif name == "OsStacksize":
                task.setOsStacksize(self.get_int(name, raw))
            else:
                self.logger.debug("Ignore non-standard OsTask parameter %s" % name)

        for name, path in self.iter_references(container):
            if name == "OsTaskAccessingApplication":
                continue
            elif name == "OsTaskEventRef":
                task.addOsTaskEventRef(self.check_reference_path(name, path, index))
            elif name == "OsTaskResourceRef":
                task.addOsTaskResourceRef(self.check_reference_path(name, path, index))
            elif name == "OsMemoryMappingCodeLocationRef":
                task.setOsMemoryMappingCodeLocationRef(self.check_reference_path(name, path, index))
            else:
                self.logger.debug("Ignore non-standard OsTask reference %s" % name)

        sub_containers = self.get_sub_containers_by_name(container)
        for autostart in sub_containers.get("OsTaskAutostart", []):
            for name, path in self.iter_references(autostart):
                if name == "OsTaskAppModeRef":
                    task.addOsTaskAppModeRef(self.check_reference_path(name, path, index))
                else:
                    self.logger.debug("Ignore non-standard OsTaskAutostart reference %s" % name)

        for timing_protection in sub_containers.get("OsTaskTimingProtection", []):
            for name, raw in self.iter_parameters(timing_protection):
                if name == "OsTaskAllInterruptLockBudget":
                    task.setOsTaskAllInterruptLockBudget(self.get_float(name, raw))
                elif name == "OsTaskExecutionBudget":
                    task.setOsTaskExecutionBudget(self.get_float(name, raw))
                elif name == "OsTaskOsInterruptLockBudget":
                    task.setOsTaskOsInterruptLockBudget(self.get_float(name, raw))
                elif name == "OsTaskTimeFrame":
                    task.setOsTaskTimeFrame(self.get_float(name, raw))
                else:
                    self.logger.debug("Ignore non-standard OsTaskTimingProtection parameter %s" % name)
            for resource_lock in self.get_sub_containers_by_name(timing_protection).get("OsTaskResourceLock", []):
                for name, raw in self.iter_parameters(resource_lock):
                    if name == "OsTaskResourceLockBudget":
                        budget = self.get_float(name, raw)
                        if budget is not None:
                            task.addOsTaskResourceLockBudget(budget)
                    else:
                        self.logger.debug("Ignore non-standard OsTaskResourceLock parameter %s" % name)
                for name, path in self.iter_references(resource_lock):
                    if name == "OsTaskResourceLockResourceRef":
                        task.addOsTaskResourceLockResourceRef(self.check_reference_path(name, path, index))
                    else:
                        self.logger.debug("Ignore non-standard OsTaskResourceLock reference %s" % name)

    def get_collect_application(self, application: OsApplication, container: Container, index: Dict[str, Container], warning: bool) -> None:
        for name, raw in self.iter_parameters(container):
            if name == "OsTrusted":
                application.setOsTrusted(self.get_bool(name, raw))
            elif name == "OsTrustedApplicationDelayTimingViolationCall":
                application.setOsTrustedApplicationDelayTimingViolationCall(self.get_bool(name, raw))
            elif name == "OsTrustedApplicationWithProtection":
                application.setOsTrustedApplicationWithProtection(self.get_bool(name, raw))
            else:
                self.logger.debug("Ignore non-standard OsApplication parameter %s" % name)

        for name, path in self.iter_references(container):
            if name in ("OsAppTaskRef", "OsRestartTask", "OsTaskAccessingApplication"):
                continue
            elif name == "OsAppAlarmRef":
                application.addOsAppAlarmRef(self.check_reference_path(name, path, index))
            elif name == "OsAppCounterRef":
                application.addOsAppCounterRef(self.check_reference_path(name, path, index))
            elif name == "OsAppEcucPartitionRef":
                application.setOsAppEcucPartitionRef(self.check_reference_path(name, path, index))
            elif name == "OsAppIsrRef":
                application.addOsAppIsrRef(self.check_reference_path(name, path, index))
            elif name == "OsAppScheduleTableRef":
                application.addOsAppScheduleTableRef(self.check_reference_path(name, path, index))
            elif name == "OsMemoryMappingCodeLocationRef":
                application.setOsMemoryMappingCodeLocationRef(self.check_reference_path(name, path, index))
            else:
                self.logger.debug("Ignore non-standard OsApplication reference %s" % name)

        sub_containers = self.get_sub_containers_by_name(container)
        for hooks in sub_containers.get("OsApplicationHooks", []):
            for name, raw in self.iter_parameters(hooks):
                if name == "OsAppStartupHook":
                    application.setOsAppStartupHook(self.get_bool(name, raw))
                elif name == "OsAppErrorHook":
                    application.setOsAppErrorHook(self.get_bool(name, raw))
                elif name == "OsAppShutdownHook":
                    application.setOsAppShutdownHook(self.get_bool(name, raw))
                else:
                    self.logger.debug("Ignore non-standard OsApplicationHooks parameter %s" % name)
        for trusted_function in sub_containers.get("OsTrustedFunction", []):
            for name, raw in self.iter_parameters(trusted_function):
                if name == "OsTrustedFunctionName":
                    value = self.get_str(name, raw)
                    if value is not None:
                        application.addOsTrustedFunctionName(value)
                else:
                    self.logger.debug("Ignore non-standard OsTrustedFunction parameter %s" % name)

    def get_resolve_task_objects(self, task: OsTask, container: Container, applications: Dict[str, OsApplication], index: Dict[str, Container], warning: bool) -> None:
        for name, path in self.iter_references(container):
            if name == "OsTaskAccessingApplication":
                application = self.get_lookup_application(name, path, applications, index, warning)
                if application is not None:
                    self.get_unique(task.osTaskAccessingApplication, application)

    def get_resolve_application_objects(self, application: OsApplication, container: Container, tasks: Dict[str, OsTask], index: Dict[str, Container], warning: bool) -> None:
        for name, path in self.iter_references(container):
            if name == "OsAppTaskRef":
                task = self.get_lookup_task(name, path, tasks, index, warning)
                if task is not None:
                    self.get_unique(application.osAppTaskRef, task)
            elif name == "OsRestartTask":
                task = self.get_lookup_task(name, path, tasks, index, warning)
                if task is not None:
                    application.setOsRestartTask(task)
