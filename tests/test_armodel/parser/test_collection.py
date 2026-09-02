"""
Tests for parsing COLLECTION elements (Collection, Table 13.1).

Round-trip counterpart: tests/test_armodel/writer/test_collection.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection import (
    AutoCollectEnum,
    Collection,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    NameToken,
    RefType,
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


def _make_collection() -> Collection:
    AUTOSAR.getInstance().new()
    ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
    return ar_root.createCollection("MyCollection")


class TestReadCollection:
    """
    Test readCollection (Collection, Table 13.1).
    """

    def test_read_optional_attributes(self, parser):
        """Test that AUTO-COLLECT, COLLECTION-SEMANTICS and ELEMENT-ROLE populate the model."""
        collection = _make_collection()
        element = ET.fromstring(
            f"""<COLLECTION xmlns='{NS}'>
                <SHORT-NAME>MyCollection</SHORT-NAME>
                <CATEGORY>RELATION</CATEGORY>
                <AUTO-COLLECT>REF-ALL</AUTO-COLLECT>
                <COLLECTION-SEMANTICS>DECLINATION_OF</COLLECTION-SEMANTICS>
                <ELEMENT-ROLE>PART_OF_SUBSET</ELEMENT-ROLE>
            </COLLECTION>"""
        )

        parser.readCollection(element, collection)

        assert collection.getAutoCollect() is not None
        assert collection.getAutoCollect().getValue() == "refAll"
        assert collection.getCollectionSemantics() is not None
        assert collection.getCollectionSemantics().getValue() == "DECLINATION_OF"
        assert collection.getElementRole() is not None
        assert collection.getElementRole().getValue() == "PART_OF_SUBSET"

    def test_read_absent_optional_attributes(self, parser):
        """Test that absent optional attribute elements leave the fields untouched."""
        collection = _make_collection()
        element = ET.fromstring(
            f"""<COLLECTION xmlns='{NS}'>
                <SHORT-NAME>MyCollection</SHORT-NAME>
            </COLLECTION>"""
        )

        parser.readCollection(element, collection)

        assert collection.getAutoCollect() is None
        assert collection.getCollectionSemantics() is None
        assert collection.getElementRole() is None

    def test_read_element_refs(self, parser):
        """Test that the ELEMENT-REFS wrapper populates elementRefs with DEST and value."""
        collection = _make_collection()
        element = ET.fromstring(
            f"""<COLLECTION xmlns='{NS}'>
                <SHORT-NAME>MyCollection</SHORT-NAME>
                <ELEMENT-REFS>
                    <ELEMENT-REF DEST="PORT-PROTOTYPE-BLUEPRINT">/AUTOSAR/EngN</ELEMENT-REF>
                    <ELEMENT-REF DEST="COLLECTION">/AUTOSAR/ExpandedView</ELEMENT-REF>
                </ELEMENT-REFS>
            </COLLECTION>"""
        )

        parser.readCollection(element, collection)

        refs = collection.getElementRefs()
        assert len(refs) == 2
        assert refs[0].getDest() == "PORT-PROTOTYPE-BLUEPRINT"
        assert refs[0].getValue() == "/AUTOSAR/EngN"
        assert refs[1].getDest() == "COLLECTION"
        assert refs[1].getValue() == "/AUTOSAR/ExpandedView"

    def test_read_source_element_refs(self, parser):
        """Test that the SOURCE-ELEMENT-REFS wrapper populates sourceElementRefs."""
        collection = _make_collection()
        element = ET.fromstring(
            f"""<COLLECTION xmlns='{NS}'>
                <SHORT-NAME>MyCollection</SHORT-NAME>
                <SOURCE-ELEMENT-REFS>
                    <SOURCE-ELEMENT-REF DEST="COLLECTION">/AUTOSAR/DefinedView</SOURCE-ELEMENT-REF>
                </SOURCE-ELEMENT-REFS>
            </COLLECTION>"""
        )

        parser.readCollection(element, collection)

        refs = collection.getSourceElementRefs()
        assert len(refs) == 1
        assert refs[0].getDest() == "COLLECTION"
        assert refs[0].getValue() == "/AUTOSAR/DefinedView"

    def test_read_collected_instance_irefs(self, parser):
        """Test that COLLECTED-INSTANCE-IREFS/COLLECTED-INSTANCE-IREF populates collectedInstanceIRefs."""
        collection = _make_collection()
        element = ET.fromstring(
            f"""<COLLECTION xmlns='{NS}'>
                <SHORT-NAME>MyCollection</SHORT-NAME>
                <COLLECTED-INSTANCE-IREFS>
                    <COLLECTED-INSTANCE-IREF>
                        <BASE-REF DEST="IDENTIFIABLE">/AUTOSAR/Base</BASE-REF>
                        <CONTEXT-ELEMENT-REF DEST="COLLECTION">/AUTOSAR/Ctx</CONTEXT-ELEMENT-REF>
                        <TARGET-REF DEST="IDENTIFIABLE">/AUTOSAR/Target</TARGET-REF>
                    </COLLECTED-INSTANCE-IREF>
                </COLLECTED-INSTANCE-IREFS>
            </COLLECTION>"""
        )

        parser.readCollection(element, collection)

        irefs = collection.getCollectedInstanceIRefs()
        assert len(irefs) == 1
        assert irefs[0].getBaseRef().getValue() == "/AUTOSAR/Base"
        assert irefs[0].getContextElementRefs()[0].getValue() == "/AUTOSAR/Ctx"
        assert irefs[0].getTargetRef().getValue() == "/AUTOSAR/Target"

    def test_read_source_instance_irefs(self, parser):
        """Test that SOURCE-INSTANCE-IREFS/SOURCE-INSTANCE-IREF populates sourceInstanceIRefs."""
        collection = _make_collection()
        element = ET.fromstring(
            f"""<COLLECTION xmlns='{NS}'>
                <SHORT-NAME>MyCollection</SHORT-NAME>
                <SOURCE-INSTANCE-IREFS>
                    <SOURCE-INSTANCE-IREF>
                        <TARGET-REF DEST="IDENTIFIABLE">/AUTOSAR/Target</TARGET-REF>
                    </SOURCE-INSTANCE-IREF>
                </SOURCE-INSTANCE-IREFS>
            </COLLECTION>"""
        )

        parser.readCollection(element, collection)

        irefs = collection.getSourceInstanceIRefs()
        assert len(irefs) == 1
        assert irefs[0].getTargetRef().getValue() == "/AUTOSAR/Target"

    def test_load_via_ar_package(self, parser):
        """Test that the ARPackage ELEMENTS dispatch reads a COLLECTION into getCollections()."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        content = f"""<?xml version="1.0" encoding="utf-8"?>
