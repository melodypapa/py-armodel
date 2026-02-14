"""
AUTOSAR Package - RequirementsTracing

Package: M2::MSR::Documentation::BlockElements::RequirementsTracing
"""


from __future__ import annotations

from abc import ABC
from typing import TYPE_CHECKING, List, Optional

if TYPE_CHECKING:
    from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Referrable import (
        MultilanguageReferrable,
    )
    from armodel.v2.models.M2.MSR.Documentation.BlockElements import (
        DocumentationBlock,
    )
else:
    # Import at runtime for class inheritance
    from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Referrable import (
        MultilanguageReferrable,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.v2.models.M2.MSR.Documentation.BlockElements.PaginationAndView import (
    DateTime,
    Paginateable,
)


class StructuredReq(Paginateable):
    """
    that this can be rendered as a labeled list.

    Package: M2::MSR::Documentation::BlockElements::RequirementsTracing::StructuredReq

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 168, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 49, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 313, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 208, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represents the platform the requirement is 719 Document ID
        # 673: AUTOSAR_CP_TPS_DiagnosticExtractTemplate Template R23-11.
        self._appliesTo: List["StandardNameEnum"] = []

    @property
    def applies_to(self) -> List["StandardNameEnum"]:
        """Get appliesTo (Pythonic accessor)."""
        return self._appliesTo
        # This represents an informal specification of conflicts.
        self._conflicts: Optional[DocumentationBlock] = None

    @property
    def conflicts(self) -> Optional[DocumentationBlock]:
        """Get conflicts (Pythonic accessor)."""
        return self._conflicts

    @conflicts.setter
    def conflicts(self, value: Optional[DocumentationBlock]) -> None:
        """
        Set conflicts with validation.

        Args:
            value: The conflicts to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._conflicts = None
            return

        if not isinstance(value, DocumentationBlock):
            raise TypeError(
                f"conflicts must be DocumentationBlock or None, got {type(value).__name__}"
            )
        self._conflicts = value
        self._date: DateTime = None

    @property
    def date(self) -> DateTime:
        """Get date (Pythonic accessor)."""
        return self._date

    @date.setter
    def date(self, value: DateTime) -> None:
        """
        Set date with validation.

        Args:
            value: The date to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, DateTime):
            raise TypeError(
                f"date must be DateTime, got {type(value).__name__}"
            )
        self._date = value
        # the property trace provided by the.
        self._dependencies: Optional[DocumentationBlock] = None

    @property
    def dependencies(self) -> Optional[DocumentationBlock]:
        """Get dependencies (Pythonic accessor)."""
        return self._dependencies

    @dependencies.setter
    def dependencies(self, value: Optional[DocumentationBlock]) -> None:
        """
        Set dependencies with validation.

        Args:
            value: The dependencies to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dependencies = None
            return

        if not isinstance(value, DocumentationBlock):
            raise TypeError(
                f"dependencies must be DocumentationBlock or None, got {type(value).__name__}"
            )
        self._dependencies = value
        self._description: Optional[DocumentationBlock] = None

    @property
    def description(self) -> Optional[DocumentationBlock]:
        """Get description (Pythonic accessor)."""
        return self._description

    @description.setter
    def description(self, value: Optional[DocumentationBlock]) -> None:
        """
        Set description with validation.

        Args:
            value: The description to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._description = None
            return

        if not isinstance(value, DocumentationBlock):
            raise TypeError(
                f"description must be DocumentationBlock or None, got {type(value).__name__}"
            )
        self._description = value
        self._importance: String = None

    @property
    def importance(self) -> String:
        """Get importance (Pythonic accessor)."""
        return self._importance

    @importance.setter
    def importance(self, value: String) -> None:
        """
        Set importance with validation.

        Args:
            value: The importance to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (String, str)):
            raise TypeError(
                f"importance must be String or str, got {type(value).__name__}"
            )
        self._importance = value
        self._issuedBy: String = None

    @property
    def issued_by(self) -> String:
        """Get issuedBy (Pythonic accessor)."""
        return self._issuedBy

    @issued_by.setter
    def issued_by(self, value: String) -> None:
        """
        Set issuedBy with validation.

        Args:
            value: The issuedBy to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (String, str)):
            raise TypeError(
                f"issuedBy must be String or str, got {type(value).__name__}"
            )
        self._issuedBy = value
        self._rationale: Optional[DocumentationBlock] = None

    @property
    def rationale(self) -> Optional[DocumentationBlock]:
        """Get rationale (Pythonic accessor)."""
        return self._rationale

    @rationale.setter
    def rationale(self, value: Optional[DocumentationBlock]) -> None:
        """
        Set rationale with validation.

        Args:
            value: The rationale to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rationale = None
            return

        if not isinstance(value, DocumentationBlock):
            raise TypeError(
                f"rationale must be DocumentationBlock or None, got {type(value).__name__}"
            )
        self._rationale = value
        # Note that this is not annotation, since these remark is still of the
                # requirement.
        self._remark: Optional[DocumentationBlock] = None

    @property
    def remark(self) -> Optional[DocumentationBlock]:
        """Get remark (Pythonic accessor)."""
        return self._remark

    @remark.setter
    def remark(self, value: Optional[DocumentationBlock]) -> None:
        """
        Set remark with validation.

        Args:
            value: The remark to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._remark = None
            return

        if not isinstance(value, DocumentationBlock):
            raise TypeError(
                f"remark must be DocumentationBlock or None, got {type(value).__name__}"
            )
        self._remark = value
        self._supporting: Optional[DocumentationBlock] = None

    @property
    def supporting(self) -> Optional[DocumentationBlock]:
        """Get supporting (Pythonic accessor)."""
        return self._supporting

    @supporting.setter
    def supporting(self, value: Optional[DocumentationBlock]) -> None:
        """
        Set supporting with validation.

        Args:
            value: The supporting to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._supporting = None
            return

        if not isinstance(value, DocumentationBlock):
            raise TypeError(
                f"supporting must be DocumentationBlock or None, got {type(value).__name__}"
            )
        self._supporting = value
        # This supports for example the of.
        self._testedItem: List[Traceable] = []

    @property
    def tested_item(self) -> List[Traceable]:
        """Get testedItem (Pythonic accessor)."""
        return self._testedItem
        # This attribute allows to denote the type of requirement to example is it an
        # "enhancement", "new feature".
        self._type: String = None

    @property
    def type(self) -> String:
        """Get type (Pythonic accessor)."""
        return self._type

    @type.setter
    def type(self, value: String) -> None:
        """
        Set type with validation.

        Args:
            value: The type to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (String, str)):
            raise TypeError(
                f"type must be String or str, got {type(value).__name__}"
            )
        self._type = value
        # Note that formal use cases should be done in the trace.
        self._useCase: Optional[DocumentationBlock] = None

    @property
    def use_case(self) -> Optional[DocumentationBlock]:
        """Get useCase (Pythonic accessor)."""
        return self._useCase

    @use_case.setter
    def use_case(self, value: Optional[DocumentationBlock]) -> None:
        """
        Set useCase with validation.

        Args:
            value: The useCase to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._useCase = None
            return

        if not isinstance(value, DocumentationBlock):
            raise TypeError(
                f"useCase must be DocumentationBlock or None, got {type(value).__name__}"
            )
        self._useCase = value

    def with_applies_to(self, value):
        """
        Set applies_to and return self for chaining.

        Args:
            value: The applies_to to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_applies_to("value")
        """
        self.applies_to = value  # Use property setter (gets validation)
        return self

    def with_tested_item(self, value):
        """
        Set tested_item and return self for chaining.

        Args:
            value: The tested_item to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tested_item("value")
        """
        self.tested_item = value  # Use property setter (gets validation)
        return self

    def with_trace(self, value):
        """
        Set trace and return self for chaining.

        Args:
            value: The trace to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_trace("value")
        """
        self.trace = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAppliesTo(self) -> List["StandardNameEnum"]:
        """
        AUTOSAR-compliant getter for appliesTo.

        Returns:
            The appliesTo value

        Note:
            Delegates to applies_to property (CODING_RULE_V2_00017)
        """
        return self.applies_to  # Delegates to property

    def getConflicts(self) -> DocumentationBlock:
        """
        AUTOSAR-compliant getter for conflicts.

        Returns:
            The conflicts value

        Note:
            Delegates to conflicts property (CODING_RULE_V2_00017)
        """
        return self.conflicts  # Delegates to property

    def setConflicts(self, value: DocumentationBlock) -> StructuredReq:
        """
        AUTOSAR-compliant setter for conflicts with method chaining.

        Args:
            value: The conflicts to set

        Returns:
            self for method chaining

        Note:
            Delegates to conflicts property setter (gets validation automatically)
        """
        self.conflicts = value  # Delegates to property setter
        return self

    def getDate(self) -> DateTime:
        """
        AUTOSAR-compliant getter for date.

        Returns:
            The date value

        Note:
            Delegates to date property (CODING_RULE_V2_00017)
        """
        return self.date  # Delegates to property

    def setDate(self, value: DateTime) -> StructuredReq:
        """
        AUTOSAR-compliant setter for date with method chaining.

        Args:
            value: The date to set

        Returns:
            self for method chaining

        Note:
            Delegates to date property setter (gets validation automatically)
        """
        self.date = value  # Delegates to property setter
        return self

    def getDependencies(self) -> DocumentationBlock:
        """
        AUTOSAR-compliant getter for dependencies.

        Returns:
            The dependencies value

        Note:
            Delegates to dependencies property (CODING_RULE_V2_00017)
        """
        return self.dependencies  # Delegates to property

    def setDependencies(self, value: DocumentationBlock) -> StructuredReq:
        """
        AUTOSAR-compliant setter for dependencies with method chaining.

        Args:
            value: The dependencies to set

        Returns:
            self for method chaining

        Note:
            Delegates to dependencies property setter (gets validation automatically)
        """
        self.dependencies = value  # Delegates to property setter
        return self

    def getDescription(self) -> DocumentationBlock:
        """
        AUTOSAR-compliant getter for description.

        Returns:
            The description value

        Note:
            Delegates to description property (CODING_RULE_V2_00017)
        """
        return self.description  # Delegates to property

    def setDescription(self, value: DocumentationBlock) -> StructuredReq:
        """
        AUTOSAR-compliant setter for description with method chaining.

        Args:
            value: The description to set

        Returns:
            self for method chaining

        Note:
            Delegates to description property setter (gets validation automatically)
        """
        self.description = value  # Delegates to property setter
        return self

    def getImportance(self) -> String:
        """
        AUTOSAR-compliant getter for importance.

        Returns:
            The importance value

        Note:
            Delegates to importance property (CODING_RULE_V2_00017)
        """
        return self.importance  # Delegates to property

    def setImportance(self, value: String) -> StructuredReq:
        """
        AUTOSAR-compliant setter for importance with method chaining.

        Args:
            value: The importance to set

        Returns:
            self for method chaining

        Note:
            Delegates to importance property setter (gets validation automatically)
        """
        self.importance = value  # Delegates to property setter
        return self

    def getIssuedBy(self) -> String:
        """
        AUTOSAR-compliant getter for issuedBy.

        Returns:
            The issuedBy value

        Note:
            Delegates to issued_by property (CODING_RULE_V2_00017)
        """
        return self.issued_by  # Delegates to property

    def setIssuedBy(self, value: String) -> StructuredReq:
        """
        AUTOSAR-compliant setter for issuedBy with method chaining.

        Args:
            value: The issuedBy to set

        Returns:
            self for method chaining

        Note:
            Delegates to issued_by property setter (gets validation automatically)
        """
        self.issued_by = value  # Delegates to property setter
        return self

    def getRationale(self) -> DocumentationBlock:
        """
        AUTOSAR-compliant getter for rationale.

        Returns:
            The rationale value

        Note:
            Delegates to rationale property (CODING_RULE_V2_00017)
        """
        return self.rationale  # Delegates to property

    def setRationale(self, value: DocumentationBlock) -> StructuredReq:
        """
        AUTOSAR-compliant setter for rationale with method chaining.

        Args:
            value: The rationale to set

        Returns:
            self for method chaining

        Note:
            Delegates to rationale property setter (gets validation automatically)
        """
        self.rationale = value  # Delegates to property setter
        return self

    def getRemark(self) -> DocumentationBlock:
        """
        AUTOSAR-compliant getter for remark.

        Returns:
            The remark value

        Note:
            Delegates to remark property (CODING_RULE_V2_00017)
        """
        return self.remark  # Delegates to property

    def setRemark(self, value: DocumentationBlock) -> StructuredReq:
        """
        AUTOSAR-compliant setter for remark with method chaining.

        Args:
            value: The remark to set

        Returns:
            self for method chaining

        Note:
            Delegates to remark property setter (gets validation automatically)
        """
        self.remark = value  # Delegates to property setter
        return self

    def getSupporting(self) -> DocumentationBlock:
        """
        AUTOSAR-compliant getter for supporting.

        Returns:
            The supporting value

        Note:
            Delegates to supporting property (CODING_RULE_V2_00017)
        """
        return self.supporting  # Delegates to property

    def setSupporting(self, value: DocumentationBlock) -> StructuredReq:
        """
        AUTOSAR-compliant setter for supporting with method chaining.

        Args:
            value: The supporting to set

        Returns:
            self for method chaining

        Note:
            Delegates to supporting property setter (gets validation automatically)
        """
        self.supporting = value  # Delegates to property setter
        return self

    def getTestedItem(self) -> List[Traceable]:
        """
        AUTOSAR-compliant getter for testedItem.

        Returns:
            The testedItem value

        Note:
            Delegates to tested_item property (CODING_RULE_V2_00017)
        """
        return self.tested_item  # Delegates to property

    def getType(self) -> String:
        """
        AUTOSAR-compliant getter for type.

        Returns:
            The type value

        Note:
            Delegates to type property (CODING_RULE_V2_00017)
        """
        return self.type  # Delegates to property

    def setType(self, value: String) -> StructuredReq:
        """
        AUTOSAR-compliant setter for type with method chaining.

        Args:
            value: The type to set

        Returns:
            self for method chaining

        Note:
            Delegates to type property setter (gets validation automatically)
        """
        self.type = value  # Delegates to property setter
        return self

    def getUseCase(self) -> DocumentationBlock:
        """
        AUTOSAR-compliant getter for useCase.

        Returns:
            The useCase value

        Note:
            Delegates to use_case property (CODING_RULE_V2_00017)
        """
        return self.use_case  # Delegates to property

    def setUseCase(self, value: DocumentationBlock) -> StructuredReq:
        """
        AUTOSAR-compliant setter for useCase with method chaining.

        Args:
            value: The useCase to set

        Returns:
            self for method chaining

        Note:
            Delegates to use_case property setter (gets validation automatically)
        """
        self.use_case = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_conflicts(self, value: Optional[DocumentationBlock]) -> StructuredReq:
        """
        Set conflicts and return self for chaining.

        Args:
            value: The conflicts to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_conflicts("value")
        """
        self.conflicts = value  # Use property setter (gets validation)
        return self

    def with_date(self, value: DateTime) -> StructuredReq:
        """
        Set date and return self for chaining.

        Args:
            value: The date to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_date("value")
        """
        self.date = value  # Use property setter (gets validation)
        return self

    def with_dependencies(self, value: Optional[DocumentationBlock]) -> StructuredReq:
        """
        Set dependencies and return self for chaining.

        Args:
            value: The dependencies to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dependencies("value")
        """
        self.dependencies = value  # Use property setter (gets validation)
        return self

    def with_description(self, value: Optional[DocumentationBlock]) -> StructuredReq:
        """
        Set description and return self for chaining.

        Args:
            value: The description to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_description("value")
        """
        self.description = value  # Use property setter (gets validation)
        return self

    def with_importance(self, value: String) -> StructuredReq:
        """
        Set importance and return self for chaining.

        Args:
            value: The importance to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_importance("value")
        """
        self.importance = value  # Use property setter (gets validation)
        return self

    def with_issued_by(self, value: String) -> StructuredReq:
        """
        Set issuedBy and return self for chaining.

        Args:
            value: The issuedBy to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_issued_by("value")
        """
        self.issued_by = value  # Use property setter (gets validation)
        return self

    def with_rationale(self, value: Optional[DocumentationBlock]) -> StructuredReq:
        """
        Set rationale and return self for chaining.

        Args:
            value: The rationale to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rationale("value")
        """
        self.rationale = value  # Use property setter (gets validation)
        return self

    def with_remark(self, value: Optional[DocumentationBlock]) -> StructuredReq:
        """
        Set remark and return self for chaining.

        Args:
            value: The remark to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_remark("value")
        """
        self.remark = value  # Use property setter (gets validation)
        return self

    def with_supporting(self, value: Optional[DocumentationBlock]) -> StructuredReq:
        """
        Set supporting and return self for chaining.

        Args:
            value: The supporting to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_supporting("value")
        """
        self.supporting = value  # Use property setter (gets validation)
        return self

    def with_type(self, value: String) -> StructuredReq:
        """
        Set type and return self for chaining.

        Args:
            value: The type to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_type("value")
        """
        self.type = value  # Use property setter (gets validation)
        return self

    def with_use_case(self, value: Optional[DocumentationBlock]) -> StructuredReq:
        """
        Set useCase and return self for chaining.

        Args:
            value: The useCase to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_use_case("value")
        """
        self.use_case = value  # Use property setter (gets validation)
        return self



