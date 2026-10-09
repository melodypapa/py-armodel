import inspect
import sys
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import SecureCommunicationAuthenticationProps


def _get_type_hints(obj):
    """typing.get_type_hints leaves PEP 563 self-references as ForwardRef on Python 3.8; resolve against the defining module."""
    hints = typing.get_type_hints(obj)
    module_vars = vars(sys.modules[obj.__module__])
    for name, hint in hints.items():
        if isinstance(hint, typing.ForwardRef):
            hints[name] = module_vars.get(hint.__forward_arg__, hint)
    return hints


CLASS_NOTE = "Authentication properties used to configure SecuredIPdus."

AUTH_INFO_TX_LENGTH_NOTE = "This attribute defines the length in bits of the authentication code to be included in the payload of the authenticated Pdu."


class TestSecureCommunicationAuthenticationProps:
    """Test cases for SecureCommunicationAuthenticationProps (Table 6.47, p.371)."""

    MEMBERS = [
        "authInfoTxLength",
    ]

    def _create(self, short_name: str = "props") -> SecureCommunicationAuthenticationProps:
        return SecureCommunicationAuthenticationProps(None, short_name)

    def test_inheritance(self):
        assert issubclass(SecureCommunicationAuthenticationProps, ARObject)
        assert issubclass(SecureCommunicationAuthenticationProps, Identifiable)

    def test_class_docstring_note(self):
        assert inspect.cleandoc(SecureCommunicationAuthenticationProps.__doc__) == inspect.cleandoc(CLASS_NOTE)

    def test_init_docless(self):
        assert SecureCommunicationAuthenticationProps.__init__.__doc__ is None

    def test_initialization_defaults(self):
        props = self._create()
        assert props.getAuthInfoTxLength() is None

    def test_member_order(self):
        props = self._create()
        members = [k for k in vars(props) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_get_set_auth_info_tx_length(self):
        props = self._create()
        value = PositiveInteger()
        value.setValue("24")
        assert props == props.setAuthInfoTxLength(value)
        assert props.getAuthInfoTxLength().getValue() == 24

        assert props == props.setAuthInfoTxLength(None)
        assert props.getAuthInfoTxLength() == value

        getter_hints = _get_type_hints(SecureCommunicationAuthenticationProps.getAuthInfoTxLength)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = _get_type_hints(SecureCommunicationAuthenticationProps.setAuthInfoTxLength)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is SecureCommunicationAuthenticationProps

    def test_docstrings_are_spec_notes(self):
        """Test that the getter/setter docstrings carry the attribute Notes verbatim (Table 6.47)."""
        assert SecureCommunicationAuthenticationProps.getAuthInfoTxLength.__doc__.strip() == AUTH_INFO_TX_LENGTH_NOTE
        assert (
            inspect.cleandoc(SecureCommunicationAuthenticationProps.setAuthInfoTxLength.__doc__).strip()
            == AUTH_INFO_TX_LENGTH_NOTE + "\nA None value is a no-op and does not overwrite an existing authInfoTxLength."
        )
