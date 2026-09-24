"""
This module contains comprehensive tests for the Communication module in SWComponentTemplate.
Tests cover all classes and methods in the Communication.py file to achieve 100% test coverage.
"""

import inspect

import pytest

from armodel.models.M2.AUTOSARTemplates.CommonStructure import TextValueSpecification
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Filter import DataFilter
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import (
    ClientComSpec,
    CompositeNetworkRepresentation,
    HandleInvalidEnum,
    HandleOutOfRangeEnum,
    HandleOutOfRangeStatusEnum,
    HandleTimeoutEnum,
    ModeSwitchedAckRequest,
    ModeSwitchReceiverComSpec,
    ModeSwitchSenderComSpec,
    NonqueuedReceiverComSpec,
    NonqueuedSenderComSpec,
    NvProvideComSpec,
    NvRequireComSpec,
    ParameterProvideComSpec,
    ParameterRequireComSpec,
    PPortComSpec,
    QueuedReceiverComSpec,
    QueuedSenderComSpec,
    ReceiverComSpec,
    ReceptionComSpecProps,
    RPortComSpec,
    SenderComSpec,
    ServerComSpec,
    TransformationComSpecProps,
    TransmissionAcknowledgementRequest,
    TransmissionComSpecProps,
    TransmissionModeDefinitionEnum,
    UserDefinedTransformationComSpecProps,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.InstanceRefs import ApplicationCompositeElementInPortInterfaceInstanceRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import EndToEndTransformationComSpecProps
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps


class TestHandleInvalidEnum:
    """Test class for HandleInvalidEnum class."""

    def test_handle_invalid_enum_initialization(self):
        """Test HandleInvalidEnum initialization and values."""
        enum = HandleInvalidEnum()
        assert enum.DONT_INVALIDATE == "dontInvalidate"
        assert enum.EXTERNAL_REPLACEMENT == "externalReplacement"
        assert enum.KEEP == "keep"
        assert enum.REPLACE == "replace"
        assert enum.getEnumValues() == (
            HandleInvalidEnum.DONT_INVALIDATE,
            HandleInvalidEnum.EXTERNAL_REPLACEMENT,
            HandleInvalidEnum.KEEP,
            HandleInvalidEnum.REPLACE,
        )

    def test_handle_invalid_enum_spec_note(self):
        """Test the Table 4.3 class note."""
        assert HandleInvalidEnum.__doc__.strip() == "Strategies of handling the reception of invalidValue."


class TestPPortComSpec:
    """Test class for PPortComSpec abstract class."""

    def test_pport_com_spec_abstract(self):
        """Test that PPortComSpec is an abstract class that raises NotImplementedError when instantiated."""
        with pytest.raises(TypeError):
            PPortComSpec()


class TestRPortComSpec:
    """Test class for RPortComSpec abstract class."""

    def test_rport_com_spec_abstract(self):
        """Test that RPortComSpec is an abstract class that raises NotImplementedError when instantiated."""
        with pytest.raises(TypeError):
            RPortComSpec()


class TestCompositeNetworkRepresentation:
    """Test class for CompositeNetworkRepresentation class (Table 4.74)."""

    def test_spec_notes_are_verbatim(self):
        """Class and member docstrings must be the Table 4.74 Notes copied verbatim."""
        assert CompositeNetworkRepresentation.__doc__.strip() == "This meta-class is used to define the network representation of leaf elements of composite application data types."
        leaf_element_note = "This represents that leaf element of an application composite data type. " "InstanceRef implemented by: ApplicationCompositeElementInPortInterfaceInstanceRef"
        assert CompositeNetworkRepresentation.getLeafElementIRef.__doc__.strip() == leaf_element_note
        assert CompositeNetworkRepresentation.setLeafElementIRef.__doc__.strip() == leaf_element_note + ". A None value is a no-op and does not overwrite an existing leafElementIRef."
        network_representation_note = (
            "The SwDataDefProps owned by the CompositeNetworkRepresentation are used to define the network representation " "of the leaf element of an ApplicationCompositeDataType."
        )
        assert CompositeNetworkRepresentation.getNetworkRepresentation.__doc__.strip() == network_representation_note
        assert (
            CompositeNetworkRepresentation.setNetworkRepresentation.__doc__.strip()
            == network_representation_note + " A None value is a no-op and does not overwrite an existing networkRepresentation."
        )

    def test_base_and_inheritance_shape(self):
        """Spec Base = ARObject — Python base is ARObject; setter return annotations resolve to the class (PEP 563 bare names, Rule 0003)."""
        assert issubclass(CompositeNetworkRepresentation, ARObject)
        for name in ("setLeafElementIRef", "setNetworkRepresentation"):
            assert CompositeNetworkRepresentation.__dict__[name].__annotations__["return"] == "CompositeNetworkRepresentation"

    def test_initialization_defaults(self):
        representation = CompositeNetworkRepresentation()
        assert representation.leafElementIRef is None
        assert representation.networkRepresentation is None
        assert representation.getLeafElementIRef() is None
        assert representation.getNetworkRepresentation() is None

    def test_get_set_leaf_element_iref(self):
        representation = CompositeNetworkRepresentation()
        iref = ApplicationCompositeElementInPortInterfaceInstanceRef()
        root_ref = RefType()
        root_ref.setValue("/Composite/Root")
        iref.setRootDataPrototypeRef(root_ref)
        target_ref = RefType()
        target_ref.setValue("/Composite/Leaf")
        iref.setTargetDataPrototypeRef(target_ref)
        result = representation.setLeafElementIRef(iref)
        assert result is representation
        assert representation.getLeafElementIRef() is iref
        assert representation.getLeafElementIRef().getRootDataPrototypeRef().getValue() == "/Composite/Root"
        assert representation.getLeafElementIRef().getTargetDataPrototypeRef().getValue() == "/Composite/Leaf"
        representation.setLeafElementIRef(None)
        assert representation.getLeafElementIRef() is iref

    def test_get_set_network_representation(self):
        representation = CompositeNetworkRepresentation()
        value = SwDataDefProps()
        result = representation.setNetworkRepresentation(value)
        assert result is representation
        assert representation.getNetworkRepresentation() is value
        representation.setNetworkRepresentation(None)
        assert representation.getNetworkRepresentation() is value


class TestTransmissionAcknowledgementRequest:
    """Test class for TransmissionAcknowledgementRequest class."""

    def test_initialization(self):
        """Test TransmissionAcknowledgementRequest field defaults."""
        request = TransmissionAcknowledgementRequest()
        assert request.timeout is None
        assert request.getTimeout() is None

    def test_get_set_timeout(self):
        """Test setTimeout returns self, value round-trips, None is a no-op."""
        request = TransmissionAcknowledgementRequest()
        timeout = TimeValue()
        timeout.setValue("0.5")
        assert request.setTimeout(timeout) is request
        assert request.getTimeout() is timeout
        request.setTimeout(None)
        assert request.getTimeout() is timeout


class TestSenderComSpec:
    """Test class for SenderComSpec abstract class (base accessors via NonqueuedSenderComSpec)."""

    def test_sender_com_spec_abstract(self):
        """Test that SenderComSpec is an abstract class that raises TypeError when instantiated."""
        with pytest.raises(TypeError):
            SenderComSpec()

    def test_sender_com_spec_base_properties(self):
        """Test all SenderComSpec base accessors through a concrete subclass."""
        sender = NonqueuedSenderComSpec()
        assert sender.compositeNetworkRepresentations == []
        assert sender.dataElementRef is None
        assert sender.handleOutOfRange is None
        assert sender.networkRepresentation is None
        assert sender.transmissionAcknowledge is None
        assert sender.transmissionProps is None
        assert sender.usesEndToEndProtection is None

        from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps

        representation = CompositeNetworkRepresentation()
        assert sender.addCompositeNetworkRepresentation(representation) is sender
        assert sender.getCompositeNetworkRepresentations() == [representation]
        sender.addCompositeNetworkRepresentation(None)
        assert len(sender.getCompositeNetworkRepresentations()) == 1

        ref = RefType()
        ref.setValue("/if/DataElement")
        assert sender.setDataElementRef(ref) is sender
        assert sender.getDataElementRef() is ref
        sender.setDataElementRef(None)
        assert sender.getDataElementRef() is ref

        handle_out_of_range = HandleOutOfRangeEnum().setValue(HandleOutOfRangeEnum.NONE)
        assert sender.setHandleOutOfRange(handle_out_of_range) is sender
        assert sender.getHandleOutOfRange() is handle_out_of_range
        sender.setHandleOutOfRange(None)
        assert sender.getHandleOutOfRange() is handle_out_of_range

        network_representation = SwDataDefProps()
        assert sender.setNetworkRepresentation(network_representation) is sender
        assert sender.getNetworkRepresentation() is network_representation
        sender.setNetworkRepresentation(None)
        assert sender.getNetworkRepresentation() is network_representation

        acknowledge = TransmissionAcknowledgementRequest()
        assert sender.setTransmissionAcknowledge(acknowledge) is sender
        assert sender.getTransmissionAcknowledge() is acknowledge
        sender.setTransmissionAcknowledge(None)
        assert sender.getTransmissionAcknowledge() is acknowledge

        transmission_props = TransmissionComSpecProps()
        assert sender.setTransmissionProps(transmission_props) is sender
        assert sender.getTransmissionProps() is transmission_props
        sender.setTransmissionProps(None)
        assert sender.getTransmissionProps() is transmission_props

        uses_e2e = Boolean()
        uses_e2e.setValue(True)
        assert sender.setUsesEndToEndProtection(uses_e2e) is sender
        assert sender.getUsesEndToEndProtection() is uses_e2e
        sender.setUsesEndToEndProtection(None)
        assert sender.getUsesEndToEndProtection() is uses_e2e


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

        handle_out_of_range = HandleOutOfRangeEnum().setValue(HandleOutOfRangeEnum.SATURATE)
        sender.setHandleOutOfRange(handle_out_of_range)
        assert sender.getHandleOutOfRange() == handle_out_of_range
        assert sender == sender.setHandleOutOfRange(handle_out_of_range)  # Test method chaining

    def test_queued_sender_com_spec_spec_base(self):
        """QueuedSenderComSpec is a concrete subclass of SenderComSpec (Table 4.68 Base row)."""
        assert issubclass(QueuedSenderComSpec, SenderComSpec)
        assert issubclass(QueuedSenderComSpec, PPortComSpec)
        assert issubclass(QueuedSenderComSpec, ARObject)

        com_spec = QueuedSenderComSpec()
        assert isinstance(com_spec, QueuedSenderComSpec)
        assert isinstance(com_spec, SenderComSpec)

    def test_queued_sender_com_spec_class_docstring_note(self):
        """Class docstring is the spec Note verbatim (Table 4.68, p.179)."""
        note = 'Communication attributes specific to distribution of events (PPortPrototype, SenderReceiverInterface and dataElement carries an "event").'
        assert inspect.cleandoc(QueuedSenderComSpec.__doc__) == note

    def test_queued_sender_com_spec_init_docless(self):
        """__init__ carries no docstring (Rule 0012.2.4)."""
        assert QueuedSenderComSpec.__init__.__doc__ is None


class TestNonqueuedSenderComSpec:
    """Test class for NonqueuedSenderComSpec class."""

    def test_nonqueued_sender_com_spec_initialization(self):
        """Test NonqueuedSenderComSpec initialization and methods."""
        sender = NonqueuedSenderComSpec()
        assert sender.dataFilter is None
        assert sender.initValue is None

    def test_get_set_data_filter(self):
        """Test dataFilter accessor pair and None no-op."""
        sender = NonqueuedSenderComSpec()
        data_filter = DataFilter()
        assert sender.setDataFilter(data_filter) is sender
        assert sender.getDataFilter() is data_filter
        sender.setDataFilter(None)
        assert sender.getDataFilter() is data_filter

    def test_get_set_init_value(self):
        """Test initValue accessor pair and None no-op."""
        sender = NonqueuedSenderComSpec()
        init_value = TextValueSpecification()
        assert sender.setInitValue(init_value) is sender
        assert sender.getInitValue() is init_value
        sender.setInitValue(None)
        assert sender.getInitValue() is init_value


class TestClientComSpec:
    """Test class for ClientComSpec class."""

    def test_client_com_spec_initialization(self):
        """Test ClientComSpec initialization and methods."""
        client = ClientComSpec()
        assert client.endToEndCallResponseTimeout is None
        assert client.operationRef is None
        assert client.transformationComSpecProps == []

    def test_get_set_end_to_end_call_response_timeout(self):
        """Test endToEndCallResponseTimeout accessor pair and None no-op."""
        client = ClientComSpec()
        timeout = TimeValue()
        timeout.setValue("1.0")
        assert client.setEndToEndCallResponseTimeout(timeout) is client
        assert client.getEndToEndCallResponseTimeout() is timeout
        client.setEndToEndCallResponseTimeout(None)
        assert client.getEndToEndCallResponseTimeout() is timeout

    def test_get_set_operation_ref(self):
        """Test operationRef accessor pair and None no-op."""
        client = ClientComSpec()
        ref = RefType()
        ref.setValue("/Test/Operation")
        assert client.setOperationRef(ref) is client
        assert client.getOperationRef() is ref
        client.setOperationRef(None)
        assert client.getOperationRef() is ref

    def test_add_transformation_com_spec_props(self):
        """Test transformationComSpecProps add/get and None no-op."""
        client = ClientComSpec()
        props = UserDefinedTransformationComSpecProps()
        assert client.addTransformationComSpecProps(props) is client
        assert client.getTransformationComSpecProps() == [props]
        client.addTransformationComSpecProps(None)
        assert len(client.getTransformationComSpecProps()) == 1


class TestModeSwitchReceiverComSpec:
    """Test class for ModeSwitchReceiverComSpec class (Table 4.81)."""

    def test_spec_notes_are_verbatim(self):
        """Class and member docstrings must be the Table 4.81 Notes copied verbatim."""
        assert ModeSwitchReceiverComSpec.__doc__.strip() == "Communication attributes of RPortPrototypes with respect to mode communication"
        enhanced_note = 'This controls the creation of the enhanced mode API that returns information about the previous mode and the next mode. If set to "true" the enhanced mode API is supposed to be generated. For more details please refer to the SWS_RTE.'
        assert ModeSwitchReceiverComSpec.getEnhancedModeApi.__doc__.strip() == enhanced_note
        assert ModeSwitchReceiverComSpec.setEnhancedModeApi.__doc__.strip() == enhanced_note + " A None value is a no-op and does not overwrite an existing enhancedModeApi."
        mode_group_note = "ModeDeclarationGroupPrototype (of the same PortInterface) to which these communication attributes apply. [constr_1896]"
        assert ModeSwitchReceiverComSpec.getModeGroupRef.__doc__.strip() == mode_group_note
        assert ModeSwitchReceiverComSpec.setModeGroupRef.__doc__.strip() == mode_group_note + " A None value is a no-op and does not overwrite an existing modeGroupRef."
        async_note = "This attribute controls the behavior of the corresponding RPortPrototype with respect to the question whether it can deal with asynchronous mode switch requests, i.e. if set to true, the RPortPrototype is able to deal with an asynchronous mode switch request."
        assert ModeSwitchReceiverComSpec.getSupportsAsynchronousModeSwitch.__doc__.strip() == async_note
        assert ModeSwitchReceiverComSpec.setSupportsAsynchronousModeSwitch.__doc__.strip() == async_note + " A None value is a no-op and does not overwrite an existing supportsAsynchronousModeSwitch."

    def test_base_and_inheritance_shape(self):
        """Spec Base = ARObject + RPortComSpec — Python base is RPortComSpec (most-derived, Table 4.59); setter return annotations resolve to the class (PEP 563 bare names, Rule 0003)."""
        assert issubclass(ModeSwitchReceiverComSpec, RPortComSpec)
        assert issubclass(ModeSwitchReceiverComSpec, ARObject)
        assert ModeSwitchReceiverComSpec.__dict__["setEnhancedModeApi"].__annotations__["return"] == "ModeSwitchReceiverComSpec"
        assert ModeSwitchReceiverComSpec.__dict__["setModeGroupRef"].__annotations__["return"] == "ModeSwitchReceiverComSpec"
        assert ModeSwitchReceiverComSpec.__dict__["setSupportsAsynchronousModeSwitch"].__annotations__["return"] == "ModeSwitchReceiverComSpec"

    def test_initialization_defaults(self):
        """Test ModeSwitchReceiverComSpec field defaults."""
        com_spec = ModeSwitchReceiverComSpec()
        assert com_spec.enhancedModeApi is None
        assert com_spec.modeGroupRef is None
        assert com_spec.supportsAsynchronousModeSwitch is None

    def test_get_set_enhanced_mode_api(self):
        """Test enhancedModeApi accessor pair, chaining and None no-op."""
        com_spec = ModeSwitchReceiverComSpec()
        value = Boolean()
        value.setValue(True)
        result = com_spec.setEnhancedModeApi(value)
        assert result is com_spec
        assert com_spec.getEnhancedModeApi() is value
        com_spec.setEnhancedModeApi(None)
        assert com_spec.getEnhancedModeApi() is value

    def test_get_set_mode_group_ref(self):
        """Test modeGroupRef accessor pair, chaining and None no-op."""
        com_spec = ModeSwitchReceiverComSpec()
        value = RefType()
        value.setValue("/ModeDcl/Group")
        result = com_spec.setModeGroupRef(value)
        assert result is com_spec
        assert com_spec.getModeGroupRef() is value
        com_spec.setModeGroupRef(None)
        assert com_spec.getModeGroupRef() is value

    def test_get_set_supports_asynchronous_mode_switch(self):
        """Test supportsAsynchronousModeSwitch accessor pair, chaining and None no-op."""
        com_spec = ModeSwitchReceiverComSpec()
        value = Boolean()
        value.setValue(False)
        result = com_spec.setSupportsAsynchronousModeSwitch(value)
        assert result is com_spec
        assert com_spec.getSupportsAsynchronousModeSwitch() is value
        com_spec.setSupportsAsynchronousModeSwitch(None)
        assert com_spec.getSupportsAsynchronousModeSwitch() is value


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

        e2e = Boolean()
        e2e.setValue(True)
        receiver.setUsesEndToEndProtection(e2e)
        assert receiver.getUsesEndToEndProtection() == e2e

        # Test composite network representation methods
        comp_rep = CompositeNetworkRepresentation()
        receiver.addCompositeNetworkRepresentation(comp_rep)
        assert comp_rep in receiver.getCompositeNetworkRepresentations()

    def test_reception_props(self):
        """Test receptionProps getter and setter with round-trip and None no-op."""
        receiver = NonqueuedReceiverComSpec()
        assert receiver.getReceptionProps() is None

        props = ReceptionComSpecProps()
        result = receiver.setReceptionProps(props)
        assert result is receiver
        assert receiver.getReceptionProps() == props

        receiver.setReceptionProps(None)
        assert receiver.getReceptionProps() == props

    def test_replace_with(self):
        """Test replaceWith getter and setter with round-trip and None no-op."""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import VariableAccess

        receiver = NonqueuedReceiverComSpec()
        assert receiver.getReplaceWith() is None

        access = VariableAccess(None, "TestAccess")
        result = receiver.setReplaceWith(access)
        assert result is receiver
        assert receiver.getReplaceWith() == access

        receiver.setReplaceWith(None)
        assert receiver.getReplaceWith() == access

    def test_sync_counter_init(self):
        """Test syncCounterInit getter and setter with round-trip and None no-op."""
        receiver = NonqueuedReceiverComSpec()
        assert receiver.getSyncCounterInit() is None

        value = PositiveInteger()
        value.setValue(3)
        result = receiver.setSyncCounterInit(value)
        assert result is receiver
        assert receiver.getSyncCounterInit() == value

        receiver.setSyncCounterInit(None)
        assert receiver.getSyncCounterInit() == value

    def test_transformation_com_spec_props(self):
        """Test transformationComSpecProps add and get with None no-op."""
        receiver = NonqueuedReceiverComSpec()
        assert receiver.getTransformationComSpecProps() == []

        props = EndToEndTransformationComSpecProps()
        result = receiver.addTransformationComSpecProps(props)
        assert result is receiver
        assert receiver.getTransformationComSpecProps() == [props]

        receiver.addTransformationComSpecProps(None)
        assert receiver.getTransformationComSpecProps() == [props]


class TestModeSwitchedAckRequest:
    """Test class for ModeSwitchedAckRequest class (Table 4.80)."""

    def test_spec_notes_are_verbatim(self):
        """Class and member docstrings must be the Table 4.80 Notes copied verbatim."""
        assert ModeSwitchedAckRequest.__doc__.strip() == "Requests acknowledgements that a mode switch has been proceeded successfully"
        timeout_note = "Number of seconds before an error is reported or in case of allowed redundancy, the value is sent again."
        assert ModeSwitchedAckRequest.getTimeout.__doc__.strip() == timeout_note
        assert ModeSwitchedAckRequest.setTimeout.__doc__.strip() == timeout_note + " A None value is a no-op and does not overwrite an existing timeout."

    def test_base_and_inheritance_shape(self):
        """Spec Base = ARObject — Python base is ARObject; setter return annotation resolves to the class (PEP 563 bare names, Rule 0003)."""
        assert issubclass(ModeSwitchedAckRequest, ARObject)
        assert ModeSwitchedAckRequest.__dict__["setTimeout"].__annotations__["return"] == "ModeSwitchedAckRequest"

    def test_initialization_defaults(self):
        ack = ModeSwitchedAckRequest()
        assert ack.timeout is None
        assert ack.getTimeout() is None

    def test_get_set_timeout(self):
        ack = ModeSwitchedAckRequest()
        value = TimeValue()
        value.setValue(5.0)
        result = ack.setTimeout(value)
        assert result is ack
        assert ack.getTimeout() is value
        ack.setTimeout(None)
        assert ack.getTimeout() is value


class TestModeSwitchSenderComSpec:
    """Test class for ModeSwitchSenderComSpec class (Table 4.79)."""

    def test_spec_notes_are_verbatim(self):
        """Class and member docstrings must be the Table 4.79 Notes copied verbatim."""
        assert ModeSwitchSenderComSpec.__doc__.strip() == "Communication attributes of PPortPrototypes with respect to mode communication"
        enhanced_note = 'This controls the creation of the enhanced mode API that returns information about the previous mode and the next mode. If set to "true" the enhanced mode API is supposed to be generated. For more details please refer to the SWS_RTE.'
        assert ModeSwitchSenderComSpec.getEnhancedModeApi.__doc__.strip() == enhanced_note
        assert ModeSwitchSenderComSpec.setEnhancedModeApi.__doc__.strip() == enhanced_note + " A None value is a no-op and does not overwrite an existing enhancedModeApi."
        mode_group_note = "ModeDeclarationGroupPrototype (of the same PortInterface) to which these communication attributes apply. [constr_1895]"
        assert ModeSwitchSenderComSpec.getModeGroupRef.__doc__.strip() == mode_group_note
        assert ModeSwitchSenderComSpec.setModeGroupRef.__doc__.strip() == mode_group_note + " A None value is a no-op and does not overwrite an existing modeGroupRef."
        ack_note = "If this aggregation exists an acknowledgement for the successful processing of the mode switch request is required."
        assert ModeSwitchSenderComSpec.getModeSwitchedAck.__doc__.strip() == ack_note
        assert ModeSwitchSenderComSpec.setModeSwitchedAck.__doc__.strip() == ack_note + " A None value is a no-op and does not overwrite an existing modeSwitchedAck."
        queue_note = "Length of call queue on the mode user side. The queue is implemented by the RTE. The value shall be greater or equal to 1. Setting the value of queueLength to 1 implies that incoming requests are rejected while another request that arrived earlier is being processed. [constr_1894]"
        assert ModeSwitchSenderComSpec.getQueueLength.__doc__.strip() == queue_note
        assert ModeSwitchSenderComSpec.setQueueLength.__doc__.strip() == queue_note + " A None value is a no-op and does not overwrite an existing queueLength."

    def test_base_and_inheritance_shape(self):
        """Spec Base = ARObject + PPortComSpec — Python base is PPortComSpec (most-derived, Table 4.58); setter return annotations resolve to the class (PEP 563 bare names, Rule 0003)."""
        assert issubclass(ModeSwitchSenderComSpec, PPortComSpec)
        assert issubclass(ModeSwitchSenderComSpec, ARObject)
        assert ModeSwitchSenderComSpec.__dict__["setEnhancedModeApi"].__annotations__["return"] == "ModeSwitchSenderComSpec"
        assert ModeSwitchSenderComSpec.__dict__["setModeGroupRef"].__annotations__["return"] == "ModeSwitchSenderComSpec"
        assert ModeSwitchSenderComSpec.__dict__["setModeSwitchedAck"].__annotations__["return"] == "ModeSwitchSenderComSpec"
        assert ModeSwitchSenderComSpec.__dict__["setQueueLength"].__annotations__["return"] == "ModeSwitchSenderComSpec"

    def test_initialization_defaults(self):
        """Test ModeSwitchSenderComSpec field defaults."""
        sender = ModeSwitchSenderComSpec()
        assert sender.enhancedModeApi is None
        assert sender.modeGroupRef is None
        assert sender.modeSwitchedAck is None
        assert sender.queueLength is None

    def test_get_set_enhanced_mode_api(self):
        """Test enhancedModeApi accessor pair, chaining and None no-op."""
        sender = ModeSwitchSenderComSpec()
        value = Boolean()
        value.setValue(True)
        result = sender.setEnhancedModeApi(value)
        assert result is sender
        assert sender.getEnhancedModeApi() is value
        sender.setEnhancedModeApi(None)
        assert sender.getEnhancedModeApi() is value

    def test_get_set_mode_group_ref(self):
        """Test modeGroupRef accessor pair, chaining and None no-op."""
        sender = ModeSwitchSenderComSpec()
        value = RefType()
        value.setValue("/ModeDcl/Group")
        result = sender.setModeGroupRef(value)
        assert result is sender
        assert sender.getModeGroupRef() is value
        sender.setModeGroupRef(None)
        assert sender.getModeGroupRef() is value

    def test_get_set_mode_switched_ack(self):
        """Test modeSwitchedAck accessor pair, chaining and None no-op."""
        sender = ModeSwitchSenderComSpec()
        value = ModeSwitchedAckRequest()
        result = sender.setModeSwitchedAck(value)
        assert result is sender
        assert sender.getModeSwitchedAck() is value
        sender.setModeSwitchedAck(None)
        assert sender.getModeSwitchedAck() is value

    def test_get_set_queue_length(self):
        """Test queueLength accessor pair, chaining and None no-op."""
        sender = ModeSwitchSenderComSpec()
        value = PositiveInteger()
        value.setValue(5)
        result = sender.setQueueLength(value)
        assert result is sender
        assert sender.getQueueLength() is value
        sender.setQueueLength(None)
        assert sender.getQueueLength() is value


class TestParameterProvideComSpec:
    """Test class for ParameterProvideComSpec class."""

    def test_parameter_provide_com_spec_initialization(self):
        """Test ParameterProvideComSpec field defaults."""
        com_spec = ParameterProvideComSpec()
        assert com_spec.initValue is None
        assert com_spec.parameterRef is None

    def test_get_set_init_value(self):
        """Test initValue accessor pair and None no-op."""
        com_spec = ParameterProvideComSpec()
        init_value = TextValueSpecification()
        assert com_spec.setInitValue(init_value) is com_spec
        assert com_spec.getInitValue() is init_value
        com_spec.setInitValue(None)
        assert com_spec.getInitValue() is init_value

    def test_get_set_parameter_ref(self):
        """Test parameterRef accessor pair and None no-op."""
        com_spec = ParameterProvideComSpec()
        ref = RefType()
        ref.setValue("/if/Parameter")
        assert com_spec.setParameterRef(ref) is com_spec
        assert com_spec.getParameterRef() is ref
        com_spec.setParameterRef(None)
        assert com_spec.getParameterRef() is ref


class TestTransmissionComSpecProps:
    """Test class for TransmissionComSpecProps class."""

    def test_initialization(self):
        """Test TransmissionComSpecProps field defaults."""
        props = TransmissionComSpecProps()
        assert props.dataUpdatePeriod is None
        assert props.minimumSendInterval is None
        assert props.transmissionMode is None

    def test_get_set_data_update_period(self):
        """Test dataUpdatePeriod accessor pair and None no-op."""
        props = TransmissionComSpecProps()
        period = TimeValue()
        period.setValue("0.01")
        assert props.setDataUpdatePeriod(period) is props
        assert props.getDataUpdatePeriod() is period
        props.setDataUpdatePeriod(None)
        assert props.getDataUpdatePeriod() is period

    def test_get_set_minimum_send_interval(self):
        """Test minimumSendInterval accessor pair and None no-op."""
        props = TransmissionComSpecProps()
        interval = TimeValue()
        interval.setValue("0.1")
        assert props.setMinimumSendInterval(interval) is props
        assert props.getMinimumSendInterval() is interval
        props.setMinimumSendInterval(None)
        assert props.getMinimumSendInterval() is interval

    def test_get_set_transmission_mode(self):
        """Test transmissionMode accessor pair and None no-op."""
        props = TransmissionComSpecProps()
        mode = TransmissionModeDefinitionEnum().setValue(TransmissionModeDefinitionEnum.TRIGGERED)
        assert props.setTransmissionMode(mode) is props
        assert props.getTransmissionMode() is mode
        props.setTransmissionMode(None)
        assert props.getTransmissionMode() is mode


class TestTransmissionModeDefinitionEnum:
    """Test class for TransmissionModeDefinitionEnum class."""

    def test_members(self):
        """Test TransmissionModeDefinitionEnum member values."""
        enum = TransmissionModeDefinitionEnum()
        values = enum.getEnumValues()
        assert TransmissionModeDefinitionEnum.CYCLIC == "cyclic"
        assert TransmissionModeDefinitionEnum.CYCLIC_AND_ON_CHANGE == "cyclicAndOnChange"
        assert TransmissionModeDefinitionEnum.TRIGGERED == "triggered"
        assert TransmissionModeDefinitionEnum.CYCLIC in values
        assert TransmissionModeDefinitionEnum.CYCLIC_AND_ON_CHANGE in values
        assert TransmissionModeDefinitionEnum.TRIGGERED in values
        assert len(values) == 3

    def test_instantiable(self):
        """Test that the enum can be instantiated and hold a value."""
        enum = TransmissionModeDefinitionEnum()
        enum.setValue(TransmissionModeDefinitionEnum.CYCLIC_AND_ON_CHANGE)
        assert enum.getValue() == "cyclicAndOnChange"


class TestTransformationComSpecProps:
    """Test class for TransformationComSpecProps abstract class."""

    def test_transformation_com_spec_props_abstract(self):
        """Test that TransformationComSpecProps is an abstract class that raises NotImplementedError when instantiated."""
        with pytest.raises(TypeError):
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
        clear_valid = Boolean()
        clear_valid.setValue(True)
        e2e.setClearFromValidToInvalid(clear_valid)
        assert e2e.getClearFromValidToInvalid() == clear_valid

        disable_check = Boolean()
        disable_check.setValue(False)
        e2e.setDisableEndToEndCheck(disable_check)
        assert e2e.getDisableEndToEndCheck() == disable_check

        disable_sm = Boolean()
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
        _user_def = UserDefinedTransformationComSpecProps()
        # Just verify it can be initialized

    def test_user_defined_transformation_com_spec_props_spec_base(self):
        """UserDefinedTransformationComSpecProps is a concrete subclass of TransformationComSpecProps (Table 4.91 Base row)."""
        assert issubclass(UserDefinedTransformationComSpecProps, TransformationComSpecProps)
        assert issubclass(UserDefinedTransformationComSpecProps, ARObject)

        props = UserDefinedTransformationComSpecProps()
        assert isinstance(props, UserDefinedTransformationComSpecProps)
        assert isinstance(props, TransformationComSpecProps)

    def test_user_defined_transformation_com_spec_props_class_docstring_note(self):
        """Class docstring is the spec Note verbatim (Table 4.91, p.200)."""
        note = "The UserDefinedTransformationComSpecProps is used to specify port specific configuration properties for custom transformers."
        assert inspect.cleandoc(UserDefinedTransformationComSpecProps.__doc__) == note

    def test_user_defined_transformation_com_spec_props_init_docless(self):
        """__init__ carries no docstring (Rule 0012.2.4)."""
        assert UserDefinedTransformationComSpecProps.__init__.__doc__ is None


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

        # None no-op checks
        server.setOperationRef(None)
        assert server.getOperationRef() is ref
        server.setQueueLength(None)
        assert server.getQueueLength() is queue_len
        server.addTransformationComSpecProps(None)
        assert len(server.getTransformationComSpecProps()) == 1


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
        assert receiver.getAliveTimeout() is None
        assert receiver.getEnableUpdate() is None
        assert receiver.getFilter() is None
        assert receiver.getHandleDataStatus() is None
        assert receiver.getHandleNeverReceived() is None
        assert receiver.getHandleTimeoutType() is None
        assert receiver.getInitValue() is None
        assert receiver.getTimeoutSubstitutionValue() is None

        # Test setters and getters
        alive_timeout = TimeValue()
        alive_timeout.setValue("10.5")
        receiver.setAliveTimeout(alive_timeout)
        assert receiver.getAliveTimeout() == alive_timeout

        enable_updated = Boolean()
        enable_updated.setValue(True)
        receiver.setEnableUpdate(enable_updated)
        assert receiver.getEnableUpdate() == enable_updated

        from armodel.models.M2.AUTOSARTemplates.CommonStructure.Filter import DataFilter

        filter_value = DataFilter()
        receiver.setFilter(filter_value)
        assert receiver.getFilter() == filter_value

        handle_data = Boolean()
        handle_data.setValue(True)
        receiver.setHandleDataStatus(handle_data)
        assert receiver.getHandleDataStatus() == handle_data

        handle_never = Boolean()
        handle_never.setValue(False)
        receiver.setHandleNeverReceived(handle_never)
        assert receiver.getHandleNeverReceived() == handle_never

        timeout_type = HandleTimeoutEnum()
        timeout_type.setValue(HandleTimeoutEnum.REPLACE)
        receiver.setHandleTimeoutType(timeout_type)
        assert receiver.getHandleTimeoutType() == timeout_type

        from armodel.models.M2.AUTOSARTemplates.CommonStructure import TextValueSpecification

        init_value = TextValueSpecification()
        receiver.setInitValue(init_value)
        assert receiver.getInitValue() == init_value

        timeout_sub = TextValueSpecification()
        receiver.setTimeoutSubstitutionValue(timeout_sub)
        assert receiver.getTimeoutSubstitutionValue() == timeout_sub

    def test_alive_timeout_none_noop(self):
        """Test setAliveTimeout with None is a no-op."""
        receiver = NonqueuedReceiverComSpec()
        alive_timeout = TimeValue()
        alive_timeout.setValue("10.5")
        receiver.setAliveTimeout(alive_timeout)
        receiver.setAliveTimeout(None)
        assert receiver.getAliveTimeout() == alive_timeout

    def test_enable_update_none_noop(self):
        """Test setEnableUpdate with None is a no-op."""
        receiver = NonqueuedReceiverComSpec()
        enable = Boolean()
        enable.setValue(True)
        receiver.setEnableUpdate(enable)
        receiver.setEnableUpdate(None)
        assert receiver.getEnableUpdate() == enable

    def test_handle_timeout_type_none_noop(self):
        """Test setHandleTimeoutType with None is a no-op."""
        receiver = NonqueuedReceiverComSpec()
        timeout_type = HandleTimeoutEnum()
        timeout_type.setValue(HandleTimeoutEnum.NONE)
        receiver.setHandleTimeoutType(timeout_type)
        receiver.setHandleTimeoutType(None)
        assert receiver.getHandleTimeoutType() == timeout_type

    def test_timeout_substitution_value_none_noop(self):
        """Test setTimeoutSubstitutionValue with None is a no-op."""
        from armodel.models.M2.AUTOSARTemplates.CommonStructure import TextValueSpecification

        receiver = NonqueuedReceiverComSpec()
        timeout_sub = TextValueSpecification()
        receiver.setTimeoutSubstitutionValue(timeout_sub)
        receiver.setTimeoutSubstitutionValue(None)
        assert receiver.getTimeoutSubstitutionValue() == timeout_sub


class TestHandleOutOfRangeStatusEnum:
    """Test cases for HandleOutOfRangeStatusEnum class."""

    def test_members(self):
        """Test HandleOutOfRangeStatusEnum member values."""
        enum = HandleOutOfRangeStatusEnum()
        values = enum.getEnumValues()
        assert HandleOutOfRangeStatusEnum.INDICATE == "indicate"
        assert HandleOutOfRangeStatusEnum.SILENT == "silent"
        assert HandleOutOfRangeStatusEnum.INDICATE in values
        assert HandleOutOfRangeStatusEnum.SILENT in values


class TestHandleTimeoutEnum:
    """Test cases for HandleTimeoutEnum class."""

    def test_members(self):
        """Test HandleTimeoutEnum member values."""
        enum = HandleTimeoutEnum()
        values = enum.getEnumValues()
        assert HandleTimeoutEnum.NONE == "none"
        assert HandleTimeoutEnum.REPLACE == "replace"
        assert HandleTimeoutEnum.REPLACE_BY_TIMEOUT_SUBSTITUTION_VALUE == "replaceByTimeoutSubstitutionValue"
        assert HandleTimeoutEnum.NONE in values
        assert HandleTimeoutEnum.REPLACE in values
        assert HandleTimeoutEnum.REPLACE_BY_TIMEOUT_SUBSTITUTION_VALUE in values


class TestQueuedReceiverComSpec:
    """Test class for QueuedReceiverComSpec class."""

    def test_queued_receiver_com_spec_initialization(self):
        """Test QueuedReceiverComSpec initialization and methods."""
        receiver = QueuedReceiverComSpec()
        assert receiver.queueLength is None

        # Test setters and getters
        queue_len = PositiveInteger()
        queue_len.setValue(5)
        receiver.setQueueLength(queue_len)
        assert receiver.getQueueLength() == queue_len


class TestHandleOutOfRangeEnum:
    """Test cases for HandleOutOfRangeEnum class."""

    def test_members(self):
        """Test HandleOutOfRangeEnum member values."""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import HandleOutOfRangeEnum

        enum = HandleOutOfRangeEnum()
        values = enum.getEnumValues()
        assert HandleOutOfRangeEnum.DEFAULT == "default"
        assert HandleOutOfRangeEnum.EXTERNAL_REPLACEMENT == "externalReplacement"
        assert HandleOutOfRangeEnum.IGNORE == "ignore"
        assert HandleOutOfRangeEnum.INVALID == "invalid"
        assert HandleOutOfRangeEnum.NONE == "none"
        assert HandleOutOfRangeEnum.SATURATE == "saturate"
        assert HandleOutOfRangeEnum.DEFAULT in values
        assert HandleOutOfRangeEnum.EXTERNAL_REPLACEMENT in values
        assert HandleOutOfRangeEnum.IGNORE in values
        assert HandleOutOfRangeEnum.INVALID in values
        assert HandleOutOfRangeEnum.NONE in values
        assert HandleOutOfRangeEnum.SATURATE in values


class TestReceptionComSpecProps:
    """Test class for ReceptionComSpecProps class (Table 4.64)."""

    def test_spec_notes_are_verbatim(self):
        """Class and member docstrings must be the Table 4.64 Notes copied verbatim."""
        assert ReceptionComSpecProps.__doc__.strip() == "This meta-class defines a set of reception attributes which the application software is assumed to implement."
        data_update_period_note = (
            "This attribute defines the period in which the application shall check for updated data. This attribute is used for the configuration "
            "of the E2E protection, but may also indicate a general data reception period."
        )
        assert ReceptionComSpecProps.getDataUpdatePeriod.__doc__.strip() == data_update_period_note
        assert ReceptionComSpecProps.setDataUpdatePeriod.__doc__.strip() == data_update_period_note + " A None value is a no-op and does not overwrite an existing dataUpdatePeriod."
        timeout_note = (
            "This attribute defines the time interval after which the application shall assume that the to be received data reception has timed out, "
            "i.e. the respective data has not been received for that amount of time."
        )
        assert ReceptionComSpecProps.getTimeout.__doc__.strip() == timeout_note
        assert ReceptionComSpecProps.setTimeout.__doc__.strip() == timeout_note + " A None value is a no-op and does not overwrite an existing timeout."

    def test_base_and_inheritance_shape(self):
        """Spec Base = ARObject — Python base is ARObject; setter return annotations resolve to the class (PEP 563 bare names, Rule 0003)."""
        assert issubclass(ReceptionComSpecProps, ARObject)
        for name in ("setDataUpdatePeriod", "setTimeout"):
            assert ReceptionComSpecProps.__dict__[name].__annotations__["return"] == "ReceptionComSpecProps"

    def test_initialization_defaults(self):
        props = ReceptionComSpecProps()
        assert props.dataUpdatePeriod is None
        assert props.timeout is None
        assert props.getDataUpdatePeriod() is None
        assert props.getTimeout() is None

    def test_get_set_data_update_period(self):
        props = ReceptionComSpecProps()
        value = TimeValue()
        value.setValue(0.02)
        result = props.setDataUpdatePeriod(value)
        assert result is props
        assert props.getDataUpdatePeriod() is value
        props.setDataUpdatePeriod(None)
        assert props.getDataUpdatePeriod() is value

    def test_get_set_timeout(self):
        props = ReceptionComSpecProps()
        value = TimeValue()
        value.setValue(2.5)
        result = props.setTimeout(value)
        assert result is props
        assert props.getTimeout() is value
        props.setTimeout(None)
        assert props.getTimeout() is value
