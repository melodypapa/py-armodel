import inspect
import typing

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import ApplicationPartition


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class TestApplicationPartition:
    """Test cases for ApplicationPartition (Table 5.5, p.201)."""

    def test_inheritance(self):
        assert issubclass(ApplicationPartition, ARElement)

    def test_class_docstring_note(self):
        expected = (
            "ApplicationPartition to which SwComponentPrototypes are mapped at a point in time when the corresponding "
            "EcuInstance is not yet known or defined. In a later methodology step the Application Partition can be "
            "assigned to an EcuPartition. Tags: atp.recommendedPackage=ApplicationPartitions"
        )
        assert inspect.cleandoc(ApplicationPartition.__doc__) == expected

    def test_init_has_no_docstring(self):
        assert ApplicationPartition.__init__.__doc__ is None

    def test_initialization(self):
        parent = MockParent()
        app_partition = ApplicationPartition(parent, "AP1")
        assert app_partition.getShortName() == "AP1"
        assert app_partition.getParent() is parent

    def test_no_own_members(self):
        parent = MockParent()
        app_partition = ApplicationPartition(parent, "AP1")
        base_partition = ARElement.__new__(ApplicationPartition)
        ARElement.__init__(base_partition, parent, "BASE")
        own_members = [k for k in vars(app_partition) if k not in vars(base_partition)]
        assert own_members == []

    def test_create_via_ar_package(self):
        document = AUTOSAR.getInstance()
        document.setARRelease("R23-11")
        pkg = document.createARPackage("Pkg")
        app_partition = pkg.createApplicationPartition("AP1")
        assert isinstance(app_partition, ApplicationPartition)
        assert app_partition.getShortName() == "AP1"
        duplicate = pkg.createApplicationPartition("AP1")
        assert duplicate is app_partition

    def test_type_hints(self):
        hints = typing.get_type_hints(ApplicationPartition.__init__)
        assert hints.get("parent") is ARObject
        assert hints.get("short_name") is str
