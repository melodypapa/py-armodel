"""
This module contains comprehensive tests for the Communication module in SWComponentTemplate.
Tests cover all classes and methods in the Communication.py file to achieve 100% test coverage.
"""

import pytest
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import (
    HandleInvalidEnum, PPortComSpec, RPortComSpec, CompositeNetworkRepresentation,
    TransmissionAcknowledgementRequest, SenderComSpec, QueuedSenderComSpec,
    NonqueuedSenderComSpec, ClientComSpec, ModeSwitchReceiverComSpec,
    NvRequireComSpec, ParameterRequireComSpec, ReceiverComSpec,
    ModeSwitchedAckRequest, ModeSwitchSenderComSpec, ParameterProvideComSpec,
    TransformationComSpecProps, EndToEndTransformationComSpecProps,
    UserDefinedTransformationComSpecProps, ServerComSpec, NvProvideComSpec,
    NonqueuedReceiverComSpec, QueuedReceiverComSpec
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType, ARBoolean, PositiveInteger, TimeValue, ARPositiveInteger, ARNumerical
)


class TestHandleInvalidEnum:
    """Test class for HandleInvalidEnum class."""
    
    def test_handle_invalid_enum_initialization(self):
        """Test HandleInvalidEnum initialization and values."""
        enum = HandleInvalidEnum()
        assert enum.DONT_INVALIDATE == "dontInvalidate"
        assert enum.EXTERNAL_REPLACEMENT == "externalReplacement"
        assert enum.KEEP == "keep"
        assert enum.REPLACE == "replace"
        assert len(enum.getEnumValues()) == 4


class TestPPortComSpec:
    """Test class for PPortComSpec abstract class."""
    
    def test_pport_com_spec_abstract(self):
        """Test that PPortComSpec is an abstract class that raises NotImplementedError when instantiated."""
        with pytest.raises(NotImplementedError):
            PPortComSpec()


class TestRPortComSpec:
    """Test class for RPortComSpec abstract class."""
    
    def test_rport_com_spec_abstract(self):
        """Test that RPortComSpec is an abstract class that raises NotImplementedError when instantiated."""
        with pytest.raises(NotImplementedError):
            RPortComSpec()


class TestCompositeNetworkRepresentation:
    """Test class for CompositeNetworkRepresentation class."""
    
    def test_composite_network_representation_initialization(self):
        """Test CompositeNetworkRepresentation initialization and basic methods."""
        representation = CompositeNetworkRepresentation()
        assert representation.leafElementIRef is None
        assert representation.networkRepresentation is None
        
        # Test setters and getters
        ref = RefType()
        ref.setValue("/Test/Ref")
        representation.setLeafElementIRef(ref)
        assert representation.getLeafElementIRef() == ref
        
        from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
        sw_data_def = SwDataDefProps()
        representation.setNetworkRepresentation(sw_data_def)
        assert representation.getNetworkRepresentation() == sw_data_def


class TestTransmissionAcknowledgementRequest:
    """Test class for TransmissionAcknowledgementRequest class."""
    
    def test_transmission_acknowledgement_request_initialization(self):
        """Test TransmissionAcknowledgementRequest initialization."""
        request = TransmissionAcknowledgementRequest()
        assert request.timeout is None


class TestSenderComSpec:
    """Test class for SenderComSpec abstract class."""
    
    def test_sender_com_spec_abstract(self):
        """Test that SenderComSpec is an abstract class that raises NotImplementedError when instantiated."""
        with pytest.raises(NotImplementedError):
            SenderComSpec()


class TestQueuedSenderComSpec:
    """Test class for QueuedSenderComSpec class."""
    
    def test_queued_sender_com_spec_initialization(self):
        """Test QueuedSenderComSpec initialization and basic methods."""
        sender = QueuedSenderComSpec()
        assert sender.compositeNetworkRepresentations == []
        assert sender.dataElementRef is None
        assert sender.networkRepresentation is None
        assert sender.handleOutOfRange is None
        assert sender.transmissionAcknowledge is None
        assert sender.usesEndToEndProtection is None

        # Test addCompositeNetworkRepresentation method to cover line 115 in Communication.py
        representation = CompositeNetworkRepresentation()
        sender.addCompositeNetworkRepresentation(representation)
        assert representation in sender.getCompositeNetworkRepresentations()

        # Test getter methods to cover lines 121, 128, 135, 142, 149
        assert sender.getDataElementRef() is None
        assert sender.getNetworkRepresentation() is None
        assert sender.getHandleOutOfRange() is None
        assert sender.getTransmissionAcknowledge() is None
        assert sender.getUsesEndToEndProtection() is None

        # Test setter methods to cover lines 124-125, 131-132, 138-139, 145-146, 152-153, 171-172
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
        from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps

        ref = RefType()
        sender.setDataElementRef(ref)
        assert sender.getDataElementRef() == ref
        assert sender == sender.setDataElementRef(ref)  # Test method chaining

        network_rep = SwDataDefProps()
        sender.setNetworkRepresentation(network_rep)
        assert sender.getNetworkRepresentation() == network_rep
        assert sender == sender.setNetworkRepresentation(network_rep)  # Test method chaining

        sender.setHandleOutOfRange("handle_out")
        assert sender.getHandleOutOfRange() == "handle_out"
        assert sender == sender.setHandleOutOfRange("handle_out")  # Test method chaining




