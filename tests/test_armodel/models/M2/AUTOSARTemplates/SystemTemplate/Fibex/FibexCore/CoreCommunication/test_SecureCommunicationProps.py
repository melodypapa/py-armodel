import inspect
import sys
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import SecureCommunicationProps


def _get_type_hints(obj):
    """typing.get_type_hints leaves PEP 563 self-references as ForwardRef on Python 3.8; resolve against the defining module."""
    hints = typing.get_type_hints(obj)
    module_vars = vars(sys.modules[obj.__module__])
    for name, hint in hints.items():
        if isinstance(hint, typing.ForwardRef):
            hints[name] = module_vars.get(hint.__forward_arg__, hint)
    return hints


CLASS_NOTE = (
    "This meta-class contains configuration settings that are specific for an individual SecuredIPdu.\n"
    "\n"
    "[constr_9205] Existence of SecureCommunicationProps.dataId: For each SecureCommunicationProps, "
    "the attribute dataId shall exist at the time when the System Description is complete.\n"
)

AUTH_DATA_FRESHNESS_LENGTH_NOTE = "This attribute defines the length in bits of the authentic PDU data that is passed to the SWC that verifies and generates the Freshness."

AUTH_DATA_FRESHNESS_START_POSITION_NOTE = (
    "This value determines the start position in bits of the Authentic PDU that shall be passed on to the SWC that verifies and generates the Freshness. "
    "The bit counting is done according to TPS_SYST_01068."
)

AUTHENTICATION_BUILD_ATTEMPTS_NOTE = "This attribute specifies the number of authentication build attempts."

AUTHENTICATION_RETRIES_NOTE = (
    "This attribute defines the additional number of authentication attempts that are to be carried out when the generation of the authentication information "
    "failed for a given SecuredIPdu. If zero is set than only one authentication attempt is done."
)

DATA_ID_NOTE = "This attribute defines a numerical identifier for the Secured I-PDU."

FRESHNESS_VALUE_ID_NOTE = "This attribute defines the Id of the Freshness Value. The Freshness Value might be a normal counter or a time value."

MESSAGE_LINK_LENGTH_NOTE = (
    "SecOC links an AuthenticIPdu and CryptographicIPdu together by repeating a specific part (Message Linker) of the AuthenticIPdu in the CryptographicIPdu. "
    "This attribute defines the length in bits of the messageLinker."
)

MESSAGE_LINK_POSITION_NOTE = (
    "SecOC links an AuthenticIPdu and CryptographicIPdu together by repeating a specific part (Message Linker) of the AuthenticIPdu in the CryptographicIPdu. "
    "This attribute defines the startPosition in bits of the messageLinker."
)

SECONDARY_FRESHNESS_VALUE_ID_NOTE = (
    "This attribute defines the Id of the Secondary Freshness Value. The Secondary Freshness Value might be a normal counter or a time value. "
    "Please note that this attribute is for documentation only to allow the configuration of required freshness value manager and no upstream mapping is defined for it."
)

SECURED_AREA_LENGTH_NOTE = "This attribute defines the length in bytes of the area within the payload Pdu which will be secured."

SECURED_AREA_OFFSET_NOTE = "This attribute defines the start position (offset in byte) of the area within the payload Pdu which will be secured."


