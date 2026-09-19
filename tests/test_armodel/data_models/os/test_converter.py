import logging
from pathlib import Path

import pytest

from armodel.data_models.os import OsOs
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import (
    BooleanValue,
    Container,
    EnumerationValue,
    FloatValue,
    IntegerValue,
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
from armodel.parser import OsEcucConversionError, OsEcucParser

DEMO_FILE = Path("tests/integration_tests/test_files/Os_ECUC.arxml")


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


def test_from_file_converts_demo_os_configuration():
    result = OsEcucParser().load(Path("tests/integration_tests/test_files/Os_ECUC.arxml"))

    assert [item.getName() for item in result.getOsApplications()] == ["OsApplication_QM"]
    assert [item.getName() for item in result.getOsTasks()] == [
        "Init_Task",
        "Rte_Time_Task",
        "Rte_Event_Task",
        "SchMDiagStateTask_20ms",
    ]
    application = result.getOsApplications()[0]
    assert [item.getName() for item in application.getOsAppTaskRefs()] == [
        "Init_Task",
        "Rte_Time_Task",
        "Rte_Event_Task",
        "SchMDiagStateTask_20ms",
    ]
    assert application.OsTrusted is False


def test_os_os_takes_module_name_and_task_scalar_fields():
    result = OsEcucParser().load(DEMO_FILE)

    assert result.getName() == "Os"
    init_task = result.getOsTasks()[0]
    assert init_task.getName() == "Init_Task"
    assert init_task.OsTaskActivation == 1
    assert init_task.OsTaskPeriod == pytest.approx(0.02)
    assert init_task.OsTaskPriority == 127
    assert init_task.OsTaskSchedule == "NON"
    assert init_task.OsStacksize == 1024

    rte_time_task = result.getOsTasks()[1]
    assert rte_time_task.OsTaskPeriod == pytest.approx(0.01)
    assert rte_time_task.OsTaskSchedule == "FULL"


def test_demo_application_fields_hooks_and_restart_task():
    result = OsEcucParser().load(DEMO_FILE)

    application = result.getOsApplications()[0]
    assert application.OsTrusted is False
    assert application.getOsAppAlarmRefs() == ["/Os/Os/AlarmIncrementRteCounter"]
    assert application.getOsAppCounterRefs() == ["/Os/Os/HwCounter", "/Os/Os/Rte_Counter"]
    assert application.OsAppEcucPartitionRef is None
    assert application.OsAppStartupHook is False
    assert application.OsAppErrorHook is False
    assert application.OsAppShutdownHook is False
    assert application.getOsTrustedFunctionNames() == []
    assert application.ApplicationState == "APPLICATION_ACCESSIBLE"

    restart_task = application.getOsRestartTask()
    assert restart_task is not None
    assert restart_task.getName() == "Init_Task"


def test_demo_task_flattened_autostart_timing_protection_and_resource_locks():
    result = OsEcucParser().load(DEMO_FILE)

    init_task = result.getOsTasks()[0]
    assert init_task.getOsTaskAppModeRefs() == ["/Os/Os/OSDEFAULTAPPMODE"]
    assert init_task.OsTaskAllInterruptLockBudget == pytest.approx(0.001)
    assert init_task.OsTaskExecutionBudget == pytest.approx(0.005)
    assert init_task.OsTaskOsInterruptLockBudget == pytest.approx(0.002)
    assert init_task.OsTaskTimeFrame == pytest.approx(0.02)
    assert init_task.getOsTaskResourceLockBudgets() == [pytest.approx(0.001), pytest.approx(0.002)]
    assert init_task.getOsTaskResourceLockResourceRefs() == ["/Os/Os/Resource_Init", "/Os/Os/Resource_Diag"]

    rte_time_task = result.getOsTasks()[1]
    assert rte_time_task.getOsTaskAppModeRefs() == []
    assert rte_time_task.OsTaskAllInterruptLockBudget is None
    assert rte_time_task.getOsTaskResourceLockBudgets() == []


def test_bidirectional_membership_shares_task_instances():
    result = OsEcucParser().load(DEMO_FILE)

    application = result.getOsApplications()[0]
    for member in application.getOsAppTaskRefs():
        assert member in result.getOsTasks()
        assert member is result.getOsTasks()[result.getOsTasks().index(member)]
        assert application in member.getOsTaskAccessingApplications()
    assert len(result.getOsTasks()) == 4
    for task in result.getOsTasks():
        assert len(task.getOsTaskAccessingApplications()) == 1


def test_task_event_references_preserve_order():
    result = OsEcucParser().load(DEMO_FILE)

    rte_event_task = result.getOsTasks()[2]
    assert rte_event_task.getOsTaskEventRefs() == [
        "/Os/Os/Rte_OSShutdownEvent",
        "/Os/Os/Rte_OSTriggerExecutableEvent_Rte_Event_Task_DRE_523E8C37B43C9473DFA14A98BC1F65F2",
        "/Os/Os/Rte_OSTriggerExecutableEvent_Rte_Event_Task_MSE_4FF9241E67DF8B0AADC83685D425BB32",
    ]


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
    assert result.getOsTasks()[0].OsTaskActivation == 1


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
    assert result.getOsTasks()[0].OsTaskPriority == 5


def test_from_file_delegate_matches_parser(tmp_path):
    result = OsOs.from_file(DEMO_FILE)

    assert [item.getName() for item in result.getOsTasks()] == [
        "Init_Task",
        "Rte_Time_Task",
        "Rte_Event_Task",
        "SchMDiagStateTask_20ms",
    ]
