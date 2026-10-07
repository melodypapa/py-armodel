import typing
from inspect import cleandoc
from typing import Optional

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    MacAddressString,
    PositiveInteger,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp import IEEE1722TpConnection


def _ref(value, dest):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _mac(value):
    mac = MacAddressString()
    mac.setValue(value)
    return mac


def _pos_int(value):
    integer = PositiveInteger()
    integer.setValue(value)
    return integer


class TestIEEE1722TpConnection:
    def test_docstring_is_spec_note_verbatim(self):
        # Table 6.275, p.637 — class Note verbatim from the markdown
        assert cleandoc(IEEE1722TpConnection.__doc__) == "Definition of the IEEE1722Tp protocol. Tags: atp.Status=candidate"

    def test_abstract(self):
        with pytest.raises(TypeError):
            IEEE1722TpConnection(None, "Conn")

    def test_heritage(self):
        assert issubclass(IEEE1722TpConnection, ARElement)

    def test_initialization(self):
        class _Conn(IEEE1722TpConnection):
            pass

        connection = _Conn(None, "Conn")
        assert connection.getDestinationMacAddress() is None
        assert connection.getMacAddressStreamId() is None
        assert connection.getPduRef() is None
        assert connection.getUniqueStreamId() is None
        assert connection.getVersion() is None
        assert connection.getVlanPriority() is None

    def test_base_accessors(self):
        class _Conn(IEEE1722TpConnection):
            pass

        connection = _Conn(None, "Conn")

        mac = _mac("00:11:22:33:44:55")
        assert connection.setDestinationMacAddress(mac) is connection
        assert connection.getDestinationMacAddress() is mac
        assert connection.setDestinationMacAddress(None) is connection
        assert connection.getDestinationMacAddress() is mac

        mac_stream = _mac("66:77:88:99:AA:BB")
        assert connection.setMacAddressStreamId(mac_stream) is connection
        assert connection.getMacAddressStreamId() is mac_stream
        assert connection.setMacAddressStreamId(None) is connection
        assert connection.getMacAddressStreamId() is mac_stream

        pdu_ref = _ref("/Pdu/Pt1", "PDU-TRIGGERING")
        assert connection.setPduRef(pdu_ref) is connection
        assert connection.getPduRef() is pdu_ref
        assert connection.setPduRef(None) is connection
        assert connection.getPduRef() is pdu_ref

        unique_stream_id = _pos_int(42)
        assert connection.setUniqueStreamId(unique_stream_id) is connection
        assert connection.getUniqueStreamId() is unique_stream_id
        assert connection.getUniqueStreamId().getValue() == 42
        assert connection.setUniqueStreamId(None) is connection
        assert connection.getUniqueStreamId() is unique_stream_id

        version = _pos_int(2)
        assert connection.setVersion(version) is connection
        assert connection.getVersion() is version
        assert connection.setVersion(None) is connection
        assert connection.getVersion() is version

        vlan_priority = _pos_int(5)
        assert connection.setVlanPriority(vlan_priority) is connection
        assert connection.getVlanPriority() is vlan_priority
        assert connection.setVlanPriority(None) is connection
        assert connection.getVlanPriority() is vlan_priority

    def test_annotations(self):
        hints = typing.get_type_hints(IEEE1722TpConnection.getDestinationMacAddress)
        assert hints["return"] == Optional[MacAddressString]
        hints = typing.get_type_hints(IEEE1722TpConnection.setPduRef)
        assert hints["value"] == Optional[RefType]
        hints = typing.get_type_hints(IEEE1722TpConnection.getUniqueStreamId)
        assert hints["return"] == Optional[PositiveInteger]
