"""
This module contains tests for the SignalServiceTranslationEventProps class in the
AUTOSAR CommonStructure.SignalServiceTranslation module.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.SignalServiceTranslation import (
    SignalServiceTranslationElementProps,
    SignalServiceTranslationEventProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import VariableDataPrototypeInSystemInstanceRef


class TestSignalServiceTranslationEventProps:
    """
    Test class for SignalServiceTranslationEventProps functionality.
    """

    def test_initialization(self):
        obj = SignalServiceTranslationEventProps(None, "Test")
        assert isinstance(obj, SignalServiceTranslationEventProps)
        assert obj.getSignalServiceTranslationElementProps() == []
        assert obj.getSafeTranslation() is None
        assert obj.getSecureTranslation() is None
        assert obj.getTranslationTarget() is None

    def test_create_signal_service_translation_element_props(self):
        obj = SignalServiceTranslationEventProps(None, "Test")
        child = obj.createSignalServiceTranslationElementProps("Element1")
        assert isinstance(child, SignalServiceTranslationElementProps)
        assert child.getParent() is obj
        assert obj.getSignalServiceTranslationElementProps() == [child]

    def test_set_safe_translation(self):
        obj = SignalServiceTranslationEventProps(None, "Test")
        safe = True
        assert obj.setSafeTranslation(safe) is obj
        assert obj.getSafeTranslation() is safe
        assert obj.setSafeTranslation(None) is obj
        assert obj.getSafeTranslation() is safe

    def test_set_secure_translation(self):
        obj = SignalServiceTranslationEventProps(None, "Test")
        secure = True
        assert obj.setSecureTranslation(secure) is obj
        assert obj.getSecureTranslation() is secure
        assert obj.setSecureTranslation(None) is obj
        assert obj.getSecureTranslation() is secure

    def test_set_translation_target(self):
        obj = SignalServiceTranslationEventProps(None, "Test")
        iref = VariableDataPrototypeInSystemInstanceRef()
        assert obj.setTranslationTarget(iref) is obj
        assert obj.getTranslationTarget() is iref
        assert obj.setTranslationTarget(None) is obj
        assert obj.getTranslationTarget() is iref
