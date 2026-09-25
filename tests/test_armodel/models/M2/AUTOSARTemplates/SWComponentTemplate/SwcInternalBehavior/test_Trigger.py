"""
This module contains comprehensive tests for the Trigger module in SWComponentTemplate.SwcInternalBehavior.
Tests cover all classes and methods in the Trigger.py file to achieve 100% test coverage.
"""

import typing

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import PTriggerInAtomicSwcTypeInstanceRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount import RteApiReturnValueProvisionEnum
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.Trigger import ExternalTriggeringPoint, ExternalTriggeringPointIdent, InternalTriggeringPoint
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwImplPolicyEnum


class TestInternalTriggeringPoint:
    """Test class for InternalTriggeringPoint class."""

    def test_initialization(self):
        """Test InternalTriggeringPoint initialization defaults."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        trigger_point = InternalTriggeringPoint(ar_root, "TestInternalTriggeringPoint")

        assert trigger_point.parent == ar_root
        assert trigger_point.short_name == "TestInternalTriggeringPoint"
        assert trigger_point.returnValueProvision is None
        assert trigger_point.swImplPolicy is None

    def test_get_set_returnValueProvision(self):
        """Test the inherited AbstractAccessPoint returnValueProvision accessor."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        trigger_point = InternalTriggeringPoint(ar_root, "TestInternalTriggeringPoint")

        provision = RteApiReturnValueProvisionEnum().setValue(RteApiReturnValueProvisionEnum.RETURN_VALUE_PROVIDED)
        assert trigger_point.setReturnValueProvision(provision) is trigger_point
        assert trigger_point.getReturnValueProvision() is provision

        assert trigger_point.setReturnValueProvision(None) is trigger_point
        assert trigger_point.getReturnValueProvision() is provision

    def test_get_set_swImplPolicy(self):
        """Test swImplPolicy round-trip, None no-op and type hints."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        trigger_point = InternalTriggeringPoint(ar_root, "TestInternalTriggeringPoint")

        policy = SwImplPolicyEnum().setValue(SwImplPolicyEnum.QUEUED)
        assert trigger_point.setSwImplPolicy(policy) is trigger_point
        assert trigger_point.getSwImplPolicy() is policy
        assert trigger_point.getSwImplPolicy().getValue() == "queued"

        assert trigger_point.setSwImplPolicy(None) is trigger_point
        assert trigger_point.getSwImplPolicy() is policy

        hints = typing.get_type_hints(InternalTriggeringPoint.setSwImplPolicy)
        assert hints.get("value") == typing.Optional[SwImplPolicyEnum]
        assert hints.get("return") is InternalTriggeringPoint
        assert typing.get_type_hints(InternalTriggeringPoint.getSwImplPolicy).get("return") == typing.Optional[SwImplPolicyEnum]


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
    ref = RefType()
    ref.setValue(value)
    return ref
