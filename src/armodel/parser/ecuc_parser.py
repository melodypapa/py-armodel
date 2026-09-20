import logging
from typing import Dict, List, Optional, Tuple

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import (
    EcucModuleConfigurationValues,
    ModuleConfiguration,
)
from armodel.parser.arxml_parser import ARXMLParser


class EcucParser:
    """Common traversal and value extraction helpers for ECUC parsers."""

    container_info_type = None
    conversion_error = Exception

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def load(self, path, document=None, warning: bool = False):
        if document is None:
            document = AUTOSAR.getInstance()
            document.clear()
            document.setARRelease("R23-11")
        ARXMLParser().load(str(path), document)
        return self.parseEcuc(document, warning=warning)

    def parseEcuc(self, document, warning: bool = False):
        return document

    def get_modules(self, document) -> List[Tuple[str, object]]:
        modules: List[Tuple[str, object]] = []
        for package in document.getARPackages():
            self.get_collect_modules(package, "/" + package.getShortName(), modules)
        return modules

    def get_module_containers(self, document, module_name: Optional[str] = None) -> Dict[str, object]:
        index = {}
        for module_path, module in self.get_modules(document):
            if module_name is not None and self.get_definition_name(module.getDefinitionRef()) != module_name:
                continue
            for container in module.getContainers():
                path = module_path + "/" + container.getShortName()
                index[path] = self._make_container_info(path, container)
        return index

    def _make_container_info(self, path: str, container) -> object:
        info_type = self.container_info_type
        if info_type is None:
            return container
        return info_type(path, self.get_definition_name(container.getDefinitionRef()), container)

    def get_definition_name(self, definition_ref) -> str:
        if definition_ref is None or definition_ref.getValue() is None:
            return ""
        return definition_ref.getValue().rstrip("/").rsplit("/", 1)[-1]

    def get_raw_value(self, parameter) -> object:
        value = parameter.getValue()
        if value is None:
            return None
        return getattr(value, "value", None)

    def get_sub_name(self, container) -> str:
        name = self.get_definition_name(container.getDefinitionRef())
        return name or container.getShortName()

    def get_parameter_values(self, container) -> List[Tuple[str, object]]:
        return [(self.get_definition_name(parameter.getDefinitionRef()), self.get_raw_value(parameter)) for parameter in container.getParameterValues()]

    def get_reference_values(self, container) -> List[Tuple[str, str]]:
        result = []
        for reference in container.getReferenceValues():
            name = self.get_definition_name(reference.getDefinitionRef())
            value_ref = reference.getValueRef()
            if value_ref is not None and value_ref.getValue() is not None:
                result.append((name, value_ref.getValue().strip()))
        return result

    def get_sub_containers_by_name(self, container) -> Dict[str, List]:
        result: Dict[str, List] = {}
        for sub_container in container.getSubContainers():
            result.setdefault(self.get_sub_name(sub_container), []).append(sub_container)
        return result

    def get_collect_modules(self, package, package_path: str, modules: List[Tuple[str, object]]) -> None:
        for element in package.getElements():
            if isinstance(element, (ModuleConfiguration, EcucModuleConfigurationValues)):
                modules.append((package_path + "/" + element.getShortName(), element))
        for sub_package in package.getARPackages():
            self.get_collect_modules(sub_package, package_path + "/" + sub_package.getShortName(), modules)

    def get_check_reference_path(self, name: str, path: str, index: Dict[str, object], warning: bool) -> str:
        if path in index:
            return path
        message = "Unresolved standard reference %s -> %s" % (name, path)
        if warning:
            self.logger.warning(message)
        else:
            raise self.conversion_error(message)
        return path
