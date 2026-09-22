"""Parser tests for DiagnosticAccessPermission (Table 4.29, p.73).

XSD group DIAGNOSTIC-ACCESS-PERMISSION (AUTOSAR_00052.xsd l.31480) element
order: AUTHENTICATION-ENABLED, (AUTHENTICATION-ROLE-REFS — atp.Status=removed,
skipped), DIAGNOSTIC-SESSION-REFS, ENVIRONMENTAL-CONDITION-REF,
SECURITY-LEVEL-REFS, (SOVD-LOCK-REF — atp.Status=candidate/AP, skipped).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm import DiagnosticAccessPermission, DiagnosticAuthRoleProxy

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-ACCESS-PERMISSION") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticAccessPermission:
    def test_read_sets_all_fields(self, parser):
        permission = DiagnosticAccessPermission(AUTOSAR.getInstance(), "Ap1")
        element = _snip(
            "<SHORT-NAME>Ap1</SHORT-NAME>"
            "<AUTHENTICATION-ENABLED>"
            "<AUTHENTICATION-ROLE-REFS>"
            '<AUTHENTICATION-ROLE-REF DEST="DIAGNOSTIC-AUTH-ROLE">/Diag/AuthRoles/Role1</AUTHENTICATION-ROLE-REF>'
            "</AUTHENTICATION-ROLE-REFS>"
            "</AUTHENTICATION-ENABLED>"
            "<DIAGNOSTIC-SESSION-REFS>"
            '<DIAGNOSTIC-SESSION-REF DEST="DIAGNOSTIC-SESSION">/Diag/Sessions/S1</DIAGNOSTIC-SESSION-REF>'
            "</DIAGNOSTIC-SESSION-REFS>"
            '<ENVIRONMENTAL-CONDITION-REF DEST="DIAGNOSTIC-ENVIRONMENTAL-CONDITION">/Diag/EnvConds/C1</ENVIRONMENTAL-CONDITION-REF>'
            "<SECURITY-LEVEL-REFS>"
            '<SECURITY-LEVEL-REF DEST="DIAGNOSTIC-SECURITY-LEVEL">/Diag/SecLevels/L1</SECURITY-LEVEL-REF>'
            '<SECURITY-LEVEL-REF DEST="DIAGNOSTIC-SECURITY-LEVEL">/Diag/SecLevels/L2</SECURITY-LEVEL-REF>'
            "</SECURITY-LEVEL-REFS>"
        )
        parser.readDiagnosticAccessPermission(element, permission)
        proxy = permission.getAuthenticationEnabled()
        assert isinstance(proxy, DiagnosticAuthRoleProxy)
        assert proxy.getAuthenticationRoleRefs()[0].getValue() == "/Diag/AuthRoles/Role1"
        sessions = permission.getDiagnosticSessionRefs()
        assert len(sessions) == 1
        assert sessions[0].getValue() == "/Diag/Sessions/S1"
        assert sessions[0].getDest() == "DIAGNOSTIC-SESSION"
        assert permission.getEnvironmentalConditionRef().getValue() == "/Diag/EnvConds/C1"
        levels = permission.getSecurityLevelRefs()
        assert len(levels) == 2
        assert levels[0].getValue() == "/Diag/SecLevels/L1"
        assert levels[1].getValue() == "/Diag/SecLevels/L2"

    def test_read_empty(self, parser):
        permission = DiagnosticAccessPermission(AUTOSAR.getInstance(), "Ap1")
        parser.readDiagnosticAccessPermission(_snip("<SHORT-NAME>Ap1</SHORT-NAME>"), permission)
        assert permission.getAuthenticationEnabled() is None
        assert permission.getDiagnosticSessionRefs() == []
        assert permission.getEnvironmentalConditionRef() is None
        assert permission.getSecurityLevelRefs() == []


def test_arpackage_dispatch_reads_element(parser):
    package = AUTOSAR.getInstance().createARPackage("AccessPerms")
    ar_package = ET.fromstring(
        "<AR-PACKAGE xmlns='%s'>"
        "<SHORT-NAME>AccessPerms</SHORT-NAME>"
        "<ELEMENTS>"
        "<DIAGNOSTIC-ACCESS-PERMISSION>"
        "<SHORT-NAME>Ap1</SHORT-NAME>"
        "<DIAGNOSTIC-SESSION-REFS>"
        '<DIAGNOSTIC-SESSION-REF DEST="DIAGNOSTIC-SESSION">/Diag/Sessions/S1</DIAGNOSTIC-SESSION-REF>'
        "</DIAGNOSTIC-SESSION-REFS>"
        "</DIAGNOSTIC-ACCESS-PERMISSION>"
        "</ELEMENTS>"
        "</AR-PACKAGE>" % NS
    )
    parser.readARPackageElements(ar_package, package)

    permission = package.getElement("Ap1", DiagnosticAccessPermission)
    assert permission is not None
    assert isinstance(permission, DiagnosticAccessPermission)
    assert permission.getDiagnosticSessionRefs()[0].getValue() == "/Diag/Sessions/S1"