class TraceableText(Paginateable):
    """
    This meta-class represents the ability to denote a traceable text item such
    as requirements etc. The following approach applies: • shortName represents
    the tag for tracing • longName represents the head line • category
    represents the kind of the tagged text (see [constr_2540])

    Package: M2::MSR::Documentation::BlockElements::RequirementsTracing::TraceableText

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 178, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 313, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 222, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the text to which the tag applies.
        self._text: DocumentationBlock = None

    @property
    def text(self) -> DocumentationBlock:
        """Get text (Pythonic accessor)."""
        return self._text

    @text.setter
    def text(self, value: DocumentationBlock) -> None:
        """
        Set text with validation.

        Args:
            value: The text to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, DocumentationBlock):
            raise TypeError(
                f"text must be DocumentationBlock, got {type(value).__name__}"
            )
        self._text = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getText(self) -> DocumentationBlock:
        """
        AUTOSAR-compliant getter for text.

        Returns:
            The text value

        Note:
            Delegates to text property (CODING_RULE_V2_00017)
        """
        return self.text  # Delegates to property

    def setText(self, value: DocumentationBlock) -> TraceableText:
        """
        AUTOSAR-compliant setter for text with method chaining.

        Args:
            value: The text to set

        Returns:
            self for method chaining

        Note:
            Delegates to text property setter (gets validation automatically)
        """
        self.text = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_text(self, value: DocumentationBlock) -> TraceableText:
        """
        Set text and return self for chaining.

        Args:
            value: The text to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_text("value")
        """
        self.text = value  # Use property setter (gets validation)
        return self



class Traceable(MultilanguageReferrable, ABC):
    """
    that it is expected that its subclasses inherit either from
    MultilanguageReferrable or from Identifiable. Nevertheless it also inherits
    from MultilanguageReferrable in order to provide a common reference target
    for all Traceables.

    Package: M2::MSR::Documentation::BlockElements::RequirementsTracing::Traceable

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 312, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 221, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is Traceable:
            raise TypeError("Traceable is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This association represents the ability to trace to / constraints.
        # This supports for bottom up tracing MainRequirements <- Features <- BSW/AI.
        self._trace: List[Traceable] = []

    @property
    def trace(self) -> List[Traceable]:
        """Get trace (Pythonic accessor)."""
        return self._trace

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTrace(self) -> List[Traceable]:
        """
        AUTOSAR-compliant getter for trace.

        Returns:
            The trace value

        Note:
            Delegates to trace property (CODING_RULE_V2_00017)
        """
        return self.trace  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
