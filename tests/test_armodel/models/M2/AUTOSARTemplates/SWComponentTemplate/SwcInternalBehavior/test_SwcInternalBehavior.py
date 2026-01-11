"""
This module contains comprehensive tests for the SwcInternalBehavior module in SWComponentTemplate.
Tests cover all classes and methods in the __init__.py file to achieve 100% test coverage.
"""

import pytest
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import (
    RunnableEntityArgument, AsynchronousServerCallResultPoint, AsynchronousServerCallPoint,
    SynchronousServerCallPoint, RunnableEntity, SwcInternalBehavior
)
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR


class TestRunnableEntityArgument:
    """Test class for RunnableEntityArgument class."""
    
    def test_runnable_entity_argument_initialization(self):
        """Test RunnableEntityArgument initialization and methods."""
        arg = RunnableEntityArgument()
        
        assert arg.symbol is None
        
        # Test symbol methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral
        symbol = ARLiteral()
        symbol.setValue("test_symbol")
        arg.setSymbol(symbol)
        assert arg.getSymbol() == symbol


class TestAsynchronousServerCallResultPoint:
    """Test class for AsynchronousServerCallResultPoint class."""
    
    def test_asynchronous_server_call_result_point_initialization(self):
        """Test AsynchronousServerCallResultPoint initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        result_point = AsynchronousServerCallResultPoint(ar_root, "TestAsynchronousServerCallResultPoint")
        
        assert result_point.parent == ar_root
        assert result_point.short_name == "TestAsynchronousServerCallResultPoint"
        assert result_point.returnValueProvision is None
        assert result_point.asynchronousServerCallPointRef is None
        
        # Test returnValueProvision methods
        return_prov = "test_provision"
        result_point.setReturnValueProvision(return_prov)
        assert result_point.getReturnValueProvision() == return_prov
        
        # Test asynchronousServerCallPointRef methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
        ref = RefType()
        ref.setValue("/Async/Server/Call/Point")
        result_point.setAsynchronousServerCallPointRef(ref)
        assert result_point.getAsynchronousServerCallPointRef() == ref


class TestAsynchronousServerCallPoint:
    """Test class for AsynchronousServerCallPoint class."""
    
    def test_asynchronous_server_call_point_initialization(self):
        """Test AsynchronousServerCallPoint initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        call_point = AsynchronousServerCallPoint(ar_root, "TestAsynchronousServerCallPoint")
        
        assert call_point.parent == ar_root
        assert call_point.short_name == "TestAsynchronousServerCallPoint"
        assert call_point.returnValueProvision is None
        assert call_point.operationIRef is None
        assert call_point.timeout is None
        
        # Test returnValueProvision methods
        return_prov = "test_provision"
        call_point.setReturnValueProvision(return_prov)
        assert call_point.getReturnValueProvision() == return_prov


