"""
AUTOSAR Package - GeneralAnnotation

Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::GeneralAnnotation
"""


from __future__ import annotations
from abc import ABC
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from armodel.v2.models.M2.MSR.Documentation.BlockElements import (
        DocumentationBlock,
    )
    from armodel.v2.models.M2.MSR.Documentation.TextModel.MultilanguageData import (
        MultilanguageLongName,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class GeneralAnnotation(ARObject, ABC):
    """
    This class represents textual comments (called annotations) which relate to
    the object in which it is aggregated. These annotations are intended for use
    during the development process for transferring information from one step of
    the development process to the next one. The approach is similar to the
    "yellow pads" ... This abstract class can be specialized in order to add
    some further formal properties. (cid:53) 162 of 1228 Document ID 62:
    AUTOSAR_CP_TPS_SoftwareComponentTemplate Software Component Template AUTOSAR
    CP R23-11 (cid:52)

    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::GeneralAnnotation::GeneralAnnotation

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 162, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 163, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is GeneralAnnotation:
            raise TypeError("GeneralAnnotation is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute identifies the origin of the annotation.
        # It is an string since it can be an individual’s name as well name of a tool
                # or even the name of a process step.
        self._annotation: String = None

    @property
    def annotation(self) -> String:
        """Get annotation (Pythonic accessor)."""
        return self._annotation

    @annotation.setter
    def annotation(self, value: String) -> None:
        """
        Set annotation with validation.

        Args:
            value: The annotation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (String, str)):
            raise TypeError(
                f"annotation must be String or str, got {type(value).__name__}"
            )
        self._annotation = value
        self._annotationText: Optional[DocumentationBlock] = None

    @property
    def annotation_text(self) -> Optional[DocumentationBlock]:
        """Get annotationText (Pythonic accessor)."""
        return self._annotationText

    @annotation_text.setter
    def annotation_text(self, value: Optional[DocumentationBlock]) -> None:
        """
        Set annotationText with validation.

        Args:
            value: The annotationText to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._annotationText = None
            return

        if not isinstance(value, DocumentationBlock):
            raise TypeError(
                f"annotationText must be DocumentationBlock or None, got {type(value).__name__}"
            )
        self._annotationText = value
        # xml.
        # sequenceOffset=20.
        self._label: Optional[MultilanguageLongName] = None

    @property
    def label(self) -> Optional[MultilanguageLongName]:
        """Get label (Pythonic accessor)."""
        return self._label

    @label.setter
    def label(self, value: Optional[MultilanguageLongName]) -> None:
        """
        Set label with validation.

        Args:
            value: The label to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._label = None
            return

        if not isinstance(value, MultilanguageLongName):
            raise TypeError(
                f"label must be MultilanguageLongName or None, got {type(value).__name__}"
            )
        self._label = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAnnotation(self) -> String:
        """
        AUTOSAR-compliant getter for annotation.

        Returns:
            The annotation value

        Note:
            Delegates to annotation property (CODING_RULE_V2_00017)
        """
        return self.annotation  # Delegates to property

    def setAnnotation(self, value: String) -> GeneralAnnotation:
        """
        AUTOSAR-compliant setter for annotation with method chaining.

        Args:
            value: The annotation to set

        Returns:
            self for method chaining

        Note:
            Delegates to annotation property setter (gets validation automatically)
        """
        self.annotation = value  # Delegates to property setter
        return self

    def getAnnotationText(self) -> DocumentationBlock:
        """
        AUTOSAR-compliant getter for annotationText.

        Returns:
            The annotationText value

        Note:
            Delegates to annotation_text property (CODING_RULE_V2_00017)
        """
        return self.annotation_text  # Delegates to property

    def setAnnotationText(self, value: DocumentationBlock) -> GeneralAnnotation:
        """
        AUTOSAR-compliant setter for annotationText with method chaining.

        Args:
            value: The annotationText to set

        Returns:
            self for method chaining

        Note:
            Delegates to annotation_text property setter (gets validation automatically)
        """
        self.annotation_text = value  # Delegates to property setter
        return self

    def getLabel(self) -> "MultilanguageLong":
        """
        AUTOSAR-compliant getter for label.

        Returns:
            The label value

        Note:
            Delegates to label property (CODING_RULE_V2_00017)
        """
        return self.label  # Delegates to property

    def setLabel(self, value: "MultilanguageLong") -> GeneralAnnotation:
        """
        AUTOSAR-compliant setter for label with method chaining.

        Args:
            value: The label to set

        Returns:
            self for method chaining

        Note:
            Delegates to label property setter (gets validation automatically)
        """
        self.label = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_annotation(self, value: String) -> GeneralAnnotation:
        """
        Set annotation and return self for chaining.

        Args:
            value: The annotation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_annotation("value")
        """
        self.annotation = value  # Use property setter (gets validation)
        return self

    def with_annotation_text(self, value: DocumentationBlock) -> GeneralAnnotation:
        """
        Set annotationText and return self for chaining.

        Args:
            value: The annotationText to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_annotation_text("value")
        """
        self.annotation_text = value  # Use property setter (gets validation)
        return self

    def with_label(self, value: Optional["MultilanguageLong"]) -> GeneralAnnotation:
        """
        Set label and return self for chaining.

        Args:
            value: The label to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_label("value")
        """
        self.label = value  # Use property setter (gets validation)
        return self