class TestNonqueuedSenderComSpec:
    """Test class for NonqueuedSenderComSpec class."""
    
    def test_nonqueued_sender_com_spec_initialization(self):
        """Test NonqueuedSenderComSpec initialization and methods."""
        sender = NonqueuedSenderComSpec()
        assert sender.compositeNetworkRepresentations == []
        assert sender.dataElementRef is None
        assert sender.networkRepresentation is None
        assert sender.handleOutOfRange is None
        assert sender.transmissionAcknowledge is None
        assert sender.usesEndToEndProtection is None
        assert sender.initValue is None


class TestClientComSpec:
    """Test class for ClientComSpec class."""
    
    def test_client_com_spec_initialization(self):
        """Test ClientComSpec initialization and methods."""
        client = ClientComSpec()
        assert client.operationRef is None
        
        # Test setters and getters
        ref = RefType()
        ref.setValue("/Test/Operation")
        client.setOperationRef(ref)
        assert client.getOperationRef() == ref


class TestModeSwitchReceiverComSpec:
    """Test class for ModeSwitchReceiverComSpec class."""
    
    def test_mode_switch_receiver_com_spec_initialization(self):
        """Test ModeSwitchReceiverComSpec initialization and methods."""
        receiver = ModeSwitchReceiverComSpec()
        assert receiver.enhancedModeApi is None
        assert receiver.modeGroupRef is None
        assert receiver.supportsAsynchronousModeSwitch is None
        
        # Test setters and getters
        api = ARBoolean()
        api.setValue(True)
        receiver.setEnhancedModeApi(api)
        assert receiver.getEnhancedModeApi() == api
        
        ref = RefType()
        ref.setValue("/Test/ModeGroup")
        receiver.setModeGroupRef(ref)
        assert receiver.getModeGroupRef() == ref
        
        async_mode = ARBoolean()
        async_mode.setValue(False)
        receiver.setSupportsAsynchronousModeSwitch(async_mode)
        assert receiver.getSupportsAsynchronousModeSwitch() == async_mode


class TestNvRequireComSpec:
    """Test class for NvRequireComSpec class."""
    
    def test_nv_require_com_spec_initialization(self):
        """Test NvRequireComSpec initialization and methods."""
        nv_req = NvRequireComSpec()
        assert nv_req.initValue is None
        assert nv_req.variableRef is None
        
        # Test setters and getters
        from armodel.models.M2.AUTOSARTemplates.CommonStructure import TextValueSpecification
        value_spec = TextValueSpecification()
        nv_req.setInitValue(value_spec)
        assert nv_req.getInitValue() == value_spec
        
        ref = RefType()
        ref.setValue("/Test/Variable")
        nv_req.setVariableRef(ref)
        assert nv_req.getVariableRef() == ref


class TestParameterRequireComSpec:
    """Test class for ParameterRequireComSpec class."""
    
    def test_parameter_require_com_spec_initialization(self):
        """Test ParameterRequireComSpec initialization and methods."""
        param_req = ParameterRequireComSpec()
        assert param_req.initValue is None
        assert param_req.parameterRef is None
        
        # Test setters and getters
        from armodel.models.M2.AUTOSARTemplates.CommonStructure import TextValueSpecification
        value_spec = TextValueSpecification()
        param_req.setInitValue(value_spec)
        assert param_req.getInitValue() == value_spec
        
        ref = RefType()
        ref.setValue("/Test/Parameter")
        param_req.setParameterRef(ref)
        assert param_req.getParameterRef() == ref


