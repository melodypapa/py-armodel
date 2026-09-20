from armodel.data_models.ecuc import OsAlarm, OsApplication, OsIsr, OsOs, OsTask


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


def test_os_isr_default_values():
    isr = OsIsr()

    assert isr.getName() == ""
    assert isr.getOsIsrName() is None
    assert isr.getOsIsrCategory() is None
    assert isr.getOsIsrPriority() is None
    assert isr.getOsIsrPeriod() is None
    assert isr.getOsIsrResourceRef() is None
    assert isr.getOsIsrInterruptSource() is None
    assert isr.getOsIsrAccessingApplications() == []
    assert isr.getOsMemoryMappingCodeLocationRef() is None
    assert isr.getOsIsrExecutionBudget() is None
    assert isr.getOsIsrTimeFrame() is None
    assert isr.getOsIsrAllInterruptLockBudget() is None
    assert isr.getOsIsrOsInterruptLockBudget() is None
    assert isr.getOsIsrResourceLockBudgets() == []
    assert isr.getOsIsrResourceLockResourceRefs() == []


def test_os_isr_chained_setters_return_self():
    isr = OsIsr()
    result = (
        isr.setName("CanIsr")
        .setOsIsrName("CanIsrFunction")
        .setOsIsrCategory("CATEGORY_2")
        .setOsIsrPriority(5)
        .setOsIsrPeriod(0.005)
        .setOsIsrResourceRef("/Os/Os/Res1")
        .setOsIsrInterruptSource("/Os/Os/Source1")
        .setOsMemoryMappingCodeLocationRef("/Os/Os/MemRegion")
        .setOsIsrExecutionBudget(0.001)
        .setOsIsrTimeFrame(0.02)
        .setOsIsrAllInterruptLockBudget(0.0001)
        .setOsIsrOsInterruptLockBudget(0.0002)
    )

    assert result is isr
    assert isr.getName() == "CanIsr"
    assert isr.getOsIsrName() == "CanIsrFunction"
    assert isr.getOsIsrCategory() == "CATEGORY_2"
    assert isr.getOsIsrPriority() == 5
    assert isr.getOsIsrPeriod() == 0.005
    assert isr.getOsIsrResourceRef() == "/Os/Os/Res1"
    assert isr.getOsIsrInterruptSource() == "/Os/Os/Source1"
    assert isr.getOsMemoryMappingCodeLocationRef() == "/Os/Os/MemRegion"
    assert isr.getOsIsrExecutionBudget() == 0.001
    assert isr.getOsIsrTimeFrame() == 0.02
    assert isr.getOsIsrAllInterruptLockBudget() == 0.0001
    assert isr.getOsIsrOsInterruptLockBudget() == 0.0002


def test_os_isr_resource_lock_lists_are_per_instance():
    first = OsIsr().setName("ISR1")
    second = OsIsr().setName("ISR2")
    first.addOsIsrResourceLockBudget(0.0005)
    first.addOsIsrResourceLockResourceRef("/Os/Os/Res1")

    assert first.getOsIsrResourceLockBudgets() == [0.0005]
    assert first.getOsIsrResourceLockResourceRefs() == ["/Os/Os/Res1"]
    assert second.getOsIsrResourceLockBudgets() == []
    assert second.getOsIsrResourceLockResourceRefs() == []


def test_os_os_isr_collection():
    isr = OsIsr().setName("CanIsr")
    os_os = OsOs().setName("Os")

    assert os_os.addOsIsr(isr) is os_os
    assert os_os.getOsIsrs() == [isr]
