from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultilanguageLongName
from abc import ABC
from typing import Optional


class GeneralAnnotation(ARObject, ABC):
    """This class represents textual comments (called annotations) which relate to the object in which it is aggregated. These annotations are intended for use during the development process for transferring information from one step of the development process to the next one. The approach is similar to the "yellow pads" ... This abstract class can be specialized in order to add some further formal properties."""

    # GeneralAnnotation method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.56, p.163
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAnnotationOrigin  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAnnotationOrigin  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getAnnotationText    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAnnotationText    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getLabel             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setLabel             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        if type(self) is GeneralAnnotation:
            raise TypeError("GeneralAnnotation is an abstract class.")

        super().__init__()

        # This attribute identifies the origin of the annotation. It is an arbitrary string since it can be an individual's name as well as the name of a tool or even the name of a process step. Tags: xml.sequenceOffset=30
        self.annotationOrigin: Optional[String] = None

        # This is the text of the annotation. Tags: xml.sequenceOffset=40
        self.annotationText: Optional[DocumentationBlock] = None

        # This is the headline for the annotation. Tags: xml.sequenceOffset=20
        self.label: Optional[MultilanguageLongName] = None

    def getAnnotationOrigin(self) -> Optional[String]:
        """
        This attribute identifies the origin of the annotation. It is an arbitrary string since it can be an individual's name as well as the name of a tool or even the name of a process step. Tags: xml.sequenceOffset=30

        Returns:
            The origin of the annotation
        """
        return self.annotationOrigin

    def setAnnotationOrigin(self, value: Optional[String]) -> "GeneralAnnotation":
        """
        This attribute identifies the origin of the annotation. It is an arbitrary string since it can be an individual's name as well as the name of a tool or even the name of a process step. Tags: xml.sequenceOffset=30

        A None value is a no-op and does not overwrite an existing annotationOrigin.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.annotationOrigin = value
        return self

    def getAnnotationText(self) -> Optional[DocumentationBlock]:
        """
        This is the text of the annotation. Tags: xml.sequenceOffset=40

        Returns:
            The text of the annotation
        """
        return self.annotationText

    def setAnnotationText(self, value: Optional[DocumentationBlock]) -> "GeneralAnnotation":
        """
        This is the text of the annotation. Tags: xml.sequenceOffset=40

        A None value is a no-op and does not overwrite an existing annotationText.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.annotationText = value
        return self

    def getLabel(self) -> Optional[MultilanguageLongName]:
        """
        This is the headline for the annotation. Tags: xml.sequenceOffset=20

        Returns:
            The headline of the annotation
        """
        return self.label

    def setLabel(self, value: Optional[MultilanguageLongName]) -> "GeneralAnnotation":
        """
        This is the headline for the annotation. Tags: xml.sequenceOffset=20

        A None value is a no-op and does not overwrite an existing label.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.label = value
        return self


class Annotation(GeneralAnnotation):
    """
    This is a plain annotation which does not have further formal data.
    """

    # Annotation method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.72, p.163
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no own attributes)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        super().__init__()
