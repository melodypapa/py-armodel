"""
Tests for writer/parser serialization of the DocumentationOnM1 package
(Documentation, DocumentationContext) and PredefinedChapter.
"""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.DocumentationOnM1 import (
    DocumentationContext,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef import (
    AnyInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.models.M2.MSR.Documentation.Chapters import ChapterModel, PredefinedChapter
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    return ARXMLWriter()


def _parent():
    return ET.Element("PARENT")


def _ref(value, dest=None):
    ref = RefType()
    ref.setValue(value)
    if dest is not None:
        ref.setDest(dest)
    return ref


def _make_documentation():
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    return pkg.createDocumentation("Doc1")


class TestWriterPredefinedChapter:
    def test_with_chapter_model(self, writer):
        predefined = PredefinedChapter()
        predefined.setChapterModel(ChapterModel())
        parent = _parent()
        writer.writePredefinedChapter(parent, predefined)
        assert parent.find("CHAPTER-MODEL") is not None

    def test_without_chapter_model(self, writer):
        predefined = PredefinedChapter()
        parent = _parent()
        writer.writePredefinedChapter(parent, predefined)
        assert len(parent) == 0

    def test_none(self, writer):
        parent = _parent()
        writer.writePredefinedChapter(parent, None)
        assert len(parent) == 0


class TestWriterDocumentation:
    def test_full(self, writer):
        documentation = _make_documentation()
        context = DocumentationContext(documentation, "Ctx1")
        iref = AnyInstanceRef()
        iref.setBaseRef(_ref("/base", "SW-COMPONENT-TYPE"))
        iref.setTargetRef(_ref("/target", "SW-COMPONENT-TYPE"))
        context.setFeatureIRef(iref)
        context.setIdentifiableRef(_ref("/id", "IDENTIFIABLE"))
        documentation.addContext(context)
        predefined = PredefinedChapter()
        predefined.setChapterModel(ChapterModel())
        documentation.setDocumentationContent(predefined)
        parent = _parent()
        writer.writeDocumentation(parent, documentation)
        assert parent[0].tag == "DOCUMENTATION"
        assert parent[0].find("SHORT-NAME").text == "Doc1"
        contexts = parent[0].findall("CONTEXTS/DOCUMENTATION-CONTEXT")
        assert len(contexts) == 1
        assert contexts[0].find("SHORT-NAME").text == "Ctx1"
        assert contexts[0].find("FEATURE-IREF") is not None
        assert contexts[0].find("FEATURE-IREF/BASE-REF") is not None
        assert contexts[0].find("FEATURE-IREF/TARGET-REF") is not None
        assert contexts[0].find("IDENTIFIABLE-REF") is not None
        content = parent[0].find("DOCUMENTATION-CONTENT")
        assert content is not None
        assert content.find("CHAPTER-MODEL") is not None

    def test_minimal(self, writer):
        documentation = _make_documentation()
        parent = _parent()
        writer.writeDocumentation(parent, documentation)
        assert parent[0].tag == "DOCUMENTATION"
        assert parent[0].find("CONTEXTS") is None
        assert parent[0].find("DOCUMENTATION-CONTENT") is None


class TestDocumentationRoundTrip:
    def test_round_trip(self, tmp_path):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        pkg = document.createARPackage("Pkg")
        documentation = pkg.createDocumentation("Doc1")
        context = DocumentationContext(documentation, "Ctx1")
        iref = AnyInstanceRef()
        iref.setBaseRef(_ref("/base", "SW-COMPONENT-TYPE"))
        iref.setTargetRef(_ref("/target", "SW-COMPONENT-TYPE"))
        context.setFeatureIRef(iref)
        context.setIdentifiableRef(_ref("/id", "IDENTIFIABLE"))
        documentation.addContext(context)
        predefined = PredefinedChapter()
        chapter_model = ChapterModel()
        predefined.setChapterModel(chapter_model)
        documentation.setDocumentationContent(predefined)

        out_file = tmp_path / "documentation_out.arxml"
        ARXMLWriter().save(str(out_file), document)

        reloaded = AUTOSAR.getInstance()
        reloaded.clear()
        reloaded.setARRelease("R23-11")
        ARXMLParser().load(str(out_file), reloaded)

        doc = reloaded.find("/Pkg/Doc1")
        assert doc is not None
        assert len(doc.getContexts()) == 1
        ctx = doc.getContexts()[0]
        assert ctx.getShortName() == "Ctx1"
        assert ctx.getFeatureIRef() is not None
        assert ctx.getFeatureIRef().getBaseRef() is not None
        assert ctx.getFeatureIRef().getTargetRef() is not None
        assert ctx.getIdentifiableRef() is not None
        assert doc.getDocumentationContent() is not None
        assert doc.getDocumentationContent().getChapterModel() is not None

    def test_round_trip_empty(self, tmp_path):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        pkg = document.createARPackage("Pkg")
        pkg.createDocumentation("Doc1")

        out_file = tmp_path / "documentation_empty_out.arxml"
        ARXMLWriter().save(str(out_file), document)

        reloaded = AUTOSAR.getInstance()
        reloaded.clear()
        reloaded.setARRelease("R23-11")
        ARXMLParser().load(str(out_file), reloaded)

        doc = reloaded.find("/Pkg/Doc1")
        assert doc is not None
        assert doc.getContexts() == []
        assert doc.getDocumentationContent() is None
