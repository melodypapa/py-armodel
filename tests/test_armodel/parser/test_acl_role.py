"""
Tests for parsing ACL-ROLE elements (AclRole, Table 11.5).

Round-trip counterpart: tests/test_armodel/writer/test_acl_role.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.RolesAndRights import (
    AclRole,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    """Create ARXML parser instance."""
    AUTOSAR.getInstance().new()
    return ARXMLParser()


def _make_acl_role() -> AclRole:
    AUTOSAR.getInstance().new()
    ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
    return ar_root.createAclRole("MyAclRole")


class TestReadAclRole:
    """
    Test readAclRole (AclRole, Table 11.5).
    """

    def test_read_ldap_url(self, parser):
        """Test that LDAP-URL populates ldapUrl."""
        acl_role = _make_acl_role()
        element = ET.fromstring(
            f"""<ACL-ROLE xmlns='{NS}'>
                <SHORT-NAME>MyAclRole</SHORT-NAME>
                <LDAP-URL>ldap://example.com/Role</LDAP-URL>
            </ACL-ROLE>"""
        )

        parser.readAclRole(element, acl_role)

        assert acl_role.getLdapUrl() is not None
        assert acl_role.getLdapUrl().getValue() == "ldap://example.com/Role"

    def test_read_absent_optional_members(self, parser):
        """Test that an absent optional member leaves the field untouched."""
        acl_role = _make_acl_role()
        element = ET.fromstring(
            f"""<ACL-ROLE xmlns='{NS}'>
                <SHORT-NAME>MyAclRole</SHORT-NAME>
            </ACL-ROLE>"""
        )

        parser.readAclRole(element, acl_role)

        assert acl_role.getLdapUrl() is None

    def test_load_via_ar_package(self, parser):
        """Test that the ARPackage ELEMENTS dispatch reads an ACL-ROLE into getAclRoles()."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        content = f"""<?xml version="1.0" encoding="utf-8"?>
<AUTOSAR xmlns="{NS}" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="{NS} AUTOSAR_00052.xsd">
    <AR-PACKAGES>
        <AR-PACKAGE>
            <SHORT-NAME>AUTOSAR</SHORT-NAME>
            <ELEMENTS>
                <ACL-ROLE>
                    <SHORT-NAME>MyAclRole</SHORT-NAME>
                    <LDAP-URL>ldap://example.com/Role</LDAP-URL>
                </ACL-ROLE>
            </ELEMENTS>
        </AR-PACKAGE>
    </AR-PACKAGES>
</AUTOSAR>"""
        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)

            document = AUTOSAR.getInstance()
            document.clear()
            parser.load(file_path, document)

            acl_roles = document.getARPackages()[0].getAclRoles()
            assert len(acl_roles) == 1
            assert acl_roles[0].getShortName() == "MyAclRole"
            assert acl_roles[0].getLdapUrl().getValue() == "ldap://example.com/Role"
        finally:
            os.remove(file_path)
