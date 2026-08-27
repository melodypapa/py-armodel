import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement, Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, MacAddressString, PositiveInteger, String, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import (
    CryptoServiceMapping,
    MacSecCapabilityEnum,
    MacSecCipherSuiteConfig,
    MacSecConfidentialityOffsetEnum,
    MacSecFailPermissiveModeEnum,
    MacSecGlobalKayProps,
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


def _string(value):
    s = String()
    s.setValue(value)
    return s


def _ref(value):
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

    ref = RefType()
    ref.setValue(value)
    return ref


class Test_MacSecEnums:
    def test_MacSecRoleEnum(self):
        # spec literal names are camelCase per Table 3.127 (peer idx0, keyServer idx1)
        assert MacSecRoleEnum.PEER == "peer"
        assert MacSecRoleEnum.KEY_SERVER == "keyServer"
        e = MacSecRoleEnum()
        e.setValue("keyServer")
        assert e.getValue() == "keyServer"
        assert e.getText() == "keyServer"

    def test_MacSecFailPermissiveModeEnum(self):
        # spec literal names are the lower-case xml.name forms per Table 3.128 (never idx0, timeout idx1)
        assert MacSecFailPermissiveModeEnum.NEVER == "never"
        assert MacSecFailPermissiveModeEnum.TIMEOUT == "timeout"
        e = MacSecFailPermissiveModeEnum()
        e.setValue("timeout")
        assert e.getValue() == "timeout"
        assert e.getText() == "timeout"

    def test_MacSecCapabilityEnum(self):
        # spec literal names per Table 3.126 (intergrityWithoutConfidentiality idx0, intergrityAndConfidentiality idx1); note spec spells both "intergrity"
        assert MacSecCapabilityEnum.INTERGRITY_WITHOUT_CONFIDENTIALITY == "intergrityWithoutConfidentiality"
        assert MacSecCapabilityEnum.INTERGRITY_AND_CONFIDENTIALITY == "intergrityAndConfidentiality"
        e = MacSecCapabilityEnum()
        e.setValue("intergrityAndConfidentiality")
        assert e.getValue() == "intergrityAndConfidentiality"
        assert e.getText() == "intergrityAndConfidentiality"

    def test_MacSecConfidentialityOffsetEnum(self):
        # spec literal values are the UPPER-CASE xml.name forms per Table 3.125 (CONFIDENTIALITY-OFFSET-0 idx0, ...-30 idx1, ...-50 idx2)
        assert MacSecConfidentialityOffsetEnum.CONFIDENTIALITY_OFFSET_0 == "CONFIDENTIALITY-OFFSET-0"
        assert MacSecConfidentialityOffsetEnum.CONFIDENTIALITY_OFFSET_30 == "CONFIDENTIALITY-OFFSET-30"
        assert MacSecConfidentialityOffsetEnum.CONFIDENTIALITY_OFFSET_50 == "CONFIDENTIALITY-OFFSET-50"
        e = MacSecConfidentialityOffsetEnum()
        e.setValue("CONFIDENTIALITY-OFFSET-50")
        assert e.getValue() == "CONFIDENTIALITY-OFFSET-50"
        assert e.getText() == "CONFIDENTIALITY-OFFSET-50"


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
        role.setValue("keyServer")
        props.setRole(role)
        props.setSourceMacAddress(_mac("AA-BB-CC-DD-EE-FF"))

        assert props.getDestinationMacAddress().getValue() == "00-11-22-33-44-55"
        assert props.getGlobalKayProps().getValue() == "/Sec/MacSecGlobalKay"
        assert props.getKeyServerPriority().getValue() == 16
        assert [r.getValue() for r in props.getMkaParticipant()] == ["/Sec/MkaParticipant1", "/Sec/MkaParticipant2"]
        assert props.getRole().getValue() == "keyServer"
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


class Test_MacSecGlobalKayProps:
    def test_defaults(self):
        parent = MockParent()
        props = MacSecGlobalKayProps(parent, "test_global_kay")
        assert isinstance(props, ARElement)
        assert props.getBypassEtherTypes() == []
        assert props.getBypassVlans() == []

    def test_add_and_get(self):
        parent = MockParent()
        props = MacSecGlobalKayProps(parent, "test_global_kay")
        props.addBypassEtherType(_pos_int("88"))
        props.addBypassEtherType(_pos_int("90"))
        props.addBypassVlan(_pos_int("100"))
        assert [v.getValue() for v in props.getBypassEtherTypes()] == [88, 90]
        assert [v.getValue() for v in props.getBypassVlans()] == [100]

    def test_none_is_noop(self):
        parent = MockParent()
        props = MacSecGlobalKayProps(parent, "test_global_kay")
        props.addBypassEtherType(None)
        props.addBypassVlan(None)
        assert props.getBypassEtherTypes() == []
        assert props.getBypassVlans() == []


class Test_MacSecCipherSuiteConfig:
    def test_defaults(self):
        config = MacSecCipherSuiteConfig()
        assert isinstance(config, ARObject)
        assert config.getCipherSuite() is None
        assert config.getCipherSuitePriority() is None

    def test_get_set_cipher_suite(self):
        config = MacSecCipherSuiteConfig()
        cipher_suite = _string("GCM-AES-128")
        assert config.setCipherSuite(cipher_suite) is config
        assert config.getCipherSuite() is cipher_suite

    def test_get_set_cipher_suite_priority(self):
        config = MacSecCipherSuiteConfig()
        priority = _pos_int("1")
        assert config.setCipherSuitePriority(priority) is config
        assert config.getCipherSuitePriority() is priority

    def test_none_is_noop(self):
        config = MacSecCipherSuiteConfig()
        assert config.setCipherSuite(None) is config
        assert config.setCipherSuitePriority(None) is config
        assert config.getCipherSuite() is None
        assert config.getCipherSuitePriority() is None
