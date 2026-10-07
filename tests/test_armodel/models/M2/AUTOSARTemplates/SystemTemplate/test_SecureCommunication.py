import inspect

import pytest

from armodel.models import AUTOSAR
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
    MacSecParticipantSet,
    MacSecProps,
    MacSecRoleEnum,
    SecOcCryptoServiceMapping,
    TlsCryptoCipherSuite,
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
        """Test SecOcCryptoServiceMapping class functionality (Table 6.49, p.375)."""
        parent = MockParent()
        mapping = SecOcCryptoServiceMapping(parent, "test_secoc_mapping")

        assert isinstance(mapping, CryptoServiceMapping)

        # Test default values (spec displayed order: authentication, cryptoServiceKey, cryptoServiceQueue)
        assert mapping.getAuthenticationRef() is None
        assert mapping.getCryptoServiceKeyRef() is None
        assert mapping.getCryptoServiceQueueRef() is None

        # Test setter/getter round-trips + chaining
        auth_ref = _ref("/Crypto/Primitives/Auth")
        assert mapping.setAuthenticationRef(auth_ref) is mapping
        assert mapping.getAuthenticationRef() is auth_ref

        key_ref = _ref("/Crypto/Keys/Key1")
        assert mapping.setCryptoServiceKeyRef(key_ref) is mapping
        assert mapping.getCryptoServiceKeyRef() is key_ref

        queue_ref = _ref("/Crypto/Queues/Q1")
        assert mapping.setCryptoServiceQueueRef(queue_ref) is mapping
        assert mapping.getCryptoServiceQueueRef() is queue_ref

        # Test None no-ops
        mapping.setAuthenticationRef(None)
        mapping.setCryptoServiceKeyRef(None)
        mapping.setCryptoServiceQueueRef(None)
        assert mapping.getAuthenticationRef() is auth_ref
        assert mapping.getCryptoServiceKeyRef() is key_ref
        assert mapping.getCryptoServiceQueueRef() is queue_ref

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


class Test_SecOcCryptoServiceMappingSpec:
    """Spec contract of SecOcCryptoServiceMapping (AUTOSAR_CP_TPS_SystemTemplate, Table 6.49, p.375)."""

    def test_docstring_is_spec_note_verbatim(self):
        note = "This meta-class has the ability to represent a crypto service mapping for the Pdu-based communication via SecOC."
        assert SecOcCryptoServiceMapping.__doc__.strip() == note

    def test_init_has_no_docstring(self):
        assert SecOcCryptoServiceMapping.__init__.__doc__ is None

    def test_heritage(self):
        parent = MockParent()
        mapping = SecOcCryptoServiceMapping(parent, "secoc_map")
        assert isinstance(mapping, CryptoServiceMapping)
        assert isinstance(mapping, Identifiable)


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
        assert MacSecRoleEnum.PEER == "PEER"
        assert MacSecRoleEnum.KEY_SERVER == "KEY-SERVER"
        e = MacSecRoleEnum()
        e.setValue(MacSecRoleEnum.KEY_SERVER)
        assert e.getValue() == MacSecRoleEnum.KEY_SERVER
        assert e.getText() == MacSecRoleEnum.KEY_SERVER

    def test_MacSecFailPermissiveModeEnum(self):
        # spec literal names are the lower-case xml.name forms per Table 3.128 (never idx0, timeout idx1)
        assert MacSecFailPermissiveModeEnum.NEVER == "NEVER"
        assert MacSecFailPermissiveModeEnum.TIMEOUT == "TIMEOUT"
        e = MacSecFailPermissiveModeEnum()
        e.setValue(MacSecFailPermissiveModeEnum.TIMEOUT)
        assert e.getValue() == MacSecFailPermissiveModeEnum.TIMEOUT
        assert e.getText() == MacSecFailPermissiveModeEnum.TIMEOUT

    def test_MacSecCapabilityEnum(self):
        # spec literal names per Table 3.126 (intergrityWithoutConfidentiality idx0, intergrityAndConfidentiality idx1); note spec spells both "intergrity"
        assert MacSecCapabilityEnum.INTERGRITY_WITHOUT_CONFIDENTIALITY == "INTERGRITY-WITHOUT-CONFIDENTIALITY"
        assert MacSecCapabilityEnum.INTERGRITY_AND_CONFIDENTIALITY == "INTERGRITY-AND-CONFIDENTIALITY"
        e = MacSecCapabilityEnum()
        e.setValue(MacSecCapabilityEnum.INTERGRITY_AND_CONFIDENTIALITY)
        assert e.getValue() == MacSecCapabilityEnum.INTERGRITY_AND_CONFIDENTIALITY
        assert e.getText() == MacSecCapabilityEnum.INTERGRITY_AND_CONFIDENTIALITY

    def test_MacSecConfidentialityOffsetEnum(self):
        # spec literal values are the UPPER-CASE xml.name forms per Table 3.125 (CONFIDENTIALITY-OFFSET-0 idx0, ...-30 idx1, ...-50 idx2)
        assert MacSecConfidentialityOffsetEnum.CONFIDENTIALITY_OFFSET_0 == "CONFIDENTIALITY-OFFSET--0"
        assert MacSecConfidentialityOffsetEnum.CONFIDENTIALITY_OFFSET_30 == "CONFIDENTIALITY-OFFSET--30"
        assert MacSecConfidentialityOffsetEnum.CONFIDENTIALITY_OFFSET_50 == "CONFIDENTIALITY-OFFSET--50"
        e = MacSecConfidentialityOffsetEnum()
        e.setValue(MacSecConfidentialityOffsetEnum.CONFIDENTIALITY_OFFSET_50)
        assert e.getValue() == MacSecConfidentialityOffsetEnum.CONFIDENTIALITY_OFFSET_50
        assert e.getText() == MacSecConfidentialityOffsetEnum.CONFIDENTIALITY_OFFSET_50


