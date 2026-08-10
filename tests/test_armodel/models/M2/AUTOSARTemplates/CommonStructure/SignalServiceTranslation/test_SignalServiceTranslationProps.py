"""
This module contains tests for the SignalServiceTranslationProps class in the
AUTOSAR CommonStructure.SignalServiceTranslation module.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.SignalServiceTranslation import (
    SignalServiceTranslationControlEnum,
    SignalServiceTranslationEventProps,
    SignalServiceTranslationProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestSignalServiceTranslationProps:
    """
    Test class for SignalServiceTranslationProps functionality.
    """

    def test_initialization(self):
        obj = SignalServiceTranslationProps(None, "Test")
        assert isinstance(obj, SignalServiceTranslationProps)
        assert obj.getControlConsumedEventGroupRefs() == []
        assert obj.getControlPncRefs() == []
        assert obj.getControlProvidedEventGroupRefs() == []
        assert obj.getServiceControl() is None
        assert obj.getSignalServiceTranslationEventProps() == []

    def test_add_control_consumed_event_group_ref(self):
        obj = SignalServiceTranslationProps(None, "Test")
        ref = RefType().setValue("/Sys/ConsumedEveMsgGrp")
        assert obj.addControlConsumedEventGroupRef(ref) is obj
        assert obj.getControlConsumedEventGroupRefs() == [ref]
        assert obj.addControlConsumedEventGroupRef(None) is obj
        assert obj.getControlConsumedEventGroupRefs() == [ref]

    def test_add_control_pnc_ref(self):
        obj = SignalServiceTranslationProps(None, "Test")
        ref = RefType().setValue("/Sys/PncMap")
        assert obj.addControlPncRef(ref) is obj
        assert obj.getControlPncRefs() == [ref]
        assert obj.addControlPncRef(None) is obj
        assert obj.getControlPncRefs() == [ref]

    def test_add_control_provided_event_group_ref(self):
        obj = SignalServiceTranslationProps(None, "Test")
        ref = RefType().setValue("/Sys/EventHandler")
        assert obj.addControlProvidedEventGroupRef(ref) is obj
        assert obj.getControlProvidedEventGroupRefs() == [ref]
        assert obj.addControlProvidedEventGroupRef(None) is obj
        assert obj.getControlProvidedEventGroupRefs() == [ref]

    def test_set_service_control(self):
        obj = SignalServiceTranslationProps(None, "Test")
        value = SignalServiceTranslationControlEnum()
        value.setValue(SignalServiceTranslationControlEnum.TRANSLATION_START)
        assert obj.setServiceControl(value) is obj
        assert obj.getServiceControl() is value
        assert obj.setServiceControl(None) is obj
        assert obj.getServiceControl() is value

    def test_create_signal_service_translation_event_props(self):
        obj = SignalServiceTranslationProps(None, "Test")
        child = obj.createSignalServiceTranslationEventProps("Event1")
        assert isinstance(child, SignalServiceTranslationEventProps)
        assert child.getParent() is obj
        assert obj.getSignalServiceTranslationEventProps() == [child]
