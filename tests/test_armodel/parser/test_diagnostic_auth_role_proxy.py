"""Parser tests for DiagnosticAuthRoleProxy (Table 4.33, p.76).

Fragment+helper pattern: the class nests in DiagnosticAccessPermission's
AUTHENTICATION-ENABLED aggregation, so only the content helper is exercised.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm import DiagnosticAuthRoleProxy

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-AUTH-ROLE-PROXY") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticAuthRoleProxy:
    def test_read_refs_with_dest(self, parser):
        proxy = DiagnosticAuthRoleProxy()
        element = _snip(
            "<AUTHENTICATION-ROLE-REFS>"
            '<AUTHENTICATION-ROLE-REF DEST="DIAGNOSTIC-AUTH-ROLE">/Diag/AuthRoles/Role1</AUTHENTICATION-ROLE-REF>'
            '<AUTHENTICATION-ROLE-REF DEST="DIAGNOSTIC-AUTH-ROLE">/Diag/AuthRoles/Role2</AUTHENTICATION-ROLE-REF>'
            "</AUTHENTICATION-ROLE-REFS>"
        )
        parser.readDiagnosticAuthRoleProxy(element, proxy)
        refs = proxy.getAuthenticationRoleRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/Diag/AuthRoles/Role1"
        assert refs[0].getDest() == "DIAGNOSTIC-AUTH-ROLE"
        assert refs[1].getValue() == "/Diag/AuthRoles/Role2"

    def test_read_empty_omits_refs(self, parser):
        proxy = DiagnosticAuthRoleProxy()
        parser.readDiagnosticAuthRoleProxy(_snip(""), proxy)
        assert proxy.getAuthenticationRoleRefs() == []
