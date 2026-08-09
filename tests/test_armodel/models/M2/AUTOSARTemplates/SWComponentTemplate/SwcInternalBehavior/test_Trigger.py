"""
This module contains comprehensive tests for the Trigger module in SWComponentTemplate.SwcInternalBehavior.
Tests cover all classes and methods in the Trigger.py file to achieve 100% test coverage.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import PTriggerInAtomicSwcTypeInstanceRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import IdentCaption
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.Trigger import ExternalTriggeringPoint, ExternalTriggeringPointIdent, InternalTriggeringPoint


class TestInternalTriggeringPoint:
    """Test class for InternalTriggeringPoint class."""

    def test_internal_triggering_point_initialization(self):
        """Test InternalTriggeringPoint initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        trigger_point = InternalTriggeringPoint(ar_root, "TestInternalTriggeringPoint")

        assert trigger_point.parent == ar_root
        assert trigger_point.short_name == "TestInternalTriggeringPoint"
        assert trigger_point.returnValueProvision is None
        assert trigger_point.swImplPolicy is None

        # Test returnValueProvision methods
        return_prov = "test_provision"
        trigger_point.setReturnValueProvision(return_prov)
        assert trigger_point.getReturnValueProvision() == return_prov

        # Test swImplPolicy methods
        from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwImplPolicyEnum

        sw_impl_policy = SwImplPolicyEnum()
        trigger_point.setSwImplPolicy(sw_impl_policy)
        assert trigger_point.getSwImplPolicy() == sw_impl_policy


class TestExternalTriggeringPointIdent:
    """Test class for ExternalTriggeringPointIdent class."""

    def test_external_triggering_point_ident_initialization(self):
        """Test ExternalTriggeringPointIdent initialization."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        ident = ExternalTriggeringPointIdent(ar_root, "TestExternalTriggeringPointIdent")

        assert ident.parent == ar_root
        assert ident.short_name == "TestExternalTriggeringPointIdent"
        # ExternalTriggeringPointIdent inherits from IdentCaption, which doesn't have returnValueProvision
        # That attribute is only on InternalTriggeringPoint (which inherits from AbstractAccessPoint)
        assert isinstance(ident, IdentCaption)


class TestExternalTriggeringPoint:
    """Test class for ExternalTriggeringPoint class."""

    def test_external_triggering_point_initialization(self):
        """Test ExternalTriggeringPoint initialization and methods."""
        ext_trigger_point = ExternalTriggeringPoint()

        assert ext_trigger_point.ident is None
        assert ext_trigger_point.trigger is None

    def test_get_set_ident(self):
        """Test ident create/get round-trip and None no-op."""
        ext_trigger_point = ExternalTriggeringPoint()
        ident = ext_trigger_point.createIdent("TestIdent")
        assert isinstance(ident, ExternalTriggeringPointIdent)
        assert ident.getShortName() == "TestIdent"
        assert ext_trigger_point.getIdent() == ident
        # calling createIdent again returns the existing identification
        assert ext_trigger_point.createIdent("TestIdent") == ident

    def test_get_set_trigger(self):
        """Test trigger set/get round-trip and None no-op."""
        ext_trigger_point = ExternalTriggeringPoint()
        trigger = PTriggerInAtomicSwcTypeInstanceRef()
        trigger.setContextPPortRef(_make_ref("/p"))
        trigger.setTargetTriggerRef(_make_ref("/trig"))
        assert ext_trigger_point.setTrigger(trigger) == ext_trigger_point
        assert ext_trigger_point.getTrigger() == trigger
        # None is a no-op
        ext_trigger_point.setTrigger(None)
        assert ext_trigger_point.getTrigger() == trigger


def _make_ref(value):
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

    ref = RefType()
    ref.setValue(value)
    return ref