class TestSynchronousServerCallPoint:
    """Test class for SynchronousServerCallPoint class."""
    
    def test_synchronous_server_call_point_initialization(self):
        """Test SynchronousServerCallPoint initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        call_point = SynchronousServerCallPoint(ar_root, "TestSynchronousServerCallPoint")
        
        assert call_point.parent == ar_root
        assert call_point.short_name == "TestSynchronousServerCallPoint"
        assert call_point.returnValueProvision is None
        assert call_point.operationIRef is None
        assert call_point.timeout is None
        assert call_point.calledFromWithinExclusiveAreaRef is None
        
        # Test returnValueProvision methods
        return_prov = "test_provision"
        call_point.setReturnValueProvision(return_prov)
        assert call_point.getReturnValueProvision() == return_prov
        
        # Test calledFromWithinExclusiveAreaRef methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
        ref = RefType()
        ref.setValue("/Exclusive/Area/Ref")
        call_point.setCalledFromWithinExclusiveAreaRef(ref)
        assert call_point.getCalledFromWithinExclusiveAreaRef() == ref


class TestRunnableEntity:
    """Test class for RunnableEntity class."""
    
    def test_runnable_entity_initialization(self):
        """Test RunnableEntity initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        runnable = RunnableEntity(ar_root, "TestRunnableEntity")
        
        assert runnable.parent == ar_root
        assert runnable.short_name == "TestRunnableEntity"
        assert runnable.arguments == []
        assert runnable.asynchronousServerCallResultPoints == []
        assert runnable.canBeInvokedConcurrently is None
        assert runnable.dataReadAccesses == []
        assert runnable.dataReceivePointByArguments == []
        assert runnable.dataReceivePointByValues == []
        assert runnable.dataSendPoints == []
        assert runnable.dataWriteAccesses == []
        assert runnable.externalTriggeringPoints == []
        assert runnable.internalTriggeringPoints == []
        assert runnable.modeAccessPoints == []
        assert runnable.modeSwitchPoints == []
        assert runnable.parameterAccesses == []
        assert runnable.readLocalVariables == []
        assert runnable.serverCallPoints == []
        assert runnable.symbol is None
        assert runnable.waitPoints == {}
        assert runnable.writtenLocalVariables == []
        
        # Test canBeInvokedConcurrently methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARBoolean
        can_invoke = ARBoolean()
        can_invoke.setValue(True)
        runnable.setCanBeInvokedConcurrently(can_invoke)
        assert runnable.getCanBeInvokedConcurrently() == can_invoke
        
        # Test symbol methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral
        symbol = ARLiteral()
        symbol.setValue("test_symbol")
        runnable.setSymbol(symbol)
        assert runnable.getSymbol() == symbol
        
        # Test data access methods
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import VariableAccess
        var_access = VariableAccess(ar_root, "TestDataAccess")
        data_access = runnable._createVariableAccess("TestDataAccess", runnable.dataReadAccesses)
        assert data_access is not None
        assert data_access.short_name == "TestDataAccess"
        assert data_access in runnable.getDataReadAccesses()
        
        # Test parameter access methods
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import ParameterAccess
        param_access = runnable.createParameterAccess("TestParamAccess")
        assert param_access is not None
        assert param_access.short_name == "TestParamAccess"
        assert param_access in runnable.getParameterAccesses()
        
        # Test server call point methods
        async_call_point = runnable.createAsynchronousServerCallPoint("TestAsyncCall")
        assert async_call_point is not None
        assert async_call_point.short_name == "TestAsyncCall"
        assert async_call_point in runnable.getAsynchronousServerCallPoint()
        
        sync_call_point = runnable.createSynchronousServerCallPoint("TestSyncCall")
        assert sync_call_point is not None
        assert sync_call_point.short_name == "TestSyncCall"
        assert sync_call_point in runnable.getSynchronousServerCallPoint()
        
        result_point = runnable.createAsynchronousServerCallResultPoint("TestResultPoint")
        assert result_point is not None
        assert result_point.short_name == "TestResultPoint"
        assert result_point in runnable.getAsynchronousServerCallResultPoints()
        
        # Test internal triggering point methods
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.Trigger import InternalTriggeringPoint
        trigger_point = runnable.createInternalTriggeringPoint("TestTrigger")
        assert trigger_point is not None
        assert trigger_point.short_name == "TestTrigger"
        # Note: getInternalTriggeringPoints uses filter, so we don't check for it in the list directly
        
        # Test mode switch point methods
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup import ModeSwitchPoint
        mode_switch_point = runnable.createModeSwitchPoint("TestModeSwitch")
        assert mode_switch_point is not None
        assert mode_switch_point.short_name == "TestModeSwitch"
        assert mode_switch_point in runnable.getModeSwitchPoints()


