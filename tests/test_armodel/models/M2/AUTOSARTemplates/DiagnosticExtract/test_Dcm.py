"""Model tests for DiagnosticExtract Dcm classes.

DiagnosticAuthRoleProxy (Table 4.33, p.76), DiagnosticSession (Table 4.30,
p.74) and DiagnosticJumpToBootLoaderEnum (Table 4.31, p.75).
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import DiagnosticCommonElement
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm import (
    DiagnosticAuthRoleProxy,
    DiagnosticJumpToBootLoaderEnum,
    DiagnosticSecurityLevel,
    DiagnosticSession,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType, TimeValue

AUTH_ROLE_PROXY_NOTE = (
    "This meta-class indicates that an authentication is generally foreseen. The question whether the authentication is done in general or whether it is done "
    "role-specific depends on the existence of references to DiagAuthRole."
)
AUTH_ROLE_NOTE = "This reference identifies the authenticationRole applicable for the enclosing DiagnosticAccessPermission."
SESSION_NOTE = "This meta-class represents the ability to define a diagnostic session. Tags: atp.recommendedPackage=DiagnosticSessions"
JUMP_NOTE = (
    "This attribute represents the ability to define whether this diagnostic session allows to jump to Bootloader (OEM Bootloader or System Supplier Bootloader). "
    "If this diagnostic session doesn't allow to jump to Bootloader the value JumpToBootLoaderEnum.noBoot shall be chosen."
)
ID_NOTE = "This is the numerical identifier used to identify the DiagnosticSession in the scope of diagnostic workflow"
P2_SERVER_MAX_NOTE = (
    "This is the session value for P2ServerMax in seconds (per Session Control). The AUTOSAR configuration standard is to use SI units, so this parameter is " "defined as a float value in seconds."
)
P2_STAR_SERVER_MAX_NOTE = (
    "This is the session value for P2*ServerMax in seconds (per Session Control). The AUTOSAR configuration standard is to use SI units, so this parameter is " "defined as a float value in seconds."
)
JUMP_ENUM_NOTE = "This enumeration contains the options for jumping to a boot loader."


def _ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _norm(doc):
    return " ".join(doc.split())


class Test_DiagnosticAuthRoleProxy:
    """Test cases for DiagnosticAuthRoleProxy class (Table 4.33, p.76)."""

    def test_instantiation(self):
        proxy = DiagnosticAuthRoleProxy()
        assert isinstance(proxy, DiagnosticAuthRoleProxy)

    def test_is_ar_object_subclass(self):
        assert issubclass(DiagnosticAuthRoleProxy, ARObject)
        assert not issubclass(DiagnosticAuthRoleProxy, Identifiable)

    def test_class_docstring_is_spec_note_verbatim(self):
        assert DiagnosticAuthRoleProxy.__doc__ == AUTH_ROLE_PROXY_NOTE

    def test_init_has_no_docstring(self):
        assert DiagnosticAuthRoleProxy.__init__.__doc__ is None

    def test_defaults(self):
        proxy = DiagnosticAuthRoleProxy()
        assert proxy.getAuthenticationRoleRefs() == []

    def test_add_authentication_role_ref_appends_and_returns_self(self):
        proxy = DiagnosticAuthRoleProxy()
        ref = _ref("DIAGNOSTIC-AUTH-ROLE", "/Diag/AuthRoles/Role1")
        assert proxy.addAuthenticationRoleRef(ref) is proxy
        assert proxy.getAuthenticationRoleRefs() == [ref]

    def test_add_authentication_role_ref_none_is_no_op(self):
        proxy = DiagnosticAuthRoleProxy()
        ref = _ref("DIAGNOSTIC-AUTH-ROLE", "/Diag/AuthRoles/Role1")
        proxy.addAuthenticationRoleRef(ref)
        assert proxy.addAuthenticationRoleRef(None) is proxy
        assert proxy.getAuthenticationRoleRefs() == [ref]

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        assert _norm(DiagnosticAuthRoleProxy.getAuthenticationRoleRefs.__doc__) == AUTH_ROLE_NOTE
        assert _norm(DiagnosticAuthRoleProxy.addAuthenticationRoleRef.__doc__) == (AUTH_ROLE_NOTE + " A None value is a no-op and does not extend the authenticationRoleRefs list.")


def _pkg():
    return AUTOSAR.getInstance().createARPackage("DiagPkg")


class Test_DiagnosticSession:
    """Test cases for DiagnosticSession class (Table 4.30, p.74)."""

    def test_instantiation(self):
        session = DiagnosticSession(_pkg(), "MySession")
        assert session.getShortName() == "MySession"

    def test_is_diagnostic_common_element_subclass(self):
        assert issubclass(DiagnosticSession, DiagnosticCommonElement)
        assert issubclass(DiagnosticSession, ARObject)
        assert issubclass(DiagnosticSession, Identifiable)

    def test_class_docstring_is_spec_note_verbatim(self):
        assert DiagnosticSession.__doc__ == SESSION_NOTE

    def test_init_has_no_docstring(self):
        assert DiagnosticSession.__init__.__doc__ is None

    def test_defaults_in_displayed_order(self):
        session = DiagnosticSession(_pkg(), "MySession")
        assert list(session.__dict__.keys())[-4:] == ["id", "jumpToBootLoader", "p2ServerMax", "p2StarServerMax"]
        assert session.getId() is None
        assert session.getJumpToBootLoader() is None
        assert session.getP2ServerMax() is None
        assert session.getP2StarServerMax() is None

    def test_id_round_trip(self):
        session = DiagnosticSession(_pkg(), "MySession")
        value = PositiveInteger().setValue(2)
        assert session.setId(value) is session
        assert session.getId() is value

    def test_jump_to_boot_loader_round_trip(self):
        session = DiagnosticSession(_pkg(), "MySession")
        value = DiagnosticJumpToBootLoaderEnum().setValue(DiagnosticJumpToBootLoaderEnum.OEM_BOOT)
        assert session.setJumpToBootLoader(value) is session
        assert session.getJumpToBootLoader() is value

    def test_p2_server_max_round_trip(self):
        session = DiagnosticSession(_pkg(), "MySession")
        value = TimeValue().setValue(0.05)
        assert session.setP2ServerMax(value) is session
        assert session.getP2ServerMax() is value

    def test_p2_star_server_max_round_trip(self):
        session = DiagnosticSession(_pkg(), "MySession")
        value = TimeValue().setValue(0.5)
        assert session.setP2StarServerMax(value) is session
        assert session.getP2StarServerMax() is value

    def test_setter_none_is_no_op(self):
        session = DiagnosticSession(_pkg(), "MySession")
        session.setId(PositiveInteger().setValue(2))
        session.setJumpToBootLoader(DiagnosticJumpToBootLoaderEnum().setValue(DiagnosticJumpToBootLoaderEnum.NO_BOOT))
        session.setP2ServerMax(TimeValue().setValue(0.05))
        session.setP2StarServerMax(TimeValue().setValue(0.5))
        assert session.setId(None) is session
        assert session.setJumpToBootLoader(None) is session
        assert session.setP2ServerMax(None) is session
        assert session.setP2StarServerMax(None) is session
        assert session.getId().getValue() == 2
        assert session.getJumpToBootLoader().getValue() == "NO-BOOT"
        assert session.getP2ServerMax().getValue() == 0.05
        assert session.getP2StarServerMax().getValue() == 0.5

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        assert _norm(DiagnosticSession.getId.__doc__) == ID_NOTE
        assert _norm(DiagnosticSession.setId.__doc__) == (ID_NOTE + " A None value is a no-op and does not overwrite an existing id.")
        assert _norm(DiagnosticSession.getJumpToBootLoader.__doc__) == JUMP_NOTE
        assert _norm(DiagnosticSession.setJumpToBootLoader.__doc__) == (JUMP_NOTE + " A None value is a no-op and does not overwrite an existing jumpToBootLoader.")
        assert _norm(DiagnosticSession.getP2ServerMax.__doc__) == P2_SERVER_MAX_NOTE
        assert _norm(DiagnosticSession.setP2ServerMax.__doc__) == (P2_SERVER_MAX_NOTE + " A None value is a no-op and does not overwrite an existing p2ServerMax.")
        assert _norm(DiagnosticSession.getP2StarServerMax.__doc__) == P2_STAR_SERVER_MAX_NOTE
        assert _norm(DiagnosticSession.setP2StarServerMax.__doc__) == (P2_STAR_SERVER_MAX_NOTE + " A None value is a no-op and does not overwrite an existing p2StarServerMax.")


class Test_DiagnosticJumpToBootLoaderEnum:
    """Test cases for DiagnosticJumpToBootLoaderEnum (Table 4.31, p.75)."""

    def test_enum_values_are_xsd_wire_values(self):
        values = DiagnosticJumpToBootLoaderEnum().getEnumValues()
        assert values == ("NO-BOOT", "OEM-BOOT", "OEM-BOOT-RESP-APP", "SYSTEM-SUPPLIER-BOOT", "SYSTEM-SUPPLIER-BOOT-RESP-APP")

    def test_literal_members(self):
        assert DiagnosticJumpToBootLoaderEnum.NO_BOOT == "NO-BOOT"
        assert DiagnosticJumpToBootLoaderEnum.OEM_BOOT == "OEM-BOOT"
        assert DiagnosticJumpToBootLoaderEnum.OEM_BOOT_RESP_APP == "OEM-BOOT-RESP-APP"
        assert DiagnosticJumpToBootLoaderEnum.SYSTEM_SUPPLIER_BOOT == "SYSTEM-SUPPLIER-BOOT"
        assert DiagnosticJumpToBootLoaderEnum.SYSTEM_SUPPLIER_BOOT_RESP_APP == "SYSTEM-SUPPLIER-BOOT-RESP-APP"

    def test_instantiable_and_value_round_trip(self):
        enum_instance = DiagnosticJumpToBootLoaderEnum().setValue(DiagnosticJumpToBootLoaderEnum.SYSTEM_SUPPLIER_BOOT)
        assert enum_instance.getValue() == "SYSTEM-SUPPLIER-BOOT"

    def test_class_docstring_is_spec_note_verbatim(self):
        assert DiagnosticJumpToBootLoaderEnum.__doc__ == JUMP_ENUM_NOTE

    def test_literal_declaration_order_follows_xsd_simple_type(self):
        # Literal descriptions + atp.EnumerationLiteralIndex tags are inline comments
        # in the class body (FirewallActionEnum precedent — class attributes cannot
        # carry docstrings). XSD declaration order: NO-BOOT(0), OEM-BOOT(1),
        # OEM-BOOT-RESP-APP(3), SYSTEM-SUPPLIER-BOOT(2), SYSTEM-SUPPLIER-BOOT-RESP-APP(4).
        values = DiagnosticJumpToBootLoaderEnum().getEnumValues()
        assert values.index(DiagnosticJumpToBootLoaderEnum.NO_BOOT) == 0
        assert values.index(DiagnosticJumpToBootLoaderEnum.OEM_BOOT) == 1
        assert values.index(DiagnosticJumpToBootLoaderEnum.OEM_BOOT_RESP_APP) == 2
        assert values.index(DiagnosticJumpToBootLoaderEnum.SYSTEM_SUPPLIER_BOOT) == 3
        assert values.index(DiagnosticJumpToBootLoaderEnum.SYSTEM_SUPPLIER_BOOT_RESP_APP) == 4


SECURITY_LEVEL_NOTE = "This meta-class represents the ability to define a security level considered for diagnostic purposes. Tags: atp.recommendedPackage=DiagnosticSecurityLevels"
ACCESS_DATA_RECORD_SIZE_NOTE = "This represents the size of the AccessDataRecord used in GetSeed. Unit:byte."
KEY_SIZE_NOTE = "This represents the size of the security key. Unit: byte."
NUM_FAILED_SECURITY_ACCESS_NOTE = "This represents the number of failed security accesses after which the delay time is activated."
SECURITY_DELAY_TIME_NOTE = "This represents the delay time after a failed security access. Unit: second."
SEED_SIZE_NOTE = "This represents the size of the security seed. Unit: byte."


class Test_DiagnosticSecurityLevel:
    """Test cases for DiagnosticSecurityLevel class (Table 4.32, p.75)."""

    def test_instantiation(self):
        level = DiagnosticSecurityLevel(_pkg(), "SecLevel1")
        assert level.getShortName() == "SecLevel1"

    def test_is_diagnostic_common_element_subclass(self):
        assert issubclass(DiagnosticSecurityLevel, DiagnosticCommonElement)
        assert issubclass(DiagnosticSecurityLevel, ARObject)
        assert issubclass(DiagnosticSecurityLevel, Identifiable)

    def test_class_docstring_is_spec_note_verbatim(self):
        assert DiagnosticSecurityLevel.__doc__ == SECURITY_LEVEL_NOTE

    def test_init_has_no_docstring(self):
        assert DiagnosticSecurityLevel.__init__.__doc__ is None

    def test_defaults_in_displayed_order(self):
        level = DiagnosticSecurityLevel(_pkg(), "SecLevel1")
        assert list(level.__dict__.keys())[-5:] == ["accessDataRecordSize", "keySize", "numFailedSecurityAccess", "securityDelayTime", "seedSize"]
        assert level.getAccessDataRecordSize() is None
        assert level.getKeySize() is None
        assert level.getNumFailedSecurityAccess() is None
        assert level.getSecurityDelayTime() is None
        assert level.getSeedSize() is None

    def test_access_data_record_size_round_trip(self):
        level = DiagnosticSecurityLevel(_pkg(), "SecLevel1")
        value = PositiveInteger().setValue(32)
        assert level.setAccessDataRecordSize(value) is level
        assert level.getAccessDataRecordSize() is value

    def test_key_size_round_trip(self):
        level = DiagnosticSecurityLevel(_pkg(), "SecLevel1")
        value = PositiveInteger().setValue(4)
        assert level.setKeySize(value) is level
        assert level.getKeySize() is value

    def test_num_failed_security_access_round_trip(self):
        level = DiagnosticSecurityLevel(_pkg(), "SecLevel1")
        value = PositiveInteger().setValue(3)
        assert level.setNumFailedSecurityAccess(value) is level
        assert level.getNumFailedSecurityAccess() is value

    def test_security_delay_time_round_trip(self):
        level = DiagnosticSecurityLevel(_pkg(), "SecLevel1")
        value = TimeValue().setValue(1.0)
        assert level.setSecurityDelayTime(value) is level
        assert level.getSecurityDelayTime() is value

    def test_seed_size_round_trip(self):
        level = DiagnosticSecurityLevel(_pkg(), "SecLevel1")
        value = PositiveInteger().setValue(8)
        assert level.setSeedSize(value) is level
        assert level.getSeedSize() is value

    def test_setter_none_is_no_op(self):
        level = DiagnosticSecurityLevel(_pkg(), "SecLevel1")
        level.setAccessDataRecordSize(PositiveInteger().setValue(32))
        level.setKeySize(PositiveInteger().setValue(4))
        level.setNumFailedSecurityAccess(PositiveInteger().setValue(3))
        level.setSecurityDelayTime(TimeValue().setValue(1.0))
        level.setSeedSize(PositiveInteger().setValue(8))
        assert level.setAccessDataRecordSize(None) is level
        assert level.setKeySize(None) is level
        assert level.setNumFailedSecurityAccess(None) is level
        assert level.setSecurityDelayTime(None) is level
        assert level.setSeedSize(None) is level
        assert level.getAccessDataRecordSize().getValue() == 32
        assert level.getKeySize().getValue() == 4
        assert level.getNumFailedSecurityAccess().getValue() == 3
        assert level.getSecurityDelayTime().getValue() == 1.0
        assert level.getSeedSize().getValue() == 8

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        assert _norm(DiagnosticSecurityLevel.getAccessDataRecordSize.__doc__) == ACCESS_DATA_RECORD_SIZE_NOTE
        assert _norm(DiagnosticSecurityLevel.setAccessDataRecordSize.__doc__) == (ACCESS_DATA_RECORD_SIZE_NOTE + " A None value is a no-op and does not overwrite an existing accessDataRecordSize.")
        assert _norm(DiagnosticSecurityLevel.getKeySize.__doc__) == KEY_SIZE_NOTE
        assert _norm(DiagnosticSecurityLevel.setKeySize.__doc__) == (KEY_SIZE_NOTE + " A None value is a no-op and does not overwrite an existing keySize.")
        assert _norm(DiagnosticSecurityLevel.getNumFailedSecurityAccess.__doc__) == NUM_FAILED_SECURITY_ACCESS_NOTE
        assert _norm(DiagnosticSecurityLevel.setNumFailedSecurityAccess.__doc__) == (
            NUM_FAILED_SECURITY_ACCESS_NOTE + " A None value is a no-op and does not overwrite an existing numFailedSecurityAccess."
        )
        assert _norm(DiagnosticSecurityLevel.getSecurityDelayTime.__doc__) == SECURITY_DELAY_TIME_NOTE
        assert _norm(DiagnosticSecurityLevel.setSecurityDelayTime.__doc__) == (SECURITY_DELAY_TIME_NOTE + " A None value is a no-op and does not overwrite an existing securityDelayTime.")
        assert _norm(DiagnosticSecurityLevel.getSeedSize.__doc__) == SEED_SIZE_NOTE
        assert _norm(DiagnosticSecurityLevel.setSeedSize.__doc__) == (SEED_SIZE_NOTE + " A None value is a no-op and does not overwrite an existing seedSize.")
