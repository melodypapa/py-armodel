import logging
from typing import Any, Dict, List, Optional, Tuple, Type, TypeVar, Union, cast

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

    def parseEcuc(self, document: AUTOSAR, warning: bool = False) -> Any:
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
                index[self.get_path(container)] = cast(Container, container)
        return index

    def get_path(self, element: Identifiable) -> str:
        return "/" + element.getFullName().strip("/")

    def get_definition_name(self, definition_ref: Optional[RefType]) -> str:
        if definition_ref is None:
            return ""
        value = definition_ref.getValue()
        if value is None:
            return ""
        return value.rstrip("/").rsplit("/", 1)[-1]

    def get_raw_value(self, parameter: EcucParameter) -> EcucScalar:
        getter = getattr(parameter, "getValue", None)
        value = getter() if callable(getter) else None
        if value is None:
            return None
        return getattr(value, "value", None)

    def get_sub_name(self, container: Container) -> str:
        name = self.get_definition_name(container.getDefinitionRef())
        return name or container.getShortName()

    def get_parameter_values(self, container: Container) -> List[EcucParameter]:
        return cast(List[EcucParameter], container.getParameterValues())

    def get_reference_values(self, container: Container) -> List[EcucReference]:
        return cast(List[EcucReference], container.getReferenceValues())

    def get_reference_value_ref(self, reference: EcucReference) -> Optional[RefType]:
        getter = getattr(reference, "getValueRef", None)
        if callable(getter):
            return getter()
        instance_getter = getattr(reference, "getValueIRef", None)
        instance = instance_getter() if callable(instance_getter) else None
        return instance.getTargetRef() if instance is not None else None

    def get_sub_containers_by_name(self, container: Container) -> Dict[str, List[Container]]:
        result: Dict[str, List[Container]] = {}
        for sub_container in container.getSubContainers():
            result.setdefault(self.get_sub_name(sub_container), []).append(sub_container)
        return result

    def get_collect_modules(self, package: ARPackage, modules: List[EcucModule]) -> None:
        for element in package.getReferrableElements():
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

    def get_all_containers(self, document: AUTOSAR, module_name: Optional[str] = None) -> Dict[str, Container]:
        """Index every container of the module, sub-containers included, by absolute path."""
        index: Dict[str, Container] = {}
        for container in self.get_module_containers(document, module_name=module_name).values():
            self.get_collect_containers(container, index)
        return index

    def get_collect_containers(self, container: Container, index: Dict[str, Container]) -> None:
        index[self.get_path(container)] = container
        for sub_container in container.getSubContainers():
            self.get_collect_containers(sub_container, index)

    def get_containers_by_definition(self, index: Dict[str, Container], definition_name: str) -> List[Container]:
        return [container for container in index.values() if self.get_definition_name(container.getDefinitionRef()) == definition_name]

    def get_module_short_name(self, document: AUTOSAR, module_name: str) -> Optional[str]:
        for module in self.get_modules(document):
            if self.get_definition_name(module.getDefinitionRef()) == module_name:
                return module.getShortName()
        return None

    def iter_parameters(self, container: Container) -> List[Tuple[str, EcucScalar]]:
        """Return (definition short name, raw scalar) for every parameter value of the container."""
        return [(self.get_definition_name(parameter.getDefinitionRef()), self.get_raw_value(parameter)) for parameter in self.get_parameter_values(container)]

    def iter_references(self, container: Container) -> List[Tuple[str, str]]:
        """Return (definition short name, stripped target path) for every reference value that has a target."""
        result: List[Tuple[str, str]] = []
        for reference in self.get_reference_values(container):
            value_ref = self.get_reference_value_ref(reference)
            if value_ref is None:
                continue
            path = value_ref.getValue()
            if path is None:
                continue
            result.append((self.get_definition_name(reference.getDefinitionRef()), path.strip()))
        return result

    def get_typed_value(self, parameter: EcucParameter) -> EcucScalar:
        """Convert a parameter value using the DEST of its DEFINITION-REF (boolean/integer/float), else keep the raw value."""
        name = self.get_definition_name(parameter.getDefinitionRef())
        raw = self.get_raw_value(parameter)
        definition_ref = parameter.getDefinitionRef()
        dest = definition_ref.getDest() if definition_ref is not None else None
        if dest == "ECUC-BOOLEAN-PARAM-DEF":
            return self.get_bool(name, raw)
        if dest == "ECUC-INTEGER-PARAM-DEF":
            return self.get_int(name, raw)
        if dest == "ECUC-FLOAT-PARAM-DEF":
            return self.get_float(name, raw)
        return raw

    def get_bool(self, name: str, raw: EcucScalar) -> Optional[bool]:
        """Convert an ECUC scalar to a boolean.

        Accepts native booleans, ``true``/``false``, and the numbers 0/1 as
        numbers or numeric strings (``"1"``, ``"0.0"``). ``None`` is preserved;
        anything else raises :attr:`conversion_error`.
        """
        if raw is None:
            return None
        if isinstance(raw, bool):
            return raw
        value: Union[float, int, str] = raw
        if isinstance(value, str):
            text = value.strip().lower()
            if text in ("true", "false"):
                return text == "true"
            try:
                value = float(text)
            except ValueError:
                raise self.conversion_error("Parameter %s expects a boolean value, got %r" % (name, raw))
        if value in (0, 1):
            return bool(value)
        raise self.conversion_error("Parameter %s expects a boolean value, got %r" % (name, raw))

    def get_int(self, name: str, raw: EcucScalar) -> Optional[int]:
        """Convert an ECUC scalar to an integer.

        Accepts integers, integral floats, strings accepted by ``int(value, 0)``
        and integral numeric strings such as ``"10.0"``. ``None`` is preserved;
        booleans and anything else raise :attr:`conversion_error`.
        """
        if raw is None:
            return None
        if isinstance(raw, bool):
            raise self.conversion_error("Parameter %s expects an integer value, got %r" % (name, raw))
        if isinstance(raw, int):
            return raw
        value: Union[float, str] = raw
        if isinstance(value, str):
            try:
                return int(value.strip(), 0)
            except ValueError:
                try:
                    value = float(value)
                except ValueError:
                    raise self.conversion_error("Parameter %s expects an integer value, got %r" % (name, raw))
        if value.is_integer():
            return int(value)
        raise self.conversion_error("Parameter %s expects an integer value, got %r" % (name, raw))

    def get_float(self, name: str, raw: EcucScalar) -> Optional[float]:
        """Convert an ECUC scalar to a float; ``None`` is preserved, booleans and non-numeric values raise :attr:`conversion_error`."""
        if raw is None:
            return None
        if isinstance(raw, str):
            try:
                return float(raw)
            except ValueError:
                raise self.conversion_error("Parameter %s expects a float value, got %r" % (name, raw))
        if isinstance(raw, bool) or not isinstance(raw, (int, float)):
            raise self.conversion_error("Parameter %s expects a float value, got %r" % (name, raw))
        return float(raw)

    def get_str(self, name: str, raw: EcucScalar) -> Optional[str]:
        """Return a string-valued parameter; ``None`` is preserved, non-strings raise :attr:`conversion_error`."""
        if raw is None:
            return None
        if not isinstance(raw, str):
            raise self.conversion_error("Parameter %s expects a string value, got %r" % (name, raw))
        return raw
