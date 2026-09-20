import logging

import pytest

from armodel.data_models.ecuc import OsOs
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import (
    BooleanValue,
    ConfigReferenceValue,
    Container,
    EcucAbstractReferenceValue,
    EcucModuleConfigurationValues,
    EcucParameterValue,
    EnumerationValue,
    FloatValue,
    IntegerValue,
    ModuleConfiguration,
    ParameterValue,
    ReferenceValue,
    StringValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Float,
    RefType,
    String,
    UnlimitedInteger,
)
from armodel.parser import EcucParser, OsEcucConversionError, OsEcucParser


def _ref(path):
    return RefType().setValue(path)


def _int_parameter(name, value):
    parameter = IntegerValue()
    parameter.setDefinitionRef(_ref("/TS/Os/OsTask/" + name))
    value_object = UnlimitedInteger()
    value_object.value = value
    parameter.setValue(value_object)
    return parameter


def _float_parameter(name, value):
    parameter = FloatValue()
    parameter.setDefinitionRef(_ref("/TS/Os/OsTask/" + name))
    value_object = Float()
    value_object.value = value
    parameter.setValue(value_object)
    return parameter


def _bool_parameter(name, value):
    parameter = BooleanValue()
    parameter.setDefinitionRef(_ref("/TS/Os/OsTask/" + name))
    value_object = Boolean()
    value_object.value = value
    parameter.setValue(value_object)
    return parameter


def _string_parameter(name, value):
    parameter = StringValue()
    parameter.setDefinitionRef(_ref("/TS/Os/OsTask/" + name))
    value_object = String()
    value_object.value = value
    parameter.setValue(value_object)
    return parameter


def _enum_parameter(name, value):
    parameter = EnumerationValue()
    parameter.setDefinitionRef(_ref("/TS/Os/OsTask/" + name))
    value_object = String()
    value_object.value = value
    parameter.setValue(value_object)
    return parameter


def _reference(name, path):
    reference = ReferenceValue()
    reference.setDefinitionRef(_ref("/TS/Os/OsTask/" + name))
    reference.setValueRef(_ref(path))
    return reference


def _copy_children(target, blueprint):
    for sub_blueprint in blueprint.getSubContainers():
        sub_container = target.createSubContainer(sub_blueprint.getShortName())
        sub_container.setDefinitionRef(sub_blueprint.getDefinitionRef())
        for parameter in sub_blueprint.getParameterValues():
            sub_container.addParameterValue(parameter)
        for reference in sub_blueprint.getReferenceValues():
            sub_container.addReferenceValue(reference)
        _copy_children(sub_container, sub_blueprint)


def _container(short_name, definition_name, parameters=(), references=(), sub_containers=()):
    container = Container(None, short_name)
    container.setDefinitionRef(_ref("/TS/Os/" + definition_name))
    for parameter in parameters:
        container.addParameterValue(parameter)
    for reference in references:
        container.addReferenceValue(reference)
    for sub_container in sub_containers:
        container.addElement(sub_container)
        container.subContainers.append(sub_container)
    return container


def _build_document(containers):
    document = AUTOSAR.getInstance()
    document.clear()
    document.setARRelease("R23-11")
    package = document.createARPackage("Os")
    module = package.createModuleConfiguration("Os")
    module.setDefinitionRef(_ref("/TS/Os"))
    for blueprint in containers:
        target = module.createContainer(blueprint.getShortName())
        target.setDefinitionRef(blueprint.getDefinitionRef())
        for parameter in blueprint.getParameterValues():
            target.addParameterValue(parameter)
        for reference in blueprint.getReferenceValues():
            target.addReferenceValue(reference)
        _copy_children(target, blueprint)
    return document


def test_vendor_specific_parameter_is_ignored():
    containers = [
        _container(
            "Vendor_Task",
            "OsTask",
            parameters=[_int_parameter("OsTaskActivation", 1), _int_parameter("OsVendorSpecificParam", 42)],
        )
    ]
    result = OsEcucParser().parseEcuc(_build_document(containers))

    assert [item.getName() for item in result.getOsTasks()] == ["Vendor_Task"]
    assert result.getOsTasks()[0].osTaskActivation == 1


def test_generic_ecuc_parser_discovers_module_containers():
    containers = [_container("Generic_Task", "OsTask")]
    document = _build_document(containers)

    parser = EcucParser()
    index = parser.get_module_containers(document, module_name="Os")

    assert list(index) == ["/Os/Os/Generic_Task"]
    assert parser.get_definition_name(index["/Os/Os/Generic_Task"].getDefinitionRef()) == "OsTask"


