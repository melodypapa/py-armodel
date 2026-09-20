import logging
from typing import Dict, List, Optional, Tuple

from armodel.data_models.ecuc import OsApplication, OsOs, OsTask
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import (
    EcucModuleConfigurationValues,
    ModuleConfiguration,
)
from armodel.parser.arxml_parser import ARXMLParser

logger = logging.getLogger("armodel.parser.os_ecuc_parser")


class OsEcucConversionError(Exception):
    pass


class _ContainerInfo:
    def __init__(self, path: str, definition_name: str, container):
        self.path = path
        self.definition_name = definition_name
        self.container = container


def _definitionName(definition_ref) -> str:
    if definition_ref is None or definition_ref.getValue() is None:
        return ""
    return definition_ref.getValue().rstrip("/").rsplit("/", 1)[-1]


def _rawValue(parameter) -> object:
    value = parameter.getValue()
    if value is None:
        return None
    return getattr(value, "value", None)


def _subName(container) -> str:
    name = _definitionName(container.getDefinitionRef())
    if name:
        return name
    return container.getShortName()


def _parameterValues(container) -> List[Tuple[str, object]]:
    return [(_definitionName(parameter.getDefinitionRef()), _rawValue(parameter)) for parameter in container.getParameterValues()]


def _referenceValues(container) -> List[Tuple[str, str]]:
    result = []
    for reference in container.getReferenceValues():
        name = _definitionName(reference.getDefinitionRef())
        value_ref = reference.getValueRef()
        if value_ref is None or value_ref.getValue() is None:
            continue
        result.append((name, value_ref.getValue().strip()))
    return result


def _subContainersByName(container) -> Dict[str, List]:
    result: Dict[str, List] = {}
    for sub_container in container.getSubContainers():
        result.setdefault(_subName(sub_container), []).append(sub_container)
    return result


def _toBool(name: str, raw: object) -> Optional[bool]:
    if raw is None:
        return None
    if isinstance(raw, bool):
        return raw
    raise OsEcucConversionError("Parameter %s expects a boolean value, got %r" % (name, raw))


def _toInt(name: str, raw: object) -> Optional[int]:
    if raw is None:
        return None
    if isinstance(raw, bool):
        raise OsEcucConversionError("Parameter %s expects an integer value, got %r" % (name, raw))
    if isinstance(raw, int):
        return raw
    if isinstance(raw, float) and raw.is_integer():
        return int(raw)
    raise OsEcucConversionError("Parameter %s expects an integer value, got %r" % (name, raw))


def _toFloat(name: str, raw: object) -> Optional[float]:
    if raw is None:
        return None
    if isinstance(raw, bool) or not isinstance(raw, (int, float)):
        raise OsEcucConversionError("Parameter %s expects a float value, got %r" % (name, raw))
    return float(raw)


def _toStr(name: str, raw: object) -> Optional[str]:
    if raw is None:
        return None
    if not isinstance(raw, str):
        raise OsEcucConversionError("Parameter %s expects a string value, got %r" % (name, raw))
    return raw


def _addUnique(target: List, value) -> None:
    if value not in target:
        target.append(value)