class TestMacSecConfidentialityOffsetEnum:
    """Test cases for MacSecConfidentialityOffsetEnum (CP_TPS_SystemTemplate Table 3.125, p.177, R23-11)."""

    def test_member_presence_and_values(self):
        assert MacSecConfidentialityOffsetEnum.CONFIDENTIALITY_OFFSET_0 == "CONFIDENTIALITY-OFFSET--0"
        assert MacSecConfidentialityOffsetEnum.CONFIDENTIALITY_OFFSET_30 == "CONFIDENTIALITY-OFFSET--30"
        assert MacSecConfidentialityOffsetEnum.CONFIDENTIALITY_OFFSET_50 == "CONFIDENTIALITY-OFFSET--50"
        assert list(MacSecConfidentialityOffsetEnum().getEnumValues()) == [
            "CONFIDENTIALITY-OFFSET--0",
            "CONFIDENTIALITY-OFFSET--30",
            "CONFIDENTIALITY-OFFSET--50",
        ]

    def test_instantiability_round_trip(self):
        offset_0 = MacSecConfidentialityOffsetEnum().setValue(MacSecConfidentialityOffsetEnum.CONFIDENTIALITY_OFFSET_0)
        assert offset_0.getValue() == MacSecConfidentialityOffsetEnum.CONFIDENTIALITY_OFFSET_0

        offset_30 = MacSecConfidentialityOffsetEnum().setValue(MacSecConfidentialityOffsetEnum.CONFIDENTIALITY_OFFSET_30)
        assert offset_30.getValue() == MacSecConfidentialityOffsetEnum.CONFIDENTIALITY_OFFSET_30

        offset_50 = MacSecConfidentialityOffsetEnum().setValue(MacSecConfidentialityOffsetEnum.CONFIDENTIALITY_OFFSET_50)
        assert offset_50.getValue() == MacSecConfidentialityOffsetEnum.CONFIDENTIALITY_OFFSET_50

    def test_class_docstring_note(self):
        note = "This enum defines the MACsec capability options. Tags: atp.Status=candidate"
        assert inspect.cleandoc(MacSecConfidentialityOffsetEnum.__doc__) == note


class TestMacSecCapabilityEnum:
    """Test cases for MacSecCapabilityEnum (CP_TPS_SystemTemplate Table 3.126, p.177, R23-11)."""

    def test_member_presence_and_values(self):
        # spec literal names per Table 3.126 (intergrityAndConfidentiality idx1, intergrityWithoutConfidentiality idx0); note the spec spells both "intergrity"
        assert MacSecCapabilityEnum.INTERGRITY_AND_CONFIDENTIALITY == "INTERGRITY-AND-CONFIDENTIALITY"
        assert MacSecCapabilityEnum.INTERGRITY_WITHOUT_CONFIDENTIALITY == "INTERGRITY-WITHOUT-CONFIDENTIALITY"
        assert list(MacSecCapabilityEnum().getEnumValues()) == [
            "INTERGRITY-AND-CONFIDENTIALITY",
            "INTERGRITY-WITHOUT-CONFIDENTIALITY",
        ]

    def test_instantiability_round_trip(self):
        both = MacSecCapabilityEnum().setValue(MacSecCapabilityEnum.INTERGRITY_AND_CONFIDENTIALITY)
        assert both.getValue() == MacSecCapabilityEnum.INTERGRITY_AND_CONFIDENTIALITY

        without = MacSecCapabilityEnum().setValue(MacSecCapabilityEnum.INTERGRITY_WITHOUT_CONFIDENTIALITY)
        assert without.getValue() == MacSecCapabilityEnum.INTERGRITY_WITHOUT_CONFIDENTIALITY

    def test_class_docstring_note(self):
        note = "This enum defines the MACsec capability options. Tags: atp.Status=candidate"
        assert inspect.cleandoc(MacSecCapabilityEnum.__doc__) == note


