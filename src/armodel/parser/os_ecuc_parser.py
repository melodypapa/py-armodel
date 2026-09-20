import logging
from typing import Dict, List, Optional, TypeVar

from armodel.data_models.ecuc import OsAlarm, OsApplication, OsIsr, OsOs, OsTask
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import Container
from armodel.parser.ecuc_parser import EcucParser, EcucScalar

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
        return os_os

    def get_collect_alarm(self, alarm: OsAlarm, container: Container, index: Dict[str, Container], warning: bool) -> None:
        for parameter in self.get_parameter_values(container):
            name = self.get_definition_name(parameter.getDefinitionRef())
            raw = self.get_raw_value(parameter)
            if name == "OsAlarmCallbackName":
                alarm.setOsAlarmCallbackName(self.get_str(name, raw))
            else:
                self.logger.debug("Ignore non-standard OsAlarm parameter %s" % name)

        for reference in self.get_reference_values(container):
            name = self.get_definition_name(reference.getDefinitionRef())
            value_ref = reference.getValueRef()
            if value_ref is None or value_ref.getValue() is None:
                continue
            path = value_ref.getValue().strip()
            if name == "OsAlarmCounterRef":
                alarm.setOsAlarmCounterRef(self.get_check_reference_path(name, path, index, warning))
            elif name == "OsAlarmAccessingApplication":
                alarm.addOsAlarmAccessingApplication(self.get_check_reference_path(name, path, index, warning))
            else:
                self.logger.debug("Ignore non-standard OsAlarm reference %s" % name)

        sub_containers = self.get_sub_containers_by_name(container)
        for autostart in sub_containers.get("OsAlarmAutostart", []):
            for parameter in self.get_parameter_values(autostart):
                name = self.get_definition_name(parameter.getDefinitionRef())
                raw = self.get_raw_value(parameter)
                if name == "OsAlarmAlarmTime":
                    alarm.setOsAlarmAlarmTime(self.get_int(name, raw))
                elif name == "OsAlarmAutostartType":
                    alarm.setOsAlarmAutostartType(self.get_str(name, raw))
                elif name == "OsAlarmCycleTime":
                    alarm.setOsAlarmCycleTime(self.get_int(name, raw))
                else:
                    self.logger.debug("Ignore non-standard OsAlarmAutostart parameter %s" % name)
            for reference in self.get_reference_values(autostart):
                name = self.get_definition_name(reference.getDefinitionRef())
                value_ref = reference.getValueRef()
                if value_ref is None or value_ref.getValue() is None:
                    continue
                path = value_ref.getValue().strip()
                if name == "OsAlarmAppModeRef":
                    alarm.setOsAlarmAppModeRef(self.get_check_reference_path(name, path, index, warning))
                else:
                    self.logger.debug("Ignore non-standard OsAlarmAutostart reference %s" % name)

        action_containers = []
        for choice in ("OsAlarmActivateTask", "OsAlarmCallback", "OsAlarmIncrementCounter", "OsAlarmSetEvent"):
            action_containers.extend(sub_containers.get(choice, []))
        for action in action_containers:
            for reference in self.get_reference_values(action):
                name = self.get_definition_name(reference.getDefinitionRef())
                value_ref = reference.getValueRef()
                if value_ref is None or value_ref.getValue() is None:
                    continue
                path = value_ref.getValue().strip()
                if name == "OsAlarmActivateTaskRef":
                    alarm.setOsAlarmActivateTaskRef(self.get_check_reference_path(name, path, index, warning))
                elif name == "OsAlarmSetEventTaskRef":
                    alarm.setOsAlarmSetEventTaskRef(self.get_check_reference_path(name, path, index, warning))
                elif name == "OsAlarmSetEventRef":
                    alarm.setOsAlarmSetEventRef(self.get_check_reference_path(name, path, index, warning))
                elif name == "OsAlarmIncrementCounterRef":
                    alarm.setOsAlarmIncrementCounterRef(self.get_check_reference_path(name, path, index, warning))
                else:
                    self.logger.debug("Ignore non-standard OsAlarmAction reference %s" % name)
            for parameter in self.get_parameter_values(action):
                name = self.get_definition_name(parameter.getDefinitionRef())
                raw = self.get_raw_value(parameter)
                if name == "OsAlarmCallbackName":
                    alarm.setOsAlarmCallbackName(self.get_str(name, raw))
                else:
                    self.logger.debug("Ignore non-standard OsAlarmAction parameter %s" % name)

    def get_collect_isr(self, isr: OsIsr, container: Container, index: Dict[str, Container], warning: bool) -> None:
        for parameter in self.get_parameter_values(container):
            name = self.get_definition_name(parameter.getDefinitionRef())
            raw = self.get_raw_value(parameter)
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

        for reference in self.get_reference_values(container):
            name = self.get_definition_name(reference.getDefinitionRef())
            value_ref = reference.getValueRef()
            if value_ref is None or value_ref.getValue() is None:
                continue
            path = value_ref.getValue().strip()
            if name == "OsIsrResourceRef":
                isr.setOsIsrResourceRef(self.get_check_reference_path(name, path, index, warning))
            elif name == "OsIsrInterruptSource":
                isr.setOsIsrInterruptSource(self.get_check_reference_path(name, path, index, warning))
            elif name == "OsIsrAccessingApplication":
                isr.addOsIsrAccessingApplication(self.get_check_reference_path(name, path, index, warning))
            elif name == "OsMemoryMappingCodeLocationRef":
                isr.setOsMemoryMappingCodeLocationRef(self.get_check_reference_path(name, path, index, warning))
            else:
                self.logger.debug("Ignore non-standard OsIsr reference %s" % name)

        sub_containers = self.get_sub_containers_by_name(container)
        for timing_protection in sub_containers.get("OsIsrTimingProtection", []):
            for parameter in self.get_parameter_values(timing_protection):
                name = self.get_definition_name(parameter.getDefinitionRef())
                raw = self.get_raw_value(parameter)
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
                for parameter in self.get_parameter_values(resource_lock):
                    name = self.get_definition_name(parameter.getDefinitionRef())
                    raw = self.get_raw_value(parameter)
                    if name == "OsIsrResourceLockBudget":
                        isr.addOsIsrResourceLockBudget(self.get_float(name, raw))
                    else:
                        self.logger.debug("Ignore non-standard OsIsrResourceLock parameter %s" % name)
                for reference in self.get_reference_values(resource_lock):
                    name = self.get_definition_name(reference.getDefinitionRef())
                    value_ref = reference.getValueRef()
                    if value_ref is None or value_ref.getValue() is None:
                        continue
                    path = value_ref.getValue().strip()
                    if name == "OsIsrResourceLockResourceRef":
                        isr.addOsIsrResourceLockResourceRef(self.get_check_reference_path(name, path, index, warning))
                    else:
                        self.logger.debug("Ignore non-standard OsIsrResourceLock reference %s" % name)

    def get_bool(self, name: str, raw: EcucScalar) -> Optional[bool]:
        """Convert an ECUC scalar to a boolean OS parameter value.

        Boolean values accept native booleans and the strings ``true``,
        ``false``, ``1``, and ``0``. ``None`` is preserved for optional
        parameters; invalid values raise :class:`OsEcucConversionError`.
        """
        if raw is None:
            return None
        if isinstance(raw, bool):
            return raw
        if isinstance(raw, str) and raw.lower() in ("true", "false", "0", "1"):
            return raw.lower() in ("true", "1")
        raise OsEcucConversionError("Parameter %s expects a boolean value, got %r" % (name, raw))

    def get_int(self, name: str, raw: EcucScalar) -> Optional[int]:
        """Convert an ECUC scalar to an integer OS parameter value.

        Native integers, integral floats, and strings accepted by
        ``int(value, 0)`` are supported. ``None`` is preserved for optional
        parameters; booleans and invalid values raise
        :class:`OsEcucConversionError`.
        """
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

    def get_float(self, name: str, raw: EcucScalar) -> Optional[float]:
        """Convert an ECUC scalar to a floating-point OS parameter value.

        Numeric values and numeric strings are accepted. ``None`` is
        preserved for optional parameters; booleans and invalid values raise
        :class:`OsEcucConversionError`.
        """
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

    def get_str(self, name: str, raw: EcucScalar) -> Optional[str]:
        """Validate and return a string-valued OS parameter.

        ``None`` is preserved for optional parameters. Non-string values
        raise :class:`OsEcucConversionError`.
        """
        if raw is None:
            return None
        if not isinstance(raw, str):
            raise OsEcucConversionError("Parameter %s expects a string value, got %r" % (name, raw))
        return raw

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
        for parameter in self.get_parameter_values(container):
            name = self.get_definition_name(parameter.getDefinitionRef())
            raw = self.get_raw_value(parameter)
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

        for reference in self.get_reference_values(container):
            name = self.get_definition_name(reference.getDefinitionRef())
            value_ref = reference.getValueRef()
            if value_ref is None or value_ref.getValue() is None:
                continue
            path = value_ref.getValue().strip()
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
            for reference in self.get_reference_values(autostart):
                name = self.get_definition_name(reference.getDefinitionRef())
                value_ref = reference.getValueRef()
                if value_ref is None or value_ref.getValue() is None:
                    continue
                path = value_ref.getValue().strip()
                if name == "OsTaskAppModeRef":
                    task.addOsTaskAppModeRef(self.get_check_reference_path(name, path, index, warning))
                else:
                    self.logger.debug("Ignore non-standard OsTaskAutostart reference %s" % name)

        for timing_protection in sub_containers.get("OsTaskTimingProtection", []):
            for parameter in self.get_parameter_values(timing_protection):
                name = self.get_definition_name(parameter.getDefinitionRef())
                raw = self.get_raw_value(parameter)
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
                for parameter in self.get_parameter_values(resource_lock):
                    name = self.get_definition_name(parameter.getDefinitionRef())
                    raw = self.get_raw_value(parameter)
                    if name == "OsTaskResourceLockBudget":
                        task.addOsTaskResourceLockBudget(self.get_float(name, raw))
                    else:
                        self.logger.debug("Ignore non-standard OsTaskResourceLock parameter %s" % name)
                for reference in self.get_reference_values(resource_lock):
                    name = self.get_definition_name(reference.getDefinitionRef())
                    value_ref = reference.getValueRef()
                    if value_ref is None or value_ref.getValue() is None:
                        continue
                    path = value_ref.getValue().strip()
                    if name == "OsTaskResourceLockResourceRef":
                        task.addOsTaskResourceLockResourceRef(self.get_check_reference_path(name, path, index, warning))
                    else:
                        self.logger.debug("Ignore non-standard OsTaskResourceLock reference %s" % name)

    def get_collect_application(self, application: OsApplication, container: Container, index: Dict[str, Container], warning: bool) -> None:
        for parameter in self.get_parameter_values(container):
            name = self.get_definition_name(parameter.getDefinitionRef())
            raw = self.get_raw_value(parameter)
            if name == "OsTrusted":
                application.setOsTrusted(self.get_bool(name, raw))
            elif name == "OsTrustedApplicationDelayTimingViolationCall":
                application.setOsTrustedApplicationDelayTimingViolationCall(self.get_bool(name, raw))
            elif name == "OsTrustedApplicationWithProtection":
                application.setOsTrustedApplicationWithProtection(self.get_bool(name, raw))
            else:
                self.logger.debug("Ignore non-standard OsApplication parameter %s" % name)

        for reference in self.get_reference_values(container):
            name = self.get_definition_name(reference.getDefinitionRef())
            value_ref = reference.getValueRef()
            if value_ref is None or value_ref.getValue() is None:
                continue
            path = value_ref.getValue().strip()
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
            for parameter in self.get_parameter_values(hooks):
                name = self.get_definition_name(parameter.getDefinitionRef())
                raw = self.get_raw_value(parameter)
                if name == "OsAppStartupHook":
                    application.setOsAppStartupHook(self.get_bool(name, raw))
                elif name == "OsAppErrorHook":
                    application.setOsAppErrorHook(self.get_bool(name, raw))
                elif name == "OsAppShutdownHook":
                    application.setOsAppShutdownHook(self.get_bool(name, raw))
                else:
                    self.logger.debug("Ignore non-standard OsApplicationHooks parameter %s" % name)
        for trusted_function in sub_containers.get("OsTrustedFunction", []):
            for parameter in self.get_parameter_values(trusted_function):
                name = self.get_definition_name(parameter.getDefinitionRef())
                raw = self.get_raw_value(parameter)
                if name == "OsTrustedFunctionName":
                    value = self.get_str(name, raw)
                    if value is not None:
                        application.addOsTrustedFunctionName(value)
                else:
                    self.logger.debug("Ignore non-standard OsTrustedFunction parameter %s" % name)

    def get_resolve_task_objects(self, task: OsTask, container: Container, applications: Dict[str, OsApplication], index: Dict[str, Container], warning: bool) -> None:
        for reference in self.get_reference_values(container):
            name = self.get_definition_name(reference.getDefinitionRef())
            value_ref = reference.getValueRef()
            if value_ref is None or value_ref.getValue() is None:
                continue
            path = value_ref.getValue().strip()
            if name == "OsTaskAccessingApplication":
                application = self.get_lookup_application(name, path, applications, index, warning)
                if application is not None:
                    self.get_unique(task.osTaskAccessingApplication, application)

    def get_resolve_application_objects(self, application: OsApplication, container: Container, tasks: Dict[str, OsTask], index: Dict[str, Container], warning: bool) -> None:
        for reference in self.get_reference_values(container):
            name = self.get_definition_name(reference.getDefinitionRef())
            value_ref = reference.getValueRef()
            if value_ref is None or value_ref.getValue() is None:
                continue
            path = value_ref.getValue().strip()
            if name == "OsAppTaskRef":
                task = self.get_lookup_task(name, path, tasks, index, warning)
                if task is not None:
                    self.get_unique(application.osAppTaskRef, task)
            elif name == "OsRestartTask":
                task = self.get_lookup_task(name, path, tasks, index, warning)
                if task is not None:
                    application.setOsRestartTask(task)
