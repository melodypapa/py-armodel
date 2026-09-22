"""Model tests for DiagnosticExtract Dcm classes.

DiagnosticAuthRoleProxy (Table 4.33, p.76).
"""

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm import DiagnosticAuthRoleProxy
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

AUTH_ROLE_PROXY_NOTE = (
    "This meta-class indicates that an authentication is generally foreseen. The question whether the authentication is done in general or whether it is done "
    "role-specific depends on the existence of references to DiagAuthRole."
)
AUTH_ROLE_NOTE = "This reference identifies the authenticationRole applicable for the enclosing DiagnosticAccessPermission."


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