class TestMacSecRoleEnum:
    """Test cases for MacSecRoleEnum (CP_TPS_SystemTemplate Table 3.127, p.177, R23-11)."""

    def test_member_presence_and_values(self):
        # spec literal names per Table 3.127 (keyServer idx1, peer idx0)
        assert MacSecRoleEnum.KEY_SERVER == "KEY-SERVER"
        assert MacSecRoleEnum.PEER == "PEER"
        assert list(MacSecRoleEnum().getEnumValues()) == [
            "KEY-SERVER",
            "PEER",
        ]

    def test_instantiability_round_trip(self):
        key_server = MacSecRoleEnum().setValue(MacSecRoleEnum.KEY_SERVER)
        assert key_server.getValue() == MacSecRoleEnum.KEY_SERVER

        peer = MacSecRoleEnum().setValue(MacSecRoleEnum.PEER)
        assert peer.getValue() == MacSecRoleEnum.PEER

    def test_class_docstring_note(self):
        note = "This enum defines the MACsec Role options. Tags: atp.Status=candidate"
        assert inspect.cleandoc(MacSecRoleEnum.__doc__) == note


class Test_MacSecLocalKayProps:
    def test_initialization_defaults(self):
        props = MacSecLocalKayProps()
        assert props.getDestinationMacAddress() is None
        assert props.getGlobalKayPropsRef() is None
        assert props.getKeyServerPriority() is None
        assert props.getMkaParticipantRefs() == []
        assert props.getRole() is None
        assert props.getSourceMacAddress() is None

    def test_get_set_destination_mac_address(self):
        props = MacSecLocalKayProps()
        result = props.setDestinationMacAddress(_mac("00-11-22-33-44-55"))

        assert result is props
        assert props.getDestinationMacAddress().getValue() == "00-11-22-33-44-55"

        props.setDestinationMacAddress(_mac("66-77-88-99-AA-BB"))
        assert props.getDestinationMacAddress().getValue() == "66-77-88-99-AA-BB"

    def test_get_set_global_kay_props_ref(self):
        props = MacSecLocalKayProps()
        result = props.setGlobalKayPropsRef(_ref("/Sec/MacSecGlobalKay"))

        assert result is props
        assert props.getGlobalKayPropsRef().getValue() == "/Sec/MacSecGlobalKay"

        props.setGlobalKayPropsRef(_ref("/Sec/Other"))
        assert props.getGlobalKayPropsRef().getValue() == "/Sec/Other"

    def test_get_set_key_server_priority(self):
        props = MacSecLocalKayProps()
        result = props.setKeyServerPriority(_pos_int("16"))

        assert result is props
        assert props.getKeyServerPriority().getValue() == 16

        props.setKeyServerPriority(_pos_int("32"))
        assert props.getKeyServerPriority().getValue() == 32

    def test_add_mka_participant_refs(self):
        props = MacSecLocalKayProps()
        first = _ref("/Sec/MkaParticipant1")

        result = props.addMkaParticipantRef(first)

        assert result is props
        assert props.getMkaParticipantRefs() == [first]

        second = _ref("/Sec/MkaParticipant2")
        props.addMkaParticipantRef(second)
        assert props.getMkaParticipantRefs() == [first, second]

    def test_get_set_role(self):
        props = MacSecLocalKayProps()
        role = MacSecRoleEnum()
        role.setValue(MacSecRoleEnum.KEY_SERVER)

        result = props.setRole(role)

        assert result is props
        assert props.getRole().getValue() == MacSecRoleEnum.KEY_SERVER

        peer = MacSecRoleEnum()
        peer.setValue(MacSecRoleEnum.PEER)
        props.setRole(peer)
        assert props.getRole().getValue() == MacSecRoleEnum.PEER

    def test_get_set_source_mac_address(self):
        props = MacSecLocalKayProps()
        result = props.setSourceMacAddress(_mac("AA-BB-CC-DD-EE-FF"))

        assert result is props
        assert props.getSourceMacAddress().getValue() == "AA-BB-CC-DD-EE-FF"

        props.setSourceMacAddress(_mac("11-22-33-44-55-66"))
        assert props.getSourceMacAddress().getValue() == "11-22-33-44-55-66"

    def test_none_is_noop(self):
        props = MacSecLocalKayProps()
        destination = _mac("00-11-22-33-44-55")
        global_ref = _ref("/Sec/MacSecGlobalKay")
        priority = _pos_int("16")
        mka_ref = _ref("/Sec/MkaParticipant1")
        role = MacSecRoleEnum()
        role.setValue(MacSecRoleEnum.KEY_SERVER)
        source = _mac("AA-BB-CC-DD-EE-FF")
        props.setDestinationMacAddress(destination)
        props.setGlobalKayPropsRef(global_ref)
        props.setKeyServerPriority(priority)
        props.addMkaParticipantRef(mka_ref)
        props.setRole(role)
        props.setSourceMacAddress(source)

        props.setDestinationMacAddress(None)
        props.setGlobalKayPropsRef(None)
        props.setKeyServerPriority(None)
        props.addMkaParticipantRef(None)
        props.setRole(None)
        props.setSourceMacAddress(None)

        assert props.getDestinationMacAddress() is destination
        assert props.getGlobalKayPropsRef() is global_ref
        assert props.getKeyServerPriority() is priority
        assert props.getMkaParticipantRefs() == [mka_ref]
        assert props.getRole() is role
        assert props.getSourceMacAddress() is source

    def test_none_noop_on_fresh_instance(self):
        props = MacSecLocalKayProps()
        props.setDestinationMacAddress(None)
        props.setGlobalKayPropsRef(None)
        props.setKeyServerPriority(None)
        props.addMkaParticipantRef(None)
        props.setRole(None)
        props.setSourceMacAddress(None)

        assert props.getDestinationMacAddress() is None
        assert props.getGlobalKayPropsRef() is None
        assert props.getKeyServerPriority() is None
        assert props.getMkaParticipantRefs() == []
        assert props.getRole() is None
        assert props.getSourceMacAddress() is None


