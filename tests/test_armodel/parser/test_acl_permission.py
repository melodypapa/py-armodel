"""
Tests for parsing ACL-PERMISSION elements (AclPermission, Table 11.1).

Round-trip counterpart: tests/test_armodel/writer/test_acl_permission.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AclScopeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.RolesAndRights import (
    AclPermission,
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


def _make_acl_permission() -> AclPermission:
    AUTOSAR.getInstance().new()
    ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
    return ar_root.createAclPermission("MyAclPermission")


class TestReadAclPermission:
    """
    Test readAclPermission (AclPermission, Table 11.1).
    """

    def test_read_acl_contexts(self, parser):
        """Test that the ACL-CONTEXTS wrapper populates aclContexts."""
        acl_permission = _make_acl_permission()
        element = ET.fromstring(
            f"""<ACL-PERMISSION xmlns='{NS}'>
                <SHORT-NAME>MyAclPermission</SHORT-NAME>
                <ACL-CONTEXTS>
                    <ACL-CONTEXT>PRE-COMPILE</ACL-CONTEXT>
                    <ACL-CONTEXT>POST-BUILD</ACL-CONTEXT>
                </ACL-CONTEXTS>
            </ACL-PERMISSION>"""
        )

        parser.readAclPermission(element, acl_permission)

        contexts = acl_permission.getAclContexts()
        assert len(contexts) == 2
        assert contexts[0].getValue() == "PRE-COMPILE"
        assert contexts[1].getValue() == "POST-BUILD"

    def test_read_refs(self, parser):
        """Test that ACL-OBJECT-REFS, ACL-OPERATION-REFS and ACL-ROLE-REFS populate the model with DEST and value."""
        acl_permission = _make_acl_permission()
        element = ET.fromstring(
            f"""<ACL-PERMISSION xmlns='{NS}'>
                <SHORT-NAME>MyAclPermission</SHORT-NAME>
                <ACL-OBJECT-REFS>
                    <ACL-OBJECT-REF DEST="ACL-OBJECT-SET">/AUTOSAR/MyObjectSet</ACL-OBJECT-REF>
                </ACL-OBJECT-REFS>
                <ACL-OPERATION-REFS>
                    <ACL-OPERATION-REF DEST="ACL-OPERATION">/AUTOSAR/MyOperation</ACL-OPERATION-REF>
                </ACL-OPERATION-REFS>
                <ACL-ROLE-REFS>
                    <ACL-ROLE-REF DEST="ACL-ROLE">/AUTOSAR/MyRole</ACL-ROLE-REF>
                </ACL-ROLE-REFS>
            </ACL-PERMISSION>"""
        )

        parser.readAclPermission(element, acl_permission)

        object_refs = acl_permission.getAclObjectRefs()
        assert len(object_refs) == 1
        assert object_refs[0].getDest() == "ACL-OBJECT-SET"
        assert object_refs[0].getValue() == "/AUTOSAR/MyObjectSet"

        operation_refs = acl_permission.getAclOperationRefs()
        assert len(operation_refs) == 1
        assert operation_refs[0].getDest() == "ACL-OPERATION"
        assert operation_refs[0].getValue() == "/AUTOSAR/MyOperation"

        role_refs = acl_permission.getAclRoleRefs()
        assert len(role_refs) == 1
        assert role_refs[0].getDest() == "ACL-ROLE"
        assert role_refs[0].getValue() == "/AUTOSAR/MyRole"

    def test_read_acl_scope(self, parser):
        """Test that ACL-SCOPE populates aclScope with the enum literal."""
        acl_permission = _make_acl_permission()
        element = ET.fromstring(
            f"""<ACL-PERMISSION xmlns='{NS}'>
                <SHORT-NAME>MyAclPermission</SHORT-NAME>
                <ACL-SCOPE>DESCENDANT</ACL-SCOPE>
            </ACL-PERMISSION>"""
        )

        parser.readAclPermission(element, acl_permission)

        assert acl_permission.getAclScope() is not None
        assert acl_permission.getAclScope().getValue() == AclScopeEnum.DESCENDANT

    def test_read_absent_optional_members(self, parser):
        """Test that absent optional members leave the fields untouched (empty-wrapper case)."""
        acl_permission = _make_acl_permission()
        element = ET.fromstring(
            f"""<ACL-PERMISSION xmlns='{NS}'>
                <SHORT-NAME>MyAclPermission</SHORT-NAME>
            </ACL-PERMISSION>"""
        )

        parser.readAclPermission(element, acl_permission)

        assert acl_permission.getAclContexts() == []
        assert acl_permission.getAclObjectRefs() == []
        assert acl_permission.getAclOperationRefs() == []
        assert acl_permission.getAclRoleRefs() == []
        assert acl_permission.getAclScope() is None

    def test_load_via_ar_package(self, parser):
        """Test that the ARPackage ELEMENTS dispatch reads an ACL-PERMISSION into getAclPermissions()."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        content = f"""<?xml version="1.0" encoding="utf-8"?>
<AUTOSAR xmlns="{NS}" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="{NS} AUTOSAR_00052.xsd">
    <AR-PACKAGES>
        <AR-PACKAGE>
            <SHORT-NAME>AUTOSAR</SHORT-NAME>
            <ELEMENTS>
                <ACL-PERMISSION>
                    <SHORT-NAME>MyAclPermission</SHORT-NAME>
                    <ACL-CONTEXTS>
                        <ACL-CONTEXT>PRE-COMPILE</ACL-CONTEXT>
                    </ACL-CONTEXTS>
                    <ACL-OBJECT-REFS>
                        <ACL-OBJECT-REF DEST="ACL-OBJECT-SET">/AUTOSAR/MyObjectSet</ACL-OBJECT-REF>
                    </ACL-OBJECT-REFS>
                    <ACL-OPERATION-REFS>
                        <ACL-OPERATION-REF DEST="ACL-OPERATION">/AUTOSAR/MyOperation</ACL-OPERATION-REF>
                    </ACL-OPERATION-REFS>
                    <ACL-ROLE-REFS>
                        <ACL-ROLE-REF DEST="ACL-ROLE">/AUTOSAR/MyRole</ACL-ROLE-REF>
                    </ACL-ROLE-REFS>
                    <ACL-SCOPE>EXPLICIT</ACL-SCOPE>
                </ACL-PERMISSION>
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

            acl_permissions = document.getARPackages()[0].getAclPermissions()
            assert len(acl_permissions) == 1
            assert acl_permissions[0].getShortName() == "MyAclPermission"
            assert acl_permissions[0].getAclContexts()[0].getValue() == "PRE-COMPILE"
            assert acl_permissions[0].getAclObjectRefs()[0].getValue() == "/AUTOSAR/MyObjectSet"
            assert acl_permissions[0].getAclOperationRefs()[0].getValue() == "/AUTOSAR/MyOperation"
            assert acl_permissions[0].getAclRoleRefs()[0].getValue() == "/AUTOSAR/MyRole"
            assert acl_permissions[0].getAclScope().getValue() == AclScopeEnum.EXPLICIT
        finally:
            os.remove(file_path)
