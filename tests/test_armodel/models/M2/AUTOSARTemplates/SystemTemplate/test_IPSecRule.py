"""
This module contains tests for the IPSecRule class
in the AUTOSAR SystemTemplate SecureCommunication module.
"""

import inspect
import re
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import CommunicationDirectionType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import (
    IPsecHeaderTypeEnum,
    IPsecIpProtocolEnum,
    IPsecModeEnum,
    IPsecPolicyEnum,
    IPSecRule,
)

CLASS_NOTE = "This element defines an IPsec rule that describes communication traffic that is monitored, protected and filtered."

CLASS_DOCSTRING = "\n".join(
    [
        CLASS_NOTE,
        "",
        "[TPS_SYST_02266] Definition of IPSecRules: The IPSecConfig meta-class may contain one or several IPSecRules. Each IPSecRule defines the network connection that is monitored by IPsec by defining the local endpoint and the remote endpoint. Each endpoint is defined by the IP Address and the Tcp/Udp Port. The communication direction for which the IPSecRule is valid is defined by the direction attribute.",
        "",
        "[constr_5163] Existence of IPSecRule.headerType: For each IPSecRule, the attribute headerType shall exist at the time when the System Description is complete.",
        "",
        "[constr_5164] Existence of IPSecRule.ipProtocol: For each IPSecRule, the attribute ipProtocol shall exist at the time when the System Description is complete.",
        "",
        "[constr_5165] Existence of IPSecRule.policy: For each IPSecRule, the attribute policy shall exist at the time when the System Description is complete.",
    ]
)

FIELD_ORDER = [
    "direction",
    "headerType",
    "ipProtocol",
    "localCertificateRefs",
    "localId",
    "localPortRangeEnd",
    "localPortRangeStart",
    "mode",
    "policy",
    "preSharedKeyRef",
    "priority",
    "remoteCertificateRefs",
    "remoteId",
    "remoteIpAddressRefs",
    "remotePortRangeEnd",
    "remotePortRangeStart",
]

METHOD_ORDER = [
    "__init__",
    "getDirection",
    "setDirection",
    "getHeaderType",
    "setHeaderType",
    "getIpProtocol",
    "setIpProtocol",
    "addLocalCertificateRef",
    "getLocalCertificateRefs",
    "getLocalId",
    "setLocalId",
    "getLocalPortRangeEnd",
    "setLocalPortRangeEnd",
    "getLocalPortRangeStart",
    "setLocalPortRangeStart",
    "getMode",
    "setMode",
    "getPolicy",
    "setPolicy",
    "getPreSharedKeyRef",
    "setPreSharedKeyRef",
    "getPriority",
    "setPriority",
    "addRemoteCertificateRef",
    "getRemoteCertificateRefs",
    "getRemoteId",
    "setRemoteId",
    "addRemoteIpAddressRef",
    "getRemoteIpAddressRefs",
    "getRemotePortRangeEnd",
    "setRemotePortRangeEnd",
    "getRemotePortRangeStart",
    "setRemotePortRangeStart",
]