class Test_MacSecProps:
    def test_initialization_defaults(self):
        props = MacSecProps()
        assert props.getAutoStart() is None
        assert props.getMacSecKayConfig() is None
        assert props.getOnFailPermissiveMode() is None
        assert props.getOnFailPermissiveModeTimeout() is None
        assert props.getSakRekeyTimeSpan() is None

    def test_get_set_auto_start(self):
        props = MacSecProps()
        result = props.setAutoStart(_bool("true"))

        assert result is props
        assert props.getAutoStart().getValue() is True

        props.setAutoStart(_bool("false"))
        assert props.getAutoStart().getValue() is False

    def test_get_set_mac_sec_kay_config(self):
        props = MacSecProps()
        kay = MacSecLocalKayProps()
        kay.setKeyServerPriority(_pos_int("16"))

        result = props.setMacSecKayConfig(kay)

        assert result is props
        assert isinstance(props.getMacSecKayConfig(), MacSecLocalKayProps)
        assert props.getMacSecKayConfig().getKeyServerPriority().getValue() == 16

    def test_get_set_on_fail_permissive_mode(self):
        props = MacSecProps()
        fail_mode = MacSecFailPermissiveModeEnum()
        fail_mode.setValue(MacSecFailPermissiveModeEnum.TIMEOUT)

        result = props.setOnFailPermissiveMode(fail_mode)

        assert result is props
        assert props.getOnFailPermissiveMode().getValue() == MacSecFailPermissiveModeEnum.TIMEOUT

        never = MacSecFailPermissiveModeEnum()
        never.setValue(MacSecFailPermissiveModeEnum.NEVER)
        props.setOnFailPermissiveMode(never)
        assert props.getOnFailPermissiveMode().getValue() == MacSecFailPermissiveModeEnum.NEVER

    def test_get_set_on_fail_permissive_mode_timeout(self):
        props = MacSecProps()
        result = props.setOnFailPermissiveModeTimeout(_time("30.0"))

        assert result is props
        assert props.getOnFailPermissiveModeTimeout().getValue() == 30.0

    def test_get_set_sak_rekey_time_span(self):
        props = MacSecProps()
        result = props.setSakRekeyTimeSpan(_time("3600.0"))

        assert result is props
        assert props.getSakRekeyTimeSpan().getValue() == 3600.0

    def test_none_is_noop(self):
        props = MacSecProps()
        auto_start = _bool("true")
        kay = MacSecLocalKayProps()
        fail_mode = MacSecFailPermissiveModeEnum()
        fail_mode.setValue(MacSecFailPermissiveModeEnum.NEVER)
        timeout = _time("30.0")
        rekey = _time("3600.0")
        props.setAutoStart(auto_start)
        props.setMacSecKayConfig(kay)
        props.setOnFailPermissiveMode(fail_mode)
        props.setOnFailPermissiveModeTimeout(timeout)
        props.setSakRekeyTimeSpan(rekey)

        props.setAutoStart(None)
        props.setMacSecKayConfig(None)
        props.setOnFailPermissiveMode(None)
        props.setOnFailPermissiveModeTimeout(None)
        props.setSakRekeyTimeSpan(None)

        assert props.getAutoStart() is auto_start
        assert props.getMacSecKayConfig() is kay
        assert props.getOnFailPermissiveMode() is fail_mode
        assert props.getOnFailPermissiveModeTimeout() is timeout
        assert props.getSakRekeyTimeSpan() is rekey

    def test_none_noop_on_fresh_instance(self):
        props = MacSecProps()
        props.setAutoStart(None)
        props.setMacSecKayConfig(None)
        props.setOnFailPermissiveMode(None)
        props.setOnFailPermissiveModeTimeout(None)
        props.setSakRekeyTimeSpan(None)

        assert props.getAutoStart() is None
        assert props.getMacSecKayConfig() is None
        assert props.getOnFailPermissiveMode() is None
        assert props.getOnFailPermissiveModeTimeout() is None
        assert props.getSakRekeyTimeSpan() is None


