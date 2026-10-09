import inspect
import sys
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import PackageableElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    FibexElement,
    SecureCommunicationAuthenticationProps,
    SecureCommunicationFreshnessProps,
    SecureCommunicationPropsSet,
)


def _get_type_hints(obj):
    """typing.get_type_hints leaves PEP 563 self-references as ForwardRef on Python 3.8; resolve against the defining module."""
    hints = typing.get_type_hints(obj)
    module_vars = vars(sys.modules[obj.__module__])
    for name, hint in hints.items():
        if isinstance(hint, typing.ForwardRef):
            hints[name] = module_vars.get(hint.__forward_arg__, hint)
    return hints


CLASS_NOTE = "Collection of properties used to configure SecuredIPdus. Tags: atp.recommendedPackage=SecureCommunicationPropsSet"

AUTHENTICATION_PROPS_NOTE = "Authentication properties used to configure Secured IPdus."

FRESHNESS_PROPS_NOTE = "Freshness properties used to configure SecuredIPdus."


class TestSecureCommunicationPropsSet:
    """Test cases for SecureCommunicationPropsSet (Table 6.45, p.370)."""

    MEMBERS = ["authenticationProps", "freshnessProps"]

    def test_inheritance(self):
        assert issubclass(SecureCommunicationPropsSet, FibexElement)
        assert issubclass(SecureCommunicationPropsSet, Identifiable)
        assert issubclass(SecureCommunicationPropsSet, PackageableElement)

    def test_class_docstring_note(self):
        assert inspect.cleandoc(SecureCommunicationPropsSet.__doc__) == CLASS_NOTE

    def test_init_docless(self):
        assert SecureCommunicationPropsSet.__init__.__doc__ is None

    def test_initialization_defaults(self):
        props_set = SecureCommunicationPropsSet(None, "PropsSet")
        assert props_set.getAuthenticationProps() == []
        assert props_set.getFreshnessProps() == []

    def test_member_order(self):
        props_set = SecureCommunicationPropsSet(None, "PropsSet")
        members = [k for k in vars(props_set) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_create_authentication_props(self):
        props_set = SecureCommunicationPropsSet(None, "PropsSet")

        props = props_set.createSecureCommunicationAuthenticationProps("authProps")
        assert isinstance(props, SecureCommunicationAuthenticationProps)
        assert props.getShortName() == "authProps"
        assert props_set.getAuthenticationProps() == [props]

        props_dup = props_set.createSecureCommunicationAuthenticationProps("authProps")
        assert props_dup is props
        assert len(props_set.getAuthenticationProps()) == 1

        create_hints = _get_type_hints(SecureCommunicationPropsSet.createSecureCommunicationAuthenticationProps)
        assert create_hints.get("short_name") is str
        assert create_hints.get("return") is SecureCommunicationAuthenticationProps

        getter_hints = _get_type_hints(SecureCommunicationPropsSet.getAuthenticationProps)
        assert getter_hints.get("return") == typing.List[SecureCommunicationAuthenticationProps]

    def test_create_freshness_props(self):
        props_set = SecureCommunicationPropsSet(None, "PropsSet")

        props = props_set.createSecureCommunicationFreshnessProps("freshProps")
        assert isinstance(props, SecureCommunicationFreshnessProps)
        assert props.getShortName() == "freshProps"
        assert props_set.getFreshnessProps() == [props]

        props_dup = props_set.createSecureCommunicationFreshnessProps("freshProps")
        assert props_dup is props
        assert len(props_set.getFreshnessProps()) == 1

        create_hints = _get_type_hints(SecureCommunicationPropsSet.createSecureCommunicationFreshnessProps)
        assert create_hints.get("short_name") is str
        assert create_hints.get("return") is SecureCommunicationFreshnessProps

        getter_hints = _get_type_hints(SecureCommunicationPropsSet.getFreshnessProps)
        assert getter_hints.get("return") == typing.List[SecureCommunicationFreshnessProps]

    def test_docstrings_are_spec_notes(self):
        """Test that the accessor docstrings carry the attribute Notes verbatim (Table 6.45)."""
        assert inspect.cleandoc(SecureCommunicationPropsSet.createSecureCommunicationAuthenticationProps.__doc__) == AUTHENTICATION_PROPS_NOTE
        assert inspect.cleandoc(SecureCommunicationPropsSet.getAuthenticationProps.__doc__) == AUTHENTICATION_PROPS_NOTE
        assert inspect.cleandoc(SecureCommunicationPropsSet.createSecureCommunicationFreshnessProps.__doc__) == FRESHNESS_PROPS_NOTE
        assert inspect.cleandoc(SecureCommunicationPropsSet.getFreshnessProps.__doc__) == FRESHNESS_PROPS_NOTE