<AUTOSAR xmlns="{NS}" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="{NS} AUTOSAR_00052.xsd">
    <AR-PACKAGES>
        <AR-PACKAGE>
            <SHORT-NAME>AUTOSAR</SHORT-NAME>
            <ELEMENTS>
                <COLLECTION>
                    <SHORT-NAME>MyCollection</SHORT-NAME>
                    <CATEGORY>SET</CATEGORY>
                    <AUTO-COLLECT>REF-NONE</AUTO-COLLECT>
                    <ELEMENT-ROLE>PART_OF_SUBSET</ELEMENT-ROLE>
                    <ELEMENT-REFS>
                        <ELEMENT-REF DEST="PORT-PROTOTYPE-BLUEPRINT">/AUTOSAR/EngN</ELEMENT-REF>
                    </ELEMENT-REFS>
                </COLLECTION>
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

            collections = document.getARPackages()[0].getCollections()
            assert len(collections) == 1
            assert collections[0].getShortName() == "MyCollection"
            assert collections[0].getAutoCollect().getValue() == "refNone"
            assert collections[0].getElementRefs()[0].getValue() == "/AUTOSAR/EngN"
        finally:
            os.remove(file_path)

    def test_round_trip(self):
        """Write a Collection with every attribute set, reparse, and assert all fields survive."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        collection = ar_root.createCollection("MyCollection")

        collection.setAutoCollect(AutoCollectEnum().setValue(AutoCollectEnum.REF_ALL))
        collection.setCollectionSemantics(NameToken().setValue("DECLINATION_OF"))
        collection.setElementRole(Identifier().setValue("PART_OF_SUBSET"))

        element_ref = RefType()
        element_ref.setDest("COLLECTION")
        element_ref.setValue("/AUTOSAR/ExpandedView")
        collection.addElementRef(element_ref)

        source_ref = RefType()
        source_ref.setDest("COLLECTION")
        source_ref.setValue("/AUTOSAR/DefinedView")
        collection.addSourceElementRef(source_ref)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            from armodel.writer.arxml_writer import ARXMLWriter

            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            collection_2 = document_2.getARPackages()[0].getCollections()[0]
            assert collection_2.getShortName() == "MyCollection"
            assert collection_2.getAutoCollect().getValue() == "refAll"
            assert collection_2.getCollectionSemantics().getValue() == "DECLINATION_OF"
            assert collection_2.getElementRole().getValue() == "PART_OF_SUBSET"
            assert collection_2.getElementRefs()[0].getValue() == "/AUTOSAR/ExpandedView"
            assert collection_2.getElementRefs()[0].getDest() == "COLLECTION"
            assert collection_2.getSourceElementRefs()[0].getValue() == "/AUTOSAR/DefinedView"
        finally:
            os.remove(file_path)