class Test_MacSecGlobalKayProps:
    def test_initialization_defaults(self):
        parent = MockParent()
        props = MacSecGlobalKayProps(parent, "test_global_kay")

        assert isinstance(props, ARElement)
        assert props.getBypassEtherTypes() == []
        assert props.getBypassVlans() == []

    def test_add_bypass_ether_types(self):
        parent = MockParent()
        props = MacSecGlobalKayProps(parent, "test_global_kay")
        first = _pos_int("88")

        result = props.addBypassEtherType(first)

        assert result is props
        assert props.getBypassEtherTypes() == [first]

        second = _pos_int("90")
        props.addBypassEtherType(second)
        assert [v.getValue() for v in props.getBypassEtherTypes()] == [88, 90]

    def test_add_bypass_vlans(self):
        parent = MockParent()
        props = MacSecGlobalKayProps(parent, "test_global_kay")
        first = _pos_int("100")

        result = props.addBypassVlan(first)

        assert result is props
        assert props.getBypassVlans() == [first]

        second = _pos_int("200")
        props.addBypassVlan(second)
        assert [v.getValue() for v in props.getBypassVlans()] == [100, 200]

    def test_ar_package_create_factory(self):
        document = AUTOSAR.getInstance()
        document.new()
        document.setARRelease("R23-11")

        pkg = document.createARPackage("Sec")
        props = pkg.createMacSecGlobalKayProps("GKP")

        assert isinstance(props, MacSecGlobalKayProps)
        assert props.getShortName() == "GKP"

        again = pkg.createMacSecGlobalKayProps("GKP")
        assert again is props

    def test_none_is_noop(self):
        parent = MockParent()
        props = MacSecGlobalKayProps(parent, "test_global_kay")
        ether_type = _pos_int("88")
        vlan = _pos_int("100")
        props.addBypassEtherType(ether_type)
        props.addBypassVlan(vlan)

        props.addBypassEtherType(None)
        props.addBypassVlan(None)

        assert props.getBypassEtherTypes() == [ether_type]
        assert props.getBypassVlans() == [vlan]

    def test_none_noop_on_fresh_instance(self):
        parent = MockParent()
        props = MacSecGlobalKayProps(parent, "test_global_kay")

        props.addBypassEtherType(None)
        props.addBypassVlan(None)

        assert props.getBypassEtherTypes() == []
        assert props.getBypassVlans() == []


class Test_MacSecParticipantSet:
    def test_initialization_defaults(self):
        parent = MockParent()
        participant_set = MacSecParticipantSet(parent, "test_participant_set")

        assert isinstance(participant_set, ARElement)
        assert participant_set.getEthernetClusterRef() is None
        assert participant_set.getMkaParticipants() == []

    def test_get_set_ethernet_cluster_ref(self):
        parent = MockParent()
        participant_set = MacSecParticipantSet(parent, "test_participant_set")

        result = participant_set.setEthernetClusterRef(_ref("/Clusters/EthernetCluster"))

        assert result is participant_set
        assert participant_set.getEthernetClusterRef().getValue() == "/Clusters/EthernetCluster"

        participant_set.setEthernetClusterRef(_ref("/Clusters/Other"))
        assert participant_set.getEthernetClusterRef().getValue() == "/Clusters/Other"

    def test_create_mka_participants(self):
        parent = MockParent()
        participant_set = MacSecParticipantSet(parent, "test_participant_set")

        participant = participant_set.createMacSecKayParticipant("MKA1")

        assert isinstance(participant, MacSecKayParticipant)
        assert participant_set.getMkaParticipants() == [participant]

        again = participant_set.createMacSecKayParticipant("MKA1")
        assert again is participant
        assert len(participant_set.getMkaParticipants()) == 1

        second = participant_set.createMacSecKayParticipant("MKA2")
        assert participant_set.getMkaParticipants() == [participant, second]

    def test_ar_package_create_factory(self):
        document = AUTOSAR.getInstance()
        document.new()
        document.setARRelease("R23-11")

        pkg = document.createARPackage("Sec")
        participant_set = pkg.createMacSecParticipantSet("MPS")

        assert isinstance(participant_set, MacSecParticipantSet)
        assert participant_set.getShortName() == "MPS"

        again = pkg.createMacSecParticipantSet("MPS")
        assert again is participant_set

    def test_none_is_noop(self):
        parent = MockParent()
        participant_set = MacSecParticipantSet(parent, "test_participant_set")
        cluster_ref = _ref("/Clusters/EthernetCluster")
        participant_set.setEthernetClusterRef(cluster_ref)
        participant = participant_set.createMacSecKayParticipant("MKA1")

        participant_set.setEthernetClusterRef(None)

        assert participant_set.getEthernetClusterRef() is cluster_ref
        assert participant_set.getMkaParticipants() == [participant]

    def test_none_noop_on_fresh_instance(self):
        parent = MockParent()
        participant_set = MacSecParticipantSet(parent, "test_participant_set")

        participant_set.setEthernetClusterRef(None)

        assert participant_set.getEthernetClusterRef() is None
        assert participant_set.getMkaParticipants() == []