def test_generic_ecuc_parser_returns_existing_model_objects():
    parameter = _int_parameter("OsTaskActivation", 1)
    reference = _reference("OsTaskEventRef", "/Os/Os/Event")
    container = _container("Typed_Task", "OsTask", parameters=[parameter], references=[reference])
    document = _build_document([container])

    parser = EcucParser()
    modules = parser.get_modules(document)
    values = parser.get_parameter_values(document.getARPackages()[0].getElement("Os", ModuleConfiguration).getContainers()[0])
    references = parser.get_reference_values(document.getARPackages()[0].getElement("Os", ModuleConfiguration).getContainers()[0])

    assert isinstance(modules[0], (ModuleConfiguration, EcucModuleConfigurationValues))
    assert isinstance(values[0], (ParameterValue, EcucParameterValue))
    assert isinstance(references[0], (ConfigReferenceValue, EcucAbstractReferenceValue))


def test_numeric_string_values_are_converted_for_autosar_4_ecuc():
    containers = [_container("String_Task", "OsTask", parameters=[_string_parameter("OsStacksize", "1024")])]

    result = OsEcucParser().parseEcuc(_build_document(containers))

    assert result.getOsTasks()[0].getOsStacksize() == 1024


def test_unresolved_reference_raises_in_strict_mode():
    containers = [
        _container(
            "Dangling_Task",
            "OsTask",
            parameters=[_int_parameter("OsTaskActivation", 1)],
            references=[_reference("OsTaskEventRef", "/Os/Os/MissingEvent")],
        )
    ]
    document = _build_document(containers)

    with pytest.raises(OsEcucConversionError, match="MissingEvent"):
        OsEcucParser().parseEcuc(document)


def test_unresolved_reference_warns_in_warning_mode(caplog):
    containers = [
        _container(
            "Dangling_Task",
            "OsTask",
            parameters=[_int_parameter("OsTaskActivation", 1)],
            references=[_reference("OsTaskEventRef", "/Os/Os/MissingEvent")],
        )
    ]
    document = _build_document(containers)

    with caplog.at_level(logging.WARNING):
        result = OsEcucParser().parseEcuc(document, warning=True)

    assert result.getOsTasks()[0].getOsTaskEventRefs() == ["/Os/Os/MissingEvent"]
    assert any("MissingEvent" in record.message for record in caplog.records)


def test_unresolved_task_accessing_application_warns_in_warning_mode():
    containers = [
        _container(
            "Lonely_Task",
            "OsTask",
            parameters=[_int_parameter("OsTaskActivation", 1)],
            references=[_reference("OsTaskAccessingApplication", "/Os/Os/MissingApplication")],
        )
    ]
    document = _build_document(containers)

    result = OsEcucParser().parseEcuc(document, warning=True)

    assert result.getOsTasks()[0].getOsTaskAccessingApplications() == []


def test_membership_reference_to_non_task_container_is_rejected():
    containers = [
        _container("NotATask", "OsCounter"),
        _container(
            "Wrong_Task",
            "OsTask",
            parameters=[_int_parameter("OsTaskActivation", 1)],
        ),
        _container(
            "App",
            "OsApplication",
            references=[_reference("OsAppTaskRef", "/Os/Os/NotATask")],
        ),
    ]
    document = _build_document(containers)

    with pytest.raises(OsEcucConversionError, match="must target an OsTask container"):
        OsEcucParser().parseEcuc(document)


def test_malformed_scalar_value_is_rejected():
    parameter = IntegerValue()
    parameter.setDefinitionRef(_ref("/TS/Os/OsTask/OsTaskActivation"))
    parameter.setValue(String().setValue("not-a-number"))
    containers = [_container("Bad_Task", "OsTask", parameters=[parameter])]
    document = _build_document(containers)

    with pytest.raises(OsEcucConversionError, match="expects an integer value"):
        OsEcucParser().parseEcuc(document)


def test_from_ecuc_delegate_matches_parser():
    containers = [_container("Delegate_Task", "OsTask", parameters=[_int_parameter("OsTaskPriority", 5)])]
    document = _build_document(containers)

    result = OsOs.from_ecuc(document)

    assert result.getName() == "Os"
    assert result.getOsTasks()[0].osTaskPriority == 5
