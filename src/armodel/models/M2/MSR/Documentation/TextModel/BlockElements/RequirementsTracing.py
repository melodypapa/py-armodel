from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from abc import ABC
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, String

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock


class Traceable(Identifiable, ABC):
    """
    This meta class represents the ability to be subject to tracing within an AUTOSAR model. Note that it is expected that its subclasses inherit either from MultilanguageReferrable or from Identifiable. Nevertheless it also inherits from MultilanguageReferrable in order to provide a common reference target for all Traceables.
    """

    # Traceable method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.29, p.313
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__         [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getTraceRefs     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] addTraceRef      [x] impl  [x] docstring  [x] test  [x] reader  [x] writer

    def __init__(self, parent, short_name: str):
        if type(self) is Traceable:
            raise TypeError("Traceable is an abstract class.")
        super().__init__(parent, short_name)

        # This association represents the ability to trace to upstream requirements / constraints.
        self.traceRefs: List[RefType] = []

    def getTraceRefs(self) -> List[RefType]:
        """
        This association represents the ability to trace to upstream requirements / constraints.

        Returns:
            The upstream requirements / constraints references
        """
        return self.traceRefs

    def addTraceRef(self, value: Optional[RefType]) -> "Traceable":
        """
        This association represents the ability to trace to upstream requirements / constraints. A None value is a no-op and is not appended.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.traceRefs.append(value)
        return self


class TraceableText(ARObject):
    """
    This meta-class represents the ability to denote a traceable text item such as requirements etc. The following approach applies: shortName represents the tag for tracing, longName represents the head line, category represents the kind of the tagged text.
    """

    # TraceableText method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.30, p.313
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getText          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setText          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTraceRefs     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addTraceRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This represents the text to which the tag applies.
        self.text: Optional["DocumentationBlock"] = None

        # This association represents the ability to trace to upstream requirements / constraints.
        self.traceRefs: List[RefType] = []

    def getText(self) -> Optional["DocumentationBlock"]:
        """
        This represents the text to which the tag applies.

        Returns:
            The text to which the tag applies
        """
        return self.text

    def setText(self, value: Optional["DocumentationBlock"]) -> "TraceableText":
        """
        This represents the text to which the tag applies. A None value is a no-op and does not overwrite an existing text.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.text = value
        return self

    def getTraceRefs(self) -> List[RefType]:
        """
        This association represents the ability to trace to upstream requirements / constraints.

        Returns:
            The upstream requirements / constraints references
        """
        return self.traceRefs

    def addTraceRef(self, value: Optional[RefType]) -> "TraceableText":
        """
        This association represents the ability to trace to upstream requirements / constraints. A None value is a no-op and is not appended.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.traceRefs.append(value)
        return self


class StructuredReq(ARObject):
    """
    This represents a structured requirement. This is intended for a case where specific requirements for features are collected. Note that this can be rendered as a labeled list.
    """

    # StructuredReq method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.31, p.314
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDate                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDate                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getImportance          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setImportance          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getIssuedBy            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setIssuedBy            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getType                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setType                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDescription         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDescription         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRationale           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRationale           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDependencies        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDependencies        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getUseCase             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setUseCase             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getConflicts           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setConflicts           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSupportingMaterial  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSupportingMaterial  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRemark              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRemark              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTestedItemRefs      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addTestedItemRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This represents the date when the requirement was initiated.
        self.date: Optional[String] = None

        # This allows to represent the importance of the requirement.
        self.importance: Optional[String] = None

        # This represents the person, organization or authority which issued the requirement.
        self.issuedBy: Optional[String] = None

        # This attribute allows to denote the type of requirement to denote for example is it an "enhancement", "new feature" etc.
        self.type: Optional[String] = None

        # This represents the general description of the requirement.
        self.description: Optional["DocumentationBlock"] = None

        # This represents the rationale of the requirement.
        self.rationale: Optional["DocumentationBlock"] = None

        # This represents an informal specification of dependencies.
        self.dependencies: Optional["DocumentationBlock"] = None

        # This describes the relevant use cases.
        self.useCase: Optional["DocumentationBlock"] = None

        # This represents an informal specification of conflicts.
        self.conflicts: Optional["DocumentationBlock"] = None

        # This represents an informal specification of the supporting material.
        self.supportingMaterial: Optional["DocumentationBlock"] = None

        # This represents an informal remark.
        self.remark: Optional["DocumentationBlock"] = None

        # This association represents the ability to trace on the same specification level.
        self.testedItemRefs: List[RefType] = []

    def getDate(self) -> Optional[String]:
        """
        This represents the date when the requirement was initiated.

        Returns:
            The date when the requirement was initiated
        """
        return self.date

    def setDate(self, value: Optional[String]) -> "StructuredReq":
        """
        This represents the date when the requirement was initiated. A None value is a no-op and does not overwrite an existing date.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.date = value
        return self

    def getImportance(self) -> Optional[String]:
        """
        This allows to represent the importance of the requirement.

        Returns:
            The importance of the requirement
        """
        return self.importance

    def setImportance(self, value: Optional[String]) -> "StructuredReq":
        """
        This allows to represent the importance of the requirement. A None value is a no-op and does not overwrite an existing importance.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.importance = value
        return self

    def getIssuedBy(self) -> Optional[String]:
        """
        This represents the person, organization or authority which issued the requirement.

        Returns:
            The person, organization or authority which issued the requirement
        """
        return self.issuedBy

    def setIssuedBy(self, value: Optional[String]) -> "StructuredReq":
        """
        This represents the person, organization or authority which issued the requirement. A None value is a no-op and does not overwrite an existing issuedBy.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.issuedBy = value
        return self

    def getType(self) -> Optional[String]:
        """
        This attribute allows to denote the type of requirement to denote for example is it an "enhancement", "new feature" etc.

        Returns:
            The type of requirement
        """
        return self.type

    def setType(self, value: Optional[String]) -> "StructuredReq":
        """
        This attribute allows to denote the type of requirement to denote for example is it an "enhancement", "new feature" etc. A None value is a no-op and does not overwrite an existing type.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.type = value
        return self

    def getDescription(self) -> Optional["DocumentationBlock"]:
        """
        This represents the general description of the requirement.

        Returns:
            The general description of the requirement
        """
        return self.description

    def setDescription(self, value: Optional["DocumentationBlock"]) -> "StructuredReq":
        """
        This represents the general description of the requirement. A None value is a no-op and does not overwrite an existing description.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.description = value
        return self

    def getRationale(self) -> Optional["DocumentationBlock"]:
        """
        This represents the rationale of the requirement.

        Returns:
            The rationale of the requirement
        """
        return self.rationale

    def setRationale(self, value: Optional["DocumentationBlock"]) -> "StructuredReq":
        """
        This represents the rationale of the requirement. A None value is a no-op and does not overwrite an existing rationale.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.rationale = value
        return self

    def getDependencies(self) -> Optional["DocumentationBlock"]:
        """
        This represents an informal specification of dependencies.

        Returns:
            The informal specification of dependencies
        """
        return self.dependencies

    def setDependencies(self, value: Optional["DocumentationBlock"]) -> "StructuredReq":
        """
        This represents an informal specification of dependencies. A None value is a no-op and does not overwrite an existing dependencies.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.dependencies = value
        return self

    def getUseCase(self) -> Optional["DocumentationBlock"]:
        """
        This describes the relevant use cases.

        Returns:
            The relevant use cases
        """
        return self.useCase

    def setUseCase(self, value: Optional["DocumentationBlock"]) -> "StructuredReq":
        """
        This describes the relevant use cases. A None value is a no-op and does not overwrite an existing useCase.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.useCase = value
        return self

    def getConflicts(self) -> Optional["DocumentationBlock"]:
        """
        This represents an informal specification of conflicts.

        Returns:
            The informal specification of conflicts
        """
        return self.conflicts

    def setConflicts(self, value: Optional["DocumentationBlock"]) -> "StructuredReq":
        """
        This represents an informal specification of conflicts. A None value is a no-op and does not overwrite an existing conflicts.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.conflicts = value
        return self

    def getSupportingMaterial(self) -> Optional["DocumentationBlock"]:
        """
        This represents an informal specification of the supporting material.

        Returns:
            The informal specification of the supporting material
        """
        return self.supportingMaterial

    def setSupportingMaterial(self, value: Optional["DocumentationBlock"]) -> "StructuredReq":
        """
        This represents an informal specification of the supporting material. A None value is a no-op and does not overwrite an existing supportingMaterial.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.supportingMaterial = value
        return self

    def getRemark(self) -> Optional["DocumentationBlock"]:
        """
        This represents an informal remark.

        Returns:
            The informal remark
        """
        return self.remark

    def setRemark(self, value: Optional["DocumentationBlock"]) -> "StructuredReq":
        """
        This represents an informal remark. A None value is a no-op and does not overwrite an existing remark.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.remark = value
        return self

    def getTestedItemRefs(self) -> List[RefType]:
        """
        This association represents the ability to trace on the same specification level.

        Returns:
            The references on the same specification level
        """
        return self.testedItemRefs

    def addTestedItemRef(self, value: Optional[RefType]) -> "StructuredReq":
        """
        This association represents the ability to trace on the same specification level. A None value is a no-op and is not appended.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.testedItemRefs.append(value)
        return self
