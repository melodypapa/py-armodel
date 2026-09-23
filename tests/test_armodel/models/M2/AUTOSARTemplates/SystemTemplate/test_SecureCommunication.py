import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, MacAddressString, PositiveInteger, String, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import (
    CryptoCertificateAlgorithmFamilyEnum,
    CryptoCertificateFormatEnum,
    CryptoEllipticCurveProps,
    CryptoServiceCertificate,
    CryptoServiceMapping,
    CryptoServicePrimitive,
    CryptoSignatureScheme,
    MacSecCapabilityEnum,
    MacSecCipherSuiteConfig,
    MacSecConfidentialityOffsetEnum,
    MacSecCryptoAlgoConfig,
    MacSecFailPermissiveModeEnum,
    MacSecGlobalKayProps,
    MacSecKayParticipant,
    MacSecLocalKayProps,
    MacSecProps,
    MacSecRoleEnum,
    SecOcCryptoServiceMapping,
    TlsCryptoCipherSuiteProps,
    TlsCryptoServiceMapping,
    TlsPskIdentity,
    TlsVersionEnum,
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
        """Test TlsCryptoServiceMapping class functionality (Table 6.211, p.560)."""
        parent = MockParent()
        mapping = TlsCryptoServiceMapping(parent, "test_tls_mapping")

        assert isinstance(mapping, CryptoServiceMapping)

        # Test default values (spec displayed order: keyExchange, tlsCipherSuite,
        # useClientAuthenticationRequest, useSecurityExtensionRecordSizeLimit)
        assert mapping.getKeyExchangeRefs() == []
        assert mapping.getTlsCipherSuites() == []
        assert mapping.getUseClientAuthenticationRequest() is None
        assert mapping.getUseSecurityExtensionRecordSizeLimit() is None

        # Test keyExchange * ref list accessor (add + None no-op + chaining)
        assert mapping.addKeyExchangeRef(_ref("/Crypto/Primitives/Ke1")) is mapping
        mapping.addKeyExchangeRef(_ref("/Crypto/Primitives/Ke2"))
        assert [r.getValue() for r in mapping.getKeyExchangeRefs()] == ["/Crypto/Primitives/Ke1", "/Crypto/Primitives/Ke2"]
        mapping.addKeyExchangeRef(None)
        assert len(mapping.getKeyExchangeRefs()) == 2

        # Test boolean attribute round-trips + None no-ops
        client_auth = _bool("true")
        assert mapping.setUseClientAuthenticationRequest(client_auth) is mapping
        assert mapping.getUseClientAuthenticationRequest() is client_auth
        record_limit = _bool("false")
        assert mapping.setUseSecurityExtensionRecordSizeLimit(record_limit) is mapping
        assert mapping.getUseSecurityExtensionRecordSizeLimit() is record_limit
        mapping.setUseClientAuthenticationRequest(None)
        mapping.setUseSecurityExtensionRecordSizeLimit(None)
        assert mapping.getUseClientAuthenticationRequest() is client_auth
        assert mapping.getUseSecurityExtensionRecordSizeLimit() is record_limit


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


class Test_CryptoServiceMappingSpec:
    """Spec contract of CryptoServiceMapping (AUTOSAR_CP_TPS_SystemTemplate, Table 6.48, p.375)."""

    def test_docstring_is_spec_note_verbatim(self):
        note = "This meta-class represents an abstract base class for specializations of crypto service mappings."
        assert CryptoServiceMapping.__doc__.strip() == note

    def test_init_has_no_docstring(self):
        assert CryptoServiceMapping.__init__.__doc__ is None

    def test_abstract_raise(self):
        parent = MockParent()
        with pytest.raises(TypeError, match="CryptoServiceMapping is an abstract class"):
            CryptoServiceMapping(parent, "abstract_mapping")

    def test_subclass_heritage(self):
        assert issubclass(SecOcCryptoServiceMapping, CryptoServiceMapping)
        assert issubclass(TlsCryptoServiceMapping, CryptoServiceMapping)
        assert issubclass(CryptoServiceMapping, Identifiable)


class Test_TlsCryptoServiceMappingSpec:
    """Spec contract of TlsCryptoServiceMapping (AUTOSAR_CP_TPS_SystemTemplate, Table 6.211, p.560)."""

    def test_docstring_is_spec_note_verbatim(self):
        note = "This meta-class has the ability to represent a crypto service mapping for the socket-based configuration of Transport Layer Security (TLS)."
        assert TlsCryptoServiceMapping.__doc__.strip() == note

    def test_init_has_no_docstring(self):
        assert TlsCryptoServiceMapping.__init__.__doc__ is None

    def test_heritage(self):
        parent = MockParent()
        mapping = TlsCryptoServiceMapping(parent, "tls_map")
        assert isinstance(mapping, CryptoServiceMapping)
        assert isinstance(mapping, Identifiable)


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
        assert props.getGlobalKayPropsRef() is None
        assert props.getKeyServerPriority() is None
        assert props.getMkaParticipantRefs() == []
        assert props.getRole() is None
        assert props.getSourceMacAddress() is None

    def test_setters_and_getters(self):
        props = MacSecLocalKayProps()
        props.setDestinationMacAddress(_mac("00-11-22-33-44-55"))
        props.setGlobalKayPropsRef(_ref("/Sec/MacSecGlobalKay"))
        props.setKeyServerPriority(_pos_int("16"))
        props.addMkaParticipantRef(_ref("/Sec/MkaParticipant1"))
        props.addMkaParticipantRef(_ref("/Sec/MkaParticipant2"))
        role = MacSecRoleEnum()
        role.setValue("keyServer")
        props.setRole(role)
        props.setSourceMacAddress(_mac("AA-BB-CC-DD-EE-FF"))

        assert props.getDestinationMacAddress().getValue() == "00-11-22-33-44-55"
        assert props.getGlobalKayPropsRef().getValue() == "/Sec/MacSecGlobalKay"
        assert props.getKeyServerPriority().getValue() == 16
        assert [r.getValue() for r in props.getMkaParticipantRefs()] == ["/Sec/MkaParticipant1", "/Sec/MkaParticipant2"]
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


class Test_MacSecCryptoAlgoConfig:
    def test_defaults(self):
        config = MacSecCryptoAlgoConfig()
        assert isinstance(config, ARObject)
        assert config.getCapability() is None
        assert config.getCipherSuiteConfigs() == []
        assert config.getConfidentialityOffset() is None
        assert config.getReplayProtection() is None
        assert config.getReplayProtectionWindow() is None

    def test_get_set_capability(self):
        config = MacSecCryptoAlgoConfig()
        capability = MacSecCapabilityEnum()
        capability.setValue("intergrityAndConfidentiality")
        assert config.setCapability(capability) is config
        assert config.getCapability() is capability

    def test_get_set_confidentiality_offset(self):
        config = MacSecCryptoAlgoConfig()
        offset = MacSecConfidentialityOffsetEnum()
        offset.setValue("CONFIDENTIALITY-OFFSET-30")
        assert config.setConfidentialityOffset(offset) is config
        assert config.getConfidentialityOffset() is offset

    def test_get_set_replay_protection(self):
        config = MacSecCryptoAlgoConfig()
        replay = _bool("true")
        assert config.setReplayProtection(replay) is config
        assert config.getReplayProtection() is replay

    def test_get_set_replay_protection_window(self):
        config = MacSecCryptoAlgoConfig()
        window = _pos_int("100")
        assert config.setReplayProtectionWindow(window) is config
        assert config.getReplayProtectionWindow() is window

    def test_create_and_get_cipher_suite_configs(self):
        config = MacSecCryptoAlgoConfig()
        c1 = config.createCipherSuiteConfig()
        c2 = config.createCipherSuiteConfig()
        assert isinstance(c1, MacSecCipherSuiteConfig)
        assert isinstance(c2, MacSecCipherSuiteConfig)
        assert config.getCipherSuiteConfigs() == [c1, c2]

    def test_none_is_noop(self):
        config = MacSecCryptoAlgoConfig()
        assert config.setCapability(None) is config
        assert config.setConfidentialityOffset(None) is config
        assert config.setReplayProtection(None) is config
        assert config.setReplayProtectionWindow(None) is config
        assert config.getCapability() is None
        assert config.getConfidentialityOffset() is None
        assert config.getReplayProtection() is None
        assert config.getReplayProtectionWindow() is None


class Test_MacSecKayParticipant:
    def test_defaults(self):
        parent = MockParent()
        participant = MacSecKayParticipant(parent, "test_kay_participant")
        assert isinstance(participant, Identifiable)
        assert participant.getCknRef() is None
        assert participant.getCryptoAlgoConfig() is None
        assert participant.getSakRef() is None

    def test_get_set_ckn(self):
        parent = MockParent()
        participant = MacSecKayParticipant(parent, "test_kay_participant")
        ckn = _ref("/Sec/CryptoKeyCkn")
        assert participant.setCknRef(ckn) is participant
        assert participant.getCknRef() is ckn

    def test_get_set_crypto_algo_config(self):
        parent = MockParent()
        participant = MacSecKayParticipant(parent, "test_kay_participant")
        config = MacSecCryptoAlgoConfig()
        assert participant.setCryptoAlgoConfig(config) is participant
        assert participant.getCryptoAlgoConfig() is config

    def test_get_set_sak(self):
        parent = MockParent()
        participant = MacSecKayParticipant(parent, "test_kay_participant")
        sak = _ref("/Sec/CryptoKeySak")
        assert participant.setSakRef(sak) is participant
        assert participant.getSakRef() is sak

    def test_none_is_noop(self):
        parent = MockParent()
        participant = MacSecKayParticipant(parent, "test_kay_participant")
        assert participant.setCknRef(None) is participant
        assert participant.setCryptoAlgoConfig(None) is participant
        assert participant.setSakRef(None) is participant
        assert participant.getCknRef() is None
        assert participant.getCryptoAlgoConfig() is None
        assert participant.getSakRef() is None


class Test_TlsVersionEnum:
    def test_TlsVersionEnum(self):
        # spec literals per Table 6.213 (tls12 idx0, tls13 idx2); xml values TLS-12/TLS-13 per XSD
        assert TlsVersionEnum.TLS_12 == "TLS-12"
        assert TlsVersionEnum.TLS_13 == "TLS-13"
        e = TlsVersionEnum()
        e.setValue("TLS-13")
        assert e.getValue() == "TLS-13"
        assert e.getText() == "TLS-13"


class Test_TlsPskIdentity:
    def test_initialization(self):
        # Table 6.214, p.563 — all three members optional (XSD minOccurs=0)
        p = TlsPskIdentity()
        assert p.getPreSharedKeyRef() is None
        assert p.getPskIdentity() is None
        assert p.getPskIdentityHint() is None

    def test_get_set_round_trip(self):
        p = TlsPskIdentity()
        p.setPreSharedKeyRef("/CryptoServiceKeys/CryptoServiceKey_Master")
        assert p.getPreSharedKeyRef() == "/CryptoServiceKeys/CryptoServiceKey_Master"
        p.setPskIdentity("psk_id_1")
        assert p.getPskIdentity() == "psk_id_1"
        p.setPskIdentityHint("hint_1")
        assert p.getPskIdentityHint() == "hint_1"

    def test_setter_none_no_op_and_chaining(self):
        p = TlsPskIdentity()
        p.setPskIdentity("keep")
        assert p.setPreSharedKeyRef(None) is p
        assert p.setPskIdentity(None) is p
        assert p.setPskIdentityHint(None) is p
        assert p.getPskIdentity() == "keep"


class Test_CryptoServicePrimitiveSpec:
    """Spec contract of CryptoServicePrimitive (AUTOSAR_CP_TPS_SystemTemplate, Table 6.50, p.376)."""

    def test_docstring_is_spec_note_verbatim(self):
        note = "This meta-class has the ability to represent a crypto primitive. Tags: atp.recommendedPackage=CryptoPrimitives"
        assert CryptoServicePrimitive.__doc__.strip() == note

    def test_init_has_no_docstring(self):
        assert CryptoServicePrimitive.__init__.__doc__ is None

    def test_heritage(self):
        parent = MockParent()
        primitive = CryptoServicePrimitive(parent, "prim")
        assert isinstance(primitive, ARElement)
        assert isinstance(primitive, Identifiable)

    def test_initialization(self):
        # Table 6.50 — all three attributes optional (Mult 0..1, XSD minOccurs=0)
        parent = MockParent()
        primitive = CryptoServicePrimitive(parent, "prim")
        assert primitive.getAlgorithmFamily() is None
        assert primitive.getAlgorithmMode() is None
        assert primitive.getAlgorithmSecondaryFamily() is None

    def test_get_set_algorithm_family(self):
        parent = MockParent()
        primitive = CryptoServicePrimitive(parent, "prim")
        family = _string("AES")
        assert primitive.setAlgorithmFamily(family) is primitive
        assert primitive.getAlgorithmFamily() is family
        primitive.setAlgorithmFamily(None)
        assert primitive.getAlgorithmFamily() is family

    def test_get_set_algorithm_mode(self):
        parent = MockParent()
        primitive = CryptoServicePrimitive(parent, "prim")
        mode = _string("CMAC")
        assert primitive.setAlgorithmMode(mode) is primitive
        assert primitive.getAlgorithmMode() is mode
        primitive.setAlgorithmMode(None)
        assert primitive.getAlgorithmMode() is mode

    def test_get_set_algorithm_secondary_family(self):
        parent = MockParent()
        primitive = CryptoServicePrimitive(parent, "prim")
        secondary = _string("SHA2")
        assert primitive.setAlgorithmSecondaryFamily(secondary) is primitive
        assert primitive.getAlgorithmSecondaryFamily() is secondary
        primitive.setAlgorithmSecondaryFamily(None)
        assert primitive.getAlgorithmSecondaryFamily() is secondary


class Test_TlsCryptoCipherSuitePropsSpec:
    """Spec contract of TlsCryptoCipherSuiteProps (AUTOSAR_CP_TPS_SystemTemplate, Table 6.215, p.563)."""

    def test_docstring_is_spec_note_verbatim(self):
        note = "This meta-class provides attributes to specify details of TLS Cipher Suites."
        assert TlsCryptoCipherSuiteProps.__doc__.strip() == note

    def test_init_has_no_docstring(self):
        assert TlsCryptoCipherSuiteProps.__init__.__doc__ is None

    def test_heritage(self):
        # Base chain ARObject, Identifiable, MultilanguageReferrable, Referrable — most-derived is Identifiable
        parent = MockParent()
        props = TlsCryptoCipherSuiteProps(parent, "props")
        assert isinstance(props, Identifiable)
        assert not isinstance(props, ARElement)

    def test_initialization(self):
        # Table 6.215 — the single attribute is optional (Mult 0..1, XSD minOccurs=0)
        parent = MockParent()
        props = TlsCryptoCipherSuiteProps(parent, "props")
        assert props.getTcpIpTlsUseSecurityExtensionForceEncryptThenMac() is None

    def test_get_set_tcp_ip_tls_use_security_extension_force_encrypt_then_mac(self):
        parent = MockParent()
        props = TlsCryptoCipherSuiteProps(parent, "props")
        flag = _bool(True)
        assert props.setTcpIpTlsUseSecurityExtensionForceEncryptThenMac(flag) is props
        assert props.getTcpIpTlsUseSecurityExtensionForceEncryptThenMac() is flag
        props.setTcpIpTlsUseSecurityExtensionForceEncryptThenMac(None)
        assert props.getTcpIpTlsUseSecurityExtensionForceEncryptThenMac() is flag


class Test_CryptoEllipticCurvePropsSpec:
    """Spec contract of CryptoEllipticCurveProps (AUTOSAR_CP_TPS_SystemTemplate, Table 6.216, p.564)."""

    def test_docstring_is_spec_note_verbatim(self):
        note = "This meta-class provides attributes to specify the properties of elliptic curves. Tags: atp.recommendedPackage=CryptoEllipticCurveProps"
        assert CryptoEllipticCurveProps.__doc__.strip() == note

    def test_init_has_no_docstring(self):
        assert CryptoEllipticCurveProps.__init__.__doc__ is None

    def test_heritage(self):
        # Base chain ARObject, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, ARElement — most-derived is ARElement
        parent = MockParent()
        props = CryptoEllipticCurveProps(parent, "curve")
        assert isinstance(props, ARElement)
        assert isinstance(props, Identifiable)

    def test_initialization(self):
        # Table 6.216 — the single attribute is optional (Mult 0..1, XSD minOccurs=0)
        parent = MockParent()
        props = CryptoEllipticCurveProps(parent, "curve")
        assert props.getNamedCurveId() is None

    def test_get_set_named_curve_id(self):
        parent = MockParent()
        props = CryptoEllipticCurveProps(parent, "curve")
        curve_id = _pos_int("23")
        assert props.setNamedCurveId(curve_id) is props
        assert props.getNamedCurveId() is curve_id
        props.setNamedCurveId(None)
        assert props.getNamedCurveId() is curve_id


class Test_CryptoSignatureSchemeSpec:
    """Spec contract of CryptoSignatureScheme (AUTOSAR_CP_TPS_SystemTemplate, Table 6.217, p.564)."""

    def test_docstring_is_spec_note_verbatim(self):
        note = "This meta-class provides attributes to specify the TLS Signature Scheme. Tags: atp.recommendedPackage=CryptoSignatureSchemas"
        assert CryptoSignatureScheme.__doc__.strip() == note

    def test_init_has_no_docstring(self):
        assert CryptoSignatureScheme.__init__.__doc__ is None

    def test_heritage(self):
        # Base chain ARObject, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, ARElement — most-derived is ARElement
        parent = MockParent()
        scheme = CryptoSignatureScheme(parent, "scheme")
        assert isinstance(scheme, ARElement)
        assert isinstance(scheme, Identifiable)

    def test_initialization(self):
        # Table 6.217 — the single attribute is optional (Mult 0..1, XSD minOccurs=0)
        parent = MockParent()
        scheme = CryptoSignatureScheme(parent, "scheme")
        assert scheme.getSignatureSchemeId() is None

    def test_get_set_signature_scheme_id(self):
        parent = MockParent()
        scheme = CryptoSignatureScheme(parent, "scheme")
        scheme_id = _pos_int("7")
        assert scheme.setSignatureSchemeId(scheme_id) is scheme
        assert scheme.getSignatureSchemeId() is scheme_id
        scheme.setSignatureSchemeId(None)
        assert scheme.getSignatureSchemeId() is scheme_id


class Test_CryptoServiceCertificateSpec:
    """Spec contract of CryptoServiceCertificate (AUTOSAR_CP_TPS_SystemTemplate, Table 6.218, p.565)."""

    def test_docstring_is_spec_note_verbatim(self):
        note = "This meta-class represents the ability to model a cryptographic certificate. Tags: atp.recommendedPackage=CryptoServiceCertificates"
        assert CryptoServiceCertificate.__doc__.strip() == note

    def test_init_has_no_docstring(self):
        assert CryptoServiceCertificate.__init__.__doc__ is None

    def test_heritage(self):
        # Base chain ARObject, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, ARElement — most-derived is ARElement
        parent = MockParent()
        certificate = CryptoServiceCertificate(parent, "certificate")
        assert isinstance(certificate, ARElement)
        assert isinstance(certificate, Identifiable)

    def test_initialization(self):
        # Table 6.218 — all five attributes are optional (Mult 0..1, XSD minOccurs=0)
        parent = MockParent()
        certificate = CryptoServiceCertificate(parent, "certificate")
        assert certificate.getAlgorithmFamily() is None
        assert certificate.getFormat() is None
        assert certificate.getMaximumLength() is None
        assert certificate.getNextHigherCertificateRef() is None
        assert certificate.getServerNameIdentification() is None

    def test_get_set_algorithm_family(self):
        parent = MockParent()
        certificate = CryptoServiceCertificate(parent, "certificate")
        family = CryptoCertificateAlgorithmFamilyEnum().setValue(CryptoCertificateAlgorithmFamilyEnum.RSA)
        assert certificate.setAlgorithmFamily(family) is certificate
        assert certificate.getAlgorithmFamily() is family
        certificate.setAlgorithmFamily(None)
        assert certificate.getAlgorithmFamily() is family

    def test_get_set_format(self):
        parent = MockParent()
        certificate = CryptoServiceCertificate(parent, "certificate")
        fmt = CryptoCertificateFormatEnum().setValue(CryptoCertificateFormatEnum.X_509)
        assert certificate.setFormat(fmt) is certificate
        assert certificate.getFormat() is fmt
        certificate.setFormat(None)
        assert certificate.getFormat() is fmt

    def test_get_set_maximum_length(self):
        parent = MockParent()
        certificate = CryptoServiceCertificate(parent, "certificate")
        length = _pos_int("4096")
        assert certificate.setMaximumLength(length) is certificate
        assert certificate.getMaximumLength() is length
        certificate.setMaximumLength(None)
        assert certificate.getMaximumLength() is length

    def test_get_set_next_higher_certificate_ref(self):
        parent = MockParent()
        certificate = CryptoServiceCertificate(parent, "certificate")
        ref = _ref("/Package/HigherCertificate")
        assert certificate.setNextHigherCertificateRef(ref) is certificate
        assert certificate.getNextHigherCertificateRef() is ref
        certificate.setNextHigherCertificateRef(None)
        assert certificate.getNextHigherCertificateRef() is ref

    def test_get_set_server_name_identification(self):
        parent = MockParent()
        certificate = CryptoServiceCertificate(parent, "certificate")
        sni = _string("example.com")
        assert certificate.setServerNameIdentification(sni) is certificate
        assert certificate.getServerNameIdentification() is sni
        certificate.setServerNameIdentification(None)
        assert certificate.getServerNameIdentification() is sni


class Test_CryptoCertificateAlgorithmFamilyEnum:
    def test_docstring_is_spec_note_verbatim(self):
        # Table 6.219, p.565 — class Note verbatim from the markdown
        note = "This meta-class defies possible cryptographic algorithm families used to create public keys and signatures within the certificate."
        assert CryptoCertificateAlgorithmFamilyEnum.__doc__.strip() == note

    def test_init_has_no_docstring(self):
        assert CryptoCertificateAlgorithmFamilyEnum.__init__.__doc__ is None

    def test_literal_values_and_indexes(self):
        # spec literals per Table 6.219 (ecc idx2, rsa idx1, displayed order ecc→rsa); xml values ECC/RSA per XSD
        assert CryptoCertificateAlgorithmFamilyEnum.ECC == "ECC"
        assert CryptoCertificateAlgorithmFamilyEnum.RSA == "RSA"
        e = CryptoCertificateAlgorithmFamilyEnum()
        assert e.getEnumValues() == ["ECC", "RSA"]
        assert e.validateEnumValue("ECC") is True
        assert e.validateEnumValue("RSA") is True
        assert e.validateEnumValue("DSA") is False

    def test_instantiation(self):
        e = CryptoCertificateAlgorithmFamilyEnum()
        e.setValue(CryptoCertificateAlgorithmFamilyEnum.RSA)
        assert e.getValue() == "RSA"
        assert e.getText() == "RSA"
        e.setValue(CryptoCertificateAlgorithmFamilyEnum.ECC)
        assert e.getValue() == "ECC"
        assert e.getText() == "ECC"


class Test_CryptoCertificateFormatEnum:
    def test_docstring_is_spec_note_verbatim(self):
        # Table 6.220, p.565 — class Note verbatim from the markdown
        note = "This meta-class defines possible formats of cryptographic certificates."
        assert CryptoCertificateFormatEnum.__doc__.strip() == note

    def test_init_has_no_docstring(self):
        assert CryptoCertificateFormatEnum.__init__.__doc__ is None

    def test_literal_values_and_indexes(self):
        # spec literals per Table 6.220 (cvc idx2, x509 idx1, displayed order cvc→x509); xml values CVC/X-509 per XSD
        assert CryptoCertificateFormatEnum.CVC == "CVC"
        assert CryptoCertificateFormatEnum.X_509 == "X-509"
        e = CryptoCertificateFormatEnum()
        assert e.getEnumValues() == ["CVC", "X-509"]
        assert e.validateEnumValue("CVC") is True
        assert e.validateEnumValue("X-509") is True
        assert e.validateEnumValue("PEM") is False

    def test_instantiation(self):
        e = CryptoCertificateFormatEnum()
        e.setValue(CryptoCertificateFormatEnum.X_509)
        assert e.getValue() == "X-509"
        assert e.getText() == "X-509"
        e.setValue(CryptoCertificateFormatEnum.CVC)
        assert e.getValue() == "CVC"
        assert e.getText() == "CVC"
