from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration import Trigger, TriggerMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import MultidimensionalTime
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwImplPolicyEnum

SPEC_NOTE = "A trigger which is provided (i.e. released) or required (i.e. used to activate something) in the given context."


class TestTrigger:
    def test_initialization(self):
        """Test Trigger initialization defaults"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        trigger = Trigger(ar_root, "TestTrigger")

        assert trigger is not None
        assert trigger.getShortName() == "TestTrigger"
        assert trigger.swImplPolicy is None
        assert trigger.triggerPeriod is None

    def test_heritage_direct_base_is_atp_structure_element(self):
        """Trigger's most-derived spec base is AtpStructureElement (Table 4.13)"""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable

        assert Trigger.__bases__[0] is AtpStructureElement
        assert issubclass(Trigger, AtpStructureElement)
        assert issubclass(Trigger, Identifiable)

    def test_class_docstring_matches_spec_note(self):
        """The class docstring must be the verbatim Table 4.13 Note"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        trigger = Trigger(ar_root, "TestTrigger")
        assert trigger.__doc__ == SPEC_NOTE

    def test_get_set_sw_impl_policy(self):
        """setSwImplPolicy/getSwImplPolicy round-trip with a real SwImplPolicyEnum"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        trigger = Trigger(ar_root, "TestTrigger")
        assert trigger.getSwImplPolicy() is None

        value = SwImplPolicyEnum().setValue(SwImplPolicyEnum.QUEUED)
        result = trigger.setSwImplPolicy(value)
        assert result is trigger
        assert trigger.getSwImplPolicy() == value

    def test_set_sw_impl_policy_none_is_noop(self):
        """setSwImplPolicy(None) is a no-op and still chains"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        trigger = Trigger(ar_root, "TestTrigger")
        value = SwImplPolicyEnum().setValue(SwImplPolicyEnum.STANDARD)
        trigger.setSwImplPolicy(value)
        result = trigger.setSwImplPolicy(None)
        assert result is trigger
        assert trigger.getSwImplPolicy() == value

    def test_get_set_trigger_period(self):
        """setTriggerPeriod/getTriggerPeriod round-trip with a real MultidimensionalTime"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        trigger = Trigger(ar_root, "TestTrigger")
        assert trigger.getTriggerPeriod() is None

        value = MultidimensionalTime()
        result = trigger.setTriggerPeriod(value)
        assert result is trigger
        assert trigger.getTriggerPeriod() is value

    def test_set_trigger_period_none_is_noop(self):
        """setTriggerPeriod(None) is a no-op and still chains"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        trigger = Trigger(ar_root, "TestTrigger")
        value = MultidimensionalTime()
        trigger.setTriggerPeriod(value)
        result = trigger.setTriggerPeriod(None)
        assert result is trigger
        assert trigger.getTriggerPeriod() is value


class TestTriggerMapping:
    def test_initialization(self):
        """Test TriggerMapping initialization"""
        mapping = TriggerMapping()

        assert mapping is not None
        assert mapping.firstTriggerRef is None
        assert mapping.secondTriggerRef is None

    def test_get_first_trigger_ref(self):
        """Test getFirstTriggerRef method"""
        mapping = TriggerMapping()
        assert mapping.getFirstTriggerRef() is None

    def test_set_first_trigger_ref(self):
        """Test setFirstTriggerRef method"""
        mapping = TriggerMapping()
        test_value = RefType().setValue("FirstTriggerRef")
        result = mapping.setFirstTriggerRef(test_value)
        assert result is mapping
        assert mapping.getFirstTriggerRef() == test_value

    def test_set_first_trigger_ref_none(self):
        """Test setFirstTriggerRef with None value"""
        mapping = TriggerMapping()
        result = mapping.setFirstTriggerRef(None)
        assert result is mapping
        assert mapping.getFirstTriggerRef() is None

    def test_get_second_trigger_ref(self):
        """Test getSecondTriggerRef method"""
        mapping = TriggerMapping()
        assert mapping.getSecondTriggerRef() is None

    def test_set_second_trigger_ref(self):
        """Test setSecondTriggerRef method"""
        mapping = TriggerMapping()
        test_value = RefType().setValue("SecondTriggerRef")
        result = mapping.setSecondTriggerRef(test_value)
        assert result is mapping
        assert mapping.getSecondTriggerRef() == test_value

    def test_set_second_trigger_ref_none(self):
        """Test setSecondTriggerRef with None value"""
        mapping = TriggerMapping()
        result = mapping.setSecondTriggerRef(None)
        assert result is mapping
        assert mapping.getSecondTriggerRef() is None

    def test_all_properties(self):
        """Test setting all properties"""
        mapping = TriggerMapping()

        ref1 = RefType().setValue("FirstTriggerRef")
        ref2 = RefType().setValue("SecondTriggerRef")

        mapping.setFirstTriggerRef(ref1)
        mapping.setSecondTriggerRef(ref2)

        assert mapping.getFirstTriggerRef() == ref1
        assert mapping.getSecondTriggerRef() == ref2
