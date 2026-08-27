import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, MacAddressString, PositiveInteger, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import (
    CryptoServiceMapping,
    MacSecFailPermissiveModeEnum,
    MacSecLocalKayProps,
    MacSecProps,
    MacSecRoleEnum,
    SecOcCryptoServiceMapping,
    TlsCryptoServiceMapping,
)


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class Test_SecureCommunication:
    """Test cases for SecureCommunication-related classes."""

    def test_CryptoServiceMapping(self):
        """Test CryptoServiceMapping abstract class functionality."""
        parent = MockParent()

        # Test that CryptoServiceMapping cannot be instantiated directly
        with pytest.raises(TypeError, match="CryptoServiceMapping is an abstract class"):
            CryptoServiceMapping(parent, "test_crypto_mapping")

        # Test that a concrete subclass can be instantiated
        mapping = SecOcCryptoServiceMapping(parent, "test_crypto_mapping")
        assert isinstance(mapping, Identifiable)
        assert isinstance(mapping, CryptoServiceMapping)

    def test_SecOcCryptoServiceMapping(self):
        """Test SecOcCryptoServiceMapping class functionality."""
        parent = MockParent()
        mapping = SecOcCryptoServiceMapping(parent, "test_secoc_mapping")

        assert isinstance(mapping, CryptoServiceMapping)

        # Test default values
        assert mapping.getAuthenticationRef() is None
        assert mapping.getCryptoServiceKeyRef() is None
        assert mapping.getCryptoServiceQueueRef() is None

        # Test setter/getter methods
        mock_auth_ref = "mock_auth_ref"
        mapping.setAuthenticationRef(mock_auth_ref)
        assert mapping.getAuthenticationRef() == mock_auth_ref

        mock_key_ref = "mock_key_ref"
        mapping.setCryptoServiceKeyRef(mock_key_ref)
        assert mapping.getCryptoServiceKeyRef() == mock_key_ref

        mock_queue_ref = "mock_queue_ref"
        mapping.setCryptoServiceQueueRef(mock_queue_ref)
        assert mapping.getCryptoServiceQueueRef() == mock_queue_ref

    def test_TlsCryptoServiceMapping(self):
        """Test TlsCryptoServiceMapping class functionality."""
        parent = MockParent()
        mapping = TlsCryptoServiceMapping(parent, "test_tls_mapping")

        assert isinstance(mapping, CryptoServiceMapping)

        # Test default values
        assert mapping.getKeyExchangeRef() is None
        assert mapping.getTlsCipherSuites() == []
        assert mapping.getUseClientAuthenticationRequest() is None
        assert mapping.getUseSecurityExtensionRecordSizeLimit() is None

        # Test setter/getter methods
        mock_key_ref = "mock_key_ref"
        mapping.setKeyExchangeRef(mock_key_ref)
        assert mapping.getKeyExchangeRef() == mock_key_ref

        mock_cipher_suite = "AES_128_GCM"
        mapping.addTlsCipherSuite(mock_cipher_suite)
        assert mapping.getTlsCipherSuites() == [mock_cipher_suite]

        mapping.setUseClientAuthenticationRequest(True)
        assert mapping.getUseClientAuthenticationRequest() is True

        mapping.setUseSecurityExtensionRecordSizeLimit(False)
        assert mapping.getUseSecurityExtensionRecordSizeLimit() is False


def _mac(value):
    mac = MacAddressString()
    mac.setValue(value)
    return mac


def _bool(value):
    b = Boolean()
    b.setValue(value)
    return b


def _time(value):
    t = TimeValue()
    t.setValue(value)
    return t


def _pos_int(value):
    p = PositiveInteger()
    p.setValue(value)
    return p


def _ref(value):
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

    ref = RefType()
    ref.setValue(value)
    return ref


