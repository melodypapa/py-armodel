"""
This module contains comprehensive tests for the Trigger module in SWComponentTemplate.SwcInternalBehavior.
Tests cover all classes and methods in the Trigger.py file to achieve 100% test coverage.
"""

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.Trigger import (
    InternalTriggeringPoint, ExternalTriggeringPointIdent, ExternalTriggeringPoint
)
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR


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
        assert ident.returnValueProvision is None


class TestExternalTriggeringPoint:
    """Test class for ExternalTriggeringPoint class."""
    
    def test_external_triggering_point_initialization(self):
        """Test ExternalTriggeringPoint initialization and methods."""
        ext_trigger_point = ExternalTriggeringPoint()
        
        assert ext_trigger_point.ident is None
        assert ext_trigger_point.trigger is None
        
        # Test ident methods
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        ident = ExternalTriggeringPointIdent(ar_root, "TestIdent")
        ext_trigger_point.setIdent(ident)
        assert ext_trigger_point.getIdent() == ident
        
        # Test trigger methods
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration import Trigger
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        trigger = Trigger(ar_root, "TestTrigger")
        ext_trigger_point.setTrigger(trigger)
        assert ext_trigger_point.getTrigger() == trigger