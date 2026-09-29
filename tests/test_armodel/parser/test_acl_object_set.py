"""
Tests for parsing ACL-OBJECT-SET elements (AclObjectSet, Table 11.2).

Round-trip counterpart: tests/test_armodel/writer/test_acl_object_set.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    AclObjectSet,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AclScopeEnum,
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


def _make_acl_object_set() -> AclObjectSet:
    AUTOSAR.getInstance().new()
    ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
    return ar_root.createAclObjectSet("MyAclObjectSet")


class TestReadAclObjectSet:
    """
    Test readAclObjectSet (AclObjectSet, Table 11.2).
    """

    def test_read_acl_object_classs(self, parser):
        """Test that the ACL-OBJECT-CLASSS wrapper (XSD spelling) populates aclObjectClasses."""
        acl_object_set = _make_acl_object_set()
        element = ET.fromstring(
            f"""<ACL-OBJECT-SET xmlns='{NS}'>
                <SHORT-NAME>MyAclObjectSet</SHORT-NAME>
                <ACL-OBJECT-CLASSS>
                    <ACL-OBJECT-CLASS>COLLECTION</ACL-OBJECT-CLASS>
                    <ACL-OBJECT-CLASS>AR-PACKAGE</ACL-OBJECT-CLASS>
                </ACL-OBJECT-CLASSS>
            </ACL-OBJECT-SET>"""
        )

        parser.readAclObjectSet(element, acl_object_set)

        acl_object_classes = acl_object_set.getAclObjectClasses()
        assert len(acl_object_classes) == 2
        assert acl_object_classes[0].getValue() == "COLLECTION"
        assert acl_object_classes[1].getValue() == "AR-PACKAGE"

    def test_read_scope_and_collection_ref(self, parser):
        """Test that ACL-SCOPE and COLLECTION-REF populate the model."""
        acl_object_set = _make_acl_object_set()
        element = ET.fromstring(
            f"""<ACL-OBJECT-SET xmlns='{NS}'>
                <SHORT-NAME>MyAclObjectSet</SHORT-NAME>
                <ACL-SCOPE>EXPLICIT</ACL-SCOPE>
                <COLLECTION-REF DEST="COLLECTION">/AUTOSAR/MyCollection</COLLECTION-REF>
            </ACL-OBJECT-SET>"""
        )

        parser.readAclObjectSet(element, acl_object_set)

        assert acl_object_set.getAclScope() is not None
        assert acl_object_set.getAclScope().getValue() == AclScopeEnum.EXPLICIT
        assert acl_object_set.getCollectionRef() is not None
        assert acl_object_set.getCollectionRef().getDest() == "COLLECTION"
        assert acl_object_set.getCollectionRef().getValue() == "/AUTOSAR/MyCollection"

    def test_read_refs_and_engineering_objects(self, parser):
        """Test that DERIVED-FROM-BLUEPRINT-REFS, ENGINEERING-OBJECTS, OBJECT-DEFINITION-REFS and OBJECT-REFS populate the model."""
        acl_object_set = _make_acl_object_set()
        element = ET.fromstring(
            f"""<ACL-OBJECT-SET xmlns='{NS}'>
                <SHORT-NAME>MyAclObjectSet</SHORT-NAME>
                <DERIVED-FROM-BLUEPRINT-REFS>
                    <DERIVED-FROM-BLUEPRINT-REF DEST="LIFE-CYCLE-STATE-DEFINITION-GROUP">/AUTOSAR/MyBlueprint</DERIVED-FROM-BLUEPRINT-REF>
                </DERIVED-FROM-BLUEPRINT-REFS>
                <ENGINEERING-OBJECTS>
                    <AUTOSAR-ENGINEERING-OBJECT>
                        <SHORT-LABEL>eo.c</SHORT-LABEL>
                        <CATEGORY>AUTOSAR</CATEGORY>
                    </AUTOSAR-ENGINEERING-OBJECT>
                </ENGINEERING-OBJECTS>
                <OBJECT-DEFINITION-REFS>
                    <OBJECT-DEFINITION-REF DEST="SW-BASE-TYPE">/AUTOSAR/MyDef</OBJECT-DEFINITION-REF>
                </OBJECT-DEFINITION-REFS>
                <OBJECT-REFS>
                    <OBJECT-REF DEST="AR-PACKAGE">/AUTOSAR/MyPackage</OBJECT-REF>
                </OBJECT-REFS>
            </ACL-OBJECT-SET>"""
        )

        parser.readAclObjectSet(element, acl_object_set)

        blueprint_refs = acl_object_set.getDerivedFromBlueprintRefs()
        assert len(blueprint_refs) == 1
        assert blueprint_refs[0].getDest() == "LIFE-CYCLE-STATE-DEFINITION-GROUP"
        assert blueprint_refs[0].getValue() == "/AUTOSAR/MyBlueprint"

        engineering_objects = acl_object_set.getEngineeringObjects()
        assert len(engineering_objects) == 1
        assert engineering_objects[0].getShortLabel().getValue() == "eo.c"
        assert engineering_objects[0].getCategory().getValue() == "AUTOSAR"

        object_definition_refs = acl_object_set.getObjectDefinitionRefs()
        assert len(object_definition_refs) == 1
        assert object_definition_refs[0].getDest() == "SW-BASE-TYPE"
        assert object_definition_refs[0].getValue() == "/AUTOSAR/MyDef"

        object_refs = acl_object_set.getObjectRefs()
        assert len(object_refs) == 1
        assert object_refs[0].getDest() == "AR-PACKAGE"
        assert object_refs[0].getValue() == "/AUTOSAR/MyPackage"

    def test_read_absent_optional_members(self, parser):
        """Test that absent optional members leave the fields untouched (empty-wrapper case)."""
        acl_object_set = _make_acl_object_set()
        element = ET.fromstring(
            f"""<ACL-OBJECT-SET xmlns='{NS}'>
                <SHORT-NAME>MyAclObjectSet</SHORT-NAME>
            </ACL-OBJECT-SET>"""
        )

        parser.readAclObjectSet(element, acl_object_set)

        assert acl_object_set.getAclObjectClasses() == []
        assert acl_object_set.getAclScope() is None
        assert acl_object_set.getCollectionRef() is None
        assert acl_object_set.getDerivedFromBlueprintRefs() == []
        assert acl_object_set.getEngineeringObjects() == []
        assert acl_object_set.getObjectDefinitionRefs() == []
        assert acl_object_set.getObjectRefs() == []

    def test_load_via_ar_package(self, parser):
        """Test that the ARPackage ELEMENTS dispatch reads an ACL-OBJECT-SET into getAclObjectSets()."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        content = f"""<?xml version="1.0" encoding="utf-8"?>