class Test_MacSecCipherSuiteConfig:
    def test_initialization_defaults(self):
        config = MacSecCipherSuiteConfig()
        assert isinstance(config, ARObject)
        assert config.getCipherSuite() is None
        assert config.getCipherSuitePriority() is None

    def test_get_set_cipher_suite(self):
        config = MacSecCipherSuiteConfig()
        cipher_suite = _string("GCM-AES-128")
        result = config.setCipherSuite(cipher_suite)

        assert result is config
        assert config.getCipherSuite() is cipher_suite

        xpn = _string("GCM-AES-XPN-256")
        config.setCipherSuite(xpn)
        assert config.getCipherSuite() is xpn

    def test_get_set_cipher_suite_priority(self):
        config = MacSecCipherSuiteConfig()
        priority = _pos_int("1")
        result = config.setCipherSuitePriority(priority)

        assert result is config
        assert config.getCipherSuitePriority() is priority

        lowest = _pos_int("4")
        config.setCipherSuitePriority(lowest)
        assert config.getCipherSuitePriority() is lowest

    def test_none_is_noop(self):
        config = MacSecCipherSuiteConfig()
        cipher_suite = _string("GCM-AES-128")
        priority = _pos_int("1")
        config.setCipherSuite(cipher_suite)
        config.setCipherSuitePriority(priority)

        config.setCipherSuite(None)
        config.setCipherSuitePriority(None)

        assert config.getCipherSuite() is cipher_suite
        assert config.getCipherSuitePriority() is priority

    def test_none_noop_on_fresh_instance(self):
        config = MacSecCipherSuiteConfig()
        assert config.setCipherSuite(None) is config
        assert config.setCipherSuitePriority(None) is config
        assert config.getCipherSuite() is None
        assert config.getCipherSuitePriority() is None


class Test_MacSecCryptoAlgoConfig:
    def test_initialization_defaults(self):
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
        capability.setValue(MacSecCapabilityEnum.INTERGRITY_AND_CONFIDENTIALITY)
        assert config.setCapability(capability) is config
        assert config.getCapability() is capability

    def test_get_set_confidentiality_offset(self):
        config = MacSecCryptoAlgoConfig()
        offset = MacSecConfidentialityOffsetEnum()
        offset.setValue(MacSecConfidentialityOffsetEnum.CONFIDENTIALITY_OFFSET_30)
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

    def test_add_and_get_cipher_suite_configs(self):
        config = MacSecCryptoAlgoConfig()
        c1 = MacSecCipherSuiteConfig()
        c1.setCipherSuite(_string("GCM-AES-128"))
        c2 = MacSecCipherSuiteConfig()
        c2.setCipherSuite(_string("GCM-AES-256"))

        assert config.addCipherSuiteConfig(c1) is config
        assert config.addCipherSuiteConfig(c2) is config
        assert config.getCipherSuiteConfigs() == [c1, c2]
        assert config.getCipherSuiteConfigs()[0].getCipherSuite().getValue() == "GCM-AES-128"
        assert config.getCipherSuiteConfigs()[1].getCipherSuite().getValue() == "GCM-AES-256"

    def test_add_cipher_suite_config_none_is_noop(self):
        config = MacSecCryptoAlgoConfig()
        assert config.addCipherSuiteConfig(None) is config
        assert config.getCipherSuiteConfigs() == []

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
    def test_initialization_defaults(self):
        parent = MockParent()
        participant = MacSecKayParticipant(parent, "test_kay_participant")
        assert isinstance(participant, Identifiable)
        assert participant.getCknRef() is None
        assert participant.getCryptoAlgoConfig() is None
        assert participant.getSakRef() is None

    def test_get_set_ckn_ref(self):
        parent = MockParent()
        participant = MacSecKayParticipant(parent, "test_kay_participant")
        ckn = _ref("/Sec/CryptoKeyCkn")

        result = participant.setCknRef(ckn)

        assert result is participant
        assert participant.getCknRef() is ckn
        assert participant.getCknRef().getValue() == "/Sec/CryptoKeyCkn"

        participant.setCknRef(_ref("/Sec/OtherCkn"))
        assert participant.getCknRef().getValue() == "/Sec/OtherCkn"

    def test_get_set_crypto_algo_config(self):
        parent = MockParent()
        participant = MacSecKayParticipant(parent, "test_kay_participant")
        config = MacSecCryptoAlgoConfig()

        result = participant.setCryptoAlgoConfig(config)

        assert result is participant
        assert participant.getCryptoAlgoConfig() is config

        other = MacSecCryptoAlgoConfig()
        participant.setCryptoAlgoConfig(other)
        assert participant.getCryptoAlgoConfig() is other

    def test_get_set_sak_ref(self):
        parent = MockParent()
        participant = MacSecKayParticipant(parent, "test_kay_participant")
        sak = _ref("/Sec/CryptoKeySak")

        result = participant.setSakRef(sak)

        assert result is participant
        assert participant.getSakRef() is sak
        assert participant.getSakRef().getValue() == "/Sec/CryptoKeySak"

        participant.setSakRef(_ref("/Sec/OtherSak"))
        assert participant.getSakRef().getValue() == "/Sec/OtherSak"

    def test_none_is_noop(self):
        parent = MockParent()
        participant = MacSecKayParticipant(parent, "test_kay_participant")
        ckn = _ref("/Sec/CryptoKeyCkn")
        config = MacSecCryptoAlgoConfig()
        sak = _ref("/Sec/CryptoKeySak")
        participant.setCknRef(ckn)
        participant.setCryptoAlgoConfig(config)
        participant.setSakRef(sak)

        participant.setCknRef(None)
        participant.setCryptoAlgoConfig(None)
        participant.setSakRef(None)

        assert participant.getCknRef() is ckn
        assert participant.getCryptoAlgoConfig() is config
        assert participant.getSakRef() is sak

    def test_none_noop_on_fresh_instance(self):
        parent = MockParent()
        participant = MacSecKayParticipant(parent, "test_kay_participant")
        participant.setCknRef(None)
        participant.setCryptoAlgoConfig(None)
        participant.setSakRef(None)

        assert participant.getCknRef() is None
        assert participant.getCryptoAlgoConfig() is None
        assert participant.getSakRef() is None


