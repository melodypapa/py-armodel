"""
Tests for the DocumentationOnM1 package classes (Documentation and
DocumentationContext).
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.DocumentationOnM1 import (
    Documentation,
    DocumentationContext,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef import (
    AnyInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.models.M2.MSR.Documentation.Chapters import PredefinedChapter


def _parent():
    document = AUTOSAR.getInstance()
    return document.createARPackage("AUTOSAR")


class TestDocumentation:
    """Test class for the Documentation class."""

    def test_initialization(self):
        parent = _parent()
        documentation = Documentation(parent, "MyDoc")
        assert documentation.getShortName() == "MyDoc"
        assert documentation.getContexts() == []
        assert documentation.getDocumentationContent() is None

    def test_add_get_context(self):
        parent = _parent()
        documentation = Documentation(parent, "MyDoc")
        context = DocumentationContext(parent, "Context1")
        assert documentation.addContext(context) is documentation
        assert documentation.getContexts() == [context]

    def test_set_get_documentation_content(self):
        parent = _parent()
        documentation = Documentation(parent, "MyDoc")
        predefined = PredefinedChapter()
        assert documentation.setDocumentationContent(predefined) is documentation
        assert documentation.getDocumentationContent() is predefined
        documentation.setDocumentationContent(None)
        assert documentation.getDocumentationContent() is predefined


class TestDocumentationContext:
    """Test class for the DocumentationContext class."""

    def test_initialization(self):
        parent = _parent()
        context = DocumentationContext(parent, "Context1")
        assert context.getShortName() == "Context1"
        assert context.getFeatureIRef() is None
        assert context.getIdentifiableRef() is None

    def test_set_get_feature_iref(self):
        parent = _parent()
        context = DocumentationContext(parent, "Context1")
        iref = AnyInstanceRef()
        assert context.setFeatureIRef(iref) is context
        assert context.getFeatureIRef() is iref
        context.setFeatureIRef(None)
        assert context.getFeatureIRef() is iref

    def test_set_get_identifiable_ref(self):
        parent = _parent()
        context = DocumentationContext(parent, "Context1")
        ref = RefType()
        ref.setValue("/Some/Path")
        assert context.setIdentifiableRef(ref) is context
        assert context.getIdentifiableRef() is ref
        context.setIdentifiableRef(None)
        assert context.getIdentifiableRef() is ref