class Test_MacSecEnums:
    def test_MacSecRoleEnum(self):
        assert MacSecRoleEnum.PEER == "PEER"
        assert MacSecRoleEnum.KEY_SERVER == "KEY-SERVER"
        e = MacSecRoleEnum()
        e.setValue("KEY-SERVER")
        assert e.getValue() == "KEY-SERVER"
        assert e.getText() == "KEY-SERVER"

    def test_MacSecFailPermissiveModeEnum(self):
        assert MacSecFailPermissiveModeEnum.NEVER == "NEVER"
        assert MacSecFailPermissiveModeEnum.TIMEOUT == "TIMEOUT"
        e = MacSecFailPermissiveModeEnum()
        e.setValue("TIMEOUT")
        assert e.getValue() == "TIMEOUT"
        assert e.getText() == "TIMEOUT"


class Test_MacSecLocalKayProps:
    def test_defaults(self):
        props = MacSecLocalKayProps()
        assert props.getDestinationMacAddress() is None
        assert props.getGlobalKayProps() is None
        assert props.getKeyServerPriority() is None
        assert props.getMkaParticipant() == []
        assert props.getRole() is None
        assert props.getSourceMacAddress() is None

    def test_setters_and_getters(self):
        props = MacSecLocalKayProps()
        props.setDestinationMacAddress(_mac("00-11-22-33-44-55"))
        props.setGlobalKayProps(_ref("/Sec/MacSecGlobalKay"))
        props.setKeyServerPriority(_pos_int("16"))
        props.addMkaParticipant(_ref("/Sec/MkaParticipant1"))
        props.addMkaParticipant(_ref("/Sec/MkaParticipant2"))
        role = MacSecRoleEnum()
        role.setValue("KEY-SERVER")
        props.setRole(role)
        props.setSourceMacAddress(_mac("AA-BB-CC-DD-EE-FF"))

        assert props.getDestinationMacAddress().getValue() == "00-11-22-33-44-55"
        assert props.getGlobalKayProps().getValue() == "/Sec/MacSecGlobalKay"
        assert props.getKeyServerPriority().getValue() == 16
        assert [r.getValue() for r in props.getMkaParticipant()] == ["/Sec/MkaParticipant1", "/Sec/MkaParticipant2"]
        assert props.getRole().getValue() == "KEY-SERVER"
        assert props.getSourceMacAddress().getValue() == "AA-BB-CC-DD-EE-FF"

    def test_none_is_noop(self):
        props = MacSecLocalKayProps()
        props.setDestinationMacAddress(None)
        props.setRole(None)
        assert props.getDestinationMacAddress() is None
        assert props.getRole() is None


class Test_MacSecProps:
    def test_defaults(self):
        props = MacSecProps()
        assert props.getAutoStart() is None
        assert props.getMacSecKayConfig() is None
        assert props.getOnFailPermissiveMode() is None
        assert props.getOnFailPermissiveModeTimeout() is None
        assert props.getSakRekeyTimeSpan() is None

    def test_setters_and_getters(self):
        props = MacSecProps()
        props.setAutoStart(_bool("true"))
        kay = MacSecLocalKayProps()
        kay.setKeyServerPriority(_pos_int("16"))
        props.setMacSecKayConfig(kay)
        fail_mode = MacSecFailPermissiveModeEnum()
        fail_mode.setValue("TIMEOUT")
        props.setOnFailPermissiveMode(fail_mode)
        props.setOnFailPermissiveModeTimeout(_time("30.0"))
        props.setSakRekeyTimeSpan(_time("3600.0"))

        assert props.getAutoStart().getValue() is True
        assert isinstance(props.getMacSecKayConfig(), MacSecLocalKayProps)
        assert props.getMacSecKayConfig().getKeyServerPriority().getValue() == 16
        assert props.getOnFailPermissiveMode().getValue() == "TIMEOUT"
        assert props.getOnFailPermissiveModeTimeout().getValue() == 30.0
        assert props.getSakRekeyTimeSpan().getValue() == 3600.0

    def test_none_is_noop(self):
        props = MacSecProps()
        props.setAutoStart(None)
        props.setOnFailPermissiveMode(None)
        assert props.getAutoStart() is None
        assert props.getOnFailPermissiveMode() is None
