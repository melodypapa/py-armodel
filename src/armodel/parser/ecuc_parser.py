import logging
from typing import Dict, List, Optional, Type, TypeVar, Union

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import (
    ConfigReferenceValue,
    Container,
    EcucAbstractReferenceValue,
    EcucModuleConfigurationValues,
    EcucParameterValue,
    ModuleConfiguration,
    ParameterValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.parser.arxml_parser import ARXMLParser

EcucModule = Union[ModuleConfiguration, EcucModuleConfigurationValues]
EcucParameter = Union[ParameterValue, EcucParameterValue]
EcucReference = Union[ConfigReferenceValue, EcucAbstractReferenceValue]
EcucScalar = Optional[Union[bool, float, int, str]]
ValueType = TypeVar("ValueType")


class EcucParser:
    """Common traversal and value extraction helpers for ECUC parsers."""

    conversion_error: Type[Exception] = Exception

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def load(self, path: str, document: Optional[AUTOSAR] = None, warning: bool = False):
        if document is None:
            document = AUTOSAR.getInstance()
            document.clear()
            document.setARRelease("R23-11")
        ARXMLParser().load(str(path), document)
        return self.parseEcuc(document, warning=warning)

    def parseEcuc(self, document: AUTOSAR, warning: bool = False) -> AUTOSAR:
        return document

    def get_modules(self, document: AUTOSAR) -> List[EcucModule]:
        modules: List[EcucModule] = []
        for package in document.getARPackages():
            self.get_collect_modules(package, modules)
        return modules

    def get_module_containers(self, document: AUTOSAR, module_name: Optional[str] = None) -> Dict[str, Container]:
        index: Dict[str, Container] = {}
        for module in self.get_modules(document):
            if module_name is not None and self.get_definition_name(module.getDefinitionRef()) != module_name:
                continue
            for container in module.getContainers():
                index[self.get_path(container)] = container
        return index

    def get_path(self, element: Identifiable) -> str:
        return "/" + element.getFullName().strip("/")

    def get_definition_name(self, definition_ref: Optional[RefType]) -> str:
        if definition_ref is None or definition_ref.getValue() is None:
            return ""
        return definition_ref.getValue().rstrip("/").rsplit("/", 1)[-1]

    def get_raw_value(self, parameter: EcucParameter) -> EcucScalar:
        value = parameter.getValue()
        if value is None:
            return None
        return getattr(value, "value", None)

    def get_sub_name(self, container: Container) -> str:
        name = self.get_definition_name(container.getDefinitionRef())
        return name or container.getShortName()

    def get_parameter_values(self, container: Container) -> List[EcucParameter]:
        return container.getParameterValues()

    def get_reference_values(self, container: Container) -> List[EcucReference]:
        return container.getReferenceValues()

    def get_sub_containers_by_name(self, container: Container) -> Dict[str, List[Container]]:
        result: Dict[str, List[Container]] = {}
        for sub_container in container.getSubContainers():
            result.setdefault(self.get_sub_name(sub_container), []).append(sub_container)
        return result

    def get_collect_modules(self, package: ARPackage, modules: List[EcucModule]) -> None:
        for element in package.getElements():
            if isinstance(element, (ModuleConfiguration, EcucModuleConfigurationValues)):
                modules.append(element)
        for sub_package in package.getARPackages():
            self.get_collect_modules(sub_package, modules)

    def check_reference_path(self, name: str, path: str, index: Dict[str, Container]) -> str:
        if path in index:
            return path
        message = "Unresolved standard reference %s -> %s" % (name, path)
        self.logger.warning(message)
        return path