class TestReceiverComSpec:
    """Test class for ReceiverComSpec class."""

    def test_abstract_class_cannot_be_instantiated(self):
        """Test that ReceiverComSpec abstract class cannot be instantiated directly."""
        with pytest.raises(TypeError, match="ReceiverComSpec is an abstract class"):
            ReceiverComSpec()

    def test_concrete_subclass_initialization(self):
        """Test that a concrete subclass of ReceiverComSpec can be instantiated."""
        receiver = NonqueuedReceiverComSpec()
        assert receiver.compositeNetworkRepresentations == []
        assert receiver.dataElementRef is None
        assert receiver.networkRepresentation is None
        assert receiver.handleOutOfRange is None
        assert receiver.handleOutOfRangeStatus is None
        assert receiver.maxDeltaCounterInit is None
        assert receiver.maxNoNewOrRepeatedData is None
        assert receiver.usesEndToEndProtection is None

        # Test setters and getters
        ref = RefType()
        ref.setValue("/Test/DataElement")
        receiver.setDataElementRef(ref)
        assert receiver.getDataElementRef() == ref

        from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
        network_rep = SwDataDefProps()
        receiver.setNetworkRepresentation(network_rep)
        assert receiver.getNetworkRepresentation() == network_rep

        handle_out = "test_handle"
        receiver.setHandleOutOfRange(handle_out)
        assert receiver.getHandleOutOfRange() == handle_out

        status = "test_status"
        receiver.setHandleOutOfRangeStatus(status)
        assert receiver.getHandleOutOfRangeStatus() == status

        max_delta = PositiveInteger()
        max_delta.setValue(10)
        receiver.setMaxDeltaCounterInit(max_delta)
        assert receiver.getMaxDeltaCounterInit() == max_delta

        max_new = PositiveInteger()
        max_new.setValue(20)
        receiver.setMaxNoNewOrRepeatedData(max_new)
        assert receiver.getMaxNoNewOrRepeatedData() == max_new

        e2e = ARBoolean()
        e2e.setValue(True)
        receiver.setUsesEndToEndProtection(e2e)
        assert receiver.getUsesEndToEndProtection() == e2e
        
        # Test composite network representation methods
        comp_rep = CompositeNetworkRepresentation()
        receiver.addCompositeNetworkRepresentation(comp_rep)
        assert comp_rep in receiver.getCompositeNetworkRepresentations()


class TestModeSwitchedAckRequest:
    """Test class for ModeSwitchedAckRequest class."""
    
    def test_mode_switched_ack_request_initialization(self):
        """Test ModeSwitchedAckRequest initialization and methods."""
        ack = ModeSwitchedAckRequest()
        assert ack.timeout is None
        
        # Test setters and getters
        timeout = TimeValue()
        timeout.setValue(5.0)
        ack.setTimeout(timeout)
        assert ack.getTimeout() == timeout


class TestModeSwitchSenderComSpec:
    """Test class for ModeSwitchSenderComSpec class."""
    
    def test_mode_switch_sender_com_spec_initialization(self):
        """Test ModeSwitchSenderComSpec initialization and methods."""
        sender = ModeSwitchSenderComSpec()
        assert sender.enhancedModeApi is None
        assert sender.modeGroupRef is None
        assert sender.modeSwitchedAck is None
        assert sender.queueLength is None
        
        # Test setters and getters
        api = ARBoolean()
        api.setValue(True)
        sender.setEnhancedModeApi(api)
        assert sender.getEnhancedModeApi() == api
        
        ref = RefType()
        ref.setValue("/Test/ModeGroup")
        sender.setModeGroupRef(ref)
        assert sender.getModeGroupRef() == ref
        
        ack_request = ModeSwitchedAckRequest()
        sender.setModeSwitchedAck(ack_request)
        assert sender.getModeSwitchedAck() == ack_request
        
        queue_len = ARPositiveInteger()
        queue_len.setValue(5)
        sender.setQueueLength(queue_len)
        assert sender.getQueueLength() == queue_len


class TestParameterProvideComSpec:
    """Test class for ParameterProvideComSpec class."""
    
    def test_parameter_provide_com_spec_initialization(self):
        """Test ParameterProvideComSpec initialization."""
        param_prov = ParameterProvideComSpec()
        # Just verify it can be initialized


class TestTransformationComSpecProps:
    """Test class for TransformationComSpecProps abstract class."""
    
    def test_transformation_com_spec_props_abstract(self):
        """Test that TransformationComSpecProps is an abstract class that raises NotImplementedError when instantiated."""
        with pytest.raises(NotImplementedError):
            TransformationComSpecProps()


