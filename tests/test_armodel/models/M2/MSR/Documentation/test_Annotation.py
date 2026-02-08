"""
This module contains tests for the Annotation module in MSR.Documentation.
"""
import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
)
from armodel.models.M2.MSR.Documentation.Annotation import *
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import (
    DocumentationBlock,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import (
    MultilanguageLongName,
)


class TestGeneralAnnotation:
    """Test class for GeneralAnnotation abstract class."""

    def test_general_annotation_abstract_class(self):
        """Test that GeneralAnnotation cannot be instantiated directly."""
        # This should raise NotImplementedError
        with pytest.raises(TypeError):
            GeneralAnnotation()

    def test_general_annotation_initialization(self):
        """Test that a concrete subclass can be initialized with default values."""
        # Create a concrete subclass for testing
        class ConcreteGeneralAnnotation(GeneralAnnotation):
            def __init__(self):
                super().__init__()

        concrete_annotation = ConcreteGeneralAnnotation()
        assert concrete_annotation.annotationOrigin is None
        assert concrete_annotation.annotationText is None
        assert concrete_annotation.label is None

    def test_general_annotation_origin_methods(self):
        """Test the annotationOrigin getter and setter."""
        class ConcreteGeneralAnnotation(GeneralAnnotation):
            def __init__(self):
                super().__init__()

        concrete_annotation = ConcreteGeneralAnnotation()
        origin = ARLiteral()

        result = concrete_annotation.setAnnotationOrigin(origin)
        assert concrete_annotation.getAnnotationOrigin() == origin
        assert result == concrete_annotation

    def test_general_annotation_text_methods(self):
        """Test the annotationText getter and setter."""
        class ConcreteGeneralAnnotation(GeneralAnnotation):
            def __init__(self):
                super().__init__()

        concrete_annotation = ConcreteGeneralAnnotation()
        text = DocumentationBlock()

        result = concrete_annotation.setAnnotationText(text)
        assert concrete_annotation.getAnnotationText() == text
        assert result == concrete_annotation

    def test_general_annotation_label_methods(self):
        """Test the label getter and setter."""
        class ConcreteGeneralAnnotation(GeneralAnnotation):
            def __init__(self):
                super().__init__()

        concrete_annotation = ConcreteGeneralAnnotation()
        label = MultilanguageLongName()

        result = concrete_annotation.setLabel(label)
        assert concrete_annotation.getLabel() == label
        assert result == concrete_annotation


class TestAnnotation:
    """Test class for Annotation class."""

    def test_annotation_initialization(self):
        """Test that an Annotation object can be initialized with default values."""
        annotation = Annotation()
        # Inherits from GeneralAnnotation, so check default values
        assert annotation.annotationOrigin is None
        assert annotation.annotationText is None
        assert annotation.label is None