<AUTOSAR xmlns="{NS}" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="{NS} AUTOSAR_00052.xsd">
    <AR-PACKAGES>
        <AR-PACKAGE>
            <SHORT-NAME>AUTOSAR</SHORT-NAME>
            <ELEMENTS>
                <ACL-OBJECT-SET>
                    <SHORT-NAME>MyAclObjectSet</SHORT-NAME>
                    <ACL-OBJECT-CLASSS>
                        <ACL-OBJECT-CLASS>COLLECTION</ACL-OBJECT-CLASS>
                    </ACL-OBJECT-CLASSS>
                    <ACL-SCOPE>DEPENDANT</ACL-SCOPE>
                    <COLLECTION-REF DEST="COLLECTION">/AUTOSAR/MyCollection</COLLECTION-REF>
                    <OBJECT-REFS>
                        <OBJECT-REF DEST="AR-PACKAGE">/AUTOSAR/MyPackage</OBJECT-REF>
                    </OBJECT-REFS>
                </ACL-OBJECT-SET>
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

            acl_object_sets = document.getARPackages()[0].getAclObjectSets()
            assert len(acl_object_sets) == 1
            assert acl_object_sets[0].getShortName() == "MyAclObjectSet"
            assert acl_object_sets[0].getAclObjectClasses()[0].getValue() == "COLLECTION"
            assert acl_object_sets[0].getAclScope().getValue() == AclScopeEnum.DEPENDANT
            assert acl_object_sets[0].getCollectionRef().getValue() == "/AUTOSAR/MyCollection"
            assert acl_object_sets[0].getObjectRefs()[0].getValue() == "/AUTOSAR/MyPackage"
        finally:
            os.remove(file_path)
