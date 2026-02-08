from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class DiagnosticParameterElement(Identifiable):
    """
    This meta-class represents an element of a DiagnosticParameter if the
    DiagnosticParameter represents a structure.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::CommonDiagnostics

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 36, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute indicates that the enclosing Diagnostic an array and
        # configures size in terms of the number of elements of the.
        self._arraySize: Optional["PositiveInteger"] = None

    @property
    def array_size(self) -> Optional["PositiveInteger"]:
        """Get arraySize (Pythonic accessor)."""
        return self._arraySize

    @array_size.setter
    def array_size(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set arraySize with validation.

        Args:
            value: The arraySize to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._arraySize = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"arraySize must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._arraySize = value
        # This collection represents the sub-elements on the next level.
        self._subElement: List["DiagnosticParameter"] = []

    @property
    def sub_element(self) -> List["DiagnosticParameter"]:
        """Get subElement (Pythonic accessor)."""
        return self._subElement

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getArraySize(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for arraySize.

        Returns:
            The arraySize value

        Note:
            Delegates to array_size property (CODING_RULE_V2_00017)
        """
        return self.array_size  # Delegates to property

    def setArraySize(self, value: "PositiveInteger") -> "DiagnosticParameterElement":
        """
        AUTOSAR-compliant setter for arraySize with method chaining.

        Args:
            value: The arraySize to set

        Returns:
            self for method chaining

        Note:
            Delegates to array_size property setter (gets validation automatically)
        """
        self.array_size = value  # Delegates to property setter
        return self

    def getSubElement(self) -> List["DiagnosticParameter"]:
        """
        AUTOSAR-compliant getter for subElement.

        Returns:
            The subElement value

        Note:
            Delegates to sub_element property (CODING_RULE_V2_00017)
        """
        return self.sub_element  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_array_size(self, value: Optional["PositiveInteger"]) -> "DiagnosticParameterElement":
        """
        Set arraySize and return self for chaining.

        Args:
            value: The arraySize to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_array_size("value")
        """
        self.array_size = value  # Use property setter (gets validation)
        return self
