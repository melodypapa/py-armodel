import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import Container, EcucNumericalParamValue, EcucReferenceValue, EnumerationValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Numerical, RefType, String
from armodel.parser import EcucParser


class StrictError(Exception):
    pass


class StrictParser(EcucParser):
    conversion_error = StrictError


def _ref(path, dest=None):
    ref = RefType().setValue(path)
    if dest is not None:
        ref.setDest(dest)
    return ref


def _numerical(name, value, dest):
    parameter = EcucNumericalParamValue()
    parameter.setDefinitionRef(_ref("/V/M/C/" + name, dest))
    value_object = Numerical()
    value_object.value = value
    parameter.setValue(value_object)
    return parameter


def _reference(name, path):
    reference = EcucReferenceValue()
    reference.setDefinitionRef(_ref("/V/M/C/" + name, "ECUC-REFERENCE-DEF"))
    reference.setValueRef(_ref(path))
    return reference


def _document():
    document = AUTOSAR.getInstance()
    document.clear()
    document.setARRelease("R23-11")
    package = document.createARPackage("V")
    module = package.createModuleConfiguration("MyModule")
    module.setDefinitionRef(_ref("/V/M"))
    outer = module.createContainer("Outer")
    outer.setDefinitionRef(_ref("/V/M/Outer"))
    inner = outer.createSubContainer("Inner")
    inner.setDefinitionRef(_ref("/V/M/Outer/Inner"))
    return document


@pytest.mark.parametrize("raw, expected", [(True, True), ("true", True), ("FALSE", False), ("1", True), ("0.0", False), (1.0, True), (0, False), (None, None)])
def test_get_bool_accepts_ecuc_boolean_spellings(raw, expected):
    assert StrictParser().get_bool("P", raw) is expected


@pytest.mark.parametrize("raw, expected", [(10, 10), (10.0, 10), ("10", 10), ("0x10", 16), ("10.0", 10), (None, None)])
def test_get_int_accepts_integral_values_and_strings(raw, expected):
    assert StrictParser().get_int("P", raw) == expected


@pytest.mark.parametrize("raw", ["abc", "1.5", 1.5, True])
def test_get_int_rejects_non_integral_values_with_the_subclass_error(raw):
    with pytest.raises(StrictError, match="expects an integer value"):
        StrictParser().get_int("P", raw)


def test_get_bool_rejects_other_numbers_with_the_subclass_error():
    with pytest.raises(StrictError, match="expects a boolean value"):
        StrictParser().get_bool("P", "2")


def test_get_typed_value_converts_by_definition_dest():
    parser = EcucParser()
    enumeration = EnumerationValue()
    enumeration.setDefinitionRef(_ref("/V/M/C/E", "ECUC-ENUMERATION-PARAM-DEF"))
    enumeration.setValue(String().setValue("BSWM_AND"))

    assert parser.get_typed_value(_numerical("B", "1.0", "ECUC-BOOLEAN-PARAM-DEF")) is True
    assert parser.get_typed_value(_numerical("I", "20.0", "ECUC-INTEGER-PARAM-DEF")) == 20
    assert parser.get_typed_value(_numerical("F", "0.5", "ECUC-FLOAT-PARAM-DEF")) == 0.5
    assert parser.get_typed_value(enumeration) == "BSWM_AND"


def test_iter_parameters_and_references_return_definition_names():
    container = Container(None, "C")
    container.addParameterValue(_numerical("Index", "3", "ECUC-INTEGER-PARAM-DEF"))
    container.addReferenceValue(_reference("TargetRef", "  /V/M/Outer  "))
    empty = EcucReferenceValue()
    empty.setDefinitionRef(_ref("/V/M/C/EmptyRef"))
    container.addReferenceValue(empty)

    parser = EcucParser()

    assert parser.iter_parameters(container) == [("Index", 3.0)]
    assert parser.iter_references(container) == [("TargetRef", "/V/M/Outer")]


def test_get_all_containers_indexes_sub_containers_and_finds_by_definition():
    document = _document()
    parser = EcucParser()

    index = parser.get_all_containers(document, module_name="M")

    assert list(index) == ["/V/MyModule/Outer", "/V/MyModule/Outer/Inner"]
    assert [container.getShortName() for container in parser.get_containers_by_definition(index, "Inner")] == ["Inner"]
    assert parser.get_module_short_name(document, "M") == "MyModule"
    assert parser.get_module_short_name(document, "Other") is None
