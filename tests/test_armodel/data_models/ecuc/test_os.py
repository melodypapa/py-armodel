from armodel.data_models.ecuc import OsAlarm, OsApplication, OsOs, OsTask


def test_os_model_identity_and_standard_fields():
    application = OsApplication()
    task = OsTask()
    application.setName("App")
    task.setName("Task")
    assert application.getName() == "App"
    assert task.getName() == "Task"
    assert hasattr(application, "osTrusted")
    assert hasattr(task, "osTaskPriority")
    assert hasattr(task, "osTaskAppModeRef")
    assert hasattr(task, "osTaskExecutionBudget")
    assert hasattr(task, "osStacksize")


def test_os_relationship_fields_are_initialized_independently():
    application = OsApplication().setName("App")
    task = OsTask().setName("Task")
    first = OsOs().setName("Os")
    second = OsOs().setName("OtherOs")

    first.addOsApplication(application)
    second.addOsApplication(OsApplication().setName("Other"))
    application.addOsAppTaskRef(task)

    assert first.getOsApplications()[0].getOsAppTaskRefs() == [task]
    assert second.getOsApplications()[0].getOsAppTaskRefs() == []


def test_os_model_default_values():
    application = OsApplication()
    task = OsTask()
    os_os = OsOs()

    assert application.osTrusted is None
    assert application.osAppEcucPartitionRef is None
    assert application.osRestartTask is None
    assert application.osAppTaskRef == []
    assert application.osTrustedFunctionName == []
    assert application.applicationState == "APPLICATION_ACCESSIBLE"
    assert task.osTaskActivation is None
    assert task.osStacksize is None
    assert task.osTaskResourceLockBudget == []
    assert task.osTaskAccessingApplication == []
    assert os_os.getOsApplications() == []
    assert os_os.getOsTasks() == []


def test_os_model_chained_setters_return_self():
    task = OsTask()
    assert task.setName("T").setOsTaskPriority(10).setOsStacksize(512) is task


def test_os_alarm_default_values():
    alarm = OsAlarm()

    assert alarm.getName() == ""
    assert alarm.getOsAlarmCounterRef() is None
    assert alarm.getOsAlarmAccessingApplications() == []
    assert alarm.getOsAlarmActivateTaskRef() is None
    assert alarm.getOsAlarmSetEventTaskRef() is None
    assert alarm.getOsAlarmSetEventRef() is None
    assert alarm.getOsAlarmIncrementCounterRef() is None
    assert alarm.getOsAlarmCallbackName() is None
    assert alarm.getOsAlarmAlarmTime() is None
    assert alarm.getOsAlarmAutostartType() is None
    assert alarm.getOsAlarmCycleTime() is None
    assert alarm.getOsAlarmAppModeRef() is None


def test_os_alarm_chained_setters_return_self():
    alarm = OsAlarm()
    result = (
        alarm.setName("Alarm1")
        .setOsAlarmCounterRef("/Os/Os/HwCounter")
        .setOsAlarmActivateTaskRef("/Os/Os/Task1")
        .setOsAlarmSetEventTaskRef("/Os/Os/Task2")
        .setOsAlarmSetEventRef("/Os/Os/Event1")
        .setOsAlarmIncrementCounterRef("/Os/Os/Counter1")
        .setOsAlarmCallbackName("AlarmCb")
        .setOsAlarmAlarmTime(1)
        .setOsAlarmAutostartType("RELATIVE")
        .setOsAlarmCycleTime(2)
        .setOsAlarmAppModeRef("/Os/Os/OSDEFAULTAPPMODE")
    )

    assert result is alarm
    assert alarm.getName() == "Alarm1"
    assert alarm.getOsAlarmCounterRef() == "/Os/Os/HwCounter"
    assert alarm.getOsAlarmActivateTaskRef() == "/Os/Os/Task1"
    assert alarm.getOsAlarmSetEventTaskRef() == "/Os/Os/Task2"
    assert alarm.getOsAlarmSetEventRef() == "/Os/Os/Event1"
    assert alarm.getOsAlarmIncrementCounterRef() == "/Os/Os/Counter1"
    assert alarm.getOsAlarmCallbackName() == "AlarmCb"
    assert alarm.getOsAlarmAlarmTime() == 1
    assert alarm.getOsAlarmAutostartType() == "RELATIVE"
    assert alarm.getOsAlarmCycleTime() == 2
    assert alarm.getOsAlarmAppModeRef() == "/Os/Os/OSDEFAULTAPPMODE"


def test_os_alarm_accessing_application_list_is_per_instance():
    first = OsAlarm().setName("A1")
    second = OsAlarm().setName("A2")
    first.addOsAlarmAccessingApplication("/Os/Os/App1")

    assert first.getOsAlarmAccessingApplications() == ["/Os/Os/App1"]
    assert second.getOsAlarmAccessingApplications() == []


def test_os_os_alarm_collection():
    alarm = OsAlarm().setName("A1")
    os_os = OsOs().setName("Os")
    other = OsOs().setName("OtherOs")

    assert os_os.addOsAlarm(alarm) is os_os

    assert os_os.getOsAlarms() == [alarm]
    assert other.getOsAlarms() == []
