"""
Tests for writing ACL-OBJECT-SET elements (AclObjectSet, Table 11.2).

Round-trip counterpart: tests/test_armodel/parser/test_acl_object_set.py
"""

import logging
import os
import tempfile
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject import (
    AutosarEngineeringObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AclScopeEnum,
    NameToken,
    ReferrableSubtypesEnum,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.RolesAndRights import (
    AclObjectSet,
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


class TestWriteAclObjectSet:
    """
    Test writeAclObjectSet (AclObjectSet, Table 11.2).
    """

    def test_write_members_in_xsd_order(self):
        """Test that own members are written in the XSD ACL-OBJECT-SET group order."""
        writer = _make_writer()
        element = ET.Element("AR-PACKAGE")

        acl_object_set = AclObjectSet(None, "MyAclObjectSet")
        acl_object_set.addAclObjectClass(ReferrableSubtypesEnum().setValue("COLLECTION"))
        acl_object_set.setAclScope(AclScopeEnum().setValue(AclScopeEnum.EXPLICIT))
        acl_object_set.setCollectionRef(_ref("COLLECTION", "/AUTOSAR/MyCollection"))
        acl_object_set.addDerivedFromBlueprintRef(_ref("LIFE-CYCLE-STATE-DEFINITION-GROUP", "/AUTOSAR/MyBlueprint"))
        engineering_object = AutosarEngineeringObject()
        engineering_object.setShortLabel(NameToken().setValue("eo.c"))
        acl_object_set.addEngineeringObject(engineering_object)
        acl_object_set.addObjectDefinitionRef(_ref("SW-BASE-TYPE", "/AUTOSAR/MyDef"))
        acl_object_set.addObjectRef(_ref("AR-PACKAGE", "/AUTOSAR/MyPackage"))

        writer.writeAclObjectSet(element, acl_object_set)

        acl_object_set_tag = element.find("ACL-OBJECT-SET")
        assert acl_object_set_tag is not None
        own_tags = [
            child.tag
            for child in acl_object_set_tag
            if child.tag in ("ACL-OBJECT-CLASSS", "ACL-SCOPE", "COLLECTION-REF", "DERIVED-FROM-BLUEPRINT-REFS", "ENGINEERING-OBJECTS", "OBJECT-DEFINITION-REFS", "OBJECT-REFS")
        ]
        assert own_tags == ["ACL-OBJECT-CLASSS", "ACL-SCOPE", "COLLECTION-REF", "DERIVED-FROM-BLUEPRINT-REFS", "ENGINEERING-OBJECTS", "OBJECT-DEFINITION-REFS", "OBJECT-REFS"]
        assert acl_object_set_tag.find("ACL-OBJECT-CLASSS/ACL-OBJECT-CLASS").text == "COLLECTION"
        assert acl_object_set_tag.find("ACL-SCOPE").text == "EXPLICIT"
        collection_ref_tag = acl_object_set_tag.find("COLLECTION-REF")
        assert collection_ref_tag.attrib["DEST"] == "COLLECTION"
        assert collection_ref_tag.text == "/AUTOSAR/MyCollection"
        assert acl_object_set_tag.find("DERIVED-FROM-BLUEPRINT-REFS/DERIVED-FROM-BLUEPRINT-REF").text == "/AUTOSAR/MyBlueprint"
        assert acl_object_set_tag.find("ENGINEERING-OBJECTS/AUTOSAR-ENGINEERING-OBJECT") is not None
        assert acl_object_set_tag.find("OBJECT-DEFINITION-REFS/OBJECT-DEFINITION-REF").text == "/AUTOSAR/MyDef"
        assert acl_object_set_tag.find("OBJECT-REFS/OBJECT-REF").text == "/AUTOSAR/MyPackage"

    def test_write_empty_wrappers(self):
        """Test that a AclObjectSet with no own members writes no own elements (empty-wrapper case)."""
        writer = _make_writer()
        element = ET.Element("AR-PACKAGE")

        acl_object_set = AclObjectSet(None, "MyAclObjectSet")
        writer.writeAclObjectSet(element, acl_object_set)

        acl_object_set_tag = element.find("ACL-OBJECT-SET")
        assert acl_object_set_tag is not None
        assert acl_object_set_tag.find("ACL-OBJECT-CLASSS") is None
        assert acl_object_set_tag.find("ACL-SCOPE") is None
        assert acl_object_set_tag.find("COLLECTION-REF") is None
        assert acl_object_set_tag.find("DERIVED-FROM-BLUEPRINT-REFS") is None
        assert acl_object_set_tag.find("ENGINEERING-OBJECTS") is None
        assert acl_object_set_tag.find("OBJECT-DEFINITION-REFS") is None
        assert acl_object_set_tag.find("OBJECT-REFS") is None

    def test_round_trip(self):
        """Write a AclObjectSet with every member set, reparse, and assert all fields survive."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        acl_object_set = ar_root.createAclObjectSet("MyAclObjectSet")

        acl_object_set.addAclObjectClass(ReferrableSubtypesEnum().setValue("COLLECTION"))
        acl_object_set.setAclScope(AclScopeEnum().setValue(AclScopeEnum.DEPENDANT))
        acl_object_set.setCollectionRef(_ref("COLLECTION", "/AUTOSAR/MyCollection"))
        acl_object_set.addDerivedFromBlueprintRef(_ref("LIFE-CYCLE-STATE-DEFINITION-GROUP", "/AUTOSAR/MyBlueprint"))
        engineering_object = AutosarEngineeringObject()
        engineering_object.setShortLabel(NameToken().setValue("eo.c"))
        acl_object_set.addEngineeringObject(engineering_object)
        acl_object_set.addObjectDefinitionRef(_ref("SW-BASE-TYPE", "/AUTOSAR/MyDef"))
        acl_object_set.addObjectRef(_ref("AR-PACKAGE", "/AUTOSAR/MyPackage"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            from armodel.parser.arxml_parser import ARXMLParser

            ARXMLParser().load(file_path, document_2)

            acl_object_set_2 = document_2.getARPackages()[0].getAclObjectSets()[0]
            assert acl_object_set_2.getShortName() == "MyAclObjectSet"
            assert acl_object_set_2.getAclObjectClasses()[0].getValue() == "COLLECTION"
            assert acl_object_set_2.getAclScope().getValue() == AclScopeEnum.DEPENDANT
            assert acl_object_set_2.getCollectionRef().getDest() == "COLLECTION"
            assert acl_object_set_2.getCollectionRef().getValue() == "/AUTOSAR/MyCollection"
            assert acl_object_set_2.getDerivedFromBlueprintRefs()[0].getValue() == "/AUTOSAR/MyBlueprint"
            assert len(acl_object_set_2.getEngineeringObjects()) == 1
            assert acl_object_set_2.getEngineeringObjects()[0].getShortLabel().getValue() == "eo.c"
            assert acl_object_set_2.getObjectDefinitionRefs()[0].getValue() == "/AUTOSAR/MyDef"
            assert acl_object_set_2.getObjectRefs()[0].getDest() == "AR-PACKAGE"
            assert acl_object_set_2.getObjectRefs()[0].getValue() == "/AUTOSAR/MyPackage"
        finally:
            os.remove(file_path)
