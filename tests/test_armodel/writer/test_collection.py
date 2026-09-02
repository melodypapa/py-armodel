"""
Tests for writing COLLECTION elements (Collection, Table 13.1).

Round-trip counterpart: tests/test_armodel/parser/test_collection.py
"""

import logging
import os
import tempfile
import xml.etree.ElementTree as ET

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
from armodel.writer.arxml_writer import ARXMLWriter


def _make_writer() -> ARXMLWriter:
    writer = ARXMLWriter.__new__(ARXMLWriter)
    writer.logger = logging.getLogger("test.writer")
    return writer


class TestWriteCollection:
    """
    Test writeCollection (Collection, Table 13.1).
    """

    def test_write_optional_attributes(self):
        """Test that autoCollect, collectionSemantics and elementRole are written in XSD order."""
        writer = _make_writer()
        element = ET.Element("AR-PACKAGE")

        collection = Collection(None, "MyCollection")
        collection.setAutoCollect(AutoCollectEnum().setValue(AutoCollectEnum.REF_ALL))
        collection.setCollectionSemantics(NameToken().setValue("DECLINATION_OF"))
        collection.setElementRole(Identifier().setValue("PART_OF_SUBSET"))

        writer.writeCollection(element, collection)

        collection_tag = element.find("COLLECTION")
        assert collection_tag is not None
        tags = [child.tag for child in collection_tag]
        # SHORT-NAME/CATEGORY come from writeIdentifiable; the own attributes follow in
        # XSD sequenceOffset order: AUTO-COLLECT(20) < COLLECTION-SEMANTICS(25) < ELEMENT-ROLE(30)
        own_tags = [tag for tag in tags if tag in ("AUTO-COLLECT", "COLLECTION-SEMANTICS", "ELEMENT-ROLE")]
        assert own_tags == ["AUTO-COLLECT", "COLLECTION-SEMANTICS", "ELEMENT-ROLE"]
        assert collection_tag.find("AUTO-COLLECT").text == "REF-ALL"
        assert collection_tag.find("COLLECTION-SEMANTICS").text == "DECLINATION_OF"
        assert collection_tag.find("ELEMENT-ROLE").text == "PART_OF_SUBSET"

    def test_write_empty_collection(self):
        """Test that a Collection with no own attributes writes no own elements."""
        writer = _make_writer()
        element = ET.Element("AR-PACKAGE")

        collection = Collection(None, "MyCollection")
        writer.writeCollection(element, collection)

        collection_tag = element.find("COLLECTION")
        assert collection_tag is not None
        assert collection_tag.find("AUTO-COLLECT") is None
        assert collection_tag.find("ELEMENT-REFS") is None
        assert collection_tag.find("SOURCE-ELEMENT-REFS") is None
        assert collection_tag.find("COLLECTED-INSTANCE-IREFS") is None
        assert collection_tag.find("SOURCE-INSTANCE-IREFS") is None

    def test_write_element_refs(self):
        """Test that elementRefs are written as an ELEMENT-REFS wrapper with DEST attributes."""
        writer = _make_writer()
        element = ET.Element("AR-PACKAGE")

        collection = Collection(None, "MyCollection")
        ref = RefType()
        ref.setDest("PORT-PROTOTYPE-BLUEPRINT")
        ref.setValue("/AUTOSAR/EngN")
        collection.addElementRef(ref)

        writer.writeCollection(element, collection)

        collection_tag = element.find("COLLECTION")
        refs_tag = collection_tag.find("ELEMENT-REFS")
        assert refs_tag is not None
        ref_tag = refs_tag.find("ELEMENT-REF")
        assert ref_tag is not None
        assert ref_tag.attrib["DEST"] == "PORT-PROTOTYPE-BLUEPRINT"
        assert ref_tag.text == "/AUTOSAR/EngN"

    def test_write_source_element_refs(self):
        """Test that sourceElementRefs are written as a SOURCE-ELEMENT-REFS wrapper."""
        writer = _make_writer()
        element = ET.Element("AR-PACKAGE")

        collection = Collection(None, "MyCollection")
        ref = RefType()
        ref.setDest("COLLECTION")
        ref.setValue("/AUTOSAR/DefinedView")
        collection.addSourceElementRef(ref)

        writer.writeCollection(element, collection)

        collection_tag = element.find("COLLECTION")
        refs_tag = collection_tag.find("SOURCE-ELEMENT-REFS")
        assert refs_tag is not None
        ref_tag = refs_tag.find("SOURCE-ELEMENT-REF")
        assert ref_tag is not None
        assert ref_tag.attrib["DEST"] == "COLLECTION"
        assert ref_tag.text == "/AUTOSAR/DefinedView"

    def test_write_collected_instance_irefs(self):
        """Test that collectedInstanceIRefs are written as a COLLECTED-INSTANCE-IREFS wrapper."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef import (
            AnyInstanceRef,
        )

        writer = _make_writer()
        element = ET.Element("AR-PACKAGE")

        collection = Collection(None, "MyCollection")
        iref = AnyInstanceRef()
        target = RefType()
        target.setDest("IDENTIFIABLE")
        target.setValue("/AUTOSAR/Target")
        iref.setTargetRef(target)
        collection.addCollectedInstanceIRef(iref)

        writer.writeCollection(element, collection)

        collection_tag = element.find("COLLECTION")
        irefs_tag = collection_tag.find("COLLECTED-INSTANCE-IREFS")
        assert irefs_tag is not None
        iref_tag = irefs_tag.find("COLLECTED-INSTANCE-IREF")
        assert iref_tag is not None
        assert iref_tag.find("TARGET-REF").text == "/AUTOSAR/Target"

    def test_round_trip(self):
        """Build a model, write it, reparse, and assert every attribute survives."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        collection = ar_root.createCollection("MyCollection")
        collection.setAutoCollect(AutoCollectEnum().setValue(AutoCollectEnum.REF_NONE))
        collection.setElementRole(Identifier().setValue("PART_OF_SUBSET"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            from armodel.parser.arxml_parser import ARXMLParser

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            collection_2 = document_2.getARPackages()[0].getCollections()[0]
            assert collection_2.getShortName() == "MyCollection"
            assert collection_2.getAutoCollect().getValue() == "refNone"
            assert collection_2.getElementRole().getValue() == "PART_OF_SUBSET"
        finally:
            os.remove(file_path)