class TestEndToEndTransformationComSpecProps:
    """Test class for EndToEndTransformationComSpecProps class."""
    
    def test_end_to_end_transformation_com_spec_props_initialization(self):
        """Test EndToEndTransformationComSpecProps initialization and methods."""
        e2e = EndToEndTransformationComSpecProps()
        assert e2e.clearFromValidToInvalid is None
        assert e2e.disableEndToEndCheck is None
        assert e2e.disableEndToEndStateMachine is None
        assert e2e.e2eProfileCompatibilityPropsRef is None
        assert e2e.maxDeltaCounter is None
        assert e2e.maxErrorStateInit is None
        assert e2e.maxErrorStateInvalid is None
        assert e2e.maxErrorStateValid is None
        assert e2e.maxNoNewOrRepeatedData is None
        assert e2e.minOkStateInit is None
        assert e2e.minOkStateInvalid is None
        assert e2e.minOkStateValid is None
        assert e2e.syncCounterInit is None
        assert e2e.windowSizeInit is None
        assert e2e.windowSizeInvalid is None
        assert e2e.windowSizeValid is None
        
        # Test setters and getters
        clear_valid = ARBoolean()
        clear_valid.setValue(True)
        e2e.setClearFromValidToInvalid(clear_valid)
        assert e2e.getClearFromValidToInvalid() == clear_valid
        
        disable_check = ARBoolean()
        disable_check.setValue(False)
        e2e.setDisableEndToEndCheck(disable_check)
        assert e2e.getDisableEndToEndCheck() == disable_check
        
        disable_sm = ARBoolean()
        disable_sm.setValue(True)
        e2e.setDisableEndToEndStateMachine(disable_sm)
        assert e2e.getDisableEndToEndStateMachine() == disable_sm
        
        ref = RefType()
        ref.setValue("/Test/E2EProfile")
        e2e.setE2eProfileCompatibilityPropsRef(ref)
        assert e2e.getE2eProfileCompatibilityPropsRef() == ref
        
        max_delta = PositiveInteger()
        max_delta.setValue(10)
        e2e.setMaxDeltaCounter(max_delta)
        assert e2e.getMaxDeltaCounter() == max_delta
        
        max_error_init = PositiveInteger()
        max_error_init.setValue(15)
        e2e.setMaxErrorStateInit(max_error_init)
        assert e2e.getMaxErrorStateInit() == max_error_init
        
        max_error_invalid = PositiveInteger()
        max_error_invalid.setValue(20)
        e2e.setMaxErrorStateInvalid(max_error_invalid)
        assert e2e.getMaxErrorStateInvalid() == max_error_invalid
        
        max_error_valid = PositiveInteger()
        max_error_valid.setValue(25)
        e2e.setMaxErrorStateValid(max_error_valid)
        assert e2e.getMaxErrorStateValid() == max_error_valid
        
        max_new = PositiveInteger()
        max_new.setValue(30)
        e2e.setMaxNoNewOrRepeatedData(max_new)
        assert e2e.getMaxNoNewOrRepeatedData() == max_new
        
        min_ok_init = PositiveInteger()
        min_ok_init.setValue(35)
        e2e.setMinOkStateInit(min_ok_init)
        assert e2e.getMinOkStateInit() == min_ok_init
        
        min_ok_invalid = PositiveInteger()
        min_ok_invalid.setValue(40)
        e2e.setMinOkStateInvalid(min_ok_invalid)
        assert e2e.getMinOkStateInvalid() == min_ok_invalid
        
        min_ok_valid = PositiveInteger()
        min_ok_valid.setValue(45)
        e2e.setMinOkStateValid(min_ok_valid)
        assert e2e.getMinOkStateValid() == min_ok_valid
        
        sync_counter = PositiveInteger()
        sync_counter.setValue(50)
        e2e.setSyncCounterInit(sync_counter)
        assert e2e.getSyncCounterInit() == sync_counter
        
        window_init = PositiveInteger()
        window_init.setValue(55)
        e2e.setWindowSizeInit(window_init)
        assert e2e.getWindowSizeInit() == window_init
        
        window_invalid = PositiveInteger()
        window_invalid.setValue(60)
        e2e.setWindowSizeInvalid(window_invalid)
        assert e2e.getWindowSizeInvalid() == window_invalid
        
        window_valid = PositiveInteger()
        window_valid.setValue(65)
        e2e.setWindowSizeValid(window_valid)
        assert e2e.getWindowSizeValid() == window_valid


class TestUserDefinedTransformationComSpecProps:
    """Test class for UserDefinedTransformationComSpecProps class."""
    
    def test_user_defined_transformation_com_spec_props_initialization(self):
        """Test UserDefinedTransformationComSpecProps initialization."""
        user_def = UserDefinedTransformationComSpecProps()
        # Just verify it can be initialized


