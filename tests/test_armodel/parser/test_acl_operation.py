"""
Tests for parsing ACL-OPERATION elements (AclOperation, Table 11.4).

Round-trip counterpart: tests/test_armodel/writer/test_acl_operation.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    AclOperation,
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


def _make_acl_operation() -> AclOperation:
    AUTOSAR.getInstance().new()
    ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
    return ar_root.createAclOperation("MyAclOperation")


class TestReadAclOperation:
    """
    Test readAclOperation (AclOperation, Table 11.4).
    """

    def test_read_implied_operation_refs(self, parser):
        """Test that the IMPLIED-OPERATION-REFS wrapper populates impliedOperationRefs with DEST and value."""
        acl_operation = _make_acl_operation()
        element = ET.fromstring(
            f"""<ACL-OPERATION xmlns='{NS}'>
                <SHORT-NAME>MyAclOperation</SHORT-NAME>
                <IMPLIED-OPERATION-REFS>
                    <IMPLIED-OPERATION-REF DEST="ACL-OPERATION">/AUTOSAR/ImpliedOperation</IMPLIED-OPERATION-REF>
                </IMPLIED-OPERATION-REFS>
            </ACL-OPERATION>"""
        )

        parser.readAclOperation(element, acl_operation)

        refs = acl_operation.getImpliedOperationRefs()
        assert len(refs) == 1
        assert refs[0].getDest() == "ACL-OPERATION"
        assert refs[0].getValue() == "/AUTOSAR/ImpliedOperation"

    def test_read_absent_optional_members(self, parser):
        """Test that absent optional members leave the fields untouched (empty-wrapper case)."""
        acl_operation = _make_acl_operation()
        element = ET.fromstring(
            f"""<ACL-OPERATION xmlns='{NS}'>
                <SHORT-NAME>MyAclOperation</SHORT-NAME>
            </ACL-OPERATION>"""
        )

        parser.readAclOperation(element, acl_operation)

        assert acl_operation.getImpliedOperationRefs() == []

    def test_load_via_ar_package(self, parser):
        """Test that the ARPackage ELEMENTS dispatch reads an ACL-OPERATION into getAclOperations()."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        content = f"""<?xml version="1.0" encoding="utf-8"?>
<AUTOSAR xmlns="{NS}" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="{NS} AUTOSAR_00052.xsd">
    <AR-PACKAGES>
        <AR-PACKAGE>
            <SHORT-NAME>AUTOSAR</SHORT-NAME>
            <ELEMENTS>
                <ACL-OPERATION>
                    <SHORT-NAME>MyAclOperation</SHORT-NAME>
                    <IMPLIED-OPERATION-REFS>
                        <IMPLIED-OPERATION-REF DEST="ACL-OPERATION">/AUTOSAR/ImpliedOperation</IMPLIED-OPERATION-REF>
                    </IMPLIED-OPERATION-REFS>
                </ACL-OPERATION>
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

            acl_operations = document.getARPackages()[0].getAclOperations()
            assert len(acl_operations) == 1
            assert acl_operations[0].getShortName() == "MyAclOperation"
            assert acl_operations[0].getImpliedOperationRefs()[0].getValue() == "/AUTOSAR/ImpliedOperation"
        finally:
            os.remove(file_path)
