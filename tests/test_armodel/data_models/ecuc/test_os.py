from armodel.data_models.ecuc import OsAlarm, OsApplication, OsIsr, OsOs, OsScheduleTable, OsScheduleTableExpiryPoint, OsTask


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


def test_os_schedule_table_expiry_point_default_values_and_setters():
    expiry_point = OsScheduleTableExpiryPoint()

    assert expiry_point.getOsScheduleTableExpiryPointOffset() is None
    assert expiry_point.getOsScheduleTableMaxShorten() is None
    assert expiry_point.getOsScheduleTableMaxLengthen() is None
    assert expiry_point.getOsScheduleTableActivateTaskRef() is None
    assert expiry_point.getOsScheduleTableSetEventTaskRef() is None
    assert expiry_point.getOsScheduleTableSetEventRef() is None

    assert (
        expiry_point.setOsScheduleTableExpiryPointOffset(2)
        .setOsScheduleTableMaxShorten(1)
        .setOsScheduleTableMaxLengthen(1)
        .setOsScheduleTableActivateTaskRef("/Os/Os/Task1")
        .setOsScheduleTableSetEventTaskRef("/Os/Os/Task2")
        .setOsScheduleTableSetEventRef("/Os/Os/Event1")
        is expiry_point
    )

    assert expiry_point.getOsScheduleTableExpiryPointOffset() == 2
    assert expiry_point.getOsScheduleTableMaxShorten() == 1
    assert expiry_point.getOsScheduleTableMaxLengthen() == 1
    assert expiry_point.getOsScheduleTableActivateTaskRef() == "/Os/Os/Task1"
    assert expiry_point.getOsScheduleTableSetEventTaskRef() == "/Os/Os/Task2"
    assert expiry_point.getOsScheduleTableSetEventRef() == "/Os/Os/Event1"


def test_os_schedule_table_default_values():
    schedule_table = OsScheduleTable()

    assert schedule_table.getName() == ""
    assert schedule_table.getOsScheduleTableCounterRef() is None
    assert schedule_table.getOsScheduleTableDuration() is None
    assert schedule_table.getOsScheduleTableRepeating() is None
    assert schedule_table.getOsScheduleTableAccessingApplications() == []
    assert schedule_table.getOsScheduleTableExpiryPoints() == []
    assert schedule_table.getOsScheduleTableAutostartType() is None
    assert schedule_table.getOsScheduleTableStartValue() is None
    assert schedule_table.getOsScheduleTableAppModeRef() is None
    assert schedule_table.getOsScheduleTableSyncStrategy() is None
    assert schedule_table.getOsScheduleTableExplicitPrecision() is None


def test_os_schedule_table_chained_setters_return_self():
    schedule_table = OsScheduleTable()
    first = OsScheduleTableExpiryPoint().setOsScheduleTableExpiryPointOffset(2)
    second = OsScheduleTableExpiryPoint().setOsScheduleTableExpiryPointOffset(5)
    result = (
        schedule_table.setName("Table1")
        .setOsScheduleTableCounterRef("/Os/Os/HwCounter")
        .setOsScheduleTableDuration(10)
        .setOsScheduleTableRepeating(True)
        .setOsScheduleTableAutostartType("RELATIVE")
        .setOsScheduleTableStartValue(0)
        .setOsScheduleTableAppModeRef("/Os/Os/OSDEFAULTAPPMODE")
        .setOsScheduleTableSyncStrategy("IMPLICIT")
        .setOsScheduleTableExplicitPrecision(0)
    )

    assert result is schedule_table
    assert schedule_table.addOsScheduleTableAccessingApplication("/Os/Os/App1") is schedule_table
    assert schedule_table.addOsScheduleTableExpiryPoint(first) is schedule_table
    schedule_table.addOsScheduleTableExpiryPoint(second)

    assert schedule_table.getName() == "Table1"
    assert schedule_table.getOsScheduleTableCounterRef() == "/Os/Os/HwCounter"
    assert schedule_table.getOsScheduleTableDuration() == 10
    assert schedule_table.getOsScheduleTableRepeating() is True
    assert schedule_table.getOsScheduleTableAccessingApplications() == ["/Os/Os/App1"]
    assert schedule_table.getOsScheduleTableExpiryPoints() == [first, second]
    assert schedule_table.getOsScheduleTableAutostartType() == "RELATIVE"
    assert schedule_table.getOsScheduleTableStartValue() == 0
    assert schedule_table.getOsScheduleTableAppModeRef() == "/Os/Os/OSDEFAULTAPPMODE"
    assert schedule_table.getOsScheduleTableSyncStrategy() == "IMPLICIT"
    assert schedule_table.getOsScheduleTableExplicitPrecision() == 0


def test_os_os_schedule_table_collection():
    schedule_table = OsScheduleTable().setName("Table1")
    os_os = OsOs().setName("Os")

    assert os_os.addOsScheduleTable(schedule_table) is os_os
    assert os_os.getOsScheduleTables() == [schedule_table]
