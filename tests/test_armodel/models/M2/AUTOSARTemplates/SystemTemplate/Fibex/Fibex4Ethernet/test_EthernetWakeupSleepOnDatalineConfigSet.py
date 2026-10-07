"""Model tests for EthernetWakeupSleepOnDatalineConfigSet (R23-11 CP_TPS_SystemTemplate, Table 3.116, p.159)."""

import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    EthernetWakeupSleepOnDatalineConfig,
    EthernetWakeupSleepOnDatalineConfigSet,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore import FibexElement

CLASS_NOTE = (
    "This meta-class is the main element that aggregates different config set regarding the ethernet wakeup and sleep on data line. "
    "Tags: atp.recommendedPackage=EthernetWakeupSleepOnDatalineConfigSets"
)

MEMBER_NOTE = "The relationship defines a collection of EthernetWakeup SleepOnDatalineConfig configurations which are available."


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class TestEthernetWakeupSleepOnDatalineConfigSet:
    """Spec-sync tests for EthernetWakeupSleepOnDatalineConfigSet (Table 3.116, p.159)."""

    def _make(self) -> EthernetWakeupSleepOnDatalineConfigSet:
        return EthernetWakeupSleepOnDatalineConfigSet(MockParent(), "WSD_CFG_SET")

    def test_inheritance(self):
        assert issubclass(EthernetWakeupSleepOnDatalineConfigSet, FibexElement)
        assert issubclass(EthernetWakeupSleepOnDatalineConfigSet, ARObject)

    def test_initialization_defaults(self):
        obj = self._make()
        assert obj.getEthernetWakeupSleepOnDatalineConfigs() == []

    def test_create_appends_and_round_trips(self):
        obj = self._make()
        config = obj.createEthernetWakeupSleepOnDatalineConfig("WSD_CFG")
        assert isinstance(config, EthernetWakeupSleepOnDatalineConfig)
        assert config.getShortName() == "WSD_CFG"
        assert obj.getEthernetWakeupSleepOnDatalineConfigs() == [config]

        other = obj.createEthernetWakeupSleepOnDatalineConfig("WSD_CFG_OTHER")
        assert obj.getEthernetWakeupSleepOnDatalineConfigs() == [config, other]

    def test_create_duplicate_returns_existing(self):
        obj = self._make()
        first = obj.createEthernetWakeupSleepOnDatalineConfig("WSD_CFG")
        second = obj.createEthernetWakeupSleepOnDatalineConfig("WSD_CFG")
        assert second is first
        assert len(obj.getEthernetWakeupSleepOnDatalineConfigs()) == 1

    def test_configs_own_dedicated_list_field(self):
        obj = self._make()
        assert isinstance(obj.__dict__["ethernetWakeupSleepOnDatalineConfigs"], list)

    def test_member_order_matches_spec(self):
        source = inspect.getsource(EthernetWakeupSleepOnDatalineConfigSet.__init__)
        assert source.index("self.ethernetWakeupSleepOnDatalineConfigs:") >= 0

    def test_class_docstring_is_spec_note(self):
        assert inspect.cleandoc(EthernetWakeupSleepOnDatalineConfigSet.__doc__) == CLASS_NOTE

    def test_init_has_no_docstring(self):
        assert EthernetWakeupSleepOnDatalineConfigSet.__init__.__doc__ is None

    def test_accessor_docstrings_are_spec_notes(self):
        obj = self._make()
        create = obj.createEthernetWakeupSleepOnDatalineConfig
        getter = obj.getEthernetWakeupSleepOnDatalineConfigs
        existing = "The existing element is returned when the short name already exists (no duplicate creation)."
        assert inspect.cleandoc(create.__doc__).strip() == MEMBER_NOTE + "\n" + existing
        assert getter.__doc__.strip() == MEMBER_NOTE
