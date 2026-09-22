"""Writer round-trip tests for DiagnosticAuthRoleProxy (Table 4.33, p.76).

Child order per XSD complexType DIAGNOSTIC-AUTH-ROLE-PROXY
(AUTOSAR_00052.xsd l.31747): AR-OBJECT (attributes only) then
AUTHENTICATION-ROLE-REFS.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm import DiagnosticAuthRoleProxy
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


def _new_proxy():
    proxy = DiagnosticAuthRoleProxy()
    proxy.addAuthenticationRoleRef(_ref("DIAGNOSTIC-AUTH-ROLE", "/Diag/AuthRoles/Role1"))
    proxy.addAuthenticationRoleRef(_ref("DIAGNOSTIC-AUTH-ROLE", "/Diag/AuthRoles/Role2"))
    return proxy


class TestWriteDiagnosticAuthRoleProxy:
    def test_write_refs_in_xsd_order(self):
        # Content-only helper: the element tag is created by the calling
        # context (AUTHENTICATION-ENABLED in DiagnosticAccessPermission).
        parent = ET.Element("DIAGNOSTIC-AUTH-ROLE-PROXY")
        ARXMLWriter().writeDiagnosticAuthRoleProxy(parent, _new_proxy())
        assert [child.tag for child in parent] == ["AUTHENTICATION-ROLE-REFS"]
        refs = parent.findall("AUTHENTICATION-ROLE-REFS/AUTHENTICATION-ROLE-REF")
        assert len(refs) == 2
        assert refs[0].text == "/Diag/AuthRoles/Role1"
        assert refs[0].attrib["DEST"] == "DIAGNOSTIC-AUTH-ROLE"
        assert refs[1].text == "/Diag/AuthRoles/Role2"

    def test_write_empty_omits_refs(self):
        parent = ET.Element("DIAGNOSTIC-AUTH-ROLE-PROXY")
        ARXMLWriter().writeDiagnosticAuthRoleProxy(parent, DiagnosticAuthRoleProxy())
        assert len(list(parent)) == 0

    def test_round_trip_preserves_all_values(self):
        parent = ET.Element("PARENT")
        proxy_element = ET.SubElement(parent, "DIAGNOSTIC-AUTH-ROLE-PROXY")
        ARXMLWriter().writeDiagnosticAuthRoleProxy(proxy_element, _new_proxy())
        root = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))
        parsed = DiagnosticAuthRoleProxy()
        ARXMLParser().readDiagnosticAuthRoleProxy(root[0], parsed)
        refs = parsed.getAuthenticationRoleRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/Diag/AuthRoles/Role1"
        assert refs[0].getDest() == "DIAGNOSTIC-AUTH-ROLE"
        assert refs[1].getValue() == "/Diag/AuthRoles/Role2"
        assert refs[1].getDest() == "DIAGNOSTIC-AUTH-ROLE"