# (attribute, getter, note) in spec displayed row order (Table 6.222, p.572)
SPEC_NOTES = [
    ("direction", "getDirection", "This attribute defines the direction in which the traffic is monitored. If this attribute is not set a bidirectional traffic monitoring is assumed."),
    ("headerType", "getHeaderType", "Header type specifying the IPsec security mechanism."),
    ("ipProtocol", "getIpProtocol", "This attribute defines the relevant IP protocol used in the Security Policy Database (SPD) entry."),
    ("localCertificateRefs", "getLocalCertificateRefs", "This reference identifies the applicable certificate used for a local authentication."),
    ("localId", "getLocalId", "This attribute defines how the local participant should be identified for authentication."),
    (
        "localPortRangeEnd",
        "getLocalPortRangeEnd",
        "This attribute restricts the traffic monitoring and defines an end value for the local port range. If this attribute is not set then this rule shall be effective for all local ports. Please note that port ranges are currently not supported in the AUTOSAR AP's operating system backend. If AP systems are involved, each IPsec rule may only contain a single port.",
    ),
    (
        "localPortRangeStart",
        "getLocalPortRangeStart",
        "This attribute restricts the traffic monitoring and defines a start value for the local port range. If this attribute is not set then this rule shall be effective for all local ports. Please note that port ranges are currently not supported in the AUTOSAR AP's operating system backend. If AP systems are involved, each IPsec rule may only contain a single port.",
    ),
    ("mode", "getMode", "This attribute defines the type of the connection."),
    ("policy", "getPolicy", "An IPsec policy defines the rules that determine which type of IP traffic needs to be secured using IPsec and how that traffic is secured."),
    ("preSharedKeyRef", "getPreSharedKeyRef", "This reference identifies the applicable cryptograhic key used for authentication."),
    ("priority", "getPriority", 'This attribute defines the priority of the IPSecRule (SPD entry). The processing of entries is based on priority, starting with the highest priority "0".'),
    ("remoteCertificateRefs", "getRemoteCertificateRefs", "This reference identifies the applicable certificate used for a remote authentication."),
    ("remoteId", "getRemoteId", "This attribute defines how the remote participant should be identified for authentication."),
    (
        "remoteIpAddressRefs",
        "getRemoteIpAddressRefs",
        "Definition of the remote NetworkEndpoint. With this reference the connection between the local Network Endpoint and the remote NetworkEndpoint is described on which the traffic is monitored.",
    ),
    (
        "remotePortRangeEnd",
        "getRemotePortRangeEnd",
        "This attribute restricts the traffic monitoring and defines an end value for the remote port range. If this attribute is not set then this rule shall be effective for all local ports. Please note that port ranges are currently not supported in the AUTOSAR AP's operating system backend. If AP systems are involved, each IPsec rule may only contain a single port.",
    ),
    (
        "remotePortRangeStart",
        "getRemotePortRangeStart",
        "This attribute restricts the traffic monitoring and defines a start value for the remote port range. If this attribute is not set then this rule shall be effective for all local ports. Please note that port ranges are currently not supported in the AUTOSAR AP's operating system backend. If AP systems are involved, each IPsec rule may only contain a single port.",
    ),
]


def _pos_int(value):
    p = PositiveInteger()
    p.setValue(value)
    return p


def _string(value):
    s = String()
    s.setValue(value)
    return s


def _ref(value):
    ref = RefType()
    ref.setValue(value)
    return ref


def _enum(enum_cls, member):
    e = enum_cls()
    e.setValue(member)
    return e