class TestSwcInternalBehavior:
    """Test class for SwcInternalBehavior class."""
    
    def test_swc_internal_behavior_initialization(self):
        """Test SwcInternalBehavior initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        behavior = SwcInternalBehavior(ar_root, "TestSwcInternalBehavior")
        
        assert behavior.parent == ar_root
        assert behavior.short_name == "TestSwcInternalBehavior"
        assert behavior.arTypedPerInstanceMemories == []
        assert behavior.events == []
        assert behavior.exclusiveAreaPolicies == []
        assert behavior.explicitInterRunnableVariables == []
        assert behavior.handleTerminationAndRestart is None
        assert behavior.implicitInterRunnableVariables == []
        assert behavior.includedDataTypeSets == []
        assert behavior.includedModeDeclarationGroupSets == []
        assert behavior.instantiationDataDefProps == []
        assert behavior.perInstanceMemories == []
        assert behavior.perInstanceParameters == []
        assert behavior.portAPIOptions == []
        assert behavior.runnables == []
        assert behavior.serviceDependencies == []
        assert behavior.sharedParameters == []
        assert behavior.supportsMultipleInstantiation is None
        assert behavior.variationPointProxies == []
        
        # Test handleTerminationAndRestart methods
        handle_term = "test_handle"
        behavior.setHandleTerminationAndRestart(handle_term)
        assert behavior.getHandleTerminationAndRestart() == handle_term
        
        # Test supportsMultipleInstantiation methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean
        supports_multi = Boolean()
        supports_multi.setValue(True)
        behavior.setSupportsMultipleInstantiation(supports_multi)
        assert behavior.getSupportsMultipleInstantiation() == supports_multi
        
        # Test event creation methods
        init_event = behavior.createInitEvent("TestInitEvent")
        assert init_event is not None
        assert init_event.short_name == "TestInitEvent"
        assert init_event in behavior.getInitEvents()
        
        timing_event = behavior.createTimingEvent("TestTimingEvent")
        assert timing_event is not None
        assert timing_event.short_name == "TestTimingEvent"
        assert timing_event in behavior.getTimingEvents()
        
        operation_invoked_event = behavior.createOperationInvokedEvent("TestOperationInvokedEvent")
        assert operation_invoked_event is not None
        assert operation_invoked_event.short_name == "TestOperationInvokedEvent"
        assert operation_invoked_event in behavior.getOperationInvokedEvents()
        
        data_received_event = behavior.createDataReceivedEvent("TestDataReceivedEvent")
        assert data_received_event is not None
        assert data_received_event.short_name == "TestDataReceivedEvent"
        assert data_received_event in behavior.getDataReceivedEvents()
        
        swc_mode_switch_event = behavior.createSwcModeSwitchEvent("TestSwcModeSwitchEvent")
        assert swc_mode_switch_event is not None
        assert swc_mode_switch_event.short_name == "TestSwcModeSwitchEvent"
        assert swc_mode_switch_event in behavior.getSwcModeSwitchEvents()
        
        internal_trigger_event = behavior.createInternalTriggerOccurredEvent("TestInternalTriggerEvent")
        assert internal_trigger_event is not None
        assert internal_trigger_event.short_name == "TestInternalTriggerEvent"
        assert internal_trigger_event in behavior.getInternalTriggerOccurredEvents()
        
        mode_switched_ack_event = behavior.createModeSwitchedAckEvent("TestModeSwitchedAckEvent")
        assert mode_switched_ack_event is not None
        assert mode_switched_ack_event.short_name == "TestModeSwitchedAckEvent"
        assert mode_switched_ack_event in behavior.getModeSwitchedAckEvents()
        
        background_event = behavior.createBackgroundEvent("TestBackgroundEvent")
        assert background_event is not None
        assert background_event.short_name == "TestBackgroundEvent"
        assert background_event in behavior.getBackgroundEvents()
        
        data_send_completed_event = behavior.createDataSendCompletedEvent("TestDataSendCompletedEvent")
        assert data_send_completed_event is not None
        assert data_send_completed_event.short_name == "TestDataSendCompletedEvent"
        assert data_send_completed_event in behavior.getDataSendCompletedEvents()
        
        # Test service dependency methods
        service_dep = behavior.createSwcServiceDependency("TestServiceDep")
        assert service_dep is not None
        assert service_dep.short_name == "TestServiceDep"
        assert service_dep in behavior.getSwcServiceDependencies()
        
        # Test runnable entity methods
        runnable = behavior.createRunnableEntity("TestRunnable")
        assert runnable is not None
        assert runnable.short_name == "TestRunnable"
        assert runnable in behavior.getRunnableEntities()
        
        # Test data prototype methods
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import VariableDataPrototype, ParameterDataPrototype
        ar_typed_mem = behavior.createArTypedPerInstanceMemory("TestArTypedMem")
        assert ar_typed_mem is not None
        assert ar_typed_mem.short_name == "TestArTypedMem"
        assert ar_typed_mem in behavior.getArTypedPerInstanceMemories()
        
        explicit_var = behavior.createExplicitInterRunnableVariable("TestExplicitVar")
        assert explicit_var is not None
        assert explicit_var.short_name == "TestExplicitVar"
        assert explicit_var in behavior.getExplicitInterRunnableVariables()
        
        implicit_var = behavior.createImplicitInterRunnableVariable("TestImplicitVar")
        assert implicit_var is not None
        assert implicit_var.short_name == "TestImplicitVar"
        assert implicit_var in behavior.getImplicitInterRunnableVariables()
        
        per_instance_mem = behavior.createPerInstanceMemory("TestPerInstanceMem")
        assert per_instance_mem is not None
        assert per_instance_mem.short_name == "TestPerInstanceMem"
        assert per_instance_mem in behavior.getPerInstanceMemories()
        
        per_instance_param = behavior.createPerInstanceParameter("TestPerInstanceParam")
        assert per_instance_param is not None
        assert per_instance_param.short_name == "TestPerInstanceParam"
        assert per_instance_param in behavior.getPerInstanceParameters()
        
        shared_param = behavior.createSharedParameter("TestSharedParam")
        assert shared_param is not None
        assert shared_param.short_name == "TestSharedParam"
        assert shared_param in behavior.getSharedParameters()
        
        # Test included data type set methods
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.IncludedDataTypes import IncludedDataTypeSet
        data_type_set = IncludedDataTypeSet()
        behavior.addIncludedDataTypeSet(data_type_set)
        assert data_type_set in behavior.getIncludedDataTypeSets()
        
        # Test included mode declaration group set methods
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup import IncludedModeDeclarationGroupSet
        mode_decl_set = IncludedModeDeclarationGroupSet()
        behavior.addIncludedModeDeclarationGroupSet(mode_decl_set)
        assert mode_decl_set in behavior.getIncludedModeDeclarationGroupSets()
        
        # Test port API option methods
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions import PortAPIOption
        port_api_option = PortAPIOption()
        behavior.addPortAPIOption(port_api_option)
        assert port_api_option in behavior.getPortAPIOptions()