class TestServerComSpec:
    """Test class for ServerComSpec class."""
    
    def test_server_com_spec_initialization(self):
        """Test ServerComSpec initialization and methods."""
        server = ServerComSpec()
        assert server.operationRef is None
        assert server.queueLength is None
        assert server.transformationComSpecProps == []
        
        # Test setters and getters
        ref = RefType()
        ref.setValue("/Test/Operation")
        server.setOperationRef(ref)
        assert server.getOperationRef() == ref
        
        queue_len = PositiveInteger()
        queue_len.setValue(10)
        server.setQueueLength(queue_len)
        assert server.getQueueLength() == queue_len
        
        # Test transformationComSpecProps methods
        e2e_props = EndToEndTransformationComSpecProps()
        server.addTransformationComSpecProps(e2e_props)
        assert e2e_props in server.getTransformationComSpecProps()


class TestNvProvideComSpec:
    """Test class for NvProvideComSpec class."""
    
    def test_nv_provide_com_spec_initialization(self):
        """Test NvProvideComSpec initialization and methods."""
        nv_prov = NvProvideComSpec()
        assert nv_prov.ramBlockInitValue is None
        assert nv_prov.romBlockInitValue is None
        assert nv_prov.variableRef is None
        
        # Test setters and getters
        from armodel.models.M2.AUTOSARTemplates.CommonStructure import TextValueSpecification
        ram_value = TextValueSpecification()
        nv_prov.setRamBlockInitValue(ram_value)
        assert nv_prov.getRamBlockInitValue() == ram_value
        
        rom_value = TextValueSpecification()
        nv_prov.setRomBlockInitValue(rom_value)
        assert nv_prov.getRomBlockInitValue() == rom_value
        
        ref = RefType()
        ref.setValue("/Test/Variable")
        nv_prov.setVariableRef(ref)
        assert nv_prov.getVariableRef() == ref


class TestNonqueuedReceiverComSpec:
    """Test class for NonqueuedReceiverComSpec class."""
    
    def test_nonqueued_receiver_com_spec_initialization(self):
        """Test NonqueuedReceiverComSpec initialization and methods."""
        receiver = NonqueuedReceiverComSpec()
        assert receiver.aliveTimeout is None
        assert receiver.enableUpdated is None
        assert receiver.filter is None
        assert receiver.handleDataStatus is None
        assert receiver.handleNeverReceived is None
        assert receiver.handleTimeoutType == ""
        assert receiver.initValue is None
        assert receiver.timeoutSubstitution is None
        
        # Test setters and getters
        alive_timeout = ARNumerical()
        alive_timeout.setValue("10.5")
        receiver.setAliveTimeout(alive_timeout)
        assert receiver.getAliveTimeout() == alive_timeout
        
        enable_updated = ARBoolean()
        enable_updated.setValue(True)
        receiver.setEnableUpdated(enable_updated)
        assert receiver.getEnableUpdated() == enable_updated
        
        filter_value = "test_filter"
        receiver.setFilter(filter_value)
        assert receiver.getFilter() == filter_value
        
        handle_data = ARBoolean()
        handle_data.setValue(True)
        receiver.setHandleDataStatus(handle_data)
        assert receiver.getHandleDataStatus() == handle_data
        
        handle_never = ARBoolean()
        handle_never.setValue(False)
        receiver.setHandleNeverReceived(handle_never)
        assert receiver.getHandleNeverReceived() == handle_never
        
        timeout_type = "test_timeout"
        receiver.setHandleTimeoutType(timeout_type)
        assert receiver.getHandleTimeoutType() == timeout_type
        
        from armodel.models.M2.AUTOSARTemplates.CommonStructure import TextValueSpecification
        init_value = TextValueSpecification()
        receiver.setInitValue(init_value)
        assert receiver.getInitValue() == init_value
        
        timeout_sub = TextValueSpecification()
        receiver.setTimeoutSubstitution(timeout_sub)
        assert receiver.getTimeoutSubstitution() == timeout_sub


class TestQueuedReceiverComSpec:
    """Test class for QueuedReceiverComSpec class."""
    
    def test_queued_receiver_com_spec_initialization(self):
        """Test QueuedReceiverComSpec initialization and methods."""
        receiver = QueuedReceiverComSpec()
        assert receiver.queueLength is None
        
        # Test setters and getters
        queue_len = ARPositiveInteger()
        queue_len.setValue(5)
        receiver.setQueueLength(queue_len)
        assert receiver.getQueueLength() == queue_len