class TestIPSecRule:
    def test_initialization(self):
        """Test that IPSecRule is an Identifiable wired with parent and short name and all fields default"""
        parent = _parent()
        rule = IPSecRule(parent, "TestIPSecRule")

        assert isinstance(rule, Identifiable)
        assert rule.getShortName() == "TestIPSecRule"

        for field, getter, _ in SPEC_NOTES:
            assert getattr(rule, getter)() == ([] if field.endswith("Refs") else None)

    def test_class_docstring_is_spec_note_and_constraints(self):
        """Test that the class docstring carries the spec Note verbatim plus the class constraint paragraphs"""
        assert inspect.cleandoc(IPSecRule.__doc__) == CLASS_DOCSTRING

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert IPSecRule.__init__.__doc__ is None

    def test_member_order_follows_spec_row_order(self):
        """Test that fields and accessor methods follow the displayed table row order"""
        init_src = inspect.getsource(IPSecRule.__init__)
        fields = re.findall(r"self\.(\w+):", init_src)
        assert fields == FIELD_ORDER

        class_src = inspect.getsource(IPSecRule)
        methods = re.findall(r"def (\w+)\(self", class_src)
        assert methods == METHOD_ORDER

    def test_get_set_direction(self):
        """Test direction default, guarded set chaining, None no-op and typing"""
        rule = _new_rule()
        assert rule.getDirection() is None

        direction = _enum(CommunicationDirectionType, CommunicationDirectionType.IN)
        assert rule.setDirection(direction) is rule
        assert rule.getDirection() is direction

        rule.setDirection(None)
        assert rule.getDirection() is direction

        hints = typing.get_type_hints(IPSecRule.getDirection)
        assert hints.get("return") == typing.Optional[CommunicationDirectionType]
        setter_hints = typing.get_type_hints(IPSecRule.setDirection)
        assert setter_hints.get("value") == typing.Optional[CommunicationDirectionType]
        assert setter_hints.get("return") is IPSecRule

    def test_get_set_header_type(self):
        """Test headerType default, guarded set chaining, None no-op and typing"""
        rule = _new_rule()
        assert rule.getHeaderType() is None

        header_type = _enum(IPsecHeaderTypeEnum, IPsecHeaderTypeEnum.AH)
        assert rule.setHeaderType(header_type) is rule
        assert rule.getHeaderType() is header_type

        rule.setHeaderType(None)
        assert rule.getHeaderType() is header_type

        hints = typing.get_type_hints(IPSecRule.getHeaderType)
        assert hints.get("return") == typing.Optional[IPsecHeaderTypeEnum]
        setter_hints = typing.get_type_hints(IPSecRule.setHeaderType)
        assert setter_hints.get("value") == typing.Optional[IPsecHeaderTypeEnum]
        assert setter_hints.get("return") is IPSecRule

    def test_get_set_ip_protocol(self):
        """Test ipProtocol default, guarded set chaining, None no-op and typing"""
        rule = _new_rule()
        assert rule.getIpProtocol() is None

        ip_protocol = _enum(IPsecIpProtocolEnum, IPsecIpProtocolEnum.TCP)
        assert rule.setIpProtocol(ip_protocol) is rule
        assert rule.getIpProtocol() is ip_protocol

        rule.setIpProtocol(None)
        assert rule.getIpProtocol() is ip_protocol

        hints = typing.get_type_hints(IPSecRule.getIpProtocol)
        assert hints.get("return") == typing.Optional[IPsecIpProtocolEnum]
        setter_hints = typing.get_type_hints(IPSecRule.setIpProtocol)
        assert setter_hints.get("value") == typing.Optional[IPsecIpProtocolEnum]
        assert setter_hints.get("return") is IPSecRule

    def test_add_local_certificate_refs(self):
        """Test localCertificateRefs default, add chaining, None no-op and typing"""
        rule = _new_rule()
        assert rule.getLocalCertificateRefs() == []

        ref1 = _ref("/Crypto/Certs/Local1")
        assert rule.addLocalCertificateRef(ref1) is rule
        ref2 = _ref("/Crypto/Certs/Local2")
        rule.addLocalCertificateRef(ref2)
        assert rule.getLocalCertificateRefs() == [ref1, ref2]

        rule.addLocalCertificateRef(None)
        assert len(rule.getLocalCertificateRefs()) == 2

        hints = typing.get_type_hints(IPSecRule.getLocalCertificateRefs)
        assert hints.get("return") == typing.List[RefType]
        add_hints = typing.get_type_hints(IPSecRule.addLocalCertificateRef)
        assert add_hints.get("ref") == typing.Optional[RefType]
        assert add_hints.get("return") is IPSecRule

    def test_get_set_local_id(self):
        """Test localId default, guarded set chaining, None no-op and typing"""
        rule = _new_rule()
        assert rule.getLocalId() is None

        local_id = _string("local-id")
        assert rule.setLocalId(local_id) is rule
        assert rule.getLocalId() is local_id

        rule.setLocalId(None)
        assert rule.getLocalId() is local_id

        hints = typing.get_type_hints(IPSecRule.getLocalId)
        assert hints.get("return") == typing.Optional[String]
        setter_hints = typing.get_type_hints(IPSecRule.setLocalId)
        assert setter_hints.get("value") == typing.Optional[String]
        assert setter_hints.get("return") is IPSecRule

    def test_get_set_local_port_range_end(self):
        """Test localPortRangeEnd default, guarded set chaining, None no-op and typing"""
        rule = _new_rule()
        assert rule.getLocalPortRangeEnd() is None

        value = _pos_int("8080")
        assert rule.setLocalPortRangeEnd(value) is rule
        assert rule.getLocalPortRangeEnd() is value

        rule.setLocalPortRangeEnd(None)
        assert rule.getLocalPortRangeEnd() is value

        hints = typing.get_type_hints(IPSecRule.getLocalPortRangeEnd)
        assert hints.get("return") == typing.Optional[PositiveInteger]
        setter_hints = typing.get_type_hints(IPSecRule.setLocalPortRangeEnd)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is IPSecRule

    def test_get_set_local_port_range_start(self):
        """Test localPortRangeStart default, guarded set chaining, None no-op and typing"""
        rule = _new_rule()
        assert rule.getLocalPortRangeStart() is None

        value = _pos_int("1024")
        assert rule.setLocalPortRangeStart(value) is rule
        assert rule.getLocalPortRangeStart() is value

        rule.setLocalPortRangeStart(None)
        assert rule.getLocalPortRangeStart() is value

        hints = typing.get_type_hints(IPSecRule.getLocalPortRangeStart)
        assert hints.get("return") == typing.Optional[PositiveInteger]
        setter_hints = typing.get_type_hints(IPSecRule.setLocalPortRangeStart)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is IPSecRule

    def test_get_set_mode(self):
        """Test mode default, guarded set chaining, None no-op and typing"""
        rule = _new_rule()
        assert rule.getMode() is None

        mode = _enum(IPsecModeEnum, IPsecModeEnum.TUNNEL)
        assert rule.setMode(mode) is rule
        assert rule.getMode() is mode

        rule.setMode(None)
        assert rule.getMode() is mode

        hints = typing.get_type_hints(IPSecRule.getMode)
        assert hints.get("return") == typing.Optional[IPsecModeEnum]
        setter_hints = typing.get_type_hints(IPSecRule.setMode)
        assert setter_hints.get("value") == typing.Optional[IPsecModeEnum]
        assert setter_hints.get("return") is IPSecRule

    def test_get_set_policy(self):
        """Test policy default, guarded set chaining, None no-op and typing"""
        rule = _new_rule()
        assert rule.getPolicy() is None

        policy = _enum(IPsecPolicyEnum, IPsecPolicyEnum.IPSEC)
        assert rule.setPolicy(policy) is rule
        assert rule.getPolicy() is policy

        rule.setPolicy(None)
        assert rule.getPolicy() is policy

        hints = typing.get_type_hints(IPSecRule.getPolicy)
        assert hints.get("return") == typing.Optional[IPsecPolicyEnum]
        setter_hints = typing.get_type_hints(IPSecRule.setPolicy)
        assert setter_hints.get("value") == typing.Optional[IPsecPolicyEnum]
        assert setter_hints.get("return") is IPSecRule

    def test_get_set_pre_shared_key_ref(self):
        """Test preSharedKeyRef default, guarded set chaining, None no-op and typing"""
        rule = _new_rule()
        assert rule.getPreSharedKeyRef() is None

        ref = _ref("/Crypto/Keys/PreShared")
        assert rule.setPreSharedKeyRef(ref) is rule
        assert rule.getPreSharedKeyRef() is ref

        rule.setPreSharedKeyRef(None)
        assert rule.getPreSharedKeyRef() is ref

        hints = typing.get_type_hints(IPSecRule.getPreSharedKeyRef)
        assert hints.get("return") == typing.Optional[RefType]
        setter_hints = typing.get_type_hints(IPSecRule.setPreSharedKeyRef)
        assert setter_hints.get("value") == typing.Optional[RefType]
        assert setter_hints.get("return") is IPSecRule

    def test_get_set_priority(self):
        """Test priority default, guarded set chaining, None no-op and typing"""
        rule = _new_rule()
        assert rule.getPriority() is None

        priority = _pos_int("0")
        assert rule.setPriority(priority) is rule
        assert rule.getPriority() is priority

        rule.setPriority(None)
        assert rule.getPriority() is priority

        hints = typing.get_type_hints(IPSecRule.getPriority)
        assert hints.get("return") == typing.Optional[PositiveInteger]
        setter_hints = typing.get_type_hints(IPSecRule.setPriority)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is IPSecRule

    def test_add_remote_certificate_refs(self):
        """Test remoteCertificateRefs default, add chaining, None no-op and typing"""
        rule = _new_rule()
        assert rule.getRemoteCertificateRefs() == []

        ref1 = _ref("/Crypto/Certs/Remote1")
        assert rule.addRemoteCertificateRef(ref1) is rule
        ref2 = _ref("/Crypto/Certs/Remote2")
        rule.addRemoteCertificateRef(ref2)
        assert rule.getRemoteCertificateRefs() == [ref1, ref2]

        rule.addRemoteCertificateRef(None)
        assert len(rule.getRemoteCertificateRefs()) == 2

        hints = typing.get_type_hints(IPSecRule.getRemoteCertificateRefs)
        assert hints.get("return") == typing.List[RefType]
        add_hints = typing.get_type_hints(IPSecRule.addRemoteCertificateRef)
        assert add_hints.get("ref") == typing.Optional[RefType]
        assert add_hints.get("return") is IPSecRule

    def test_get_set_remote_id(self):
        """Test remoteId default, guarded set chaining, None no-op and typing"""
        rule = _new_rule()
        assert rule.getRemoteId() is None

        remote_id = _string("remote-id")
        assert rule.setRemoteId(remote_id) is rule
        assert rule.getRemoteId() is remote_id

        rule.setRemoteId(None)
        assert rule.getRemoteId() is remote_id

        hints = typing.get_type_hints(IPSecRule.getRemoteId)
        assert hints.get("return") == typing.Optional[String]
        setter_hints = typing.get_type_hints(IPSecRule.setRemoteId)
        assert setter_hints.get("value") == typing.Optional[String]
        assert setter_hints.get("return") is IPSecRule

    def test_add_remote_ip_address_refs(self):
        """Test remoteIpAddressRefs default, add chaining, None no-op and typing"""
        rule = _new_rule()
        assert rule.getRemoteIpAddressRefs() == []

        ref1 = _ref("/Cluster/NetworkEndpoints/RemoteEp1")
        assert rule.addRemoteIpAddressRef(ref1) is rule
        ref2 = _ref("/Cluster/NetworkEndpoints/RemoteEp2")
        rule.addRemoteIpAddressRef(ref2)
        assert rule.getRemoteIpAddressRefs() == [ref1, ref2]

        rule.addRemoteIpAddressRef(None)
        assert len(rule.getRemoteIpAddressRefs()) == 2

        hints = typing.get_type_hints(IPSecRule.getRemoteIpAddressRefs)
        assert hints.get("return") == typing.List[RefType]
        add_hints = typing.get_type_hints(IPSecRule.addRemoteIpAddressRef)
        assert add_hints.get("ref") == typing.Optional[RefType]
        assert add_hints.get("return") is IPSecRule

    def test_get_set_remote_port_range_end(self):
        """Test remotePortRangeEnd default, guarded set chaining, None no-op and typing"""
        rule = _new_rule()
        assert rule.getRemotePortRangeEnd() is None

        value = _pos_int("9090")
        assert rule.setRemotePortRangeEnd(value) is rule
        assert rule.getRemotePortRangeEnd() is value

        rule.setRemotePortRangeEnd(None)
        assert rule.getRemotePortRangeEnd() is value

        hints = typing.get_type_hints(IPSecRule.getRemotePortRangeEnd)
        assert hints.get("return") == typing.Optional[PositiveInteger]
        setter_hints = typing.get_type_hints(IPSecRule.setRemotePortRangeEnd)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is IPSecRule

    def test_get_set_remote_port_range_start(self):
        """Test remotePortRangeStart default, guarded set chaining, None no-op and typing"""
        rule = _new_rule()
        assert rule.getRemotePortRangeStart() is None

        value = _pos_int("2048")
        assert rule.setRemotePortRangeStart(value) is rule
        assert rule.getRemotePortRangeStart() is value

        rule.setRemotePortRangeStart(None)
        assert rule.getRemotePortRangeStart() is value

        hints = typing.get_type_hints(IPSecRule.getRemotePortRangeStart)
        assert hints.get("return") == typing.Optional[PositiveInteger]
        setter_hints = typing.get_type_hints(IPSecRule.setRemotePortRangeStart)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is IPSecRule

    def test_docstrings_are_spec_notes_verbatim(self):
        """Test that every getter/setter docstring carries the spec Note verbatim"""
        for _, getter, note in SPEC_NOTES:
            getter_method = getattr(IPSecRule, getter)
            assert getter_method.__doc__.strip() == note, getter

            if getter.endswith("Refs"):
                mutator = "add" + getter[3:-4] + "Ref"
            else:
                mutator = "set" + getter[3:]
            mutator_method = getattr(IPSecRule, mutator)
            assert mutator_method.__doc__.strip().startswith(note), mutator
            assert "A None value is a no-op" in mutator_method.__doc__, mutator


def _parent():
    from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

    document = AUTOSAR.getInstance()
    document.clear()
    document.setARRelease("R23-11")
    return document


def _new_rule() -> IPSecRule:
    return IPSecRule(_parent(), "TestIPSecRule")
