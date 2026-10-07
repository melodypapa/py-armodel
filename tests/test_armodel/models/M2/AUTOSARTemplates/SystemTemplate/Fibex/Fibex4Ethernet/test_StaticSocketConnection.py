"""Model unit tests for StaticSocketConnection — Table 6.201, p.544 (R23-11).

Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.201, p.544 (pre-caption split render).
Base most-derived = Identifiable; attributes iPduIdentifier (SoConIPduIdentifier, *,
ref → plural iPduIdentifierRefs), remoteAddress (SocketAddress, 0..1, ref →
remoteAddressRef), tcpConnectTimeout (TimeValue), tcpRole (TcpRoleEnum). VP-capable
(VARIATION-POINT in XSD group, AUTOSAR_00052.xsd l.113239).
"""

import typing

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import StaticSocketConnection, TcpRoleEnum


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


class TestStaticSocketConnection:
    def test_inheritance(self):
        connection = StaticSocketConnection(AUTOSAR.getInstance(), "Conn1")
        assert isinstance(connection, Identifiable)
        assert connection.getShortName() == "Conn1"

    def test_initialization(self):
        connection = StaticSocketConnection(AUTOSAR.getInstance(), "Conn1")
        assert connection.getIPduIdentifierRefs() == []
        assert connection.getRemoteAddressRef() is None
        assert connection.getTcpConnectTimeout() is None
        assert connection.getTcpRole() is None

    def test_add_ipdu_identifier_ref(self):
        connection = StaticSocketConnection(AUTOSAR.getInstance(), "Conn1")
        ref_1 = RefType().setValue("/Ecu/SoCon/IPdu1")
        ref_2 = RefType().setValue("/Ecu/SoCon/IPdu2")

        result = connection.addIPduIdentifierRef(ref_1)
        assert result is connection
        connection.addIPduIdentifierRef(ref_2)
        refs = connection.getIPduIdentifierRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/Ecu/SoCon/IPdu1"
        assert refs[1].getValue() == "/Ecu/SoCon/IPdu2"

    def test_add_ipdu_identifier_ref_none_no_op(self):
        connection = StaticSocketConnection(AUTOSAR.getInstance(), "Conn1")
        ref_1 = RefType().setValue("/Ecu/SoCon/IPdu1")
        connection.addIPduIdentifierRef(ref_1)
        connection.addIPduIdentifierRef(None)
        assert connection.getIPduIdentifierRefs() == [ref_1]

    def test_get_set_remote_address_ref(self):
        connection = StaticSocketConnection(AUTOSAR.getInstance(), "Conn1")
        remote_ref = RefType().setDest("SOCKET-ADDRESS").setValue("/Ecu/SoAd/SocketAddress/Remote")

        result = connection.setRemoteAddressRef(remote_ref)
        assert result is connection
        assert connection.getRemoteAddressRef() is remote_ref
        connection.setRemoteAddressRef(None)
        assert connection.getRemoteAddressRef() is remote_ref

    def test_get_set_tcp_connect_timeout(self):
        connection = StaticSocketConnection(AUTOSAR.getInstance(), "Conn1")
        timeout = TimeValue().setValue(30)

        result = connection.setTcpConnectTimeout(timeout)
        assert result is connection
        assert connection.getTcpConnectTimeout() is timeout
        connection.setTcpConnectTimeout(None)
        assert connection.getTcpConnectTimeout() is timeout

    def test_get_set_tcp_role(self):
        connection = StaticSocketConnection(AUTOSAR.getInstance(), "Conn1")
        role = TcpRoleEnum().setValue(TcpRoleEnum.CONNECT)

        result = connection.setTcpRole(role)
        assert result is connection
        assert connection.getTcpRole() is role
        assert connection.getTcpRole().getValue() == "CONNECT"
        connection.setTcpRole(None)
        assert connection.getTcpRole() is role

    def test_type_annotations(self):
        connection = StaticSocketConnection(AUTOSAR.getInstance(), "Conn1")
        assert typing.get_type_hints(connection.setRemoteAddressRef)["ref"] == typing.Optional[RefType]
        assert typing.get_type_hints(connection.setTcpConnectTimeout)["value"] == typing.Optional[TimeValue]
        assert typing.get_type_hints(connection.setTcpRole)["value"] == typing.Optional[TcpRoleEnum]
        assert typing.get_type_hints(connection.getIPduIdentifierRefs)["return"] == typing.List[RefType]

    def test_class_docstring_verbatim(self):
        assert StaticSocketConnection.__doc__.strip() == ("Definition of static SocketConnection between the Socket that is defined by the aggregating SocketAddress and the remoteAddress.")

    def test_ipdu_identifier_note_verbatim(self):
        connection = StaticSocketConnection(AUTOSAR.getInstance(), "Conn1")
        note = "Assignment of IPduIdentifiers that are transmitted over the static SocketConnection. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=iPduIdentifier.soConIPduIdentifier, iPduIdentifier.variationPoint.shortLabel vh.latestBindingTime=postBuild"
        assert connection.getIPduIdentifierRefs.__doc__ == note
        assert "A None value is a no-op and does not append to iPduIdentifierRefs." in connection.addIPduIdentifierRef.__doc__

    def test_remote_address_note_verbatim(self):
        connection = StaticSocketConnection(AUTOSAR.getInstance(), "Conn1")
        note = "RemoteAddress of the static SocketConnection. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=remoteAddress.socketAddress, remoteAddress.variationPoint.shortLabel vh.latestBindingTime=postBuild"
        assert connection.getRemoteAddressRef.__doc__ == note
        assert "A None value is a no-op and does not overwrite an existing remoteAddressRef." in connection.setRemoteAddressRef.__doc__
