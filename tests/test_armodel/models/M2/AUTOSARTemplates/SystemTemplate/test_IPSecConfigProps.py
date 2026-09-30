"""
This module contains tests for the IPSecConfigProps class
in the AUTOSAR SystemTemplate SecureCommunication module.
"""

import inspect
import re
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, String, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import IPSecConfigProps, IPsecDpdActionEnum

CLASS_NOTE = "This element holds all the attributes for configuration of IPsec that are independent of specific IPsec rules. Tags: atp.recommendedPackage=IPSecConfigProps"

CLASS_DOCSTRING = "\n".join(
    [
        CLASS_NOTE,
        "",
        "[TPS_SYST_02270] Definition of general IPsec configuration settings: General configuration properties that are independent of particular IPSecRule s are collected in the IPSecConfigProps element that is referenced from the IPSecConfig in the role ipSecConfigProps .",
    ]
)

FIELD_ORDER = [
    "ahCipherSuiteNames",
    "dpdAction",
    "dpdDelay",
    "espCipherSuiteNames",
    "ikeCipherSuiteName",
    "ikeOverTime",
    "ikeRandTime",
    "ikeReauthTime",
    "ikeRekeyTime",
    "saOverTime",
    "saRandTime",
    "saRekeyTime",
]

METHOD_ORDER = [
    "__init__",
    "addAhCipherSuiteName",
    "getAhCipherSuiteNames",
    "getDpdAction",
    "setDpdAction",
    "getDpdDelay",
    "setDpdDelay",
    "addEspCipherSuiteName",
    "getEspCipherSuiteNames",
    "getIkeCipherSuiteName",
    "setIkeCipherSuiteName",
    "getIkeOverTime",
    "setIkeOverTime",
    "getIkeRandTime",
    "setIkeRandTime",
    "getIkeReauthTime",
    "setIkeReauthTime",
    "getIkeRekeyTime",
    "setIkeRekeyTime",
    "getSaOverTime",
    "setSaOverTime",
    "getSaRandTime",
    "setSaRandTime",
    "getSaRekeyTime",
    "setSaRekeyTime",
]

# (attribute, getter, note) in spec displayed row order (Table 6.223, p.573)
SPEC_NOTES = [
    ("ahCipherSuiteNames", "getAhCipherSuiteNames", "AH (Authentication Header) algorithm to be used for the connection, e.g. HMAC/SHA2-256"),
    ("dpdAction", "getDpdAction", 'This attribute defines what to do if the peer is considered dead. If not configured "restart" shall be assumed.'),
    (
        "dpdDelay",
        "getDpdDelay",
        'This attribute describes the interval to check the liveness of a peer actively using IKEv2 INFORMATIONAL exchanges. Active DPD checking is only enforced if no IKE or ESP/AH packet has been received for the configured DPD delay. In not configured the value "5 minutes" shall be assumed.',
    ),
    ("espCipherSuiteNames", "getEspCipherSuiteNames", "ESP (Encapsulating Security Payload) algorithm that provides encryption and optional authentication for the connection, e.g. AES-128+SHA2-256."),
    ("ikeCipherSuiteName", "getIkeCipherSuiteName", "IKE encryption/authentication algorithms to be used for the connection."),
    ("ikeOverTime", "getIkeOverTime", "This attribute describes the hard deadline when an SA becomes invalid in percentage. Example: ikeOverTime of max(ikeReauthTime, ikeRekeyTime). Default: 10%"),
    ("ikeRandTime", "getIkeRandTime", "This attribute defines in percentage by how long before the expiration of ikeReauthTime and ikeRekeyTime will be rekeyed/reauthenticated. Default: 10%"),
    ("ikeReauthTime", "getIkeReauthTime", "This attribute defines the absolute time after which an IKE SA will be reauthenticated. 0 means reauthentication is disabled."),
    ("ikeRekeyTime", "getIkeRekeyTime", "This attribute defines the absolute time after which an IKE SA will be rekeyed. 0 means rekey is disabled."),
    ("saOverTime", "getSaOverTime", "This attribute describes the hard deadline when an IPsec SA becomes invalid in percentage. Example: saOverTime * saRekeyTime. Default: 110%"),
    ("saRandTime", "getSaRandTime", "This attribute defines by how long before the expiration of saRekeyTime will be rekeyed."),
    ("saRekeyTime", "getSaRekeyTime", "This attribute defines the absolute time after which an IPsec SA will be rekeyed. 0 means rekey is disabled."),
]


