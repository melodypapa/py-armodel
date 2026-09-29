"""
Tests for writing ACL-ROLE elements (AclRole, Table 11.5).

Round-trip counterpart: tests/test_armodel/parser/test_acl_role.py
"""

import logging
import os
import tempfile
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    AclRole,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    UriString,
)
from armodel.writer.arxml_writer import ARXMLWriter


def _make_writer() -> ARXMLWriter:
    writer = ARXMLWriter.__new__(ARXMLWriter)
    writer.logger = logging.getLogger("test.writer")
    return writer


class TestWriteAclRole:
    """
    Test writeAclRole (AclRole, Table 11.5).
    """

    def test_write_ldap_url(self):
        """Test that ldapUrl is written as an LDAP-URL element."""
        writer = _make_writer()
        element = ET.Element("AR-PACKAGE")

        acl_role = AclRole(None, "MyAclRole")
        acl_role.setLdapUrl(UriString().setValue("ldap://example.com/Role"))

        writer.writeAclRole(element, acl_role)

        acl_role_tag = element.find("ACL-ROLE")
        assert acl_role_tag is not None
        ldap_url_tag = acl_role_tag.find("LDAP-URL")
        assert ldap_url_tag is not None
        assert ldap_url_tag.text == "ldap://example.com/Role"

    def test_write_empty(self):
        """Test that a AclRole with no own members writes no own elements (empty case)."""
        writer = _make_writer()
        element = ET.Element("AR-PACKAGE")

        acl_role = AclRole(None, "MyAclRole")
        writer.writeAclRole(element, acl_role)

        acl_role_tag = element.find("ACL-ROLE")
        assert acl_role_tag is not None
        assert acl_role_tag.find("LDAP-URL") is None

    def test_round_trip(self):
        """Write a AclRole with every member set, reparse, and assert all fields survive."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        acl_role = ar_root.createAclRole("MyAclRole")

        acl_role.setLdapUrl(UriString().setValue("ldap://example.com/Role"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            from armodel.parser.arxml_parser import ARXMLParser

            ARXMLParser().load(file_path, document_2)

            acl_role_2 = document_2.getARPackages()[0].getAclRoles()[0]
            assert acl_role_2.getShortName() == "MyAclRole"
            assert acl_role_2.getLdapUrl().getValue() == "ldap://example.com/Role"
        finally:
            os.remove(file_path)
