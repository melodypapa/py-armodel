from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration import Trigger, TriggerMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
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


SPEC_NOTE_TRIGGER_MAPPING = "Defines the mapping of two particular unequally named Triggers in the given context."


class TestTriggerMapping:
    """
    Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.31, p.134 (R23-11)
    """

    def test_initialization(self):
        """Test TriggerMapping initialization defaults (Table 4.31)"""
        mapping = TriggerMapping()

        assert mapping is not None
        assert mapping.firstTriggerRef is None
        assert mapping.secondTriggerRef is None

    def test_heritage_direct_base_is_ar_object(self):
        """TriggerMapping's spec Base is ARObject only (Table 4.31) — no Referrable"""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable, Referrable

        assert TriggerMapping.__bases__[0] is ARObject
        assert issubclass(TriggerMapping, ARObject)
        assert not issubclass(TriggerMapping, Referrable)
        assert not issubclass(TriggerMapping, Identifiable)

    def test_class_docstring_matches_spec_note(self):
        """The class docstring must be the verbatim Table 4.31 Note"""
        mapping = TriggerMapping()
        assert mapping.__doc__ == SPEC_NOTE_TRIGGER_MAPPING

    def test_get_set_first_trigger_ref(self):
        """setFirstTriggerRef/getFirstTriggerRef round-trip with a real RefType"""
        mapping = TriggerMapping()
        assert mapping.getFirstTriggerRef() is None

        value = RefType().setValue("/PortInterfaces/TriggerInterface/Trig1")
        result = mapping.setFirstTriggerRef(value)
        assert result is mapping
        assert mapping.getFirstTriggerRef() == value
        assert mapping.getFirstTriggerRef().getValue() == "/PortInterfaces/TriggerInterface/Trig1"

    def test_set_first_trigger_ref_none_is_noop(self):
        """setFirstTriggerRef(None) is a no-op and still chains"""
        mapping = TriggerMapping()
        value = RefType().setValue("/PortInterfaces/TriggerInterface/Trig1")
        mapping.setFirstTriggerRef(value)
        result = mapping.setFirstTriggerRef(None)
        assert result is mapping
        assert mapping.getFirstTriggerRef() == value

    def test_get_set_second_trigger_ref(self):
        """setSecondTriggerRef/getSecondTriggerRef round-trip with a real RefType"""
        mapping = TriggerMapping()
        assert mapping.getSecondTriggerRef() is None

        value = RefType().setValue("/PortInterfaces/TriggerInterface/Trig2")
        result = mapping.setSecondTriggerRef(value)
        assert result is mapping
        assert mapping.getSecondTriggerRef() == value
        assert mapping.getSecondTriggerRef().getValue() == "/PortInterfaces/TriggerInterface/Trig2"

    def test_set_second_trigger_ref_none_is_noop(self):
        """setSecondTriggerRef(None) is a no-op and still chains"""
        mapping = TriggerMapping()
        value = RefType().setValue("/PortInterfaces/TriggerInterface/Trig2")
        mapping.setSecondTriggerRef(value)
        result = mapping.setSecondTriggerRef(None)
        assert result is mapping
        assert mapping.getSecondTriggerRef() == value