def _pos_int(value):
    p = PositiveInteger()
    p.setValue(value)
    return p


def _string(value):
    s = String()
    s.setValue(value)
    return s


def _time_value(value):
    t = TimeValue()
    t.setValue(value)
    return t


def _enum(enum_cls, member):
    e = enum_cls()
    e.setValue(member)
    return e


class TestIPSecConfigProps:
    def test_initialization(self):
        """Test that IPSecConfigProps is an ARElement wired with parent and short name and all fields default"""
        parent = _parent()
        props = IPSecConfigProps(parent, "TestIPSecConfigProps")

        assert isinstance(props, ARElement)
        assert props.getShortName() == "TestIPSecConfigProps"

        for field, getter, _ in SPEC_NOTES:
            assert getattr(props, getter)() == ([] if field.endswith("Names") else None)

    def test_class_docstring_is_spec_note_and_constraints(self):
        """Test that the class docstring carries the spec Note verbatim plus the class constraint paragraphs"""
        assert inspect.cleandoc(IPSecConfigProps.__doc__) == CLASS_DOCSTRING

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert IPSecConfigProps.__init__.__doc__ is None

    def test_member_order_follows_spec_row_order(self):
        """Test that fields and accessor methods follow the displayed table row order"""
        init_src = inspect.getsource(IPSecConfigProps.__init__)
        fields = re.findall(r"self\.(\w+):", init_src)
        assert fields == FIELD_ORDER

        class_src = inspect.getsource(IPSecConfigProps)
        methods = re.findall(r"def (\w+)\(self", class_src)
        assert methods == METHOD_ORDER

    def test_add_ah_cipher_suite_names(self):
        """Test ahCipherSuiteNames default, add chaining, None no-op and typing"""
        props = _new_props()
        assert props.getAhCipherSuiteNames() == []

        value1 = _string("HMAC/SHA2-256")
        assert props.addAhCipherSuiteName(value1) is props
        value2 = _string("HMAC/SHA2-384")
        props.addAhCipherSuiteName(value2)
        assert props.getAhCipherSuiteNames() == [value1, value2]

        props.addAhCipherSuiteName(None)
        assert len(props.getAhCipherSuiteNames()) == 2

        hints = typing.get_type_hints(IPSecConfigProps.getAhCipherSuiteNames)
        assert hints.get("return") == typing.List[String]
        add_hints = typing.get_type_hints(IPSecConfigProps.addAhCipherSuiteName)
        assert add_hints.get("value") == typing.Optional[String]
        assert add_hints.get("return") is IPSecConfigProps

    def test_get_set_dpd_action(self):
        """Test dpdAction default, guarded set chaining, None no-op and typing"""
        props = _new_props()
        assert props.getDpdAction() is None

        dpd_action = _enum(IPsecDpdActionEnum, IPsecDpdActionEnum.RESTART)
        assert props.setDpdAction(dpd_action) is props
        assert props.getDpdAction() is dpd_action

        props.setDpdAction(None)
        assert props.getDpdAction() is dpd_action

        hints = typing.get_type_hints(IPSecConfigProps.getDpdAction)
        assert hints.get("return") == typing.Optional[IPsecDpdActionEnum]
        setter_hints = typing.get_type_hints(IPSecConfigProps.setDpdAction)
        assert setter_hints.get("value") == typing.Optional[IPsecDpdActionEnum]
        assert setter_hints.get("return") is IPSecConfigProps

    def test_get_set_dpd_delay(self):
        """Test dpdDelay default, guarded set chaining, None no-op and typing"""
        props = _new_props()
        assert props.getDpdDelay() is None

        dpd_delay = _time_value(300.0)
        assert props.setDpdDelay(dpd_delay) is props
        assert props.getDpdDelay() is dpd_delay

        props.setDpdDelay(None)
        assert props.getDpdDelay() is dpd_delay

        hints = typing.get_type_hints(IPSecConfigProps.getDpdDelay)
        assert hints.get("return") == typing.Optional[TimeValue]
        setter_hints = typing.get_type_hints(IPSecConfigProps.setDpdDelay)
        assert setter_hints.get("value") == typing.Optional[TimeValue]
        assert setter_hints.get("return") is IPSecConfigProps

    def test_add_esp_cipher_suite_names(self):
        """Test espCipherSuiteNames default, add chaining, None no-op and typing"""
        props = _new_props()
        assert props.getEspCipherSuiteNames() == []

        value1 = _string("AES-128+SHA2-256")
        assert props.addEspCipherSuiteName(value1) is props
        value2 = _string("AES-256+SHA2-384")
        props.addEspCipherSuiteName(value2)
        assert props.getEspCipherSuiteNames() == [value1, value2]

        props.addEspCipherSuiteName(None)
        assert len(props.getEspCipherSuiteNames()) == 2

        hints = typing.get_type_hints(IPSecConfigProps.getEspCipherSuiteNames)
        assert hints.get("return") == typing.List[String]
        add_hints = typing.get_type_hints(IPSecConfigProps.addEspCipherSuiteName)
        assert add_hints.get("value") == typing.Optional[String]
        assert add_hints.get("return") is IPSecConfigProps

    def test_get_set_ike_cipher_suite_name(self):
        """Test ikeCipherSuiteName default, guarded set chaining, None no-op and typing"""
        props = _new_props()
        assert props.getIkeCipherSuiteName() is None

        value = _string("AES-128+SHA2-256")
        assert props.setIkeCipherSuiteName(value) is props
        assert props.getIkeCipherSuiteName() is value

        props.setIkeCipherSuiteName(None)
        assert props.getIkeCipherSuiteName() is value

        hints = typing.get_type_hints(IPSecConfigProps.getIkeCipherSuiteName)
        assert hints.get("return") == typing.Optional[String]
        setter_hints = typing.get_type_hints(IPSecConfigProps.setIkeCipherSuiteName)
        assert setter_hints.get("value") == typing.Optional[String]
        assert setter_hints.get("return") is IPSecConfigProps

    def test_get_set_ike_over_time(self):
        """Test ikeOverTime default, guarded set chaining, None no-op and typing"""
        props = _new_props()
        assert props.getIkeOverTime() is None

        value = _time_value(10.0)
        assert props.setIkeOverTime(value) is props
        assert props.getIkeOverTime() is value

        props.setIkeOverTime(None)
        assert props.getIkeOverTime() is value

        hints = typing.get_type_hints(IPSecConfigProps.getIkeOverTime)
        assert hints.get("return") == typing.Optional[TimeValue]
        setter_hints = typing.get_type_hints(IPSecConfigProps.setIkeOverTime)
        assert setter_hints.get("value") == typing.Optional[TimeValue]
        assert setter_hints.get("return") is IPSecConfigProps

    def test_get_set_ike_rand_time(self):
        """Test ikeRandTime default, guarded set chaining, None no-op and typing"""
        props = _new_props()
        assert props.getIkeRandTime() is None

        value = _pos_int("10")
        assert props.setIkeRandTime(value) is props
        assert props.getIkeRandTime() is value

        props.setIkeRandTime(None)
        assert props.getIkeRandTime() is value

        hints = typing.get_type_hints(IPSecConfigProps.getIkeRandTime)
        assert hints.get("return") == typing.Optional[PositiveInteger]
        setter_hints = typing.get_type_hints(IPSecConfigProps.setIkeRandTime)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is IPSecConfigProps

    def test_get_set_ike_reauth_time(self):
        """Test ikeReauthTime default, guarded set chaining, None no-op and typing"""
        props = _new_props()
        assert props.getIkeReauthTime() is None

        value = _time_value(3600.0)
        assert props.setIkeReauthTime(value) is props
        assert props.getIkeReauthTime() is value

        props.setIkeReauthTime(None)
        assert props.getIkeReauthTime() is value

        hints = typing.get_type_hints(IPSecConfigProps.getIkeReauthTime)
        assert hints.get("return") == typing.Optional[TimeValue]
        setter_hints = typing.get_type_hints(IPSecConfigProps.setIkeReauthTime)
        assert setter_hints.get("value") == typing.Optional[TimeValue]
        assert setter_hints.get("return") is IPSecConfigProps

    def test_get_set_ike_rekey_time(self):
        """Test ikeRekeyTime default, guarded set chaining, None no-op and typing"""
        props = _new_props()
        assert props.getIkeRekeyTime() is None

        value = _time_value(7200.0)
        assert props.setIkeRekeyTime(value) is props
        assert props.getIkeRekeyTime() is value

        props.setIkeRekeyTime(None)
        assert props.getIkeRekeyTime() is value

        hints = typing.get_type_hints(IPSecConfigProps.getIkeRekeyTime)
        assert hints.get("return") == typing.Optional[TimeValue]
        setter_hints = typing.get_type_hints(IPSecConfigProps.setIkeRekeyTime)
        assert setter_hints.get("value") == typing.Optional[TimeValue]
        assert setter_hints.get("return") is IPSecConfigProps

    def test_get_set_sa_over_time(self):
        """Test saOverTime default, guarded set chaining, None no-op and typing"""
        props = _new_props()
        assert props.getSaOverTime() is None

        value = _pos_int("110")
        assert props.setSaOverTime(value) is props
        assert props.getSaOverTime() is value

        props.setSaOverTime(None)
        assert props.getSaOverTime() is value

        hints = typing.get_type_hints(IPSecConfigProps.getSaOverTime)
        assert hints.get("return") == typing.Optional[PositiveInteger]
        setter_hints = typing.get_type_hints(IPSecConfigProps.setSaOverTime)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is IPSecConfigProps

    def test_get_set_sa_rand_time(self):
        """Test saRandTime default, guarded set chaining, None no-op and typing"""
        props = _new_props()
        assert props.getSaRandTime() is None

        value = _time_value(30.0)
        assert props.setSaRandTime(value) is props
        assert props.getSaRandTime() is value

        props.setSaRandTime(None)
        assert props.getSaRandTime() is value

        hints = typing.get_type_hints(IPSecConfigProps.getSaRandTime)
        assert hints.get("return") == typing.Optional[TimeValue]
        setter_hints = typing.get_type_hints(IPSecConfigProps.setSaRandTime)
        assert setter_hints.get("value") == typing.Optional[TimeValue]
        assert setter_hints.get("return") is IPSecConfigProps

    def test_get_set_sa_rekey_time(self):
        """Test saRekeyTime default, guarded set chaining, None no-op and typing"""
        props = _new_props()
        assert props.getSaRekeyTime() is None

        value = _time_value(4800.0)
        assert props.setSaRekeyTime(value) is props
        assert props.getSaRekeyTime() is value

        props.setSaRekeyTime(None)
        assert props.getSaRekeyTime() is value

        hints = typing.get_type_hints(IPSecConfigProps.getSaRekeyTime)
        assert hints.get("return") == typing.Optional[TimeValue]
        setter_hints = typing.get_type_hints(IPSecConfigProps.setSaRekeyTime)
        assert setter_hints.get("value") == typing.Optional[TimeValue]
        assert setter_hints.get("return") is IPSecConfigProps

    def test_docstrings_are_spec_notes_verbatim(self):
        """Test that every getter/setter docstring carries the spec Note verbatim"""
        for field, getter, note in SPEC_NOTES:
            getter_method = getattr(IPSecConfigProps, getter)
            assert getter_method.__doc__.strip() == note, getter

            if field.endswith("Names"):
                mutator = "add" + getter[3:-1]
            else:
                mutator = "set" + getter[3:]
            mutator_method = getattr(IPSecConfigProps, mutator)
            assert mutator_method.__doc__.strip().startswith(note), mutator
            assert "A None value is a no-op" in mutator_method.__doc__, mutator


def _parent():
    from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

    document = AUTOSAR.getInstance()
    document.clear()
    document.setARRelease("R23-11")
    return document


def _new_props() -> IPSecConfigProps:
    return IPSecConfigProps(_parent(), "TestIPSecConfigProps")
