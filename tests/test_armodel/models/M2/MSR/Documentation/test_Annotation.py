"""
This module contains tests for the Annotation module in MSR.Documentation.
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
from armodel.models.M2.MSR.Documentation.Annotation import Annotation, GeneralAnnotation
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultilanguageLongName

NOTE = (
    "This class represents textual comments (called annotations) which relate to the object in which it is aggregated. "
    "These annotations are intended for use during the development process for transferring information from one step of "
    'the development process to the next one. The approach is similar to the "yellow pads" ... This abstract class can be '
    "specialized in order to add some further formal properties."
)


class ConcreteGeneralAnnotation(GeneralAnnotation):
    def __init__(self):
        super().__init__()


class TestGeneralAnnotation:
    """Test class for GeneralAnnotation abstract class (AUTOSAR_CP_TPS_SoftwareComponentTemplate, Table 4.56, p.163)."""

    def test_general_annotation_class_note_verbatim(self):
        """The class docstring must reproduce the Table 4.56 Note verbatim."""
        assert GeneralAnnotation.__doc__ == NOTE

    def test_general_annotation_init_has_no_docstring(self):
        """__init__ must not carry a docstring."""
        assert GeneralAnnotation.__init__.__doc__ is None

    def test_general_annotation_base_chain(self):
        """GeneralAnnotation derives from ARObject and Annotation from GeneralAnnotation."""
        assert issubclass(GeneralAnnotation, ARObject)
        assert issubclass(Annotation, GeneralAnnotation)

    def test_general_annotation_abstract_class(self):
        """Test that GeneralAnnotation cannot be instantiated directly."""
        with pytest.raises(TypeError):
            GeneralAnnotation()

    def test_general_annotation_initialization(self):
        """Test that a concrete subclass can be initialized with default values."""
        concrete_annotation = ConcreteGeneralAnnotation()
        assert concrete_annotation.annotationOrigin is None
        assert concrete_annotation.annotationText is None
        assert concrete_annotation.label is None

    def test_general_annotation_origin_methods(self):
        """Test the annotationOrigin getter and setter round-trip."""
        concrete_annotation = ConcreteGeneralAnnotation()
        origin = String()
        origin.setValue("manual")

        result = concrete_annotation.setAnnotationOrigin(origin)
        assert concrete_annotation.getAnnotationOrigin() == origin
        assert result == concrete_annotation

    def test_general_annotation_origin_none_noop(self):
        """A None passed to setAnnotationOrigin is a no-op and does not overwrite an existing annotationOrigin."""
        concrete_annotation = ConcreteGeneralAnnotation()
        origin = String()
        origin.setValue("manual")
        concrete_annotation.setAnnotationOrigin(origin)

        result = concrete_annotation.setAnnotationOrigin(None)
        assert concrete_annotation.getAnnotationOrigin() == origin
        assert result == concrete_annotation

    def test_general_annotation_text_methods(self):
        """Test the annotationText getter and setter round-trip."""
        concrete_annotation = ConcreteGeneralAnnotation()
        text = DocumentationBlock()

        result = concrete_annotation.setAnnotationText(text)
        assert concrete_annotation.getAnnotationText() == text
        assert result == concrete_annotation

    def test_general_annotation_text_none_noop(self):
        """A None passed to setAnnotationText is a no-op and does not overwrite an existing annotationText."""
        concrete_annotation = ConcreteGeneralAnnotation()
        text = DocumentationBlock()
        concrete_annotation.setAnnotationText(text)

        result = concrete_annotation.setAnnotationText(None)
        assert concrete_annotation.getAnnotationText() == text
        assert result == concrete_annotation

    def test_general_annotation_label_methods(self):
        """Test the label getter and setter round-trip."""
        concrete_annotation = ConcreteGeneralAnnotation()
        label = MultilanguageLongName()

        result = concrete_annotation.setLabel(label)
        assert concrete_annotation.getLabel() == label
        assert result == concrete_annotation

    def test_general_annotation_label_none_noop(self):
        """A None passed to setLabel is a no-op and does not overwrite an existing label."""
        concrete_annotation = ConcreteGeneralAnnotation()
        label = MultilanguageLongName()
        concrete_annotation.setLabel(label)

        result = concrete_annotation.setLabel(None)
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
