import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import ClientServerToSignalMapping, DataMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import OperationInSystemInstanceRef


def _ref(value: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    return ref


class TestClientServerToSignalMapping:
    """Test cases for ClientServerToSignalMapping (Table 5.33, p.242)."""

    MEMBERS = [
        "callSignalRef",
        "clientServerOperationIRef",
        "returnSignalRef",
    ]

    def test_inheritance(self):
        assert issubclass(ClientServerToSignalMapping, DataMapping)

    def test_class_docstring_note(self):
        expected = "This element maps the ClientServerOperation to call- and return-SystemSignals."
        assert inspect.cleandoc(ClientServerToSignalMapping.__doc__).split("\n\n")[0] == expected

    def test_init_has_no_docstring(self):
        assert ClientServerToSignalMapping.__init__.__doc__ is None

    def test_initialization_defaults(self):
        mapping = ClientServerToSignalMapping()
        assert mapping.getCallSignalRef() is None
        assert mapping.getClientServerOperationIRef() is None
        assert mapping.getReturnSignalRef() is None

    def test_member_order(self):
        mapping = ClientServerToSignalMapping()
        members = [k for k in vars(mapping) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_get_set_call_signal_ref(self):
        mapping = ClientServerToSignalMapping()
        result = mapping.setCallSignalRef(_ref("/System/CallSignal"))
        assert result is mapping
        assert mapping.getCallSignalRef().getValue() == "/System/CallSignal"
        mapping.setCallSignalRef(None)
        assert mapping.getCallSignalRef().getValue() == "/System/CallSignal"

    def test_get_set_client_server_operation_i_ref(self):
        mapping = ClientServerToSignalMapping()
        iref = OperationInSystemInstanceRef()
        result = mapping.setClientServerOperationIRef(iref)
        assert result is mapping
        assert mapping.getClientServerOperationIRef() is iref
        mapping.setClientServerOperationIRef(None)
        assert mapping.getClientServerOperationIRef() is iref

    def test_get_set_return_signal_ref(self):
        mapping = ClientServerToSignalMapping()
        result = mapping.setReturnSignalRef(_ref("/System/ReturnSignal"))
        assert result is mapping
        assert mapping.getReturnSignalRef().getValue() == "/System/ReturnSignal"
        mapping.setReturnSignalRef(None)
        assert mapping.getReturnSignalRef().getValue() == "/System/ReturnSignal"

    def test_type_hints(self):
        hints = typing.get_type_hints(ClientServerToSignalMapping.getCallSignalRef)
        assert hints["return"] == typing.Optional[RefType]
        hints = typing.get_type_hints(ClientServerToSignalMapping.setCallSignalRef)
        assert hints["value"] == typing.Optional[RefType]
        assert hints["return"] is ClientServerToSignalMapping
        hints = typing.get_type_hints(ClientServerToSignalMapping.getClientServerOperationIRef)
        assert hints["return"] == typing.Optional[OperationInSystemInstanceRef]
        hints = typing.get_type_hints(ClientServerToSignalMapping.setClientServerOperationIRef)
        assert hints["value"] == typing.Optional[OperationInSystemInstanceRef]
        assert hints["return"] is ClientServerToSignalMapping
        hints = typing.get_type_hints(ClientServerToSignalMapping.getReturnSignalRef)
        assert hints["return"] == typing.Optional[RefType]
        hints = typing.get_type_hints(ClientServerToSignalMapping.setReturnSignalRef)
        assert hints["value"] == typing.Optional[RefType]
        assert hints["return"] is ClientServerToSignalMapping
