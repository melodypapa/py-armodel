from armodel.data_models.os import OsApplication, OsOs, OsTask


def test_os_model_identity_and_standard_fields():
    application = OsApplication()
    task = OsTask()
    application.setName("App")
    task.setName("Task")
    assert application.getName() == "App"
    assert task.getName() == "Task"
    assert hasattr(application, "OsTrusted")
    assert hasattr(task, "OsTaskPriority")
    assert hasattr(task, "OsTaskAppModeRef")
    assert hasattr(task, "OsTaskExecutionBudget")
    assert hasattr(task, "OsStacksize")


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

    assert application.OsTrusted is None
    assert application.OsAppEcucPartitionRef is None
    assert application.OsRestartTask is None
    assert application.OsAppTaskRef == []
    assert application.OsTrustedFunctionName == []
    assert application.ApplicationState == "APPLICATION_ACCESSIBLE"
    assert task.OsTaskActivation is None
    assert task.OsStacksize is None
    assert task.OsTaskResourceLockBudget == []
    assert task.OsTaskAccessingApplication == []
    assert os_os.getOsApplications() == []
    assert os_os.getOsTasks() == []


def test_os_model_chained_setters_return_self():
    task = OsTask()
    assert task.setName("T").setOsTaskPriority(10).setOsStacksize(512) is task
