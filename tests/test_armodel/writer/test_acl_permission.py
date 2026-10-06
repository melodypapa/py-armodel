"""
Tests for writing ACL-PERMISSION elements (AclPermission, Table 11.1).

Round-trip counterpart: tests/test_armodel/parser/test_acl_permission.py
"""

import logging
import os
import tempfile
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AclScopeEnum,
    NameToken,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.RolesAndRights import (
    AclPermission,
)
from armodel.writer.arxml_writer import ARXMLWriter


def _make_writer() -> ARXMLWriter:
    writer = ARXMLWriter.__new__(ARXMLWriter)
    writer.logger = logging.getLogger("test.writer")
    return writer


def _ref(dest: str, value: str) -> RefType:
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


class TestWriteAclPermission:
    """
    Test writeAclPermission (AclPermission, Table 11.1).
    """

    def test_write_members_in_xsd_order(self):
        """Test that own members are written in the XSD ACL-PERMISSION group order."""
        writer = _make_writer()
        element = ET.Element("AR-PACKAGE")

        acl_permission = AclPermission(None, "MyAclPermission")
        acl_permission.addAclContext(NameToken().setValue("PRE-COMPILE"))
        acl_permission.addAclObjectRef(_ref("ACL-OBJECT-SET", "/AUTOSAR/MyObjectSet"))
        acl_permission.addAclOperationRef(_ref("ACL-OPERATION", "/AUTOSAR/MyOperation"))
        acl_permission.addAclRoleRef(_ref("ACL-ROLE", "/AUTOSAR/MyRole"))
        acl_permission.setAclScope(AclScopeEnum().setValue(AclScopeEnum.EXPLICIT))

        writer.writeAclPermission(element, acl_permission)

        acl_permission_tag = element.find("ACL-PERMISSION")
        assert acl_permission_tag is not None
        own_tags = [child.tag for child in acl_permission_tag if child.tag in ("ACL-CONTEXTS", "ACL-OBJECT-REFS", "ACL-OPERATION-REFS", "ACL-ROLE-REFS", "ACL-SCOPE")]
        assert own_tags == ["ACL-CONTEXTS", "ACL-OBJECT-REFS", "ACL-OPERATION-REFS", "ACL-ROLE-REFS", "ACL-SCOPE"]
        assert acl_permission_tag.find("ACL-CONTEXTS/ACL-CONTEXT").text == "PRE-COMPILE"
        object_ref_tag = acl_permission_tag.find("ACL-OBJECT-REFS/ACL-OBJECT-REF")
        assert object_ref_tag.attrib["DEST"] == "ACL-OBJECT-SET"
        assert object_ref_tag.text == "/AUTOSAR/MyObjectSet"
        operation_ref_tag = acl_permission_tag.find("ACL-OPERATION-REFS/ACL-OPERATION-REF")
        assert operation_ref_tag.attrib["DEST"] == "ACL-OPERATION"
        assert operation_ref_tag.text == "/AUTOSAR/MyOperation"
        role_ref_tag = acl_permission_tag.find("ACL-ROLE-REFS/ACL-ROLE-REF")
        assert role_ref_tag.attrib["DEST"] == "ACL-ROLE"
        assert role_ref_tag.text == "/AUTOSAR/MyRole"
        assert acl_permission_tag.find("ACL-SCOPE").text == "EXPLICIT"

    def test_write_empty_wrappers(self):
        """Test that a AclPermission with no own members writes no own elements (empty-wrapper case)."""
        writer = _make_writer()
        element = ET.Element("AR-PACKAGE")

        acl_permission = AclPermission(None, "MyAclPermission")
        writer.writeAclPermission(element, acl_permission)

        acl_permission_tag = element.find("ACL-PERMISSION")
        assert acl_permission_tag is not None
        assert acl_permission_tag.find("ACL-CONTEXTS") is None
        assert acl_permission_tag.find("ACL-OBJECT-REFS") is None
        assert acl_permission_tag.find("ACL-OPERATION-REFS") is None
        assert acl_permission_tag.find("ACL-ROLE-REFS") is None
        assert acl_permission_tag.find("ACL-SCOPE") is None

    def test_round_trip(self):
        """Write a AclPermission with every member set, reparse, and assert all fields survive."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        acl_permission = ar_root.createAclPermission("MyAclPermission")

        acl_permission.addAclContext(NameToken().setValue("PRE-COMPILE"))
        acl_permission.addAclObjectRef(_ref("ACL-OBJECT-SET", "/AUTOSAR/MyObjectSet"))
        acl_permission.addAclOperationRef(_ref("ACL-OPERATION", "/AUTOSAR/MyOperation"))
        acl_permission.addAclRoleRef(_ref("ACL-ROLE", "/AUTOSAR/MyRole"))
        acl_permission.setAclScope(AclScopeEnum().setValue(AclScopeEnum.DEPENDANT))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            from armodel.parser.arxml_parser import ARXMLParser

            ARXMLParser().load(file_path, document_2)

            acl_permission_2 = document_2.getARPackages()[0].getAclPermissions()[0]
            assert acl_permission_2.getShortName() == "MyAclPermission"
            assert acl_permission_2.getAclContexts()[0].getValue() == "PRE-COMPILE"
            assert acl_permission_2.getAclObjectRefs()[0].getDest() == "ACL-OBJECT-SET"
            assert acl_permission_2.getAclObjectRefs()[0].getValue() == "/AUTOSAR/MyObjectSet"
            assert acl_permission_2.getAclOperationRefs()[0].getDest() == "ACL-OPERATION"
            assert acl_permission_2.getAclOperationRefs()[0].getValue() == "/AUTOSAR/MyOperation"
            assert acl_permission_2.getAclRoleRefs()[0].getDest() == "ACL-ROLE"
            assert acl_permission_2.getAclRoleRefs()[0].getValue() == "/AUTOSAR/MyRole"
            assert acl_permission_2.getAclScope().getValue() == AclScopeEnum.DEPENDANT
        finally:
            os.remove(file_path)