class OsEcucParser:
    def __init__(self):
        self.logger = logging.getLogger("OsEcucParser")

    def load(self, path, document=None, warning: bool = False) -> OsOs:
        if document is None:
            document = AUTOSAR.getInstance()
            document.clear()
            document.setARRelease("R23-11")
        ARXMLParser().load(str(path), document)
        return self.parseEcuc(document, warning=warning)

    def parseEcuc(self, document, warning: bool = False) -> OsOs:
        modules: List[Tuple[str, object]] = []
        for package in document.getARPackages():
            self._collectModules(package, "/" + package.getShortName(), modules)

        index: Dict[str, _ContainerInfo] = {}
        os_name = None
        for module_path, module in modules:
            if _definitionName(module.getDefinitionRef()) != "Os":
                continue
            if os_name is None:
                os_name = module.getShortName()
            for container in module.getContainers():
                path = module_path + "/" + container.getShortName()
                index[path] = _ContainerInfo(path, _definitionName(container.getDefinitionRef()), container)

        os_os = OsOs()
        os_os.setName(os_name if os_name is not None else "Os")

        tasks: Dict[str, OsTask] = {}
        applications: Dict[str, OsApplication] = {}
        for path in index:
            info = index[path]
            if info.definition_name == "OsTask":
                task = OsTask()
                task.setName(info.container.getShortName())
                self._collectTask(task, info.container, index, warning)
                tasks[path] = task
                os_os.addOsTask(task)
        for path in index:
            info = index[path]
            if info.definition_name == "OsApplication":
                application = OsApplication()
                application.setName(info.container.getShortName())
                self._collectApplication(application, info.container, index, warning)
                applications[path] = application
                os_os.addOsApplication(application)

        for path in tasks:
            self._resolveTaskObjects(tasks[path], index[path].container, applications, index, warning)
        for path in applications:
            self._resolveApplicationObjects(applications[path], index[path].container, tasks, index, warning)
        return os_os

    def _collectModules(self, package, package_path: str, modules: List[Tuple[str, object]]) -> None:
        for element in package.getElements():
            if isinstance(element, (ModuleConfiguration, EcucModuleConfigurationValues)):
                modules.append((package_path + "/" + element.getShortName(), element))
        for sub_package in package.getARPackages():
            self._collectModules(sub_package, package_path + "/" + sub_package.getShortName(), modules)

    def _checkReferencePath(self, name: str, path: str, index: Dict[str, _ContainerInfo], warning: bool) -> str:
        if path in index:
            return path
        message = "Unresolved standard reference %s -> %s" % (name, path)
        if warning:
            self.logger.warning(message)
        else:
            raise OsEcucConversionError(message)
        return path

    def _lookupTask(self, name: str, path: str, tasks: Dict[str, OsTask], index: Dict[str, _ContainerInfo], warning: bool) -> Optional[OsTask]:
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

    def _lookupApplication(self, name: str, path: str, applications: Dict[str, OsApplication], index: Dict[str, _ContainerInfo], warning: bool) -> Optional[OsApplication]:
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

    def _collectTask(self, task: OsTask, container, index: Dict[str, _ContainerInfo], warning: bool) -> None:
        for name, raw in _parameterValues(container):
            if name == "OsTaskActivation":
                task.setOsTaskActivation(_toInt(name, raw))
            elif name == "OsTaskPeriod":
                task.setOsTaskPeriod(_toFloat(name, raw))
            elif name == "OsTaskPriority":
                task.setOsTaskPriority(_toInt(name, raw))
            elif name == "OsTaskSchedule":
                task.setOsTaskSchedule(_toStr(name, raw))
            elif name == "OsStacksize":
                task.setOsStacksize(_toInt(name, raw))
            else:
                self.logger.debug("Ignore non-standard OsTask parameter %s" % name)

        for name, path in _referenceValues(container):
            if name == "OsTaskAccessingApplication":
                continue
            elif name == "OsTaskEventRef":
                task.addOsTaskEventRef(self._checkReferencePath(name, path, index, warning))
            elif name == "OsTaskResourceRef":
                task.addOsTaskResourceRef(self._checkReferencePath(name, path, index, warning))
            elif name == "OsMemoryMappingCodeLocationRef":
                task.setOsMemoryMappingCodeLocationRef(self._checkReferencePath(name, path, index, warning))
            else:
                self.logger.debug("Ignore non-standard OsTask reference %s" % name)

        sub_containers = _subContainersByName(container)
        for autostart in sub_containers.get("OsTaskAutostart", []):
            for name, path in _referenceValues(autostart):
                if name == "OsTaskAppModeRef":
                    task.addOsTaskAppModeRef(self._checkReferencePath(name, path, index, warning))
                else:
                    self.logger.debug("Ignore non-standard OsTaskAutostart reference %s" % name)

        for timing_protection in sub_containers.get("OsTaskTimingProtection", []):
            for name, raw in _parameterValues(timing_protection):
                if name == "OsTaskAllInterruptLockBudget":
                    task.setOsTaskAllInterruptLockBudget(_toFloat(name, raw))
                elif name == "OsTaskExecutionBudget":
                    task.setOsTaskExecutionBudget(_toFloat(name, raw))
                elif name == "OsTaskOsInterruptLockBudget":
                    task.setOsTaskOsInterruptLockBudget(_toFloat(name, raw))
                elif name == "OsTaskTimeFrame":
                    task.setOsTaskTimeFrame(_toFloat(name, raw))
                else:
                    self.logger.debug("Ignore non-standard OsTaskTimingProtection parameter %s" % name)
            for resource_lock in _subContainersByName(timing_protection).get("OsTaskResourceLock", []):
                for name, raw in _parameterValues(resource_lock):
                    if name == "OsTaskResourceLockBudget":
                        task.addOsTaskResourceLockBudget(_toFloat(name, raw))
                    else:
                        self.logger.debug("Ignore non-standard OsTaskResourceLock parameter %s" % name)
                for name, path in _referenceValues(resource_lock):
                    if name == "OsTaskResourceLockResourceRef":
                        task.addOsTaskResourceLockResourceRef(self._checkReferencePath(name, path, index, warning))
                    else:
                        self.logger.debug("Ignore non-standard OsTaskResourceLock reference %s" % name)

    def _collectApplication(self, application: OsApplication, container, index: Dict[str, _ContainerInfo], warning: bool) -> None:
        for name, raw in _parameterValues(container):
            if name == "OsTrusted":
                application.setOsTrusted(_toBool(name, raw))
            elif name == "OsTrustedApplicationDelayTimingViolationCall":
                application.setOsTrustedApplicationDelayTimingViolationCall(_toBool(name, raw))
            elif name == "OsTrustedApplicationWithProtection":
                application.setOsTrustedApplicationWithProtection(_toBool(name, raw))
            else:
                self.logger.debug("Ignore non-standard OsApplication parameter %s" % name)

        for name, path in _referenceValues(container):
            if name in ("OsAppTaskRef", "OsRestartTask", "OsTaskAccessingApplication"):
                continue
            elif name == "OsAppAlarmRef":
                application.addOsAppAlarmRef(self._checkReferencePath(name, path, index, warning))
            elif name == "OsAppCounterRef":
                application.addOsAppCounterRef(self._checkReferencePath(name, path, index, warning))
            elif name == "OsAppEcucPartitionRef":
                application.setOsAppEcucPartitionRef(self._checkReferencePath(name, path, index, warning))
            elif name == "OsAppIsrRef":
                application.addOsAppIsrRef(self._checkReferencePath(name, path, index, warning))
            elif name == "OsAppScheduleTableRef":
                application.addOsAppScheduleTableRef(self._checkReferencePath(name, path, index, warning))
            elif name == "OsMemoryMappingCodeLocationRef":
                application.setOsMemoryMappingCodeLocationRef(self._checkReferencePath(name, path, index, warning))
            else:
                self.logger.debug("Ignore non-standard OsApplication reference %s" % name)

        sub_containers = _subContainersByName(container)
        for hooks in sub_containers.get("OsApplicationHooks", []):
            for name, raw in _parameterValues(hooks):
                if name == "OsAppStartupHook":
                    application.setOsAppStartupHook(_toBool(name, raw))
                elif name == "OsAppErrorHook":
                    application.setOsAppErrorHook(_toBool(name, raw))
                elif name == "OsAppShutdownHook":
                    application.setOsAppShutdownHook(_toBool(name, raw))
                else:
                    self.logger.debug("Ignore non-standard OsApplicationHooks parameter %s" % name)
        for trusted_function in sub_containers.get("OsTrustedFunction", []):
            for name, raw in _parameterValues(trusted_function):
                if name == "OsTrustedFunctionName":
                    value = _toStr(name, raw)
                    if value is not None:
                        application.addOsTrustedFunctionName(value)
                else:
                    self.logger.debug("Ignore non-standard OsTrustedFunction parameter %s" % name)

    def _resolveTaskObjects(self, task: OsTask, container, applications: Dict[str, OsApplication], index: Dict[str, _ContainerInfo], warning: bool) -> None:
        for name, path in _referenceValues(container):
            if name == "OsTaskAccessingApplication":
                application = self._lookupApplication(name, path, applications, index, warning)
                if application is not None:
                    _addUnique(task.OsTaskAccessingApplication, application)

    def _resolveApplicationObjects(self, application: OsApplication, container, tasks: Dict[str, OsTask], index: Dict[str, _ContainerInfo], warning: bool) -> None:
        for name, path in _referenceValues(container):
            if name == "OsAppTaskRef":
                task = self._lookupTask(name, path, tasks, index, warning)
                if task is not None:
                    _addUnique(application.OsAppTaskRef, task)
            elif name == "OsRestartTask":
                task = self._lookupTask(name, path, tasks, index, warning)
                if task is not None:
                    application.setOsRestartTask(task)
