"""Writer round-trip tests for DiagnosticAccessPermission (Table 4.29, p.73).

Child order per XSD complexType DIAGNOSTIC-ACCESS-PERMISSION
(AUTOSAR_00052.xsd l.31587): SHORT-NAME (inherited), AUTHENTICATION-ENABLED,
DIAGNOSTIC-SESSION-REFS, ENVIRONMENTAL-CONDITION-REF, SECURITY-LEVEL-REFS.
(AUTHENTICATION-ROLE-REFS is atp.Status=removed, SOVD-LOCK-REF is
candidate/AP — neither in Table 4.29, both skipped.)
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm import DiagnosticAccessPermission, DiagnosticAuthRoleProxy
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _new_permission():
    pkg = AUTOSAR.getInstance().createARPackage("DiagPkg")
    permission = pkg.createDiagnosticAccessPermission("Ap1")
    proxy = DiagnosticAuthRoleProxy()
    proxy.addAuthenticationRoleRef(_ref("DIAGNOSTIC-AUTH-ROLE", "/Diag/AuthRoles/Role1"))
    permission.setAuthenticationEnabled(proxy)
    permission.addDiagnosticSessionRef(_ref("DIAGNOSTIC-SESSION", "/Diag/Sessions/S1"))
    permission.addDiagnosticSessionRef(_ref("DIAGNOSTIC-SESSION", "/Diag/Sessions/S2"))
    permission.setEnvironmentalConditionRef(_ref("DIAGNOSTIC-ENVIRONMENTAL-CONDITION", "/Diag/EnvConds/C1"))
    permission.addSecurityLevelRef(_ref("DIAGNOSTIC-SECURITY-LEVEL", "/Diag/SecLevels/L1"))
    return permission


class TestWriteDiagnosticAccessPermission:
    def test_write_all_fields_in_xsd_order(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticAccessPermission(parent, _new_permission())
        node = parent.find("DIAGNOSTIC-ACCESS-PERMISSION")
        assert node is not None
        assert [child.tag for child in node] == ["SHORT-NAME", "AUTHENTICATION-ENABLED", "DIAGNOSTIC-SESSION-REFS", "ENVIRONMENTAL-CONDITION-REF", "SECURITY-LEVEL-REFS"]
        enabled = node.find("AUTHENTICATION-ENABLED")
        assert [child.tag for child in enabled] == ["AUTHENTICATION-ROLE-REFS"]
        auth_ref = enabled.find("AUTHENTICATION-ROLE-REFS/AUTHENTICATION-ROLE-REF")
        assert auth_ref.text == "/Diag/AuthRoles/Role1"
        assert auth_ref.attrib["DEST"] == "DIAGNOSTIC-AUTH-ROLE"
        session_refs = node.findall("DIAGNOSTIC-SESSION-REFS/DIAGNOSTIC-SESSION-REF")
        assert len(session_refs) == 2
        assert session_refs[0].text == "/Diag/Sessions/S1"
        env_ref = node.find("ENVIRONMENTAL-CONDITION-REF")
        assert env_ref.text == "/Diag/EnvConds/C1"
        assert env_ref.attrib["DEST"] == "DIAGNOSTIC-ENVIRONMENTAL-CONDITION"
        level_refs = node.findall("SECURITY-LEVEL-REFS/SECURITY-LEVEL-REF")
        assert len(level_refs) == 1
        assert level_refs[0].text == "/Diag/SecLevels/L1"

    def test_write_empty_fields_omits_optional_tags(self):
        pkg = AUTOSAR.getInstance().createARPackage("DiagPkg")
        permission = pkg.createDiagnosticAccessPermission("Ap2")
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticAccessPermission(parent, permission)
        node = parent.find("DIAGNOSTIC-ACCESS-PERMISSION")
        assert node is not None
        assert [child.tag for child in node] == ["SHORT-NAME"]

    def test_round_trip_preserves_all_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticAccessPermission(parent, _new_permission())
        root = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))
        parsed = DiagnosticAccessPermission(AUTOSAR.getInstance(), "Ap3")
        ARXMLParser().readDiagnosticAccessPermission(root[0], parsed)
        proxy = parsed.getAuthenticationEnabled()
        assert isinstance(proxy, DiagnosticAuthRoleProxy)
        assert proxy.getAuthenticationRoleRefs()[0].getValue() == "/Diag/AuthRoles/Role1"
        assert parsed.getDiagnosticSessionRefs()[0].getValue() == "/Diag/Sessions/S1"
        assert parsed.getDiagnosticSessionRefs()[1].getValue() == "/Diag/Sessions/S2"
        assert parsed.getEnvironmentalConditionRef().getValue() == "/Diag/EnvConds/C1"
        assert parsed.getSecurityLevelRefs()[0].getValue() == "/Diag/SecLevels/L1"
