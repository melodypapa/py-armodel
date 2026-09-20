import logging
from typing import Dict, List, Optional

from armodel.data_models.ecuc import OsApplication, OsOs, OsTask
from armodel.parser.ecuc_parser import EcucParser

logger = logging.getLogger("armodel.parser.os_ecuc_parser")


class OsEcucConversionError(Exception):
    pass


class _ContainerInfo:
    def __init__(self, path: str, definition_name: str, container):
        self.path = path
        self.definition_name = definition_name
        self.container = container


class OsEcucParser(EcucParser):
    container_info_type = _ContainerInfo
    conversion_error = OsEcucConversionError

    def __init__(self):
        super().__init__()

    def load(self, path, document=None, warning: bool = False) -> OsOs:
        return super().load(path, document=document, warning=warning)

    def parseEcuc(self, document, warning: bool = False) -> OsOs:
        modules = self.get_modules(document)
        index: Dict[str, _ContainerInfo] = self.get_module_containers(document, module_name="Os")
        os_name = None
        for module_path, module in modules:
            if self.get_definition_name(module.getDefinitionRef()) != "Os":
                continue
            if os_name is None:
                os_name = module.getShortName()

        os_os = OsOs()
        os_os.setName(os_name if os_name is not None else "Os")

        tasks: Dict[str, OsTask] = {}
        applications: Dict[str, OsApplication] = {}
        for path in index:
            info = index[path]
            if info.definition_name == "OsTask":
                task = OsTask()
                task.setName(info.container.getShortName())
                self.get_collect_task(task, info.container, index, warning)
                tasks[path] = task
                os_os.addOsTask(task)
        for path in index:
            info = index[path]
            if info.definition_name == "OsApplication":
                application = OsApplication()
                application.setName(info.container.getShortName())
                self.get_collect_application(application, info.container, index, warning)
                applications[path] = application
                os_os.addOsApplication(application)

        for path in tasks:
            self.get_resolve_task_objects(tasks[path], index[path].container, applications, index, warning)
        for path in applications:
            self.get_resolve_application_objects(applications[path], index[path].container, tasks, index, warning)
        return os_os

    def get_bool(self, name: str, raw: object) -> Optional[bool]:
        if raw is None:
            return None
        if isinstance(raw, bool):
            return raw
        if isinstance(raw, str) and raw.lower() in ("true", "false", "0", "1"):
            return raw.lower() in ("true", "1")
        raise OsEcucConversionError("Parameter %s expects a boolean value, got %r" % (name, raw))

    def get_int(self, name: str, raw: object) -> Optional[int]:
        if raw is None:
            return None
        if isinstance(raw, bool):
            raise OsEcucConversionError("Parameter %s expects an integer value, got %r" % (name, raw))
        if isinstance(raw, int):
            return raw
        if isinstance(raw, float) and raw.is_integer():
            return int(raw)
        if isinstance(raw, str):
            try:
                return int(raw, 0)
            except ValueError:
                pass
        raise OsEcucConversionError("Parameter %s expects an integer value, got %r" % (name, raw))

    def get_float(self, name: str, raw: object) -> Optional[float]:
        if raw is None:
            return None
        if isinstance(raw, str):
            try:
                return float(raw)
            except ValueError:
                raise OsEcucConversionError("Parameter %s expects a float value, got %r" % (name, raw))
        if isinstance(raw, bool) or not isinstance(raw, (int, float)):
            raise OsEcucConversionError("Parameter %s expects a float value, got %r" % (name, raw))
        return float(raw)

    def get_str(self, name: str, raw: object) -> Optional[str]:
        if raw is None:
            return None
        if not isinstance(raw, str):
            raise OsEcucConversionError("Parameter %s expects a string value, got %r" % (name, raw))
        return raw

    def get_unique(self, target: List, value) -> None:
        if value not in target:
            target.append(value)

    def get_lookup_task(self, name: str, path: str, tasks: Dict[str, OsTask], index: Dict[str, _ContainerInfo], warning: bool) -> Optional[OsTask]:
        if path in tasks:
            return tasks[path]
        info = index.get(path)
        if info is not None:
            message = "Reference %s must target an OsTask container, but %s is a %s" % (name, path, info.definition_name)
        else:
            message = "Unresolved standard reference %s -> %s" % (name, path)
        if warning:
            self.logger.warning(message)
        else:
            raise OsEcucConversionError(message)
        return None

    def get_lookup_application(self, name: str, path: str, applications: Dict[str, OsApplication], index: Dict[str, _ContainerInfo], warning: bool) -> Optional[OsApplication]:
        if path in applications:
            return applications[path]
        info = index.get(path)
        if info is not None:
            message = "Reference %s must target an OsApplication container, but %s is a %s" % (name, path, info.definition_name)
        else:
            message = "Unresolved standard reference %s -> %s" % (name, path)
        if warning:
            self.logger.warning(message)
        else:
            raise OsEcucConversionError(message)
        return None

    def get_collect_task(self, task: OsTask, container, index: Dict[str, _ContainerInfo], warning: bool) -> None:
        for name, raw in self.get_parameter_values(container):
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

        for name, path in self.get_reference_values(container):
            if name == "OsTaskAccessingApplication":
                continue
            elif name == "OsTaskEventRef":
                task.addOsTaskEventRef(self.get_check_reference_path(name, path, index, warning))
            elif name == "OsTaskResourceRef":
                task.addOsTaskResourceRef(self.get_check_reference_path(name, path, index, warning))
            elif name == "OsMemoryMappingCodeLocationRef":
                task.setOsMemoryMappingCodeLocationRef(self.get_check_reference_path(name, path, index, warning))
            else:
                self.logger.debug("Ignore non-standard OsTask reference %s" % name)

        sub_containers = self.get_sub_containers_by_name(container)
        for autostart in sub_containers.get("OsTaskAutostart", []):
            for name, path in self.get_reference_values(autostart):
                if name == "OsTaskAppModeRef":
                    task.addOsTaskAppModeRef(self.get_check_reference_path(name, path, index, warning))
                else:
                    self.logger.debug("Ignore non-standard OsTaskAutostart reference %s" % name)

        for timing_protection in sub_containers.get("OsTaskTimingProtection", []):
            for name, raw in self.get_parameter_values(timing_protection):
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
                for name, raw in self.get_parameter_values(resource_lock):
                    if name == "OsTaskResourceLockBudget":
                        task.addOsTaskResourceLockBudget(self.get_float(name, raw))
                    else:
                        self.logger.debug("Ignore non-standard OsTaskResourceLock parameter %s" % name)
                for name, path in self.get_reference_values(resource_lock):
                    if name == "OsTaskResourceLockResourceRef":
                        task.addOsTaskResourceLockResourceRef(self.get_check_reference_path(name, path, index, warning))
                    else:
                        self.logger.debug("Ignore non-standard OsTaskResourceLock reference %s" % name)

    def get_collect_application(self, application: OsApplication, container, index: Dict[str, _ContainerInfo], warning: bool) -> None:
        for name, raw in self.get_parameter_values(container):
            if name == "OsTrusted":
                application.setOsTrusted(self.get_bool(name, raw))
            elif name == "OsTrustedApplicationDelayTimingViolationCall":
                application.setOsTrustedApplicationDelayTimingViolationCall(self.get_bool(name, raw))
            elif name == "OsTrustedApplicationWithProtection":
                application.setOsTrustedApplicationWithProtection(self.get_bool(name, raw))
            else:
                self.logger.debug("Ignore non-standard OsApplication parameter %s" % name)

        for name, path in self.get_reference_values(container):
            if name in ("OsAppTaskRef", "OsRestartTask", "OsTaskAccessingApplication"):
                continue
            elif name == "OsAppAlarmRef":
                application.addOsAppAlarmRef(self.get_check_reference_path(name, path, index, warning))
            elif name == "OsAppCounterRef":
                application.addOsAppCounterRef(self.get_check_reference_path(name, path, index, warning))
            elif name == "OsAppEcucPartitionRef":
                application.setOsAppEcucPartitionRef(self.get_check_reference_path(name, path, index, warning))
            elif name == "OsAppIsrRef":
                application.addOsAppIsrRef(self.get_check_reference_path(name, path, index, warning))
            elif name == "OsAppScheduleTableRef":
                application.addOsAppScheduleTableRef(self.get_check_reference_path(name, path, index, warning))
            elif name == "OsMemoryMappingCodeLocationRef":
                application.setOsMemoryMappingCodeLocationRef(self.get_check_reference_path(name, path, index, warning))
            else:
                self.logger.debug("Ignore non-standard OsApplication reference %s" % name)

        sub_containers = self.get_sub_containers_by_name(container)
        for hooks in sub_containers.get("OsApplicationHooks", []):
            for name, raw in self.get_parameter_values(hooks):
                if name == "OsAppStartupHook":
                    application.setOsAppStartupHook(self.get_bool(name, raw))
                elif name == "OsAppErrorHook":
                    application.setOsAppErrorHook(self.get_bool(name, raw))
                elif name == "OsAppShutdownHook":
                    application.setOsAppShutdownHook(self.get_bool(name, raw))
                else:
                    self.logger.debug("Ignore non-standard OsApplicationHooks parameter %s" % name)
        for trusted_function in sub_containers.get("OsTrustedFunction", []):
            for name, raw in self.get_parameter_values(trusted_function):
                if name == "OsTrustedFunctionName":
                    value = self.get_str(name, raw)
                    if value is not None:
                        application.addOsTrustedFunctionName(value)
                else:
                    self.logger.debug("Ignore non-standard OsTrustedFunction parameter %s" % name)

    def get_resolve_task_objects(self, task: OsTask, container, applications: Dict[str, OsApplication], index: Dict[str, _ContainerInfo], warning: bool) -> None:
        for name, path in self.get_reference_values(container):
            if name == "OsTaskAccessingApplication":
                application = self.get_lookup_application(name, path, applications, index, warning)
                if application is not None:
                    self.get_unique(task.osTaskAccessingApplication, application)

    def get_resolve_application_objects(self, application: OsApplication, container, tasks: Dict[str, OsTask], index: Dict[str, _ContainerInfo], warning: bool) -> None:
        for name, path in self.get_reference_values(container):
            if name == "OsAppTaskRef":
                task = self.get_lookup_task(name, path, tasks, index, warning)
                if task is not None:
                    self.get_unique(application.osAppTaskRef, task)
            elif name == "OsRestartTask":
                task = self.get_lookup_task(name, path, tasks, index, warning)
                if task is not None:
                    application.setOsRestartTask(task)
