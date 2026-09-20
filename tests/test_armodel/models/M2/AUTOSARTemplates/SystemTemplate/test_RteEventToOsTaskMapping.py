import inspect

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping import AppOsTaskProxyToEcuTaskProxyMapping, OsTaskPreemptabilityEnum, OsTaskProxy


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class Test_RteEventToOsTaskMapping:
    """Test cases for RteEventToOsTaskMapping-related classes."""

    def test_AppOsTaskProxyToEcuTaskProxyMapping(self):
        """Test AppOsTaskProxyToEcuTaskProxyMapping class functionality."""
        parent = MockParent()
        mapping = AppOsTaskProxyToEcuTaskProxyMapping(parent, "test_app_ecu_mapping")

        assert isinstance(mapping, Identifiable)

        # Test default values
        assert mapping.getAppTaskProxyRef() is None
        assert mapping.getEcuTaskProxyRef() is None
        assert mapping.getOffset() is None

        # Test setter/getter methods
        mock_app_task_ref = "mock_app_task_ref"
        mapping.setAppTaskProxyRef(mock_app_task_ref)
        assert mapping.getAppTaskProxyRef() == mock_app_task_ref

        mock_ecu_task_ref = "mock_ecu_task_ref"
        mapping.setEcuTaskProxyRef(mock_ecu_task_ref)
        assert mapping.getEcuTaskProxyRef() == mock_ecu_task_ref

        mock_offset = "mock_offset"
        mapping.setOffset(mock_offset)
        assert mapping.getOffset() == mock_offset


class Test_OsTaskPreemptabilityEnum:
    """Test cases for OsTaskPreemptabilityEnum (Table 5.16, p.209)."""

    def test_enum_members(self):
        """Spec literal values per Table 5.16 (full idx1, none idx0; displayed order full, none)."""
        assert OsTaskPreemptabilityEnum.FULL == "full"
        assert OsTaskPreemptabilityEnum.NONE == "none"

    def test_instantiability(self):
        e = OsTaskPreemptabilityEnum()
        e.setValue(OsTaskPreemptabilityEnum.FULL)
        assert e.getValue() == "full"
        assert e.getText() == "full"
        e2 = OsTaskPreemptabilityEnum()
        e2.setValue(OsTaskPreemptabilityEnum.NONE)
        assert e2.getValue() == "none"
        assert e2.getText() == "none"

    def test_enum_values(self):
        e = OsTaskPreemptabilityEnum()
        assert list(e.getEnumValues()) == ["full", "none"]


class Test_OsTaskProxy:
    """Test cases for OsTaskProxy (Table 5.15, p.208)."""

    MEMBERS = [
        "period",
        "preemptability",
        "priority",
    ]

    def test_inheritance(self):
        assert issubclass(OsTaskProxy, ARElement)
        assert issubclass(OsTaskProxy, Identifiable)

    def test_class_docstring_note(self):
        expected = "This meta-class represents a proxy for an OsTask in the System Description. Tags: atp.recommendedPackage=OsTaskProxies"
        assert inspect.cleandoc(OsTaskProxy.__doc__) == expected

    def test_initialization_defaults(self):
        pkg = AUTOSAR.getInstance().createARPackage("OsTaskProxyPkg")
        obj = OsTaskProxy(pkg, "TaskProxy1")
        assert obj.getPeriod() is None
        assert obj.getPreemptability() is None
        assert obj.getPriority() is None

    def test_member_order(self):
        pkg = AUTOSAR.getInstance().createARPackage("OsTaskProxyPkg")
        obj = OsTaskProxy(pkg, "TaskProxy1")
        members = [k for k in vars(obj) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_get_set_period(self):
        pkg = AUTOSAR.getInstance().createARPackage("OsTaskProxyPkg")
        obj = OsTaskProxy(pkg, "TaskProxy1")
        value = TimeValue()
        value.setValue("0.01")
        result = obj.setPeriod(value)
        assert result is obj
        assert obj.getPeriod() is value
        obj.setPeriod(None)
        assert obj.getPeriod() is value

    def test_get_set_preemptability(self):
        pkg = AUTOSAR.getInstance().createARPackage("OsTaskProxyPkg")
        obj = OsTaskProxy(pkg, "TaskProxy1")
        value = OsTaskPreemptabilityEnum()
        value.setValue(OsTaskPreemptabilityEnum.FULL)
        result = obj.setPreemptability(value)
        assert result is obj
        assert obj.getPreemptability() is value
        assert obj.getPreemptability().getValue() == "full"
        obj.setPreemptability(None)
        assert obj.getPreemptability() is value

    def test_get_set_priority(self):
        pkg = AUTOSAR.getInstance().createARPackage("OsTaskProxyPkg")
        obj = OsTaskProxy(pkg, "TaskProxy1")
        value = PositiveInteger()
        value.setValue("4")
        result = obj.setPriority(value)
        assert result is obj
        assert obj.getPriority() is value
        obj.setPriority(None)
        assert obj.getPriority() is value

    def test_arpackage_create_os_task_proxy(self):
        pkg = AUTOSAR.getInstance().createARPackage("OsTaskProxyPkg")
        proxy = pkg.createOsTaskProxy("TaskProxy1")
        assert isinstance(proxy, OsTaskProxy)
        assert pkg.getElement("TaskProxy1", OsTaskProxy) is proxy
        again = pkg.createOsTaskProxy("TaskProxy1")
        assert again is proxy