class Test_TlsCryptoCipherSuiteSpec:
    """Spec contract of TlsCryptoCipherSuite (AUTOSAR_CP_TPS_SystemTemplate, Table 6.212, p.562)."""

    def test_docstring_is_spec_note_verbatim(self):
        note = "This meta-class represents a cipher suite for describing cryptographic operations in the context of establishing a connection of ApplicationEndpoints that is protected by TLS."
        assert TlsCryptoCipherSuite.__doc__.strip() == note

    def test_init_has_no_docstring(self):
        assert TlsCryptoCipherSuite.__init__.__doc__ is None

    def test_heritage(self):
        # Base chain ARObject, Identifiable, MultilanguageReferrable, Referrable — most-derived is Identifiable
        parent = MockParent()
        suite = TlsCryptoCipherSuite(parent, "suite")
        assert isinstance(suite, Identifiable)
        assert not isinstance(suite, ARElement)

    def test_initialization(self):
        # Table 6.212 — all 14 attributes are optional (Mult 0..1 or *, XSD minOccurs=0)
        parent = MockParent()
        suite = TlsCryptoCipherSuite(parent, "suite")
        assert suite.getAuthenticationRef() is None
        assert suite.getCertificateRef() is None
        assert suite.getCipherSuiteId() is None
        assert suite.getCipherSuiteShortLabel() is None
        assert suite.getEllipticCurveRefs() == []
        assert suite.getEncryptionRef() is None
        assert suite.getKeyExchangeRefs() == []
        assert suite.getKeyExchangeAuthenticationRefs() == []
        assert suite.getPriority() is None
        assert suite.getProps() is None
        assert suite.getPskIdentity() is None
        assert suite.getRemoteCertificateRef() is None
        assert suite.getSignatureSchemeRefs() == []
        assert suite.getVersion() is None

    def test_get_set_authentication_ref(self):
        parent = MockParent()
        suite = TlsCryptoCipherSuite(parent, "suite")
        ref = _ref("/Crypto/Primitives/Mac1")
        assert suite.setAuthenticationRef(ref) is suite
        assert suite.getAuthenticationRef() is ref
        suite.setAuthenticationRef(None)
        assert suite.getAuthenticationRef() is ref

    def test_get_set_certificate_ref(self):
        parent = MockParent()
        suite = TlsCryptoCipherSuite(parent, "suite")
        ref = _ref("/Crypto/Certificates/Local1")
        assert suite.setCertificateRef(ref) is suite
        assert suite.getCertificateRef() is ref
        suite.setCertificateRef(None)
        assert suite.getCertificateRef() is ref

    def test_get_set_encryption_ref(self):
        parent = MockParent()
        suite = TlsCryptoCipherSuite(parent, "suite")
        ref = _ref("/Crypto/Primitives/Enc1")
        assert suite.setEncryptionRef(ref) is suite
        assert suite.getEncryptionRef() is ref
        suite.setEncryptionRef(None)
        assert suite.getEncryptionRef() is ref

    def test_get_set_remote_certificate_ref(self):
        parent = MockParent()
        suite = TlsCryptoCipherSuite(parent, "suite")
        ref = _ref("/Crypto/Certificates/Remote1")
        assert suite.setRemoteCertificateRef(ref) is suite
        assert suite.getRemoteCertificateRef() is ref
        suite.setRemoteCertificateRef(None)
        assert suite.getRemoteCertificateRef() is ref

    def test_get_set_cipher_suite_id(self):
        parent = MockParent()
        suite = TlsCryptoCipherSuite(parent, "suite")
        cipher_id = _pos_int("4865")
        assert suite.setCipherSuiteId(cipher_id) is suite
        assert suite.getCipherSuiteId() is cipher_id
        suite.setCipherSuiteId(None)
        assert suite.getCipherSuiteId() is cipher_id

    def test_get_set_cipher_suite_short_label(self):
        parent = MockParent()
        suite = TlsCryptoCipherSuite(parent, "suite")
        label = _string("TLS_AES_128_GCM_SHA256")
        assert suite.setCipherSuiteShortLabel(label) is suite
        assert suite.getCipherSuiteShortLabel() is label
        suite.setCipherSuiteShortLabel(None)
        assert suite.getCipherSuiteShortLabel() is label

    def test_get_set_priority(self):
        parent = MockParent()
        suite = TlsCryptoCipherSuite(parent, "suite")
        priority = _pos_int("10")
        assert suite.setPriority(priority) is suite
        assert suite.getPriority() is priority
        suite.setPriority(None)
        assert suite.getPriority() is priority

    def test_add_elliptic_curve_refs(self):
        parent = MockParent()
        suite = TlsCryptoCipherSuite(parent, "suite")
        assert suite.addEllipticCurveRef(_ref("/Crypto/EllipticCurves/C1")) is suite
        suite.addEllipticCurveRef(_ref("/Crypto/EllipticCurves/C2"))
        suite.addEllipticCurveRef(None)
        assert [r.getValue() for r in suite.getEllipticCurveRefs()] == ["/Crypto/EllipticCurves/C1", "/Crypto/EllipticCurves/C2"]

    def test_add_key_exchange_refs(self):
        parent = MockParent()
        suite = TlsCryptoCipherSuite(parent, "suite")
        assert suite.addKeyExchangeRef(_ref("/Crypto/Primitives/Ke1")) is suite
        suite.addKeyExchangeRef(_ref("/Crypto/Primitives/Ke2"))
        suite.addKeyExchangeRef(None)
        assert [r.getValue() for r in suite.getKeyExchangeRefs()] == ["/Crypto/Primitives/Ke1", "/Crypto/Primitives/Ke2"]

    def test_add_key_exchange_authentication_refs(self):
        parent = MockParent()
        suite = TlsCryptoCipherSuite(parent, "suite")
        assert suite.addKeyExchangeAuthenticationRef(_ref("/Crypto/Primitives/Sig1")) is suite
        suite.addKeyExchangeAuthenticationRef(_ref("/Crypto/Primitives/Sig2"))
        suite.addKeyExchangeAuthenticationRef(None)
        assert [r.getValue() for r in suite.getKeyExchangeAuthenticationRefs()] == ["/Crypto/Primitives/Sig1", "/Crypto/Primitives/Sig2"]

    def test_add_signature_scheme_refs(self):
        parent = MockParent()
        suite = TlsCryptoCipherSuite(parent, "suite")
        assert suite.addSignatureSchemeRef(_ref("/Crypto/SignatureSchemes/S1")) is suite
        suite.addSignatureSchemeRef(_ref("/Crypto/SignatureSchemes/S2"))
        suite.addSignatureSchemeRef(None)
        assert [r.getValue() for r in suite.getSignatureSchemeRefs()] == ["/Crypto/SignatureSchemes/S1", "/Crypto/SignatureSchemes/S2"]

    def test_get_set_props(self):
        parent = MockParent()
        suite = TlsCryptoCipherSuite(parent, "suite")
        props = TlsCryptoCipherSuiteProps(parent, "props")
        assert suite.setProps(props) is suite
        assert suite.getProps() is props
        suite.setProps(None)
        assert suite.getProps() is props

    def test_get_set_psk_identity(self):
        parent = MockParent()
        suite = TlsCryptoCipherSuite(parent, "suite")
        psk = TlsPskIdentity()
        assert suite.setPskIdentity(psk) is suite
        assert suite.getPskIdentity() is psk
        suite.setPskIdentity(None)
        assert suite.getPskIdentity() is psk

    def test_get_set_version(self):
        parent = MockParent()
        suite = TlsCryptoCipherSuite(parent, "suite")
        version = TlsVersionEnum().setValue(TlsVersionEnum.TLS_13)
        assert suite.setVersion(version) is suite
        assert suite.getVersion() is version
        suite.setVersion(None)
        assert suite.getVersion() is version

    def test_consumer_typed_tls_cipher_suites_list(self):
        # extend pass — TlsCryptoServiceMapping.tlsCipherSuites becomes a typed TlsCryptoCipherSuite list
        mapping = TlsCryptoServiceMapping(MockParent(), "mapping")
        suite = TlsCryptoCipherSuite(mapping, "suite")
        assert mapping.addTlsCipherSuite(suite) is mapping
        assert mapping.getTlsCipherSuites() == [suite]


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