class TestSecureCommunicationProps:
    """Test cases for SecureCommunicationProps (Table 6.44, p.369)."""

    MEMBERS = [
        "authDataFreshnessLength",
        "authDataFreshnessStartPosition",
        "authenticationBuildAttempts",
        "authenticationRetries",
        "dataId",
        "freshnessValueId",
        "messageLinkLength",
        "messageLinkPosition",
        "secondaryFreshnessValueId",
        "securedAreaLength",
        "securedAreaOffset",
    ]

    def test_inheritance(self):
        assert issubclass(SecureCommunicationProps, ARObject)

    def test_class_docstring_note(self):
        assert inspect.cleandoc(SecureCommunicationProps.__doc__) == inspect.cleandoc(CLASS_NOTE)

    def test_init_docless(self):
        assert SecureCommunicationProps.__init__.__doc__ is None

    def test_initialization_defaults(self):
        props = SecureCommunicationProps()
        assert props.getAuthDataFreshnessLength() is None
        assert props.getAuthDataFreshnessStartPosition() is None
        assert props.getAuthenticationBuildAttempts() is None
        assert props.getAuthenticationRetries() is None
        assert props.getDataId() is None
        assert props.getFreshnessValueId() is None
        assert props.getMessageLinkLength() is None
        assert props.getMessageLinkPosition() is None
        assert props.getSecondaryFreshnessValueId() is None
        assert props.getSecuredAreaLength() is None
        assert props.getSecuredAreaOffset() is None

    def test_member_order(self):
        props = SecureCommunicationProps()
        members = [k for k in vars(props) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_get_set_auth_data_freshness_length(self):
        props = SecureCommunicationProps()
        value = PositiveInteger()
        value.setValue("10")
        assert props == props.setAuthDataFreshnessLength(value)
        assert props.getAuthDataFreshnessLength().getValue() == 10

        assert props == props.setAuthDataFreshnessLength(None)
        assert props.getAuthDataFreshnessLength() == value

        getter_hints = _get_type_hints(SecureCommunicationProps.getAuthDataFreshnessLength)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = _get_type_hints(SecureCommunicationProps.setAuthDataFreshnessLength)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is SecureCommunicationProps

    def test_get_set_auth_data_freshness_start_position(self):
        props = SecureCommunicationProps()
        value = PositiveInteger()
        value.setValue("20")
        assert props == props.setAuthDataFreshnessStartPosition(value)
        assert props.getAuthDataFreshnessStartPosition().getValue() == 20

        assert props == props.setAuthDataFreshnessStartPosition(None)
        assert props.getAuthDataFreshnessStartPosition() == value

        getter_hints = _get_type_hints(SecureCommunicationProps.getAuthDataFreshnessStartPosition)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = _get_type_hints(SecureCommunicationProps.setAuthDataFreshnessStartPosition)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is SecureCommunicationProps

    def test_get_set_authentication_build_attempts(self):
        props = SecureCommunicationProps()
        value = PositiveInteger()
        value.setValue("5")
        assert props == props.setAuthenticationBuildAttempts(value)
        assert props.getAuthenticationBuildAttempts().getValue() == 5

        assert props == props.setAuthenticationBuildAttempts(None)
        assert props.getAuthenticationBuildAttempts() == value

        getter_hints = _get_type_hints(SecureCommunicationProps.getAuthenticationBuildAttempts)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = _get_type_hints(SecureCommunicationProps.setAuthenticationBuildAttempts)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is SecureCommunicationProps

    def test_get_set_authentication_retries(self):
        props = SecureCommunicationProps()
        value = PositiveInteger()
        value.setValue("3")
        assert props == props.setAuthenticationRetries(value)
        assert props.getAuthenticationRetries().getValue() == 3

        assert props == props.setAuthenticationRetries(None)
        assert props.getAuthenticationRetries() == value

        getter_hints = _get_type_hints(SecureCommunicationProps.getAuthenticationRetries)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = _get_type_hints(SecureCommunicationProps.setAuthenticationRetries)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is SecureCommunicationProps

    def test_get_set_data_id(self):
        props = SecureCommunicationProps()
        value = PositiveInteger()
        value.setValue("42")
        assert props == props.setDataId(value)
        assert props.getDataId().getValue() == 42

        assert props == props.setDataId(None)
        assert props.getDataId() == value

        getter_hints = _get_type_hints(SecureCommunicationProps.getDataId)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = _get_type_hints(SecureCommunicationProps.setDataId)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is SecureCommunicationProps

    def test_get_set_freshness_value_id(self):
        props = SecureCommunicationProps()
        value = PositiveInteger()
        value.setValue("100")
        assert props == props.setFreshnessValueId(value)
        assert props.getFreshnessValueId().getValue() == 100

        assert props == props.setFreshnessValueId(None)
        assert props.getFreshnessValueId() == value

        getter_hints = _get_type_hints(SecureCommunicationProps.getFreshnessValueId)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = _get_type_hints(SecureCommunicationProps.setFreshnessValueId)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is SecureCommunicationProps

    def test_get_set_message_link_length(self):
        props = SecureCommunicationProps()
        value = PositiveInteger()
        value.setValue("70")
        assert props == props.setMessageLinkLength(value)
        assert props.getMessageLinkLength().getValue() == 70

        assert props == props.setMessageLinkLength(None)
        assert props.getMessageLinkLength() == value

        getter_hints = _get_type_hints(SecureCommunicationProps.getMessageLinkLength)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = _get_type_hints(SecureCommunicationProps.setMessageLinkLength)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is SecureCommunicationProps

    def test_get_set_message_link_position(self):
        props = SecureCommunicationProps()
        value = PositiveInteger()
        value.setValue("80")
        assert props == props.setMessageLinkPosition(value)
        assert props.getMessageLinkPosition().getValue() == 80

        assert props == props.setMessageLinkPosition(None)
        assert props.getMessageLinkPosition() == value

        getter_hints = _get_type_hints(SecureCommunicationProps.getMessageLinkPosition)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = _get_type_hints(SecureCommunicationProps.setMessageLinkPosition)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is SecureCommunicationProps

    def test_get_set_secondary_freshness_value_id(self):
        props = SecureCommunicationProps()
        value = PositiveInteger()
        value.setValue("200")
        assert props == props.setSecondaryFreshnessValueId(value)
        assert props.getSecondaryFreshnessValueId().getValue() == 200

        assert props == props.setSecondaryFreshnessValueId(None)
        assert props.getSecondaryFreshnessValueId() == value

        getter_hints = _get_type_hints(SecureCommunicationProps.getSecondaryFreshnessValueId)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = _get_type_hints(SecureCommunicationProps.setSecondaryFreshnessValueId)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is SecureCommunicationProps

    def test_get_set_secured_area_length(self):
        props = SecureCommunicationProps()
        value = PositiveInteger()
        value.setValue("90")
        assert props == props.setSecuredAreaLength(value)
        assert props.getSecuredAreaLength().getValue() == 90

        assert props == props.setSecuredAreaLength(None)
        assert props.getSecuredAreaLength() == value

        getter_hints = _get_type_hints(SecureCommunicationProps.getSecuredAreaLength)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = _get_type_hints(SecureCommunicationProps.setSecuredAreaLength)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is SecureCommunicationProps

    def test_get_set_secured_area_offset(self):
        props = SecureCommunicationProps()
        value = PositiveInteger()
        value.setValue("100")
        assert props == props.setSecuredAreaOffset(value)
        assert props.getSecuredAreaOffset().getValue() == 100

        assert props == props.setSecuredAreaOffset(None)
        assert props.getSecuredAreaOffset() == value

        getter_hints = _get_type_hints(SecureCommunicationProps.getSecuredAreaOffset)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = _get_type_hints(SecureCommunicationProps.setSecuredAreaOffset)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is SecureCommunicationProps

    def test_docstrings_are_spec_notes(self):
        """Test that the getter/setter docstrings carry the attribute Notes verbatim (Table 6.44)."""
        assert SecureCommunicationProps.getAuthDataFreshnessLength.__doc__.strip() == AUTH_DATA_FRESHNESS_LENGTH_NOTE
        assert (
            inspect.cleandoc(SecureCommunicationProps.setAuthDataFreshnessLength.__doc__).strip()
            == AUTH_DATA_FRESHNESS_LENGTH_NOTE + "\nA None value is a no-op and does not overwrite an existing authDataFreshnessLength."
        )
        assert SecureCommunicationProps.getAuthDataFreshnessStartPosition.__doc__.strip() == AUTH_DATA_FRESHNESS_START_POSITION_NOTE
        assert (
            inspect.cleandoc(SecureCommunicationProps.setAuthDataFreshnessStartPosition.__doc__).strip()
            == AUTH_DATA_FRESHNESS_START_POSITION_NOTE + "\nA None value is a no-op and does not overwrite an existing authDataFreshnessStartPosition."
        )
        assert SecureCommunicationProps.getAuthenticationBuildAttempts.__doc__.strip() == AUTHENTICATION_BUILD_ATTEMPTS_NOTE
        assert (
            inspect.cleandoc(SecureCommunicationProps.setAuthenticationBuildAttempts.__doc__).strip()
            == AUTHENTICATION_BUILD_ATTEMPTS_NOTE + "\nA None value is a no-op and does not overwrite an existing authenticationBuildAttempts."
        )
        assert SecureCommunicationProps.getAuthenticationRetries.__doc__.strip() == AUTHENTICATION_RETRIES_NOTE
        assert (
            inspect.cleandoc(SecureCommunicationProps.setAuthenticationRetries.__doc__).strip()
            == AUTHENTICATION_RETRIES_NOTE + "\nA None value is a no-op and does not overwrite an existing authenticationRetries."
        )
        assert SecureCommunicationProps.getDataId.__doc__.strip() == DATA_ID_NOTE
        assert inspect.cleandoc(SecureCommunicationProps.setDataId.__doc__).strip() == DATA_ID_NOTE + "\nA None value is a no-op and does not overwrite an existing dataId."
        assert SecureCommunicationProps.getFreshnessValueId.__doc__.strip() == FRESHNESS_VALUE_ID_NOTE
        assert (
            inspect.cleandoc(SecureCommunicationProps.setFreshnessValueId.__doc__).strip() == FRESHNESS_VALUE_ID_NOTE + "\nA None value is a no-op and does not overwrite an existing freshnessValueId."
        )
        assert SecureCommunicationProps.getMessageLinkLength.__doc__.strip() == MESSAGE_LINK_LENGTH_NOTE
        assert (
            inspect.cleandoc(SecureCommunicationProps.setMessageLinkLength.__doc__).strip()
            == MESSAGE_LINK_LENGTH_NOTE + "\nA None value is a no-op and does not overwrite an existing messageLinkLength."
        )
        assert SecureCommunicationProps.getMessageLinkPosition.__doc__.strip() == MESSAGE_LINK_POSITION_NOTE
        assert (
            inspect.cleandoc(SecureCommunicationProps.setMessageLinkPosition.__doc__).strip()
            == MESSAGE_LINK_POSITION_NOTE + "\nA None value is a no-op and does not overwrite an existing messageLinkPosition."
        )
        assert SecureCommunicationProps.getSecondaryFreshnessValueId.__doc__.strip() == SECONDARY_FRESHNESS_VALUE_ID_NOTE
        assert (
            inspect.cleandoc(SecureCommunicationProps.setSecondaryFreshnessValueId.__doc__).strip()
            == SECONDARY_FRESHNESS_VALUE_ID_NOTE + "\nA None value is a no-op and does not overwrite an existing secondaryFreshnessValueId."
        )
        assert SecureCommunicationProps.getSecuredAreaLength.__doc__.strip() == SECURED_AREA_LENGTH_NOTE
        assert (
            inspect.cleandoc(SecureCommunicationProps.setSecuredAreaLength.__doc__).strip()
            == SECURED_AREA_LENGTH_NOTE + "\nA None value is a no-op and does not overwrite an existing securedAreaLength."
        )
        assert SecureCommunicationProps.getSecuredAreaOffset.__doc__.strip() == SECURED_AREA_OFFSET_NOTE
        assert (
            inspect.cleandoc(SecureCommunicationProps.setSecuredAreaOffset.__doc__).strip()
            == SECURED_AREA_OFFSET_NOTE + "\nA None value is a no-op and does not overwrite an existing securedAreaOffset."
        )
