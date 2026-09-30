"""
Tests for writing ACL-OPERATION elements (AclOperation, Table 11.4).

Round-trip counterpart: tests/test_armodel/parser/test_acl_operation.py
"""

import logging
import os
import tempfile
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.RolesAndRights import (
    AclOperation,
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


class TestWriteAclOperation:
    """
    Test writeAclOperation (AclOperation, Table 11.4).
    """

    def test_write_implied_operation_refs(self):
        """Test that impliedOperationRefs are written as an IMPLIED-OPERATION-REFS wrapper with DEST attributes."""
        writer = _make_writer()
        element = ET.Element("AR-PACKAGE")

        acl_operation = AclOperation(None, "MyAclOperation")
        acl_operation.addImpliedOperationRef(_ref("ACL-OPERATION", "/AUTOSAR/ImpliedOperation"))

        writer.writeAclOperation(element, acl_operation)

        acl_operation_tag = element.find("ACL-OPERATION")
        assert acl_operation_tag is not None
        refs_tag = acl_operation_tag.find("IMPLIED-OPERATION-REFS")
        assert refs_tag is not None
        ref_tag = refs_tag.find("IMPLIED-OPERATION-REF")
        assert ref_tag is not None
        assert ref_tag.attrib["DEST"] == "ACL-OPERATION"
        assert ref_tag.text == "/AUTOSAR/ImpliedOperation"

    def test_write_empty_wrappers(self):
        """Test that a AclOperation with no own members writes no own elements (empty-wrapper case)."""
        writer = _make_writer()
        element = ET.Element("AR-PACKAGE")

        acl_operation = AclOperation(None, "MyAclOperation")
        writer.writeAclOperation(element, acl_operation)

        acl_operation_tag = element.find("ACL-OPERATION")
        assert acl_operation_tag is not None
        assert acl_operation_tag.find("IMPLIED-OPERATION-REFS") is None

    def test_round_trip(self):
        """Write a AclOperation with every member set, reparse, and assert all fields survive."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        acl_operation = ar_root.createAclOperation("MyAclOperation")

        acl_operation.addImpliedOperationRef(_ref("ACL-OPERATION", "/AUTOSAR/ImpliedOperation"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            from armodel.parser.arxml_parser import ARXMLParser

            ARXMLParser().load(file_path, document_2)

            acl_operation_2 = document_2.getARPackages()[0].getAclOperations()[0]
            assert acl_operation_2.getShortName() == "MyAclOperation"
            assert acl_operation_2.getImpliedOperationRefs()[0].getDest() == "ACL-OPERATION"
            assert acl_operation_2.getImpliedOperationRefs()[0].getValue() == "/AUTOSAR/ImpliedOperation"
        finally:
            os.remove(file_path)
