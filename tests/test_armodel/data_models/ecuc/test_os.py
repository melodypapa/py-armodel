from armodel.data_models.ecuc import OsApplication, OsOs, OsTask


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
